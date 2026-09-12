# Batch 4 — R Pattern Detail Docs (8 patterns): `regression_and_glm`

Third batch of the R data-science sphere.

**R-sphere note:** most patterns are top-level scripts. Where the source defines an Entry function, its signature is copied verbatim from `SIGNATURES_REFERENCE_R.md`; otherwise the Entry field records `top-level script` and the Valid-input contract describes the expected top-level variables. Defects are sourced from the actual source.

---

## Category: regression_and_glm

### 1. bootstrap_regression.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Numeric predictor vector `x` and response vector `y` of equal length; a scalar `true_slope` for the coverage assertion.
**Core:** Resamples `(x, y)` cases with replacement `n_boot` times, fits `lm(y_boot ~ x_boot)` each time, and records the slope. Returns the percentile 95% CI and demonstrates CI width reduction with `n = 200` versus `n = 50`.
**Assert:** The planted `true_slope` lies within the 95% CI; the larger-sample CI width is strictly smaller than the smaller-sample width; all bootstrap slopes are non-`NA`; the bootstrap slope mean is within 0.5 of `true_slope`.
**⚠️ Defect:** Hardcoded `n_boot = 1000` and `alpha = 0.05`. Uses only the percentile method — no BCa or bias correction. `NA` values in `x`/`y` silently propagate through `lm()`. No input validation (length mismatch, constant vectors, empty inputs). No function wrapper.

### 2. cv_model_selection.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Numeric predictor vector `x` and response vector `y` of equal length, generated from a polynomial of known degree. The demo assumes a degree-3 polynomial and tests degrees 1–5.
**Core:** 5-fold cross-validation for polynomial degree selection. Builds design matrices up to degree 5, fits via normal equations on each fold, and picks the degree with the lowest CV MSE.
**Assert:** `selected_degree == true_degree`; degree-3 CV MSE is lower than degree-1 and degree-5; all CV MSEs are positive; the selected degree index is valid.
**⚠️ Defect:** Hardcoded `k_folds = 5` and test degrees `1:5`. Folds are assigned sequentially, not randomly stratified. Polynomial design matrices are rebuilt fully up to degree 5 and then subset — wasteful and numerically unstable for high degrees. No input validation (length mismatch, non-numeric, all-constant `x`). No function wrapper.

### 3. hosmer_lemeshow_lite.R
**Entry fn:** `hl_test <- function(y_true, y_pred, n_groups = 10)`
**Valid input:** Binary response vector `y_true` in `{0, 1}` of length `n`; predicted probability vector `y_pred` in `[0, 1]` of the same length; integer `n_groups` (default 10) such that `n_groups %/% 2 > 0`.
**Core:** Groups observations by sorted predicted-probability deciles, computes observed and expected event counts per group, and forms the Hosmer-Lemeshow chi-square statistic with `df = n_groups - 2`.
**Assert:** A well-specified logistic model has HL p-value `> 0.05`; an underspecified model has p-value `< 0.05`; the badly-calibrated model has a larger chi-square statistic than the well-calibrated one.
**⚠️ Defect:** Uses quantile-based grouping without tie handling, so tied probabilities may be split across deciles. Adds `1e-10` to expected counts to avoid division by zero rather than validating expected counts. No validation that `y_true` is binary or that `y_pred` is in `[0, 1]`. `n_groups` default is hardcoded; changing it requires source edit at the call site.

### 4. linear_regression_normal_eq.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Numeric design matrix `X` with an intercept column and one or more predictors, and numeric response vector `y` of length `nrow(X)`. The demo uses `n = 100`, two predictors, and planted coefficients `c(2, 0.5, -0.3)`.
**Core:** Solves the normal equations `β = (XᵀX)⁻¹ Xᵀy` and compares coefficients against `lm()`.
**Assert:** Manual coefficients match `lm()` within `1e-8`.
**⚠️ Defect:** No input validation: singular or rank-deficient `XᵀX` raises an uncontrolled `solve()` error; non-numeric or length-mismatched `X`/`y` produce confusing errors; collinear predictors silently produce numerically unstable coefficients. No function wrapper, so the demo cannot be reused as a function.

