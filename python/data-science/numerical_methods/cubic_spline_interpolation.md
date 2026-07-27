# cubic spline interpolation

**Language:** Python · **Sphere:** data-science · **Category:** Numerical Methods

**Signature:** `(x_data: list, y_data: list, x_eval: list) → list`

## What it does

Natural cubic spline: piecewise cubic interpolation with C² continuity.

Solves tridiagonal system for interior knot second derivatives; uses them to
define cubic polynomials on each segment. Core claim: C² continuity + smooth
approximation. Planted function (sin curve) interpolated; values and derivatives
recovered exactly at nodes, smooth between.

## Guarantee

When it runs, cubic spline interpolation guarantees abs(y_s - y_e) < 0.05 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(y_s - y_e) < 0.05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
