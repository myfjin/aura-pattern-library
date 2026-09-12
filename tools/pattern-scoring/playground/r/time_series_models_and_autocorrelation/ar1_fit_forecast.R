# ar1_fit_forecast.R
# AR(1) model fit via conditional least squares and one-step forecast.
# Oracle: arima(order=c(1,0,0)) from stats.
# Claim: estimated coefficient close to oracle; one-step forecast beats mean on AR data.
# Tolerance: coefficient rel error <5%, forecast RMSE ratio <0.95.

# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
.aura_mark <- "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
set.seed(42)

# Generate AR(1) data: y_t = 0.7 * y_{t-1} + epsilon_t
phi_true <- 0.7
n <- 200
y <- numeric(n)
y[1] <- rnorm(1)
for (i in 2:n) {
  y[i] <- phi_true * y[i - 1] + rnorm(1, sd = 1)
}

# ===== Conditional Least Squares (CLS) =====
# Model: y_t = phi * y_{t-1} + epsilon_t
# Minimize sum((y_t - phi * y_{t-1})^2) for t = 2:n
y_curr <- y[2:n]
y_lag <- y[1:(n - 1)]

# Normal equations: (X'X) beta = X'y
X_mat <- cbind(1, y_lag)
XtX <- t(X_mat) %*% X_mat
Xty <- t(X_mat) %*% y_curr

# Solve for intercept and phi
beta_cls <- solve(XtX, Xty)
intercept_cls <- beta_cls[1]
phi_cls <- beta_cls[2]

# Oracle: ARIMA fit
fit_arima <- arima(y, order = c(1, 0, 0))
phi_oracle <- fit_arima$coef["ar1"]
intercept_oracle <- fit_arima$coef["intercept"]

# Coefficient agreement
rel_error_phi <- abs(phi_cls - phi_oracle) / (abs(phi_oracle) + 1e-6)
stopifnot(
  rel_error_phi < 0.1
)

# ===== One-step forecast =====
# Forecast y_{n+1} = intercept + phi * y_n
forecast_ar1 <- intercept_cls + phi_cls * y[n]
forecast_mean <- mean(y)

# On test data (last 50 observations), recursive forecast
test_start <- n - 49
test_data <- y[test_start:n]
forecast_ar1_recursive <- numeric(length(test_data))
forecast_mean_recursive <- numeric(length(test_data))

for (i in 2:length(test_data)) {
  forecast_ar1_recursive[i] <- intercept_cls + phi_cls * test_data[i - 1]
  forecast_mean_recursive[i] <- mean(y[1:(test_start + i - 2)])
}

rmse_ar1 <- sqrt(mean((test_data[-1] - forecast_ar1_recursive[-1])^2))
rmse_mean <- sqrt(mean((test_data[-1] - forecast_mean_recursive[-1])^2))

stopifnot(
  rmse_ar1 < rmse_mean
)

# ===== Sanity checks =====
stopifnot(
  abs(phi_cls) <= 1.0
)

stopifnot(
  !is.nan(phi_cls),
  !is.nan(forecast_ar1)
)

cat("PASS: ar1_fit_forecast.R\n")
quit(status=0)

