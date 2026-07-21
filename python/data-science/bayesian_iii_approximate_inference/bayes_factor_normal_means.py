"""Bayes factor for comparing two normal means: H1 (θ ≠ 0) vs H0 (θ = 0).

BF = p(data|H1) / p(data|H0). Core claim: BF>1 when H1 is true AND BF<1 when H0 is true
(BOTH directions asserted; the two-sided test).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import Tuple

class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))


def _validate_bf_inputs(data, prior_var_h1):
    v = []
    if not isinstance(data, (list, tuple)):
        v.append(f"AURA-E-B1: data must be a sequence, got {type(data).__name__}")
    elif len(data) == 0:
        v.append("AURA-E-B8: data must be non-empty")
    elif not all(isinstance(y, (int, float)) and math.isfinite(y) for y in data):
        v.append("AURA-E008: data must contain only finite numbers (NaN/Inf rejected)")
    if not isinstance(prior_var_h1, (int, float)) or not math.isfinite(prior_var_h1):
        v.append(f"AURA-E-B1: prior_var_h1 must be a finite number, got {prior_var_h1!r}")
    elif prior_var_h1 <= 0:
        v.append(f"AURA-E-B5: prior_var_h1 must be > 0, got {prior_var_h1}")
    if v:
        raise AuraInputError(v)


def bayes_factor_normal(data, prior_var_h1=1.0) -> float:
    """Compute Bayes factor for H1: θ ~ N(0, prior_var_h1) vs H0: θ=0.

    Assumes data ~ N(θ, 1.0). Conjugate closed form: with S = Σy and n = len(data),
      log BF = -½·log(1 + n·τ²) + ½·τ²·S² / (1 + n·τ²)   where τ² = prior_var_h1.
    (The evidence term carries the full τ²·S²/denom factor — the missing n·τ² factor was
    the shipped wrong-math bug that sign-flipped conclusions; snapshot preserved as the
    validator regression fixture bayes_factor_normal_means.BROKEN.py.)
    """
    _validate_bf_inputs(data, prior_var_h1)
    n = len(data)
    S = sum(data)
    denom = 1.0 + n * prior_var_h1

    log_bf = -0.5 * math.log(denom) + 0.5 * prior_var_h1 * S * S / denom
    return math.exp(log_bf) if log_bf < 700 else float("inf")

if __name__ == "__main__":
    import random
    random.seed(42)

    # Case 1: data comes from H1 (θ_true = 2.0).
    theta_true_h1 = 2.0
    data_h1 = [random.gauss(theta_true_h1, 1.0) for _ in range(30)]
    bf_h1 = bayes_factor_normal(data_h1, prior_var_h1=1.0)

    # Case 2: data comes from H0 (θ_true = 0.0).
    theta_true_h0 = 0.0
    data_h0 = [random.gauss(theta_true_h0, 1.0) for _ in range(30)]
    bf_h0 = bayes_factor_normal(data_h0, prior_var_h1=1.0)

    # Under H1: BF should be > 1 (evidence for H1).
    assert bf_h1 > 1.0, f"BF under H1 {bf_h1} should be > 1"

    # Under H0: BF should be < 1 (evidence for H0).
    assert bf_h0 < 1.0, f"BF under H0 {bf_h0} should be < 1"

    print("PASS")
