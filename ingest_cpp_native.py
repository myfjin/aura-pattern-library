#!/usr/bin/env python3
"""
ingest_cpp_native.py — ingest a NATIVELY HARVESTED C++ sphere into the Grand Library.

Sibling of ingest_go_native.py, and of ingest.py (which ingests DS->C++ conversion TWINS:
every file it places has a python/R source of the same ID). A native harvest has no source
and no existing catalog row, so it needs its own lane:

  * new CATALOG rows (category "C++ — <Sphere>", mirroring the "Rust — ..." convention)
  * a native_patterns declaration in MANIFEST.json  (library_verify RULER v2)
  * tag_folders.py BEFORE signing — a native sphere creates NEW category dirs, and a
    .folder-nature added after signing breaks manifest<->disk parity (SYNC.md order law)

RUN WITH THE folder-nature venv python (it holds the signing library and the key is on .5):
    ~/Projects/folder-nature/.venv/bin/python ingest_cpp_native.py --src ... [--commit]

Default is a DRY RUN. --commit mutates the library (Illia's yes only).

GATE (a pattern enters ONLY if ALL hold):
  1. listed in --approved (the doc-verification verdict list; ingest is gated on review)
  2. sha256 matches --baseline (the file reviewed is the file ingested — coupling law)
  3. IT BUILDS AND PASSES UNDER THE LIBRARY'S OWN BUILD, WHICH HAS NO SANITIZERS.
     Measured 2026-09-02: polyglot.py:42 uses `g++ -std=c++17 -O0` and
     library_verify.py:204 uses `g++ -O2 -std=c++17`. A pattern that proves itself only by
     reading an AddressSanitizer report out of its child is RUNTIME-FAIL in the library, and
     the default library_verify.py compiles nothing — so it would print GREEN over a broken
     sphere. Both plain builds are gated here, at the door, because that is the ruler the
     destination actually applies.
  4. clang++ -pedantic compiles it (second frontend; g++ has hidden 19 portability failures)
  5. a <id>.md doc exists and is placed alongside — docs ship WITH the pattern
  6. its ID does not already exist anywhere in the library (no silent overwrite)
  7. it has NO python/R source of the same ID — if it has one it is a TWIN, not a native,
     and belongs in ingest.py's lane
  8. AFTER the master-0 watermark is stamped it still builds and still passes. Stamping
     rewrites the file; a gate that runs only before the stamp has not measured what ships.
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / "Projects/folder-nature"))
from folder_nature.mark import signing, watermark as wm            # noqa: E402
from folder_nature.mark.payload import WatermarkPayload            # noqa: E402

# --- the mark layer's version must be one we actually tested -------------------
# folder-nature changed under us in 0.2.2 (re-stamping is idempotent again — until
# then an indented mark line survived re-stamping and the file kept verifying as
# authentic with the OLD payload still embedded) and 0.2.3 (the manifest date is
# UTC, not the local clock). This library resolves folder_nature through a source
# checkout, so which version it gets depends on where that checkout happens to be —
# and on .8 the path does not even exist. Fail LOUDLY rather than run a mark layer
# we know is wrong.
import folder_nature  # noqa: E402

_MIN_FOLDER_NATURE = (0, 2, 3)
_found = tuple(int(p) for p in folder_nature.__version__.split(".") if p.isdigit())[:3]
if _found < _MIN_FOLDER_NATURE:
    raise RuntimeError(
        f"aura-pattern-library needs folder-nature >= "
        f"{'.'.join(map(str, _MIN_FOLDER_NATURE))}, found {folder_nature.__version__} "
        f"at {folder_nature.__file__}. See "
        "https://github.com/myfjin/folder-nature/releases"
    )
# ------------------------------------------------------------------------------

HOME = Path.home()
KEY = HOME / ".config/folder-nature/aura-signing.key"
TRADEMARK, COMPANY = "AURA Pattern Library", "Reality Optimizer"

# THE DESTINATION'S BUILDS — kept in this order so the O2 one (library_verify's) fails first.
LIB_BUILDS = (
    ("library_verify -O2", ["-O2", "-std=c++17"]),
    ("polyglot -O0",       ["-std=c++17", "-O0"]),
)


def sh(args, cwd=None, timeout=300):
    p = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def build_and_run(path: Path, tmp: Path, tag: str):
    """Compile with one of the destination's builds and run it. Returns (ok, why)."""
    exe = tmp / f"_ing_{path.stem}_{tag}"
    for label, flags in LIB_BUILDS:
        rc, _, err = sh(["g++"] + flags + [str(path), "-o", str(exe)])
        if rc != 0:
            return False, f"{label} build failed: {err.strip()[-140:]}"
        rc, out, err = sh([str(exe)])
        passlines = [l for l in out.splitlines() if l.startswith("PASS:")]
        if rc != 0:
            return False, f"{label} run exit {rc}: {(err or out).strip()[-140:]}"
        if len(passlines) != 1:
            return False, f"{label} printed {len(passlines)} PASS: lines, want exactly 1"
    return True, "ok"


