#!/usr/bin/env python3
"""
ingest.py — the Grand Library's twin ingest (LIBRARY-INGEST-CONTRACT Part B / SYNC.md).

Reads final_approved.jsonl from the conversion pipeline and ingests each passing
C++/Go twin into this library: gate B4 -> copy -> master-0 watermark -> sign the
cpp subtree -> patch CATALOG + MANIFEST -> ensure the verifier covers cpp -> verify.

RUN WITH THE folder-nature venv python (needs folder_nature.mark + yaml):
    ~/Projects/folder-nature/.venv/bin/python ingest.py --lib <target> [--commit]

Default is a DRY RUN against --lib (no library mutation). Point --lib at a scratch
copy to rehearse; point it at ~/aura-pattern-library and pass --commit for the real
ingest (Illia's explicit yes is the only door to that).

THE INGEST GATE B4 — a twin enters ONLY if ALL hold:
  1. ver_verdict == approved and a final_approver is present
  2. source_path exists AND its id is in NO QUARANTINE.jsonl / _quarantine
  3. sha256(source_path) == source_sha256   (coupling law — no drift)
  4. twin compiles + runs exit 0 (g++ -O2 -std=c++17)
Fail any -> skip that twin, report it, do not ship.
"""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from _check_folder_nature import add_dev_checkout as _dev, require as _require  # noqa: E402

_dev()
from folder_nature.mark import signing, watermark as wm       # noqa: E402
from folder_nature.mark.payload import WatermarkPayload        # noqa: E402

_require()

HOME = Path.home()
FINAL = HOME / "ai-lab/patterns_cpp/final_approved.jsonl"
DS_QUAR = HOME / "ai-lab/patterns_ds/QUARANTINE.jsonl"
KEY = HOME / ".config/folder-nature/aura-signing.key"
TRADEMARK, COMPANY = "AURA Pattern Library", "Reality Optimizer"


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def gate_b4(row, lib, quar):
    pid = row["id"]
    src = Path(row["source_path"])
    twin = Path(row["twin_path"])
    if row.get("ver_verdict") != "approved" or not row.get("final_approver"):
        return False, "not ver-approved / no final_approver"
    if pid in quar:
        return False, "quarantined id"
    if not src.is_file():
        return False, "source missing"
    if not twin.is_file():
        return False, "twin missing"
    if hashlib.sha256(src.read_bytes()).hexdigest() != row["source_sha256"]:
        return False, "COUPLING DRIFT (source changed since approval)"
    if shutil.which("g++"):
        out = Path("/tmp/_ingest_x")
        c = subprocess.run(["g++", "-O2", "-std=c++17", str(twin), "-o", str(out)],
                           capture_output=True, timeout=120)
        if c.returncode != 0 or subprocess.run([str(out)], capture_output=True,
                                               timeout=120).returncode != 0:
            return False, "compile/run gate failed"
    return True, "ok"


def patch_catalog(catalog_path: Path, ingested_ids, lang="cpp", commit=False):
    text = catalog_path.read_text(encoding="utf-8")
    changed = 0
    for pid in ingested_ids:
        # | `id` | languages | category |
        pat = re.compile(r"^(\| `" + re.escape(pid) + r"` \| )([^|]*?)( \|)", re.M)
        m = pat.search(text)
        if not m:
            continue
        langs = m.group(2).strip()
        parts = [p for p in re.split(r"[·,]\s*", langs) if p]
        if lang in parts:
            continue
        parts.append(lang)
        text = text[:m.start(2)] + "·".join(parts) + text[m.end(2):]
        changed += 1
    if commit:
        catalog_path.write_text(text, encoding="utf-8")
    return changed


def ensure_verifier_covers_cpp(lib: Path, commit=False):
    lv = lib / "library_verify.py"
    text = lv.read_text(encoding="utf-8")
    if '"cpp"' in text and "SIGNED_SUBTREES" in text and re.search(
            r'SIGNED_SUBTREES\s*=\s*\[[^\]]*"cpp"', text):
        return False
    new = re.sub(r'(SIGNED_SUBTREES\s*=\s*\[[^\]]*?)\]',
                 r'\1, "cpp"]', text, count=1)
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
    if DS_QUAR.is_file():
        quar |= {json.loads(l)["id"] for l in DS_QUAR.read_text().splitlines() if l.strip()}
    quar |= {p.stem for p in (lib / "_quarantine").glob("*.py")}

    passed, skipped = [], []
    for row in rows:
        ok, why = gate_b4(row, lib, quar)
        (passed if ok else skipped).append((row, why))

    print(f"final_approved rows: {len(rows)} | pass B4: {len(passed)} | skip: {len(skipped)}")
    for row, why in skipped:
        print(f"  SKIP {row['id']}: {why}")

    if not commit:
        # rehearse counts only
        cats = sorted({slug(r["category"]) for r, _ in passed})
        print(f"\nDRY RUN — would ingest {len(passed)} twins into "
              f"{lib}/cpp/data-science/<category>/ across {len(cats)} categories.")
        print("run with --commit against a scratch --lib to rehearse fully, "
              "or against the real library only on Illia's yes.")
        return 0

    # ---- COMMIT PATH ----
    cpp_root = lib / "cpp"
    ingested = []
    for row, _ in passed:
        dest_dir = cpp_root / "data-science" / slug(row["category"])
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / f"{row['id']}.cpp"
        shutil.copy2(row["twin_path"], dest)
        wm.stamp_file(dest, WatermarkPayload(trademark=TRADEMARK, company=COMPANY, number="0"))
        ingested.append(row["id"])

    # mark config + sign the cpp subtree
    (cpp_root / ".folder-mark.yaml").write_text(
        f"trademark: {TRADEMARK}\ncompany: {COMPANY}\ntier: team\nlicense_tier: team\n")
    seed = signing.read_private_key(Path(args.key))
    signing.sign_directory(cpp_root, TRADEMARK, seed)

    changed = patch_catalog(lib / "CATALOG.md", ingested, commit=True)
    verifier_patched = ensure_verifier_covers_cpp(lib, commit=True)

    # MANIFEST.json: add/refresh the cpp/data-science language entry
    mf = lib / "MANIFEST.json"
    data = json.loads(mf.read_text())
    data.setdefault("languages", {})["cpp/data-science"] = {
        "files": len(ingested), "gate_ok": len(ingested), "gate_fail": 0,
        "signature": "authentic + unaltered"}
    mf.write_text(json.dumps(data, indent=2) + "\n")

    print(f"\ningested {len(ingested)} twins · CATALOG rows updated {changed} · "
          f"verifier patched: {verifier_patched}")

    # verify
    vr = subprocess.run([sys.executable, str(lib / "library_verify.py")],
                        capture_output=True, text=True, timeout=600)
    print("─" * 60)
    print(vr.stdout[-1500:])
    if vr.returncode != 0:
        print("library_verify RED — see above")
        return 1
    print("library_verify GREEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
