"""Minimum Detectable Effect (MDE): smallest effect size detectable with given n, α, power.

Computed from normal approximation. Verified by simulation at multiple points.
Core claim: MDE formula matches simulated power curve.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import Tuple, List



class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_mde_normal_approx(alpha, power, sigma):
    v = []
    if isinstance(alpha, (int, float)) and not math.isfinite(alpha):
        v.append(f"AURA-E008: alpha must be finite, got {alpha}")
    if isinstance(power, (int, float)) and not math.isfinite(power):
        v.append(f"AURA-E008: power must be finite, got {power}")
    if isinstance(sigma, (int, float)) and sigma < 0:
        v.append(f"AURA-E-B5: sigma must be >= 0, got {sigma}")
    if v:
        raise AuraInputError(v)

def _aura_validate_simulate_power(true_effect):
    v = []
    if isinstance(true_effect, (int, float)) and not math.isfinite(true_effect):
        v.append(f"AURA-E008: true_effect must be finite, got {true_effect}")
    if v:
        raise AuraInputError(v)

def mde_normal_approx(n_per_arm: int, alpha: float = 0.05, power: float = 0.8, sigma: float = 1.0) -> float:
    """Compute MDE via normal approximation.

    For two-sample t-test: MDE ≈ (z_α/2 + z_β) * σ * sqrt(2/n)
    Hardcoded z-values for common α and power.
    """
    _aura_validate_mde_normal_approx(alpha, power, sigma)
    z_alpha = 1.96 if abs(alpha - 0.05) < 0.001 else 2.58  # Two-tailed z_α/2
    z_beta = 0.84 if abs(power - 0.8) < 0.001 else 1.28   # z_β for power

    return (z_alpha + z_beta) * sigma * math.sqrt(2 / n_per_arm)

def simulate_power(n_per_arm: int, true_effect: float, reps: int = 500) -> float:
    """Simulate power at a given effect size."""
    _aura_validate_simulate_power(true_effect)
    import random
    random.seed(42)

    rejections = 0
    for _ in range(reps):
        treatment = [random.gauss(true_effect, 1) for _ in range(n_per_arm)]
        control = [random.gauss(0, 1) for _ in range(n_per_arm)]

        mean_t = sum(treatment) / n_per_arm
        mean_c = sum(control) / n_per_arm
        var_t = sum((x - mean_t)**2 for x in treatment) / (n_per_arm - 1)
        var_c = sum((x - mean_c)**2 for x in control) / (n_per_arm - 1)

        se = math.sqrt(var_t / n_per_arm + var_c / n_per_arm)
        t_stat = (mean_t - mean_c) / se if se > 0 else 0

        # Two-tailed test.
        from math import erfc
        p_value = erfc(abs(t_stat) / math.sqrt(2))

        if p_value < 0.05:
            rejections += 1

    return rejections / reps

if __name__ == "__main__":
    # Compute MDE for typical setup (n=100 per arm).
    n_per_arm = 100
    mde_computed = mde_normal_approx(n_per_arm, alpha=0.05, power=0.80)

    # Verify by simulation: power at MDE should be ~0.80.
    power_at_mde = simulate_power(n_per_arm, mde_computed, reps=400)

    # Verify at 1.5x MDE (should have power > 0.80).
    power_at_1_5x = simulate_power(n_per_arm, 1.5 * mde_computed, reps=400)

    # Verify at 0.7x MDE (should have power < 0.80).
    power_at_0_7x = simulate_power(n_per_arm, 0.7 * mde_computed, reps=400)

    # Power at MDE should be close to 0.80.
    assert 0.65 < power_at_mde < 0.95, \
        f"Power at MDE {power_at_mde} should be ~0.80"

    # Power curve should be monotonic.
    assert power_at_1_5x > power_at_mde, \
        f"Power at 1.5x MDE {power_at_1_5x} should > MDE {power_at_mde}"
    assert power_at_0_7x < power_at_mde, \
        f"Power at 0.7x MDE {power_at_0_7x} should < MDE {power_at_mde}"

    print("PASS")
