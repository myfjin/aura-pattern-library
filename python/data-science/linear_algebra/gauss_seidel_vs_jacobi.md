# gauss seidel vs jacobi

**Language:** Python · **Sphere:** data-science · **Category:** Linear Algebra

**Signature:** `(A: list, b: list, x0: list, max_iter: int, tol: float) → Tuple[list, int]`

## What it does

Gauss–Seidel vs Jacobi: convergence rate comparison.

Both are stationary iterative solvers for A·x = b. Gauss–Seidel uses updated
values immediately; Jacobi uses old values. Core claim: Gauss–Seidel converges
faster (lower spectral radius). Planted system; iteration counts measured, ratio
verified (typically 2–5x faster).

## Guarantee

When it runs, gauss seidel vs jacobi guarantees iter_gs < iter_jacobi; abs(x_jacobi[i] - x_gs[i]) < 0.01 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `iter_gs < iter_jacobi`
- `abs(x_jacobi[i] - x_gs[i]) < 0.01`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:**
- `jacobi_iteration(A: list, b: list, x0: list, max_iter: int = 100, tol: float = 1e-8) -> Tuple[list, int]`
- `gauss_seidel_iteration(A: list, b: list, x0: list, max_iter: int = 100, tol: float = 1e-8) -> Tuple[list, int]`
**Valid input:** `A` n×n diagonally dominant (to guarantee convergence); `b`, `x0` length n.
**Core:** Two stationary iterative solvers for `A·x = b`. Jacobi updates all coordinates from the previous iterate; Gauss–Seidel uses freshly updated values immediately. Both return the solution and the iteration count to convergence.
**Assert:** On planted diagonally dominant 3×3 system, asserts Gauss–Seidel iterations < Jacobi iterations and that both solutions agree within `0.01`.
**⚠️ Defect:** No diagonal-zero guard. If any diagonal element is zero, both methods divide by zero and crash. Convergence is also not guaranteed for non-diagonally-dominant matrices; the docstring claims GS is faster as a general rule, but this only holds for systems where both methods converge.

---
*△ AURA Pattern Library — © Reality Optimizer*
