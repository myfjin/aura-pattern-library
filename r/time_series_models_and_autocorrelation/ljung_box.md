# ljung box

**Language:** R · **Sphere:** R · **Category:** Time Series — Models & Autocorrelation

## What it does

ljung_box.R
Ljung-Box Q statistic for autocorrelation significance.
Oracle: Box.test(type="Ljung-Box") in stats.
Claim: manual Q statistic matches oracle; AR residuals pass, raw AR series fails.
Tolerance: Q statistic exact match (rel error <1e-10), p-value agreement <1e-4.

## Guarantee

When it runs, ljung box guarantees rel_error_q < 1e-10; p_resid > 0.05; p_raw < 0.05 (proven by run).

**Checkable constraints:**

- `rel_error_q < 1e-10`
- `p_resid > 0.05`
- `p_raw < 0.05`
- `all(!is.nan(acf_manual))`
- `Q_manual > 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; AR(1) sim φ=0.8, n=150, h=10 lags.
**Core:** Ljung-Box portmanteau statistic `Q = n(n+2)·Σ ρ_k²/(n−k)` computed from a manual ACF, verified against `Box.test(type="Ljung-Box")`; then confirms AR(1) residuals are white (p>0.05).
**Assert:** relative Q error < 1e-10; residual Box test p > 0.05.
**⚠️ Defect:** Recomputes `mean(y)` inside the ACF loop each lag (minor waste) and uses the biased ACF. Fixed h=10 — the test's power depends heavily on this undisclosed lag choice. The residual-whiteness assert assumes the AR(1) fit is correct, so it's a joint (fit + test) check rather than an isolated Ljung-Box unit.

---
*△ AURA Pattern Library — © Reality Optimizer*
