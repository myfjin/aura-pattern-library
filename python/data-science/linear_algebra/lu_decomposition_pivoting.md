# lu decomposition pivoting

**Language:** Python · **Sphere:** data-science · **Category:** Linear Algebra

**Signature:** `(A: list) → Tuple[list, list, list]`

## What it does

LU decomposition with partial pivoting: PA = LU factorization.

Permutation matrix P reorders rows for numerical stability; L and U satisfy
PA = LU. Core claim: factorization recovered exactly; reconstruction PA = LU
verified. Planted 3×3 matrix; decomposition and forward/backward solves tested.

## Guarantee

When it runs, lu decomposition pivoting guarantees abs(PA[i][j] - LU[i][j]) < 1e-10 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(PA[i][j] - LU[i][j]) < 1e-10`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:**
- `lu_decomposition_pivoting(A: list) -> Tuple[list, list, list]`
- `matrix_mult(A: list, B: list) -> list`
**Valid input:** `A` is an n×n invertible matrix.
**Core:** LU factorization with partial row pivoting. Returns permutation matrix `P`, lower triangular `L`, and upper triangular `U` such that `P·A = L·U`.
**Assert:** On planted 3×3 matrix, verifies `P·A = L·U` element-wise within `1e-10`.
**⚠️ Defect:** No forward/backward substitution helper is provided, so the factorization cannot actually be used to solve `A·x = b` without the caller writing the solve step. The module advertises "decomposition and forward/backward solves tested" in the top comment, but only the decomposition is exposed.

---
*△ AURA Pattern Library — © Reality Optimizer*
