# Shapley Value Sampling

**File:** `python/data-science/model_understanding_and_tuning/shapley_value_sampling.py`
**Sphere:** Data Science — Model Understanding and Tuning

---

## What it solves

**Estimate each feature's marginal contribution via random coalition sampling.** For a simple additive model, sampled Shapley values match analytic per-feature contributions. Avoids computing all 2^n coalitions.

**When to use:** Fair feature attribution that respects coalition marginal values, without exponential computation.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `feature_idx` | int, feature to evaluate | |
| `num_features` | int, total features | |
| `num_samples` | int, Monte Carlo samples | |
| `feature_values` | List[float], feature values | |

---

## How inputs shape the output

- **Sampled Shapley matches analytic** within 0.5 for additive model.
- **Error < 30% of max contribution** — reasonable approximation.
- **Monte Carlo sampling** avoids 2^n enumeration.

---

## Worked example (real run)

```
$ python3 python/data-science/model_understanding_and_tuning/shapley_value_sampling.py
Shapley Value Estimation (Additive Model)
==================================================
Feature 0: Sampled 2.0000, Analytic 2.0000, Error 0.0000
Feature 1: Sampled 6.0000, Analytic 6.0000, Error 0.0000
Feature 2: Sampled 4.5000, Analytic 4.5000, Error 0.0000
Feature 3: Sampled 10.0000, Analytic 10.0000, Error 0.0000
✓ Shapley Value Sampling: PASS
```

**Reading the output:** for an additive model f(x) = Σ (i+1)·x_i, sampled Shapley values match analytic values exactly.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| too few samples | high variance | needs more Monte Carlo samples |
| non-additive model | approximation error | Shapley still valid but harder to estimate |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20