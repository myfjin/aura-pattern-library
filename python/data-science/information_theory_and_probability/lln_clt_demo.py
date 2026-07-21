"""
Law of Large Numbers and Central Limit Theorem: asymptotic behavior of sample means.

Core idea: LLN: sample mean converges to population mean as n → ∞.
CLT: the distribution of sample means approaches normal, regardless of source distribution.
Standardized sample means satisfy ~68% within 1σ, ~95% within 2σ, ~99.7% within 3σ.

Use when: understanding sampling distributions, validating statistical inference,
demonstrating convergence rates, checking normality of sample statistics.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List, Tuple


def sample_means(source_distribution: List[float], sample_size: int, num_samples: int) -> List[float]:
    """
    Draw num_samples bootstrap samples of size sample_size from source_distribution.
    Return the mean of each sample.
    """
    means = []
    for _ in range(num_samples):
        sample = [random.choice(source_distribution) for _ in range(sample_size)]
        means.append(sum(sample) / len(sample))
    return means


def empirical_mean(samples: List[float]) -> float:
    """Compute sample mean."""
    return sum(samples) / len(samples) if samples else 0.0


def empirical_std(samples: List[float]) -> float:
    """Compute sample standard deviation."""
    if len(samples) < 2:
        return 0.0
    mean = empirical_mean(samples)
    variance = sum((x - mean) ** 2 for x in samples) / (len(samples) - 1)
    return math.sqrt(variance)




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_coverage_percentile(true_mean, num_stds):
    v = []
    if isinstance(true_mean, (int, float)) and not math.isfinite(true_mean):
        v.append(f"AURA-E008: true_mean must be finite, got {true_mean}")
    if isinstance(true_mean, (int, float)) and true_mean <= 0:
        v.append(f"AURA-E009: true_mean must be > 0, got {true_mean}")
    if isinstance(num_stds, (int, float)) and not math.isfinite(num_stds):
        v.append(f"AURA-E008: num_stds must be finite, got {num_stds}")
    if isinstance(num_stds, (int, float)) and num_stds <= 0:
        v.append(f"AURA-E009: num_stds must be > 0, got {num_stds}")
    if v:
        raise AuraInputError(v)

def coverage_percentile(samples: List[float], true_mean: float, num_stds: float) -> float:
    """
    Compute empirical coverage: fraction of samples within num_stds standard deviations of true_mean.
    E.g., num_stds=1 should give ~68% for a normal distribution.
    """
    _aura_validate_coverage_percentile(true_mean, num_stds)
    sample_std = empirical_std(samples)
    if sample_std < 1e-10:
        return 0.0
    within = sum(1 for x in samples if abs(x - true_mean) <= num_stds * sample_std)
    return within / len(samples) if samples else 0.0


def skewness(samples: List[float]) -> float:
    """Compute sample skewness (third standardized moment)."""
    if len(samples) < 3:
        return 0.0
    mean = empirical_mean(samples)
    std = empirical_std(samples)
    if std < 1e-10:
        return 0.0
    third_moment = sum((x - mean) ** 3 for x in samples) / len(samples)
    return third_moment / (std ** 3)


if __name__ == "__main__":
    random.seed(42)

    # ========== SKEWED SOURCE DISTRIBUTION ==========
    # Exponential is heavily skewed; CLT should still normalize sample means
    # Generate source distribution: exponential(rate=1)
    lambda_exp = 1.0
    true_mean_exp = 1.0 / lambda_exp  # E[X] = 1
    true_std_exp = 1.0 / lambda_exp   # SD[X] = 1

    # Create a large pool of exponential samples for resampling
    source_pool = [random.expovariate(lambda_exp) for _ in range(10000)]

    # Verify source distribution properties
    source_mean = empirical_mean(source_pool)
    source_std = empirical_std(source_pool)
    source_skew = skewness(source_pool)

    assert 0.9 < source_mean < 1.1, f"Source mean should be ~1, got {source_mean}"
    assert source_skew > 1.5, f"Exponential should be skewed, got skewness {source_skew}"
    print(f"Source: mean≈{source_mean:.3f}, std≈{source_std:.3f}, skew≈{source_skew:.3f}")

    # ========== LAW OF LARGE NUMBERS ==========
    # As sample size increases, sample mean converges to population mean
    sample_sizes = [10, 50, 100, 500]
    errors = []

    for n in sample_sizes:
        means = sample_means(source_pool, n, 300)  # 300 independent samples of size n
        empirical_sample_mean = empirical_mean(means)
        error = abs(empirical_sample_mean - true_mean_exp)
        errors.append(error)
        print(f"  n={n:3d}: sample mean={empirical_sample_mean:.4f}, error={error:.4f}")

    # Test 1: Larger sample sizes generally have smaller error (LLN)
    # Note: individual sample errors fluctuate, but trend should be downward over large sizes
    assert errors[-1] < errors[0], f"LLN: final error should be < initial error, got {errors}"
    print("✓ LLN: error decreases with sample size")

    # ========== CENTRAL LIMIT THEOREM ==========
    # The distribution of sample means approaches normal, regardless of skewness

    # Small sample size (n=10): sample means still somewhat skewed
    means_small = sample_means(source_pool, 10, 500)
    skew_small = skewness(means_small)

    # Moderate sample size (n=50): sample means more normal
    means_medium = sample_means(source_pool, 50, 500)
    skew_medium = skewness(means_medium)

    # Large sample size (n=500): sample means nearly normal
    means_large = sample_means(source_pool, 500, 500)
    skew_large = skewness(means_large)

    print(f"\nSkewness of sample means:")
    print(f"  n=10:  skew={skew_small:.3f}")
    print(f"  n=50:  skew={skew_medium:.3f}")
    print(f"  n=500: skew={skew_large:.3f}")

    # Test 2: CLT reduces skewness as n increases
    assert skew_small > skew_medium > skew_large, (
        f"CLT: skewness should decrease: {skew_small} > {skew_medium} > {skew_large}"
    )
    print("✓ CLT: skewness of sample means decreases toward normal as n increases")

    # ========== EMPIRICAL RULE (68-95-99.7) ==========
    # For large n, ~68% within 1σ, ~95% within 2σ, ~99.7% within 3σ

    cov_1sig = coverage_percentile(means_large, true_mean_exp, 1.0)
    cov_2sig = coverage_percentile(means_large, true_mean_exp, 2.0)
    cov_3sig = coverage_percentile(means_large, true_mean_exp, 3.0)

    print(f"\nEmpirical rule coverage (n=500):")
    print(f"  1σ: {100*cov_1sig:.1f}% (expect ~68%)")
    print(f"  2σ: {100*cov_2sig:.1f}% (expect ~95%)")
    print(f"  3σ: {100*cov_3sig:.1f}% (expect ~99.7%)")

    # Test 3: Large n should satisfy empirical rule
    assert 0.60 < cov_1sig < 0.76, f"1σ coverage should be ~68%, got {100*cov_1sig:.1f}%"
    assert 0.92 < cov_2sig < 0.98, f"2σ coverage should be ~95%, got {100*cov_2sig:.1f}%"
    assert 0.98 < cov_3sig < 1.00, f"3σ coverage should be ~99.7%, got {100*cov_3sig:.1f}%"
    print("✓ Empirical rule: coverage bands match normal expectations")

    # ========== COMPARISON: small n does NOT follow empirical rule ==========
    cov_1sig_small = coverage_percentile(means_small, true_mean_exp, 1.0)
    cov_2sig_small = coverage_percentile(means_small, true_mean_exp, 2.0)

    print(f"\nEmpirical rule coverage (n=10):")
    print(f"  1σ: {100*cov_1sig_small:.1f}%")
    print(f"  2σ: {100*cov_2sig_small:.1f}%")

    # Test 4: Small n has worse coverage (not yet normal)
    # n=10 is too small to be fully normal, so coverage can be off
    # But coverage should improve with n
    assert cov_1sig_small < cov_1sig or cov_2sig_small < cov_2sig, (
        "Coverage should improve with larger n"
    )

    print("✓ LLN + CLT demo: all assertions PASS")
