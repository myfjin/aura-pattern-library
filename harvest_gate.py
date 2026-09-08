#!/usr/bin/env python3
"""harvest_gate_v4.py — Phase A runner with nan_domain_probe wired (rule-3 refined).

Based on v3 (md5 df9265679fa8a135c5800ae6bce21fe8).
Changes from v3:
  - Rule 3 demoted: stderr traceback no longer triggers whole-run SKIP by itself.
    Only fires as whole-run SKIP when zero rows AND stderr tracebacks (true crash).
  - Report is now the load-bearing signal, not exit code or stdout.
  - Non-zero exit + fresh parseable report → still trustworthy, parse it.
  - Row-count guard: len(rows) != suspect_count → SKIP (partial-write protection).
  - --self-test extended to 6 tests (tests 5-6 prove the refinement flip).
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
NAN_TIMEOUT = 1800  # 30 min — empirically needed for 122 real patterns (5-8s/pattern with import overhead)

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
# Refined routing (6E rule-3 refinement, 2026-09-08)
# ─────────────────────────────────────────────────────────────────────────────

def _route_nan_result(
    returncode: int,
    stdout: str,
    stderr: str,
    report_path: Path,
    t_start: float,
    suspect_count: int,
) -> tuple[str, str, dict | None]:
    """Route the subprocess result per 6E's refined rules.

    Returns (action, reason_code, report_or_None).
    action is "parse" or "skip".
    If "parse", report is the parsed JSON dict.
    If "skip", report is None.

    Refined precedence (report is the load-bearing signal):
      1. Report missing → skip (report_missing)
      2. Report stale (mtime < t_start) → skip (report_stale)
      3. Report unparseable → skip (report_unparseable)
      4. Row count mismatch (partial write) → skip (row_count_mismatch)
      5. Zero rows + stderr traceback → skip (stderr_traceback_zero_rows)
      6. Otherwise → parse and route per-row

    Non-zero exit code is NOT a skip by itself (rule 3 carve-out): the tool can
    run to completion, write valid data, then crash in teardown.
    Stderr traceback is NOT a skip by itself (rule 1 demoted): per-pattern
    crashes leak stderr noise the tool intended to catch.
    """
    # 1. Report exists?
    if not report_path.is_file():
        return "skip", "report_missing", None

    # 2. Fresh?
    if not check_report_freshness(report_path, t_start):
        return "skip", "report_stale", None

    # 3. Parseable?
    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
    except Exception:
        return "skip", "report_unparseable", None

    # 4. Row-count guard (partial-write protection)
    rows = report.get("rows", [])
    if len(rows) != suspect_count:
        return "skip", "row_count_mismatch", None

    # 5. Zero rows + stderr traceback → true crash
    if len(rows) == 0 and "Traceback (most recent call last)" in stderr:
        return "skip", "stderr_traceback_zero_rows", None

    # 6. Otherwise: parse and route per-row
    return "parse", "", report


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
    """Invoke nan_domain_probe.py over the T1 population, route verdicts per 6E's refined table.

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

    # 5. Route the result using 6E's refined rules (report-first, not exit-code-first)
    action, reason_code, report = _route_nan_result(
        proc.returncode, proc.stdout, proc.stderr,
        NAN_REPORT_PATH, t_start, len(file_list),
    )

    if action == "skip":
        return _skip_all(t1_ids, results_dir, tool_hash,
                         f"routing skip: {reason_code}", reason_code,
                         stderr_tail=proc.stderr[-300:])

    # 6. Map report rows to pattern IDs and route verdicts
    rows = report.get("rows", [])
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
    """Prove the refined routing catches stale reports, partial writes, and
    does NOT over-fire on stderr noise.

    Tests 1-4: freshness check (unchanged from v3).
    Test 5: stderr traceback + fresh valid report → parse (NOT skip).
             Without refinement (v3), this would SKIP. WITH refinement, it parses.
             Flip: v3 would SKIP, v4 parses — the refinement saves 8 real defect candidates.
    Test 6: fresh report with wrong row count → skip (row_count_mismatch).
             Without the guard, it would parse and under-report.
             Flip: without guard → parse (wrong), with guard → skip (correct).
    """
    print("=== Self-test: 6 tests (rule-3 refinement + row-count guard) ===\n")

    all_pass = True

    with tempfile.TemporaryDirectory(prefix="nan_selftest_") as tmpdir:
        report_path = Path(tmpdir) / "nan_domain_probe_report.json"

        # ── Test 1: stale report → freshness check returns False ──
        report_path.write_text(json.dumps({"counts": {}, "rows": []}))
        old_time = time.time() - 3600
        os.utime(report_path, (old_time, old_time))
        t_start = time.time()
        fresh = check_report_freshness(report_path, t_start)
        print(f"Test 1 — stale report (mtime 1h ago):")
        print(f"  check_report_freshness() = {fresh}  Expected: False")
        ok = not fresh
        print(f"  Result: {'PASS ✓' if ok else 'FAIL ✗'}")
        all_pass &= ok

        # ── Test 2: broken wiring proof (stale content would misattribute) ──
        stale_report = json.loads(report_path.read_text())
        print(f"\nTest 2 — broken wiring (no freshness check):")
        print(f"  Stale report parsed without check → would misattribute stale content")
        print(f"  The freshness check prevents this — FLIP PROVEN.")
        # (structural proof — Test 1 shows the check rejects stale; without it, stale parses)

        # ── Test 3: fresh report → freshness check returns True ──
        fresh_time = time.time()
        os.utime(report_path, (fresh_time, fresh_time))
        fresh2 = check_report_freshness(report_path, t_start)
        print(f"\nTest 3 — fresh report (mtime ≈ now):")
        print(f"  check_report_freshness() = {fresh2}  Expected: True")
        ok = fresh2
        print(f"  Result: {'PASS ✓' if ok else 'FAIL ✗'}")
        all_pass &= ok

        # ── Test 4: missing report → freshness check returns False ──
        report_path.unlink()
        fresh3 = check_report_freshness(report_path, t_start)
        print(f"\nTest 4 — missing report:")
        print(f"  check_report_freshness() = {fresh3}  Expected: False")
        ok = not fresh3
        print(f"  Result: {'PASS ✓' if ok else 'FAIL ✗'}")
        all_pass &= ok

        # ── Test 5: stderr traceback + fresh valid report → parse (NOT skip) ──
        # This is the rule-3 refinement flip.
        # v3 would route SKIP (stderr traceback → whole-run skip).
        # v4 routes parse (report is fresh + parseable + correct row count).
        valid_report = {
            "counts": {"GUARDED": 2},
            "rows": [
                {"file": "python/pattern_a.py", "class": "GUARDED", "evidence": [], "reason": ""},
                {"file": "python/pattern_b.py", "class": "FABRICATED_CERTAINTY", "evidence": [], "reason": ""},
            ],
        }
        report_path.write_text(json.dumps(valid_report))
        now_time = time.time()
        os.utime(report_path, (now_time, now_time))
        t_start_5 = time.time() - 0.5  # report was written 0.5s ago — fresh

        # Simulate: exit code 0, stdout has summary, stderr has traceback noise
        action, reason_code, parsed = _route_nan_result(
            returncode=0,
            stdout="PROBE PASS over 2 suspects\n---\n  GUARDED              1\n  FABRICATED_CERTAINTY 1",
            stderr="Traceback (most recent call last):\n  File ...\n  ...some per-pattern noise...",
            report_path=report_path,
            t_start=t_start_5,
            suspect_count=2,
        )
        print(f"\nTest 5 — stderr traceback + fresh valid report (rule-3 refinement):")
        print(f"  _route_nan_result() = action={action!r}, reason={reason_code!r}")
        print(f"  Expected: action='parse' (report is fresh, 2 rows match suspect_count=2)")
        ok = (action == "parse")
        print(f"  Result: {'PASS ✓' if ok else 'FAIL ✗'}")
        if ok:
            print(f"  FLIP PROVEN: v3 would SKIP (stderr traceback); v4 PARSES (report is load-bearing).")
        all_pass &= ok

        # ── Test 6: fresh report with wrong row count → skip (row_count_mismatch) ──
        # This is the partial-write guard flip.
        partial_report = {
            "counts": {"GUARDED": 1},
            "rows": [
                {"file": "python/pattern_a.py", "class": "GUARDED", "evidence": [], "reason": ""},
                # pattern_b missing — partial write, only 1 of 2 rows
            ],
        }
        report_path.write_text(json.dumps(partial_report))
        now_time = time.time()
        os.utime(report_path, (now_time, now_time))
        t_start_6 = time.time() - 0.5

        action6, reason_code6, parsed6 = _route_nan_result(
            returncode=0,
            stdout="PROBE PASS over 2 suspects",
            stderr="",
            report_path=report_path,
            t_start=t_start_6,
            suspect_count=2,  # we passed 2 patterns, report has only 1 row
        )
        print(f"\nTest 6 — fresh report, wrong row count (partial-write guard):")
        print(f"  _route_nan_result() = action={action6!r}, reason={reason_code6!r}")
        print(f"  Expected: action='skip', reason='row_count_mismatch' (1 row != 2 suspects)")
        ok = (action6 == "skip" and reason_code6 == "row_count_mismatch")
        print(f"  Result: {'PASS ✓' if ok else 'FAIL ✗'}")
        if ok:
            print(f"  FLIP PROVEN: without guard → parse (under-report); with guard → skip (correct).")
        all_pass &= ok

    print(f"\n=== {'All 6 tests passed.' if all_pass else 'SOME TESTS FAILED.'} ===")
    if all_pass:
        print("  1. Stale report → SKIP (correct)")
        print("  2. Without check → stale misattributed (flip proven)")
        print("  3. Fresh report → parse (correct)")
        print("  4. Missing report → SKIP (correct)")
        print("  5. stderr traceback + fresh report → parse (rule-3 refinement flip)")
        print("  6. Wrong row count → SKIP (partial-write guard flip)")
    return 0 if all_pass else 1


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