import math
"""
Benjamini-Hochberg False Discovery Rate Correction

Core idea: When testing many hypotheses, Bonferroni is overly conservative. Benjamini-Hochberg
controls the False Discovery Rate (FDR): the expected proportion of false positives among
rejected hypotheses. Sort p-values, find largest index i where p_i <= (i/m) * alpha,
then reject all p-values up to that index.

When to use: Multiple hypothesis testing (e.g., genome-wide association, gene expression).
FDR is less stringent than family-wise error rate (FWER), allowing more discoveries.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_benjamini_hochberg(alpha):
    v = []
    if isinstance(alpha, (int, float)) and not math.isfinite(alpha):
        v.append(f"AURA-E008: alpha must be finite, got {alpha}")
    if v:
        raise AuraInputError(v)

def benjamini_hochberg(p_values: List[float], alpha: float = 0.05) -> Tuple[List[bool], float]:
    """
    Benjamini-Hochberg FDR procedure.

    Args:
        p_values: List of p-values from m independent or positively correlated tests.
        alpha: Target FDR level (e.g., 0.05).

    Returns:
        Tuple of (rejected, threshold) where:
        - rejected: Boolean list indicating rejected hypotheses (True = reject H0, H1 accepted).
        - threshold: The p-value threshold used.
    """
    _aura_validate_benjamini_hochberg(alpha)
    m = len(p_values)

    # Pair each p-value with its original index
    indexed_pvals = [(p_values[i], i) for i in range(m)]

    # Sort by p-value
    indexed_pvals.sort()

    # Find largest index i where p_values[i] <= (i+1)/m * alpha
    # (using 1-indexed i: i ranges from 1 to m)
    threshold = 0.0
    largest_i = -1

    for rank, (p_val, orig_idx) in enumerate(indexed_pvals):
        i = rank + 1  # 1-indexed rank
        if p_val <= (i / m) * alpha:
            largest_i = rank
            threshold = p_val

    # Reject all hypotheses with p-value <= threshold
    rejected = [False] * m
    if largest_i >= 0:
        for rank in range(largest_i + 1):
            _, orig_idx = indexed_pvals[rank]
            rejected[orig_idx] = True

    return rejected, threshold


if __name__ == "__main__":
    # Scenario 1: No true effects (all p-values under H0, approximately uniform)
    p_values_null = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]
    rejected_null, threshold_null = benjamini_hochberg(p_values_null, alpha=0.05)
    num_rejected_null = sum(rejected_null)
    print(f"Null case (10 p-values): {num_rejected_null} rejected, threshold={threshold_null:.4f}")
    # With uniform p-values, expect few or zero rejections
    assert num_rejected_null <= 2, "Null case should have few false positives"

    # Scenario 2: True effects mixed with null (some small p-values)
    p_values_mixed = [0.001, 0.002, 0.003, 0.01, 0.02, 0.1, 0.2, 0.3, 0.4, 0.5]
    rejected_mixed, threshold_mixed = benjamini_hochberg(p_values_mixed, alpha=0.05)
    num_rejected_mixed = sum(rejected_mixed)
    print(f"Mixed case (10 p-values): {num_rejected_mixed} rejected, threshold={threshold_mixed:.4f}")
    # Should reject the small p-values
    assert num_rejected_mixed >= 3, "Mixed case should reject some true signals"
    assert rejected_mixed[0] and rejected_mixed[1] and rejected_mixed[2], "Smallest p-values should be rejected"

    # Scenario 3: All true effects (very small p-values)
    p_values_alt = [0.0001, 0.0002, 0.0003, 0.0005, 0.001, 0.002, 0.003, 0.004, 0.005, 0.01]
    rejected_alt, threshold_alt = benjamini_hochberg(p_values_alt, alpha=0.05)
    num_rejected_alt = sum(rejected_alt)
    print(f"True effects (10 p-values): {num_rejected_alt} rejected, threshold={threshold_alt:.4f}")
    assert num_rejected_alt >= 5, "True effects should result in many rejections"

    # Scenario 4: Large-scale multiple testing (1000 tests, 50 true effects)
    import random
    random.seed(42)

    # 50 p-values from true effects (small) + 950 null (uniform)
    true_effects = [random.uniform(0, 0.001) for _ in range(50)]
    nulls = [random.uniform(0, 1) for _ in range(950)]
    p_values_large = true_effects + nulls
    random.shuffle(p_values_large)

    rejected_large, threshold_large = benjamini_hochberg(p_values_large, alpha=0.05)
    num_rejected_large = sum(rejected_large)
    print(f"Large-scale (1000 tests, 50 true): {num_rejected_large} rejected, threshold={threshold_large:.6f}")

    # Should catch most true effects with few false positives
    assert num_rejected_large >= 40, "Should detect most true effects"
    assert num_rejected_large <= 150, "Should have controlled FDR (not too many false positives)"

    print("✓ Benjamini-Hochberg FDR PASSED")
