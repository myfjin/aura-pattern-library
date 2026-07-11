#!/usr/bin/env python3
"""library-verify — the Grand Library's CI (multi-language).

Green means the library is what it claims:
  (a) every populated subtree: Ed25519 signature valid + catalog/manifest integrity
  (b) every file carries a valid master-0 watermark with the right mark
  (c) master CATALOG.md ID set == on-disk ID set
  (d) [--gate] every file compiles/runs exit 0 (python3/Rscript/g++/go/rustc);
      a missing toolchain is a LOUD per-language SKIP that turns the run RED —
      a skipped language is never counted as validated
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
SIGNED_SUBTREES = ["python/programming", "python/data-science", "python/system-administration", "r", "cpp", "rust", "go"]
GATE = {".py": ["python3"], ".R": ["Rscript"]}          # cpp/go/rust handled specially
SRC_EXT = (".py", ".R", ".cpp", ".go", ".rs")


def run_gate(p: Path) -> str:
    """Gate one file. Returns 'ok' | 'fail' | 'skip:<toolchain>'.

    A missing toolchain is NEVER a pass — the caller records the skip and the
    run goes RED, so an ungated language can't hide behind a green."""
    if p.suffix in (".py", ".R"):
        runner = GATE[p.suffix][0]
        if not shutil.which(runner):
            return f"skip:{runner}"
        ok = subprocess.run([runner, str(p)], capture_output=True, timeout=120).returncode == 0
        return "ok" if ok else "fail"
    if p.suffix == ".cpp":
        if not shutil.which("g++"):
            return "skip:g++"
        out = Path("/tmp/_apl_x")
        c = subprocess.run(["g++", "-O2", "-std=c++17", str(p), "-o", str(out)],
                           capture_output=True, timeout=120)
        ok = c.returncode == 0 and subprocess.run([str(out)], capture_output=True,
                                                  timeout=120).returncode == 0
        return "ok" if ok else "fail"
    if p.suffix == ".go":
        if not shutil.which("go"):
            return "skip:go"
        ok = subprocess.run(["go", "run", str(p)], capture_output=True, timeout=120).returncode == 0
        return "ok" if ok else "fail"
    if p.suffix == ".rs":
        if not shutil.which("rustc"):
            return "skip:rustc"
        out = Path("/tmp/_apl_rs")
        c = subprocess.run(["rustc", "-O", "--edition", "2021", "-D", "warnings", str(p), "-o", str(out)],
                           capture_output=True, timeout=120)
        ok = c.returncode == 0 and subprocess.run([str(out)], capture_output=True,
                                                  timeout=120).returncode == 0
        return "ok" if ok else "fail"
    return "ok"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pubkey", default=str(ROOT / "aura-signing.pub"))
    ap.add_argument("--gate", action="store_true", help="also compile/run every file (slow)")
    args = ap.parse_args()
    pub = Path(args.pubkey).read_text().strip() if Path(args.pubkey).exists() else args.pubkey

    fails, disk_ids, source_ids = [], set(), set()
    skipped = {}   # toolchain -> file count (missing compiler/runner under --gate)
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
            if st.startswith("python") or st == "r":
                source_ids.add(p.stem)
            mr = verify_file(p)
            if mr.status != "authentic" or (mr.payload and not mr.payload.is_master):
                bad += 1; fails.append(f"{p.relative_to(ROOT)}: watermark {mr.status}")
            if p.stem in quarantined:
                fails.append(f"{p.relative_to(ROOT)}: quarantined ID present in shippable tree")
            if args.gate:
                g = run_gate(p)
                if g == "fail":
                    fails.append(f"{p.relative_to(ROOT)}: GATE fail")
                elif g.startswith("skip:"):
                    skipped[g[5:]] = skipped.get(g[5:], 0) + 1
        print(f"                         watermark: {'all valid' if not bad else f'{bad} BAD'}")

    if skipped:
        for tc, n in sorted(skipped.items()):
            print(f"!! GATE SKIPPED — toolchain '{tc}' missing: {n} file(s) NOT validated")
            fails.append(f"GATE SKIPPED: toolchain '{tc}' missing — {n} file(s) not validated")

    # (f) twin integrity — cpp/go twin whose source ID is missing or quarantined.
    # source_ids holds python/r stems only (disk_ids would include the twin itself).
    # cpp/go are SIGNED_SUBTREES, so the loop above already gated them — no re-gate here.
    for tl in ("cpp", "go"):
        for p in (ROOT / tl).rglob("*"):
            if p.suffix not in (".cpp", ".go"):
                continue
            if p.stem in quarantined:
                fails.append(f"{p.relative_to(ROOT)}: twin of a quarantined pattern")
            if p.stem not in source_ids:
                fails.append(f"{p.relative_to(ROOT)}: twin with no python/r source ID")

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
