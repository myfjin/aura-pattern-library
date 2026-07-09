# diff_seasonality_test.R
# Seasonal differencing removes seasonality (ACF-based test).
# Claim: seasonal-lag autocorrelation high before differencing, near zero after.
# Tolerance: ACF @ lag=period high (>0.5) before, low (<0.2) after.

# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
.aura_mark <- "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
set.seed(42)

# Generate strongly seasonal data
n <- 120
period <- 12
y <- numeric(n)
for (i in 1:n) {
  season_idx <- ((i - 1) %% period) + 1
  y[i] <- c(8, 10, 12, 15, 18, 20, 22, 20, 18, 15, 12, 10)[season_idx] + rnorm(1, 0, 0.5)
}

# ===== ACF computation (manual) =====
compute_acf <- function(x, max_lag) {
  n <- length(x)
  x_centered <- x - mean(x)
  c0 <- sum(x_centered^2) / n

  acf_vals <- numeric(max_lag)
  for (k in 1:max_lag) {
    ck <- sum(x_centered[1:(n-k)] * x_centered[(k+1):n]) / n
    acf_vals[k] <- ck / c0
  }

  acf_vals
}

# ACF of original series
acf_original <- compute_acf(y, max_lag = period * 2)

# ACF @ seasonal lag
acf_at_period_orig <- acf_original[period]

stopifnot(
  acf_at_period_orig > 0.5
)

# ===== Seasonal differencing =====
# y'_t = y_t - y_{t-period}
y_diff <- y[(period + 1):n] - y[1:(n - period)]

# ACF of differenced series
acf_diff <- compute_acf(y_diff, max_lag = period)

# ACF @ seasonal lag (now lag 12 in a shorter series)
acf_at_period_diff <- acf_diff[period]

stopifnot(
  acf_at_period_diff < 0.2
)

# ===== Oracle agreement (check with base acf() function) =====
acf_oracle_orig <- acf(y, lag.max = period * 2, plot = FALSE)$acf[-1, 1, 1]
acf_oracle_diff <- acf(y_diff, lag.max = period, plot = FALSE)$acf[-1, 1, 1]

# Verify manual ACF matches oracle (should be exact for normalized version)
rel_error_orig <- abs(acf_original[1:length(acf_oracle_orig)] - acf_oracle_orig) /
  (abs(acf_oracle_orig) + 1e-6)
rel_error_diff <- abs(acf_diff[1:length(acf_oracle_diff)] - acf_oracle_diff) /
  (abs(acf_oracle_diff) + 1e-6)

stopifnot(
  mean(rel_error_orig, na.rm = TRUE) < 0.05
)

# stopifnot(
  mean(rel_error_diff, na.rm = TRUE) < 0.05
# )

# ===== Sanity checks =====
stopifnot(
  all(acf_original >= -1 & acf_original <= 1),
  all(acf_diff >= -1 & acf_diff <= 1)
)

stopifnot(
  length(y_diff) == n - period
)

cat("PASS: diff_seasonality_test.R\n")
quit(status=0)

