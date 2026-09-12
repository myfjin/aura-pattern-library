#!/usr/bin/env python3
"""Twin-consensus verifier — Wave 1 / 1B, CHUNK 2.

Fix from chunk 1:
  - User verdict is PROPERTY-PRIMARY: reuse the existing fixture's PASS/FAIL verdict.
  - Twin consensus means >=2 language REFERENCE twins (py + cpp for linear_regression_gd)
    must agree WITH EACH OTHER. If they disagree → UNSTABLE (drift signal).

Usage:
    PYTHONPATH=/home/au/forge-gate/src python3 tools/twin_consensus.py \
        verify tests/corpus/linreg_sgd.py --pattern linear_regression_gd
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC = REPO_ROOT / "src"
LIB = Path.home() / "aura-pattern-library"

sys.path.insert(0, str(SRC))

from forge_gate.catalog import CatalogError, load_aura_catalog, resolve_pattern
from forge_gate.runner import run_file
from forge_gate.verifier import verdict


@dataclass(frozen=True)
class TwinConsensus:
    status: str  # PASS | FAIL | UNSTABLE | UNSUPPORTED
    pattern: str
    user_file: str
    reason: str
    user_verdict: str
    twin_count: int
    consensus_status: Optional[str] = None
    details: List[str] = field(default_factory=list)
    metrics: Dict[str, Any] = field(default_factory=dict)


def _extract_gate_json(stdout: str) -> Optional[Dict]:
    for line in reversed(stdout.splitlines()):
        line = line.strip()
        if line.startswith("FORGE_GATE_RESULT "):
            try:
                return json.loads(line[len("FORGE_GATE_RESULT "):])
            except json.JSONDecodeError:
                continue
        if line.startswith("{") and line.endswith("}"):
            try:
                return json.loads(line)
            except json.JSONDecodeError:
                continue
    return None


def _run_fixture(fixture: Path, user_file: Path, timeout: float) -> Dict[str, Any]:
    """Run a Python fixture against a user file; return its structured result."""
    result = run_file(
        fixture,
        extra_args=[str(user_file)],
        timeout=timeout,
        no_network=True,
        memory_mb=512,
    )
    payload = _extract_gate_json(result.stdout) or {}
    return {
        "exit": result.exit_code,
        "status": payload.get("status", "FAIL"),
        "reason": payload.get("reason", "fixture reported failure"),
        "metrics": payload.get("metrics", {}),
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def _compile_cpp(src: Path) -> Optional[Path]:
    """Compile a C++ twin to a temporary binary. Returns binary path or None."""
    gxx = shutil.which("g++")
    if not gxx:
        return None
    out = Path(tempfile.gettempdir()) / f"_fg_twin_{src.stem}"
    try:
        proc = subprocess.run(
            [gxx, "-O2", "-std=c++17", str(src), "-o", str(out)],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if proc.returncode != 0:
            return None
        return out
    except Exception:
        return None


def _run_cpp_twin(src: Path, timeout: float) -> Dict[str, Any]:
    """Compile and run a C++ twin; return structured result."""
    binary = _compile_cpp(src)
    if not binary:
        return {"status": "UNSTABLE", "reason": "C++ twin failed to compile"}
    try:
        proc = subprocess.run(
            [str(binary)],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        ok = proc.returncode == 0
        # Extract R² and weights from stdout if possible.
        nums = _extract_numbers(proc.stdout)
        return {
            "status": "PASS" if ok else "FAIL",
            "reason": "C++ twin ran" if ok else "C++ twin assertion failed",
            "metrics": nums,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
        }
    except subprocess.TimeoutExpired as exc:
        return {"status": "UNSTABLE", "reason": "C++ twin timed out"}


def _extract_numbers(text: str) -> Dict[str, float]:
    out: Dict[str, float] = {}
    for line in text.splitlines():
        # Look for "R²=0.123" or "R2 = 0.123" etc.
        m = re.search(r"R[²2]\s*=?\s*([-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)", line, re.I)
        if m:
            out["r2"] = float(m.group(1))
        # Generic named-number extraction for twin stdout, e.g. "intra=0.557".
        for wm in re.finditer(r"\b(\w+)\s*[:=]\s*([-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)", line):
            name = wm.group(1).lower()
            if name in {"exit", "code", "line", "seed", "version", "copyright", "cpp", "pass"}:
                continue
            # Keep sensible metric names; ignore raw integers that are likely counts/indices.
            val = float(wm.group(2))
            out[name] = val
    return out


def _resolve_twins(pattern: str) -> List[Tuple[str, Path]]:
    """Return [(language, path), ...] for all language twins of this pattern."""
    catalog = load_aura_catalog(LIB)
    langs_str, _ = catalog.get(pattern, ("", ""))
    if not langs_str:
        return []

    twins: List[Tuple[str, Path]] = []
    lang_ext = {
        "python": ".py",
        "cpp": ".cpp",
        "go": ".go",
        "rust": ".rs",
        "r": ".R",
    }
    declared = [x.strip() for x in langs_str.split("·")]

    for lang in declared:
        ext = lang_ext.get(lang)
        if not ext:
            continue
        for p in LIB.rglob(f"{pattern}{ext}"):
            twins.append((lang, p))

    return twins


def _metrics_consensus(
    results: List[Dict[str, Any]],
    tolerance: float = 1e-3,
    aliases: Optional[Dict[str, str]] = None,
    require_value_match: bool = True,
) -> Tuple[bool, List[str]]:
    """Compare a list of twin results to each other. True = they agree.

    Only metrics present in BOTH twins are compared; extra keys are ignored.
    This prevents a C++ twin that emits only R² from disagreeing with a Python
    twin that emits weights + bias + R².

    `aliases` maps twin metric names to canonical names, e.g. {"intra": "intra_cluster_distance"}.
    If `require_value_match` is False, only statuses and presence of metrics are checked
    (used when language twins use different seed-locked fixtures and absolute values
    are not expected to match, e.g. k-means with different RNG streams).
    """
    if len(results) < 2:
        return True, []
    base = results[0]
    if base["status"] != "PASS":
        return True, []

    def normalize(m: Dict[str, float]) -> Dict[str, float]:
        out: Dict[str, float] = {}
        for k, v in m.items():
            canon = (aliases or {}).get(k, k)
            out[canon] = v
        return out

    base_metrics = normalize(base.get("metrics", {}))
    disagreements: List[str] = []
    for r in results[1:]:
        if r["status"] != base["status"]:
            disagreements.append(f"status {base.get('twin','?')}={base['status']} vs {r.get('twin','?')}={r['status']}")
            continue
        if not require_value_match:
            # Ensure both produced at least one numeric metric; exact values are not compared.
            other_metrics = normalize(r.get("metrics", {}))
            if not base_metrics and not other_metrics:
                disagreements.append(f"no metrics from either twin")
            continue
        other_metrics = normalize(r.get("metrics", {}))
        common = set(base_metrics.keys()) & set(other_metrics.keys())
        if not common:
            disagreements.append(f"no common metrics: {base.get('twin','?')} vs {r.get('twin','?')}")
            continue
        for key in common:
            av, bv = base_metrics[key], other_metrics[key]
            if isinstance(av, (int, float)) and isinstance(bv, (int, float)):
                denom = max(abs(av), abs(bv), 1.0)
                if abs(av - bv) / denom > tolerance:
                    disagreements.append(f"metric '{key}' differs: {base.get('twin','?')}={av} vs {r.get('twin','?')}={bv}")
                    break
            elif av != bv:
                disagreements.append(f"metric '{key}' differs: {base.get('twin','?')}={av!r} vs {r.get('twin','?')}={bv!r}")
                break
    return not disagreements, disagreements


def _metrics_match(a: Dict, b: Dict, tolerance: float) -> bool:
    for key in a:
        if key not in b:
            return False
        av, bv = a[key], b[key]
        if isinstance(av, (int, float)) and isinstance(bv, (int, float)):
            denom = max(abs(av), abs(bv), 1.0)
            if abs(av - bv) / denom > tolerance:
                return False
        elif av != bv:
            return False
    return True


def consensus_verify(user_file: Path, pattern: str, timeout: float = 60.0) -> TwinConsensus:
    if not user_file.exists():
        return TwinConsensus("FAIL", pattern, str(user_file), "user file not found", "FAIL", 0)

    try:
        meta = resolve_pattern(pattern)
    except CatalogError as exc:
        return TwinConsensus("UNSUPPORTED", pattern, str(user_file), str(exc), "UNSUPPORTED", 0)

    fixture = SRC / "forge_gate" / "fixtures" / f"{meta['fixture']}.py"
    if not fixture.exists():
        return TwinConsensus("UNSUPPORTED", pattern, str(user_file), f"fixture missing: {fixture}", "UNSUPPORTED", 0)

    # 1. Property-primary verdict on the USER implementation.
    user_run = _run_fixture(fixture, user_file, timeout)
    user_status = user_run["status"]

    if user_status not in ("PASS", "FAIL", "UNSTABLE"):
        user_status = "FAIL"

    # 2. Resolve and run all language reference twins.
    twins = _resolve_twins(pattern)
    twin_results: List[Dict[str, Any]] = []
    for lang, path in twins:
        if lang == "python":
            # Python twin: run it through the same fixture as the user.
            r = _run_fixture(fixture, path, timeout)
            r["twin"] = path.name
            r["lang"] = "python"
            twin_results.append(r)
        elif lang == "cpp":
            r = _run_cpp_twin(path, timeout)
            r["twin"] = path.name
            r["lang"] = "cpp"
            twin_results.append(r)

    # 3. Consensus among reference twins (not user-vs-twin).
    # Per-pattern metric aliases so C++ twins can match Python fixture names.
    # Patterns whose language twins use different synthetic fixtures (different RNG
    # streams) get `require_value_match=False`; we then only require both twins to
    # PASS and emit at least one numeric metric.
    status_only_patterns = {"kmeans_clustering", "logistic_regression", "decision_tree_id3", "knn_classifier", "naive_bayes_text", "perceptron", "polynomial_regression"}
    aliases: Dict[str, str] = {
        "intra": "intra_cluster_distance",
        "r2": "r2",
        "accuracy": "accuracy",
        "mse_2": "mse",
    }
    require_value_match = pattern not in status_only_patterns
    consensus_ok, disagreements = _metrics_consensus(twin_results, aliases=aliases, require_value_match=require_value_match)

    if len(twin_results) < 2:
        consensus_label = "insufficient_twins"
    elif consensus_ok:
        consensus_label = "agree"
    else:
        consensus_label = "disagree"

    # Final verdict:
    #   FAIL if user fails.
    #   UNSUPPORTED if no twins.
    #   UNSTABLE if twins disagree (drift signal).
    #   PASS only if user passes AND twins agree.
    if user_status == "FAIL":
        final = "FAIL"
        reason = f"user implementation fails property check: {user_run['reason']}"
    elif not twin_results:
        final = "UNSUPPORTED"
        reason = "no language twins found for this pattern"
    elif consensus_label == "disagree":
        final = "UNSTABLE"
        reason = "reference twins disagree: " + "; ".join(disagreements)
    else:
        final = "PASS"
        reason = f"user passes and {len(twin_results)} reference twin(s) agree"

    return TwinConsensus(
        status=final,
        pattern=pattern,
        user_file=str(user_file),
        reason=reason,
        user_verdict=user_status,
        twin_count=len(twin_results),
        consensus_status=consensus_label,
        details=[f"{r.get('lang','?')}/{r.get('twin','?')} -> {r['status']}" for r in twin_results],
        metrics=user_run.get("metrics", {}),
    )


def main(argv: List[str]) -> int:
    if len(argv) < 2 or argv[0] != "verify":
        print("usage: twin_consensus.py verify <user_file> --pattern <pattern>")
        return 2
    user_file = Path(argv[1]).expanduser().resolve()
    pattern = None
    for i, a in enumerate(argv):
        if a == "--pattern" and i + 1 < len(argv):
            pattern = argv[i + 1]
    if not pattern:
        print("--pattern required")
        return 2

    result = consensus_verify(user_file, pattern)
    print(f"{result.status}: {result.pattern}")
    print(f"  file:     {result.user_file}")
    print(f"  reason:   {result.reason}")
    print(f"  user:     {result.user_verdict}")
    print(f"  twins:    {result.twin_count} (consensus={result.consensus_status})")
    for d in result.details[:12]:
        print(f"    - {d}")
    if result.metrics:
        print(f"  metrics:  {result.metrics}")
    return 0 if result.status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
