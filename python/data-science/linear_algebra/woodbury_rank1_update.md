# woodbury rank1 update

**Language:** Python · **Sphere:** data-science · **Category:** Linear Algebra

**Signature:** `(A: list) → list`

## What it does

Woodbury matrix identity: update A⁻¹ efficiently after rank-1 A change.

If A_new = A + u·v^T, then (A_new)⁻¹ = A⁻¹ - (A⁻¹·u·v^T·A⁻¹) / (1 + v^T·A⁻¹·u).
Core claim: inverse updated in O(n²) vs O(n³) re-inversion. Planted rank-1
update; updated inverse verified exactly against full recomputation.

## Guarantee

When it runs, woodbury rank1 update guarantees abs(A_new_inv_woodbury[i][j] - A_new_inv_direct[i][j]) < 1e-08 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(A_new_inv_woodbury[i][j] - A_new_inv_direct[i][j]) < 1e-08`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:**
- `matrix_inverse_lu(A: list) -> list`
- `vector_outer_product(u: list, v: list) -> list`
- `matrix_add(A: list, B: list) -> list`
- `woodbury_update(A_inv: list, u: list, v: list) -> list`
**Valid input:** `A_inv` is the inverse of an n×n invertible matrix `A`; `u`, `v` length-n vectors; `1 + v^T·A_inv·u ≠ 0`.
**Core:** Applies the Woodbury identity for a rank-1 update: `(A + u·v^T)⁻¹ = A⁻¹ - (A⁻¹·u·v^T·A⁻¹)/(1 + v^T·A⁻¹·u)`.
**Assert:** On 2×2 matrix `A = [[4,1],[1,3]]` with `u = [1,0]`, `v = [2,1]`, compares Woodbury result against direct 2×2 inversion within `1e-8`.
**⚠️ Defect:** The helper `matrix_inverse_lu` has the same forward-substitution bug as `matrix_condition_number` (overwrites `b` during the loop). For the demo’s 2×2 case the bug does not trigger visibly, but for larger matrices the supplied `A_inv` would be inaccurate, making `woodbury_update` silently wrong.

---

## Category: optimization_and_distances

---
*△ AURA Pattern Library — © Reality Optimizer*
