#!/usr/bin/env python3
"""
metamorphic_scan.py — FOLD 3: metamorphic relations as a behavioral oracle (the unit/dimension-
scaling oracle generalized). Adapted from forge-gate/tools/metamorphic/ (inherited, NOT merged —
tools stay separate). Forge runs these relations against USER code for a PASS/FAIL; we re-aim the
SAME relations at OUR signed library oracles to ask: does each pattern obey its metamorphic laws?

A metamorphic relation is a (transform, comparator) pair that needs no ground-truth output — only
that a KNOWN input transform produces a KNOWN output relation. Examples (inherited):
  regression:  scale all targets by k  -> predictions scale by k;  shift by c -> shift by c;
               permute feature columns -> predictions invariant.
  classification: permute labels -> predictions permute the same way; duplicate rows -> invariant;
               noise feature -> invariant; clean-separable data -> perfect separation.
  clustering:  shift/scale/duplicate invariance of assignments.

This catches what a single fixed-input check misses: an oracle can be right on one input yet violate
the scaling/permutation LAW (validation-theater that memorized a case). It's a positive oracle of
kind 'metamorphic'.

Verdict-ladder mapping:
  all relations PASS  -> the pattern earns metamorphic positive-oracle coverage (adds to oracle_coverage)
  a relation FAILs    -> INVALID candidate (the pattern violates a behavioral law) -> evidence card,
                         routed to calibration. Per the fold law it may NOT auto-flip a FROZEN exam
                         verdict: a metamorphic FAIL that contradicts a frozen PASS means the RELATION
                         is miscalibrated (tolerance/seed), not the ruler — investigate, never overfit.

Observation-only: relations read the signed oracle's behavior; the library is never mutated and the
exam grader is never touched.
"""
from __future__ import annotations
import importlib.util, json, os, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIB = Path(os.path.expanduser("~/aura-pattern-library"))
sys.path.insert(0, str(HERE / "inherited_forge_code"))
from metamorphic.relations import evaluate_relations  # noqa: E402  (inherited, unmodified)


# pattern -> (category, oracle relpath). All function names verified present in our signed library.
PATTERNS = {
    "linear_regression_gd":       ("regression",     "python/data-science/core_ml/linear_regression_gd.py"),
    "ridge_regression_normal_eq": ("regression",     "python/data-science/core_ml/ridge_regression_normal_eq.py"),
    "polynomial_regression":      ("regression",     "python/data-science/statistical_modeling/polynomial_regression.py"),
    "logistic_regression":        ("classification", "python/data-science/core_ml/logistic_regression.py"),
    "knn_classifier":             ("classification", "python/data-science/core_ml/knn_classifier.py"),
    "decision_tree_id3":          ("classification", "python/data-science/core_ml/decision_tree_id3.py"),
    "naive_bayes_text":           ("classification", "python/data-science/core_ml/naive_bayes_text.py"),
    "perceptron":                 ("classification", "python/data-science/core_ml/perceptron.py"),
    "kmeans_clustering":          ("clustering",     "python/data-science/core_ml/kmeans_clustering.py"),
}


def _load(relpath, name):
    spec = importlib.util.spec_from_file_location(name, str(LIB / relpath))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def _card(pattern, relpath, failed, total):
    if failed:
        return {"pattern": relpath, "technique": "metamorphic-relations", "severity": "high",
                "class": "metamorphic-law-violation",
                "fixture": f"metamorphic relations for {pattern}",
                "expected": "known input transform -> known output relation (scale/shift/permute/duplicate)",
                "actual": f"{len(failed)}/{total} relations FAILED: {[r.name for r in failed]}",
                "why": "the oracle violates a behavioral law a single fixed input can't expose (possible theater)",
                "verdict": "INVALID-CANDIDATE", "verdict_target": "PATTERN",
                "note": "MUST NOT auto-flip a frozen exam verdict; a contradiction means the RELATION is miscalibrated",
                "confidence": "high", "repro_cmd": f"python3 metamorphic_scan.py {pattern}",
                "oracle_coverage_kind": "metamorphic", "detail": [r.reason for r in failed]}
    return {"pattern": relpath, "technique": "metamorphic-relations", "severity": "info",
            "class": "metamorphic-coverage", "fixture": f"metamorphic relations for {pattern}",
            "expected": "all behavioral laws hold", "actual": f"{total}/{total} relations passed",
            "why": "pattern obeys its scaling/shift/permutation/duplicate laws -> metamorphic positive oracle",
            "verdict": "PASS", "verdict_target": "PATTERN", "confidence": "high",
            "repro_cmd": f"python3 metamorphic_scan.py {pattern}", "oracle_coverage_kind": "metamorphic"}


def scan(patterns, verbose=True):
    cards = []
    for pattern in patterns:
        category, relpath = PATTERNS[pattern]
        try:
            mod = _load(relpath, f"mm_{pattern}")
            results = evaluate_relations(category, mod, pattern=pattern)
        except Exception as exc:
            if verbose:
                print(f"  {pattern:30} ERROR {type(exc).__name__}: {exc}")
            cards.append({"pattern": relpath, "technique": "metamorphic-relations", "severity": "medium",
                          "class": "metamorphic-harness-error", "verdict": "FLAG",
                          "actual": f"{type(exc).__name__}: {exc}", "oracle_coverage_kind": "metamorphic"})
            continue
        failed = [r for r in results if not r.passed]
        status = "PASS" if not failed else f"FAIL {len(failed)}/{len(results)}"
        if verbose:
            print(f"  {pattern:30} {len(results)-len(failed)}/{len(results)} relations hold  [{status}]"
                  + (f"  VIOLATIONS: {[r.name for r in failed]}" if failed else ""))
        cards.append(_card(pattern, relpath, failed, len(results)))
    json.dump({"cards": cards}, open(HERE / "metamorphic_report.json", "w"), indent=1)
    return cards


def negative_control():
    """Test-of-the-test: a broken linreg that IGNORES y must fail the scale/shift laws. Proves the
    relations have teeth (not cosmetic) before we trust their all-PASS on the signed library."""
    import types
    m = types.ModuleType("broken_nc")
    m.linear_regression_gd = lambda X, y, lr, it: ([1.0, 1.0], 0.0)  # ignores y -> violates scale/shift
    res = evaluate_relations("regression", m, pattern="linear_regression_gd")
    fails = [r for r in res if not r.passed]
    ok = len(fails) >= 2  # scale_target + shift_target must catch it
    print(f"negative control: broken-linreg fails {len(fails)}/{len(res)} laws "
          f"-> {'DETECTION WORKS' if ok else 'COSMETIC (ABORT)'}")
    return ok


def main():
    pats = sys.argv[1:] or list(PATTERNS)
    print("METAMORPHIC RELATION ORACLE (fold 3) — do the signed oracles obey their behavioral laws?")
    print("=" * 92)
    if not negative_control():
        print("ABORT: metamorphic detection is cosmetic (negative control failed).")
        return 1
    print("-" * 92)
    cards = scan(pats)
    print("=" * 92)
    viol = [c for c in cards if c["verdict"] in ("INVALID-CANDIDATE", "FLAG")]
    passed = [c for c in cards if c["verdict"] == "PASS"]
    print(f"metamorphic PASS: {len(passed)}/{len(cards)} patterns · violations/flags: {len(viol)}")
    if viol:
        print("INVESTIGATE (relation miscalibration vs real law-violation):",
              [c["pattern"].split("/")[-1] for c in viol])
    return 0


if __name__ == "__main__":
    sys.exit(main())
