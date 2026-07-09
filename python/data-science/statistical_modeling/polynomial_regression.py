"""
Polynomial Regression via Least Squares (Vandermonde Design Matrix).

A polynomial regression solver using Gaussian elimination on the Vandermonde matrix.
Fits a degree-d polynomial to (x, y) data by solving the normal equations directly.
Use when you need interpretable polynomial fit without external libraries.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


def gaussian_elimination(A: List[List[float]], b: List[float]) -> List[float]:
    """Solve Ax=b via Gaussian elimination with partial pivoting."""
    n = len(A)
    # Augment A with b
    aug = [A[i][:] + [b[i]] for i in range(n)]

    # Forward elimination
    for col in range(n):
        # Find pivot
        max_row = col
        for row in range(col + 1, n):
            if abs(aug[row][col]) > abs(aug[max_row][col]):
                max_row = row
        aug[col], aug[max_row] = aug[max_row], aug[col]

        if abs(aug[col][col]) < 1e-12:
            raise ValueError("Matrix is singular")

        # Eliminate below
        for row in range(col + 1, n):
            factor = aug[row][col] / aug[col][col]
            for j in range(col, n + 1):
                aug[row][j] -= factor * aug[col][j]

    # Back substitution
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = aug[i][n]
        for j in range(i + 1, n):
            x[i] -= aug[i][j] * x[j]
        x[i] /= aug[i][i]

    return x


def vandermonde_matrix(x_vals: List[float], degree: int) -> List[List[float]]:
    """Build Vandermonde design matrix for polynomial regression."""
    n = len(x_vals)
    V = [[0.0] * (degree + 1) for _ in range(n)]
    for i in range(n):
        for j in range(degree + 1):
            V[i][j] = x_vals[i] ** j
    return V


def fit_polynomial(x_vals: List[float], y_vals: List[float], degree: int) -> List[float]:
    """Fit polynomial of given degree. Returns coefficients [c0, c1, ..., cd]."""
    V = vandermonde_matrix(x_vals, degree)

    # Compute V^T * V and V^T * y
    n_cols = degree + 1
    VtV = [[0.0] * n_cols for _ in range(n_cols)]
    Vty = [0.0] * n_cols

    for j in range(n_cols):
        for k in range(n_cols):
            for i in range(len(x_vals)):
                VtV[j][k] += V[i][j] * V[i][k]
        for i in range(len(x_vals)):
            Vty[j] += V[i][j] * y_vals[i]

    # Solve normal equations
    coeffs = gaussian_elimination(VtV, Vty)
    return coeffs


def eval_poly(coeffs: List[float], x: float) -> float:
    """Evaluate polynomial at x given coefficients."""
    result = 0.0
    power = 1.0
    for c in coeffs:
        result += c * power
        power *= x
    return result


def mse(y_true: List[float], y_pred: List[float]) -> float:
    """Mean squared error."""
    return sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / len(y_true)


if __name__ == "__main__":
    random.seed(42)

    # Plant a quadratic: y = 2 + 3*x + 0.5*x^2 + noise
    true_coeffs = [2.0, 3.0, 0.5]
    x_vals = [float(i) * 0.5 for i in range(20)]
    y_vals = [eval_poly(true_coeffs, x) + random.gauss(0, 0.1) for x in x_vals]

    # Fit degree 2
    fitted_coeffs_2 = fit_polynomial(x_vals, y_vals, 2)

    # Fit degree 1 (linear)
    fitted_coeffs_1 = fit_polynomial(x_vals, y_vals, 1)

    y_pred_2 = [eval_poly(fitted_coeffs_2, x) for x in x_vals]
    y_pred_1 = [eval_poly(fitted_coeffs_1, x) for x in x_vals]

    mse_2 = mse(y_vals, y_pred_2)
    mse_1 = mse(y_vals, y_pred_1)

    # Verify fitted coefficients recover planted values within tolerance
    for i, (true_c, fit_c) in enumerate(zip(true_coeffs, fitted_coeffs_2)):
        assert abs(true_c - fit_c) < 0.2, f"Coeff {i}: true={true_c}, fit={fit_c}"

    # Verify quadratic beats linear
    assert mse_2 < mse_1, f"Quadratic MSE {mse_2} should beat linear {mse_1}"

    print(f"polynomial_regression.py: fitted_coeffs={fitted_coeffs_2}, mse_2={mse_2:.4f}, mse_1={mse_1:.4f} PASS")
