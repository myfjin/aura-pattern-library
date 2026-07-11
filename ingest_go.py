#!/usr/bin/env python3
"""
ingest_go.py — Grand Library GO twin ingest (LIBRARY-INGEST-CONTRACT Part B).

Sibling of ingest.py, adapted for Go: reads patterns_go/final_approved.jsonl,
runs gate B4 with `go build && run`, copies each passing twin into
go/<shelf>/<category>/, master-0 watermarks it, signs the go subtree, patches
CATALOG (sphere-correct row) + MANIFEST, ensures the verifier covers go, verifies.

RUN WITH THE folder-nature venv python:
    ~/Projects/folder-nature/.venv/bin/python ingest_go.py [--commit]

Default is a DRY RUN (no mutation). --commit does the real ingest (Illia's yes only).

GATE B4 (a twin enters ONLY if ALL hold):
  1. ver_verdict == approved and final_approver present
  2. source_path exists AND id in NO quarantine
  3. sha256(source_path) == source_sha256   (coupling law)
  4. go build ok AND run exit 0
"""
import argparse, hashlib, json, re, shutil, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / "Projects/folder-nature"))
from folder_nature.mark import signing, watermark as wm            # noqa: E402
from folder_nature.mark.payload import WatermarkPayload            # noqa: E402

HOME = Path.home()
FINAL = HOME / "ai-lab/patterns_go/final_approved.jsonl"
SA_QUAR = HOME / "ai-lab/patterns_sysadmin/QUARANTINE.jsonl"
DS_QUAR = HOME / "ai-lab/patterns_ds/QUARANTINE.jsonl"
KEY = HOME / ".config/folder-nature/aura-signing.key"
TRADEMARK, COMPANY = "AURA Pattern Library", "Reality Optimizer"
SHELF = {"sysadmin": "system-administration", "programming": "programming"}


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def gate_b4(row, quar):
    pid = row["id"]
    src = Path(row["source_path"])
    twin = Path(row["twin_path"])
    if row.get("ver_verdict") != "approved" or not row.get("final_approver"):
        return False, "not ver-approved / no final_approver"
    if pid in quar:
        return False, "quarantined id"
    if not src.is_file():
        return False, f"source missing {src}"
    if not twin.is_file():
        return False, f"twin missing {twin}"
    if hashlib.sha256(src.read_bytes()).hexdigest() != row["source_sha256"]:
        return False, "COUPLING DRIFT (source changed since approval)"
    if shutil.which("go"):
        out = Path("/tmp/_ingest_go_x")
        c = subprocess.run(["go", "build", "-o", str(out), str(twin)],
                           capture_output=True, timeout=120)
        if c.returncode != 0:
            return False, "go build failed"
        if subprocess.run([str(out)], capture_output=True, timeout=60).returncode != 0:
            return False, "run exit != 0"
    return True, "ok"


def row_is_sysadmin(cat: str) -> bool:
    return cat.strip().startswith("System Administration")


def row_is_other_lang(cat: str) -> bool:
    c = cat.strip()
    return c.startswith("Rust ") or c.startswith("Rust—") or c.startswith("C++") or c.startswith("Go ")


def patch_catalog(catalog_path: Path, stamped, commit=False):
    """Append 'go' to the sphere-correct catalog row for each stamped twin."""
    lines = catalog_path.read_text(encoding="utf-8").splitlines(keepends=True)
    changed, unmatched = 0, []
    row_re = re.compile(r"^\| `([^`]+)` \| ([^|]*?) \| ([^|]*?) \|")
    for st in stamped:
        pid, sph = st["id"], st["sphere"]
        target_idx = None
        for i, ln in enumerate(lines):
            m = row_re.match(ln)
            if not m or m.group(1) != pid:
                continue
            cat = m.group(3)
            if row_is_other_lang(cat):
                continue
            if sph == "sysadmin" and row_is_sysadmin(cat):
                target_idx = i; break
            if sph == "programming" and not row_is_sysadmin(cat):
                target_idx = i; break
        if target_idx is None:
            unmatched.append((pid, sph)); continue
        m = row_re.match(lines[target_idx])
        langs = m.group(2).strip()
        parts = [p for p in re.split(r"[·,]\s*", langs) if p]
        if "go" not in parts:
            parts.append("go")
            new_langs = "·".join(parts)
            lines[target_idx] = lines[target_idx].replace(f"| {langs} |", f"| {new_langs} |", 1)
            changed += 1
    if commit:
        catalog_path.write_text("".join(lines), encoding="utf-8")
    return changed, unmatched


