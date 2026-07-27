# matrix condition number

**Language:** Python · **Sphere:** data-science · **Category:** Linear Algebra

**Signature:** `(A: list) → float`

## What it does

Matrix condition number: measure sensitivity to perturbations in A and b.

κ(A) = ||A|| · ||A⁻¹||. Large κ means small changes in A or b cause large
changes in solution x. Core claim: error amplification measured; ill-conditioned
system shows large error magnification vs small-κ system, identical perturbation size.

## Guarantee

When it runs, matrix condition number guarantees kappa_bad > 100 * kappa_good (weak-grade: directional, proven by run).

**Checkable constraints:**

- `kappa_bad > 100 * kappa_good`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:**
- `condition_number(A: list) -> float`
- `matrix_norm_frobenius(A: list) -> float`
- `matrix_inverse_lu(A: list) -> list`
**Valid input:** `A` is an n×n invertible matrix.
**Core:** Estimates `κ(A) = ||A||_F · ||A⁻¹||_F` by inverting `A` via LU with partial pivoting and computing Frobenius norms.
**Assert:** Compares a well-conditioned matrix (`κ ≈ 4.6`) against an ill-conditioned matrix (`κ ≈ 60001`) and asserts the ill-conditioned one is at least 100× larger.
**⚠️ Defect:** The internal inverse routine is fragile. The forward-substitution loop uses `b[j]` after it has already been overwritten (`b[i] = sum_val`), so the solve with multiple right-hand sides is wrong for all columns after the first. The demo only computes the condition number, and the bug may still produce a plausible-looking (but incorrect) inverse for matrices larger than 2×2.

---
*△ AURA Pattern Library — © Reality Optimizer*
