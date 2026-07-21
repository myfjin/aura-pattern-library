"""Beta-binomial: recover the planted overdispersion and beat the plain binomial.

Counts with a random per-trial success probability p ~ Beta(α, β) are OVERDISPERSED
relative to a binomial. Method-of-moments recovers (α, β) from the sample mean and variance
(via the intra-class correlation ρ), and the beta-binomial log-likelihood at the recovered
parameters beats the binomial at its MLE. Core claim: (α, β) recovered AND beta-binomial
fits the overdispersed data strictly better than the binomial.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from math import lgamma
from typing import List, Tuple



class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_beta_binomial_loglik(n_trials):
    v = []
    if isinstance(n_trials, (int, float)) and n_trials <= 0:
        v.append(f"AURA-E009: n_trials must be > 0, got {n_trials}")
    if v:
        raise AuraInputError(v)

def _aura_validate_binomial_loglik(n_trials):
    v = []
    if isinstance(n_trials, (int, float)) and n_trials <= 0:
        v.append(f"AURA-E009: n_trials must be > 0, got {n_trials}")
    if v:
        raise AuraInputError(v)

def beta_binomial_loglik(counts: List[int], n_trials: int, alpha: float, beta: float) -> float:
    """Log-likelihood of counts under Beta-Binomial(n_trials, α, β)."""
    _aura_validate_beta_binomial_loglik(n_trials)
    return sum(lgamma(alpha + k) + lgamma(beta + n_trials - k) - lgamma(alpha + beta + n_trials)
               + lgamma(alpha + beta) - lgamma(alpha) - lgamma(beta) for k in counts)

def binomial_loglik(counts: List[int], n_trials: int, p: float) -> float:
    """Log-likelihood under Binomial(n_trials, p)."""
    _aura_validate_binomial_loglik(n_trials)
    if not 0 < p < 1:
        return float("-inf")
    return sum(k * math.log(p) + (n_trials - k) * math.log(1 - p) for k in counts)

def moment_match_beta_binomial(counts: List[int], n_trials: int) -> Tuple[float, float]:
    """Recover (α, β) by method of moments (via the intra-class correlation ρ)."""
    m = len(counts)
    mean = sum(counts) / m
    var = sum((c - mean) ** 2 for c in counts) / m
    mu = mean / n_trials
    # var = n·μ(1−μ)·(1 + (n−1)ρ)  →  solve for ρ.
    rho = (var / (n_trials * mu * (1 - mu)) - 1.0) / (n_trials - 1)
    rho = max(1e-3, min(0.99, rho))
    scale = 1.0 / rho - 1.0
    return mu * scale, (1 - mu) * scale

if __name__ == "__main__":
    import random
    random.seed(42)

    n_trials = 20
    alpha_true, beta_true = 2.0, 3.0
    counts = []
    for _ in range(80):
        p = random.betavariate(alpha_true, beta_true)
        counts.append(sum(1 for _ in range(n_trials) if random.random() < p))

    a_est, b_est = moment_match_beta_binomial(counts, n_trials)

    # Overdispersion present.
    mean = sum(counts) / len(counts)
    obs_var = sum((c - mean) ** 2 for c in counts) / len(counts)
    binom_var = n_trials * (mean / n_trials) * (1 - mean / n_trials)

    p_mle = mean / n_trials
    ll_bb = beta_binomial_loglik(counts, n_trials, a_est, b_est)
    ll_binom = binomial_loglik(counts, n_trials, p_mle)

    # Defining property: recover (α, β) near truth AND the beta-binomial explains the data
    # strictly better than the binomial. Measured (seed 42): α≈1.73, β≈3.14; llbb −958.7 > −1041.4.
    assert abs(a_est - alpha_true) < 0.8, f"α_est {a_est:.2f} should recover {alpha_true}"
    assert abs(b_est - beta_true) < 1.0, f"β_est {b_est:.2f} should recover {beta_true}"
    assert obs_var > binom_var, f"Data should be overdispersed: var {obs_var:.2f} > binomial {binom_var:.2f}"
    assert ll_bb > ll_binom, f"Beta-binomial loglik {ll_bb:.1f} should beat binomial {ll_binom:.1f}"

    print("PASS")
