# least squares qr

**Language:** Python · **Sphere:** data-science · **Category:** Linear Algebra

**Signature:** `(A: list, b: list) → list`

## What it does

Least-squares via QR: solve A·x ≈ b using numerically stable QR factorization.

QR decomposes A into orthogonal Q and upper-triangular R. Then A·x = b becomes
R·x = Q^T·b (small overdetermined system). Numerically more stable than normal
equations A^T·A·x = A^T·b. Core claim: solution recovered with better conditioning.
Planted overdetermined system; solution accuracy vs normal equations compared.

## Guarantee

When it runs, least squares qr guarantees residual_norm < 2.0; residual_norm > 0.1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `residual_norm < 2.0`
- `residual_norm > 0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:**
- `qr_gram_schmidt_tall(A: list) -> Tuple[list, list]`
- `least_squares_qr(A: list, b: list) -> list`
**Valid input:** `A` is m×n with `m > n` and full column rank; `b` length m.
**Core:** Gram–Schmidt QR for tall matrices, then solves `R·x = Q^T·b` by back-substitution. Avoids normal-equation squaring of the condition number.
**Assert:** On overdetermined 4×2 system `A = [[1,1],[1,2],[1,3],[1,4]]`, `b = [2,3,5,4]`, checks residual norm is between `0.1` and `2.0`.
**⚠️ Defect:** Uses classical (not modified) Gram–Schmidt, which is numerically unstable for nearly dependent columns. The test matrix is well-conditioned, so the defect is hidden; on ill-conditioned least-squares problems the computed `Q` can lose orthogonality and the solution accuracy degrades.

---
*△ AURA Pattern Library — © Reality Optimizer*
