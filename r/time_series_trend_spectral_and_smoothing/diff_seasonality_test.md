# diff seasonality test

**Language:** R · **Sphere:** R · **Category:** Time Series — Trend, Spectral & Smoothing

**Signature:** `(x: ?, max_lag: ?) → ?`

## What it does

diff_seasonality_test.R
Seasonal differencing removes seasonality (ACF-based test).
Claim: seasonal-lag autocorrelation high before differencing, near zero after.
Tolerance: ACF @ lag=period high (>0.5) before, low (<0.2) after.

## Guarantee

When it runs, diff seasonality test guarantees acf_at_period_diff < 0.2; mean(rel_error_orig, na.rm = TRUE) < 0.05; all(acf_diff >= -1 & acf_diff <= 1) (proven by run).

**Checkable constraints:**

- `acf_at_period_orig > 0.5`
- `acf_at_period_diff < 0.2`
- `mean(rel_error_orig, na.rm = TRUE) < 0.05`
- `all(acf_original >= -1 & acf_original <= 1)`
- `all(acf_diff >= -1 & acf_diff <= 1)`
- `length(y_diff) == n - period`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** helper `compute_acf(x, max_lag)`; pattern runs as a script.
**Valid input:** No params; strongly seasonal series (period 12), n=120.
**Core:** Detects seasonality via the ACF at the seasonal lag, then applies seasonal differencing `y_t − y_{t−period}` and shows the period-lag ACF collapses. Cross-checks ACF against base `acf()`.
**Assert:** original ACF at period > 0.5; differenced ACF at period < 0.2; both match `acf()`.
**⚠️ Defect:** Uses the biased (÷n) ACF. Seasonal differencing shortens the series by one period and can *introduce* negative MA-type autocorrelation (over-differencing) — not checked. Period is assumed known/fixed at 12.

---
*△ AURA Pattern Library — © Reality Optimizer*
