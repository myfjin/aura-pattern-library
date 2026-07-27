# rolling origin cv

**Language:** R · **Sphere:** R · **Category:** Time Series — Trend, Spectral & Smoothing

## What it does

rolling_origin_cv.R
Walk-forward (rolling origin) cross-validation for time series.
Claim: seasonal-naive forecast beats mean forecaster on seasonal data (measured MAE).
Tolerance: seasonal-naive MAE <80% of mean forecaster MAE.

## Guarantee

When it runs, rolling origin cv guarantees mae_sn_avg < mae_m_avg; ratio_sn_to_mean < 0.95; mae_sn_avg > 0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `mae_sn_avg < mae_m_avg`
- `ratio_sn_to_mean < 0.95`
- `all(!is.na(mae_seasonal_naive))`
- `mae_sn_avg > 0`
- `mae_m_avg > 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; seasonal(period 4)+trend+noise, n=144, initial train 50.
**Core:** Rolling-origin (expanding-window) 1-step cross-validation: at each origin refit/forecast with three methods — seasonal-naïve (value one period back), historical mean, and a linear-trend `lm` extrapolation — accumulating per-origin MAE.
**Assert:** MAE arrays per method (the trend/seasonal-naïve methods beat the mean on this trended-seasonal series).
**⚠️ Defect:** **Refits `lm` from scratch every origin** (O(n²) total) instead of updating — expensive on long series. Only 1-step-ahead is evaluated (no multi-horizon). The linear-trend forecast ignores the seasonal component entirely, so it's a deliberately weak baseline. Early origins (`test_idx ≤ period`) fall back to the mean, mixing methods.

---
*△ AURA Pattern Library — © Reality Optimizer*
