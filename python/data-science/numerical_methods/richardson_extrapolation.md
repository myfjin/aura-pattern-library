# richardson extrapolation

**Language:** Python · **Sphere:** data-science · **Category:** Numerical Methods

**Signature:** `(F: Callable[[float], float], h: float, p: int) → float`

## What it does

Richardson extrapolation: boost convergence order via linear combination.

If F(h) ≈ L + C·h^p + O(h^(2p)) and the step is halved, then
(2^p·F(h/2) - F(h))/(2^p - 1) ≈ L + O(h^(2p)) — the C·h^p term cancels because
F(h/2) carries it scaled by (1/2)^p. Core claim: raises O(h^p) error to O(h^(2p))
without changing the method. Planted integral; error dropped to O(h^(2p)) verified.

NOTE: the elimination factor is 2^p (the halving ratio raised to the order), NOT p.
Using p leaves a residual -C·h^p/2 and stays O(h^p) — see romberg_integration's 4^j.

## Guarantee

When it runs, richardson extrapolation guarantees error_after < error_before; error_after < 1e-10 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `error_after < error_before`
- `error_after < 1e-10`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
