# adaptive simpson

**Language:** Python · **Sphere:** data-science · **Category:** Numerical Methods

**Signature:** `(f: Callable[[float], float], a: float, b: float, tol: float) → float`

## What it does

Adaptive Simpson's rule: automatic step refinement via error estimation.

Compares Simpson's estimate on [a, b] with two estimates on [a, c] and [c, b].
If error is acceptable, return result; else recurse. Typical result: O(h⁴)
accuracy with far fewer function evals than fixed-step methods. Planted
integral recovered; function eval count measured vs fixed Simpson.

## Guarantee

When it runs, adaptive simpson guarantees abs(integral - 2.0) < 1e-07 (proven by run).

**Checkable constraints:**

- `abs(integral - 2.0) < 1e-07`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
