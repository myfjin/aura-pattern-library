"""
Principal Component Analysis via Power Iteration (from scratch).

Core idea: Find directions of maximum variance in data by computing eigenvalues
and eigenvectors of the covariance matrix. Use power iteration to find the top
eigenvector without full eigendecomposition.

When to use: Dimensionality reduction; data visualization; noise reduction.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple as TupleType


def matrix_mean_center(X: List[List[float]]) -> TupleType[List[List[float]], List[float]]:
    """Center data by subtracting mean of each column."""
    n_samples = len(X)
    n_features = len(X[0]) if X else 0

    means = [sum(X[i][j] for i in range(n_samples)) / n_samples for j in range(n_features)]
    X_centered = [[X[i][j] - means[j] for j in range(n_features)] for i in range(n_samples)]

    return X_centered, means


def matrix_multiply(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """Multiply two matrices A (m x n) and B (n x p) -> result (m x p)."""
    m = len(A)
    n = len(A[0]) if A else 0
    p = len(B[0]) if B else 0

    result = [[0.0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result


def matrix_transpose(A: List[List[float]]) -> List[List[float]]:
    """Transpose a matrix."""
    if not A:
        return []
    m = len(A)
    n = len(A[0])
    return [[A[i][j] for i in range(m)] for j in range(n)]


def covariance_matrix(X: List[List[float]]) -> List[List[float]]:
    """Compute covariance matrix: (1/n) * X^T * X (on centered data)."""
    X_T = matrix_transpose(X)
    cov = matrix_multiply(X_T, X)
    n = len(X)
    return [[cov[i][j] / n for j in range(len(cov[0]))] for i in range(len(cov))]


def vector_norm(v: List[float]) -> float:
    """Compute L2 norm of a vector."""
    return math.sqrt(sum(x ** 2 for x in v))


def matrix_vector_multiply(A: List[List[float]], v: List[float]) -> List[float]:
    """Multiply matrix A by vector v."""
    result = [0.0] * len(A)
    for i in range(len(A)):
        for j in range(len(v)):
            result[i] += A[i][j] * v[j]
    return result


def power_iteration(
    cov: List[List[float]],
    num_components: int = 1,
    max_iterations: int = 100
) -> Tuple[List[List[float]], List[float]]:
    """
    Find top eigenvectors using power iteration.

    Args:
        cov: covariance matrix (symmetric)
        num_components: number of principal components
        max_iterations: iterations per component

    Returns:
        (eigenvectors, eigenvalues): list of eigenvectors and their eigenvalues
    """
    n_features = len(cov)
    components = []
    eigenvalues = []
    cov_deflate = [row[:] for row in cov]  # Copy for deflation

    for comp_idx in range(num_components):
        # Random initial vector
        v = [random.gauss(0, 1) for _ in range(n_features)]
        norm_v = vector_norm(v)
        v = [x / norm_v for x in v]

        # Power iteration on deflated matrix
        for _ in range(max_iterations):
            v_new = matrix_vector_multiply(cov_deflate, v)
            norm_v = vector_norm(v_new)
            if norm_v > 1e-10:
                v_new = [x / norm_v for x in v_new]
            else:
                break

            # Check convergence
            change = sum((v_new[i] - v[i]) ** 2 for i in range(len(v)))
            v = v_new
            if change < 1e-6:
                break

        # Estimate eigenvalue
        v_new = matrix_vector_multiply(cov_deflate, v)
        eigenvalue = sum(v[i] * v_new[i] for i in range(len(v)))

        components.append(v)
        eigenvalues.append(eigenvalue)

        # Deflate: cov_new = cov - eigenvalue * v * v^T
        for i in range(n_features):
            for j in range(n_features):
                cov_deflate[i][j] -= eigenvalue * v[i] * v[j]

    return components, eigenvalues


def pca_transform(X: List[List[float]], components: List[List[float]]) -> List[List[float]]:
    """Project data onto principal components."""
    n_samples = len(X)
    n_components = len(components)

    result = []
    for i in range(n_samples):
        row = []
        for c in range(n_components):
            proj = sum(X[i][j] * components[c][j] for j in range(len(X[i])))
            row.append(proj)
        result.append(row)

    return result


if __name__ == "__main__":
    random.seed(42)

    # Generate synthetic data with clear variance structure
    # Mostly along one direction
    n_samples = 50
    X = []
    for _ in range(n_samples):
        # Variance mostly in first dimension
        x1 = random.gauss(0, 3.0)
        x2 = random.gauss(0, 0.5)
        X.append([x1, x2])

    # Center data
    X_centered, means = matrix_mean_center(X)

    # Compute covariance
    cov = covariance_matrix(X_centered)

    # Find first 2 principal components
    components, eigenvalues = power_iteration(cov, num_components=2, max_iterations=100)

    # Transform data
    X_pca = pca_transform(X_centered, components)

    # Check: eigenvalue in first component should be much larger than second
    assert eigenvalues[0] > eigenvalues[1], f"First eigenvalue {eigenvalues[0]} should be > second {eigenvalues[1]}"
    assert eigenvalues[0] > 2.0, f"First eigenvalue = {eigenvalues[0]} is too low"

    print(f"PCA_POWER_ITERATION PASS: ev1 = {eigenvalues[0]:.3f}, ev2 = {eigenvalues[1]:.3f}")
