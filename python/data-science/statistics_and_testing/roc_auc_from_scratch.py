"""
ROC Curve and AUC Computation

Core idea: For binary classification with probabilistic predictions, compute TPR (recall)
and FPR at various thresholds to build the ROC curve. AUC is the area under this curve,
computed via the Mann-Whitney U statistic (equivalent to the probability that a random
positive scores higher than a random negative).

When to use: Evaluate classifier quality across all decision thresholds, especially for
imbalanced data where AUC is more informative than accuracy.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple


def roc_curve_points(y_true: List[int], y_scores: List[float]) -> List[Tuple[float, float]]:
    """
    Compute ROC curve points (FPR, TPR) at various thresholds.

    Args:
        y_true: True binary labels (0 or 1).
        y_scores: Predicted scores/probabilities (higher = more likely positive).

    Returns:
        List of (FPR, TPR) tuples, sorted by threshold (descending).
    """
    # Pair scores with labels and sort by score (descending)
    paired = [(y_scores[i], y_true[i]) for i in range(len(y_true))]
    paired.sort(reverse=True, key=lambda x: x[0])

    # Count positives and negatives
    n_pos = sum(y_true)
    n_neg = len(y_true) - n_pos

    if n_pos == 0 or n_neg == 0:
        return [(0, 0), (1, 1)]  # Degenerate case

    roc_points = [(0, 0)]  # Start at origin
    tp = 0
    fp = 0

    for score, label in paired:
        if label == 1:
            tp += 1
        else:
            fp += 1

        tpr = tp / n_pos
        fpr = fp / n_neg
        roc_points.append((fpr, tpr))

    return roc_points


def auc_from_ranks(y_true: List[int], y_scores: List[float]) -> float:
    """
    Compute AUC using Mann-Whitney U statistic.

    AUC = P(score(positive) > score(negative))
    Count pairs (pos, neg) where pos_score > neg_score, divide by total pairs.

    Args:
        y_true: True binary labels (0 or 1).
        y_scores: Predicted scores.

    Returns:
        AUC (0 to 1).
    """
    n_pos = sum(y_true)
    n_neg = len(y_true) - n_pos

    if n_pos == 0 or n_neg == 0:
        return 0.5  # Degenerate case

    # Count concordant pairs: pos_score > neg_score
    concordant = 0
    for i in range(len(y_true)):
        for j in range(len(y_true)):
            if y_true[i] == 1 and y_true[j] == 0:
                if y_scores[i] > y_scores[j]:
                    concordant += 1

    auc = concordant / (n_pos * n_neg)
    return auc


def auc_trapezoid(roc_points: List[Tuple[float, float]]) -> float:
    """
    Compute AUC as area under the ROC curve using trapezoid rule.

    Args:
        roc_points: List of (FPR, TPR) tuples.

    Returns:
        AUC (0 to 1).
    """
    if len(roc_points) < 2:
        return 0.0

    auc = 0.0
    for i in range(1, len(roc_points)):
        fpr_prev, tpr_prev = roc_points[i - 1]
        fpr_curr, tpr_curr = roc_points[i]

        # Trapezoid area: average height * width
        auc += (tpr_prev + tpr_curr) / 2 * (fpr_curr - fpr_prev)

    return auc


if __name__ == "__main__":
    # Scenario 1: Perfect separation (AUC = 1.0)
    y_true_perfect = [0, 0, 0, 1, 1, 1]
    y_scores_perfect = [0.1, 0.2, 0.3, 0.8, 0.9, 1.0]
    auc_perfect_rank = auc_from_ranks(y_true_perfect, y_scores_perfect)
    roc_perfect = roc_curve_points(y_true_perfect, y_scores_perfect)
    auc_perfect_trap = auc_trapezoid(roc_perfect)
    print(f"Perfect case: AUC (rank)={auc_perfect_rank:.3f}, AUC (trapezoid)={auc_perfect_trap:.3f}")
    assert abs(auc_perfect_rank - 1.0) < 0.01, "Perfect separation should have AUC ≈ 1"
    assert abs(auc_perfect_trap - 1.0) < 0.01, "Perfect separation should have AUC ≈ 1"

    # Scenario 2: Weak signal (AUC moderate)
    y_true_weak = [0, 1, 0, 1, 0, 1, 1, 0]
    y_scores_weak = [0.3, 0.4, 0.35, 0.6, 0.2, 0.65, 0.55, 0.5]
    auc_weak_rank = auc_from_ranks(y_true_weak, y_scores_weak)
    roc_weak = roc_curve_points(y_true_weak, y_scores_weak)
    auc_weak_trap = auc_trapezoid(roc_weak)
    print(f"Weak case: AUC (rank)={auc_weak_rank:.3f}, AUC (trapezoid)={auc_weak_trap:.3f}")
    assert 0.4 < auc_weak_rank < 1.0, "Weak signal should have moderate AUC"
    assert 0.4 < auc_weak_trap < 1.0, "Weak signal should have moderate AUC"

    # Scenario 3: Strong signal (AUC > 0.8)
    y_true_strong = [0, 0, 0, 1, 1, 1, 0, 1]
    y_scores_strong = [0.2, 0.1, 0.3, 0.9, 0.8, 0.85, 0.35, 0.7]
    auc_strong_rank = auc_from_ranks(y_true_strong, y_scores_strong)
    roc_strong = roc_curve_points(y_true_strong, y_scores_strong)
    auc_strong_trap = auc_trapezoid(roc_strong)
    print(f"Strong case: AUC (rank)={auc_strong_rank:.3f}, AUC (trapezoid)={auc_strong_trap:.3f}")
    assert 0.75 <= auc_strong_rank <= 1.0, "Strong signal should have AUC >= 0.75"
    assert 0.75 <= auc_strong_trap <= 1.0, "Strong signal should have AUC >= 0.75"

    print("✓ ROC/AUC PASSED")
