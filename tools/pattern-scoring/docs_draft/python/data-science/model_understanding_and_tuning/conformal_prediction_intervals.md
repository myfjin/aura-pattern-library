# Split-Conformal Prediction Intervals

**File:** `python/data-science/model_understanding_and_tuning/conformal_prediction_intervals.py`
**Sphere:** Data Science — Model Understanding and Tuning

---

## What it solves

**Prediction intervals with a formal coverage guarantee, even if the model is miscalibrated or the error distribution is non-Gaussian.** Split data into train/calibration. Train a regression model, then on calibration data compute residuals to set interval width.

**When to use:** You want prediction intervals with guaranteed coverage, model-agnostic.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `X_train`, `y_train` | List[float], training data | |
| `X_cal`, `y_cal` | List[float], calibration data | |
| `confidence` | float in (0, 1), target coverage | |

---

## How inputs shape the output

- **Coverage ≥ 70%** (target 90%) — the defining guarantee.
- **Interval width is reasonable** (> 0, < 100).
- **Model-agnostic** — works with any regression model.

---

## Worked example (real run)

```
$ python3 python/data-science/model_understanding_and_tuning/conformal_prediction_intervals.py
Coverage: 88.00% (target 90%)
Average interval width: 6.52
✓ Conformal Prediction Intervals: PASS
```

**Reading the output:** on a linear model with Gaussian noise, split-conformal achieves 88% coverage (near the 90% target) with average interval width 6.52.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| very small calibration set | coverage may be conservative | needs enough calibration data |
| non-exchangeable data | coverage guarantee may not hold | assumes exchangeability |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20