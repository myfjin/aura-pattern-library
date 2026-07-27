# rts kalman smoother

**Language:** Python · **Sphere:** data-science · **Category:** Probabilistic Modeling

**Signature:** `(observations: List[float], process_var: float, meas_var: float) → Tuple[List[float], List[float], List[float], List[float]]`

## What it does

RTS (Rauch-Tung-Striebel) Kalman smoother: forward-backward pass for optimal smoothing.

Core idea: forward Kalman filter, then backward pass corrects trajectory.
Smoothed RMSE < filtered RMSE < raw observations.

When to use: trajectory estimation, state inference after all data arrives.

## Guarantee

When it runs, rts kalman smoother guarantees len(x_smooth) == len(observations); len(P_smooth) == len(observations); rmse_smooth < rmse_filt (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(x_smooth) == len(observations)`
- `len(P_smooth) == len(observations)`
- `rmse_smooth < rmse_filt`
- `rmse_filt < rmse_raw`
- `p > 0`
- `p > 0`
- `ps <= pf * 1.01`
- `range_val > 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
