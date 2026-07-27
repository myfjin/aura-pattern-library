# quantile regression pinball

**Language:** Python · **Sphere:** data-science · **Category:** Statistical Modeling

**Signature:** `(y: float, pred: float, tau: float) → float`

## What it does

Quantile Regression via Pinball Loss and Gradient Descent.

Estimates conditional quantiles (e.g., median, 90th percentile) by minimizing
the pinball (check) loss: L_tau(y, pred) = (tau - 1)*min(y-pred,0) + tau*max(y-pred,0).
Use when you need robust estimates of specific quantiles instead of the mean.

## Guarantee

When it runs, quantile regression pinball guarantees 0.35 < frac_below_median < 0.65; 0.75 < frac_below_90 < 0.99; a_90 + b_90 * 0.5 > a_median + b_median * 0.5 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `0.35 < frac_below_median < 0.65`
- `0.75 < frac_below_90 < 0.99`
- `a_90 + b_90 * 0.5 > a_median + b_median * 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `quantile_regression_linear(x_vals, y_vals, tau, learning_rate=0.01, n_iter=1000) → (intercept, slope)`
**Valid input:** `x_vals, y_vals: List[float]` — same length. `tau` in (0, 1). `learning_rate > 0`.
**Core:** Linear quantile regression via pinball loss gradient descent. Pinball loss: L_τ(y, ŷ) = τ·max(y-ŷ, 0) + (τ-1)·min(y-ŷ, 0). Gradient: -τ if y > ŷ, -(τ-1) if y ≤ ŷ. Fit median (τ=0.5) and 90th percentile (τ=0.9) lines.
**Assert:** On y = 1 + 0.5x + N(0,0.5) with 50 points, median line has 35-65% of points below it, 90th percentile line has 75-99% below, and 90th line is above median line.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
