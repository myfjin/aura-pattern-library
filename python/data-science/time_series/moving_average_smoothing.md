# moving average smoothing

**Language:** Python · **Sphere:** data-science · **Category:** Time Series

**Signature:** `(series: List[float], window: int) → List[float]`

## What it does

Moving Average Smoothing

Smooth a noisy time series using simple and weighted moving averages.
Reduces short-term fluctuations while preserving trend; wider windows smooth
more but lag the signal. Use for noise reduction in raw sensor or market data.

## Guarantee

When it runs, moving average smoothing guarantees sma_var < raw_var; wma_var < raw_var; sma_var > 0 and wma_var > 0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `sma_var < raw_var`
- `wma_var < raw_var`
- `sma_var > 0 and wma_var > 0`
- `len(sma) == len(noisy_series)`
- `len(wma) == len(noisy_series)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
