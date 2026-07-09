"""
DISTANCE METRIC: Mahalanobis Distance

Core idea: Euclidean distance treats all dimensions equally; Mahalanobis accounts
for covariance structure, scaling by the inverse covariance matrix. On correlated
data, Mahalanobis distance can reveal structure that Euclidean misses.

When to use: Multivariate outlier detection, anomaly detection on correlated data,
or whenever covariance structure is meaningful (e.g., finance, quality control).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple


def matrix_multiply_2x2(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """Multiply two 2x2 matrices."""
    result = [[0.0, 0.0], [0.0, 0.0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
    return result


def matrix_invert_2x2(M: List[List[float]]) -> List[List[float]]:
    """
    Invert a 2x2 matrix from scratch.
    For [[a, b], [c, d]], inverse = (1/det) * [[d, -b], [-c, a]]
    where det = a*d - b*c
    """
    a, b = M[0][0], M[0][1]
    c, d = M[1][0], M[1][1]

    det = a * d - b * c
    assert abs(det) > 1e-12, f"Matrix is singular, determinant={det}"

    inv = [[d / det, -b / det], [-c / det, a / det]]
    return inv


def compute_covariance_2d(points: List[Tuple[float, float]]) -> List[List[float]]:
    """
    Compute 2x2 covariance matrix from a list of 2D points.
    Cov[i, j] = E[(X_i - mu_i)(X_j - mu_j)]
    """
    n = len(points)
    mean_x = sum(p[0] for p in points) / n
    mean_y = sum(p[1] for p in points) / n

    cov_xx = sum((p[0] - mean_x) ** 2 for p in points) / n
    cov_yy = sum((p[1] - mean_y) ** 2 for p in points) / n
    cov_xy = sum((p[0] - mean_x) * (p[1] - mean_y) for p in points) / n

    return [[cov_xx, cov_xy], [cov_xy, cov_yy]]


def mahalanobis_distance(
    point: Tuple[float, float],
    mean: Tuple[float, float],
    cov_inv: List[List[float]],
) -> float:
    """
    Compute Mahalanobis distance from point to mean.
    D_M = sqrt((x - mu)^T * Cov^-1 * (x - mu))
    """
    dx = point[0] - mean[0]
    dy = point[1] - mean[1]

    # Multiply: cov_inv * [dx, dy]
    term1 = cov_inv[0][0] * dx + cov_inv[0][1] * dy
    term2 = cov_inv[1][0] * dx + cov_inv[1][1] * dy

    # Dot product: [dx, dy] · [term1, term2]
    quad_form = dx * term1 + dy * term2

    if quad_form < 0:
        quad_form = 0  # Numerical noise

    return math.sqrt(quad_form)


def euclidean_distance(p: Tuple[float, float], q: Tuple[float, float]) -> float:
    """Standard Euclidean distance."""
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


if __name__ == "__main__":
    import random

    random.seed(42)

    # Create a dataset with strong positive correlation
    # points cluster along x=y line
    points = [
        (0.0, 0.1),
        (1.0, 1.1),
        (2.0, 1.9),
        (3.0, 2.9),
        (4.0, 4.1),
    ]

    # Compute mean
    mean_x = sum(p[0] for p in points) / len(points)
    mean_y = sum(p[1] for p in points) / len(points)
    mean = (mean_x, mean_y)

    # Compute covariance matrix
    cov = compute_covariance_2d(points)

    # Invert covariance
    cov_inv = matrix_invert_2x2(cov)

    # Test 1: Mahalanobis distance from mean to itself should be 0
    mdist_self = mahalanobis_distance(mean, mean, cov_inv)
    assert mdist_self < 1e-10, f"Mahalanobis distance from mean to self not 0: {mdist_self}"

    # Test 2: Point on the correlation axis should be close in Mahalanobis
    # Point along the x=y direction (aligned with correlation)
    point_aligned = (mean[0] + 1.0, mean[1] + 1.0)
    mdist_aligned = mahalanobis_distance(point_aligned, mean, cov_inv)

    # Point perpendicular to correlation (harder to reach in correlated data)
    point_perp = (mean[0] + 1.0, mean[1] - 1.0)
    mdist_perp = mahalanobis_distance(point_perp, mean, cov_inv)

    # Mahalanobis should penalize the perpendicular direction more (it's unusual given correlation)
    assert (
        mdist_perp > mdist_aligned
    ), f"Mahalanobis should penalize perpendicular direction: {mdist_perp} not > {mdist_aligned}"

    # Test 3: Euclidean would treat them equally (naive)
    edist_aligned = euclidean_distance(point_aligned, mean)
    edist_perp = euclidean_distance(point_perp, mean)

    # Euclidean should give them equal distances (both are sqrt(2) away)
    assert (
        abs(edist_aligned - edist_perp) < 1e-6
    ), f"Euclidean should be equal for equal displacement: {edist_aligned} vs {edist_perp}"

    # Test 4: Mahalanobis distance is always non-negative
    assert mdist_aligned >= 0, f"Mahalanobis negative: {mdist_aligned}"
    assert mdist_perp >= 0, f"Mahalanobis negative: {mdist_perp}"

    # Test 5: Covariance is symmetric
    assert abs(cov[0][1] - cov[1][0]) < 1e-10, "Covariance not symmetric"

    print(
        f"mahalanobis_distance.py: aligned_mdist={mdist_aligned:.4f} perp_mdist={mdist_perp:.4f} ranking_correct PASS"
    )
