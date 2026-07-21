"""
Gamma-Poisson conjugate prior: Gamma prior on Poisson rate parameter.

Core idea: prior Gamma(α, β); observe Poisson counts; posterior is Gamma(α + Σcount, β + n).
Sequential updates ≡ batch update (conjugacy). Posterior matches closed form.

When to use: rate estimation, count data modeling, reliability/failure analysis.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple

def log_gamma_func(x: float) -> float:
    """Approximation of log Γ(x)."""
    if x < 1:
        return math.log(abs(1 / (x * math.sin(math.pi * x) * (1 - x)))) if x != int(x) else float('-inf')
    # Stirling
    return 0.5 * math.log(2 * math.pi) + (x - 0.5) * math.log(x) - x



class AuraInputError(ValueError):
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))


def _aura_validate_pos(**named):
    """alpha/beta/prior params are shape/concentration -> must be finite and > 0
    (domains written down in validator/ALPHA_BETA_DOMAINS.md)."""
    v = []
    for name, val in named.items():
        if isinstance(val, (int, float)) and not math.isfinite(val):
            v.append(f"AURA-E008: {name} must be finite, got {val}")
        elif isinstance(val, (int, float)) and val <= 0:
            v.append(f"AURA-E001: {name} must be > 0, got {val}")
    if v:
        raise AuraInputError(v)

def gamma_poisson_posterior(counts: List[int], alpha_prior: float,
                            beta_prior: float) -> Tuple[float, float]:
    """
    Posterior Gamma parameters given Poisson counts.
    Posterior: Gamma(α + Σcount, β + n)
    Return: (alpha_post, beta_post)
    """
    _aura_validate_pos(alpha_prior=alpha_prior, beta_prior=beta_prior)
    n = len(counts)
    sum_counts = sum(counts)
    alpha_post = alpha_prior + sum_counts
    beta_post = beta_prior + n
    return alpha_post, beta_post



class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_gamma_poisson_ll(beta):
    v = []
    if isinstance(beta, (int, float)) and not math.isfinite(beta):
        v.append(f"AURA-E008: beta must be finite, got {beta}")
    if v:
        raise AuraInputError(v)

def _aura_validate_gamma_posterior_mean(beta):
    v = []
    if isinstance(beta, (int, float)) and not math.isfinite(beta):
        v.append(f"AURA-E008: beta must be finite, got {beta}")
    if v:
        raise AuraInputError(v)

def _aura_validate_gamma_posterior_var(beta):
    v = []
    if isinstance(beta, (int, float)) and not math.isfinite(beta):
        v.append(f"AURA-E008: beta must be finite, got {beta}")
    if v:
        raise AuraInputError(v)

def _aura_validate_poisson_sample(lam):
    v = []
    if isinstance(lam, (int, float)) and not math.isfinite(lam):
        v.append(f"AURA-E008: lam must be finite, got {lam}")
    if isinstance(lam, (int, float)) and lam <= 0:
        v.append(f"AURA-E001: lam must be > 0, got {lam}")
    if v:
        raise AuraInputError(v)

def gamma_posterior_mean(alpha: float, beta: float) -> float:
    """Mean of Gamma(α, β) is α/β."""
    _aura_validate_pos(alpha=alpha, beta=beta)
    _aura_validate_gamma_posterior_mean(beta)
    return alpha / beta

def gamma_posterior_var(alpha: float, beta: float) -> float:
    """Variance of Gamma(α, β) is α/β²."""
    _aura_validate_pos(alpha=alpha, beta=beta)
    _aura_validate_gamma_posterior_var(beta)
    return alpha / (beta ** 2)

def gamma_poisson_ll(counts: List[int], alpha: float, beta: float) -> float:
    """Log-likelihood under Gamma-Poisson model."""
    _aura_validate_pos(alpha=alpha, beta=beta)
    _aura_validate_gamma_poisson_ll(beta)
    # Marginal likelihood: ∫ p(counts|λ) p(λ) dλ
    # = ∏_i (α/β)^count_i * Γ(α + count_i) / (Γ(α) * (β+1)^count_i * count_i!)
    # Simplified log: sum log Γ(α + count_i) - count_i * log(β+1) - log count_i!

    ll = 0.0
    for count in counts:
        ll += log_gamma_func(alpha + count) - log_gamma_func(alpha)
        ll -= count * math.log(beta + 1) if beta + 1 > 0 else 0
        # Log factorial
        ll -= sum(math.log(j) for j in range(1, count + 1))

    return ll

def poisson_sample(lam: float) -> int:
    """Simple Poisson sampler via Knuth algorithm."""
    _aura_validate_poisson_sample(lam)
    import random
    L = math.exp(-lam)
    k = 0
    p = 1.0
    while p > L:
        k += 1
        p *= random.random()
    return k - 1

if __name__ == '__main__':
    import random
    random.seed(42)

    # Planted Poisson: λ = 3.5
    true_lambda = 3.5
    counts = [poisson_sample(true_lambda) for _ in range(50)]

    # Weak prior: Gamma(1, 1) (exponential)
    alpha_weak, beta_weak = 1.0, 1.0
    alpha_weak_post, beta_weak_post = gamma_poisson_posterior(counts, alpha_weak, beta_weak)
    mean_weak_post = gamma_posterior_mean(alpha_weak_post, beta_weak_post)

    # Strong prior: Gamma(2, 1) centered at λ=2
    alpha_strong, beta_strong = 2.0, 1.0
    alpha_strong_post, beta_strong_post = gamma_poisson_posterior(counts, alpha_strong, beta_strong)
    mean_strong_post = gamma_posterior_mean(alpha_strong_post, beta_strong_post)

    # Assertions
    # Posterior parameters should match closed form
    assert alpha_weak_post == alpha_weak + sum(counts), "α posterior formula"
    assert beta_weak_post == beta_weak + len(counts), "β posterior formula"

    # Posterior mean should be between prior and empirical mean
    empirical_mean = sum(counts) / len(counts)
    prior_mean_weak = gamma_posterior_mean(alpha_weak, beta_weak)
    # Posterior mean pulled by data toward empirical
    assert prior_mean_weak < mean_weak_post < empirical_mean or prior_mean_weak > mean_weak_post > empirical_mean, \
        f"Weak posterior {mean_weak_post} should be between prior {prior_mean_weak} and empirical {empirical_mean}"

    # Strong prior posterior should be in [prior, empirical] range
    prior_mean_strong = gamma_posterior_mean(alpha_strong, beta_strong)
    # Posterior should be between prior and empirical (convex combination)
    assert min(prior_mean_strong, empirical_mean) <= mean_strong_post <= max(prior_mean_strong, empirical_mean), \
        f"Strong posterior {mean_strong_post} should be between prior {prior_mean_strong} and empirical {empirical_mean}"

    # Posterior variance should shrink
    var_weak_prior = gamma_posterior_var(alpha_weak, beta_weak)
    var_weak_post = gamma_posterior_var(alpha_weak_post, beta_weak_post)
    assert var_weak_post < var_weak_prior, f"Posterior variance {var_weak_post} should shrink from prior {var_weak_prior}"

    # Likelihood should be well-defined and finite
    ll = gamma_poisson_ll(counts, alpha_weak, beta_weak)
    assert not math.isnan(ll) and not math.isinf(ll), f"Likelihood should be finite, got {ll}"

    # Sequential updates should match batch
    seq_alpha, seq_beta = alpha_weak, beta_weak
    for count in counts:
        seq_alpha += count
        seq_beta += 1
    assert seq_alpha == alpha_weak_post and seq_beta == beta_weak_post, "Sequential should match batch"

    print("PASS")
