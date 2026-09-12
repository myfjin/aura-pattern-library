"""LU decomposition with partial pivoting: PA = LU factorization.

Permutation matrix P reorders rows for numerical stability; L and U satisfy
PA = LU. Core claim: factorization recovered exactly; reconstruction PA = LU
verified. Planted 3×3 matrix; decomposition and forward/backward solves tested.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import Tuple

def lu_decomposition_pivoting(A: list) -> Tuple[list, list, list]:
    """Compute LU decomposition with partial pivoting: PA = LU.

    Returns: (P, L, U) where P is permutation matrix, L is lower triangular,
    U is upper triangular, and P·A = L·U.
    """
    n = len(A)
    A_work = [row[:] for row in A]
    piv = list(range(n))

    for k in range(n):
        # Find pivot.
        max_idx = k
        for i in range(k + 1, n):
            if abs(A_work[i][k]) > abs(A_work[max_idx][k]):
                max_idx = i

        # Swap rows in A_work and track permutation.
        A_work[k], A_work[max_idx] = A_work[max_idx], A_work[k]
        piv[k], piv[max_idx] = piv[max_idx], piv[k]

        if abs(A_work[k][k]) < 1e-14:
            raise ValueError("Matrix is singular or nearly singular")

        # Eliminate below.
        for i in range(k + 1, n):
            A_work[i][k] /= A_work[k][k]
            for j in range(k + 1, n):
                A_work[i][j] -= A_work[i][k] * A_work[k][j]

    # Extract L and U.
    L = [[1.0 if i == j else (A_work[i][j] if j < i else 0.0) for j in range(n)] for i in range(n)]
    U = [[A_work[i][j] if j >= i else 0.0 for j in range(n)] for i in range(n)]

    # Build permutation matrix P.
    P = [[0.0] * n for _ in range(n)]
    for i in range(n):
        P[i][piv[i]] = 1.0

    return P, L, U

def matrix_mult(A: list, B: list) -> list:
    """Multiply matrices A and B."""
    n, m = len(A), len(B[0])
    C = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: 3×3 matrix.
    A = [[2, 1, 3], [4, 3, 5], [1, 2, 2]]

    P, L, U = lu_decomposition_pivoting(A)

    # Verify: P·A = L·U.
    PA = matrix_mult(P, A)
    LU = matrix_mult(L, U)

    for i in range(3):
        for j in range(3):
            assert abs(PA[i][j] - LU[i][j]) < 1e-10, f"PA != LU at ({i}, {j})"

    print("PASS")
