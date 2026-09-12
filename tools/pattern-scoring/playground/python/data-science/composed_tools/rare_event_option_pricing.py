"""
Rare-Event Option Pricing — importance sampling where naive Monte Carlo goes blind.

CROSS-SPHERE COMPOSED PATTERN: black_scholes_monte_carlo (Econometrics & Finance)
x metropolis_hastings_mcmc / importance_sampling (Statistical Modeling) — embedding
bridge 0.532, found 2026-07-08. A deep out-of-the-money option's payoff almost
never triggers: naive MC with thousands of paths sees ~zero hits and prices it as
0 (or one wild outlier). Importance sampling SHIFTS the sampling drift toward the
payoff region and re-weights by the likelihood ratio — a thousand tilted paths
beat a million blind ones, verified against the Black-Scholes closed form (the
oracle this composition is judged by).

Human logic of the name: the payoff is a RARE EVENT; you price it by going to
where it lives instead of waiting for it to visit you.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import Tuple

S0, K, R, SIGMA, T = 100.0, 200.0, 0.02, 0.2, 1.0   # deep OTM call


def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def black_scholes_call() -> float:
    d1 = (math.log(S0 / K) + (R + SIGMA**2 / 2) * T) / (SIGMA * math.sqrt(T))
    d2 = d1 - SIGMA * math.sqrt(T)
    return S0 * norm_cdf(d1) - K * math.exp(-R * T) * norm_cdf(d2)


def terminal_price(z: float) -> float:
    return S0 * math.exp((R - SIGMA**2 / 2) * T + SIGMA * math.sqrt(T) * z)


def naive_mc(n: int, rng: random.Random) -> float:
    disc = math.exp(-R * T)
    total = 0.0
    for _ in range(n):
        total += max(terminal_price(rng.gauss(0, 1)) - K, 0.0)
    return disc * total / n


def importance_sampled_mc(n: int, rng: random.Random) -> Tuple[float, float]:
    """Sample Z ~ N(theta, 1) with theta aimed at the strike, re-weight by the
    likelihood ratio w(Z) = exp(-theta*Z + theta^2/2). Returns (price, ESS)."""
    theta = (math.log(K / S0) - (R - SIGMA**2 / 2) * T) / (SIGMA * math.sqrt(T))
    disc = math.exp(-R * T)
    vals = []
    for _ in range(n):
        z = rng.gauss(theta, 1.0)
        w = math.exp(-theta * z + theta**2 / 2)
        vals.append(disc * max(terminal_price(z) - K, 0.0) * w)
    mean = sum(vals) / n
    var = sum((v - mean) ** 2 for v in vals) / (n - 1)
    se = math.sqrt(var / n)
    # NOTE: raw-weight ESS is the WRONG diagnostic here — it measures precision
    # for E[1] under the shift, but the payoff zeroes the region where weights
    # explode. The estimator's own standard error is the honest precision.
    return mean, se


if __name__ == "__main__":
    random.seed(42)
    truth = black_scholes_call()
    n = 2000
    rng_naive = random.Random(42)
    rng_is = random.Random(42)

    naive = naive_mc(n, rng_naive)
    is_price, se = importance_sampled_mc(n, rng_is)

    err_naive = abs(naive - truth) / truth
    err_is = abs(is_price - truth) / truth
    print(f"Black-Scholes truth: {truth:.6f}")
    print(f"naive MC  (n={n}): {naive:.6f}  rel err {err_naive:.0%}")
    print(f"IS MC     (n={n}): {is_price:.6f}  rel err {err_is:.1%} · SE/truth {se/truth:.1%}")

    # The composed claim, measured against the closed-form oracle:
    assert err_is < 0.10, f"importance sampling should land within 10%: {err_is:.1%}"
    assert err_naive > 3 * err_is, \
        f"naive MC must be visibly blind here: {err_naive:.0%} vs IS {err_is:.1%}"
    assert se / truth < 0.10, f"estimator SE should be under 10% of truth: {se/truth:.1%}"
    print("rare_event_option_pricing.py PASS")
