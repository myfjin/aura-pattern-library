#!/usr/bin/env python3
"""census — validity sweep (L1∧L2∧L3) + census of the AURA Pattern Library.

Every number in LIBRARY-CENSUS-*.md is reproduced by re-running this script.
Nothing is cited from memory; disk is the truth, CATALOG.md/MANIFEST.json are
cross-checked against it and every mismatch is REPORTED, never papered over.

VALIDITY (a pattern file is VALID iff all three hold):
  L1 RUNS          — compiles (where applicable) and executes exit 0.
  L2 REAL ASSERTS  — python: assert_linter AST tiering (REJECT = fail).
                     other languages: idiom-aware failure-path scan (weaker
                     instrument, honestly labeled): R stopifnot/stop · cpp
                     assert() · go os.Exit(1)/log.Fatal/panic · rust assert!*/
                     panic!/process::exit. Zero failure paths = L2 flag.
  L3 DETERMINISTIC — 3 fresh runs (python: PYTHONHASHSEED 0/1/2; compiled:
                     same binary 3x; R/go: 3 runs) → all exit 0 AND
                     byte-identical stdout. Any non-zero exit = REJECT;
                     exit-0 with varying stdout = NOTE (read-pass, not fail),
                     mirroring ~/ai-lab/tools/determinism_check.py semantics.

CPP PORTABILITY (finding-level, not quarantine): clang++ -std=c++17 -O2
compile is checked alongside g++; failures are reported separately.

CENSUS: pattern = one CATALOG.md row (id + languages + category); the same
stem in two spheres is TWO patterns (circuit_breaker exists 3x). Twins fold
into their source sphere. All six breakdowns are computed from disk AND from
the catalog, and the two must reconcile.

CLI: census.py [--jobs N] [--runs N] [--out results.json] [--skip-gate]
Exit: 0 = swept clean (mismatches/failures still exit 1).
"""
import argparse
import concurrent.futures as cf
import json
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path.home() / "ai-lab/tools"))
import assert_linter  # noqa: E402  (the committed AST gate — reused, not reinvented)

# tree prefix -> (sphere, lang, is_twin)
TREES = [
    ("python/programming", "programming", "python", False),
    ("python/data-science", "data-science", "python", False),
    ("python/system-administration", "system-administration", "python", False),
    ("r", "r-statistics", "r", False),
    ("cpp/data-science", "data-science", "cpp", True),
    ("go/programming", "programming", "go", True),
    ("go/system-administration", "system-administration", "go", True),
    ("rust", "rust-systems", "rust", False),
]
EXT = {"python": ".py", "r": ".R", "cpp": ".cpp", "go": ".go", "rust": ".rs"}
TOOLCHAINS = ["python3", "g++", "clang++", "go", "rustc", "Rscript"]

# categories that mark the composed/premium tier
COMPOSED_MARKERS = ("Composed Tools (bridge-born)", "Composed Systems (bridge)")
CROSS_SPHERE_MARKER = "Cross-Sphere Twins (bridge)"

# Lock/timing patterns assert on sub-second hold/wait windows (multiprocessing
# holder/waiter with 0.05–0.5s stagger); under --jobs contention the scheduler
# can starve those windows, so they flake in the pool yet pass standalone
# (census-flake law, proven 2026-07-12: failed as L3 then L1 across runs, 2/2
# standalone). Each uses its own mkdtemp, so it is starvation, not lock-path
# collision. They run in a single-worker lane AFTER the parallel pool drains.
SERIAL_LANE_DIR = "/concurrency-locking/"
SERIAL_LANE_RX = re.compile(r"flock|advisory_lock")


def needs_serial_lane(rec):
    return SERIAL_LANE_DIR in rec["path"] or bool(SERIAL_LANE_RX.search(rec["id"]))


def scan_disk():
    """Every source file in a shippable tree -> {sphere, lang, id, path, twin}."""
    files = []
    for prefix, sphere, lang, twin in TREES:
        base = ROOT / prefix
        if not base.exists():
            continue
        for p in sorted(base.rglob(f"*{EXT[lang]}")):
            files.append({"sphere": sphere, "lang": lang, "id": p.stem,
                          "path": str(p), "twin": twin})
    return files


