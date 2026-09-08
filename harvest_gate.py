#!/usr/bin/env python3
"""harvest_gate.py — Phase A observation-mode runner over the T1 population.

Reads .harvest/t1_manifest.json (static snapshot from t1_detect_v2, Step 1 close).
For each T1 pattern, checks which Phase A tools cover it, and (in --run mode) invokes
them. Writes per-pattern results to .harvest/results/<date>/<pid>.json.

INVARIANTS (Draft 1 v2 + Illia's D1 call 2026-09-07):
  1. NEVER mutates the signed library tree.
  2. NEVER auto-flips a frozen exam verdict — contradictions log to .harvest/contradictions/.
  3. Harvest tools are IMPORTED from ~/ai-lab/pattern-scoring/validator/ (staging),
     NOT vendored into the library. Their sha256 is recorded in every result.
  4. FAIL HARD on tool-hash mismatch vs .harvest/tool_hashes.json (no silent staleness).
  5. Twin_divergence is EXPLICITLY OMITTED here — held for Draft 2 (needs trusted reference).

Modes:
  --dry-run  (default) — print T1 count, per-tool coverage, would-run pairs. No writes.
  --run                — invoke tools, write results + contradictions + tool_hashes.json.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

LIB = Path(__file__).resolve().parent
HARVEST = LIB / ".harvest"
MANIFEST = HARVEST / "t1_manifest.json"
TOOL_HASHES = HARVEST / "tool_hashes.json"
STAGING = Path.home() / "ai-lab/pattern-scoring/validator"

# Phase A tools (twin_divergence explicitly held for Draft 2)
PHASE_A_TOOLS = {
    "metamorphic_scan": STAGING / "metamorphic_scan.py",
    "chaos_scan":       STAGING / "chaos_scan.py",
    "invariant_mine":   STAGING / "invariant_mine.py",
    "nan_domain_probe": STAGING / "nan_domain_probe.py",
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_manifest() -> dict:
    if not MANIFEST.is_file():
        sys.exit(f"FATAL: {MANIFEST} missing. Run t1_detect_v2.py + regenerate manifest first.")
    return json.loads(MANIFEST.read_text())


# Per-tool coverage mappings.
# Kept HERE in the library repo (not in staging tools) so the library owns the
# "what patterns are covered" question. tool_hashes.json is the drift detector —
# a mismatch means somebody edited a target-declaring function; re-verify the
# mapping. Each tool has its own disclosure style; we adapt per tool.

# chaos_scan.py: hardcoded `chaos_<name>` functions map to library pattern IDs.
# The mapping is not implicit — some names abbreviate (chaos_wal -> write_ahead_log).
# Keep this table in sync with `grep -oE '^def chaos_\w+' chaos_scan.py`.
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

# invariant_mine.py: hardcoded `_gen_<name>` adapter functions define coverage.
INVARIANT_ADAPTER_TO_PID = {
    "_gen_linreg": "linear_regression_gd",
    "_gen_ridge":  "ridge_regression_normal_eq",
    "_gen_poly":   "polynomial_regression",
}


def resolve_tool_coverage(tool_name: str, tool_path: Path) -> tuple[set[str], str]:
    """Return (named-target coverage set, style).

    Style is one of:
      - "name-dict"    : tool declares PATTERNS = {"pid": (...)} (metamorphic_scan)
      - "function-map" : chaos_scan-style, mapped via CHAOS_FUNCTION_TO_PID
      - "adapter-map"  : invariant_mine-style, mapped via INVARIANT_ADAPTER_TO_PID
      - "universal"    : nan_domain_probe — no named targets, driven by CLI arg
      - "unknown"      : no coverage disclosure found
    """
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
        return set(), "universal"  # applies to any pattern via CLI arg

    return set(), "unknown"


def check_tool_hashes(current: dict[str, str]) -> tuple[bool, list[str]]:
    """Compare current tool hashes to recorded ones. Returns (ok, mismatches)."""
    if not TOOL_HASHES.is_file():
        return True, []  # first run — will be written below
    recorded = json.loads(TOOL_HASHES.read_text())
    mismatches = []
    for tool, h in current.items():
        if tool in recorded and recorded[tool] != h:
            mismatches.append(f"{tool}: recorded={recorded[tool][:12]} current={h[:12]}")
    return not mismatches, mismatches


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true", help="actually invoke tools (default: dry-run)")
    args = ap.parse_args(argv[1:])

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

    # Coverage report — split named-target coverage from universal-probe applicability.
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

    # Actual tool invocation is deferred to a subsequent commit — this commit
    # only lands the runner + coverage report. Invocation wiring per-tool needs
    # careful subprocess handling (executor.py / compiled_harness.py boundaries)
    # and belongs in its own review cycle.
    print("\nTool invocation not yet wired — scaffolding commit only.")
    print("Next commit: per-tool subprocess wiring under two-seat review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
