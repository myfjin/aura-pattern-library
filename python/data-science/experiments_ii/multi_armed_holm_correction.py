"""Holm correction (step-down Bonferroni) for multiple comparisons.

Many variants of a treatment tested; uncorrected testing breaks FWER over replications.
Holm correction controls FWER; trades power for false-positive control.
Core claim: uncorrected breaks FWER; Holm holds it.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import List

def bonferroni_threshold(alpha: float, num_tests: int) -> float:
    """Bonferroni-corrected α."""
    return alpha / num_tests

def holm_thresholds(alpha: float, num_tests: int) -> List[float]:
    """Holm step-down thresholds: α/(m), α/(m-1), ..., α/1."""
    return [alpha / (num_tests - i) for i in range(num_tests)]

def run_multiple_tests(p_values: List[float], method: str = "uncorrected") -> List[bool]:
    """Apply multiple testing correction and return rejections."""
    m = len(p_values)

    if method == "uncorrected":
        threshold = 0.05
        return [p < threshold for p in p_values]

    elif method == "bonferroni":
        threshold = bonferroni_threshold(0.05, m)
        return [p < threshold for p in p_values]

    elif method == "holm":
        thresholds = holm_thresholds(0.05, m)
        sorted_idx = sorted(range(m), key=lambda i: p_values[i])
        rejections = [False] * m
        for rank, idx in enumerate(sorted_idx):
            if p_values[idx] < thresholds[rank]:
                rejections[idx] = True
            else:
                break  # Holm: stop after first non-rejection.
        return rejections

    return [False] * m

if __name__ == "__main__":
    import random
    random.seed(42)

    # Simulate 10 test variants, all under null (no true effect).
    num_tests = 10
    reps = 200

    fwer_uncorrected = 0
    fwer_bonferroni = 0
    fwer_holm = 0

    for _ in range(reps):
        # Generate p-values from uniform(0,1) under null.
        p_values = [random.random() for _ in range(num_tests)]

        # Uncorrected.
        rejections_unc = run_multiple_tests(p_values, method="uncorrected")
        if any(rejections_unc):
            fwer_uncorrected += 1

        # Bonferroni.
        rejections_bonf = run_multiple_tests(p_values, method="bonferroni")
        if any(rejections_bonf):
            fwer_bonferroni += 1

        # Holm.
        rejections_holm = run_multiple_tests(p_values, method="holm")
        if any(rejections_holm):
            fwer_holm += 1

    fwer_unc_rate = fwer_uncorrected / reps
    fwer_bonf_rate = fwer_bonferroni / reps
    fwer_holm_rate = fwer_holm / reps

    # Uncorrected should have higher FWER than corrected methods.
    assert fwer_unc_rate > fwer_bonf_rate, f"Uncorrected {fwer_unc_rate} should be > Bonferroni {fwer_bonf_rate}"
    assert fwer_unc_rate > fwer_holm_rate, f"Uncorrected {fwer_unc_rate} should be > Holm {fwer_holm_rate}"

    # Corrected methods should control type-I better.
    assert fwer_bonf_rate < 0.20, f"Bonferroni FWER {fwer_bonf_rate} should be reasonable"
    assert fwer_holm_rate < 0.20, f"Holm FWER {fwer_holm_rate} should be reasonable"

    # Holm should not be more conservative than Bonferroni (or very close).
    assert fwer_holm_rate >= fwer_bonf_rate - 0.05, "Holm should be at least as liberal as Bonferroni"

    print("PASS")
