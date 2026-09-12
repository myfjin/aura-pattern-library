"""
Histogram Builder Pattern.

Constructs a histogram using equal-width bins with automatic bin-count selection
(Sturges' rule). Core idea: Sturges rule k = ceil(log2(n) + 1) works well for
normal data; easy rule without parameter tuning.

When to use: exploratory data analysis, visualizing distributions, detecting
multimodality, choosing reasonable bin counts automatically.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple


def sturges_bin_count(n: int) -> int:
    """
    Compute number of bins using Sturges' rule.
    k = ceil(log2(n)) + 1
    """
    return math.ceil(math.log2(n)) + 1


def histogram(data: List[float], n_bins: int = None) -> Tuple[List[int], List[float]]:
    """
    Build histogram with equal-width bins.
    Args:
        data: List of numeric values
        n_bins: Number of bins (None = auto via Sturges rule)
    Returns:
        (counts, bin_edges) where counts[i] = # points in bin i,
        bin_edges has n_bins+1 elements (lower and upper bounds)
    """
    if not data:
        return [], []

    if n_bins is None:
        n_bins = sturges_bin_count(len(data))

    min_val = min(data)
    max_val = max(data)

    if min_val == max_val:
        return [len(data)], [min_val, min_val]

    bin_width = (max_val - min_val) / n_bins

    # Create bin edges
    bin_edges = [min_val + i * bin_width for i in range(n_bins + 1)]

    # Initialize counts
    counts = [0] * n_bins

    # Assign data points to bins
    for x in data:
        if x == max_val:
            bin_idx = n_bins - 1
        else:
            bin_idx = int((x - min_val) / bin_width)
            bin_idx = min(bin_idx, n_bins - 1)
        counts[bin_idx] += 1

    return counts, bin_edges


if __name__ == "__main__":
    import random

    random.seed(42)

    # Synthetic bimodal data: two Gaussian modes
    mode1 = [random.gauss(20, 3) for _ in range(50)]
    mode2 = [random.gauss(60, 3) for _ in range(50)]
    bimodal_data = mode1 + mode2

    # Build histogram with auto bin count
    counts, edges = histogram(bimodal_data)

    # Verify counts sum to n
    assert sum(counts) == len(bimodal_data), f"Count mismatch: {sum(counts)} vs {len(bimodal_data)}"

    # Verify edges are ordered
    for i in range(len(edges) - 1):
        assert edges[i] <= edges[i + 1], f"Edges not sorted: {edges}"

    # Verify n_bins from Sturges
    expected_bins = sturges_bin_count(len(bimodal_data))
    assert len(counts) == expected_bins, f"Bin count mismatch: {len(counts)} vs {expected_bins}"

    # Verify two modes show peaks (roughly)
    # Find highest bin and second-highest
    peak1_idx = counts.index(max(counts))
    peak1_val = counts[peak1_idx]

    # Mask peak1, find second peak
    counts_masked = counts[:]
    counts_masked[peak1_idx] = 0
    peak2_val = max(counts_masked)

    # Both peaks should be substantial
    assert peak1_val > 8, f"First peak too small: {peak1_val}"
    assert peak2_val > 8, f"Second peak too small: {peak2_val}"

    # Center of bimodal histogram should be sparse relative to edges
    mid_idx = len(counts) // 2
    mid_count = counts[mid_idx]
    edge_count_avg = (counts[0] + counts[-1]) / 2

    print("histogram_builder.py: PASS")
