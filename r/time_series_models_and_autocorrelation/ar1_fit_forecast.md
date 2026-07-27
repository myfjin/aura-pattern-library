# ar1 fit forecast

**Language:** R · **Sphere:** R · **Category:** Time Series — Models & Autocorrelation

## What it does

ar1_fit_forecast.R
AR(1) model fit via conditional least squares and one-step forecast.
Oracle: arima(order=c(1,0,0)) from stats.
Claim: estimated coefficient close to oracle; one-step forecast beats mean on AR data.
Tolerance: coefficient rel error <5%, forecast RMSE ratio <0.95.

## Guarantee

When it runs, ar1 fit forecast guarantees rel_error_phi < 0.1; rmse_ar1 < rmse_mean; abs(phi_cls) <= 1 (proven by run).

**Checkable constraints:**

- `rel_error_phi < 0.1`
- `rmse_ar1 < rmse_mean`
- `abs(phi_cls) <= 1`
- `!is.nan(phi_cls)`
- `!is.nan(forecast_ar1)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; AR(1) sim φ=0.7, n=200.
**Core:** Fits AR(1) by OLS (regress y_t on y_{t−1} with intercept via normal equations), checks φ against `arima(order=c(1,0,0))`, then 1-step-ahead forecasts vs a mean baseline on a 50-point test window.
**Assert:** relative φ error < 0.1; forecast comparison over the test window.
**⚠️ Defect:** The OLS AR(1) estimator is **downward-biased** in finite samples (Hurwicz bias ≈ −(1+3φ)/n) — the 0.1 tolerance absorbs it, but it's not a small-sample-correct estimator. Uses `solve(XtX, Xty)` (normal equations) rather than a stable QR. Forecast horizon and window are hard-coded.

---
*△ AURA Pattern Library — © Reality Optimizer*
