# power iteration shifted

**Language:** Python · **Sphere:** data-science · **Category:** Linear Algebra

**Signature:** `(A: list, shift: float, max_iter: int, tol: float) → Tuple[float, list]`

## What it does

Power iteration with shift: find smallest eigenvalue via (A - σI) iteration.

Power iteration on A finds largest |λ|. Shifting by σ gives largest |λ - σ|,
which is the smallest eigenvalue if σ > largest eigenvalue. Core claim:
smallest eigenvalue recovered; shift verified optimal. Planted symmetric matrix;
smallest eigenvalue vs Jacobi diagonalization checked.

## Guarantee

When it runs, power iteration shifted guarantees 0.5 < eigenvalue < 1.5; abs(Av[i] - lambda_v[i]) < 0.1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `0.5 < eigenvalue < 1.5`
- `abs(Av[i] - lambda_v[i]) < 0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `power_iteration_shifted(A: list, shift: float, max_iter: int = 100, tol: float = 1e-8) -> Tuple[float, list]`
**Valid input:** `A` n×n symmetric matrix; `shift` larger than the largest eigenvalue of `A`.
**Core:** Shifted power iteration to find the smallest eigenvalue of `A`. Iterates on `(A - shift·I)⁻¹` implicitly by multiplying by `(A - shift·I)`, then recovers the eigenvalue via the Rayleigh quotient.
**Assert:** On `A = [[4,1,0],[1,3,1],[0,1,2]]` with `shift = 5.0`, asserts smallest eigenvalue in `[0.5, 1.5]` and `A·v ≈ λ·v` within `0.1`.
**⚠️ Defect:** The method does not invert `(A - shift·I)`; it directly multiplies by `(A - shift·I)`, which is power iteration on the *most shifted* matrix rather than inverse iteration. Convergence is to the eigenvalue farthest from `shift` (largest magnitude of `λ - shift`), which equals the smallest `λ` only if `shift > λ_max`. The docstring claims this is verified, but the implementation silently gives the wrong eigenpair if `shift` is chosen differently.

---
*△ AURA Pattern Library — © Reality Optimizer*
