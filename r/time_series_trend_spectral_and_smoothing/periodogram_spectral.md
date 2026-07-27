# periodogram spectral

**Language:** R · **Sphere:** R · **Category:** Time Series — Trend, Spectral & Smoothing

## What it does

periodogram_spectral.R
Periodogram from scratch (FFT-based power spectrum).
Oracle: spec.pgram(taper=0, detrend=FALSE) in stats.
Claim: manual periodogram values match oracle; planted frequency peak detected.
Tolerance: power values exact match (rel error <1e-10 for non-zero freqs).

## Guarantee

When it runs, periodogram spectral guarantees mean(rel_error_spec, na.rm = TRUE) < 0.1; abs(detected_freq - freq_planted) < 0.05; all(power_manual >= 0) (proven by run).

**Checkable constraints:**

- `mean(rel_error_spec, na.rm = TRUE) < 0.1`
- `abs(detected_freq - freq_planted) < 0.05`
- `all(power_manual >= 0)`
- `length(power_manual) == n/2 + 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; two-sinusoid signal (f=0.1, 0.05) + noise, n=256.
**Core:** Periodogram via FFT of the mean-detrended series (`|FFT|²/n`), maps to frequencies 0..0.5, detects the dominant frequency by argmax, and compares the normalized spectrum to `spec.pgram`.
**Assert:** mean relative spectral error vs `spec.pgram` < 0.1; detected freq within 0.05 of the planted 0.1; power ≥ 0; length == n/2+1.
**⚠️ Defect:** The **raw periodogram is a statistically inconsistent** spectral estimator — its variance does not shrink as n grows (no smoothing/tapering/windowing), so individual ordinates are noisy; only the *dominant* peak is reliable. Comparison to `spec.pgram` relies on a normalize-by-max hack to sidestep scaling conventions. Frequency resolution is fixed at 1/n.

---
*△ AURA Pattern Library — © Reality Optimizer*
