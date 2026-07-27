# gradient descent momentum

**Language:** Python · **Sphere:** data-science · **Category:** Optimization & Distances

**Signature:** `(x: float, y: float) → float`

## What it does

OPTIMIZATION: Gradient Descent with Momentum

Core idea: Vanilla gradient descent oscillates in narrow valleys; momentum accumulates
velocity across iterations, smoothing the path and converging faster. Compare vanilla GD
vs momentum GD on a 2D quadratic bowl.

When to use: Convex optimization with non-isotropic (elongated) loss landscapes; standard
in neural network training to accelerate convergence and reduce oscillation.

## Guarantee

When it runs, gradient descent momentum guarantees fx_vanilla < 1e-06; fx_momentum < 1e-06; iters_momentum < iters_vanilla (weak-grade: directional, proven by run).

**Checkable constraints:**

- `fx_vanilla < 1e-06`
- `fx_momentum < 1e-06`
- `iters_momentum < iters_vanilla`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:**
- `vanilla_gd(x: float, y: float, learning_rate: float = 0.005, tolerance: float = 1e-6, max_iters: int = 10000) -> Tuple[int, float]`
- `momentum_gd(x: float, y: float, learning_rate: float = 0.005, momentum: float = 0.9, tolerance: float = 1e-6, max_iters: int = 10000) -> Tuple[int, float]`
**Valid input:** Any real `x`, `y`; `learning_rate > 0`; `momentum` in `[0,1)`; `tolerance > 0`.
**Core:** Minimizes the 2D quadratic bowl `f(x,y)=100x²+y²`. Vanilla GD takes raw gradient steps; momentum GD accumulates velocity `v = β·v + lr·grad` and subtracts `v` from parameters.
**Assert:** From `(10,10)` with `lr=0.005`, both reach `f < 1e-6`, and momentum uses fewer iterations than vanilla.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
