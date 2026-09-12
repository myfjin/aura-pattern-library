# Calibration Curve & Brier Score

**File:** `python/data-science/model_diagnostics/calibration_curve.py`
**Sphere:** Data Science — Model Diagnostics

---

## What it solves

**Is your model's confidence trustworthy?** A well-calibrated classifier: when it predicts 70% probability, the event actually happens ~70% of the time. This pattern bins predicted probabilities, compares them to observed frequencies, and computes the Expected Calibration Error (ECE) and Brier Score. It demonstrates the difference between a well-calibrated model and an overconfident one.

**When to use:** Any time your classifier outputs probabilities and you need to trust them — risk assessment, medical diagnosis, credit scoring. Overconfident models (predicting near 0 or 1 when they should be cautious) are dangerous.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `scores` | list of float in [0, 1] | — |
| `labels` | list of int {0, 1} | — |
| `n_bins` | int ≥ 2 | — |

---

## How inputs shape the output

- **Well-calibrated data has low ECE:** when P(y=1) = score by construction, the calibration curve is near the diagonal.
- **Overconfident data has high ECE:** when scores are extreme but labels are uniform, the calibration curve deviates from the diagonal.
- **Brier score confirms the pattern:** the MSE between predictions and labels is lower for well-calibrated models.

---

## Worked example (real run)

```
$ python3 python/data-science/model_diagnostics/calibration_curve.py
calibration_curve.py: PASS
```

**Reading the output:** the well-calibrated model has lower ECE and lower Brier score than the overconfident model — the metrics correctly identify calibration quality.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| empty bin | skipped (no indices) | correct |
| all same score | single bin, ECE = 0 | degenerate but correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18
