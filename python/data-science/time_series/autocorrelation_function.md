# autocorrelation function

**Language:** Python · **Sphere:** data-science · **Category:** Time Series

**Signature:** `(series: List[float], nlags: int) → List[float]`

## What it does

Autocorrelation Function (ACF)

Compute the autocorrelation of a time series at multiple lags.
ACF(k) = correlation between y_t and y_{t-k}.
Include simple significance bounds (±2/sqrt(n)) to identify significant lags.
Use to detect seasonality and memory in the data.

## Guarantee

When it runs, autocorrelation function guarantees acf_vals[0] == 1.0; 0.4 < acf_vals[1] < 0.8; acf_vals[1] > acf_vals[2] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(acf_vals) == 21`
- `acf_vals[0] == 1.0`
- `0.4 < acf_vals[1] < 0.8`
- `acf_vals[1] > acf_vals[2]`
- `acf_vals[2] > acf_vals[5]`
- `bound > 0 and bound < 0.2`
- `len(sig_lags) > 0`
- `1 in sig_lags`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