def parse_catalog():
    """CATALOG.md rows -> [{id, langs, category}] (header row excluded)."""
    rows = []
    txt = (ROOT / "CATALOG.md").read_text(encoding="utf-8")
    for m in re.finditer(r"^\| `([^`]+)` \| ([^|]+) \| ([^|]+) \|", txt, re.M):
        rows.append({"id": m.group(1).strip(),
                     "langs": tuple(sorted(m.group(2).strip().split("·"))),
                     "category": m.group(3).strip()})
    return rows


def row_sphere(row, prog_python_ids):
    cat = row["category"]
    if cat.startswith("System Administration"):
        return "system-administration"
    if cat.startswith("Rust"):
        return "rust-systems"
    if row["langs"] == ("r",):
        return "r-statistics"
    return "programming" if row["id"] in prog_python_ids else "data-science"


# ---------- L1 + L3 (run in a worker) ----------

def _runs(cmd_builder, n, timeout=120):
    outs, codes = [], []
    for i in range(n):
        try:
            p = subprocess.run(cmd_builder(i), capture_output=True, timeout=timeout,
                               env=cmd_builder.env(i) if hasattr(cmd_builder, "env") else None)
            codes.append(p.returncode)
            outs.append(p.stdout)
        except subprocess.TimeoutExpired:
            codes.append(124)
            outs.append(b"<timeout>")
    return codes, outs


def gate_file(rec, n_runs):
    """L1+L3 for one file. Returns dict of verdicts. Compiled langs build once."""
    import os
    path, lang = rec["path"], rec["lang"]
    r = {"l1": None, "l3": None, "l3_note": False, "clangxx_ok": None, "detail": ""}
    tmp = None
    try:
        if lang in ("cpp", "rust", "go"):
            tmp = tempfile.mkdtemp(prefix="apl_census_")
            binp = str(Path(tmp) / "a.out")
            if lang == "cpp":
                c = subprocess.run(["g++", "-O2", "-std=c++17", path, "-o", binp],
                                   capture_output=True, timeout=240)
                cl = subprocess.run(["clang++", "-O2", "-std=c++17", path, "-o",
                                     str(Path(tmp) / "a_clang.out")],
                                    capture_output=True, timeout=240)
                r["clangxx_ok"] = cl.returncode == 0
            elif lang == "rust":
                c = subprocess.run(["rustc", "-O", "--edition", "2021", "-D", "warnings",
                                    path, "-o", binp], capture_output=True, timeout=240)
            else:  # go
                c = subprocess.run(["go", "build", "-o", binp, path],
                                   capture_output=True, timeout=240)
            if c.returncode != 0:
                r["l1"] = False
                r["detail"] = ("compile fail: " + c.stderr.decode(errors="replace")[:300])
                return r
            codes, outs = [], []
            for _ in range(n_runs):
                try:
                    p = subprocess.run([binp], capture_output=True, timeout=120)
                    codes.append(p.returncode); outs.append(p.stdout)
                except subprocess.TimeoutExpired:
                    codes.append(124); outs.append(b"<timeout>")
        elif lang == "python":
            codes, outs = [], []
            for hs in range(n_runs):
                env = dict(os.environ, PYTHONHASHSEED=str(hs))
                try:
                    p = subprocess.run([sys.executable, path], capture_output=True,
                                       timeout=120, env=env)
                    codes.append(p.returncode); outs.append(p.stdout)
                except subprocess.TimeoutExpired:
                    codes.append(124); outs.append(b"<timeout>")
        else:  # r
            codes, outs = [], []
            for _ in range(n_runs):
                try:
                    p = subprocess.run(["Rscript", path], capture_output=True, timeout=120)
                    codes.append(p.returncode); outs.append(p.stdout)
                except subprocess.TimeoutExpired:
                    codes.append(124); outs.append(b"<timeout>")
        r["l1"] = codes[0] == 0
        r["l3"] = all(c == 0 for c in codes)
        r["l3_note"] = r["l3"] and len(set(outs)) > 1
        if not r["l3"]:
            r["detail"] = f"exit codes {codes}"
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)
    return r


# ---------- L2 ----------

RX = {
    "r": re.compile(r"stopifnot\s*\(|\bstop\s*\("),
    "cpp": re.compile(r"\bassert\s*\(|static_assert\s*\("),
    "go": re.compile(r"os\.Exit\(1\)|log\.Fatal|\bpanic\("),
    "rust": re.compile(r"\bassert(_eq|_ne)?!|\bdebug_assert|\bpanic!|process::exit\(1\)"),
}
RX_HOLLOW = {
    "r": re.compile(r"stopifnot\s*\(\s*TRUE\s*\)"),
    "cpp": re.compile(r"\bassert\s*\(\s*(true|1)\s*\)"),
    "go": re.compile(r"a^"),          # no trivial idiom to catch mechanically
    "rust": re.compile(r"\bassert!\s*\(\s*true\s*\)"),
}


