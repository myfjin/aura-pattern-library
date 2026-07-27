# fixed point iteration

**Language:** Python · **Sphere:** data-science · **Category:** Numerical Methods

**Signature:** `(g: Callable[[float], float], x0: float, tol: float, max_iter: int) → float`

## What it does

Fixed-point iteration: find x where g(x) = x.

Equivalently solves f(x) = 0 by reformulating as g(x) = x where g(x) = x - f(x).
Core claim: convergence speed depends on |g'(x*)|; contraction mapping guarantees.
Planted fixed point recovered; measured iteration count vs theory (linear order).

## Guarantee

When it runs, fixed point iteration guarantees abs(fixed_pt - 0.7391) < 0.001; abs(g_planted(fixed_pt) - fixed_pt) < 1e-07 (proven by run).

**Checkable constraints:**

- `abs(g_planted(fixed_pt) - fixed_pt) < 1e-07`
- `abs(fixed_pt - 0.7391) < 0.001`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
