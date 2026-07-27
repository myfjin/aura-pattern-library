# differencing stationarity

**Language:** Python · **Sphere:** data-science · **Category:** Time Series

**Signature:** `(series: List[float]) → List[float]`

## What it does

Differencing for Stationarity

First differencing transforms a non-stationary series (e.g., random walk)
into a stationary one. Differenced series: d_t = y_t - y_{t-1}.
Stationarity (constant mean, variance) enables forecasting with AR models.
Demonstrate that differencing reduces mean and variance drift in a trend.

## Guarantee

When it runs, differencing stationarity guarantees vr_diff < vr_rw; drift_diff < drift_orig; len(diff_rw) == len(series_rw) - 1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `vr_diff < vr_rw`
- `drift_diff < drift_orig`
- `len(diff_rw) == len(series_rw) - 1`
- `len(diff_trend) == len(series_trend) - 1`
- `abs(diff_mean) < 1.0`
- `abs(diff_trend_mean) < 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
