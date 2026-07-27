# differencing stationarity

**Language:** C++ · **Sphere:** data-science · **Category:** Time Series

**Signature:** `(series: List[float]) → List[float]`

## What it does

Differencing for Stationarity — C++17 port.
First-difference a random walk and a trend; check stationarity diagnostics.

## Guarantee

When it runs, differencing stationarity guarantees vr_diff < vr_rw; drift_diff < drift_orig; len(diff_rw) == len(series_rw) - 1 (weak-grade: directional, proven by run on the PY original).

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
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
