# hosmer lemeshow lite

**Language:** R · **Sphere:** R · **Category:** Regression & GLM

**Signature:** `(y_true: ?, y_pred: ?, n_groups: ?) → ?`

## What it does

hosmer_lemeshow_lite.R
Hosmer-Lemeshow calibration test for logistic regression.
_lite: manual decile table without correction for ties.
Claim: well-calibrated model passes; badly calibrated model fails.
Tolerance: HL statistic exact match; goodness-of-fit p-values match.

## Guarantee

When it runs, hosmer lemeshow lite guarantees hl_good$p_val > 0.05; hl_bad$p_val < 0.05; hl_bad$chi_sq > hl_good$chi_sq (weak-grade: directional, proven by run).

**Checkable constraints:**

- `hl_good$p_val > 0.05`
- `hl_bad$p_val < 0.05`
- `hl_bad$chi_sq > hl_good$chi_sq`
- `hl_good$chi_sq >= 0`
- `hl_bad$chi_sq >= 0`
- `hl_good$p_val >= 0 & hl_good$p_val <= 1`
- `hl_bad$p_val >= 0 & hl_bad$p_val <= 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `hl_test <- function(y_true, y_pred, n_groups = 10)`
**Valid input:** Binary response vector `y_true` in `{0, 1}` of length `n`; predicted probability vector `y_pred` in `[0, 1]` of the same length; integer `n_groups` (default 10) such that `n_groups %/% 2 > 0`.
**Core:** Groups observations by sorted predicted-probability deciles, computes observed and expected event counts per group, and forms the Hosmer-Lemeshow chi-square statistic with `df = n_groups - 2`.
**Assert:** A well-specified logistic model has HL p-value `> 0.05`; an underspecified model has p-value `< 0.05`; the badly-calibrated model has a larger chi-square statistic than the well-calibrated one.
**⚠️ Defect:** Uses quantile-based grouping without tie handling, so tied probabilities may be split across deciles. Adds `1e-10` to expected counts to avoid division by zero rather than validating expected counts. No validation that `y_true` is binary or that `y_pred` is in `[0, 1]`. `n_groups` default is hardcoded; changing it requires source edit at the call site.

---
*△ AURA Pattern Library — © Reality Optimizer*
