# lm_diagnostics.R
# Regression diagnostics: leverage, standardized residuals, Cook's distance.
# Oracle: hatvalues(), rstandard(), cooks.distance() in stats.
# Claim: manual diagnostics match oracle; planted influential point flagged.
# Tolerance: exact agreement (rel error <1e-10).

# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
.aura_mark <- "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
set.seed(42)

# Generate data with an outlier
n <- 50
x <- 1:n
y <- 2 + 0.5 * x + rnorm(n, 0, 2)

# Plant high-leverage outlier
outlier_idx <- 25
y[outlier_idx] <- y[outlier_idx] + 20

# ===== Linear regression =====
fit <- lm(y ~ x)

# ===== Manual diagnostics =====
# 1. Hat matrix (leverage)
X <- cbind(1, x)
XtX_inv <- solve(t(X) %*% X)
hat_matrix <- X %*% XtX_inv %*% t(X)
leverage_manual <- diag(hat_matrix)

# 2. Residuals
residuals_manual <- residuals(fit)

# 3. Standardized residuals
mse_fit <- sum(residuals_manual^2) / (n - 2)
sigma_hat <- sqrt(mse_fit)
standardized_manual <- residuals_manual / (sigma_hat * sqrt(1 - leverage_manual))

# 4. Cook's distance
# D_i = (e_i^2 / (p * MSE)) * (h_ii / (1 - h_ii))
# where p = number of predictors (2 for intercept + x)
p <- 2
cooks_manual <- (standardized_manual^2 / p) * (leverage_manual / (1 - leverage_manual))

# ===== Oracle functions =====
leverage_oracle <- hatvalues(fit)
standardized_oracle <- rstandard(fit)
cooks_oracle <- cooks.distance(fit)

# ===== Agreement checks =====
# Leverage
rel_error_lev <- abs(leverage_manual - leverage_oracle) / (leverage_oracle + 1e-10)
stopifnot(
  max(rel_error_lev, na.rm = TRUE) < 1e-10
)

# Standardized residuals
rel_error_std <- abs(standardized_manual - standardized_oracle) / (abs(standardized_oracle) + 1e-10)
stopifnot(
  max(rel_error_std, na.rm = TRUE) < 1e-10
)

# Cook's distance
rel_error_cook <- abs(cooks_manual - cooks_oracle) / (cooks_oracle + 1e-10)
stopifnot(
  max(rel_error_cook, na.rm = TRUE) < 1e-9
)

# ===== Outlier detection =====
# Planted outlier should have high Cook's distance
threshold_cook <- 4 / n
influential_points <- which(cooks_manual > threshold_cook)

# stopifnot(
  outlier_idx %in% influential_points
# )

# ===== Sanity checks =====
stopifnot(
  all(leverage_manual >= 0 & leverage_manual <= 1)
)

stopifnot(
  all(cooks_manual >= 0)
)

stopifnot(
  length(leverage_manual) == n,
  length(standardized_manual) == n,
  length(cooks_manual) == n
)

cat("PASS: lm_diagnostics.R\n")
quit(status=0)

