# Platt Scaling for Probability Calibration

**File:** `python/data-science/model_understanding_and_tuning/platt_scaling_calibration.py`
**Sphere:** Data Science — Model Understanding and Tuning

---

## What it solves

**When a classifier outputs uncalibrated scores (overconfident), fit a logistic function (Platt scaling) on a hold-out set to map scores to true probabilities.** Improves Brier score and reliability.

**When to use:** You've trained a classifier and want to recalibrate confidence scores to match true conditional probabilities.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `scores` | List[float], uncalibrated scores | |
| `labels` | List[float], binary labels | |

---

## How inputs shape the output

- **Calibrated Brier score < baseline Brier score** — the defining improvement.
- **Calibrated Brier < 0.25** — reasonable calibration.
- **Logistic function** p = 1 / (1 + exp(−(a·score + b))).

---

## Worked example (real run)

```
$ python3 python/data-science/model_understanding_and_tuning/platt_scaling_calibration.py
Baseline Brier: 0.2500
Calibrated Brier: 0.2400
Improvement: 4.0%
✓ Platt Scaling Calibration: PASS
```

**Reading the output:** extreme scores (0.05 or 0.95) with ~50/50 labels are poorly calibrated. Platt scaling reduces Brier score.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| already calibrated | scaling is near-identity | no harm |
| very small calibration set | may overfit | needs enough data |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20