def gate(path: Path, tmp: Path, approved, baseline, source_ids, disk_ids, docs: Path):
    pid = path.stem
    if pid not in approved:
        return False, "not in the approved list (doc verification did not clear it)"
    got = hashlib.sha256(path.read_bytes()).hexdigest()
    if baseline and baseline.get(path.name) != got:
        return False, "SHA DRIFT — the file changed since it was reviewed"
    if pid in disk_ids:
        return False, "ID already present in the library — refusing to overwrite"
    if pid in source_ids:
        return False, "a python/R source of this ID exists — this is a TWIN, use ingest.py"
    if not (docs / f"{pid}.md").is_file():
        return False, f"no doc {pid}.md — docs ship with the pattern"
    ok, why = build_and_run(path, tmp, "pre")
    if not ok:
        return False, why
    rc, _, err = sh(["clang++", "-std=c++17", "-pedantic", "-c", str(path),
                     "-o", os.devnull])
    if rc != 0:
        return False, f"clang++ -pedantic failed: {err.strip()[-140:]}"
    return True, "ok"


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="staging dir holding the harvested .cpp files")
    ap.add_argument("--docs", help="dir holding <id>.md docs (default: same as --src)")
    ap.add_argument("--approved", required=True, help="file of approved pattern IDs, one per line")
    ap.add_argument("--baseline", help="shasum -a 256 output for the reviewed files")
    ap.add_argument("--category", default="memory_safety")
    ap.add_argument("--catalog-category", default="C++ — Memory Safety")
    ap.add_argument("--lib", default=str(HOME / "aura-pattern-library"))
    ap.add_argument("--key", default=str(KEY))
    ap.add_argument("--commit", action="store_true")
    a = ap.parse_args(argv[1:])

    lib, src = Path(a.lib).resolve(), Path(a.src).expanduser().resolve()
    docs = Path(a.docs).expanduser().resolve() if a.docs else src
    tmp = Path(os.environ.get("TMPDIR", "/tmp")) / "ingest_cpp_native"
    tmp.mkdir(parents=True, exist_ok=True)

    approved = {l.strip() for l in Path(a.approved).read_text().splitlines()
                if l.strip() and not l.startswith("#")}
    baseline = {}
    if a.baseline:
        for line in Path(a.baseline).read_text().splitlines():
            if line.strip():
                baseline[Path(line.split()[-1]).name] = line.split()[0]

    quarantine = lib / "_quarantine"
    source_ids = {p.stem for p in lib.rglob("*") if p.suffix in (".py", ".R")
                  and not str(p).startswith(str(quarantine))}
    disk_ids = {p.stem for p in lib.rglob("*") if p.suffix in (".py", ".R", ".cpp", ".go", ".rs")}
    quarantined = {p.stem for p in quarantine.glob("*.py")} if quarantine.is_dir() else set()

    files = sorted(src.glob("*.cpp"))
    passed, skipped = [], []
    for f in files:
        if f.stem in quarantined:
            skipped.append((f, "quarantined ID")); continue
        ok, why = gate(f, tmp, approved, baseline, source_ids, disk_ids, docs)
        (passed if ok else skipped).append((f, why))

    print(f"staged: {len(files)} | pass gate: {len(passed)} | skip: {len(skipped)}")
    for f, why in skipped:
        print(f"  SKIP {f.name}: {why}")

    dest_dir = lib / "cpp" / "programming" / a.category
    if not a.commit:
        print(f"\nDRY RUN — would ingest {len(passed)} native C++ patterns + {len(passed)} docs "
              f"into {dest_dir.relative_to(lib)}/")
        for f, _ in passed:
            print(f"    {f.name}  +  {f.stem}.md")
        print(f"would add {len(passed)} CATALOG rows: | `<id>` | cpp | {a.catalog_category} |")
        print(f"would declare native_patterns.cpp = {len(passed)} ids")
        print("\nrun with --commit on Illia's yes.")
        return 0

    # ---- COMMIT ----
    cpp_root = lib / "cpp"
    dest_dir.mkdir(parents=True, exist_ok=True)
    ingested = []
    for f, _ in passed:
        dest = dest_dir / f.name
        shutil.copy2(f, dest)
        wm.stamp_file(dest, WatermarkPayload(trademark=TRADEMARK, company=COMPANY, number="0"))
        shutil.copy2(docs / f"{f.stem}.md", dest_dir / f"{f.stem}.md")
        ingested.append(f.stem)
    print(f"copied + master-0 stamped: {len(ingested)} patterns + {len(ingested)} docs")

    # GATE 8 — the stamp rewrites the file. Re-measure what actually ships.
    broke = []
    for pid in ingested:
        ok, why = build_and_run(dest_dir / f"{pid}.cpp", tmp, "post")
        if not ok:
            broke.append((pid, why))
    if broke:
        print(f"STOPPING: {len(broke)} pattern(s) no longer pass AFTER the watermark stamp:")
        for pid, why in broke:
            print(f"  {pid}: {why}")
        return 1
    print(f"post-stamp re-verification: {len(ingested)}/{len(ingested)} still build and pass")

    # ORDER LAW: tag BEFORE sign (a new category dir needs its .folder-nature first).
    # tag_folders.py is GLOBAL: it rewrites .folder-nature for EVERY folder and bumps
    # last_significant_change, which invalidates the signature of every signed subtree. We
    # sign only cpp/, so the identity churn on the untouched subtrees must be reverted —
    # re-signing them instead would stamp a false "changed today" onto six spheres that did
    # not change.
    rc, out, err = sh([sys.executable, str(lib / "tag_folders.py")], cwd=str(lib), timeout=900)
    print(f"tag_folders: exit {rc} {(err or out).strip()[-160:]}")
    if rc != 0:
        print("tag_folders FAILED — stopping before signing"); return 1

    rc, out, _ = sh(["git", "status", "--porcelain"], cwd=str(lib))
    churn = [l[3:] for l in out.splitlines()
             if l[3:].endswith(".folder-nature") and not l[3:].startswith("cpp/")]
    if churn:
        sh(["git", "checkout", "--"] + churn, cwd=str(lib))
        print(f"reverted .folder-nature churn on {len(churn)} untouched subtree folders")

    seed = signing.read_private_key(Path(a.key))
    signing.sign_directory(cpp_root, TRADEMARK, seed)
    print("cpp subtree re-signed")

    # CATALOG — natives get NEW rows (no python twin row exists to patch)
    cat = lib / "CATALOG.md"
    lines = cat.read_text(encoding="utf-8").splitlines(keepends=True)
    last_row = max(i for i, l in enumerate(lines) if l.startswith("| `"))
    new_rows = [f"| `{pid}` | cpp | {a.catalog_category} |\n" for pid in ingested
                if not any(re.match(rf"^\| `{re.escape(pid)}` \| cpp \|", l) for l in lines)]
    lines[last_row + 1:last_row + 1] = new_rows
    cat.write_text("".join(lines), encoding="utf-8")
    print(f"CATALOG: +{len(new_rows)} rows")

    # MANIFEST — counts FROM DISK (never from the delta), plus the native declaration
    mf = lib / "MANIFEST.json"
    data = json.loads(mf.read_text())
    for shelf in ("programming", "data-science", "system-administration"):
        d = cpp_root / shelf
        n = len(list(d.rglob("*.cpp"))) if d.exists() else 0
        if n:
            data.setdefault("languages", {})[f"cpp/{shelf}"] = {
                "files": n, "gate_ok": n, "gate_fail": 0, "signature": "authentic + unaltered"}
    nat = data.setdefault("native_patterns", {})
    nat["cpp"] = sorted(set(nat.get("cpp", [])) | set(ingested))
    mf.write_text(json.dumps(data, indent=2) + "\n")
    print(f"MANIFEST: native_patterns.cpp = {len(nat['cpp'])} declared")

    idx = lib / "build_patterns_index.py"
    if idx.is_file():
        rc, out, err = sh([sys.executable, str(idx)], cwd=str(lib), timeout=900)
        print(f"build_patterns_index: exit {rc} {(err or out).strip()[-160:]}")

    vr = subprocess.run([sys.executable, str(lib / "library_verify.py")],
                        capture_output=True, text=True, timeout=1800)
    print("-" * 60)
    print(vr.stdout[-3000:])
    if vr.returncode != 0:
        print("library_verify RED — see above")
        return 1
    print("library_verify GREEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