def lint_l2(rec):
    """L2 verdict: PASS/WARN/FLAG(=REJECT-equivalent). Python gets full AST tiering."""
    path, lang = rec["path"], rec["lang"]
    if lang == "python":
        verdict, detail = assert_linter.lint_file(path)
        return {"l2": verdict, "l2_detail": sorted({t for _, t in detail})}
    src = Path(path).read_text(encoding="utf-8", errors="replace")
    real = len(RX[lang].findall(src))
    hollow = len(RX_HOLLOW[lang].findall(src))
    if real - hollow <= 0:
        return {"l2": "REJECT", "l2_detail": [f"no real failure paths ({lang} scan)"]}
    return {"l2": "PASS", "l2_detail": [f"{real - hollow} failure path(s) ({lang} scan)"]}


# ---------- census ----------

def build_census(files, rows):
    prog_python_ids = {f["id"] for f in files
                       if f["sphere"] == "programming" and f["lang"] == "python"}
    for row in rows:
        row["sphere"] = row_sphere(row, prog_python_ids)

    # disk-side pattern keys: (sphere, id); catalog-side likewise
    disk_patterns = {(f["sphere"], f["id"]) for f in files}
    cat_patterns = {(r["sphere"], r["id"]) for r in rows}
    dup_rows = [k for k, c in Counter((r["sphere"], r["id"]) for r in rows).items() if c > 1]

    # per-row disk reconciliation: every claimed language must have its file
    tree_of = {}
    for f in files:
        tree_of.setdefault((f["sphere"], f["id"]), set()).add(f["lang"])
    # r-twins: an r file whose stem matches a non-r-sphere row claiming lang r
    r_twin_ids = {r["id"] for r in rows if "r" in r["langs"] and r["sphere"] != "r-statistics"}
    lang_mismatches = []
    for r_ in rows:
        have = set(tree_of.get((r_["sphere"], r_["id"]), set()))
        if r_["id"] in r_twin_ids and r_["sphere"] != "r-statistics":
            if ("r-statistics", r_["id"]) in tree_of:
                have.add("r")
        want = set(r_["langs"])
        if have != want:
            lang_mismatches.append({"id": r_["id"], "sphere": r_["sphere"],
                                    "catalog": sorted(want), "disk": sorted(have)})
    # disk patterns with no catalog row (r-twin files are consumed by their DS row)
    consumed_r = {("r-statistics", i) for i in r_twin_ids}
    orphans = sorted(k for k in disk_patterns - cat_patterns - consumed_r)
    ghost_rows = sorted(k for k in cat_patterns - disk_patterns)

    per_lang_files = Counter(f["lang"] for f in files)
    per_lang_ids = {lg: len({f["id"] for f in files if f["lang"] == lg})
                    for lg in per_lang_files}
    per_sphere_files = Counter(f["sphere"] for f in files)
    per_sphere_patterns = Counter(s for s, _ in disk_patterns)
    per_cat = defaultdict(Counter)
    for r_ in rows:
        per_cat[r_["sphere"]][r_["category"]] += 1

    composed = [r_ for r_ in rows if any(m in r_["category"] for m in COMPOSED_MARKERS)]
    cross_sphere = [r_ for r_ in rows if CROSS_SPHERE_MARKER in r_["category"]]
    base_n = len(rows) - len(composed) - len(cross_sphere)

    coverage = Counter("+".join(r_["langs"]) for r_ in rows)
    stem_collisions = {i: c for i, c in
                       Counter(i for _, i in cat_patterns).items() if c > 1}

    free_rows = [r_ for r_ in rows
                 if r_["sphere"] == "programming" and "python" in r_["langs"]]

    return {
        "total_files": len(files),
        "total_patterns_catalog_rows": len(rows),
        "total_patterns_disk": len(disk_patterns) - len(consumed_r & disk_patterns),
        "total_unique_stems": len({i for _, i in cat_patterns}),
        "duplicate_catalog_rows": dup_rows,
        "per_language_files": dict(per_lang_files),
        "per_language_unique_ids": per_lang_ids,
        "per_sphere_files": dict(per_sphere_files),
        "per_sphere_patterns": dict(per_sphere_patterns),
        "per_category": {s: dict(c) for s, c in per_cat.items()},
        "composed_patterns": sorted((r_["sphere"], r_["id"]) for r_ in composed),
        "cross_sphere_twin_patterns": sorted((r_["sphere"], r_["id"]) for r_ in cross_sphere),
        "base_patterns": base_n,
        "coverage_matrix": dict(coverage),
        "stem_collisions_across_spheres": stem_collisions,
        "free_tier_patterns": len(free_rows),
        "free_tier_ids": sorted(r_["id"] for r_ in free_rows),
        "lang_mismatches": lang_mismatches,
        "disk_orphans_not_in_catalog": orphans,
        "catalog_rows_missing_on_disk": ghost_rows,
    }


