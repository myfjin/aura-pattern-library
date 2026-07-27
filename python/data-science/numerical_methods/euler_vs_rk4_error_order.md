# euler vs rk4 error order

**Language:** Python · **Sphere:** data-science · **Category:** Numerical Methods

**Signature:** `(f: Callable[[float, float], float], t: float, y: float, h: float) → float`

## What it does

Forward Euler vs RK4: measure convergence order difference.

Solves same ODE with both methods at successive step sizes; measures error vs h.
Core claim: Euler is O(h), RK4 is O(h⁴). Planted ODE with known solution;
measured convergence rates match theory, RK4 dominates at fine steps.

## Guarantee

When it runs, euler vs rk4 error order guarantees 1.5 < euler_ratio < 2.5; 10 < rk4_ratio < 20 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `1.5 < euler_ratio < 2.5`
- `10 < rk4_ratio < 20`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
