"""
Quantile Binning Pattern.

Partitions a continuous numeric column into equal-frequency bins (quantile-based)
vs equal-width bins. Core idea: quantile binning preserves bin counts (roughly equal)
even on skewed data; equal-width creates imbalanced bins on skew.

When to use: discretizing continuous features, handling skewed distributions,
creating balanced categorical features, non-uniform binning.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple


def quantile_binning(data: List[float], n_bins: int) -> List[int]:
    """
    Partition data into equal-frequency (quantile-based) bins.
    Args:
        data: List of numeric values
        n_bins: Number of bins
    Returns:
        List of bin labels (0 to n_bins-1) for each data point
    """
    sorted_data = sorted(enumerate(data), key=lambda x: x[1])
    n = len(data)
    bin_size = n / n_bins

    # Create bin edges: quantile cutoffs
    edges = []
    for i in range(1, n_bins):
        idx = min(int(i * bin_size), n - 1)
        edges.append(sorted_data[idx][1])

    # Assign bins based on edges
    result = [0] * n
    for original_idx, value in sorted_data:
        bin_num = 0
        for edge in edges:
            if value >= edge:
                bin_num += 1
        result[original_idx] = bin_num

    return result


def equal_width_binning(data: List[float], n_bins: int) -> List[int]:
    """
    Partition data into equal-width bins.
    Args:
        data: List of numeric values
        n_bins: Number of bins
    Returns:
        List of bin labels (0 to n_bins-1) for each data point
    """
    min_val = min(data)
    max_val = max(data)
    bin_width = (max_val - min_val) / n_bins

    result = []
    for x in data:
        if x == max_val:
            bin_num = n_bins - 1
        else:
            bin_num = int((x - min_val) / bin_width)
        result.append(bin_num)

    return result


if __name__ == "__main__":
    import random

    random.seed(42)

    # Synthetic skewed data: exponential-like distribution
    # Most values small, few large values
    data_skewed = [random.expovariate(0.3) for _ in range(100)]

    n_bins = 4

    # Quantile binning
    quantile_bins = quantile_binning(data_skewed, n_bins)
    quantile_counts = [quantile_bins.count(i) for i in range(n_bins)]

    # Equal-width binning
    equal_bins = equal_width_binning(data_skewed, n_bins)
    equal_counts = [equal_bins.count(i) for i in range(n_bins)]

    # Verify quantile bins are roughly equal-frequency
    # Allow some variance (binning is discrete)
    expected_per_bin = len(data_skewed) / n_bins
    for count in quantile_counts:
        assert 15 <= count <= 35, f"Quantile bin imbalanced: {quantile_counts}"

    # Verify equal-width bins on skewed data are imbalanced
    # (early bins packed, late bins sparse)
    first_half = sum(equal_counts[:n_bins // 2])
    second_half = sum(equal_counts[n_bins // 2 :])
    assert (
        first_half > second_half * 1.5
    ), f"Equal-width should be imbalanced on skew: {equal_counts}"

    # Verify all bins are used
    assert len(set(quantile_bins)) == n_bins, "Not all quantile bins used"
    assert len(set(equal_bins)) == n_bins, "Not all equal bins used"

    print("quantile_binning.py: PASS")
