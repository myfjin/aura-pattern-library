"""Jacobi eigenvalue algorithm: iterative diagonalization of symmetric matrix.

Applies Givens rotations to progressively zero off-diagonal elements.
Core claim: converges to diagonal matrix of eigenvalues; eigenvectors are
product of rotations. Planted 3×3 symmetric matrix; eigenvalues verified vs
characteristic polynomial roots.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import Tuple

def jacobi_eigen(A: list, max_iter: int = 100, tol: float = 1e-10) -> Tuple[list, list]:
    """Compute eigenvalues and eigenvectors of symmetric matrix A via Jacobi.

    Returns: (eigenvalues, eigenvectors) where eigenvectors[i] is the i-th eigenvector.
    """
    n = len(A)
    A_work = [row[:] for row in A]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for iteration in range(max_iter):
        # Find largest off-diagonal element.
        p, q = 0, 1
        max_elem = abs(A_work[0][1])
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A_work[i][j]) > max_elem:
                    max_elem = abs(A_work[i][j])
                    p, q = i, j

        if max_elem < tol:
            break

        # Compute Givens rotation angle.
        theta = 0.5 * math.atan2(2 * A_work[p][q], A_work[q][q] - A_work[p][p])
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)

        # Apply rotation.
        for i in range(n):
            if i != p and i != q:
                A_ip = A_work[i][p]
                A_iq = A_work[i][q]
                A_work[i][p] = cos_theta * A_ip - sin_theta * A_iq
                A_work[p][i] = A_work[i][p]
                A_work[i][q] = sin_theta * A_ip + cos_theta * A_iq
                A_work[q][i] = A_work[i][q]

        A_pp = A_work[p][p]
        A_qq = A_work[q][q]
        A_work[p][p] = cos_theta**2 * A_pp - 2 * sin_theta * cos_theta * A_work[p][q] + sin_theta**2 * A_qq
        A_work[q][q] = sin_theta**2 * A_pp + 2 * sin_theta * cos_theta * A_work[p][q] + cos_theta**2 * A_qq
        A_work[p][q] = 0.0
        A_work[q][p] = 0.0

        # Update eigenvector matrix.
        for i in range(n):
            V_ip = V[i][p]
            V_iq = V[i][q]
            V[i][p] = cos_theta * V_ip - sin_theta * V_iq
            V[i][q] = sin_theta * V_ip + cos_theta * V_iq

    eigenvalues = [A_work[i][i] for i in range(n)]
    return eigenvalues, V

if __name__ == "__main__":
    import math
    import random
    random.seed(42)

    # Planted: symmetric 3×3 matrix. A = [[4, 1, 0], [1, 3, 1], [0, 1, 2]].
    # Exact eigenvalues: 3 is a root of det(A-λI); the other two are 3±√3.
    #   → {3 - √3, 3, 3 + √3} ≈ {1.2679, 3.0, 4.7321}, sum = trace = 9.
    A = [[4, 1, 0], [1, 3, 1], [0, 1, 2]]
    true_eigs = sorted([3.0 - math.sqrt(3), 3.0, 3.0 + math.sqrt(3)])

    eigenvalues, eigenvectors = jacobi_eigen(A)
    assert len(eigenvalues) == 3, "Expected 3 eigenvalues"

    # Rank the eigenpairs by eigenvalue WITHOUT desyncing values from vectors:
    # eigenvectors[i][j] is component i of the j-th eigenvector (column j pairs with
    # eigenvalues[j]). Sorting the value list alone would mismatch value↔vector.
    order = sorted(range(3), key=lambda j: eigenvalues[j])

    for rank, j in enumerate(order):
        lam = eigenvalues[j]
        v = [eigenvectors[i][j] for i in range(3)]
        # Eigenvalue matches the exact spectrum...
        assert abs(lam - true_eigs[rank]) < 1e-8, \
            f"Eigenvalue {lam} != expected {true_eigs[rank]}"
        # ...and its OWN eigenvector satisfies A·v = λ·v (the defining property, all 3).
        Av = [sum(A[i][k] * v[k] for k in range(3)) for i in range(3)]
        for i in range(3):
            assert abs(Av[i] - lam * v[i]) < 1e-8, \
                f"A·v ≠ λ·v for eigenvalue {lam} at index {i}: {Av[i]} vs {lam * v[i]}"

    print("PASS")
