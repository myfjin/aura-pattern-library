"""
A/B Test for Two Proportions

Core idea: Test whether two conversion rates differ using a z-test for proportions.
Compute pooled standard error under the null, then the z-statistic. Also compute effect
size (Cohen's h) to quantify the practical difference.

When to use: Compare two click-through rates, conversion rates, or any binary outcomes
in A/B testing scenarios.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import Tuple


def ab_test_proportions(conversions_a: int, trials_a: int, conversions_b: int, trials_b: int) -> Tuple[float, float, float]:
    """
    Perform z-test for two proportions.

    Args:
        conversions_a: Number of successes in group A.
        trials_a: Total trials in group A.
        conversions_b: Number of successes in group B.
        trials_b: Total trials in group B.

    Returns:
        Tuple of (z_statistic, p_value_approx, cohens_h).
    """
    p_a = conversions_a / trials_a
    p_b = conversions_b / trials_b
    diff = p_a - p_b

    # Pooled proportion (under null: p_a == p_b)
    p_pooled = (conversions_a + conversions_b) / (trials_a + trials_b)

    # Standard error under null
    se_null = math.sqrt(p_pooled * (1 - p_pooled) * (1 / trials_a + 1 / trials_b))

    # Z-statistic
    if se_null > 0:
        z = diff / se_null
    else:
        z = 0.0

    # Approximate p-value using normal CDF (two-tailed)
    # Use Abramowitz & Stegun approximation for standard normal CDF
    def normal_cdf(z):
        """Approximate standard normal CDF using Hart's rational approximation."""
        if z < 0:
            return 1 - normal_cdf(-z)
        t = 1 / (1 + 0.2316419 * z)
        d = 0.3989423 * math.exp(-z * z / 2)
        approx = 1 - d * t * (0.319381530 + t * (-0.356563782 + t * (1.781477937 + t * (-1.821255978 + t * 1.330274429))))
        return approx

    # One-tailed p-value: P(Z > |z|)
    p_one_tail = 1 - normal_cdf(abs(z))
    # Two-tailed
    p_value = min(2 * p_one_tail, 1.0)

    # Cohen's h: effect size for proportions
    # h = 2 * (arcsin(sqrt(p_a)) - arcsin(sqrt(p_b)))
    h_a = 2 * math.asin(math.sqrt(p_a))
    h_b = 2 * math.asin(math.sqrt(p_b))
    cohens_h = (h_a - h_b) / 2

    return z, p_value, cohens_h


if __name__ == "__main__":
    # Scenario 1: No difference (null)
    # Both groups have ~10% conversion
    z_null, p_null, h_null = ab_test_proportions(10, 100, 11, 100)
    print(f"Null case: z={z_null:.3f}, p={p_null:.3f}, Cohen's h={h_null:.3f}")
    assert p_null > 0.05, "Null case should have high p-value"

    # Scenario 2: Real difference
    # Group A: 15%, Group B: 10%
    z_alt, p_alt, h_alt = ab_test_proportions(30, 200, 15, 200)
    print(f"Alt case: z={z_alt:.3f}, p={p_alt:.3f}, Cohen's h={h_alt:.3f}")
    assert p_alt < 0.05, "Alt case should have low p-value"
    assert abs(h_alt) > 0.1, "Effect size should be non-negligible"

    print("✓ A/B test for proportions PASSED")
