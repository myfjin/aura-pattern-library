# black scholes monte carlo

**Language:** Python · **Sphere:** data-science · **Category:** Econometrics & Finance

**Signature:** `(S: float, K: float, T: float, r: float, sigma: float) → float`

## What it does

Black-Scholes Monte Carlo: European option pricing via simulation.

True closed-form price vs MC estimate. Core claim: MC price within CI of
closed-form; as simulations increase, confidence tightens. Planted S0, K, T,
r, σ; verifies formula and MC agreement.

## Guarantee

When it runs, black scholes monte carlo guarantees abs(call_mc - call_bs) < 3 * mc_se; call_bs > 0 and call_mc > 0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(call_mc - call_bs) < 3 * mc_se`
- `call_bs > 0 and call_mc > 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
