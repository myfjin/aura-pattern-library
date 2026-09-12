# CUSUM Change-Point Detection

**File:** `python/data-science/time_series/cusum_changepoint.py`
**Sphere:** Data Science — Time Series

---

## What it solves

**Detect step changes in the mean of a time series.** CUSUM_t = max(0, CUSUM_{t-1} + (y_t − target) − k). When CUSUM exceeds a threshold h, a change is signaled and the CUSUM resets. Use to detect sensor drift, process shifts, or any sudden level change.

**When to use:** Monitoring industrial processes, sensor data, or any stream where you need to detect a mean shift quickly.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `series` | List[float], time series | numeric |
| `target` | float, reference mean | should be pre-change mean |
| `k` | float, slack parameter | typically shift_size / 2 |
| `h` | float, decision threshold | several times the std |

---

## How inputs shape the output

- **CUSUM stays low before the change** and **rises after** — the cumulative deviation accumulates.
- **Detection near the true change point** (within ~10 samples for a 5σ shift).
- **Resets after each detection** so multiple changes can be found.

---

## Worked example (real run)

```
$ python3 python/data-science/time_series/cusum_changepoint.py
cusum_changepoint.py PASS
```

**Reading the output:** on a series shifting from mean 10 to mean 15 at index 50, CUSUM detects the change near index 50 with k=2.5, h=8.0.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| k too large | misses small shifts | too much slack |
| h too small | false alarms on noise | threshold too tight |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20