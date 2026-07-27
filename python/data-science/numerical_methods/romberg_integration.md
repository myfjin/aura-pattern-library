# romberg integration

**Language:** Python · **Sphere:** data-science · **Category:** Numerical Methods

**Signature:** `(f: Callable[[float], float], a: float, b: float, n: int) → float`

## What it does

Romberg integration: Richardson extrapolation on trapezoid rule.

Generates a table of progressively refined trapezoid estimates, then
extrapolates to higher-order accuracy. Core claim: O(h⁴) error for smooth
integrand vs O(h²) from bare trapezoid. Planted integral recovered; order verified.

## Guarantee

When it runs, romberg integration guarantees abs(integral - 2.0) < 1e-06 (proven by run).

**Checkable constraints:**

- `abs(integral - 2.0) < 1e-06`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
