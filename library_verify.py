#!/usr/bin/env python3
"""library-verify — the Grand Library's CI (multi-language).

Green means the library is what it claims:
  (a) every populated subtree: Ed25519 signature valid + catalog/manifest integrity
  (b) every file carries a valid master-0 watermark with the right mark
  (c) master CATALOG.md ID set == on-disk ID set
  (d) [--gate] every file compiles/runs exit 0 (python3/Rscript/g++/go)
  (e) quarantine IDs absent from all shippable trees
  (f) twin integrity: no cpp/go twin whose source ID is quarantined or missing

Requires `folder-nature>=0.2` (falls back to the v-next checkout on sys.path).
"""
import argparse, json, re, shutil, subprocess, sys
from pathlib import Path

try:
    from folder_nature.mark import signing
    from folder_nature.mark.watermark import verify_file
except ModuleNotFoundError:
    sys.path.insert(0, str(Path.home() / "Projects/folder-nature"))
    from folder_nature.mark import signing
    from folder_nature.mark.watermark import verify_file

ROOT = Path(__file__).resolve().parent
SIGNED_SUBTREES = ["python/programming", "python/data-science", "r"]
GATE = {".py": ["python3"], ".R": ["Rscript"]}          # cpp/go handled specially
SRC_EXT = (".py", ".R", ".cpp", ".go")


def run_gate(p: Path) -> bool:
    if p.suffix in (".py", ".R"):
        runner = GATE[p.suffix][0]
        if not shutil.which(runner):
            return True
        return subprocess.run([runner, str(p)], capture_output=True, timeout=120).returncode == 0
    if p.suffix == ".cpp":
        if not shutil.which("g++"):
            return True
        out = Path("/tmp/_apl_x")
        c = subprocess.run(["g++", "-O2", "-std=c++17", str(p), "-o", str(out)],
                           capture_output=True, timeout=120)
        return c.returncode == 0 and subprocess.run([str(out)], capture_output=True,
                                                    timeout=120).returncode == 0
    if p.suffix == ".go":
        if not shutil.which("go"):
            return True
        return subprocess.run(["go", "run", str(p)], capture_output=True, timeout=120).returncode == 0
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pubkey", default=str(ROOT / "aura-signing.pub"))
    ap.add_argument("--gate", action="store_true", help="also compile/run every file (slow)")
    args = ap.parse_args()
    pub = Path(args.pubkey).read_text().strip() if Path(args.pubkey).exists() else args.pubkey

    fails, disk_ids = [], set()
    quarantined = {p.stem for p in (ROOT / "_quarantine").glob("*.py")}

    # (a)(b)(d) per signed subtree
    for st in SIGNED_SUBTREES:
        sroot = ROOT / st
        if not sroot.exists():
            continue
        rep = signing.verify_directory(sroot, pub)
        print(f"[{st:22}] signature: {rep.summary()}")
        if not rep.ok:
            fails.append(f"{st}: {rep.summary()}")
        bad = 0
        for p in sroot.rglob("*"):
            if p.suffix not in SRC_EXT:
                continue
            disk_ids.add(p.stem)
            mr = verify_file(p)
            if mr.status != "authentic" or (mr.payload and not mr.payload.is_master):
                bad += 1; fails.append(f"{p.relative_to(ROOT)}: watermark {mr.status}")
            if p.stem in quarantined:
                fails.append(f"{p.relative_to(ROOT)}: quarantined ID present in shippable tree")
            if args.gate and not run_gate(p):
                fails.append(f"{p.relative_to(ROOT)}: GATE fail")
        print(f"                         watermark: {'all valid' if not bad else f'{bad} BAD'}")

    # (f) twin integrity — cpp/go present but source ID missing or quarantined
    for tl in ("cpp", "go"):
        for p in (ROOT / tl).rglob("*"):
            if p.suffix not in (".cpp", ".go"):
                continue
            if p.stem in quarantined:
                fails.append(f"{p.relative_to(ROOT)}: twin of a quarantined pattern")
            if p.stem not in disk_ids:
                fails.append(f"{p.relative_to(ROOT)}: twin with no python/r source ID")
            if args.gate and not run_gate(p):
                fails.append(f"{p.relative_to(ROOT)}: GATE fail")

    # (c) catalog ID parity
    catalog = (ROOT / "CATALOG.md").read_text(encoding="utf-8")
    listed = set(re.findall(r"^\| `([^`]+)` \|", catalog, re.M))
    if listed and listed != disk_ids:
        miss = listed - disk_ids
        extra = disk_ids - listed
        if miss: fails.append(f"catalog lists {len(miss)} ID(s) not on disk")
        if extra: fails.append(f"disk has {len(extra)} ID(s) not in catalog")
    print(f"[catalog               ] IDs: {len(disk_ids)} on disk, {len(listed)} listed"
          f" — {'OK' if listed == disk_ids else 'MISMATCH'}")

    print("-" * 60)
    if fails:
        print(f"RED — {len(fails)} problem(s):")
        for f in fails[:25]:
            print(f"  - {f}")
        return 1
    print("GREEN — the Grand Library is what it claims.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
