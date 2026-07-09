"""
Ridge Regression via Normal Equations (from scratch).

Core idea: Linear regression with L2 regularization: minimize ||Xw - y||^2 + λ||w||^2.
Solved analytically via normal equations: w = (X^T X + λI)^(-1) X^T y.
Implement matrix operations (transpose, multiply, Gaussian elimination) from scratch.

When to use: Regression with collinearity; small to medium data; interpretable model.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple


def matrix_transpose(A: List[List[float]]) -> List[List[float]]:
    """Transpose a matrix."""
    if not A:
        return []
    m = len(A)
    n = len(A[0])
    return [[A[i][j] for i in range(m)] for j in range(n)]


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


def matrix_vector_multiply(A: List[List[float]], v: List[float]) -> List[float]:
    """Multiply matrix A (m x n) by vector v (n,) -> result (m,)."""
    result = [0.0] * len(A)
    for i in range(len(A)):
        for j in range(len(v)):
            result[i] += A[i][j] * v[j]
    return result


def add_identity_scaled(A: List[List[float]], lambda_val: float) -> List[List[float]]:
    """Add λ*I to matrix A."""
    n = len(A)
    result = [row[:] for row in A]
    for i in range(n):
        result[i][i] += lambda_val
    return result


def gaussian_elimination(A: List[List[float]], b: List[float]) -> List[float]:
    """
    Solve Ax = b using Gaussian elimination with partial pivoting.
    Modifies A and b in place.
    """
    n = len(A)

    # Forward elimination with partial pivoting
    for col in range(n):
        # Find pivot
        max_row = col
        for row in range(col + 1, n):
            if abs(A[row][col]) > abs(A[max_row][col]):
                max_row = row

        # Swap rows
        A[col], A[max_row] = A[max_row], A[col]
        b[col], b[max_row] = b[max_row], b[col]

        # Eliminate below
        for row in range(col + 1, n):
            if A[col][col] != 0:
                factor = A[row][col] / A[col][col]
                for j in range(col, n):
                    A[row][j] -= factor * A[col][j]
                b[row] -= factor * b[col]

    # Back substitution
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        if A[i][i] != 0:
            x[i] /= A[i][i]

    return x


def ridge_regression_normal_eq(
    X: List[List[float]],
    y: List[float],
    lambda_reg: float = 0.01
) -> List[float]:
    """
    Fit ridge regression using normal equations.

    Args:
        X: list of feature vectors (n_samples x n_features)
        y: list of target values
        lambda_reg: regularization parameter (λ)

    Returns:
        weights: fitted coefficients
    """
    # Compute X^T * X
    X_T = matrix_transpose(X)
    XTX = matrix_multiply(X_T, X)

    # Compute X^T * y
    XTy = matrix_vector_multiply(X_T, y)

    # Compute (X^T * X + λI)
    XTX_regularized = add_identity_scaled(XTX, lambda_reg)

    # Solve (X^T * X + λI) w = X^T * y
    weights = gaussian_elimination(XTX_regularized, XTy)

    return weights


def ridge_regression_predict(
    X: List[List[float]],
    weights: List[float]
) -> List[float]:
    """Predict using fitted weights."""
    return matrix_vector_multiply(X, weights)


if __name__ == "__main__":
    import random

    random.seed(42)

    # Generate synthetic regression data
    n_samples = 30
    n_features = 3
    X = [[random.uniform(-5, 5) for _ in range(n_features)] for _ in range(n_samples)]

    # True weights: [2, 3, -1]
    true_weights = [2.0, 3.0, -1.0]
    y = [sum(true_weights[j] * X[i][j] for j in range(n_features)) + random.gauss(0, 0.5)
         for i in range(n_samples)]

    # Fit ridge regression
    weights = ridge_regression_normal_eq(X, y, lambda_reg=0.01)

    # Compute R² on training data
    predictions = ridge_regression_predict(X, weights)
    ss_res = sum((predictions[i] - y[i]) ** 2 for i in range(n_samples))
    ss_tot = sum((y[i] - sum(y) / len(y)) ** 2 for i in range(n_samples))
    r2 = 1.0 - (ss_res / ss_tot) if ss_tot > 0 else 0.0

    assert r2 > 0.8, f"R² = {r2} is too low"
    assert all(abs(weights[i] - true_weights[i]) < 1.0 for i in range(n_features)), \
        f"Weights {weights} too far from true {true_weights}"

    print(f"RIDGE_REGRESSION_NORMAL_EQ PASS: R² = {r2:.3f}, weights = {[f'{w:.2f}' for w in weights]}")
