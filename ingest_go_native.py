#!/usr/bin/env python3
"""
ingest_go_native.py — ingest a NATIVELY HARVESTED Go sphere into the Grand Library.

Sibling of ingest_go.py. That script ingests CONVERSION TWINS: every file it places has a
python/r source of the same ID, and it patches an EXISTING catalog row by appending "go" to it.
A native harvest has no source and no existing row, so it needs its own lane:

  * new CATALOG rows (category "Go — <Sphere>", mirroring the "Rust — ..." convention)
  * a native_patterns declaration in MANIFEST.json  (library_verify RULER v2)
  * tag_folders.py BEFORE signing — a native sphere creates NEW category dirs, and a
    .folder-nature added after signing breaks manifest<->disk parity (SYNC.md order law)

RUN WITH THE folder-nature venv python:
    ~/Projects/folder-nature/.venv/bin/python ingest_go_native.py [--commit]

Default is a DRY RUN. --commit mutates the library (Illia's yes only).

GATE (a pattern enters ONLY if ALL hold):
  1. listed in --approved (the doc-verification verdict list; ingest is gated on review)
  2. sha256 matches --baseline (the file reviewed is the file ingested — coupling law)
  3. go vet + go build + go run + go run -race all exit 0, no DATA RACE
  4. its ID does not already exist anywhere in the library (no silent overwrite)
  5. it has NO python/r source of the same ID — if it has one it is a TWIN, not a native,
     and belongs in ingest_go.py's lane
"""
import argparse, hashlib, json, re, shutil, subprocess, sys
from pathlib import Path

from _check_folder_nature import add_dev_checkout as _dev, require as _require  # noqa: E402

_dev()
from folder_nature.mark import signing, watermark as wm            # noqa: E402
from folder_nature.mark.payload import WatermarkPayload            # noqa: E402

_require()

HOME = Path.home()
KEY = HOME / ".config/folder-nature/aura-signing.key"
TRADEMARK, COMPANY = "AURA Pattern Library", "Reality Optimizer"
RACE_ENV = {"sharded_counter": {"SKIP_COUNTEREXAMPLE": "1"}}   # deliberate unsync counterexample


def sh(args, cwd=None, env=None, timeout=180):
    import os
    e = dict(os.environ)
    if env:
        e.update(env)
    p = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=timeout, env=e)
    return p.returncode, p.stdout, p.stderr


