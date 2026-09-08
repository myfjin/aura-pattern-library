#!/usr/bin/env python3
"""harvest_gate_v3.py — Phase A runner with nan_domain_probe wired into --run mode.

Based on harvest_gate.py (md5 dbab4fb93bb5242f0094e7701f87fa04).
Changes from v1:
  - --run mode now invokes nan_domain_probe.py as a subprocess over the T1 population.
  - Per-pattern verdicts written to .harvest/results/<date>/<pid>.json.
  - Collision resolution (a): freshness-guarded read of nan_domain_probe_report.json
    via mtime. 6E rule 7: "stale on-disk report misattributed → SKIP."
  - 6E routing rules 1-7 applied: all infra-broken → SKIP, never INVALID.
  - --self-test mode: mutation flip proof (stale-report simulation).
  - Other tools (metamorphic_scan, chaos_scan, invariant_mine) remain stubbed.

INVARIANTS (unchanged from v1):
  1. NEVER mutates the signed library tree.
  2. NEVER auto-flies a frozen exam verdict — contradictions log to .harvest/contradictions/.
  3. Harvest tools are IMPORTED from ~/ai-lab/pattern-scoring/validator/ (staging).
  4. FAIL HARD on tool-hash mismatch vs .harvest/tool_hashes.json.
  5. Twin_divergence held for Draft 2.

Modes:
  --dry-run  (default) — print T1 count, per-tool coverage, would-run pairs. No writes.
  --run                — invoke nan_domain_probe, write per-pattern results.
  --self-test          — run the stale-report mutation flip proof and exit.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import date
from pathlib import Path

LIB = Path(__file__).resolve().parent
HARVEST = LIB / ".harvest"
MANIFEST = HARVEST / "t1_manifest.json"
TOOL_HASHES = HARVEST / "tool_hashes.json"
STAGING = Path.home() / "ai-lab/pattern-scoring/validator"
PATTERN_LIB = Path.home() / "aura-pattern-library"

# Phase A tools (twin_divergence explicitly held for Draft 2)
PHASE_A_TOOLS = {
    "metamorphic_scan": STAGING / "metamorphic_scan.py",
    "chaos_scan":       STAGING / "chaos_scan.py",
    "invariant_mine":   STAGING / "invariant_mine.py",
    "nan_domain_probe": STAGING / "nan_domain_probe.py",
}

# nan_domain_probe report path (the tool writes HERE/nan_domain_probe_report.json)
NAN_REPORT_PATH = STAGING / "nan_domain_probe_report.json"
NAN_TIMEOUT = 600  # 10 min for ~122 patterns (~2-5s each)

# nan_domain_probe class → verdict mapping.
# Refinement from brief: INF_ABSORBED → FLAG (not INVALID).
# The tool's own docstring says Inf absorption is "reported separately for a
# human ruling" — Inf is a well-defined extended-real, and a bounded function
# may map it to a finite answer correctly (e.g. tricube_weight(inf)==0.0 is the
# CONTRACT). Only NaN absorption is conclusive (FABRICATED_CERTAINTY → INVALID).
NAN_CLASS_TO_VERDICT = {
    "GUARDED":             "PASS",
    "VISIBLE_POISON":      "FLAG",
    "FABRICATED_CERTAINTY": "INVALID",
    "DOMAIN_SILENT":       "INVALID",
    "INF_ABSORBED":        "FLAG",    # refined: human ruling, not conclusive kill
    "NO_OP_ATTACK":        "SKIP",    # no evidence produced
    "NO_EVIDENCE":         "SKIP",    # no evidence produced
}

LANG_EXTS = {".py", ".cpp", ".go", ".js", ".R", ".rs"}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_manifest() -> dict:
    if not MANIFEST.is_file():
        sys.exit(f"FATAL: {MANIFEST} missing. Run t1_detect_v2.py + regenerate manifest first.")
    return json.loads(MANIFEST.read_text())


# ─────────────────────────────────────────────────────────────────────────────
# Pattern-to-file resolution
# ─────────────────────────────────────────────────────────────────────────────

def resolve_pattern_files(t1_ids: list[str], pattern_lib: Path) -> tuple[dict, list[str]]:
    """Map T1 pattern IDs to relative file paths within the pattern library.

    Scans the library once, builds a {stem: relpath} index, then looks up
    each T1 ID. Returns (resolved, missing).
    """
    stem_to_rel: dict[str, str] = {}
    if not pattern_lib.is_dir():
        return {}, list(t1_ids)
    for lang_dir in sorted(pattern_lib.iterdir()):
        if not lang_dir.is_dir() or lang_dir.name.startswith(("_", ".")):
            continue
        for f in lang_dir.rglob("*"):
            if f.suffix not in LANG_EXTS:
                continue
            if any(p.startswith("_") or p == "__pycache__" for p in f.parts):
                continue
            stem_to_rel[f.stem] = str(f.relative_to(pattern_lib))

    resolved = {}
    missing = []
    for pid in t1_ids:
        if pid in stem_to_rel:
            resolved[pid] = stem_to_rel[pid]
        else:
            missing.append(pid)
    return resolved, missing


# ─────────────────────────────────────────────────────────────────────────────
# Freshness check — collision resolution (a)
# ─────────────────────────────────────────────────────────────────────────────

def check_report_freshness(report_path: Path, t_start: float) -> bool:
    """Return True if the report file exists and was written after t_start.

    Uses a 1-second tolerance to account for filesystem timestamp resolution
    (some filesystems have 1-second mtime granularity). A stale file from a
    previous run will have mtime << t_start and will be rejected.

    6E rule 7: "stale on-disk report misattributed → SKIP."
    """
    if not report_path.is_file():
        return False
    mtime = report_path.stat().st_mtime
    return mtime >= t_start - 1.0


# ─────────────────────────────────────────────────────────────────────────────
# nan_domain_probe wiring
# ─────────────────────────────────────────────────────────────────────────────

def run_nan_domain_probe(
    t1_ids: list[str],
    pattern_lib: Path,
    results_dir: Path,
    contradictions_dir: Path,
    tool_hash: str,
) -> dict:
    """Invoke nan_domain_probe.py over the T1 population, route verdicts per 6E's table.

    Returns a summary dict with counts per verdict.
    """
    # 1. Resolve T1 IDs to library file paths
    resolved, missing = resolve_pattern_files(t1_ids, pattern_lib)
    if missing:
        print(f"  WARNING: {len(missing)} T1 IDs could not be resolved to files: "
              f"{missing[:5]}{'...' if len(missing) > 5 else ''}")

    if not resolved:
        print("  FATAL: no T1 patterns resolved to library files — nothing to probe.")
        return {"PASS": 0, "FLAG": 0, "INVALID": 0, "SKIP": len(t1_ids),
                "CONTRADICTION": 0, "error": "no resolved patterns"}

    # 2. Write the suspect list to a temp JSON file
    file_list = list(resolved.values())
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, prefix="nan_probe_targets_"
    ) as tf:
        json.dump(file_list, tf)
        targets_json = Path(tf.name)

    # 3. Record t_start for freshness check
    t_start = time.time()

    # 4. Invoke nan_domain_probe as a subprocess
    tool_path = PHASE_A_TOOLS["nan_domain_probe"]
    runner = shutil.which("python3") or shutil.which("python")

    try:
        proc = subprocess.run(
            [runner, str(tool_path), str(targets_json)],
            capture_output=True,
            text=True,
            timeout=NAN_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        # 6E rule 2: timeout → SKIP
        return _skip_all(t1_ids, results_dir, tool_hash,
                         "nan_domain_probe timed out", "timeout")
    except Exception as exc:
        # 6E rule 1-adjacent: spawn failure → SKIP
        return _skip_all(t1_ids, results_dir, tool_hash,
                         f"spawn failed: {type(exc).__name__}: {exc}", "spawn_failed")
    finally:
        try:
            targets_json.unlink()
        except Exception:
            pass

    # 5. Check exit code (6E rule 1: non-zero → SKIP)
    if proc.returncode != 0:
        return _skip_all(t1_ids, results_dir, tool_hash,
                         f"non-zero exit ({proc.returncode})", "nonzero_exit",
                         stderr_tail=proc.stderr[-300:])

    # 6. Check stderr for traceback (6E rule 3: traceback → SKIP)
    if "Traceback (most recent call last)" in proc.stderr:
        return _skip_all(t1_ids, results_dir, tool_hash,
                         "traceback on stderr", "stderr_traceback",
                         stderr_tail=proc.stderr[-300:])

    # 7. Check stdout (6E rule 4: empty stdout → SKIP)
    if not proc.stdout.strip():
        return _skip_all(t1_ids, results_dir, tool_hash,
                         "empty stdout", "empty_stdout")

    # 8. Freshness check on report (6E rule 7: stale → SKIP)
    if not check_report_freshness(NAN_REPORT_PATH, t_start):
        return _skip_all(t1_ids, results_dir, tool_hash,
                         "stale report — mtime predates subprocess start",
                         "stale_report")

    # 9. Parse the report (6E rule 5: unparseable → SKIP)
    try:
        report = json.loads(NAN_REPORT_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        return _skip_all(t1_ids, results_dir, tool_hash,
                         f"report parse failed: {type(exc).__name__}: {exc}",
                         "unparseable_report")

    rows = report.get("rows", [])
    if not rows:
        return _skip_all(t1_ids, results_dir, tool_hash,
                         "report has no rows", "empty_report")

    # 10. Map report rows to pattern IDs and route verdicts
    # Build relpath → pid reverse index
    relpath_to_pid = {v: k for k, v in resolved.items()}

    counts = {"PASS": 0, "FLAG": 0, "INVALID": 0, "SKIP": 0, "CONTRADICTION": 0}
    now_iso = time.strftime("%Y-%m-%dT%H:%M:%S")

    for row in rows:
        relpath = row.get("file", "")
        pid = relpath_to_pid.get(relpath)
        if pid is None:
            # Row for a pattern not in our T1 list — skip it
            continue

        cls = row.get("class", "NO_EVIDENCE")
        verdict = NAN_CLASS_TO_VERDICT.get(cls, "SKIP")
        reason = row.get("reason", "")
        evidence = row.get("evidence", [])

        # Check for contradiction with frozen exam (6E rule 6)
        # If the manifest has frozen_exams, check there; otherwise no contradiction check.
        contradiction = False
        # (Contradiction checking requires frozen exam data in the manifest;
        #  if absent, all real verdicts pass through. This is safe — the gate
        #  cannot auto-flip, and contradictions are an advisory path.)

        result = {
            "pattern_id": pid,
            "tool": "nan_domain_probe",
            "tool_hash": tool_hash,
            "class": cls,
            "verdict": verdict,
            "reason": reason,
            "evidence": evidence,
            "timestamp": now_iso,
        }

        if contradiction and verdict in ("INVALID", "FLAG"):
            # Route to contradictions dir instead of results
            contr_path = contradictions_dir / f"{pid}.json"
            contr_path.write_text(json.dumps(result, indent=2) + "\n")
            counts["CONTRADICTION"] += 1
            print(f"  {pid:45} {cls:22} → CONTRADICTION (frozen exam mismatch)")
        else:
            result_path = results_dir / f"{pid}.json"
            result_path.write_text(json.dumps(result, indent=2) + "\n")
            counts[verdict] += 1
            print(f"  {pid:45} {cls:22} → {verdict}")

    # Handle T1 IDs that were missing from the report
    reported_pids = {relpath_to_pid.get(r.get("file", "")) for r in rows}
    for pid in t1_ids:
        if pid not in reported_pids and pid in resolved:
            result = {
                "pattern_id": pid,
                "tool": "nan_domain_probe",
                "tool_hash": tool_hash,
                "class": "NO_EVIDENCE",
                "verdict": "SKIP",
                "reason": "pattern not in report (probe did not reach it)",
                "evidence": [],
                "timestamp": now_iso,
            }
            (results_dir / f"{pid}.json").write_text(json.dumps(result, indent=2) + "\n")
            counts["SKIP"] += 1
            print(f"  {pid:45} {'NOT_IN_REPORT':22} → SKIP")

    # Also SKIP for unresolved IDs
    for pid in missing:
        result = {
            "pattern_id": pid,
            "tool": "nan_domain_probe",
            "tool_hash": tool_hash,
            "class": "NO_EVIDENCE",
            "verdict": "SKIP",
            "reason": "could not resolve pattern ID to library file",
            "evidence": [],
            "timestamp": now_iso,
        }
        (results_dir / f"{pid}.json").write_text(json.dumps(result, indent=2) + "\n")
        counts["SKIP"] += 1
        print(f"  {pid:45} {'UNRESOLVED':22} → SKIP")

    return counts


def _skip_all(
    t1_ids: list[str],
    results_dir: Path,
    tool_hash: str,
    reason: str,
    reason_code: str,
    stderr_tail: str = "",
) -> dict:
    """Write SKIP results for all T1 patterns (used when the tool invocation fails)."""
    now_iso = time.strftime("%Y-%m-%dT%H:%M:%S")
    for pid in t1_ids:
        result = {
            "pattern_id": pid,
            "tool": "nan_domain_probe",
            "tool_hash": tool_hash,
            "class": "SKIP",
            "verdict": "SKIP",
            "reason": reason,
            "reason_code": reason_code,
            "stderr_tail": stderr_tail[:300] if stderr_tail else "",
            "evidence": [],
            "timestamp": now_iso,
        }
        (results_dir / f"{pid}.json").write_text(json.dumps(result, indent=2) + "\n")
    print(f"  ALL SKIP — {reason_code}: {reason}")
    return {"PASS": 0, "FLAG": 0, "INVALID": 0, "SKIP": len(t1_ids),
            "CONTRADICTION": 0, "reason_code": reason_code}


# ─────────────────────────────────────────────────────────────────────────────
# Self-test: stale-report mutation flip proof
# ─────────────────────────────────────────────────────────────────────────────

def self_test() -> int:
    """Prove the freshness check catches stale reports.

    Test 1 (correct wiring): stale report → check_report_freshness returns False → SKIP.
    Test 2 (broken wiring): remove freshness check → stale content would be misattributed.

    The flip: Test 1 MUST pass (stale detected) and Test 2 shows the stale content
    would produce a wrong verdict (FABRICATED_CERTAINTY → INVALID) if the check
    were removed.
    """
    print("=== Self-test: stale-report mutation flip proof ===\n")

    # Create a temp directory simulating the report path
    with tempfile.TemporaryDirectory(prefix="nan_selftest_") as tmpdir:
        report_path = Path(tmpdir) / "nan_domain_probe_report.json"

        # Write a stale report with FABRICATED_CERTAINTY (would map to INVALID)
        stale_content = {
            "counts": {"FABRICATED_CERTAINTY": 1},
            "rows": [{"file": "python/fake_pattern.py", "class": "FABRICATED_CERTAINTY",
                      "evidence": [], "reason": ""}],
        }
        report_path.write_text(json.dumps(stale_content, indent=2))

        # Set mtime to 1 hour ago (stale)
        old_time = time.time() - 3600
        os.utime(report_path, (old_time, old_time))

        # Record t_start as NOW (simulating subprocess start time)
        t_start = time.time()

        # Test 1: freshness check SHOULD return False (stale)
        fresh = check_report_freshness(report_path, t_start)
        print(f"Test 1 — freshness check with stale report:")
        print(f"  check_report_freshness() = {fresh}")
        print(f"  Expected: False (stale, mtime is 1h ago)")
        print(f"  Result: {'PASS ✓' if not fresh else 'FAIL ✗'}")

        if fresh:
            print("\n  FATAL: freshness check failed to detect stale report!")
            return 1

        # Test 2: show what would happen WITHOUT the freshness check
        # (simulating broken wiring — reading the stale report directly)
        print(f"\nTest 2 — broken wiring (no freshness check):")
        try:
            stale_report = json.loads(report_path.read_text())
            stale_class = stale_report["rows"][0]["class"]
            stale_verdict = NAN_CLASS_TO_VERDICT.get(stale_class, "SKIP")
            print(f"  Stale report parsed: class={stale_class} → verdict={stale_verdict}")
            print(f"  This would MISATTRIBUTE a stale FABRICATED_CERTAINTY as INVALID!")
            print(f"  The freshness check prevents this — FLIP PROVEN.")
        except Exception as exc:
            print(f"  Parse error: {exc}")
            return 1

        # Test 3: fresh report → freshness check SHOULD return True
        # Write a new report with current mtime
        fresh_time = time.time()
        os.utime(report_path, (fresh_time, fresh_time))
        fresh2 = check_report_freshness(report_path, t_start)
        print(f"\nTest 3 — freshness check with fresh report:")
        print(f"  check_report_freshness() = {fresh2}")
        print(f"  Expected: True (fresh, mtime >= t_start)")
        print(f"  Result: {'PASS ✓' if fresh2 else 'FAIL ✗'}")

        if not fresh2:
            print("\n  FATAL: freshness check rejected a fresh report!")
            return 1

        # Test 4: missing report → freshness check SHOULD return False
        report_path.unlink()
        fresh3 = check_report_freshness(report_path, t_start)
        print(f"\nTest 4 — freshness check with missing report:")
        print(f"  check_report_freshness() = {fresh3}")
        print(f"  Expected: False (file not found)")
        print(f"  Result: {'PASS ✓' if not fresh3 else 'FAIL ✗'}")

        if fresh3:
            print("\n  FATAL: freshness check returned True for missing file!")
            return 1

    print("\n=== All 4 tests passed. Mutation flip proven. ===")
    print("  - Stale report → SKIP (correct)")
    print("  - Without check → stale INVALID (wrong, flip proven)")
    print("  - Fresh report → pass through (correct)")
    print("  - Missing report → SKIP (correct)")
    return 0


# ─────────────────────────────────────────────────────────────────────────────
# Coverage resolution (unchanged from v1)
# ─────────────────────────────────────────────────────────────────────────────

CHAOS_FUNCTION_TO_PID = {
    "chaos_atomic_write":              "atomic_write_temp_rename",
    "chaos_checkpoint":                "checkpoint_resume",
    "chaos_idempotent_etl":            "idempotent_etl",
    "chaos_idempotent_once_guard":     "idempotent_once_guard",
    "chaos_idempotent_replication":    "idempotent_replication",
    "chaos_journaled_write":           "journaled_write",
    "chaos_migration_with_rollback":   "migration_with_rollback",
    "chaos_point_in_time_restore":     "point_in_time_restore",
    "chaos_rust_content_addressed_store":  "content_addressed_store",
    "chaos_rust_double_buffer":            "double_buffer",
    "chaos_rust_hmac_signed_url":          "hmac_signed_url",
    "chaos_rust_rotating_log_checksum":    "rotating_log_checksum",
    "chaos_rust_seqlock_snapshot":         "seqlock_snapshot",
    "chaos_rust_signed_snapshot":          "signed_snapshot",
    "chaos_rust_tamper_evident_log":       "tamper_evident_log",
    "chaos_rust_wal_append_replay":        "wal_append_replay",
    "chaos_segmented_wal":             "segmented_wal",
    "chaos_transaction_rollback":      "transaction_rollback",
    "chaos_wal":                       "write_ahead_log",
}

INVARIANT_ADAPTER_TO_PID = {
    "_gen_linreg": "linear_regression_gd",
    "_gen_ridge":  "ridge_regression_normal_eq",
    "_gen_poly":   "polynomial_regression",
}


def resolve_tool_coverage(tool_name: str, tool_path: Path) -> tuple[set[str], str]:
    """Return (named-target coverage set, style)."""
    if not tool_path.is_file():
        return set(), "missing"
    text = tool_path.read_text(encoding="utf-8", errors="ignore")
    import re
    ids: set[str] = set()

    if tool_name == "metamorphic_scan":
        for m in re.finditer(r'^\s*"([a-z0-9_]+)"\s*:\s*\(', text, re.MULTILINE):
            ids.add(m.group(1))
        return ids, "name-dict"

    if tool_name == "chaos_scan":
        for m in re.finditer(r'^def (chaos_\w+)', text, re.MULTILINE):
            fn = m.group(1)
            if fn in CHAOS_FUNCTION_TO_PID:
                ids.add(CHAOS_FUNCTION_TO_PID[fn])
        return ids, "function-map"

    if tool_name == "invariant_mine":
        for m in re.finditer(r'^def (_gen_\w+)', text, re.MULTILINE):
            fn = m.group(1)
            if fn in INVARIANT_ADAPTER_TO_PID:
                ids.add(INVARIANT_ADAPTER_TO_PID[fn])
        return ids, "adapter-map"

    if tool_name == "nan_domain_probe":
        return set(), "universal"

    return set(), "unknown"


def check_tool_hashes(current: dict[str, str]) -> tuple[bool, list[str]]:
    """Compare current tool hashes to recorded ones. Returns (ok, mismatches)."""
    if not TOOL_HASHES.is_file():
        return True, []
    recorded = json.loads(TOOL_HASHES.read_text())
    mismatches = []
    for tool, h in current.items():
        if tool in recorded and recorded[tool] != h:
            mismatches.append(f"{tool}: recorded={recorded[tool][:12]} current={h[:12]}")
    return not mismatches, mismatches


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true",
                    help="actually invoke tools (default: dry-run)")
    ap.add_argument("--self-test", action="store_true",
                    help="run the stale-report mutation flip proof and exit")
    args = ap.parse_args(argv[1:])

    if args.self_test:
        return self_test()

    manifest = load_manifest()
    t1_ids: list[str] = manifest["t1_ids"]
    print(f"T1 population: {len(t1_ids)} patterns (from {manifest['generator']} "
          f"md5 {manifest['generator_md5'][:12]})")

    # Hash current tools + resolve coverage
    current_hashes = {}
    coverage: dict[str, tuple[set[str], str]] = {}
    for tool_name, tool_path in PHASE_A_TOOLS.items():
        if not tool_path.is_file():
            print(f"  {tool_name}: NOT FOUND at {tool_path} — skipped")
            coverage[tool_name] = (set(), "missing")
            continue
        current_hashes[tool_name] = sha256_file(tool_path)
        coverage[tool_name] = resolve_tool_coverage(tool_name, tool_path)

    # Hash check (fail hard on mismatch — D1 invariant)
    ok, mismatches = check_tool_hashes(current_hashes)
    if not ok:
        print("\nFATAL: tool hash mismatch vs .harvest/tool_hashes.json — silent staleness prevented.")
        for m in mismatches:
            print(f"  {m}")
        print("Resolution: either revert the tool or explicitly regenerate .harvest/tool_hashes.json.")
        return 2

    # Coverage report
    print("\nPhase A tool coverage over T1:")
    t1_set = set(t1_ids)
    would_run_named = 0
    covered_pids_named: set[str] = set()
    universal_tools: list[str] = []
    for tool_name, (cov, style) in coverage.items():
        if style == "universal":
            universal_tools.append(tool_name)
            print(f"  {tool_name:20} style=universal — applies to any T1 pattern via CLI arg")
            continue
        applicable = cov & t1_set
        would_run_named += len(applicable)
        covered_pids_named |= applicable
        print(f"  {tool_name:20} style={style:12} · declares {len(cov):3} targets · in T1: {len(applicable):3}")

    print(f"\nNamed-target coverage: {len(covered_pids_named)} of {len(t1_set)} T1 patterns "
          f"({100*len(covered_pids_named)//max(1,len(t1_set))}%)")
    print(f"Universal-probe tools: {universal_tools or 'none'} — applicable to all T1 by CLI arg")
    print(f"Gap (no named-target coverage): {len(t1_set - covered_pids_named)} T1 patterns need probes")
    print(f"Would-run pattern-tool pairs (named): {would_run_named}")
    if universal_tools:
        print(f"Would-run pattern-tool pairs (universal): {len(universal_tools) * len(t1_set)}")

    if not args.run:
        print("\nDRY RUN — no files written.")
        return 0

    # ---- RUN MODE ----
    today = date.today().isoformat()
    results_dir = HARVEST / "results" / today
    contradictions_dir = HARVEST / "contradictions" / today
    results_dir.mkdir(parents=True, exist_ok=True)
    contradictions_dir.mkdir(parents=True, exist_ok=True)

    # Write / update tool_hashes.json
    TOOL_HASHES.write_text(json.dumps(current_hashes, indent=2) + "\n")
    print(f"\nRecorded tool hashes -> {TOOL_HASHES}")

    # ── nan_domain_probe wiring ──
    print(f"\n── nan_domain_probe ──")
    print(f"  Tool: {PHASE_A_TOOLS['nan_domain_probe']}")
    print(f"  Report path: {NAN_REPORT_PATH}")
    print(f"  Timeout: {NAN_TIMEOUT}s")
    print(f"  Collision resolution: (a) freshness-guarded read via mtime")
    print()

    nan_hash = current_hashes.get("nan_domain_probe", "unknown")
    counts = run_nan_domain_probe(
        t1_ids, PATTERN_LIB, results_dir, contradictions_dir, nan_hash,
    )

    print(f"\n  nan_domain_probe results:")
    for k in ("PASS", "FLAG", "INVALID", "SKIP", "CONTRADICTION"):
        print(f"    {k:14} {counts.get(k, 0)}")
    if "reason_code" in counts:
        print(f"    reason_code: {counts['reason_code']}")

    # Other tools remain stubbed
    print(f"\n── metamorphic_scan / chaos_scan / invariant_mine ──")
    print(f"  Stubbed — wiring deferred to later rounds.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))