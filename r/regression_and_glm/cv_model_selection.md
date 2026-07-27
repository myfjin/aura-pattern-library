# cv model selection

**Language:** R · **Sphere:** R · **Category:** Regression & GLM

## What it does

cv_model_selection.R
k-fold cross-validation for polynomial degree selection.
Claim: CV MSE selects true-degree model over under/over-fit.
Tolerance: true degree has lowest CV MSE with >95% probability.

## Guarantee

When it runs, cv model selection guarantees selected_degree == true_degree; cv_mse[3] < cv_mse[1]; cv_mse[3] < cv_mse[5] (proven by run).

**Checkable constraints:**

- `selected_degree == true_degree`
- `cv_mse[3] < cv_mse[1]`
- `cv_mse[3] < cv_mse[5]`
- `all(cv_mse > 0)`
- `length(cv_mse) == length(degrees_test)`
- `which.min(cv_mse) > 0 && which.min(cv_mse) <= length(degrees_test)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Numeric predictor vector `x` and response vector `y` of equal length, generated from a polynomial of known degree. The demo assumes a degree-3 polynomial and tests degrees 1–5.
**Core:** 5-fold cross-validation for polynomial degree selection. Builds design matrices up to degree 5, fits via normal equations on each fold, and picks the degree with the lowest CV MSE.
**Assert:** `selected_degree == true_degree`; degree-3 CV MSE is lower than degree-1 and degree-5; all CV MSEs are positive; the selected degree index is valid.
**⚠️ Defect:** Hardcoded `k_folds = 5` and test degrees `1:5`. Folds are assigned sequentially, not randomly stratified. Polynomial design matrices are rebuilt fully up to degree 5 and then subset — wasteful and numerically unstable for high degrees. No input validation (length mismatch, non-numeric, all-constant `x`). No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
