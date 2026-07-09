"""
Mutual information detects nonlinear dependence that Pearson correlation misses.

Core idea: Pearson correlation measures LINEAR association; MI measures ANY dependence.
For y = x^2 + noise on symmetric x, Pearson correlation ≈ 0 but MI > 0 (high dependence).
Both are computed from scratch using binning (discrete approximation).

Use when: detecting nonlinear relationships, comparing linear vs nonlinear association measures,
validating correlation against information-theoretic measures.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List, Tuple
from collections import Counter


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


def pearson_correlation(x: List[float], y: List[float]) -> float:
    """Compute Pearson correlation coefficient."""
    assert len(x) == len(y), "x and y must have same length"
    n = len(x)

    mean_x = empirical_mean(x)
    mean_y = empirical_mean(y)

    cov_xy = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / (n - 1)
    std_x = empirical_std(x)
    std_y = empirical_std(y)

    if std_x < 1e-10 or std_y < 1e-10:
        return 0.0

    return cov_xy / (std_x * std_y)


def binned_entropy(samples: List[float], num_bins: int = 10) -> float:
    """Estimate Shannon entropy from samples using binning."""
    if not samples:
        return 0.0

    # Determine bin edges
    min_val = min(samples)
    max_val = max(samples)
    if min_val == max_val:
        return 0.0

    bin_width = (max_val - min_val) / num_bins
    if bin_width <= 0:
        return 0.0

    # Bin the samples
    bins = []
    for sample in samples:
        bin_idx = min(int((sample - min_val) / bin_width), num_bins - 1)
        bins.append(bin_idx)

    # Compute entropy
    counts = Counter(bins)
    n = len(samples)
    entropy = 0.0
    for count in counts.values():
        p = count / n
        if p > 0:
            entropy -= p * math.log2(p)

    return entropy


def binned_mutual_information(x: List[float], y: List[float], num_bins: int = 10) -> float:
    """
    Estimate mutual information I(X; Y) from samples using binning.
    MI = H(X) + H(Y) - H(X, Y)
    """
    assert len(x) == len(y), "x and y must have same length"

    # Marginal entropies
    h_x = binned_entropy(x, num_bins)
    h_y = binned_entropy(y, num_bins)

    # Joint entropy
    min_x, max_x = min(x), max(x)
    min_y, max_y = min(y), max(y)

    bin_width_x = (max_x - min_x) / num_bins if max_x > min_x else 1
    bin_width_y = (max_y - min_y) / num_bins if max_y > min_y else 1

    if bin_width_x <= 0 or bin_width_y <= 0:
        return 0.0

    joint_bins = []
    for xi, yi in zip(x, y):
        bin_x = min(int((xi - min_x) / bin_width_x), num_bins - 1)
        bin_y = min(int((yi - min_y) / bin_width_y), num_bins - 1)
        joint_bins.append((bin_x, bin_y))

    counts_joint = Counter(joint_bins)
    n = len(x)
    h_xy = 0.0
    for count in counts_joint.values():
        p = count / n
        if p > 0:
            h_xy -= p * math.log2(p)

    # MI = H(X) + H(Y) - H(X, Y)
    mi = h_x + h_y - h_xy

    return max(mi, 0.0)  # MI should be non-negative


def independent_mutual_information_baseline(x_dist: List[float], y_dist: List[float], num_bins: int = 10) -> float:
    """
    Compute MI if x and y were independent (should be ~0).
    This shuffles one variable to break dependence.
    """
    # y_shuffled is independent of x
    y_shuffled = y_dist.copy()
    random.shuffle(y_shuffled)
    return binned_mutual_information(x_dist, y_shuffled, num_bins)


if __name__ == "__main__":
    random.seed(42)

    n = 2000

    # ========== NONLINEAR DEPENDENCY: y = x^2 + noise ==========
    # x is symmetric around 0, so E[x*y] ≈ 0, but y depends strongly on x
    x_nonlinear = [random.gauss(0, 1) for _ in range(n)]
    noise = [random.gauss(0, 0.1) for _ in range(n)]  # Small noise
    y_nonlinear = [xi**2 + noise[i] for i, xi in enumerate(x_nonlinear)]

    # Pearson correlation should be close to 0 (x and x^2 uncorrelated when x is symmetric)
    corr_nonlinear = pearson_correlation(x_nonlinear, y_nonlinear)
    assert abs(corr_nonlinear) < 0.15, (
        f"Pearson correlation should be ~0 for y=x^2: got {corr_nonlinear}"
    )

    # But MI should be HIGH (strong dependence)
    mi_nonlinear = binned_mutual_information(x_nonlinear, y_nonlinear, num_bins=15)
    assert mi_nonlinear > 1.0, (
        f"MI should be high for y=x^2: got {mi_nonlinear}"
    )

    # Test 1: MI detects nonlinear dependence
    print(f"✓ Nonlinear y=x^2: Pearson r ≈ {corr_nonlinear:.3f}, MI ≈ {mi_nonlinear:.3f} bits")
    assert mi_nonlinear > abs(corr_nonlinear), "MI should exceed |Pearson r| for nonlinear dependence"

    # ========== INDEPENDENCE: y is random noise ==========
    y_independent = [random.gauss(0, 1) for _ in range(n)]

    corr_indep = pearson_correlation(x_nonlinear, y_independent)
    mi_indep = binned_mutual_information(x_nonlinear, y_independent, num_bins=15)

    # Test 2: Both measures should be low for independence
    assert abs(corr_indep) < 0.15, "Pearson r should be ~0 for independent variables"
    assert mi_indep < 0.2, f"MI should be low for independent variables, got {mi_indep}"

    # Test 3: MI baseline (shuffled) is near zero
    mi_baseline = independent_mutual_information_baseline(x_nonlinear, y_nonlinear, num_bins=15)
    assert mi_baseline < 0.2, f"MI of shuffled should be ~0, got {mi_baseline}"

    # Test 4: Strong linear dependence: y = 2*x + noise
    y_linear = [2 * xi + random.gauss(0, 0.1) for xi in x_nonlinear]
    corr_linear = pearson_correlation(x_nonlinear, y_linear)
    mi_linear = binned_mutual_information(x_nonlinear, y_linear, num_bins=15)

    # Both should be high
    assert corr_linear > 0.95, f"Linear dependence: Pearson r should be ~1, got {corr_linear}"
    assert mi_linear > 1.0, f"Linear dependence: MI should be high, got {mi_linear}"

    print(f"✓ Linear y=2x: Pearson r ≈ {corr_linear:.3f}, MI ≈ {mi_linear:.3f} bits")

    # Test 5: Nonlinear MI substantially exceeds linear Pearson r
    assert mi_nonlinear > 2 * abs(corr_nonlinear), (
        f"Nonlinear MI should be much larger than |Pearson r|: {mi_nonlinear} vs {abs(corr_nonlinear)}"
    )

    print("Nonlinear dependence (mutual information): all assertions PASS")
