# jacobi eigen symmetric

**Language:** Python · **Sphere:** data-science · **Category:** Linear Algebra

**Signature:** `(A: list, max_iter: int, tol: float) → Tuple[list, list]`

## What it does

Jacobi eigenvalue algorithm: iterative diagonalization of symmetric matrix.

Applies Givens rotations to progressively zero off-diagonal elements.
Core claim: converges to diagonal matrix of eigenvalues; eigenvectors are
product of rotations. Planted 3×3 symmetric matrix; eigenvalues verified vs
characteristic polynomial roots.

## Guarantee

When it runs, jacobi eigen symmetric guarantees abs(lam - true_eigs[rank]) < 1e-08; abs(Av[i] - lam * v[i]) < 1e-08 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(eigenvalues) == 3`
- `abs(lam - true_eigs[rank]) < 1e-08`
- `abs(Av[i] - lam * v[i]) < 1e-08`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `jacobi_eigen(A: list, max_iter: int = 100, tol: float = 1e-10) -> Tuple[list, list]`
**Valid input:** `A` is an n×n symmetric matrix.
**Core:** Jacobi eigenvalue algorithm. Repeatedly applies Givens rotations to zero the largest off-diagonal element, accumulating rotations in `V`. Returns eigenvalues (diagonal of the transformed matrix) and eigenvector matrix `V`.
**Assert:** On planted symmetric 3×3 matrix with known spectrum `{3-√3, 3, 3+√3}`, sorts eigenpairs and verifies each eigenvalue within `1e-8` and `A·v = λ·v` within `1e-8`.
**⚠️ Defect:** Eigenvector matrix layout is transposed relative to the docstring. The docstring says "eigenvectors[i] is the i-th eigenvector", but the code stores `V[i][j]` as component `i` of eigenvector `j`. The demo happens to access it correctly, but a caller using `eigenvectors[i]` directly will get the wrong vector.

---
*△ AURA Pattern Library — © Reality Optimizer*
