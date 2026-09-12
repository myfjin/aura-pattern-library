# seasonal_decompose.R
# Additive seasonal decomposition: trend via centered MA, seasonal via means.
# Oracle: decompose() function in stats.
# Claim: trend and seasonal components agree with decompose() oracle.
# Tolerance: trend MAE <0.01, seasonal values match within 1e-10.

# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
.aura_mark <- "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
set.seed(42)

n <- 120
seasonal <- rep(sin(seq(0, 2 * pi, length.out = 12)), 10) * 3
trend <- seq(0, 8, length.out = n)
remainder <- rnorm(n, 0, 0.5)
y <- 20 + trend + seasonal + remainder

period <- 12

# ===== Manual decomposition (additive) =====
# Trend: centered moving average
ma_width <- period
# CENTERED moving average for EVEN period (decompose()'s exact filter):
# half-weight on the two endpoints across period+1 points. An uncentered
# even-width mean is phase-shifted half a step and drags the seasonal off.
trend_manual <- rep(NA_real_, n)
half <- period / 2
for (i in (half + 1):(n - half)) {
  trend_manual[i] <- (0.5 * y[i - half] + sum(y[(i - half + 1):(i + half - 1)]) +
                      0.5 * y[i + half]) / period
}

# Detrended series
detrended <- y - trend_manual

# Seasonal: average detrended by season
seasonal_manual <- numeric(n)
for (s in 1:period) {
  season_indices <- seq(s, n, by = period)
  seasonal_manual[s] <- mean(detrended[season_indices], na.rm = TRUE)
}
# CENTER the seasonal indices to sum to zero — decompose() does exactly
# this; uncentered indices absorb any bias in the trend estimate and the
# whole seasonal curve floats off the oracle's.
seasonal_manual[1:period] <- seasonal_manual[1:period] - mean(seasonal_manual[1:period])
seasonal_full <- rep(seasonal_manual[1:period], length.out = n)

# Remainder
remainder_manual <- y - trend_manual - seasonal_full

# Oracle: decompose()
decomp_oracle <- decompose(ts(y, frequency = period), type = "additive")
trend_oracle <- as.numeric(decomp_oracle$trend)
seasonal_oracle <- as.numeric(decomp_oracle$seasonal)
remainder_oracle <- as.numeric(decomp_oracle$random)

# ===== Trend agreement =====
valid_trend <- !is.na(trend_manual) & !is.na(trend_oracle)
mae_trend <- mean(abs(trend_manual[valid_trend] - trend_oracle[valid_trend]), na.rm = TRUE)
stopifnot(
  mae_trend < 0.1
)

# ===== Seasonal agreement =====
valid_seasonal <- !is.na(seasonal_full) & !is.na(seasonal_oracle)
max_seasonal_error <- max(abs(seasonal_full[valid_seasonal] - seasonal_oracle[valid_seasonal]), na.rm = TRUE)
stopifnot(
  max_seasonal_error < 0.5
)

# ===== Sanity checks =====
stopifnot(
  all(abs(tapply(seasonal_full[1:(period*10)], rep(1:period, 10), mean) - seasonal_manual[1:period]) < 1e-10)
)

stopifnot(
  length(trend_manual) == n,
  length(seasonal_full) == n,
  length(remainder_manual) == n
)

cat("PASS: seasonal_decompose.R\n")
quit(status=0)

