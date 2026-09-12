"""Runner for metamorphic relation checks."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any, List, Tuple

from .relations import RelationResult, evaluate_relations, registry

REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"


def load_module(path: str, module_name: str = "user_impl") -> Any:
    p = Path(path)
    if not p.is_absolute():
        p = Path.cwd() / p
    p = p.resolve()
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")
    spec = importlib.util.spec_from_file_location(module_name, str(p))
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {p}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _category_for_pattern(pattern: str) -> str:
    if pattern in {
        "linear_regression_gd",
        "polynomial_regression",
        "ridge_regression_normal_eq",
    }:
        return "regression"
    if pattern in {
        "logistic_regression",
        "knn_classifier",
        "decision_tree_id3",
        "naive_bayes_text",
        "perceptron",
    }:
        return "classification"
    if pattern == "kmeans_clustering":
        return "clustering"
    if pattern == "gradient_descent_momentum":
        return "optimization"
    return "unknown"


def run_metamorphic(user_file: Path, pattern: str) -> Tuple[str, List[RelationResult], str]:
    """Run metamorphic relations for a pattern against a user file.

    Returns (verdict, results, summary). Verdict is RELATION-PASS, RELATION-FAIL,
    UNSUPPORTED, or ERROR.
    """
    category = _category_for_pattern(pattern)
    if category == "unknown":
        return "UNSUPPORTED", [], f"No metamorphic relations for pattern {pattern}"

    relations = registry().get(category, [])
    if not relations:
        return "UNSUPPORTED", [], f"No relations registered for category {category}"

    try:
        mod = load_module(str(user_file))
        results = evaluate_relations(category, mod, pattern=pattern)
    except Exception as exc:
        return "ERROR", [], f"{type(exc).__name__}: {exc}"

    failed = [r for r in results if not r.passed]
    if failed:
        summary = f"{len(failed)}/{len(results)} relations failed; first: {failed[0].name}"
        return "RELATION-FAIL", results, summary
    return "RELATION-PASS", results, f"All {len(results)} relations passed"


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: python3 -m metamorphic.runner <user_file.py> <pattern>", file=sys.stderr)
        return 2
    user_file = Path(sys.argv[1])
    pattern = sys.argv[2]
    verdict, results, summary = run_metamorphic(user_file, pattern)
    print(f"{verdict}: {pattern}")
    print(f"  file: {user_file}")
    print(f"  summary: {summary}")
    if results:
        print("  relations:")
        for r in results:
            mark = "PASS" if r.passed else "FAIL"
            print(f"    {r.name:40} {mark:4} {r.reason}")
    return 0 if verdict == "RELATION-PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
