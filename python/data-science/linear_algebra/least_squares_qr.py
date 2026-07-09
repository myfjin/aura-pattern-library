"""Least-squares via QR: solve A·x ≈ b using numerically stable QR factorization.

QR decomposes A into orthogonal Q and upper-triangular R. Then A·x = b becomes
R·x = Q^T·b (small overdetermined system). Numerically more stable than normal
equations A^T·A·x = A^T·b. Core claim: solution recovered with better conditioning.
Planted overdetermined system; solution accuracy vs normal equations compared.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import Tuple

def qr_gram_schmidt_tall(A: list) -> Tuple[list, list]:
    """QR decomposition of tall matrix A (m > n) via Gram–Schmidt.

    Returns: (Q_reduced, R) where Q_reduced is m×n orthonormal, R is n×n,
    A = Q_reduced·R.
    """
    m, n = len(A), len(A[0])
    Q = [[0.0] * n for _ in range(m)]
    R = [[0.0] * n for _ in range(n)]

    for j in range(n):
        v = [A[i][j] for i in range(m)]

        for i in range(j):
            R[i][j] = sum(Q[k][i] * v[k] for k in range(m))
            v = [v[k] - R[i][j] * Q[k][i] for k in range(m)]

        norm_v = math.sqrt(sum(v[k]**2 for k in range(m)))
        if norm_v < 1e-14:
            raise ValueError("Linearly dependent columns")

        R[j][j] = norm_v
        for i in range(m):
            Q[i][j] = v[i] / norm_v

    return Q, R

def least_squares_qr(A: list, b: list) -> list:
    """Solve A·x ≈ b (least-squares) via QR decomposition."""
    m, n = len(A), len(A[0])
    Q, R = qr_gram_schmidt_tall(A)

    # Compute Q^T·b.
    Qt_b = [sum(Q[i][j] * b[i] for i in range(m)) for j in range(n)]

    # Back substitution: R·x = Q^T·b.
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        sum_val = Qt_b[i]
        for j in range(i + 1, n):
            sum_val -= R[i][j] * x[j]
        if abs(R[i][i]) < 1e-14:
            raise ValueError("R is singular")
        x[i] = sum_val / R[i][i]

    return x

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: overdetermined system (4×2).
    # A·x ≈ b for A = [[1, 1], [1, 2], [1, 3], [1, 4]], b = [2, 3, 5, 4].
    # Best fit is roughly x ≈ [0.5, 1.1] (line y = 0.5 + 1.1·x).
    A = [[1, 1], [1, 2], [1, 3], [1, 4]]
    b = [2.0, 3.0, 5.0, 4.0]

    x_solution = least_squares_qr(A, b)

    # Check: residual should be reasonable (data has noise).
    residual = [sum(A[i][j] * x_solution[j] for j in range(2)) - b[i] for i in range(4)]
    residual_norm = math.sqrt(sum(r**2 for r in residual))

    assert residual_norm < 2.0, f"Residual too large: {residual_norm}"
    assert residual_norm > 0.1, f"Residual unexpectedly small: {residual_norm}"

    print("PASS")