def twin_ledger_check():
    """Coupling law (INGEST-CONTRACT B3): every cpp/go twin needs a
    final_approved.jsonl row whose pinned source_sha256 still matches the
    source on disk. Drift = the source was fixed after approval = the twin
    is invalidated until re-converted + re-approved."""
    import hashlib
    out = {}
    for lang, ledger, tree, ext in [("cpp", "patterns_cpp", "cpp", ".cpp"),
                                    ("go", "patterns_go", "go", ".go")]:
        lp = Path.home() / "ai-lab" / ledger / "final_approved.jsonl"
        if not lp.exists():
            out[lang] = {"error": "ledger missing"}
            continue
        rows = [json.loads(l) for l in lp.read_text().splitlines() if l.strip()]
        # Append-only ledger: a re-converted id has an old (drifted) row + a new row.
        # Dedupe to the LAST row per id (latest stamp wins) before the drift loop,
        # else the superseded old row would flag COUPLING forever.
        rows = list({r["id"]: r for r in rows}.values())
        twin_ids = {p.stem for p in (ROOT / tree).rglob(f"*{ext}")}
        ledger_ids = {r["id"] for r in rows}
        drift, missing = [], []
        for r in rows:
            sp = Path(r["source_path"])
            if not sp.exists():
                missing.append(r["id"])
            elif hashlib.sha256(sp.read_bytes()).hexdigest() != r["source_sha256"]:
                drift.append(r["id"])
        out[lang] = {"twins_on_disk": len(twin_ids), "ledger_rows": len(rows),
                     "twins_without_ledger_row": sorted(twin_ids - ledger_ids),
                     "ledger_rows_without_twin": sorted(ledger_ids - twin_ids),
                     "source_missing": missing, "source_hash_drift": drift}
    return out


