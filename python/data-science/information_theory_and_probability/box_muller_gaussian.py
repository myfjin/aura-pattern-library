"""
Box-Muller transform: generate Gaussian-distributed samples from uniform random variables.

Core idea: Given two independent Uniform(0, 1) variables U1 and U2, compute
Z1 = sqrt(-2 * log(U1)) * cos(2π * U2) and Z2 = sqrt(-2 * log(U1)) * sin(2π * U2).
Both Z1 and Z2 are independent standard Normal(0, 1).

Use when: generating Gaussian random variables without scipy, implementing statistical
algorithms that need normal samples, seeding or validating normal distributions.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List, Tuple


def box_muller_pair() -> Tuple[float, float]:
    """Generate one pair of independent standard normal random variables."""
    u1 = random.random()
    u2 = random.random()

    # Ensure u1 is not exactly 0 (log(0) is undefined)
    if u1 < 1e-10:
        u1 = 1e-10

    r = math.sqrt(-2 * math.log(u1))
    theta = 2 * math.pi * u2

    z1 = r * math.cos(theta)
    z2 = r * math.sin(theta)

    return z1, z2


def generate_gaussians(n: int) -> List[float]:
    """Generate n Gaussian samples using Box-Muller."""
    samples = []
    for _ in range(n // 2):
        z1, z2 = box_muller_pair()
        samples.extend([z1, z2])
    # If n is odd, generate one more pair and use one value
    if n % 2 == 1:
        z1, z2 = box_muller_pair()
        samples.append(z1)
    return samples[:n]


def empirical_mean(samples: List[float]) -> float:
    """Compute sample mean."""
    return sum(samples) / len(samples) if samples else 0.0


def empirical_variance(samples: List[float]) -> float:
    """Compute sample variance."""
    if len(samples) < 2:
        return 0.0
    mean = empirical_mean(samples)
    return sum((x - mean) ** 2 for x in samples) / (len(samples) - 1)


def empirical_skewness(samples: List[float]) -> float:
    """Compute sample skewness (third standardized moment)."""
    if len(samples) < 3:
        return 0.0
    mean = empirical_mean(samples)
    std = math.sqrt(empirical_variance(samples))
    if std < 1e-10:
        return 0.0
    third_moment = sum((x - mean) ** 3 for x in samples) / len(samples)
    return third_moment / (std ** 3)


def coverage_percentile(samples: List[float], num_stds: float) -> float:
    """
    Compute empirical coverage: fraction of samples within num_stds standard deviations of mean.
    E.g., num_stds=1 should give ~68% for a normal distribution.
    """
    mean = empirical_mean(samples)
    std = math.sqrt(empirical_variance(samples))
    within = sum(1 for x in samples if abs(x - mean) <= num_stds * std)
    return within / len(samples) if samples else 0.0


if __name__ == "__main__":
    random.seed(42)

    # Generate large sample
    n = 10000
    samples = generate_gaussians(n)

    # Test 1: Mean should be close to 0
    emp_mean = empirical_mean(samples)
    assert abs(emp_mean) < 0.05, f"Mean should be ~0, got {emp_mean}"

    # Test 2: Variance should be close to 1
    emp_var = empirical_variance(samples)
    assert 0.95 < emp_var < 1.05, f"Variance should be ~1, got {emp_var}"

    # Test 3: Skewness should be close to 0 (normal is symmetric)
    emp_skew = empirical_skewness(samples)
    assert abs(emp_skew) < 0.1, f"Skewness should be ~0, got {emp_skew}"

    # Test 4: Empirical rule ~ 68% within 1σ
    coverage_1sigma = coverage_percentile(samples, 1.0)
    assert 0.65 < coverage_1sigma < 0.72, (
        f"Coverage at 1σ should be ~68%, got {100*coverage_1sigma:.1f}%"
    )

    # Test 5: Empirical rule ~ 95% within 2σ
    coverage_2sigma = coverage_percentile(samples, 2.0)
    assert 0.93 < coverage_2sigma < 0.97, (
        f"Coverage at 2σ should be ~95%, got {100*coverage_2sigma:.1f}%"
    )

    # Test 6: Empirical rule ~ 99.7% within 3σ
    coverage_3sigma = coverage_percentile(samples, 3.0)
    assert 0.99 < coverage_3sigma < 1.0, (
        f"Coverage at 3σ should be ~99.7%, got {100*coverage_3sigma:.1f}%"
    )

    # Test 7: Negative values should be present (symmetric around 0)
    negatives = sum(1 for x in samples if x < 0)
    positives = sum(1 for x in samples if x > 0)
    assert negatives > 0 and positives > 0, "Should have both positive and negative values"
    # Roughly balanced
    ratio = min(negatives, positives) / max(negatives, positives)
    assert ratio > 0.45, f"Positive/negative balance off: {negatives} vs {positives}"

    print("Box-Muller Gaussian generation: all assertions PASS")
