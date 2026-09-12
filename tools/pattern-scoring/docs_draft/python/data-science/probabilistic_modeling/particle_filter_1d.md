# Particle Filter (SMC)

**File:** `python/data-science/probabilistic_modeling/particle_filter_1d.py`
**Sphere:** Data Science — Probabilistic Modeling

---

## What it solves

**Track a noisy 1D random walk target using sequential Monte Carlo.** Maintain weighted particles; predict, weight by observation likelihood, resample. Particle-mean RMSE beats raw observations. Effective sample size monitors degeneracy.

**When to use:** Nonlinear filtering, state tracking, online Bayesian inference.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `particles` | List[float], particle states | |
| `weights` | List[float], particle weights | sum to 1 |
| `observation` | float, noisy measurement | |
| `process_noise` | float > 0, state transition noise | |
| `obs_noise` | float > 0, measurement noise | |

---

## How inputs shape the output

- **Particle-mean RMSE beats raw observation RMSE** — the defining claim.
- **ESS is positive and ≤ n_particles** — valid diagnostic.
- **Average ESS is reasonable** (not always 1 or n_particles).

---

## Worked example (real run)

```
$ python3 python/data-science/probabilistic_modeling/particle_filter_1d.py
PASS
```

**Reading the output:** on a 50-step random walk with observation noise σ=0.5, the particle filter (100 particles) achieves lower RMSE than raw observations.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| too few particles | ESS collapses | resampling fails |
| very high process noise | particles diverge | needs more particles |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20