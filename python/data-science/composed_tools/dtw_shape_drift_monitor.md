# dtw shape drift monitor

**Language:** Python · **Sphere:** data-science · **Category:** Composed Tools

**Signature:** `(a: List[float], b: List[float]) → float`

## What it does

DTW Shape-Drift Monitor — catching "the day looks wrong" when every point
statistic looks fine.

COMPOSED PATTERN: dtw_dynamic_time_warping (Optimization & Distances) x
ewma_streaming_metrics (Applied DS Practice) — embedding bridge 0.501, found
2026-07-06. Point monitors (mean/variance z-scores) are blind to SHAPE: a
daily profile whose peak moved six hours has the same mean and variance as a
normal day. This monitor DTW-matches each day against a reference profile and
EWMA-smooths the distances; drift = smoothed distance crossing a calibrated
MAD fence. Shape becomes a monitored quantity.

Use when: monitoring periodic profiles (traffic, load, sales) where timing
and shape matter, not just level.

## Guarantee

When it runs, dtw shape drift monitor guarantees not any((i >= change_at for i in point_alarms)); shape_alarms and change_at <= first_alarm <= change_at + 2; not any((i < change_at for i in shape_alarms)) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `not any((i >= change_at for i in point_alarms))`
- `shape_alarms and change_at <= first_alarm <= change_at + 2`
- `not any((i < change_at for i in shape_alarms))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
