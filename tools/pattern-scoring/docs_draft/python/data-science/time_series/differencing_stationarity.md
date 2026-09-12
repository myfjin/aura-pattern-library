# Differencing for Stationarity

**File:** `python/data-science/time_series/differencing_stationarity.py`
**Sphere:** Data Science — Time Series

---

## What it solves

**Transform a non-stationary series into a stationary one via first differencing.** Differenced series: d_t = y_t − y_{t-1}. Stationarity (constant mean, variance) enables forecasting with AR models. Demonstrates that differencing reduces mean and variance drift in trends and random walks.

**When to use:** Preprocessing step before fitting AR/ARIMA models — make the series stationary first.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `series` | List[float], time series | numeric |

---

## How inputs shape the output

- **Differenced random walk is more stationary** (variance ratio closer to 1) than the original.
- **Differencing reduces mean drift** in trended series — the defining claim.
- **Differenced series is shorter by 1** (no d_0).
- **Differenced random walk has mean close to 0** — the increments are zero-mean noise.

---

## Worked example (real run)

```
$ python3 python/data-science/time_series/differencing_stationarity.py
differencing_stationarity.py PASS
```

**Reading the output:** on a random walk and a linear trend, first differencing reduces variance drift and mean drift — both series become more stationary.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| already stationary series | differencing adds noise | may induce negative autocorrelation |
| seasonal pattern | first difference may not suffice | needs seasonal differencing |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20