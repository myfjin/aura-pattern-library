"""
Rank Correlation (Spearman's rho & Kendall's tau)

Computes Spearman's rank correlation (Pearson on ranks) and Kendall's tau (proportion of concordant pairs).
Both measure association between two ordinal or continuous variables.

Use this when data may be non-linearly related, has outliers, or contains ordinal rankings.
Rank correlations are more robust than Pearson to non-linear monotone relationships.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


def rank_data(data: List[float]) -> List[float]:
    """Assign ranks to data (1 = smallest, n = largest). Ties get average rank."""
    n = len(data)
    indices = list(range(n))
    indices.sort(key=lambda i: data[i])

    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        # Find tied values
        while j < n and data[indices[j]] == data[indices[i]]:
            j += 1
        # Assign average rank to ties
        avg_rank = (i + j + 1) / 2.0
        for k in range(i, j):
            ranks[indices[k]] = avg_rank
        i = j

    return ranks


def spearman_correlation(x: List[float], y: List[float]) -> float:
    """Compute Spearman's rho: Pearson correlation on ranks."""
    assert len(x) == len(y)
    n = len(x)

    # Rank both variables
    rank_x = rank_data(x)
    rank_y = rank_data(y)

    # Pearson correlation on ranks
    mean_rank_x = sum(rank_x) / n
    mean_rank_y = sum(rank_y) / n

    num = sum((rx - mean_rank_x) * (ry - mean_rank_y) for rx, ry in zip(rank_x, rank_y))
    var_x = sum((rx - mean_rank_x) ** 2 for rx in rank_x)
    var_y = sum((ry - mean_rank_y) ** 2 for ry in rank_y)

    if var_x == 0 or var_y == 0:
        return 0.0

    return num / math.sqrt(var_x * var_y)


def kendall_tau(x: List[float], y: List[float]) -> float:
    """
    Compute Kendall's tau: proportion of concordant pairs minus discordant pairs.
    tau = (concordant - discordant) / (n choose 2)
    """
    assert len(x) == len(y)
    n = len(x)

    concordant = 0
    discordant = 0

    for i in range(n):
        for j in range(i + 1, n):
            # Check sign of (xi - xj) * (yi - yj)
            x_diff = x[i] - x[j]
            y_diff = y[i] - y[j]

            if x_diff * y_diff > 0:
                concordant += 1
            elif x_diff * y_diff < 0:
                discordant += 1
            # Tied pairs don't contribute

    total = concordant + discordant
    if total == 0:
        return 0.0

    return (concordant - discordant) / total


def test_rank_correlation() -> None:
    """
    Test rank correlation:
    - Monotone increasing: rho ≈ 1, tau ≈ 1
    - Independent: rho ≈ 0, tau ≈ 0
    - Known small examples
    """
    random.seed(42)

    # Test 1: Perfectly monotone increasing
    x_perfect = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_perfect = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    rho_perfect = spearman_correlation(x_perfect, y_perfect)
    tau_perfect = kendall_tau(x_perfect, y_perfect)

    assert abs(rho_perfect - 1.0) < 0.01, f"Perfect monotone rho should be 1: {rho_perfect}"
    assert abs(tau_perfect - 1.0) < 0.01, f"Perfect monotone tau should be 1: {tau_perfect}"

    # Test 2: Independent random data
    x_random = [random.uniform(0, 10) for _ in range(100)]
    y_random = [random.uniform(0, 10) for _ in range(100)]

    rho_random = spearman_correlation(x_random, y_random)
    tau_random = kendall_tau(x_random, y_random)

    assert abs(rho_random) < 0.4, f"Random data rho should be near 0: {rho_random}"
    assert abs(tau_random) < 0.4, f"Random data tau should be near 0: {tau_random}"

    # Test 3: Monotone decreasing
    x_decreasing = [1, 2, 3, 4, 5]
    y_decreasing = [5, 4, 3, 2, 1]

    rho_decreasing = spearman_correlation(x_decreasing, y_decreasing)
    tau_decreasing = kendall_tau(x_decreasing, y_decreasing)

    assert abs(rho_decreasing - (-1.0)) < 0.01, f"Perfect decreasing rho should be -1: {rho_decreasing}"
    assert abs(tau_decreasing - (-1.0)) < 0.01, f"Perfect decreasing tau should be -1: {tau_decreasing}"

    print("rank_correlation.py: PASS")


if __name__ == "__main__":
    test_rank_correlation()
