# newton method optimization

**Language:** Python · **Sphere:** data-science · **Category:** Optimization & Distances

**Signature:** `(x: float) → float`

## What it does

OPTIMIZATION: Newton's Method for 1D Minimization

Core idea: Use second-order (curvature) information via the Hessian to take
smarter steps than gradient descent. Newton's method quadratically converges
near the optimum, often faster than first-order methods on well-conditioned problems.

When to use: 1D or small-scale smooth optimization where second derivatives are
available; faster convergence than GD on strongly convex objectives, but can diverge
if not near optimum or if Hessian is singular.

## Guarantee

When it runs, newton method optimization guarantees abs(x_newton - 2.0) < 1e-08; abs(x_gd - 2.0) < 1e-06; iters_newton < iters_gd (proven by run).

**Checkable constraints:**

- `abs(x_newton - 2.0) < 1e-08`
- `abs(x_gd - 2.0) < 1e-06`
- `iters_newton < iters_gd`
- `abs(f_newton - -2.0) < 1e-08`
- `abs(f_gd - -2.0) < 1e-06`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:**
- `newton_method(x_init: float, tolerance: float = 1e-10, max_iters: int = 100) -> Tuple[int, float]`
- `gradient_descent(x_init: float, learning_rate: float = 0.1, tolerance: float = 1e-10, max_iters: int = 1000) -> Tuple[int, float]`
**Valid input:** Any real `x_init`; hard-wired to the quadratic `f(x)=3x²-12x+10`.
**Core:** Demonstrates 1D Newton’s method and gradient descent on a fixed quadratic. Newton uses exact gradient and constant Hessian (`6.0`); GD uses fixed learning rate.
**Assert:** From `x_init=0`, both methods converge to `x=2` and `f=-2`, and Newton uses fewer iterations than GD.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