### 5. lm_diagnostics.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Numeric predictor vector `x` and response vector `y` of equal length.
**Core:** Computes leverage via the hat matrix, standardized residuals (with internal estimate of `σ`), and Cook's distance by hand. Verifies against `hatvalues()`, `rstandard()`, and `cooks.distance()`.
**Assert:** Manual leverage, standardized residuals, and Cook's distance match the oracles within relative error `1e-10`, `1e-10`, and `1e-9` respectively; all leverages are in `[0, 1]`; all Cook's distances are non-negative; diagnostics vectors have length `n`.
**⚠️ Defect:** The planted-influential-point assertion (`outlier_idx %in% influential_points`) is commented out, so the script does not actually enforce detection of the planted outlier. Builds the full `n × n` hat matrix explicitly — quadratic in memory and slow for large `n`. No input validation (length mismatch, non-numeric, `n < p`). No function wrapper.

### 6. logistic_regression_irls.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Numeric design matrix `X` with an intercept column and one or more predictors, and binary response vector `y` in `{0, 1}` of length `nrow(X)`. The demo uses two predictors.
**Core:** IRLS (Newton-Raphson) loop for logistic regression with logit link: computes linear predictor, fitted probabilities, working weights, and adjusted response; solves the weighted least-squares system until convergence.
**Assert:** Manual coefficients match `glm(..., family = binomial)` within `1e-4`.
**⚠️ Defect:** No input validation: perfect separation can make weights `w` numerically zero and send coefficients to `±Inf`; non-binary `y` runs silently; singular `X` raises uncontrolled errors. Convergence tolerance and max iterations are hardcoded. Does not compute standard errors, deviance, or fitted values. No function wrapper.

### 7. poisson_regression_irls.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Numeric predictor vector `x` and integer/count response vector `y` of equal length.
**Core:** IRLS for Poisson regression with log link using a diagonal weight matrix `W = diag(μ)` and adjusted response `z = η + (y - μ)/μ`.
**Assert:** Manual coefficients match `glm(..., family = poisson)` within `1e-6`.
**⚠️ Defect:** No input validation: zero or negative `y` values still work in the algorithm but are statistically invalid for Poisson; non-numeric inputs raise uncontrolled errors; `x` is coerced to a single-predictor design matrix. Convergence tolerance and max iterations are hardcoded. Does not compute deviance or standard errors. No function wrapper.

### 8. ridge_regression.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Numeric design matrix `X` with an intercept column and one or more predictors, and numeric response vector `y` of length `nrow(X)`. The demo uses three predictors and a lambda sequence `c(0, 0.1, 1, 10, 100)`.
**Core:** Computes ridge coefficients `β = (XᵀX + λI)⁻¹ Xᵀy` for a sequence of lambdas, verifies `λ = 0` matches `lm()`, and checks that the L2 norm of non-intercept coefficients is non-increasing in `λ`.
**Assert:** `λ = 0` coefficients match `lm()` within `1e-6`; `L2` norm of slopes is non-increasing across the lambda sequence.
**⚠️ Defect:** No input validation: singular `XᵀX` even for small `λ` can fail; non-numeric or mismatched `X`/`y` raise uncontrolled errors. The intercept is included in the regularization (`λI` for all columns), which is usually not desired — standard practice either centers/scales data or excludes the intercept from shrinkage. Lambda sequence is hardcoded. No function wrapper.

---

**R-sphere batch 4: 8/8 patterns documented.** Verifier should check source at `/home/au/aura-pattern-library/r/regression_and_glm/` (canonical) or `/tmp/aura-review/aura-pattern-library/r/regression_and_glm/` (review copy). No Rscript on `.8`, so verification is doc-accuracy only: signatures, top-level script vs function, and defect claims vs source.
