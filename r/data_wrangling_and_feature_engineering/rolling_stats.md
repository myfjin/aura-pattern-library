# rolling stats

**Language:** R · **Sphere:** R · **Category:** Data Wrangling & Feature Engineering

## What it does

Rolling Statistics (Mean & SD)
Implements rolling mean/sd; window results equal brute force
Use when: computing moving averages or smoothing time series

## Guarantee

When it runs, rolling stats guarantees all.equal(rolling_mean, brute_mean, tolerance = 1e-08); all.equal(rolling_sd, brute_sd, tolerance = 1e-08) (proven by run).

**Checkable constraints:**

- `all.equal(rolling_mean, brute_mean, tolerance = 1e-08)`
- `all.equal(rolling_sd, brute_sd, tolerance = 1e-08)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric vector named `x` and a positive integer `window_size` such that `window_size <= length(x)`.
**Core:** Computes rolling mean and rolling sample standard deviation over a fixed window using explicit loops.
**Assert:** Rolling mean and rolling SD match brute-force per-window calculations within tolerance.
**⚠️ Defect:** No input validation: if `window_size > length(x)`, the loop range becomes negative/empty and results are silently empty or invalid. `NA` values in `x` silently propagate through `mean()` and `sd()`, making entire windows `NA` without warning. Edge windows and partial windows are not handled. No function wrapper.

---

## Category: distributions_and_resampling

---
*△ AURA Pattern Library — © Reality Optimizer*
