# Partial Dependence Plot

**File:** `python/data-science/model_understanding_and_tuning/partial_dependence_data.py`
**Sphere:** Data Science — Model Understanding and Tuning

---

## What it solves

**For each feature, marginalize over other features and plot the average model prediction as that feature varies.** Linear features show monotone curves; noise features show flat.

**When to use:** Understanding the marginal effect of a feature on predictions, holding other features constant in aggregate.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `X` | List[List[float]], training data | |
| `intercept`, `weights` | model parameters | |
| `feat_idx` | int, feature index to analyze | |
| `x_range` | List[float], values to evaluate | |

---

## How inputs shape the output

- **Informative feature shows monotone increasing curve** — the defining signal.
- **Noise feature shows flat curve** — no marginal effect.
- **Average over all data points** — marginalization.

---

## Worked example (real run)

```
$ python3 python/data-science/model_understanding_and_tuning/partial_dependence_data.py
PD Feature 1: ['10.00', '11.00', '12.00', '13.00', '14.00', '15.00', '16.00', '17.00', '18.00', '19.00', '20.00']
PD Feature 2: ['15.00', '15.00', '15.00', '15.00', '15.00', '15.00', '15.00', '15.00', '15.00', '15.00', '15.00']
✓ Partial Dependence Plot: PASS
```

**Reading the output:** feature 1 (weight 2.0) shows a clear increasing trend. Feature 2 (weight 0.1) is flat — it's noise.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| correlated features | PD may show extrapolation artifacts | assumes independence |
| very small data | PD may be noisy | needs enough samples |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20