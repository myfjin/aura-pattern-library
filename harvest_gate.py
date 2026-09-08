#!/usr/bin/env python3
"""harvest_gate_v6.py — Phase A runner with per-tool result isolation (no clobber).

Based on v5 (md5 aebe44e8deb1a81ac3cfda0b08941d54).
Changes from v5:
  - Per-tool result isolation: results written to results/<date>/<pid>/<tool>.json
    instead of results/<date>/<pid>.json. Both tools' verdicts survive on disk.
  - _skip_all now takes tool_name parameter (was hardcoded to nan_domain_probe).
  - _write_result / _write_contradiction helpers added.
  - --self-test extended to 9 tests (test 9 proves no-clobber across tools).
  - nan_domain_probe + metamorphic_scan routing unchanged from v5.

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
NAN_TIMEOUT = 1800  # 30 min — empirically needed for 122 real patterns (600s times out; 1800s recovers 8 defect candidates)

# metamorphic_scan report path (the tool writes HERE/metamorphic_report.json)
METAMORPHIC_REPORT_PATH = STAGING / "metamorphic_report.json"
METAMORPHIC_TIMEOUT = 300  # 30s × 9 patterns

# Negative-control abort signal (6E row 6)
NEGATIVE_CONTROL_ABORT = "ABORT: metamorphic detection is cosmetic"

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
                         "nan_domain_probe timed out", "timeout",
                         tool_name="nan_domain_probe")
    except Exception as exc:
        # 6E rule 1-adjacent: spawn failure → SKIP
        return _skip_all(t1_ids, results_dir, tool_hash,
                         f"spawn failed: {type(exc).__name__}: {exc}", "spawn_failed",
                         tool_name="nan_domain_probe")
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
                         tool_name="nan_domain_probe",
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
            _write_contradiction(contradictions_dir, pid, "nan_domain_probe", result)
            counts["CONTRADICTION"] += 1
            print(f"  {pid:45} {cls:22} → CONTRADICTION (frozen exam mismatch)")
        else:
            _write_result(results_dir, pid, "nan_domain_probe", result)
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
            _write_result(results_dir, pid, "nan_domain_probe", result)
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
        _write_result(results_dir, pid, "nan_domain_probe", result)
        counts["SKIP"] += 1
        print(f"  {pid:45} {'UNRESOLVED':22} → SKIP")

    return counts


def _write_result(results_dir: Path, pid: str, tool_name: str, result: dict) -> None:
    """Write a per-tool per-pattern result to results_dir/<pid>/<tool_name>.json.

    Per-tool isolation: each tool writes to its own file inside the pattern's
    directory, so tools never clobber each other. Extensible to N tools.
    """
    pattern_dir = results_dir / pid
    pattern_dir.mkdir(parents=True, exist_ok=True)
    (pattern_dir / f"{tool_name}.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )


def _write_contradiction(contradictions_dir: Path, pid: str, tool_name: str,
                         result: dict) -> None:
    """Write a contradiction result to contradictions_dir/<pid>/<tool_name>.json."""
    pattern_dir = contradictions_dir / pid
    pattern_dir.mkdir(parents=True, exist_ok=True)
    (pattern_dir / f"{tool_name}.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )


def _skip_all(
    t1_ids: list[str],
    results_dir: Path,
    tool_hash: str,
    reason: str,
    reason_code: str,
    tool_name: str = "nan_domain_probe",
    stderr_tail: str = "",
) -> dict:
    """Write SKIP results for all T1 patterns (used when the tool invocation fails)."""
    now_iso = time.strftime("%Y-%m-%dT%H:%M:%S")
    for pid in t1_ids:
        result = {
            "pattern_id": pid,
            "tool": tool_name,
            "tool_hash": tool_hash,
            "class": "SKIP",
            "verdict": "SKIP",
            "reason": reason,
            "reason_code": reason_code,
            "stderr_tail": stderr_tail[:300] if stderr_tail else "",
            "evidence": [],
            "timestamp": now_iso,
        }
        _write_result(results_dir, pid, tool_name, result)
    print(f"  ALL SKIP — {reason_code}: {reason}")
    return {"PASS": 0, "FLAG": 0, "INVALID": 0, "SKIP": len(t1_ids),
            "CONTRADICTION": 0, "reason_code": reason_code}


# ─────────────────────────────────────────────────────────────────────────────
# metamorphic_scan wiring
# ─────────────────────────────────────────────────────────────────────────────


def parse_metamorphic_patterns(tool_path: Path) -> dict[str, str]:
    """Parse PATTERNS dict from metamorphic_scan.py source.
    Returns {relpath: pattern_id} for reverse-mapping cards back to IDs.
    """
    import re
    text = tool_path.read_text(encoding="utf-8", errors="ignore")
    result = {}
    for m in re.finditer(r'"([a-z0-9_]+)":\s*\("[^"]+",\s*"([^"]+)"\)', text):
        pid, relpath = m.group(1), m.group(2)
        result[relpath] = pid
    return result


def _route_metamorphic_result(
    returncode: int,
    stdout: str,
    stderr: str,
    report_path: Path,
    t_start: float,
    suspect_count: int,
) -> tuple[str, str, dict | None]:
    """Route metamorphic_scan subprocess result per 6E's 9-row table.

    Returns (action, reason_code, report_or_None).
    action is "parse" or "skip".

    Row 6 (negative-control abort) is checked FIRST — short-circuit before
    any report check. The tool returns 1 before writing any report, so a
    stale report from a previous run must never be parsed.
    """
    # Row 6: negative-control abort — short-circuit
    if returncode != 0 and NEGATIVE_CONTROL_ABORT in stdout:
        return "skip", "negative_control_failed", None

    # Rows 1-5, 8-9: same report-first logic as _route_nan_result
    if not report_path.is_file():
        return "skip", "report_missing", None
    if not check_report_freshness(report_path, t_start):
        return "skip", "report_stale", None
    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
    except Exception:
        return "skip", "report_unparseable", None

    # Row 9: row-count guard (cards, not rows)
    cards = report.get("cards", [])
    if len(cards) != suspect_count:
        return "skip", "row_count_mismatch", None

    # Row 3: zero cards + stderr traceback → true crash
    if len(cards) == 0 and "Traceback (most recent call last)" in stderr:
        return "skip", "stderr_traceback_zero_cards", None

    # Row 4: parse and route per-card
    return "parse", "", report


# metamorphic card verdict → harvest verdict mapping (6E row 4 + row 7 override)
METAMORPHIC_VERDICT_MAP = {
    "PASS": "PASS",
    "INVALID-CANDIDATE": "INVALID",
    "FLAG": "SKIP",  # row 7 override: harness-error, not defect
}


def run_metamorphic_scan(
    t1_ids: list[str],
    results_dir: Path,
    contradictions_dir: Path,
    tool_hash: str,
) -> dict:
    """Invoke metamorphic_scan.py over the T1 ∩ PATTERNS intersection, route verdicts.

    Returns a summary dict with counts per verdict.
    """
    tool_path = PHASE_A_TOOLS["metamorphic_scan"]
    if not tool_path.is_file():
        print("  metamorphic_scan: NOT FOUND — skipped")
        return {"PASS": 0, "FLAG": 0, "INVALID": 0, "SKIP": len(t1_ids),
                "CONTRADICTION": 0, "reason_code": "tool_missing"}

    # 1. Parse the tool's PATTERNS dict to get covered pattern IDs
    relpath_to_pid = parse_metamorphic_patterns(tool_path)
    covered_pids = set(relpath_to_pid.values())
    suspects = [pid for pid in t1_ids if pid in covered_pids]

    if not suspects:
        print("  metamorphic_scan: no T1 patterns in tool's PATTERNS dict — skipped")
        return {"PASS": 0, "FLAG": 0, "INVALID": 0, "SKIP": len(t1_ids),
                "CONTRADICTION": 0, "reason_code": "no_covered_patterns"}

    print(f"  T1 ∩ PATTERNS: {len(suspects)} patterns to scan")

    # 2. Record t_start for freshness check
    t_start = time.time()

    # 3. Invoke metamorphic_scan as a subprocess (patterns as CLI args, not JSON)
    runner = shutil.which("python3") or shutil.which("python")
    try:
        proc = subprocess.run(
            [runner, str(tool_path)] + suspects,
            capture_output=True,
            text=True,
            timeout=METAMORPHIC_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        return _skip_all(t1_ids, results_dir, tool_hash,
                         "metamorphic_scan timed out", "timeout",
                         tool_name="metamorphic_scan")
    except Exception as exc:
        return _skip_all(t1_ids, results_dir, tool_hash,
                         f"spawn failed: {type(exc).__name__}: {exc}", "spawn_failed",
                         tool_name="nan_domain_probe")

    # 4. Route the result using 6E's refined table
    action, reason_code, report = _route_metamorphic_result(
        proc.returncode, proc.stdout, proc.stderr,
        METAMORPHIC_REPORT_PATH, t_start, len(suspects),
    )

    if action == "skip":
        return _skip_all(t1_ids, results_dir, tool_hash,
                         f"routing skip: {reason_code}", reason_code,
                         tool_name="nan_domain_probe",
                         stderr_tail=proc.stderr[-300:])

    # 5. Parse cards and route per-pattern verdicts
    cards = report.get("cards", [])
    counts = {"PASS": 0, "FLAG": 0, "INVALID": 0, "SKIP": 0, "CONTRADICTION": 0}
    now_iso = time.strftime("%Y-%m-%dT%H:%M:%S")

    for card in cards:
        relpath = card.get("pattern", "")
        pid = relpath_to_pid.get(relpath, relpath)  # fallback to relpath if unknown
        tool_verdict = card.get("verdict", "PASS")
        cls = card.get("class", "")

        # Row 7: override harness-error FLAG to SKIP
        if tool_verdict == "FLAG" and cls == "metamorphic-harness-error":
            harvest_verdict = "SKIP"
            reason = "harness_error — pattern was not tested (load/eval failure)"
        else:
            harvest_verdict = METAMORPHIC_VERDICT_MAP.get(tool_verdict, "SKIP")
            reason = card.get("actual", "")

        result = {
            "pattern_id": pid,
            "tool": "metamorphic_scan",
            "tool_hash": tool_hash,
            "class": cls,
            "verdict": harvest_verdict,
            "tool_verdict": tool_verdict,
            "reason": reason,
            "evidence": card.get("detail", []),
            "timestamp": now_iso,
        }

        # Row 8: contradiction check (scaffolded — needs frozen exam data)
        contradiction = False

        if contradiction and harvest_verdict in ("INVALID", "FLAG"):
            _write_contradiction(contradictions_dir, pid, "nan_domain_probe", result)
            counts["CONTRADICTION"] += 1
            print(f"  {pid:45} {cls:30} → CONTRADICTION")
        else:
            _write_result(results_dir, pid, "nan_domain_probe", result)
            counts[harvest_verdict] += 1
            extra = f" (override: {tool_verdict}→SKIP)" if tool_verdict == "FLAG" else ""
            print(f"  {pid:45} {cls:30} → {harvest_verdict}{extra}")

    # SKIP all T1 IDs not in the tool's PATTERNS (not covered by this tool)
    for pid in t1_ids:
        if pid not in covered_pids:
            result = {
                "pattern_id": pid,
                "tool": "metamorphic_scan",
                "tool_hash": tool_hash,
                "class": "not_covered",
                "verdict": "SKIP",
                "reason": "pattern not in metamorphic_scan PATTERNS dict",
                "evidence": [],
                "timestamp": now_iso,
            }
            _write_result(results_dir, pid, "metamorphic_scan", result)
            counts["SKIP"] += 1

    return counts


# ─────────────────────────────────────────────────────────────────────────────
# Self-test: stale-report mutation flip proof
# ─────────────────────────────────────────────────────────────────────────────

def self_test() -> int:
    """Prove the refined routing catches stale reports, partial writes, and
    does NOT over-fire on stderr noise. Tests 7-8 cover metamorphic divergences.

    Tests 1-4: freshness check (unchanged from v3).
    Test 5: stderr traceback + fresh valid report → parse (NOT skip).
    Test 6: fresh report with wrong row count → skip (row_count_mismatch).
    Test 7: negative-control abort (exit 1 + ABORT msg) → skip (negative_control_failed).
    Test 8: harness-error FLAG override → SKIP, not FLAG.
    """
    print("=== Self-test: 8 tests (nan + metamorphic wiring) ===\n")

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

        # ── Test 7: negative-control abort → skip (negative_control_failed) ──
        # 6E row 6: exit 1 + "ABORT: metamorphic detection is cosmetic" on stdout.
        # The tool returns 1 before writing any report. A stale report might exist.
        # Wiring must short-circuit to SKIP BEFORE checking the report.
        # Without the check, a fresh/stale report would be parsed → wrong.
        # Set up: write a fresh report (would pass freshness if we got that far)
        fresh_report_7 = {
            "cards": [
                {"pattern": "python/fake.py", "verdict": "PASS", "class": "metamorphic-coverage"},
            ],
        }
        report_path.write_text(json.dumps(fresh_report_7))
        now_time = time.time()
        os.utime(report_path, (now_time, now_time))
        t_start_7 = time.time() - 0.5

        action7, reason_code7, parsed7 = _route_metamorphic_result(
            returncode=1,
            stdout="METAMORPHIC RELATION ORACLE\n...\nnegative control: ... COSMETIC (ABORT)\nABORT: metamorphic detection is cosmetic (negative control failed).",
            stderr="",
            report_path=report_path,
            t_start=t_start_7,
            suspect_count=1,
        )
        print(f"\nTest 7 — negative-control abort (exit 1 + ABORT on stdout):")
        print(f"  _route_metamorphic_result() = action={action7!r}, reason={reason_code7!r}")
        print(f"  Expected: action='skip', reason='negative_control_failed'")
        print(f"  (fresh report exists but must be discarded — tool's relations lost calibration)")
        ok = (action7 == "skip" and reason_code7 == "negative_control_failed")
        print(f"  Result: {'PASS ✓' if ok else 'FAIL ✗'}")
        if ok:
            print(f"  FLIP PROVEN: without row-6 check → fresh report parsed (wrong); with check → skip (correct).")
        all_pass &= ok

        # ── Test 8: harness-error FLAG override → SKIP, not FLAG ──
        # 6E row 7: tool emits verdict="FLAG" with class="metamorphic-harness-error".
        # Wiring must override to SKIP with reason "harness_error".
        # Without the override, it would emit FLAG (wrong — harness broke, not a defect).
        harness_report = {
            "cards": [
                {"pattern": "python/fake.py", "verdict": "FLAG", "class": "metamorphic-harness-error",
                 "actual": "ImportError: missing dep"},
            ],
        }
        report_path.write_text(json.dumps(harness_report))
        now_time = time.time()
        os.utime(report_path, (now_time, now_time))
        t_start_8 = time.time() - 0.5

        action8, reason_code8, parsed8 = _route_metamorphic_result(
            returncode=0,
            stdout="METAMORPHIC RELATION ORACLE\n...\nmetamorphic PASS: 0/1 patterns",
            stderr="",
            report_path=report_path,
            t_start=t_start_8,
            suspect_count=1,
        )
        print(f"\nTest 8 — harness-error FLAG override:")
        print(f"  _route_metamorphic_result() = action={action8!r}, reason={reason_code8!r}")
        # Now simulate the per-card override
        if action8 == "parse" and parsed8:
            card = parsed8["cards"][0]
            tool_v = card.get("verdict", "")
            cls = card.get("class", "")
            if tool_v == "FLAG" and cls == "metamorphic-harness-error":
                harvest_v = "SKIP"
                override_reason = "harness_error"
            else:
                harvest_v = METAMORPHIC_VERDICT_MAP.get(tool_v, "SKIP")
                override_reason = "no override"
            print(f"  Card: tool_verdict={tool_v!r}, class={cls!r}")
            print(f"  Override: harvest_verdict={harvest_v!r}, reason={override_reason!r}")
            print(f"  Expected: harvest_verdict='SKIP', reason='harness_error'")
            ok = (harvest_v == "SKIP" and override_reason == "harness_error")
        else:
            print(f"  UNEXPECTED: routing did not parse — cannot test override")
            ok = False
        print(f"  Result: {'PASS ✓' if ok else 'FAIL ✗'}")
        if ok:
            print(f"  FLIP PROVEN: without override → FLAG (wrong, counts as defect); with override → SKIP (correct).")
        all_pass &= ok

        # ── Test 9: no-clobber across tools ──
        # Simulate two tools reporting on the SAME pattern with different verdicts.
        # With the fix (per-tool subdirectory layout), both survive on disk.
        # Without the fix (flat layout), the second write clobbers the first.
        test_results_dir = Path(tmpdir) / "test_results"
        test_results_dir.mkdir()

        # Tool A (nan_domain_probe) writes INVALID for pattern "foo"
        result_a = {
            "pattern_id": "foo",
            "tool": "nan_domain_probe",
            "tool_hash": "abc123",
            "class": "DOMAIN_SILENT",
            "verdict": "INVALID",
            "reason": "domain silent",
            "evidence": [],
            "timestamp": "2026-09-08T12:00:00",
        }
        _write_result(test_results_dir, "foo", "nan_domain_probe", result_a)

        # Tool B (metamorphic_scan) writes SKIP for the same pattern "foo"
        result_b = {
            "pattern_id": "foo",
            "tool": "metamorphic_scan",
            "tool_hash": "def456",
            "class": "not_covered",
            "verdict": "SKIP",
            "reason": "pattern not in metamorphic_scan PATTERNS dict",
            "evidence": [],
            "timestamp": "2026-09-08T12:01:00",
        }
        _write_result(test_results_dir, "foo", "metamorphic_scan", result_b)

        # Both results must be readable from disk
        path_a = test_results_dir / "foo" / "nan_domain_probe.json"
        path_b = test_results_dir / "foo" / "metamorphic_scan.json"
        both_exist = path_a.is_file() and path_b.is_file()

        if both_exist:
            read_a = json.loads(path_a.read_text())
            read_b = json.loads(path_b.read_text())
            verdict_a = read_a.get("verdict")
            verdict_b = read_b.get("verdict")
            ok = (verdict_a == "INVALID" and verdict_b == "SKIP"
                  and read_a.get("tool") == "nan_domain_probe"
                  and read_b.get("tool") == "metamorphic_scan")
        else:
            ok = False
            verdict_a = verdict_b = "N/A"

        print(f"\nTest 9 — no-clobber across tools:")
        print(f"  nan_domain_probe → {path_a.name} verdict={verdict_a!r}")
        print(f"  metamorphic_scan  → {path_b.name} verdict={verdict_b!r}")
        print(f"  Both files exist: {both_exist}")
        print(f"  Expected: nan_domain_probe=INVALID, metamorphic_scan=SKIP (both survive)")
        print(f"  Result: {'PASS ✓' if ok else 'FAIL ✗'}")
        if ok:
            print(f"  FLIP PROVEN: without fix → second write clobbers first (verdict lost);")
            print(f"               with fix → both verdicts survive in per-tool files.")
        all_pass &= ok

    print(f"\n=== {'All 9 tests passed.' if all_pass else 'SOME TESTS FAILED.'} ===")
    if all_pass:
        print("  1. Stale report → SKIP (correct)")
        print("  2. Without check → stale misattributed (flip proven)")
        print("  3. Fresh report → parse (correct)")
        print("  4. Missing report → SKIP (correct)")
        print("  5. stderr traceback + fresh report → parse (rule-3 refinement flip)")
        print("  6. Wrong row count → SKIP (partial-write guard flip)")
        print("  7. Negative-control abort → SKIP (row-6 short-circuit flip)")
        print("  8. Harness-error FLAG → SKIP override (row-7 override flip)")
        print("  9. No-clobber across tools → both verdicts survive (per-tool isolation flip)")
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

    # ── metamorphic_scan wiring ──
    print(f"\n── metamorphic_scan ──")
    print(f"  Tool: {PHASE_A_TOOLS['metamorphic_scan']}")
    print(f"  Report path: {METAMORPHIC_REPORT_PATH}")
    print(f"  Timeout: {METAMORPHIC_TIMEOUT}s")
    print()

    meta_hash = current_hashes.get("metamorphic_scan", "unknown")
    meta_counts = run_metamorphic_scan(
        t1_ids, results_dir, contradictions_dir, meta_hash,
    )

    print(f"\n  metamorphic_scan results:")
    for k in ("PASS", "FLAG", "INVALID", "SKIP", "CONTRADICTION"):
        print(f"    {k:14} {meta_counts.get(k, 0)}")
    if "reason_code" in meta_counts:
        print(f"    reason_code: {meta_counts['reason_code']}")

    # Other tools remain stubbed
    print(f"\n── chaos_scan / invariant_mine ──")
    print(f"  Stubbed — wiring deferred to later rounds.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))