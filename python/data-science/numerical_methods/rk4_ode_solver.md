# rk4 ode solver

**Language:** Python · **Sphere:** data-science · **Category:** Numerical Methods

**Signature:** `(f: Callable[[float, float], float], t0: float, y0: float, t_final: float, num_steps: int) → Tuple[list, list]`

## What it does

Fourth-order Runge–Kutta: standard explicit ODE integrator.

Solves dy/dt = f(t, y) using 4-stage RK scheme with O(h⁵) local error.
Core claim: high accuracy on smooth systems; verified vs analytic solutions.
Planted ODE (exponential decay) integrated; solution recovered to tight tolerance.

## Guarantee

When it runs, rk4 ode solver guarantees abs(y_final - expected) < 1e-05 (proven by run).

**Checkable constraints:**

- `abs(y_final - expected) < 1e-05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
