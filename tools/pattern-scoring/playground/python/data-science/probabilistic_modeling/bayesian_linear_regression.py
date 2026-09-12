"""
Bayesian linear regression: conjugate normal prior, known noise, closed-form posterior.

Core idea: prior N(μ₀, Σ₀); likelihood N(y | Xβ, σ²I); posterior is N(μ_post, Σ_post)
with closed-form updates. Posterior mean is between prior and OLS; variance shrinks with data.

When to use: interpretable regression with uncertainty, small data, informative priors.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import Tuple, List

def bayesian_linreg_conjugate(X: List[float], y: List[float],
                              mu0: float = 0.0, sigma0_sq: float = 100.0,
                              sigma_sq: float = 1.0) -> Tuple[float, float]:
    """
    Conjugate normal posterior for simple univariate linear regression.
    y_i = β * x_i + ε_i, ε ~ N(0, σ²)
    Prior: β ~ N(μ₀, σ₀²)
    Return: (posterior mean, posterior variance)
    """
    n = len(X)
    if n == 0:
        return mu0, sigma0_sq

    # Sufficient statistics
    sum_x = sum(X)
    sum_y = sum(y)
    sum_xy = sum(x * yv for x, yv in zip(X, y))
    sum_x_sq = sum(x ** 2 for x in X)

    # OLS estimate
    ols_beta = (n * sum_xy - sum_x * sum_y) / (n * sum_x_sq - sum_x ** 2) if (n * sum_x_sq - sum_x ** 2) != 0 else 0

    # Conjugate posterior (univariate case)
    prior_prec = 1.0 / sigma0_sq
    likelihood_prec = sum_x_sq / sigma_sq
    post_prec = prior_prec + likelihood_prec

    mu_post = (prior_prec * mu0 + likelihood_prec * ols_beta) / post_prec
    sigma_sq_post = 1.0 / post_prec

    return mu_post, sigma_sq_post

if __name__ == '__main__':
    import random
    random.seed(42)

    # Generate data from y = 2*x + noise
    true_beta = 2.0
    X = [float(i) / 10.0 for i in range(1, 21)]
    y = [true_beta * x + random.gauss(0, 0.5) for x in X]

    # Weak prior: μ₀=0, σ₀²=100 (very uncertain)
    mu_weak, sigma_sq_weak = bayesian_linreg_conjugate(X, y, mu0=0.0, sigma0_sq=100.0, sigma_sq=0.5)

    # Strong prior: μ₀=1.5, σ₀²=0.1 (centered near wrong value)
    mu_strong, sigma_sq_strong = bayesian_linreg_conjugate(X, y, mu0=1.5, sigma0_sq=0.1, sigma_sq=0.5)

    # OLS estimate (no prior)
    sum_x = sum(X)
    sum_y = sum(y)
    sum_xy = sum(x * yv for x, yv in zip(X, y))
    sum_x_sq = sum(x ** 2 for x in X)
    n = len(X)
    ols_beta = (n * sum_xy - sum_x * sum_y) / (n * sum_x_sq - sum_x ** 2)

    # Assertions
    # Weak prior posterior mean should be close to OLS (weak prior is barely influential)
    assert abs(mu_weak - ols_beta) < 0.5, f"Weak prior should be close to OLS, got {mu_weak} vs {ols_beta}"

    # Strong prior posterior mean should be pulled toward prior mean (strong prior is influential)
    assert mu_strong > 1.5 and mu_strong < ols_beta, f"Strong prior should pull mean toward 1.5, got {mu_strong}"

    # Posterior variance should shrink with data compared to prior
    assert sigma_sq_weak < 100.0, f"Weak prior posterior var should shrink from 100.0, got {sigma_sq_weak}"
    assert sigma_sq_strong < 0.1, f"Strong prior posterior var should shrink from 0.1, got {sigma_sq_strong}"

    # Both posteriors should be closer to true beta than completely wrong prior
    assert abs(mu_weak - true_beta) < 1.0, f"Posterior mean should be reasonable, got {mu_weak} vs {true_beta}"

    # Posterior mean should be between prior mean and OLS (convex combination property)
    # For weak prior: should be closer to OLS
    # For strong prior: should be closer to prior mean (1.5) but pulled by data
    assert 1.5 < mu_strong < ols_beta, f"Strong prior posterior should be between prior and data, got {mu_strong}"

    print("PASS")
