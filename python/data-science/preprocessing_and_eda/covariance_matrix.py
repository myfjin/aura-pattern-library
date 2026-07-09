"""
Covariance Matrix Pattern.

Computes sample covariance between all numeric columns. Core idea: covariance
measures how two variables jointly vary (sign = direction of relationship,
magnitude = strength). Diagonal contains variance of each variable.

When to use: understanding variance structure, multivariate analysis, principal
component analysis setup, detecting correlations with magnitude awareness.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List
import math


def covariance_matrix(data: List[List[float]]) -> List[List[float]]:
    """
    Compute sample covariance matrix.
    Args:
        data: List of columns, each column is List[float]
    Returns:
        n x n symmetric covariance matrix
    """
    n_cols = len(data)
    if n_cols == 0:
        return []

    n_rows = len(data[0])
    if n_rows < 2:
        raise ValueError("Need at least 2 rows")

    for col in data:
        if len(col) != n_rows:
            raise ValueError("All columns must have same length")

    # Compute means
    means = [sum(col) / n_rows for col in data]

    # Compute covariance matrix: cov(i,j) = E[(X_i - mean_i)(X_j - mean_j)]
    cov_matrix = [[0.0] * n_cols for _ in range(n_cols)]

    for i in range(n_cols):
        for j in range(n_cols):
            cov_sum = sum(
                (data[i][k] - means[i]) * (data[j][k] - means[j]) for k in range(n_rows)
            )
            cov_matrix[i][j] = cov_sum / (n_rows - 1)  # sample covariance

    return cov_matrix


if __name__ == "__main__":
    import random

    random.seed(42)

    # Synthetic data with planted structure
    # x: variance ~ 25, y: variance ~ 25, positive covariance
    x = [float(5 + i + random.gauss(0, 1)) for i in range(20)]
    y = [2 * xi + random.gauss(0, 1) for xi in x]  # y ~ 2*x + noise
    z = [random.gauss(50, 5) for _ in range(20)]  # independent

    data = [x, y, z]
    cov_mat = covariance_matrix(data)

    # Verify symmetric
    for i in range(3):
        for j in range(3):
            assert abs(cov_mat[i][j] - cov_mat[j][i]) < 1e-6, f"Not symmetric at ({i},{j})"

    # Diagonal should be positive (variances)
    for i in range(3):
        assert cov_mat[i][i] > 0, f"Diagonal {i} not positive: {cov_mat[i][i]}"

    # x-y covariance should be positive (both trending up together)
    assert cov_mat[0][1] > 0, f"x-y covariance should be positive: {cov_mat[0][1]}"
    assert cov_mat[1][0] > 0, f"y-x covariance should be positive: {cov_mat[1][0]}"

    # z should have lower covariance with x and y than x-y covariance
    assert abs(cov_mat[0][2]) < abs(cov_mat[0][1]), f"z should be less correlated than y: {cov_mat[0][2]} vs {cov_mat[0][1]}"

    # Verify diagonal via direct variance computation
    from statistics import variance

    var_x = variance(x)
    var_y = variance(y)
    var_z = variance(z)

    assert abs(cov_mat[0][0] - var_x) < 1e-6, "Variance x mismatch"
    assert abs(cov_mat[1][1] - var_y) < 1e-6, "Variance y mismatch"
    assert abs(cov_mat[2][2] - var_z) < 1e-6, "Variance z mismatch"

    print("covariance_matrix.py: PASS")
