"""
Pearson Correlation Matrix Pattern.

Computes pairwise Pearson correlation coefficients between all numeric columns
from scratch. Core idea: measure linear association; correlation is covariance
normalized by standard deviations. Symmetric matrix with 1s on diagonal.

When to use: exploratory data analysis to identify relationships, feature
selection (drop highly correlated features), multicollinearity detection.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple
import math


def mean_variance(data: List[float]) -> Tuple[float, float]:
    """Compute mean and sample variance."""
    n = len(data)
    if n == 0:
        raise ValueError("Empty data")
    mean_val = sum(data) / n
    variance = sum((x - mean_val) ** 2 for x in data) / (n - 1)
    return mean_val, variance


def pearson_correlation(x: List[float], y: List[float]) -> float:
    """Compute Pearson correlation coefficient between two vectors."""
    n = len(x)
    if n != len(y):
        raise ValueError("Length mismatch")
    if n < 2:
        raise ValueError("Need at least 2 points")

    mean_x = sum(x) / n
    mean_y = sum(y) / n

    covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / (n - 1)

    var_x = sum((xi - mean_x) ** 2 for xi in x) / (n - 1)
    var_y = sum((yi - mean_y) ** 2 for yi in y) / (n - 1)

    std_x = math.sqrt(var_x)
    std_y = math.sqrt(var_y)

    if std_x == 0 or std_y == 0:
        return 0.0

    return covariance / (std_x * std_y)


def correlation_matrix(data: List[List[float]]) -> List[List[float]]:
    """
    Compute full correlation matrix from list of columns.
    Args:
        data: List of columns, each column is List[float]
    Returns:
        n x n symmetric correlation matrix
    """
    n_cols = len(data)
    if n_cols == 0:
        return []

    # Verify all columns same length
    n_rows = len(data[0])
    for col in data:
        if len(col) != n_rows:
            raise ValueError("All columns must have same length")

    # Compute correlation matrix
    corr_matrix = [[0.0] * n_cols for _ in range(n_cols)]
    for i in range(n_cols):
        for j in range(n_cols):
            corr_matrix[i][j] = pearson_correlation(data[i], data[j])

    return corr_matrix


if __name__ == "__main__":
    import random

    random.seed(42)

    # Synthetic data with planted structure
    # x = [1, 2, 3, ...], y = 2*x (perfect positive correlation)
    # z = random (no correlation)
    x = list(range(1, 21))  # 1 to 20
    y = [2 * val for val in x]  # y = 2*x, perfect correlation
    z = [random.uniform(0, 100) for _ in range(20)]  # random

    data = [x, y, z]
    corr_mat = correlation_matrix(data)

    # Verify diagonal is all 1s (corr with self)
    for i in range(3):
        assert abs(corr_mat[i][i] - 1.0) < 1e-6, f"Diagonal {i} not 1: {corr_mat[i][i]}"

    # Verify symmetric
    for i in range(3):
        for j in range(3):
            assert abs(corr_mat[i][j] - corr_mat[j][i]) < 1e-6, f"Not symmetric at ({i},{j})"

    # Verify x and y are perfectly correlated (slope > 0)
    assert abs(corr_mat[0][1] - 1.0) < 1e-6, f"x-y correlation not 1: {corr_mat[0][1]}"
    assert abs(corr_mat[1][0] - 1.0) < 1e-6, f"y-x correlation not 1: {corr_mat[1][0]}"

    # Verify z has near-zero correlation with x and y
    assert abs(corr_mat[0][2]) < 0.4, f"x-z should be low: {corr_mat[0][2]}"
    assert abs(corr_mat[1][2]) < 0.4, f"y-z should be low: {corr_mat[1][2]}"

    print("pearson_correlation_matrix.py: PASS")
