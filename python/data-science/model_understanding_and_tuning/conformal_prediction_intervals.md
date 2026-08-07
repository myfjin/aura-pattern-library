# conformal prediction intervals

**Language:** Python · **Sphere:** data-science · **Category:** Model Understanding & Tuning

**Signature:** `(X: List[float], y: List[float]) → Tuple[float, float]`

## What it does

Split-Conformal Prediction Intervals for Regression

Core idea: Split data into train/calibration. Train a regression model, then on calibration
data compute residuals to set interval width such that coverage is guaranteed.

When to use: You want prediction intervals with a formal coverage guarantee, even if the
model is miscalibrated or the error distribution is non-Gaussian.

## Guarantee

When it runs, conformal prediction intervals guarantees coverage >= 0.7; avg_width > 0 and avg_width < 100 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `coverage >= 0.7`
- `avg_width > 0 and avg_width < 100`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
