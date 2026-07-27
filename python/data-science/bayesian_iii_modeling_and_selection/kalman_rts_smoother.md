# kalman rts smoother

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Modeling & Selection

**Signature:** `(y: List[float], q: float, r: float) → Tuple[List[float], List[float]]`

## What it does

Kalman filter + Rauch-Tung-Striebel (RTS) smoother: the backward pass lowers MSE.

The filter estimates each state from the past only; the RTS smoother adds a backward pass
that also uses the future, so on a random-walk state model it recovers the latent trajectory
with strictly lower error IN EXPECTATION. Core claim: over many random-walk realizations the
mean smoother MSE is below the mean filter MSE.

## Guarantee

When it runs, kalman rts smoother guarantees mean_mse_smooth < mean_mse_filt; mean_mse_smooth < 0.9 * mean_mse_filt (weak-grade: directional, proven by run).

**Checkable constraints:**

- `mean_mse_smooth < mean_mse_filt`
- `mean_mse_smooth < 0.9 * mean_mse_filt`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
