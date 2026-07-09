# hosmer_lemeshow_lite.R
# Hosmer-Lemeshow calibration test for logistic regression.
# _lite: manual decile table without correction for ties.
# Claim: well-calibrated model passes; badly calibrated model fails.
# Tolerance: HL statistic exact match; goodness-of-fit p-values match.

# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
.aura_mark <- "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
set.seed(42)

# ===== Well-calibrated model =====
n <- 500
x_good <- rnorm(n)
y_good <- rbinom(n, 1, plogis(-1 + 2 * x_good))  # True logit: -1 + 2x

# Fit logistic model (correctly specified)
fit_good <- glm(y_good ~ x_good, family = binomial(link = "logit"))
pred_good <- fitted(fit_good)

# ===== Badly calibrated model: UNDER-specification =====
# (An over-specified model fit to clean data is still calibrated in-sample —
# the score equations guarantee it. Miscalibration needs a model that CANNOT
# express the truth: the true logit is strongly curved, the model is linear.)
x2_bad <- rnorm(n)
y_bad <- rbinom(n, 1, plogis(0.5 + 1.5 * x2_bad - 2.0 * x2_bad^2))
fit_bad <- glm(y_bad ~ x2_bad, family = binomial(link = "logit"))
pred_bad <- fitted(fit_bad)

# ===== Hosmer-Lemeshow test (manual) =====
hl_test <- function(y_true, y_pred, n_groups = 10) {
  n <- length(y_true)

  # Quantile-based grouping — assignment must go through the INVERSE
  # permutation: obs with the i-th smallest prediction gets the i-th label.
  # (groups[order(...)] permutes the wrong way and scrambles the deciles,
  # which silently destroys the test's power.)
  group_size <- n %/% n_groups
  labels <- rep(1:n_groups, each = group_size)
  if (length(labels) < n) labels <- c(labels, rep(n_groups, n - length(labels)))
  groups <- integer(n)
  groups[order(y_pred)] <- labels

  # Expected and observed by group
  obs_events <- tapply(y_true, groups, sum)
  obs_total <- tapply(y_true, groups, length)
  exp_events <- tapply(y_pred, groups, sum)
  exp_non <- obs_total - exp_events

  # Chi-square statistic
  chi_sq <- sum(
    (obs_events - exp_events)^2 / (exp_events + 1e-10) +
    ((obs_total - obs_events) - exp_non)^2 / (exp_non + 1e-10)
  )

  # p-value (chi-square with n_groups - 2 df)
  p_val <- pchisq(chi_sq, df = n_groups - 2, lower.tail = FALSE)

  list(chi_sq = chi_sq, p_val = p_val)
}

hl_good <- hl_test(y_good, pred_good)
hl_bad <- hl_test(y_bad, pred_bad)

# ===== Interpretation =====
# Good calibration: should pass (p > 0.05)
cat(sprintf("well-calibrated: chi2 %.3f, p %.4f · badly calibrated: chi2 %.3f, p %.4f\n",
            hl_good$chi_sq, hl_good$p_val, hl_bad$chi_sq, hl_bad$p_val))
stopifnot(
  hl_good$p_val > 0.05
)

# Bad calibration: should fail (p < 0.05)
stopifnot(
  hl_bad$p_val < 0.05
)

# Chi-square for bad should be higher
stopifnot(
  hl_bad$chi_sq > hl_good$chi_sq
)

# ===== Sanity checks =====
stopifnot(
  hl_good$chi_sq >= 0,
  hl_bad$chi_sq >= 0
)

stopifnot(
  hl_good$p_val >= 0 & hl_good$p_val <= 1,
  hl_bad$p_val >= 0 & hl_bad$p_val <= 1
)

cat("PASS: hosmer_lemeshow_lite.R\n")
quit(status=0)

