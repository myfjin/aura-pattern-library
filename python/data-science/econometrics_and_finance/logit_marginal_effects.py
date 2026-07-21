"""Logit marginal effects: average partial derivatives of predicted probability.

AME = E[dP/dx]. Core claim: analytical gradient matches finite-difference check.
Planted logit model; derivatives verified against numerical gradient.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import List, Tuple



class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_logit_marginal_effect(x):
    v = []
    if isinstance(x, (int, float)) and not math.isfinite(x):
        v.append(f"AURA-E008: x must be finite, got {x}")
    if v:
        raise AuraInputError(v)

def _aura_validate_logit_predict(x, beta):
    v = []
    if isinstance(x, (int, float)) and not math.isfinite(x):
        v.append(f"AURA-E008: x must be finite, got {x}")
    if isinstance(beta, (int, float)) and not math.isfinite(beta):
        v.append(f"AURA-E008: beta must be finite, got {beta}")
    if v:
        raise AuraInputError(v)

def _aura_validate_numerical_gradient(x, beta, eps):
    v = []
    if isinstance(x, (int, float)) and not math.isfinite(x):
        v.append(f"AURA-E008: x must be finite, got {x}")
    if isinstance(beta, (int, float)) and not math.isfinite(beta):
        v.append(f"AURA-E008: beta must be finite, got {beta}")
    if isinstance(eps, (int, float)) and not math.isfinite(eps):
        v.append(f"AURA-E008: eps must be finite, got {eps}")
    if v:
        raise AuraInputError(v)

def logit_predict(x: float, beta: float) -> float:
    """Logistic regression prediction: P(y=1|x) = 1 / (1 + exp(-β·x))."""
    _aura_validate_logit_predict(x, beta)
    return 1.0 / (1.0 + math.exp(-beta * x))

def logit_marginal_effect(x: float, beta: float) -> float:
    """Marginal effect: dP/dx = β·P·(1-P)."""
    _aura_validate_logit_marginal_effect(x)
    p = logit_predict(x, beta)
    return beta * p * (1 - p)

def average_marginal_effect(x_values: List[float], beta: float) -> float:
    """Average marginal effect across sample."""
    return sum(logit_marginal_effect(x, beta) for x in x_values) / len(x_values)

def numerical_gradient(x: float, beta: float, eps: float = 1e-6) -> float:
    """Numerical gradient: (f(x+ε) - f(x-ε)) / (2ε)."""
    _aura_validate_numerical_gradient(x, beta, eps)
    p_plus = logit_predict(x + eps, beta)
    p_minus = logit_predict(x - eps, beta)
    return (p_plus - p_minus) / (2 * eps)

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: logit model with β = 1.5.
    beta_true = 1.5
    x_sample = [random.gauss(0, 1) for _ in range(50)]

    ame_analytical = average_marginal_effect(x_sample, beta_true)

    # Verify against numerical gradient (average).
    ame_numerical = sum(numerical_gradient(x, beta_true) for x in x_sample) / len(x_sample)

    # Check: analytical and numerical agree.
    assert abs(ame_analytical - ame_numerical) < 0.01, \
        f"Analytical AME {ame_analytical} vs numerical {ame_numerical}"

    # AME should be positive (positive coefficient).
    assert ame_analytical > 0, f"AME should be positive: {ame_analytical}"

    print("PASS")
