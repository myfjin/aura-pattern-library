# qr gram schmidt

**Language:** Python · **Sphere:** data-science · **Category:** Linear Algebra

**Signature:** `(A: list) → Tuple[list, list]`

## What it does

QR decomposition via Gram–Schmidt: orthogonal Q and upper-triangular R.

Iteratively orthogonalizes columns of A to produce Q. Core claim: Q is
orthonormal (Q^T·Q = I), A = Q·R verified. Planted 3×3 matrix; orthonormality
and reconstruction tested.

## Guarantee

When it runs, qr gram schmidt guarantees abs(QTQ[i][j] - expected) < 1e-10; abs(QR[i][j] - A[i][j]) < 1e-10 (proven by run).

**Checkable constraints:**

- `abs(QTQ[i][j] - expected) < 1e-10`
- `abs(QR[i][j] - A[i][j]) < 1e-10`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:**
- `qr_gram_schmidt(A: list) -> Tuple[list, list]`
- `matrix_mult(A: list, B: list) -> list`
- `matrix_transpose(A: list) -> list`
**Valid input:** `A` is an n×m matrix with `m` linearly independent columns.
**Core:** Classical Gram–Schmidt QR factorization. Returns Q (n×m orthonormal) and R (m×m upper triangular) such that `A = Q·R`.
**Assert:** On planted 3×3 matrix, verifies `Q^T·Q = I` and `A = Q·R` within `1e-10`.
**⚠️ Defect:** Same numerical stability issue as `least_squares_qr`: classical Gram–Schmidt loses orthogonality for nearly dependent or ill-conditioned columns. The test matrix is well-conditioned, so orthogonality appears perfect; a more realistic near-rank-deficient matrix would fail the `Q^T·Q = I` check.

---
*△ AURA Pattern Library — © Reality Optimizer*
