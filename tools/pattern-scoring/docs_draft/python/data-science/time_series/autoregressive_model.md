# Autoregressive (AR) Model

**File:** `python/data-science/time_series/autoregressive_model.py`
**Sphere:** Data Science — Time Series

---

## What it solves

**Predict the future from the past.** An AR(p) model says: the next value is a linear combination of the p previous values, plus noise. `y_t = c + φ₁·y_{t-1} + ... + φ_p·y_{t-p} + noise`. Fit by solving the normal equations directly (no external libraries). Produces one-step-ahead forecasts and beats the naive mean forecast.

**When to use:** Univariate time series prediction when past values predict the future. AR models are the foundation of all time series modeling — ARIMA, SARIMA, and state-space models all build on this idea.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `series` | list of float, length > p | too short → ValueError |
| `p` | 1 or 2 (only these implemented) | other → NotImplementedError |

---

## How inputs shape the output

- **p is the memory length:** AR(1) uses only the last value; AR(2) uses the last two. The demo's planted AR(1) with φ=0.7 is recovered within [0.5, 0.9].
- **The normal equations are solved explicitly:** for p=1, it's a single division; for p=2, it's a 2×2 system via Cramer's rule. This is the textbook method, implemented from scratch.
- **AR beats naive:** the one-step forecasts are compared against predicting the mean — AR should always win on data that has autocorrelation.

---

## Worked example (real run)

```
$ python3 python/data-science/time_series/autoregressive_model.py
autoregressive_model.py PASS
```

**Reading the output:** AR(1) recovers φ≈0.7 from the planted series. The MAE of AR forecasts beats the naive mean forecast. AR(2) also fits successfully.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| `p ≥ len(series)` | ValueError | honest |
| `p > 2` | NotImplementedError | only p=1,2 implemented |
| constant series | division by near-zero in normal eq | returns phi=0 (correct) |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18 · evidence: `output/manual_audit_2026-07-19.csv`
