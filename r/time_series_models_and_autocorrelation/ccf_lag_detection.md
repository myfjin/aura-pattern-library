# ccf lag detection

**Language:** R · **Sphere:** R · **Category:** Time Series — Models & Autocorrelation

## What it does

ccf_lag_detection.R
Cross-correlation function from scratch.
Oracle: ccf() function in stats.
Claim: manual CCF values match ccf() oracle exactly; planted lag detected as argmax.
Tolerance: CCF values exact match (rel error <1e-10).

## Guarantee

When it runs, ccf lag detection guarantees max(abs(ccf_manual - ccf_oracle_vals), na.rm = TRUE) < 1e-10; abs(detected_lag + lag_true) <= 2; all(ccf_manual >= -1 & ccf_manual <= 1) (proven by run).

**Checkable constraints:**

- `max(abs(ccf_manual - ccf_oracle_vals), na.rm = TRUE) < 1e-10`
- `abs(detected_lag + lag_true) <= 2`
- `all(ccf_manual >= -1 & ccf_manual <= 1)`
- `length(ccf_manual) == 2 * max_lag + 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; y = x delayed by lag=5 + noise, n=100, max_lag=20.
**Core:** Cross-correlation function over lags −20..20 (normalized by n·s_x·s_y), verified against base `ccf()`; detects the lead/lag by the argmax and checks it matches the planted lag.
**Assert:** manual vs `ccf()` max abs diff < 1e-10; detected lag within ±2 of truth; all CCF values in [−1,1]; length == 2·max_lag+1.
**⚠️ Defect:** Uses the biased (divide-by-n) normalization, so CCF magnitudes shrink at large lags. Lag detection is a single argmax — noisy series with multiple correlated lags could pick a spurious peak; the ±2 tolerance hides this. n=100 is small.

---
*△ AURA Pattern Library — © Reality Optimizer*
