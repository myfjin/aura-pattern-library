# secant method

**Language:** Python · **Sphere:** data-science · **Category:** Numerical Methods

**Signature:** `(f: Callable[[float], float], x0: float, x1: float, tol: float, max_iter: int) → float`

## What it does

Secant method: Newton's speed without derivatives.

Uses finite-difference slope from two prior points to approximate f'(x).
Core claim: converges superlinearly (order ≈1.618) without explicit derivative.
Planted root recovered; convergence order measured vs analytic predictions.

## Guarantee

When it runs, secant method guarantees abs(root - 1.2599) < 0.0001; abs(f_planted(root)) < 1e-08 (proven by run).

**Checkable constraints:**

- `abs(root - 1.2599) < 0.0001`
- `abs(f_planted(root)) < 1e-08`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
