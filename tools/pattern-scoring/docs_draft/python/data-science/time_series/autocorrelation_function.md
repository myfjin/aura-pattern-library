# Autocorrelation Function (ACF)

**File:** `python/data-science/time_series/autocorrelation_function.py`
**Sphere:** Data Science — Time Series

---

## What it solves

**Measure how a time series correlates with its own past.** ACF(k) = correlation between y_t and y_{t-k}. Includes simple significance bounds (±2/√n) to identify significant lags. Use to detect seasonality and memory in the data.

**When to use:** First-look analysis of any time series — does it have memory? Is it seasonal? What lag structure matters?

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `series` | List[float], time series values | numeric |
| `nlags` | int, 0 ≤ nlags < len(series) | too large → ValueError |

---

## How inputs shape the output

- **ACF at lag 0 is always 1.0** (a series is perfectly correlated with itself).
- **For AR(1) with φ=0.6, ACF decays exponentially** as 0.6^k — the demo verifies this.
- **White noise has few significant lags** (< 5 at α=0.05) — the significance bound filters noise.

---

## Worked example (real run)

```
$ python3 python/data-science/time_series/autocorrelation_function.py
autocorrelation_function.py PASS
```

**Reading the output:** on an AR(1) series with φ=0.6, ACF at lag 1 is ~0.6 and decays. White noise shows few significant lags.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| constant series | all ACF = 0 | variance is zero |
| nlags ≥ len(series) | ValueError | needs guard |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20