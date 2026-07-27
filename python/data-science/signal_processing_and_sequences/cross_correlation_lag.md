# cross correlation lag

**Language:** Python · **Sphere:** data-science · **Category:** Signal Processing & Sequences

**Signature:** `(signal1: List[float], signal2: List[float]) → List[float]`

## What it does

Cross-Correlation and Lag Detection.

Compute cross-correlation between two signals.
The lag at which cross-correlation is maximum indicates the time shift
between signals. We plant a known lag and recover it.

## Guarantee

When it runs, cross correlation lag guarantees xcorr_at_true_lag > xcorr_at_zero_lag; len(signal2) == n; lag_error <= 2 (proven by run).

**Checkable constraints:**

- `len(signal2) == n`
- `lag_error <= 2`
- `xcorr_at_true_lag > xcorr_at_zero_lag`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
