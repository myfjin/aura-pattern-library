# kalman filter 1d

**Language:** Python · **Sphere:** data-science · **Category:** Time Series

**Signature:** `(observations: List[float], process_variance: float, measurement_variance: float, initial_state: float, initial_estimate_error: float) → Tuple[List[float], List[float]]`

## What it does

1D Kalman Filter

Recursively estimate the state of a 1D system (constant velocity model).
State: x = [position, velocity]. Observations are noisy position measurements.
The filter balances prediction (prior) and observation (likelihood) using
Gaussian uncertainties (variances). Reduces observation noise.
Use for smoothing GPS, sensor readings, or tracking slow-moving targets.

## Guarantee

When it runs, kalman filter 1d guarantees abs(filtered_mean - true_value) < 0.5; filtered_mse < raw_mse; all((0 < g < 1 for g in gains)) (proven by run).

**Checkable constraints:**

- `filtered_mse < raw_mse`
- `all((0 < g < 1 for g in gains))`
- `abs(gains_early - gains_late) < 0.1`
- `abs(filtered_mean - true_value) < 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
