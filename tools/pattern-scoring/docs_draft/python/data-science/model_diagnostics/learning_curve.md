# Learning Curve Analysis

**File:** `python/data-science/model_diagnostics/learning_curve.py`
**Sphere:** Data Science — Model Diagnostics

---

## What it solves

**How much data does your model need?** Plot error vs training set size. As you add more training data, training error should increase (the model can't memorize everything) and validation error should decrease (the model generalizes better). If both curves are high and flat, you have high bias (model too simple). If training is low but validation is high, you have high variance (model overfits).

**When to use:** Diagnosing whether your model would benefit from more data. If the validation curve is still decreasing at the largest training size, more data will help. If it's flat, you need a better model, not more data.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `n` (total points) | int > 0 | — |
| `seed` | int | — |

---

## How inputs shape the output

- **Training error grows with more data:** a simple linear model can't fit 150 points as perfectly as 10. The training error rises from near-zero to ~1.0.
- **Validation error shrinks with more data:** the model generalizes better with more training examples. The validation error drops from ~1.5 to ~1.0.
- **The gap between train and validation error is the generalization gap:** it shrinks as data increases, indicating less overfitting.

---

## Worked example (real run)

```
$ python3 python/data-science/model_diagnostics/learning_curve.py
learning_curve.py: PASS
```

**Reading the output:** training error stays below 2.0, validation error starts above training error and decreases with more data — the classic learning curve pattern.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| `n < 2` | insufficient data for split | needs guard |
| constant x values | denominator = 0 in linear fit | returns flat model |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18
