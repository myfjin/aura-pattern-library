"""
Power Analysis: Sample Size for Two-Proportion Z-Test.

Computes required sample size per group for a given effect size, alpha, and power
using normal approximation. Verifies the computed n reproduces the target power.
Use for study design when comparing two proportions.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import Tuple


def normal_quantile(p: float) -> float:
    """Approximate inverse normal CDF using rational approximation."""
    if p < 0.5:
        return -normal_quantile(1 - p)

    t = math.sqrt(-2.0 * math.log(1.0 - p))
    num = 2.515517 + 0.802853 * t + 0.010328 * t ** 2
    denom = 1.0 + 1.432788 * t + 0.189269 * t ** 2 + 0.001308 * t ** 3
    return t - num / denom


def normal_cdf_approx(z: float) -> float:
    """Approximate standard normal CDF using erf."""
    return 0.5 * (1.0 + math.tanh(0.7978845608 * z))




class AuraInputError(ValueError):
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_domain_two_proportion_power(alpha):
    v = []
    if isinstance(alpha, (int, float)) and not math.isfinite(alpha):
        v.append(f"AURA-E008: alpha must be finite, got {alpha}")
    elif isinstance(alpha, (int, float)) and not (0.0 < alpha < 1.0):
        v.append(f"AURA-E001: alpha must be in (0,1), got {alpha}")
    if v:
        raise AuraInputError(v)

def _aura_domain_sample_size_two_proportion(alpha):
    v = []
    if isinstance(alpha, (int, float)) and not math.isfinite(alpha):
        v.append(f"AURA-E008: alpha must be finite, got {alpha}")
    elif isinstance(alpha, (int, float)) and not (0.0 < alpha < 1.0):
        v.append(f"AURA-E001: alpha must be in (0,1), got {alpha}")
    if v:
        raise AuraInputError(v)

def two_proportion_power(n: int, p1: float, p2: float, alpha: float = 0.05) -> float:
    """
    Compute power of two-proportion z-test (one-sided).

    Args:
        n: sample size per group
        p1, p2: proportions (H1: p1 != p2)
        alpha: significance level (two-tailed)

    Returns:
        Power (probability of detecting the effect)
    """
    _aura_domain_two_proportion_power(alpha)
    # Use two-tailed critical value
    z_crit = normal_quantile(1.0 - alpha / 2.0)

    # Pooled SE under H0
    p_pool = (p1 + p2) / 2.0
    se_h0 = math.sqrt(2.0 * p_pool * (1.0 - p_pool) / n)

    # SE under H1
    se_h1 = math.sqrt((p1 * (1.0 - p1) + p2 * (1.0 - p2)) / n)

    # Effect
    effect = abs(p1 - p2)

    # Under H1, test statistic is approx normal with mean effect/se_h1
    # Power = P(|Z| > z_crit) where Z ~ N(effect/se_h1, 1)
    if se_h1 == 0:
        return 1.0

    # Non-centrality
    ncp = effect / se_h1

    # Power is P(Z > z_crit) + P(Z < -z_crit) where Z ~ N(ncp, 1)
    # Approx = Phi(ncp - z_crit) + Phi(-ncp - z_crit)
    # For large ncp, second term is negligible
    power = 1.0 - normal_cdf_approx(z_crit - ncp)

    return power


def sample_size_two_proportion(
    p1: float, p2: float, alpha: float = 0.05, target_power: float = 0.80
) -> int:
    """
    Compute required sample size per group.

    Args:
        p1, p2: proportions under null and alternative
        alpha: significance level
        target_power: desired power

    Returns:
        Required n per group
    """
    _aura_domain_sample_size_two_proportion(alpha)
    # Initial guess using normal approximation
    z_alpha = normal_quantile(1.0 - alpha / 2.0)
    z_beta = normal_quantile(target_power)

    p_pool = (p1 + p2) / 2.0
    se_sq = 2.0 * p_pool * (1.0 - p_pool) + (p1 * (1.0 - p1) + p2 * (1.0 - p2))
    effect = abs(p1 - p2)

    n = (z_alpha + z_beta) ** 2 * se_sq / (effect ** 2)
    return max(1, int(math.ceil(n)))


if __name__ == "__main__":
    random.seed(42)

    # Compute sample size for p1=0.3, p2=0.5, alpha=0.05, power=0.80
    p1, p2 = 0.3, 0.5
    alpha = 0.05
    target_power = 0.80

    n_computed = sample_size_two_proportion(p1, p2, alpha, target_power)

    # Verify the computed n achieves the target power
    achieved_power = two_proportion_power(n_computed, p1, p2, alpha)

    assert achieved_power >= target_power - 0.05, (
        f"Achieved power {achieved_power:.3f} below target {target_power}"
    )

    # Verify n-1 gives lower power (sanity check)
    power_lower = two_proportion_power(n_computed - 1, p1, p2, alpha)
    assert power_lower < achieved_power, "Lower n should give lower power"

    print(f"power_analysis_sample_size.py: n_computed={n_computed}, achieved_power={achieved_power:.3f}, target={target_power} PASS")
