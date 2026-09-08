"""
Inverse-transform sampling: generate samples from an arbitrary distribution via inverse CDF.

Core idea: If U ~ Uniform(0, 1) and F^{-1} is the inverse CDF, then X = F^{-1}(U) is distributed
according to the target distribution. For tractable F^{-1}, this is efficient and exact.

Use when: sampling from a distribution with known CDF, generating random variates, creating
synthetic data from a specified distribution.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List, Callable


def exponential_inverse_cdf(u: float, rate: float) -> float:
    """Inverse CDF of Exponential(rate). F^{-1}(u) = -log(1-u) / rate.

    rate must be > 0 (an exponential rate); the guard mirrors the exemplary u-guard.
    The previously-shipped version guarded u but NOT rate, silently returning negative
    waiting-times on rate<0 — snapshot preserved as inverse_transform_sampling.BROKEN.py.
    """
    if u <= 0 or u >= 1:
        raise ValueError(f"u must be in (0, 1), got {u}")
    if not (rate > 0):
        raise ValueError(f"rate must be > 0, got {rate}")
    return -math.log(1 - u) / rate


def piecewise_inverse_cdf(u: float) -> float:
    """
    Custom piecewise CDF inverse with higher density on [0, 1].
    Define F(x) as:
      F(x) = 2*x/3       for x in [0, 1]  (mass 2/3 on [0,1])
      F(x) = 2/3 + (x-1)/3 for x in [1, 2] (mass 1/3 on [1,2])
    So F^{-1}(u) = 3*u/2 for u in [0, 2/3], and F^{-1}(u) = 1 + 3*(u - 2/3) for u in [2/3, 1]

    u must be in [0, 1); 1.0 is excluded because the inverse-CDF contract is
    undefined at exactly 1 (DOMAIN_SILENT — previously any u out of range was
    silently absorbed).
    """
    if not (u == u):  # NaN
        raise ValueError(f"AURA-E010: u must be in [0, 1), got {u}")
    if u < 0.0 or u >= 1.0:
        raise ValueError(f"AURA-E010: u must be in [0, 1), got {u}")
    if u < 2.0 / 3.0:
        return 3 * u / 2.0
    else:
        return 1 + 3 * (u - 2.0 / 3.0)


def sample_from_inverse_transform(
    inverse_cdf: Callable[[float], float],
    n: int
) -> List[float]:
    """Generate n samples using inverse-transform method."""
    samples = []
    for _ in range(n):
        u = random.random()
        x = inverse_cdf(u)
        samples.append(x)
    return samples


def empirical_mean(samples: List[float]) -> float:
    """Compute sample mean."""
    return sum(samples) / len(samples) if samples else 0.0


def empirical_variance(samples: List[float]) -> float:
    """Compute sample variance."""
    if len(samples) < 2:
        return 0.0
    mean = empirical_mean(samples)
    return sum((x - mean) ** 2 for x in samples) / (len(samples) - 1)


def empirical_quantile(samples: List[float], q: float) -> float:
    """Compute empirical quantile (e.g., q=0.25 for 25th percentile).

    q must be in [0, 1); 1.0 is excluded because the inverse-CDF contract is
    undefined there. Before this guard, the min-clamp silently absorbed any
    q >= 1 into the top sample (DOMAIN_SILENT).
    """
    if not (q == q):  # NaN
        raise ValueError(f"AURA-E010: q must be in [0, 1), got {q}")
    if q < 0.0 or q >= 1.0:
        raise ValueError(f"AURA-E010: q must be in [0, 1), got {q}")
    sorted_samples = sorted(samples)
    idx = int(q * len(sorted_samples))
    return sorted_samples[min(idx, len(sorted_samples) - 1)]


if __name__ == "__main__":
    random.seed(42)

    # ========== Exponential Distribution ==========
    # Known moments: mean = 1/rate, variance = 1/rate^2
    rate = 2.0
    true_mean_exp = 1.0 / rate
    true_var_exp = 1.0 / (rate ** 2)

    # Generate large sample
    n_large = 10000
    samples_exp = sample_from_inverse_transform(
        lambda u: exponential_inverse_cdf(u, rate),
        n_large
    )

    emp_mean_exp = empirical_mean(samples_exp)
    emp_var_exp = empirical_variance(samples_exp)

    # Test 1: Sample mean close to true mean
    assert abs(emp_mean_exp - true_mean_exp) < 0.05, (
        f"Exponential mean: empirical {emp_mean_exp} vs true {true_mean_exp}"
    )

    # Test 2: Sample variance close to true variance
    assert abs(emp_var_exp - true_var_exp) < 0.05, (
        f"Exponential variance: empirical {emp_var_exp} vs true {true_var_exp}"
    )

    # Test 3: All samples are non-negative (exponential support)
    assert all(x >= 0 for x in samples_exp), "Exponential samples should be non-negative"

    # Test 4: Sample quantiles reasonable (median ~= 0.693 * 1/rate for exponential)
    q50_exp = empirical_quantile(samples_exp, 0.5)
    expected_median_exp = math.log(2) / rate
    assert abs(q50_exp - expected_median_exp) < 0.05, (
        f"Exponential median: empirical {q50_exp} vs expected {expected_median_exp}"
    )

    # ========== Piecewise Distribution ==========
    # F(x) = 2x/3 on [0,1] (density 2/3), then 2/3 + (x-1)/3 on [1,2] (density 1/3)
    # This defines a distribution with higher density on [0,1]

    n_piecewise = 10000
    samples_piecewise = sample_from_inverse_transform(piecewise_inverse_cdf, n_piecewise)

    # Test 5: Support is [0, 2]
    assert all(0 <= x <= 2 for x in samples_piecewise), f"Piecewise samples should be in [0, 2], got {min(samples_piecewise)}, {max(samples_piecewise)}"

    # Test 6: More samples in [0, 1] than in [1, 2] (by design: 2/3 vs 1/3)
    count_first_half = sum(1 for x in samples_piecewise if x <= 1)
    count_second_half = sum(1 for x in samples_piecewise if x > 1)
    assert count_first_half > count_second_half, (
        f"More samples in [0,1] than [1,2]: {count_first_half} vs {count_second_half}"
    )
    assert 0.6 < count_first_half / n_piecewise < 0.75, "Expected ~2/3 in [0,1]"

    # Test 7: Empirical CDF at x=1 should be ~2/3 (by design: F(1) = 2/3)
    q_at_one = sum(1 for x in samples_piecewise if x <= 1) / n_piecewise
    assert abs(q_at_one - 2.0/3.0) < 0.05, f"Empirical CDF at x=1 should be ~2/3, got {q_at_one}"

    # Test 8: Mean of piecewise should be computable analytically
    # pdf on [0,1]: 2/3, on [1,2]: 1/3
    # E[X] = integral from 0 to 1 of x * (2/3) dx + integral from 1 to 2 of x * (1/3) dx
    #      = (2/3) * (1/2) + (1/3) * (3/2) = 1/3 + 1/2 = 5/6
    emp_mean_pw = empirical_mean(samples_piecewise)
    expected_mean_pw = 5.0 / 6.0
    assert abs(emp_mean_pw - expected_mean_pw) < 0.1, (
        f"Piecewise mean: empirical {emp_mean_pw} vs expected {expected_mean_pw}"
    )

    print("Inverse-transform sampling (exponential + piecewise): all assertions PASS")
