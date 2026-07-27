# seasonal decompose

**Language:** R · **Sphere:** R · **Category:** Time Series — Models & Autocorrelation

## What it does

seasonal_decompose.R
Additive seasonal decomposition: trend via centered MA, seasonal via means.
Oracle: decompose() function in stats.
Claim: trend and seasonal components agree with decompose() oracle.
Tolerance: trend MAE <0.01, seasonal values match within 1e-10.

## Guarantee

When it runs, seasonal decompose guarantees all(abs(tapply(seasonal_full[1:(period * 10)], rep(1:period, 10), mean) - seasonal_manual[1:period]) < 1e-10); mae_trend < 0.1; max_seasonal_error < 0.5 (proven by run).

**Checkable constraints:**

- `mae_trend < 0.1`
- `max_seasonal_error < 0.5`
- `all(abs(tapply(seasonal_full[1:(period * 10)], rep(1:period, 10), mean) - seasonal_manual[1:period]) < 1e-10)`
- `length(trend_manual) == n`
- `length(seasonal_full) == n`
- `length(remainder_manual) == n`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; additive series (trend+seasonal period 12+noise), n=120.
**Core:** Classical additive decomposition: centered moving-average trend (period-12, half-weighted endpoints), seasonal component as the mean of detrended values per season (re-centered to sum ~0), remainder = y − trend − seasonal. Verifies trend against `decompose()`.
**Assert:** trend MAE vs `decompose()` < 0.1.
**⚠️ Defect:** The centered moving average leaves **NA at both ends** (half a period each side) — those points get no trend/remainder, silently dropped from the MAE. Only the **trend** is numerically verified against the oracle; the seasonal and remainder components are computed but not asserted against `decompose()`. Assumes the period is known and the series is exactly additive.

---
*△ AURA Pattern Library — © Reality Optimizer*