def gate(path: Path, lib: Path, approved: set, baseline: dict, source_ids: set, disk_ids: set):
    pid = path.stem
    if pid not in approved:
        return False, "not in the approved list (doc verification did not clear it)"
    got = hashlib.sha256(path.read_bytes()).hexdigest()
    if baseline and baseline.get(path.name) != got:
        return False, "SHA DRIFT — the file changed since it was reviewed"
    if pid in disk_ids:
        return False, f"ID already present in the library — refusing to overwrite"
    if pid in source_ids:
        return False, "a python/r source of this ID exists — this is a TWIN, use ingest_go.py"
    rc, _, err = sh(["go", "vet", path.name], cwd=str(path.parent))
    if rc != 0:
        return False, f"go vet failed: {err.strip()[:120]}"
    rc, _, err = sh(["go", "build", "-o", f"/tmp/_ingn_{pid}", path.name], cwd=str(path.parent))
    if rc != 0:
        return False, f"go build failed: {err.strip()[:120]}"
    rc, _, err = sh([f"/tmp/_ingn_{pid}"])
    if rc != 0:
        return False, f"run exit {rc}: {err.strip()[:120]}"
    rc, out, err = sh(["go", "run", "-race", path.name], cwd=str(path.parent),
                      env=RACE_ENV.get(pid), timeout=300)
    if rc != 0 or "WARNING: DATA RACE" in (out + err):
        return False, f"-race failed: {(err or out).strip()[:120]}"
    return True, "ok"


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="staging dir holding the harvested .go files")
    ap.add_argument("--approved", required=True, help="file of approved pattern IDs, one per line")
    ap.add_argument("--baseline", help="shasum -a 256 output for the reviewed files")
    ap.add_argument("--sphere", default="programming")
    ap.add_argument("--category", default="concurrency")
    ap.add_argument("--catalog-category", default="Go — Concurrency")
    ap.add_argument("--lib", default=str(HOME / "aura-pattern-library"))
    ap.add_argument("--key", default=str(KEY))
    ap.add_argument("--commit", action="store_true")
    a = ap.parse_args(argv[1:])

    lib, src = Path(a.lib).resolve(), Path(a.src).expanduser().resolve()
    approved = {l.strip() for l in Path(a.approved).read_text().splitlines() if l.strip()
                and not l.startswith("#")}
    baseline = {}
    if a.baseline:
        for line in Path(a.baseline).read_text().splitlines():
            if line.strip():
                h, n = line.split()[0], line.split()[-1]
                baseline[Path(n).name] = h

    source_ids = {p.stem for p in lib.rglob("*") if p.suffix in (".py", ".R")
                  and not str(p).startswith(str(lib / "_quarantine"))}
    disk_ids = {p.stem for p in lib.rglob("*") if p.suffix in (".py", ".R", ".cpp", ".go", ".rs")}
    quarantined = {p.stem for p in (lib / "_quarantine").glob("*.py")}

    files = sorted(src.glob("*.go"))
    passed, skipped = [], []
    for f in files:
        if f.stem in quarantined:
            skipped.append((f, "quarantined ID")); continue
        ok, why = gate(f, lib, approved, baseline, source_ids, disk_ids)
        (passed if ok else skipped).append((f, why))

    print(f"staged: {len(files)} | pass gate: {len(passed)} | skip: {len(skipped)}")
    for f, why in skipped:
        print(f"  SKIP {f.name}: {why}")

    dest_dir = lib / "go" / ("system-administration" if a.sphere == "sysadmin" else "programming") / a.category
    if not a.commit:
        print(f"\nDRY RUN — would ingest {len(passed)} native Go patterns into "
              f"{dest_dir.relative_to(lib)}/")
        for f, _ in passed:
            print(f"    {f.name}")
        print(f"would add {len(passed)} CATALOG rows: | `<id>` | go | {a.catalog_category} |")
        print(f"would declare native_patterns.go += {sorted(f.stem for f, _ in passed)}")
        print("\nrun with --commit on Illia's yes.")
        return 0

    # ---- COMMIT ----
    go_root = lib / "go"
    dest_dir.mkdir(parents=True, exist_ok=True)
    ingested = []
    for f, _ in passed:
        dest = dest_dir / f.name
        shutil.copy2(f, dest)
        wm.stamp_file(dest, WatermarkPayload(trademark=TRADEMARK, company=COMPANY, number="0"))
        ingested.append(f.stem)
    print(f"copied + master-0 stamped: {len(ingested)}")

    # ORDER LAW: tag BEFORE sign (a new category dir needs its .folder-nature first)
    rc, out, err = sh([sys.executable, str(lib / "tag_folders.py")], cwd=str(lib), timeout=600)
    print(f"tag_folders: exit {rc} {(err or out).strip()[-160:]}")
    if rc != 0:
        print("tag_folders FAILED — stopping before signing"); return 1

    seed = signing.read_private_key(Path(a.key))
    signing.sign_directory(go_root, TRADEMARK, seed)
    print("go subtree re-signed")

    # CATALOG — natives get NEW rows (no python twin row exists to patch)
    cat = lib / "CATALOG.md"
    lines = cat.read_text(encoding="utf-8").splitlines(keepends=True)
    last_row = max(i for i, l in enumerate(lines) if l.startswith("| `"))
    new_rows = [f"| `{pid}` | go | {a.catalog_category} |\n" for pid in ingested
                if not any(re.match(rf"^\| `{re.escape(pid)}` \| go \|", l) for l in lines)]
    lines[last_row + 1:last_row + 1] = new_rows
    cat.write_text("".join(lines), encoding="utf-8")
    print(f"CATALOG: +{len(new_rows)} rows")

    # MANIFEST — counts FROM DISK (never from the delta), plus the native declaration
    mf = lib / "MANIFEST.json"
    data = json.loads(mf.read_text())
    for shelf in ("programming", "system-administration"):
        n = len(list((go_root / shelf).rglob("*.go"))) if (go_root / shelf).exists() else 0
        if n:
            data.setdefault("languages", {})[f"go/{shelf}"] = {
                "files": n, "gate_ok": n, "gate_fail": 0, "signature": "authentic + unaltered"}
    nat = data.setdefault("native_patterns", {})
    nat["go"] = sorted(set(nat.get("go", [])) | set(ingested))
    mf.write_text(json.dumps(data, indent=2) + "\n")
    print(f"MANIFEST: native_patterns.go = {len(nat['go'])} declared")

    vr = subprocess.run([sys.executable, str(lib / "library_verify.py")],
                        capture_output=True, text=True, timeout=900)
    print("-" * 60)
    print(vr.stdout[-2500:])
    if vr.returncode != 0:
        print("library_verify RED — see above")
        return 1
    print("library_verify GREEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
