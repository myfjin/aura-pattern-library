# bootstrap regression

**Language:** R · **Sphere:** R · **Category:** Regression & GLM

## What it does

bootstrap_regression.R
Case-resampling bootstrap for linear regression slope confidence interval.
Claim: bootstrap CI covers planted slope; CI width shrinks with larger n.
Tolerance: coverage >90%; width decrease demonstrable.

## Guarantee

When it runs, bootstrap regression guarantees ci_lower <= true_slope && true_slope <= ci_upper; width_large < width_small; ci_lower < ci_upper (weak-grade: directional, proven by run).

**Checkable constraints:**

- `ci_lower <= true_slope && true_slope <= ci_upper`
- `width_large < width_small`
- `all(!is.na(bootstrap_slopes))`
- `ci_lower < ci_upper`
- `abs(mean(bootstrap_slopes) - true_slope) < 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Numeric predictor vector `x` and response vector `y` of equal length; a scalar `true_slope` for the coverage assertion.
**Core:** Resamples `(x, y)` cases with replacement `n_boot` times, fits `lm(y_boot ~ x_boot)` each time, and records the slope. Returns the percentile 95% CI and demonstrates CI width reduction with `n = 200` versus `n = 50`.
**Assert:** The planted `true_slope` lies within the 95% CI; the larger-sample CI width is strictly smaller than the smaller-sample width; all bootstrap slopes are non-`NA`; the bootstrap slope mean is within 0.5 of `true_slope`.
**⚠️ Defect:** Hardcoded `n_boot = 1000` and `alpha = 0.05`. Uses only the percentile method — no BCa or bias correction. `NA` values in `x`/`y` silently propagate through `lm()`. No input validation (length mismatch, constant vectors, empty inputs). No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
