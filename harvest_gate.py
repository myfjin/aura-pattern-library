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


def resolve_tool_coverage(tool_path: Path) -> set[str]:
    """Return the set of pattern IDs a tool covers by name.

    Uses lightweight introspection: read the tool's text and grep for the PATTERNS
    dict or targets list. If a tool doesn't declare an explicit coverage set,
    returns an empty set — the runner will not invoke it in Phase A.
    """
    if not tool_path.is_file():
        return set()
    text = tool_path.read_text(encoding="utf-8", errors="ignore")
    ids = set()
    # metamorphic_scan.py: PATTERNS = { "pid": (cat, relpath), ... }
    import re
    for m in re.finditer(r'^\s*"([a-z0-9_]+)"\s*:\s*\(', text, re.MULTILINE):
        ids.add(m.group(1))
    return ids


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

    # Hash current tools
    current_hashes = {}
    coverage: dict[str, set[str]] = {}
    for tool_name, tool_path in PHASE_A_TOOLS.items():
        if not tool_path.is_file():
            print(f"  {tool_name}: NOT FOUND at {tool_path} — skipped")
            coverage[tool_name] = set()
            continue
        current_hashes[tool_name] = sha256_file(tool_path)
        coverage[tool_name] = resolve_tool_coverage(tool_path)

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
    would_run = 0
    covered_pids: set[str] = set()
    for tool_name, cov in coverage.items():
        applicable = cov & t1_set
        would_run += len(applicable)
        covered_pids |= applicable
        print(f"  {tool_name:20} covers {len(cov):3} patterns · applicable to T1: {len(applicable)}")

    print(f"\nT1 patterns covered by at least one Phase A tool: {len(covered_pids)}")
    print(f"T1 gap (no Phase A coverage today): {len(t1_set - covered_pids)}")
    print(f"Would-run pattern-tool pairs: {would_run}")

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
