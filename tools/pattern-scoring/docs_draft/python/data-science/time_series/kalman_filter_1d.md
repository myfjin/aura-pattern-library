# 1D Kalman Filter

**File:** `python/data-science/time_series/kalman_filter_1d.py`
**Sphere:** Data Science — Time Series

---

## What it solves

**Recursively estimate the state of a 1D system from noisy observations.** State is the true (unknown) value. The filter balances prediction (prior) and observation (likelihood) using Gaussian uncertainties. Reduces measurement noise by combining the prediction and the innovation weighted by the Kalman gain.

**When to use:** Smoothing GPS readings, sensor data, or tracking slow-moving targets — any setting where you have noisy observations of a slowly changing quantity.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `observations` | List[float], noisy measurements | numeric |
| `process_variance` | float > 0, how much state can change | small for constant signals |
| `measurement_variance` | float > 0, sensor noise | should match actual noise |
| `initial_state` | float, prior on state | guess |
| `initial_estimate_error` | float > 0, uncertainty in prior | larger = more trust in observations |

---

## How inputs shape the output

- **Filtered MSE is lower than raw observation MSE** — the filter reduces noise.
- **Kalman gains are in (0, 1)** and **converge** — the filter learns to trust its estimate.
- **Filtered mean is close to the true value** — the estimate is unbiased.

---

## Worked example (real run)

```
$ python3 python/data-science/time_series/kalman_filter_1d.py
kalman_filter_1d.py PASS
```

**Reading the output:** on a constant signal (true value 10) with Gaussian noise (σ=2), the Kalman filter reduces MSE and converges to the true value.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| process_variance too high | filter follows noise | overfits to observations |
| measurement_variance too low | filter ignores observations | trusts noisy predictions too much |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20