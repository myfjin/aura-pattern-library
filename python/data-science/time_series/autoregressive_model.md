# autoregressive model

**Language:** Python · **Sphere:** data-science · **Category:** Time Series

**Signature:** `(a: float, b: float, c: float, d: float, e: float, f: float) → Tuple[float, float]`

## What it does

Autoregressive (AR) Model

Fit an AR(p) model by regressing y_t on its p lagged values using least squares.
Solves the normal equations directly (no external libraries). Produces one-step-ahead
forecasts. Use for univariate time series prediction when past values predict the future.

## Guarantee

When it runs, autoregressive model guarantees 0.5 < coeffs_1[1] < 0.9; len(fcst_1) == len(series) - 1; mae_ar < mae_naive (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(coeffs_1) == 2`
- `0.5 < coeffs_1[1] < 0.9`
- `len(fcst_1) == len(series) - 1`
- `mae_ar < mae_naive`
- `len(coeffs_2) == 3`
- `len(fcst_2) == len(series) - 2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
