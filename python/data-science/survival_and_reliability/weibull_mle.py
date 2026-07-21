"""Weibull MLE: maximum-likelihood estimation of shape k and scale λ (uncensored).

For iid Weibull data the log-likelihood is
    ℓ(k,λ) = n·ln k − n·k·ln λ + (k−1)·Σ ln t_i − Σ (t_i/λ)^k.
Profiling out λ = (Σ t_i^k / n)^(1/k) leaves a single equation in k:
    1/k + (1/n)Σ ln t_i − (Σ t_i^k ln t_i)/(Σ t_i^k) = 0,
solved here by Newton-Raphson. This is the actual MLE (not a log-log probability-plot
regression). Core claim: planted shape/scale recovered by maximum likelihood.
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

def _aura_validate_weibull_mle(tol):
    v = []
    if isinstance(tol, (int, float)) and not math.isfinite(tol):
        v.append(f"AURA-E008: tol must be finite, got {tol}")
    if v:
        raise AuraInputError(v)

def weibull_mle(times: List[float], max_iter: int = 100, tol: float = 1e-10) -> Tuple[float, float]:
    """Estimate Weibull (shape k, scale λ) by maximum likelihood.

    Returns: (k, lambda). Newton-Raphson on the profiled shape equation.
    """
    _aura_validate_weibull_mle(tol)
    n = len(times)
    ln_t = [math.log(t) for t in times]
    mean_ln = sum(ln_t) / n

    k = 1.0  # start at the exponential special case
    for _ in range(max_iter):
        tk = [t**k for t in times]
        A = sum(tk)
        B = sum(tk[i] * ln_t[i] for i in range(n))
        C = sum(tk[i] * ln_t[i]**2 for i in range(n))

        # g(k) = 1/k + mean_ln − B/A ; g'(k) = −1/k² − (C·A − B²)/A²
        g = 1.0 / k + mean_ln - B / A
        g_prime = -1.0 / k**2 - (C * A - B * B) / (A * A)
        if abs(g_prime) < 1e-14:
            break
        k_new = k - g / g_prime
        if k_new <= 0:
            k_new = k / 2.0  # keep k positive
        if abs(k_new - k) < tol:
            k = k_new
            break
        k = k_new

    lam = (sum(t**k for t in times) / n)**(1.0 / k)
    return k, lam

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: Weibull with k=2.0, λ=5.0 (inverse-CDF sampling).
    k_true, lam_true = 2.0, 5.0
    times = [lam_true * (-math.log(random.random()))**(1.0 / k_true) for _ in range(80)]

    k_est, lam_est = weibull_mle(times)

    # MLE recovers tightly (measured seed 42: k≈2.13, λ≈5.26).
    assert abs(k_est - k_true) < 0.3, f"k={k_est}, expected ≈{k_true}"
    assert abs(lam_est - lam_true) < 0.5, f"λ={lam_est}, expected ≈{lam_true}"

    # Sanity: the fitted k satisfies the MLE stationarity equation (score ≈ 0).
    ln_t = [math.log(t) for t in times]
    tk = [t**k_est for t in times]
    score_k = 1.0 / k_est + sum(ln_t) / len(times) - sum(tk[i] * ln_t[i] for i in range(len(times))) / sum(tk)
    assert abs(score_k) < 1e-6, f"MLE score not zero at solution: {score_k}"

    print("PASS")
