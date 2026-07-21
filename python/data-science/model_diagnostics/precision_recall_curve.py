import math
"""
Precision-Recall Curve & Average Precision

Computes PR curve by varying decision threshold on predicted scores.
Average Precision (AP) summarizes the curve as area under the PR curve.

Use this to evaluate binary classifiers, especially on imbalanced datasets where
PR curve is more informative than ROC curve.
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

def _aura_validate_compute_pr_curve(n_points):
    v = []
    if isinstance(n_points, (int, float)) and n_points <= 0:
        v.append(f"AURA-E009: n_points must be > 0, got {n_points}")
    if v:
        raise AuraInputError(v)

def _aura_validate_generate_scored_labels(n_positive, n_negative, noise):
    v = []
    if isinstance(n_positive, (int, float)) and n_positive <= 0:
        v.append(f"AURA-E009: n_positive must be > 0, got {n_positive}")
    if isinstance(n_negative, (int, float)) and n_negative <= 0:
        v.append(f"AURA-E009: n_negative must be > 0, got {n_negative}")
    if isinstance(noise, (int, float)) and not math.isfinite(noise):
        v.append(f"AURA-E008: noise must be finite, got {noise}")
    if isinstance(noise, (int, float)) and noise <= 0:
        v.append(f"AURA-E009: noise must be > 0, got {noise}")
    if v:
        raise AuraInputError(v)

def generate_scored_labels(
    n_positive: int, n_negative: int, noise: float, seed: int
) -> List[Tuple[float, int]]:
    """
    Generate predicted scores and true labels.
    Positive labels have higher scores; noise controls overlap.
    """
    _aura_validate_generate_scored_labels(n_positive, n_negative, noise)
    random.seed(seed)
    data = []

    # Positive class: scores centered at 0.7
    for _ in range(n_positive):
        score = 0.7 + random.gauss(0, noise)
        score = max(0, min(1, score))
        data.append((score, 1))

    # Negative class: scores centered at 0.3
    for _ in range(n_negative):
        score = 0.3 + random.gauss(0, noise)
        score = max(0, min(1, score))
        data.append((score, 0))

    return data


def compute_pr_curve(
    scores: List[float], labels: List[int], n_points: int = 100
) -> Tuple[List[float], List[float], List[float]]:
    """
    Compute precision-recall curve by varying threshold.
    Returns (thresholds, precisions, recalls).
    """
    _aura_validate_compute_pr_curve(n_points)
    # Sort by score descending
    scored_labels = sorted(zip(scores, labels), key=lambda x: -x[0])
    scores_sorted = [s for s, l in scored_labels]
    labels_sorted = [l for s, l in scored_labels]

    n_pos = sum(labels_sorted)
    n = len(labels_sorted)

    thresholds = [1.0] + sorted(set(scores_sorted)) + [0.0]
    thresholds = sorted(set(thresholds), reverse=True)[:n_points]

    precisions = []
    recalls = []
    threshold_list = []

    for threshold in thresholds:
        # Predict 1 if score >= threshold
        pred_pos = sum(1 for s in scores_sorted if s >= threshold)

        if pred_pos == 0:
            precision = 0.0
        else:
            tp = sum(1 for s, l in zip(scores_sorted, labels_sorted) if s >= threshold and l == 1)
            precision = tp / pred_pos

        recall = sum(1 for s, l in zip(scores_sorted, labels_sorted) if s >= threshold and l == 1) / n_pos if n_pos > 0 else 0.0

        precisions.append(precision)
        recalls.append(recall)
        threshold_list.append(threshold)

    return threshold_list, precisions, recalls


def average_precision(recalls: List[float], precisions: List[float]) -> float:
    """
    Compute average precision using trapezoidal rule.
    """
    if len(recalls) == 0 or len(precisions) == 0:
        return 0.0

    # Sort by recall
    rp_pairs = sorted(zip(recalls, precisions))
    recalls_sorted = [r for r, p in rp_pairs]
    precisions_sorted = [p for r, p in rp_pairs]

    ap = 0.0
    for i in range(1, len(recalls_sorted)):
        dr = recalls_sorted[i] - recalls_sorted[i - 1]
        p_avg = (precisions_sorted[i] + precisions_sorted[i - 1]) / 2
        ap += dr * p_avg

    return ap


def test_precision_recall() -> None:
    """
    Test PR curve: strong classifier should have high AP, random should have AP near base rate.
    """
    random.seed(42)

    # Strong classifier (well-separated classes)
    data_strong = generate_scored_labels(50, 50, noise=0.1, seed=42)
    scores_strong = [s for s, l in data_strong]
    labels_strong = [l for s, l in data_strong]

    _, prec_strong, recall_strong = compute_pr_curve(scores_strong, labels_strong)
    ap_strong = average_precision(recall_strong, prec_strong)

    # Weak classifier (random noise)
    random.seed(42)
    data_weak = [(random.random(), random.choice([0, 1])) for _ in range(100)]
    scores_weak = [s for s, l in data_weak]
    labels_weak = [l for s, l in data_weak]

    _, prec_weak, recall_weak = compute_pr_curve(scores_weak, labels_weak)
    ap_weak = average_precision(recall_weak, prec_weak)

    # Verify: strong classifier should have much higher AP
    assert ap_strong > 0.8, f"Strong classifier AP should be high: {ap_strong}"
    assert ap_weak < 0.6, f"Weak classifier AP should be lower: {ap_weak}"
    assert ap_strong > ap_weak, f"Strong AP should exceed weak: {ap_strong} vs {ap_weak}"

    print("precision_recall_curve.py: PASS")


if __name__ == "__main__":
    test_precision_recall()