def manifest_crosscheck(files):
    man = json.loads((ROOT / "MANIFEST.json").read_text())
    tree_counts = Counter()
    for f in files:
        for prefix, sphere, lang, _ in TREES:
            if f["path"].startswith(str(ROOT / prefix) + "/") or \
               Path(f["path"]).is_relative_to(ROOT / prefix):
                tree_counts[prefix] += 1
                break
    deltas = []
    for key, info in man.get("languages", {}).items():
        got = tree_counts.get(key, tree_counts.get(key.rstrip("/"), 0))
        if key == "r":
            got = tree_counts.get("r", 0)
        if key == "rust":
            got = tree_counts.get("rust", 0)
        if info["files"] != got:
            deltas.append({"subtree": key, "manifest": info["files"], "disk": got})
    return {"manifest_deltas": deltas, "manifest_total_shippable": man.get("total_shippable"),
            "manifest_unique_ids": man.get("unique_ids")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--out", default=str(ROOT / "tools" / "census_results.json"))
    ap.add_argument("--skip-gate", action="store_true",
                    help="census + L2 only (no execution) — for quick reconciliation")
    ap.add_argument("--quarantine-out", default=None,
                    help="write failures as a QUARANTINE.jsonl ledger to this path")
    args = ap.parse_args()

    toolchains = {t: bool(shutil.which(t)) for t in TOOLCHAINS}
    print("TOOLCHAINS:", ", ".join(f"{t}={'present' if ok else 'ABSENT'}"
                                   for t, ok in toolchains.items()))
    absent = {t for t, ok in toolchains.items() if not ok}

    files = scan_disk()
    rows = parse_catalog()
    census = build_census(files, rows)
    census["toolchains"] = toolchains
    census.update(manifest_crosscheck(files))
    census["twin_ledger"] = twin_ledger_check()

    # L2 (cheap, always)
    for f in files:
        f.update(lint_l2(f))

    # L1 + L3
    skipped_langs = set()
    if not args.skip_gate:
        lang_tool = {"python": "python3", "r": "Rscript", "cpp": "g++",
                     "go": "go", "rust": "rustc"}
        gate_files = []
        for f in files:
            if lang_tool[f["lang"]] in absent:
                f.update({"l1": None, "l3": None, "l3_note": False,
                          "detail": f"SKIPPED — toolchain {lang_tool[f['lang']]} missing"})
                skipped_langs.add(f["lang"])
            else:
                gate_files.append(f)
        serial_files = [f for f in gate_files if needs_serial_lane(f)]
        pool_files = [f for f in gate_files if not needs_serial_lane(f)]
        done = 0
        with cf.ThreadPoolExecutor(max_workers=args.jobs) as ex:
            futs = {ex.submit(gate_file, f, args.runs): f for f in pool_files}
            for fut in cf.as_completed(futs):
                futs[fut].update(fut.result())
                done += 1
                if done % 100 == 0:
                    print(f"  gated {done}/{len(gate_files)}", flush=True)
        if serial_files:
            print(f"  serial lane: {len(serial_files)} timing-sensitive lock "
                  f"pattern(s), one at a time", flush=True)
        for f in serial_files:
            f.update(gate_file(f, args.runs))
            done += 1

    fails = [f for f in files if f.get("l1") is False or f.get("l3") is False
             or f["l2"] == "REJECT"]
    notes = [f for f in files if f.get("l3_note")]
    warns = [f for f in files if f["l2"] == "WARN"]
    clang_fails = [f for f in files if f.get("clangxx_ok") is False]

    census["validity"] = {
        "checked_files": len([f for f in files if f.get("l1") is not None]) if not args.skip_gate else 0,
        "skipped_languages": sorted(skipped_langs),
        "valid_files": sum(1 for f in files if f.get("l1") is True
                           and f.get("l3") is True and f["l2"] != "REJECT"),
        "failures": [{"id": f["id"], "sphere": f["sphere"], "lang": f["lang"],
                      "layer_failed": ("L1" if f.get("l1") is False else
                                       "L2" if f["l2"] == "REJECT" else "L3"),
                      "reason": (f.get("detail") or ";".join(f["l2_detail"]))
                      + ("; also L2 REJECT: " + ";".join(f["l2_detail"])
                         if f.get("l1") is False and f["l2"] == "REJECT" else "")}
                     for f in fails],
        "l3_stdout_notes": [{"id": f["id"], "sphere": f["sphere"], "lang": f["lang"]}
                            for f in notes],
        "l2_warn_files": len(warns),
        "clangxx_portability_fails": [{"id": f["id"], "path": f["path"]}
                                      for f in clang_fails],
        "runs_per_file": args.runs,
    }
    census["date"] = str(date.today())

    # coupling-law drift joins the failure ledger (twin invalidated, source fine)
    for lang, rep in census["twin_ledger"].items():
        for pid in rep.get("source_hash_drift", []):
            census["validity"]["failures"].append(
                {"id": pid, "sphere": "data-science" if lang == "cpp" else "twin",
                 "lang": lang, "layer_failed": "COUPLING",
                 "reason": "source_sha256 drift — source fixed after twin approval "
                           "(INGEST-CONTRACT B3); twin invalidated until re-approved"})

    if args.quarantine_out:
        with open(args.quarantine_out, "w") as fh:
            for f in census["validity"]["failures"]:
                fh.write(json.dumps({**f, "date": str(date.today()),
                                     "status": "fix-to-rejoin"}) + "\n")
        print(f"quarantine ledger -> {args.quarantine_out} "
              f"({len(census['validity']['failures'])} entries)")

    Path(args.out).write_text(json.dumps({"census": census, "files": files}, indent=1))
    print(json.dumps({k: v for k, v in census.items()
                      if k not in ("free_tier_ids", "per_category", "composed_patterns",
                                   "cross_sphere_twin_patterns")}, indent=2))
    print(f"full results -> {args.out}")

    bad = (fails or census["lang_mismatches"] or census["disk_orphans_not_in_catalog"]
           or census["catalog_rows_missing_on_disk"] or census["duplicate_catalog_rows"]
           or skipped_langs)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
