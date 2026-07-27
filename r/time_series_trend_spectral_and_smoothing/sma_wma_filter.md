# sma wma filter

**Language:** R · **Sphere:** R · **Category:** Time Series — Trend, Spectral & Smoothing

## What it does

sma_wma_filter.R
Simple Moving Average (SMA) and Weighted Moving Average (WMA) via manual loop.
Oracle: filter() function in base R (for SMA).
Claim: loop-computed SMA/WMA values agree exactly with filter() for SMA
and WMA computes the weighted sum correctly (verified via hand calc).
Tolerance: exact match for SMA (filter output), relative error <1e-10 for WMA logic.

## Guarantee

When it runs, sma wma filter guarantees max_diff < 1e-10; abs(sum(weights) - 1) < 1e-14; max(abs(wma_manual[window:n] - wma_verify[window:n]), na.rm = TRUE) < 1e-10 (proven by run).

**Checkable constraints:**

- `max_diff < 1e-10`
- `abs(sum(weights) - 1) < 1e-14`
- `max(abs(wma_manual[window:n] - wma_verify[window:n]), na.rm = TRUE) < 1e-10`
- `!all(is.na(sma_manual))`
- `length(wma_manual) == length(sma_manual)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; random-walk-with-drift series, n=100, window=5.
**Core:** Simple moving average and linearly-weighted moving average (weights 1:window/Σ), each computed by a trailing-window loop and cross-verified against base `filter(sides=1)` and `weighted.mean`.
**Assert:** SMA matches `filter()` (max diff < 1e-10); weights sum to 1; WMA matches `weighted.mean` (< 1e-10).
**⚠️ Defect:** The leading `window−1` positions are left as **0** in `sma_manual`/`wma_manual` (loop starts at `window`), whereas `filter()` yields NA there — a silent 0-vs-NA inconsistency masked by comparing only the valid tail. Trailing (causal) window only — introduces a lag of ~(window−1)/2 vs a centered MA. Loop-based (slow) rather than vectorized/`filter`-based.

---
*△ AURA Pattern Library — © Reality Optimizer*
