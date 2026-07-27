# autocovariance spectrum

**Language:** Python · **Sphere:** data-science · **Category:** Signal Processing & Sequences

**Signature:** `(signal: List[float], max_lag: int) → List[float]`

## What it does

Autocovariance and Power Spectral Density (Periodogram).

Periodogram = DFT of autocovariance function.
For a signal with strong periodicity, the periodogram should show a peak at that frequency.
We plant a periodic signal and verify the periodogram peaks at the correct frequency.

## Guarantee

When it runs, autocovariance spectrum guarantees freq_error < 2.0; periodogram[peak_idx] > periodogram[peak_idx - 1]; periodogram[peak_idx] > periodogram[peak_idx + 1] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `freq_error < 2.0`
- `periodogram[peak_idx] > periodogram[peak_idx - 1]`
- `periodogram[peak_idx] > periodogram[peak_idx + 1]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
