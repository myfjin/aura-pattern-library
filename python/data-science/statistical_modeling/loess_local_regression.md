# loess local regression

**Language:** Python · **Sphere:** data-science · **Category:** Statistical Modeling

**Signature:** `(u: float) → float`

## What it does

LOESS-Lite: Locally Weighted Linear Regression.

Fits a piecewise linear regression using tricube-weighted local neighborhoods.
Simple non-parametric smoothing for noisy signals.
Use for smooth, adaptive curve fitting without assuming global model form.

## Guarantee

When it runs, loess local regression guarantees mse_loess < mse_linear (weak-grade: directional, proven by run).

**Checkable constraints:**

- `mse_loess < mse_linear`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `loess_smooth(x_vals, y_vals, x_grid, frac_nearest=0.3) → List[float]`
**Valid input:** `x_vals, y_vals: List[float]` — same length. `x_grid: List[float]`. `frac_nearest` in (0, 1].
**Core:** Locally weighted linear regression with tricube kernel: w(u) = (1 - |u|³)³ for |u| ≤ 1. For each target point, find k nearest neighbors (k = frac_nearest × n), compute tricube weights, fit weighted linear regression, predict.
**Assert:** On noisy sine wave (60 points, σ=0.3), LOESS (frac=0.3) MSE < global linear MSE.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
