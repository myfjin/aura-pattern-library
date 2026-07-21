"""Doubly Robust AIPW: consistent if EITHER the outcome model OR the propensity is correct.

AIPW = (1/n) Σ [ μ₁(Xᵢ) − μ₀(Xᵢ) + Tᵢ(Yᵢ−μ₁)/eᵢ − (1−Tᵢ)(Yᵢ−μ₀)/(1−eᵢ) ].
Core claim (double robustness): it recovers the true ATE in BOTH
  Case 1 — CORRECT outcome model, WRONG propensity, and
  Case 2 — WRONG outcome model, CORRECT propensity.
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

def _aura_validate_logistic(x):
    v = []
    if isinstance(x, (int, float)) and not math.isfinite(x):
        v.append(f"AURA-E008: x must be finite, got {x}")
    if v:
        raise AuraInputError(v)

def logistic(x: float) -> float:
    _aura_validate_logistic(x)
    if x > 100:
        return 1.0
    if x < -100:
        return 0.0
    return 1.0 / (1.0 + math.exp(-x))

def fit_outcome_model(x: List[float], t: List[int], y: List[float]) -> Tuple[float, float, float]:
    """Fit y ~ a + b*t + c*x (linear); return (a, b, c)."""
    n = len(x)
    xm, tm, ym = sum(x) / n, sum(t) / n, sum(y) / n
    stt = sum((t[i] - tm)**2 for i in range(n))
    sxx = sum((x[i] - xm)**2 for i in range(n))
    stx = sum((t[i] - tm) * (x[i] - xm) for i in range(n))
    sty = sum((t[i] - tm) * (y[i] - ym) for i in range(n))
    sxy = sum((x[i] - xm) * (y[i] - ym) for i in range(n))
    den = stt * sxx - stx**2
    if abs(den) < 1e-12:
        return ym, 0.0, 0.0
    b = (sxy * stx - sty * sxx) / den
    c = (sty * stx - sxy * stt) / den
    a = ym - b * tm - c * xm
    return a, b, c

def estimate_propensity(x: List[float], t: List[int]) -> List[float]:
    n = len(x)
    beta = 0.0
    for _ in range(200):
        grad = sum((t[i] - logistic(beta * x[i])) * x[i] for i in range(n))
        beta += 0.05 * grad / n
    return [logistic(beta * xi) for xi in x]

def aipw_ate(x: List[float], t: List[int], y: List[float]) -> float:
    """Augmented IPW ATE (the doubly-robust estimator)."""
    a, b, c = fit_outcome_model(x, t, y)
    e = estimate_propensity(x, t)
    n = len(x)
    eps = 0.01
    mu1 = [a + b + c * xi for xi in x]
    mu0 = [a + c * xi for xi in x]
    s = 0.0
    for i in range(n):
        w1 = 1.0 / max(e[i], eps)
        w0 = 1.0 / max(1.0 - e[i], eps)
        s += (mu1[i] - mu0[i]) + t[i] * (y[i] - mu1[i]) * w1 - (1 - t[i]) * (y[i] - mu0[i]) * w0
    return s / n

if __name__ == "__main__":
    import random

    # Case 1: CORRECT outcome model (linear), WRONG propensity (random, ignores X).
    random.seed(1)
    n = 300
    x = [random.gauss(0, 1) for _ in range(n)]
    t = [random.randint(0, 1) for _ in range(n)]
    y = [2.0 * t[i] + 0.5 * x[i] + random.gauss(0, 0.5) for i in range(n)]
    aipw_c1 = aipw_ate(x, t, y)

    # Case 2: WRONG outcome model (truth is nonlinear x²; we fit linear), CORRECT propensity.
    random.seed(2)
    n = 300
    x = [random.gauss(0, 1) for _ in range(n)]
    t = [1 if random.random() < logistic(1.2 * x[i]) else 0 for i in range(n)]
    y = [2.0 * t[i] + 0.8 * x[i]**2 + random.gauss(0, 0.5) for i in range(n)]
    aipw_c2 = aipw_ate(x, t, y)

    # Defining property: double robustness — recover true ATE 2.0 under EITHER misspecification.
    # Measured: case1≈2.04 (correct outcome), case2≈1.72 (correct propensity).
    assert abs(aipw_c1 - 2.0) < 0.4, f"AIPW case1 {aipw_c1} should recover 2.0 (correct outcome model)"
    assert abs(aipw_c2 - 2.0) < 0.5, f"AIPW case2 {aipw_c2} should recover 2.0 (correct propensity)"

    print("PASS")
