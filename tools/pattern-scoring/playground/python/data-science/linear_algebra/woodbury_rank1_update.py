"""Woodbury matrix identity: update A⁻¹ efficiently after rank-1 A change.

If A_new = A + u·v^T, then (A_new)⁻¹ = A⁻¹ - (A⁻¹·u·v^T·A⁻¹) / (1 + v^T·A⁻¹·u).
Core claim: inverse updated in O(n²) vs O(n³) re-inversion. Planted rank-1
update; updated inverse verified exactly against full recomputation.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import Tuple

def matrix_inverse_lu(A: list) -> list:
    """Compute inverse of matrix A via LU decomposition."""
    n = len(A)
    A_copy = [row[:] for row in A]

    # Store permutation.
    piv = list(range(n))

    # Forward elimination with partial pivoting.
    for k in range(n):
        # Find pivot.
        max_idx = k
        for i in range(k + 1, n):
            if abs(A_copy[i][k]) > abs(A_copy[max_idx][k]):
                max_idx = i

        # Swap rows.
        A_copy[k], A_copy[max_idx] = A_copy[max_idx], A_copy[k]
        piv[k], piv[max_idx] = piv[max_idx], piv[k]

        if abs(A_copy[k][k]) < 1e-14:
            raise ValueError("Matrix is singular")

        # Eliminate below.
        for i in range(k + 1, n):
            factor = A_copy[i][k] / A_copy[k][k]
            for j in range(k + 1, n):
                A_copy[i][j] -= factor * A_copy[k][j]

    # Back substitution for each column of identity.
    A_inv = [[0.0] * n for _ in range(n)]
    for col in range(n):
        # Solve for column col of A_inv.
        b = [0.0] * n
        b[piv[col]] = 1.0  # Rearrange due to pivoting.

        # Forward substitution (with lower triangular part of A_copy stored implicitly).
        for i in range(n):
            sum_val = b[i]
            for j in range(i):
                sum_val -= A_copy[i][j] * b[j]
            b[i] = sum_val

        # Back substitution (with upper triangular part).
        for i in range(n - 1, -1, -1):
            sum_val = b[i]
            for j in range(i + 1, n):
                sum_val -= A_copy[i][j] * b[j]
            b[i] = sum_val / A_copy[i][i]

        for i in range(n):
            A_inv[i][col] = b[i]

    return A_inv

def vector_outer_product(u: list, v: list) -> list:
    """Compute outer product u·v^T."""
    n = len(u)
    return [[u[i] * v[j] for j in range(n)] for i in range(n)]

def matrix_add(A: list, B: list) -> list:
    """Add matrices A + B."""
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def woodbury_update(
    A_inv: list,
    u: list,
    v: list
) -> list:
    """Apply Woodbury formula: (A + u·v^T)⁻¹ = A⁻¹ - (A⁻¹·u·v^T·A⁻¹) / (1 + v^T·A⁻¹·u)."""
    n = len(A_inv)

    # Compute A_inv·u.
    A_inv_u = [sum(A_inv[i][j] * u[j] for j in range(n)) for i in range(n)]

    # Compute v^T·A_inv·u.
    v_T_A_inv_u = sum(v[i] * A_inv_u[i] for i in range(n))

    # Compute v^T·A_inv (as a row).
    v_T_A_inv = [sum(v[k] * A_inv[k][j] for k in range(n)) for j in range(n)]

    # Denominator.
    denom = 1.0 + v_T_A_inv_u
    if abs(denom) < 1e-14:
        raise ValueError("Woodbury denominator singular")

    # (A_inv·u)·(v^T·A_inv).
    numerator_matrix = [[A_inv_u[i] * v_T_A_inv[j] for j in range(n)] for i in range(n)]

    # Result: A_inv - numerator_matrix / denom.
    result = [[A_inv[i][j] - numerator_matrix[i][j] / denom for j in range(n)]
              for i in range(n)]

    return result

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: original matrix A = [[4, 1], [1, 3]].
    # A^{-1} = (1/11)·[[3, -1], [-1, 4]].
    A = [[4.0, 1.0], [1.0, 3.0]]

    # Direct 2x2 inversion for verification.
    det_A = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    A_inv = [[A[1][1] / det_A, -A[0][1] / det_A],
             [-A[1][0] / det_A, A[0][0] / det_A]]

    # Rank-1 update: u = [1, 0], v = [2, 1].
    u = [1.0, 0.0]
    v = [2.0, 1.0]

    # New matrix: A_new = A + u·v^T.
    A_new_direct = matrix_add(A, vector_outer_product(u, v))

    # Inverse via Woodbury.
    A_new_inv_woodbury = woodbury_update(A_inv, u, v)

    # Inverse via full recomputation (2x2).
    det_A_new = A_new_direct[0][0] * A_new_direct[1][1] - A_new_direct[0][1] * A_new_direct[1][0]
    A_new_inv_direct = [[A_new_direct[1][1] / det_A_new, -A_new_direct[0][1] / det_A_new],
                        [-A_new_direct[1][0] / det_A_new, A_new_direct[0][0] / det_A_new]]

    # Compare.
    for i in range(2):
        for j in range(2):
            assert abs(A_new_inv_woodbury[i][j] - A_new_inv_direct[i][j]) < 1e-8, \
                f"Woodbury and direct differ at ({i}, {j}): {A_new_inv_woodbury[i][j]} vs {A_new_inv_direct[i][j]}"

    print("PASS")
