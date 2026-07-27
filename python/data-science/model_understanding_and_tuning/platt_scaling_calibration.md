# platt scaling calibration

**Language:** Python · **Sphere:** data-science · **Category:** Model Understanding & Tuning

**Signature:** `(z: float) → float`

## What it does

Platt Scaling for Probability Calibration

Core idea: When a classifier outputs uncalibrated scores (overconfident), fit a logistic
function (Platt scaling) on a hold-out set to map scores to true probabilities.

When to use: You've trained a classifier and want to recalibrate its confidence scores to
match true conditional probabilities, improving Brier score and reliability diagrams.

## Guarantee

When it runs, platt scaling calibration guarantees baseline_brier > calibrated_brier; calibrated_brier < 0.25 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `baseline_brier > calibrated_brier`
- `calibrated_brier < 0.25`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
