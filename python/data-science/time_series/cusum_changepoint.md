# cusum changepoint

**Language:** Python · **Sphere:** data-science · **Category:** Time Series

**Signature:** `(series: List[float], target: float, k: float, h: float) → Tuple[List[float], List[int]]`

## What it does

CUSUM Change-Point Detection

Cumulative Sum (CUSUM) control chart detects shifts in mean.
CUSUM_t = max(0, CUSUM_{t-1} + (y_t - target) - k)
When CUSUM exceeds a threshold h, a change is signaled.
Use to detect step changes in level (e.g., sensor drift, process shift).

## Guarantee

When it runs, cusum changepoint guarantees 40 < first_cp < 60; cusum_after > cusum_before (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(changepoints) > 0`
- `40 < first_cp < 60`
- `cusum_after > cusum_before`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
