# ACF and PACF from Scratch: Durbin-Levinson algorithm for partial autocorrelation
# Implements ACF directly and PACF via Durbin-Levinson recursion; verifies against acf()/pacf()
# Core: ACF = γ_k / γ_0; PACF φ_{k,k} solved iteratively from Durbin-Levinson equations
# Planted: AR(2) process with known structure, compute lags 1-10

# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
.aura_mark <- "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
set.seed(42)
y <- arima.sim(list(ar=c(0.6, -0.2)), n=150)

# Sample mean and centered data
y_centered <- y - mean(y)
n <- length(y_centered)

# Autocovariance (lags 0-10)
max_lag <- 10
gamma <- sapply(0:max_lag, function(k) {
  if (k == 0) return(sum(y_centered^2) / n)
  else return(sum(y_centered[1:(n-k)] * y_centered[(k+1):n]) / n)
})

# ACF
acf_est <- gamma / gamma[1]

# Oracle ACF
acf_oracle <- acf(y, lag.max=max_lag, plot=FALSE)$acf[1:(max_lag+1)]
stopifnot(all.equal(acf_est, acf_oracle, tolerance=1e-6))

# PACF via Durbin-Levinson (use ACF ρ, not autocovariance γ)
rho <- acf_est  # ACF
pacf_est <- rep(0, max_lag)
phi <- matrix(0, nrow=max_lag, ncol=max_lag)  # φ_{k,j} storage

for (k in 1:max_lag) {
  if (k == 1) {
    pacf_est[k] <- rho[2]  # ρ_1
    phi[k, k] <- pacf_est[k]
  } else {
    # φ_{k,k} = (ρ_k - Σ_{j=1}^{k-1} φ_{k-1,j} * ρ_{k-j}) / (1 - Σ_{j=1}^{k-1} φ_{k-1,j} * ρ_j)
    numerator <- rho[k+1] - sum(phi[k-1, 1:(k-1)] * rho[k:2])
    denominator <- 1 - sum(phi[k-1, 1:(k-1)] * rho[2:k])
    pacf_est[k] <- numerator / denominator
    phi[k, k] <- pacf_est[k]
    # Update other φ_{k,j} for next iteration
    phi[k, 1:(k-1)] <- phi[k-1, 1:(k-1)] - pacf_est[k] * phi[k-1, (k-1):1]
  }
}

# Oracle PACF
pacf_oracle <- as.vector(pacf(y, lag.max=max_lag, plot=FALSE)$acf)
stopifnot(all.equal(pacf_est, pacf_oracle, tolerance=1e-5))

cat("acf_pacf_from_scratch: ACF lags 1-3 match, PACF lags 1-3 match PASS\n")