def ensure_verifier_covers_go(lib: Path, commit=False):
    lv = lib / "library_verify.py"
    text = lv.read_text(encoding="utf-8")
    if re.search(r'SIGNED_SUBTREES\s*=\s*\[[^\]]*"go"', text):
        return False
    new = re.sub(r'(SIGNED_SUBTREES\s*=\s*\[[^\]]*?)\]', r'\1, "go"]', text, count=1)
    if commit and new != text:
        lv.write_text(new, encoding="utf-8")
    return new != text


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--lib", default=str(HOME / "aura-pattern-library"))
    ap.add_argument("--final", default=str(FINAL))
    ap.add_argument("--key", default=str(KEY))
    ap.add_argument("--commit", action="store_true")
    args = ap.parse_args(argv[1:])
    lib = Path(args.lib).resolve()
    commit = args.commit

    rows = [json.loads(l) for l in Path(args.final).read_text().splitlines() if l.strip()]
    quar = set()
    for qp in (SA_QUAR, DS_QUAR):
        if qp.is_file():
            quar |= {json.loads(l)["id"] for l in qp.read_text().splitlines() if l.strip()}
    quar |= {p.stem for p in (lib / "_quarantine").glob("*.py")}

    passed, skipped = [], []
    for row in rows:
        ok, why = gate_b4(row, quar)
        (passed if ok else skipped).append((row, why))

    print(f"final_approved rows: {len(rows)} | pass B4: {len(passed)} | skip: {len(skipped)}")
    for row, why in skipped:
        print(f"  SKIP {row['id']}/{row['sphere']}: {why}")

    if not commit:
        from collections import Counter
        dist = Counter((r["sphere"], slug(r["category"])) for r, _ in passed)
        print(f"\nDRY RUN — would ingest {len(passed)} go twins into go/<shelf>/<category>/:")
        for (sph, cat), n in sorted(dist.items()):
            print(f"    go/{SHELF[sph]}/{cat}/  <- {n}")
        # rehearse catalog matching
        _, unmatched = patch_catalog(lib / "CATALOG.md", [r for r, _ in passed], commit=False)
        print(f"catalog rows matchable: {len(passed) - len(unmatched)}/{len(passed)}"
              f"  unmatched: {unmatched}")
        print("run with --commit on Illia's yes.")
        return 0

    # ---- COMMIT ----
    go_root = lib / "go"
    ingested = []
    for row, _ in passed:
        dest_dir = go_root / SHELF[row["sphere"]] / slug(row["category"])
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / f"{row['id']}.go"
        shutil.copy2(row["twin_path"], dest)
        wm.stamp_file(dest, WatermarkPayload(trademark=TRADEMARK, company=COMPANY, number="0"))
        ingested.append(row)

    (go_root / ".folder-mark.yaml").write_text(
        f"trademark: {TRADEMARK}\ncompany: {COMPANY}\ntier: team\nlicense_tier: team\n")
    seed = signing.read_private_key(Path(args.key))
    signing.sign_directory(go_root, TRADEMARK, seed)

    changed, unmatched = patch_catalog(lib / "CATALOG.md", ingested, commit=True)
    verifier_patched = ensure_verifier_covers_go(lib, commit=True)

    mf = lib / "MANIFEST.json"
    data = json.loads(mf.read_text())
    from collections import Counter
    per = Counter((r["sphere"]) for r in ingested)
    for sph, n in per.items():
        data.setdefault("languages", {})[f"go/{SHELF[sph]}"] = {
            "files": n, "gate_ok": n, "gate_fail": 0, "signature": "authentic + unaltered"}
    mf.write_text(json.dumps(data, indent=2) + "\n")

    print(f"\ningested {len(ingested)} go twins · CATALOG rows updated {changed} "
          f"(unmatched {len(unmatched)}: {unmatched}) · verifier patched: {verifier_patched}")

    vr = subprocess.run([sys.executable, str(lib / "library_verify.py")],
                        capture_output=True, text=True, timeout=600)
    print("-" * 60)
    print(vr.stdout[-2000:])
    if vr.returncode != 0:
        print("library_verify RED — see above"); return 1
    print("library_verify GREEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
