# Exponential Smoothing

**File:** `python/data-science/time_series/exponential_smoothing.py`
**Sphere:** Data Science — Time Series

---

## What it solves

**Smooth a time series and forecast short-term.** Simple Exponential Smoothing (SES) smooths the level: smooth_t = α·y_t + (1−α)·smooth_{t-1}. Holt's Double Exponential Smoothing also captures linear trend. SES forecasts a flat line; Holt's forecasts a line with trend.

**When to use:** Short-horizon forecasting when trend matters — demand planning, inventory forecasting, any "what's next?" on a smooth series.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `series` | List[float], time series | numeric |
| `alpha` | float in (0, 1), level smoothing | higher = more responsive |
| `beta` | float in (0, 1), trend smoothing | only for Holt's |

---

## How inputs shape the output

- **SES reduces variance** — smoothed series is less variable than raw.
- **Holt's detects positive trend** in upward series (avg trend > 0).
- **Holt forecast increases** (due to positive trend) — SES forecast is flat.

---

## Worked example (real run)

```
$ python3 python/data-science/time_series/exponential_smoothing.py
exponential_smoothing.py PASS
```

**Reading the output:** on a series with upward trend, SES smooths the noise and Holt's detects the positive trend. Holt's forecast increases; SES forecast is flat.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| alpha or beta out of (0,1) | ValueError | needs guard |
| very short series | Holt's trend estimate unreliable | needs more data |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20