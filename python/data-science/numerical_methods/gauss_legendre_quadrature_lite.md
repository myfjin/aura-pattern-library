# gauss legendre quadrature lite

**Language:** Python · **Sphere:** data-science · **Category:** Numerical Methods

**Signature:** `(f: Callable[[float], float], a: float, b: float) → float`

## What it does

Gauss–Legendre quadrature: optimal node placement for polynomial integration.

Hardcoded nodes and weights for n=4 (integrates degree ≤7 polynomials exactly).
Core claim: fewer function evals than trapezoid for smooth functions; exact on
high-degree polynomials. Planted integral recovered; order verified vs explicit formula.

## Guarantee

When it runs, gauss legendre quadrature lite guarantees abs(integral2 - 2.0) < 0.0001; abs(integral - 1.0 / 3.0) < 1e-10 (proven by run).

**Checkable constraints:**

- `abs(integral - 1.0 / 3.0) < 1e-10`
- `abs(integral2 - 2.0) < 0.0001`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
