# Fable R Batch — time_series_trend_spectral_and_smoothing Detail Docs (6 patterns)

Categories: `time_series_trend_spectral_and_smoothing` (6). Documented directly by Fable (mesh offline); verified against source.

## Category: time_series_trend_spectral_and_smoothing

### 1. diff_seasonality_test.R
**Entry fn:** helper `compute_acf(x, max_lag)`; pattern runs as a script.
**Valid input:** No params; strongly seasonal series (period 12), n=120.
**Core:** Detects seasonality via the ACF at the seasonal lag, then applies seasonal differencing `y_t − y_{t−period}` and shows the period-lag ACF collapses. Cross-checks ACF against base `acf()`.
**Assert:** original ACF at period > 0.5; differenced ACF at period < 0.2; both match `acf()`.
**⚠️ Defect:** Uses the biased (÷n) ACF. Seasonal differencing shortens the series by one period and can *introduce* negative MA-type autocorrelation (over-differencing) — not checked. Period is assumed known/fixed at 12.

### 2. hampel_ts_outliers.R
**Entry fn:** `hampel_outliers(x, win = 7, threshold = 3.5)` → `list(flags, median, mad)`.
**Valid input:** `x` numeric series; `win` positive half-window; `threshold` positive. In-script: n=150 with 3 planted spikes of +15.
**Core:** Hampel filter for outlier flagging: within a sliding ±win window, compute the median and normalized MAD (`1.4826·median|x−med|`), flag point i if `|x_i − med_i|/MAD_i > threshold`.
**Assert:** flags the 3 planted outliers on the dirty series; ~no flags on the clean series.
**⚠️ Defect:** Windows are **truncated (asymmetric) at the series ends** (`max(1,i−win):min(n,i+win)`), so edge points get a smaller, biased window and reduced robustness. When MAD = 0 (flat window) it can't flag anything (returns FALSE) — outliers in constant stretches are missed. A cluster of adjacent outliers within one window can corrupt the median and mask each other.

### 3. mann_kendall_trend.R
**Entry fn:** `mk_test(time, value)` → `list(S, tau, z, p_value)`.
**Valid input:** `time`, `value` equal-length numeric vectors. In-script: n=30, a trend series and a noise series.
**Core:** Mann-Kendall non-parametric trend test: S = Σ sign(t_j−t_i)·sign(v_j−v_i) over all pairs, variance `n(n−1)(2n+5)/18`, continuity-corrected Z, Kendall's τ. Verified against `cor.test(method="kendall")`.
**Assert:** trend series p<0.05, noise series p>0.05; τ and p match `cor.test` (tol 1e-6 / 1e-5).
**⚠️ Defect:** O(n²) double loop over all pairs (slow for long series). The variance formula uses the **no-ties** form — with tied values it overstates precision (no tie-correction term), so p-values are wrong for discrete/rounded data. n=30 is small for the normal approximation.

### 4. periodogram_spectral.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; two-sinusoid signal (f=0.1, 0.05) + noise, n=256.
**Core:** Periodogram via FFT of the mean-detrended series (`|FFT|²/n`), maps to frequencies 0..0.5, detects the dominant frequency by argmax, and compares the normalized spectrum to `spec.pgram`.
**Assert:** mean relative spectral error vs `spec.pgram` < 0.1; detected freq within 0.05 of the planted 0.1; power ≥ 0; length == n/2+1.
**⚠️ Defect:** The **raw periodogram is a statistically inconsistent** spectral estimator — its variance does not shrink as n grows (no smoothing/tapering/windowing), so individual ordinates are noisy; only the *dominant* peak is reliable. Comparison to `spec.pgram` relies on a normalize-by-max hack to sidestep scaling conventions. Frequency resolution is fixed at 1/n.

### 5. rolling_origin_cv.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; seasonal(period 4)+trend+noise, n=144, initial train 50.
**Core:** Rolling-origin (expanding-window) 1-step cross-validation: at each origin refit/forecast with three methods — seasonal-naïve (value one period back), historical mean, and a linear-trend `lm` extrapolation — accumulating per-origin MAE.
**Assert:** MAE arrays per method (the trend/seasonal-naïve methods beat the mean on this trended-seasonal series).
**⚠️ Defect:** **Refits `lm` from scratch every origin** (O(n²) total) instead of updating — expensive on long series. Only 1-step-ahead is evaluated (no multi-horizon). The linear-trend forecast ignores the seasonal component entirely, so it's a deliberately weak baseline. Early origins (`test_idx ≤ period`) fall back to the mean, mixing methods.

### 6. sma_wma_filter.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; random-walk-with-drift series, n=100, window=5.
**Core:** Simple moving average and linearly-weighted moving average (weights 1:window/Σ), each computed by a trailing-window loop and cross-verified against base `filter(sides=1)` and `weighted.mean`.
**Assert:** SMA matches `filter()` (max diff < 1e-10); weights sum to 1; WMA matches `weighted.mean` (< 1e-10).
**⚠️ Defect:** The leading `window−1` positions are left as **0** in `sma_manual`/`wma_manual` (loop starts at `window`), whereas `filter()` yields NA there — a silent 0-vs-NA inconsistency masked by comparing only the valid tail. Trailing (causal) window only — introduces a lag of ~(window−1)/2 vs a centered MA. Loop-based (slow) rather than vectorized/`filter`-based.
