# bisection newton hybrid

**Language:** Python · **Sphere:** data-science · **Category:** Numerical Methods

**Signature:** `(f: Callable[[float], float], df: Callable[[float], float], a: float, b: float, tol: float, max_iter: int) → float`

## What it does

Hybrid bisection–Newton root-finding for robustness.

Combines bisection's guaranteed convergence with Newton's speed: bisect when
Newton drift is detected, switch back when safe. Core claim: planted root
recovered accurately even when Newton would diverge or miss the derivative.

## Guarantee

When it runs, bisection newton hybrid guarantees abs(root - 3.0) < 1e-06; abs(f_planted(root)) < 1e-08 (proven by run).

**Checkable constraints:**

- `abs(root - 3.0) < 1e-06`
- `abs(f_planted(root)) < 1e-08`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
