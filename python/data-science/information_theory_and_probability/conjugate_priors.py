"""
Conjugate prior Bayesian updates: Beta-Binomial and Normal-Normal (known variance).

Core idea: Conjugate priors have closed-form posterior updates. Beta prior on a Binomial
likelihood updates by adding counts: Beta(α, β) → Beta(α+successes, β+failures).
Normal prior with known observation variance gives Normal posterior with updated mean/variance.
Sequential updates produce the same result as batch updating.

Use when: conjugate Bayesian inference, updating beliefs iteratively, combining prior knowledge
with observations, comparing sequential vs batch learning.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import Tuple, List


def beta_binomial_posterior(
    alpha_prior: float,
    beta_prior: float,
    successes: int,
    failures: int
) -> Tuple[float, float]:
    """
    Beta-Binomial conjugate update.

    Prior: Beta(alpha, beta)
    Likelihood: Binomial(successes, failures)
    Posterior: Beta(alpha + successes, beta + failures)
    """
    alpha_post = alpha_prior + successes
    beta_post = beta_prior + failures
    return alpha_post, beta_post


def beta_mean_variance(alpha: float, beta: float) -> Tuple[float, float]:
    """Mean and variance of Beta(alpha, beta) distribution."""
    mean = alpha / (alpha + beta)
    variance = (alpha * beta) / ((alpha + beta) ** 2 * (alpha + beta + 1))
    return mean, variance




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_normal_normal_posterior_known_variance(sigma2_prior, sigma2_obs):
    v = []
    if isinstance(sigma2_prior, (int, float)) and not math.isfinite(sigma2_prior):
        v.append(f"AURA-E008: sigma2_prior must be finite, got {sigma2_prior}")
    if isinstance(sigma2_obs, (int, float)) and not math.isfinite(sigma2_obs):
        v.append(f"AURA-E008: sigma2_obs must be finite, got {sigma2_obs}")
    if v:
        raise AuraInputError(v)

def normal_normal_posterior_known_variance(
    mu_prior: float,
    sigma2_prior: float,
    sigma2_obs: float,
    observations: List[float]
) -> Tuple[float, float]:
    """
    Normal-Normal conjugate update with known observation variance.

    Prior: N(mu_prior, sigma2_prior)
    Likelihood: each observation ~ N(mu, sigma2_obs) (known)
    Posterior: N(mu_post, sigma2_post)
    """
    _aura_validate_normal_normal_posterior_known_variance(sigma2_prior, sigma2_obs)
    n = len(observations)
    obs_mean = sum(observations) / n if n > 0 else 0.0

    # Precision = 1 / variance
    precision_prior = 1.0 / sigma2_prior
    precision_obs = 1.0 / sigma2_obs

    # Posterior precision = prior precision + n * obs precision
    precision_post = precision_prior + n * precision_obs

    # Posterior variance
    sigma2_post = 1.0 / precision_post

    # Posterior mean = (precision_prior * mu_prior + sum(x_i) * precision_obs) / precision_post
    mu_post = (precision_prior * mu_prior + n * obs_mean * precision_obs) / precision_post

    return mu_post, sigma2_post


if __name__ == "__main__":
    import random
    random.seed(42)

    # ======== Beta-Binomial ========
    # Test 1: Sequential update = Batch update
    alpha_prior = 2.0
    beta_prior = 2.0

    # Batch: 5 successes, 3 failures
    alpha_batch, beta_batch = beta_binomial_posterior(alpha_prior, beta_prior, 5, 3)

    # Sequential: update twice with different splits
    alpha_seq, beta_seq = beta_binomial_posterior(alpha_prior, beta_prior, 2, 1)
    alpha_seq, beta_seq = beta_binomial_posterior(alpha_seq, beta_seq, 3, 2)

    assert abs(alpha_batch - alpha_seq) < 1e-9, f"Batch vs seq alpha: {alpha_batch} vs {alpha_seq}"
    assert abs(beta_batch - beta_seq) < 1e-9, f"Batch vs seq beta: {beta_batch} vs {beta_seq}"

    # Test 2: Posterior mean shifts toward observed proportion
    # Prior is uniform Beta(1, 1), observe 80% success rate
    alpha_uniform = 1.0
    beta_uniform = 1.0
    mean_prior, _ = beta_mean_variance(alpha_uniform, beta_uniform)
    assert abs(mean_prior - 0.5) < 1e-9, "Uniform prior should have mean 0.5"

    alpha_post, beta_post = beta_binomial_posterior(alpha_uniform, beta_uniform, 80, 20)
    mean_post, _ = beta_mean_variance(alpha_post, beta_post)
    # Expected: (1 + 80) / (1 + 80 + 1 + 20) = 81/102 ≈ 0.7941
    assert abs(mean_post - 81.0/102.0) < 1e-9, f"Posterior mean incorrect, got {mean_post}"

    # Test 3: More data → smaller posterior variance
    alpha_few, beta_few = beta_binomial_posterior(1.0, 1.0, 5, 5)
    _, var_few = beta_mean_variance(alpha_few, beta_few)

    alpha_many, beta_many = beta_binomial_posterior(1.0, 1.0, 50, 50)
    _, var_many = beta_mean_variance(alpha_many, beta_many)

    assert var_many < var_few, f"More data should reduce variance: {var_many} vs {var_few}"

    # ======== Normal-Normal (known variance) ========
    # Test 4: Sequential = Batch for Normal-Normal
    mu_prior = 0.0
    sigma2_prior = 1.0
    sigma2_obs = 1.0

    # Batch: observations = [1.0, 2.0, 3.0]
    obs_all = [1.0, 2.0, 3.0]
    mu_batch, sigma2_batch = normal_normal_posterior_known_variance(
        mu_prior, sigma2_prior, sigma2_obs, obs_all
    )

    # Sequential: update with one observation at a time
    mu_seq = mu_prior
    sigma2_seq = sigma2_prior
    for obs in obs_all:
        mu_seq, sigma2_seq = normal_normal_posterior_known_variance(
            mu_seq, sigma2_seq, sigma2_obs, [obs]
        )

    assert abs(mu_batch - mu_seq) < 1e-9, f"Batch vs seq mu: {mu_batch} vs {mu_seq}"
    assert abs(sigma2_batch - sigma2_seq) < 1e-9, f"Batch vs seq sigma2: {sigma2_batch} vs {sigma2_seq}"

    # Test 5: Posterior mean shifts toward observed data (but is regularized by prior)
    mu_obs_mean = sum(obs_all) / len(obs_all)
    # Expected: (1.0 * 0.0 + 3 * 2.0) / (1.0 + 3) = 6.0 / 4.0 = 1.5
    assert abs(mu_batch - 1.5) < 1e-9, f"Posterior should be weighted avg of prior and data mean"

    # Test 6: More observations → smaller posterior variance
    obs_few = [1.0, 2.0]
    mu_f, sigma2_f = normal_normal_posterior_known_variance(mu_prior, sigma2_prior, sigma2_obs, obs_few)

    obs_many = [1.0] * 100
    mu_m, sigma2_m = normal_normal_posterior_known_variance(mu_prior, sigma2_prior, sigma2_obs, obs_many)

    assert sigma2_m < sigma2_f, f"More data should reduce variance: {sigma2_m} vs {sigma2_f}"

    # Test 7: Posterior variance formula check
    # sigma2_post = 1 / (1/sigma2_prior + n/sigma2_obs)
    n = len(obs_all)
    sigma2_post_expected = 1.0 / (1.0 / sigma2_prior + n / sigma2_obs)
    assert abs(sigma2_batch - sigma2_post_expected) < 1e-9, f"Posterior variance formula: {sigma2_batch} vs {sigma2_post_expected}"

    # Test 8: Very strong prior (sigma2_prior small) keeps posterior close to prior
    mu_strong_prior = 0.0
    sigma2_strong_prior = 0.001  # Very confident prior
    obs_away = [10.0, 11.0, 12.0]  # Far from prior mean
    mu_strong_post, _ = normal_normal_posterior_known_variance(
        mu_strong_prior, sigma2_strong_prior, sigma2_obs, obs_away
    )
    assert mu_strong_post < 2.0, f"Strong prior should keep posterior close: {mu_strong_post}"

    print("Conjugate priors (Beta-Binomial + Normal-Normal): all assertions PASS")
