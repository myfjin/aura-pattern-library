# RTS Kalman Smoother

**File:** `python/data-science/probabilistic_modeling/rts_kalman_smoother.py`
**Sphere:** Data Science — Probabilistic Modeling

---

## What it solves

**Forward-backward pass for optimal smoothing.** Forward Kalman filter, then backward pass (Rauch-Tung-Striebel) corrects the trajectory using all future observations. Smoothed RMSE < filtered RMSE < raw observations.

**When to use:** Trajectory estimation, state inference after all data arrives (offline).

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `observations` | List[float], noisy measurements | |
| `process_var` | float > 0, state transition variance | |
| `meas_var` | float > 0, measurement variance | |

---

## How inputs shape the output

- **Smoothed RMSE < filtered RMSE < raw RMSE** — the defining hierarchy.
- **Covariances are positive** — valid uncertainty.
- **Smoothed covariances ≤ filtered covariances** — less uncertainty after backward pass.

---

## Worked example (real run)

```
$ python3 python/data-science/probabilistic_modeling/rts_kalman_smoother.py
PASS
```

**Reading the output:** on a 30-step random walk with observation noise σ=1.0, the RTS smoother beats the Kalman filter, which beats raw observations.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| process_var too high | smoother trusts observations | overfits to noise |
| meas_var too low | smoother ignores observations | trusts predictions too much |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20