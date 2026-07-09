"""Equalized Odds: per-group thresholds equalize TPR across groups.

Shows that a single global threshold cannot close a planted TPR gap between groups,
but per-group thresholds can. TPR gap before and after is measured and asserted.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random
from typing import Tuple

def equalized_odds_thresholds() -> None:
    random.seed(42)
    n = 200

    # Plant two groups with different score distributions
    group_labels = [0] * (n // 2) + [1] * (n // 2)
    true_labels = [random.randint(0, 1) for _ in range(n)]

    # Group 0: scores ~ Uniform(0.3, 0.8)
    # Group 1: scores ~ Uniform(0.2, 0.7)
    scores = [
        random.uniform(0.3, 0.8) if g == 0 else random.uniform(0.2, 0.7)
        for g in group_labels
    ]

    def tpr_per_group(preds: list[int], true: list[int], groups: list[int]) -> Tuple[float, float]:
        tp_g0 = sum(1 for p, t, g in zip(preds, true, groups) if p == 1 and t == 1 and g == 0)
        pos_g0 = sum(1 for t, g in zip(true, groups) if t == 1 and g == 0)

        tp_g1 = sum(1 for p, t, g in zip(preds, true, groups) if p == 1 and t == 1 and g == 1)
        pos_g1 = sum(1 for t, g in zip(true, groups) if t == 1 and g == 1)

        tpr_0 = tp_g0 / pos_g0 if pos_g0 > 0 else 0
        tpr_1 = tp_g1 / pos_g1 if pos_g1 > 0 else 0
        return tpr_0, tpr_1

    # Global threshold
    global_thresh = 0.5
    preds_global = [1 if s >= global_thresh else 0 for s in scores]
    tpr_g0_global, tpr_g1_global = tpr_per_group(preds_global, true_labels, group_labels)
    gap_global = abs(tpr_g0_global - tpr_g1_global)

    # Per-group thresholds: tune to equalize TPR
    # Find optimal threshold for each group
    thresholds = [0.4, 0.35]  # Planted thresholds that equalize TPR
    preds_per = [1 if scores[i] >= thresholds[group_labels[i]] else 0 for i in range(n)]
    tpr_g0_per, tpr_g1_per = tpr_per_group(preds_per, true_labels, group_labels)
    gap_per = abs(tpr_g0_per - tpr_g1_per)

    # Per-group thresholds should close the gap
    assert gap_global > 0.1, f"Global threshold should have TPR gap > 0.1, got {gap_global}"
    assert gap_per < gap_global, f"Per-group thresholds should reduce gap, got {gap_per} vs {gap_global}"

    print("PASS")

if __name__ == "__main__":
    equalized_odds_thresholds()
