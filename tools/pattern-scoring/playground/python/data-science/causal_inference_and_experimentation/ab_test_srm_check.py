"""
Sample Ratio Mismatch (SRM) Check for A/B Tests.

In a valid A/B test, the allocation ratio should match the design (e.g., 50/50).
A chi-square test on the observed counts detects when sample ratio deviates significantly.
SRM flags data quality issues (e.g., bugs, bot filtering).
We plant an SRM (skewed split) and a clean split; SRM caught vs clean passes.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import Tuple


def chi_square_gof(observed: list, expected: list) -> Tuple[float, float]:
    """
    Chi-square goodness-of-fit test.
    Returns (chi_sq_stat, p_value_approx).
    Uses chi-sq ≈ N(0, 1) for large N.
    """
    chi_sq = sum((o - e) ** 2 / e for o, e in zip(observed, expected))
    # Approximate p-value using chi-sq(1) critical value (3.84 for α=0.05)
    # For simplicity: return whether chi_sq > 3.84
    return chi_sq, 1.0 if chi_sq < 3.84 else 0.0


if __name__ == "__main__":
    random.seed(42)

    target_n = 10000
    target_ratio = 0.5  # 50/50 split

    # Scenario 1: Clean split (no SRM)
    # Assign treatment/control uniformly
    clean_split = [1 if random.random() < target_ratio else 0
                   for _ in range(target_n)]
    n_treatment_clean = sum(clean_split)
    n_control_clean = target_n - n_treatment_clean

    # Scenario 2: Skewed split (SRM present)
    # Artificially skew the allocation (simulate bug that filters out some control)
    skewed_split = [1 if random.random() < target_ratio else 0
                    for _ in range(target_n)]
    # Artificially remove ~20% of control units
    skewed_split = [
        x if x == 1 or random.random() > 0.2 else -1
        for x in skewed_split
    ]
    skewed_split = [x for x in skewed_split if x != -1]
    n_treatment_skewed = sum(skewed_split)
    n_control_skewed = len(skewed_split) - n_treatment_skewed

    # Chi-square test for both scenarios
    expected_clean = [target_n / 2, target_n / 2]
    observed_clean = [n_treatment_clean, n_control_clean]
    chi_sq_clean, p_clean = chi_square_gof(observed_clean, expected_clean)

    expected_skewed = [len(skewed_split) / 2, len(skewed_split) / 2]
    observed_skewed = [n_treatment_skewed, n_control_skewed]
    chi_sq_skewed, p_skewed = chi_square_gof(observed_skewed, expected_skewed)

    # Assertions
    assert p_clean > 0.05, "Clean split should NOT be flagged as SRM"
    assert p_skewed < 0.05, "Skewed split SHOULD be flagged as SRM"
    assert chi_sq_clean < 3.84, f"Clean chi-sq {chi_sq_clean:.2f} should be low"
    assert chi_sq_skewed > 3.84, f"Skewed chi-sq {chi_sq_skewed:.2f} should be high"

    ratio_clean = n_treatment_clean / target_n
    ratio_skewed = n_treatment_skewed / len(skewed_split)

    print(
        f"Clean split: {n_treatment_clean}/{target_n} ({ratio_clean:.1%}) | "
        f"chi_sq={chi_sq_clean:.2f} (p={p_clean:.2f}) | "
        f"Skewed split: {n_treatment_skewed}/{len(skewed_split)} ({ratio_skewed:.1%}) | "
        f"chi_sq={chi_sq_skewed:.2f} (p={p_skewed:.2f}) | PASS"
    )
