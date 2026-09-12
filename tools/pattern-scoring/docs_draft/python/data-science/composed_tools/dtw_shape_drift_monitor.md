# DTW Shape-Drift Monitor

**File:** `python/data-science/composed_tools/dtw_shape_drift_monitor.py`
**Sphere:** Data Science — Composed Tools

---

## What it solves

**Catch "the day looks wrong" when every point statistic looks fine.** Point monitors (mean/variance z-scores) are blind to SHAPE: a daily profile whose peak moved six hours has the same mean and variance as a normal day. This monitor DTW-matches each day against a reference profile and EWMA-smooths the distances; drift = smoothed distance crossing a calibrated MAD fence.

**When to use:** Monitoring periodic profiles (traffic, load, sales) where timing and shape matter, not just level.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `reference` | List[float], reference daily profile | 24-point diurnal shape |
| `days` | List[List[float]], daily profiles to monitor | each 24 points |

---

## How inputs shape the output

- **Point monitor is blind to shape change** (mean/var preserved) — that's the whole point.
- **Shape monitor catches the drift within 3 days** of the change.
- **Zero false alarms on normal days** — the MAD fence from calibration is clean.

---

## Worked example (real run)

```
$ python3 python/data-science/composed_tools/dtw_shape_drift_monitor.py
point-statistic alarms on shape-drift days: []
shape alarms: first at day 21 (change at day 20) · fence 15.2 · calib DTW ~8.1 · drift DTW ~22.4
dtw_shape_drift_monitor.py PASS
```

**Reading the output:** the point monitor flags zero shape-drift days (blind). The shape monitor catches the drift on day 21, one day after the change at day 20.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| amplitude-only change | both monitors catch it | point monitor works for level shifts |
| very noisy profiles | shape monitor may false-alarm | MAD fence needs calibration |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20