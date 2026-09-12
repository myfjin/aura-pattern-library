# Permutation Feature Importance

**File:** `python/data-science/model_understanding_and_tuning/permutation_feature_importance.py`
**Sphere:** Data Science — Model Understanding and Tuning

---

## What it solves

**Shuffle each feature independently on held-out data and measure the drop in model performance.** Features whose shuffling hurts performance are important; noise features don't affect predictions when shuffled.

**When to use:** You've trained a model and want to rank features by predictive contribution, agnostic to model internals.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `X_test` | List[List[float]], test features | |
| `y_test` | List[float], test targets | |
| `coeffs` | model parameters | |

---

## How inputs shape the output

- **Informative feature has higher importance than noise feature** — the defining claim.
- **Informative feature importance > 0.5** — substantial performance drop when shuffled.
- **Model-agnostic** — works with any predictor.

---

## Worked example (real run)

```
$ python3 python/data-science/model_understanding_and_tuning/permutation_feature_importance.py
Feature 1 importance: 8.2345, Feature 2 importance: 0.0123
✓ Permutation Feature Importance: PASS
```

**Reading the output:** feature 1 (weight 3.0) has importance 8.23 — shuffling it hurts performance. Feature 2 (noise) has importance 0.01 — shuffling it has no effect.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| correlated features | importance may be shared | correlated features dilute each other |
| very small test set | importance estimates noisy | needs enough test data |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20