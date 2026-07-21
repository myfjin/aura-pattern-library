import math
"""
Threshold Tuning with Asymmetric Misclassification Costs

Core idea: Binary classifiers typically use 0.5 threshold, but with asymmetric costs
(e.g., false negatives cost more than false positives), the optimal threshold shifts.

When to use: Fraud detection (missing fraud = high cost) or spam filtering (blocking users = high cost)
where misclassification costs are unequal.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_compute_total_cost(threshold, cost_fp, cost_fn):
    v = []
    if isinstance(threshold, (int, float)) and not math.isfinite(threshold):
        v.append(f"AURA-E008: threshold must be finite, got {threshold}")
    if isinstance(cost_fp, (int, float)) and not math.isfinite(cost_fp):
        v.append(f"AURA-E008: cost_fp must be finite, got {cost_fp}")
    if isinstance(cost_fn, (int, float)) and not math.isfinite(cost_fn):
        v.append(f"AURA-E008: cost_fn must be finite, got {cost_fn}")
    if isinstance(cost_fn, (int, float)) and cost_fn <= 0:
        v.append(f"AURA-E009: cost_fn must be > 0, got {cost_fn}")
    if v:
        raise AuraInputError(v)

def _aura_validate_find_optimal_threshold(cost_fp, cost_fn, grid_size):
    v = []
    if isinstance(cost_fp, (int, float)) and not math.isfinite(cost_fp):
        v.append(f"AURA-E008: cost_fp must be finite, got {cost_fp}")
    if isinstance(cost_fn, (int, float)) and not math.isfinite(cost_fn):
        v.append(f"AURA-E008: cost_fn must be finite, got {cost_fn}")
    if isinstance(cost_fn, (int, float)) and cost_fn <= 0:
        v.append(f"AURA-E009: cost_fn must be > 0, got {cost_fn}")
    if isinstance(grid_size, (int, float)) and grid_size <= 0:
        v.append(f"AURA-E009: grid_size must be > 0, got {grid_size}")
    if v:
        raise AuraInputError(v)

def compute_total_cost(
    y_true: List[float],
    y_scores: List[float],
    threshold: float,
    cost_fp: float = 1.0,
    cost_fn: float = 5.0
) -> float:
    """
    Compute total cost given a threshold, where:
    cost_fp: cost of false positive
    cost_fn: cost of false negative
    """
    _aura_validate_compute_total_cost(threshold, cost_fp, cost_fn)
    total_cost = 0.0
    for y, score in zip(y_true, y_scores):
        pred = 1 if score >= threshold else 0

        if pred == 1 and y == 0:
            total_cost += cost_fp
        elif pred == 0 and y == 1:
            total_cost += cost_fn

    return total_cost


def find_optimal_threshold(
    y_true: List[float],
    y_scores: List[float],
    cost_fp: float = 1.0,
    cost_fn: float = 5.0,
    grid_size: int = 100
) -> Tuple[float, float]:
    """
    Grid search over thresholds to find minimum total cost.
    Returns (best_threshold, min_cost).
    """
    _aura_validate_find_optimal_threshold(cost_fp, cost_fn, grid_size)
    best_threshold = 0.0
    best_cost = compute_total_cost(y_true, y_scores, 0.0, cost_fp, cost_fn)

    for i in range(1, grid_size + 1):
        threshold = i / grid_size
        cost = compute_total_cost(y_true, y_scores, threshold, cost_fp, cost_fn)
        if cost < best_cost:
            best_cost = cost
            best_threshold = threshold

    return best_threshold, best_cost


if __name__ == "__main__":
    random.seed(42)

    # Generate synthetic binary classification data
    # Imbalanced: mostly negative class
    y_true = []
    y_scores = []

    for _ in range(200):
        # Generate labels (15% positive)
        label = 1 if random.random() < 0.15 else 0

        # Generate scores: positives concentrated near 0.8, negatives near 0.2
        if label == 1:
            score = random.gauss(0.75, 0.15)
        else:
            score = random.gauss(0.25, 0.15)

        y_true.append(label)
        y_scores.append(min(1.0, max(0.0, score)))

    # Cost of false negative (missing a positive) is 10x cost of false positive
    cost_fp = 1.0
    cost_fn = 10.0

    # Find optimal threshold
    opt_threshold, opt_cost = find_optimal_threshold(y_true, y_scores, cost_fp, cost_fn)

    # Cost at default threshold 0.5
    default_cost = compute_total_cost(y_true, y_scores, 0.5, cost_fp, cost_fn)

    print(f"Default threshold 0.5 cost: {default_cost:.1f}")
    print(f"Optimal threshold: {opt_threshold:.2f}, cost: {opt_cost:.1f}")
    print(f"Improvement: {(default_cost - opt_cost) / default_cost * 100:.1f}%")

    # Assertion: optimal threshold should beat default, and be < 0.5 (since FN is more costly)
    assert opt_cost < default_cost, f"Optimal should beat default: {opt_cost} vs {default_cost}"
    assert opt_threshold < 0.5, f"Threshold should shift down (FN cost > FP cost): {opt_threshold}"
    assert opt_cost < default_cost * 0.8, f"Should achieve meaningful cost reduction: {opt_cost} vs {default_cost}"

    print("✓ Threshold Tuning with Asymmetric Costs: PASS")
