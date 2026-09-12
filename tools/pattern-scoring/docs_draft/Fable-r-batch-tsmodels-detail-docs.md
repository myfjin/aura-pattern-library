# Fable R Batch — time_series_models_and_autocorrelation Detail Docs (7 patterns)

Categories: `time_series_models_and_autocorrelation` (7). Documented directly by Fable (mesh offline); verified against source.

## Category: time_series_models_and_autocorrelation

### 1. acf_pacf_from_scratch.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; y = AR(2) sim (φ=0.6,−0.2), n=150, max_lag=10.
**Core:** Autocovariance γ_k, ACF ρ_k = γ_k/γ_0, and PACF via the Durbin-Levinson recursion (`φ_{k,k}` and the reflected `φ_{k,1:(k-1)}` update). Verifies against base `acf()` / `pacf()`.
**Assert:** `all.equal(acf_est, acf oracle, 1e-6)`; `all.equal(pacf_est, pacf oracle, 1e-5)`.
**⚠️ Defect:** Uses the **biased** autocovariance estimator (divides by `n`, not `n−k`) — this deliberately matches R's `acf()` default, but is biased low at large lags. Durbin-Levinson can be numerically unstable near a unit root. `max_lag` fixed; not a reusable function.

### 2. ar1_fit_forecast.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; AR(1) sim φ=0.7, n=200.
**Core:** Fits AR(1) by OLS (regress y_t on y_{t−1} with intercept via normal equations), checks φ against `arima(order=c(1,0,0))`, then 1-step-ahead forecasts vs a mean baseline on a 50-point test window.
**Assert:** relative φ error < 0.1; forecast comparison over the test window.
**⚠️ Defect:** The OLS AR(1) estimator is **downward-biased** in finite samples (Hurwicz bias ≈ −(1+3φ)/n) — the 0.1 tolerance absorbs it, but it's not a small-sample-correct estimator. Uses `solve(XtX, Xty)` (normal equations) rather than a stable QR. Forecast horizon and window are hard-coded.

### 3. ar_yule_walker.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; AR(2) sim φ=(0.7,−0.3), n=200, order p=2.
**Core:** Estimates AR(2) coefficients via the Yule-Walker equations: builds the Toeplitz autocovariance matrix R and solves `R·φ = γ`. Verifies against `ar(method="yw")`.
**Assert:** `all.equal(φ_yw, ar()$ar, 1e-3)`; recovered order == p.
**⚠️ Defect:** Yule-Walker estimates are **biased toward stationarity** (shrink coefficients) in small samples. Order p=2 is fixed — the script assumes the true order, so it can't detect over/under-fitting. Uses the biased ACF (matching `ar`'s default).

### 4. ccf_lag_detection.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; y = x delayed by lag=5 + noise, n=100, max_lag=20.
**Core:** Cross-correlation function over lags −20..20 (normalized by n·s_x·s_y), verified against base `ccf()`; detects the lead/lag by the argmax and checks it matches the planted lag.
**Assert:** manual vs `ccf()` max abs diff < 1e-10; detected lag within ±2 of truth; all CCF values in [−1,1]; length == 2·max_lag+1.
**⚠️ Defect:** Uses the biased (divide-by-n) normalization, so CCF magnitudes shrink at large lags. Lag detection is a single argmax — noisy series with multiple correlated lags could pick a spurious peak; the ±2 tolerance hides this. n=100 is small.

### 5. holt_winters_lite.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; additive series level+trend+seasonal(period 12), n=120; α=0.2, β=0.1, γ=0.1 fixed.
**Core:** Additive Holt-Winters triple exponential smoothing — level `lt`, trend `bt`, seasonal `st` recursions with one-step fitted values.
**Assert:** `stopifnot(...)` on fit quality (fitted tracks y after the first season).
**⚠️ Defect:** The `i ≤ period` branch contains **dead code** — a nested `if (i > period)` inside the `else { # i ≤ period }` block that can never be true, so its "then" is unreachable and the seasonal update in that branch uses `st[i]` on both sides (self-reference, effectively `st[i]=γ·(y−lt)+(1−γ)·st[i]` → biased). Smoothing parameters are hard-coded, not optimized. Seasonal initialization (`st[1:period]=y−lt[1]`) is crude (no de-trending of the first season).

### 6. ljung_box.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; AR(1) sim φ=0.8, n=150, h=10 lags.
**Core:** Ljung-Box portmanteau statistic `Q = n(n+2)·Σ ρ_k²/(n−k)` computed from a manual ACF, verified against `Box.test(type="Ljung-Box")`; then confirms AR(1) residuals are white (p>0.05).
**Assert:** relative Q error < 1e-10; residual Box test p > 0.05.
**⚠️ Defect:** Recomputes `mean(y)` inside the ACF loop each lag (minor waste) and uses the biased ACF. Fixed h=10 — the test's power depends heavily on this undisclosed lag choice. The residual-whiteness assert assumes the AR(1) fit is correct, so it's a joint (fit + test) check rather than an isolated Ljung-Box unit.

### 7. seasonal_decompose.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; additive series (trend+seasonal period 12+noise), n=120.
**Core:** Classical additive decomposition: centered moving-average trend (period-12, half-weighted endpoints), seasonal component as the mean of detrended values per season (re-centered to sum ~0), remainder = y − trend − seasonal. Verifies trend against `decompose()`.
**Assert:** trend MAE vs `decompose()` < 0.1.
**⚠️ Defect:** The centered moving average leaves **NA at both ends** (half a period each side) — those points get no trend/remainder, silently dropped from the MAE. Only the **trend** is numerically verified against the oracle; the seasonal and remainder components are computed but not asserted against `decompose()`. Assumes the period is known and the series is exactly additive.
