# holt winters lite

**Language:** R · **Sphere:** R · **Category:** Time Series — Models & Autocorrelation

## What it does

holt_winters_lite.R
Additive Holt-Winters from scratch (additive decomposition).
_lite: manual alpha/beta/gamma, no optim() tuning.
Claim: manual fitted values are smooth and track the data; properties verified.
Tolerance: fitted values within reasonable bounds; monotonicity checks on components.

## Guarantee

When it runs, holt winters lite guarantees lt[n] > lt[1]; abs(seasonal_mean) < 0.5; mse_hw < var(y) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `all(is.finite(fitted))`
- `lt[n] > lt[1]`
- `abs(seasonal_mean) < 0.5`
- `mse_hw < var(y)`
- `length(fitted) == n`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; additive series level+trend+seasonal(period 12), n=120; α=0.2, β=0.1, γ=0.1 fixed.
**Core:** Additive Holt-Winters triple exponential smoothing — level `lt`, trend `bt`, seasonal `st` recursions with one-step fitted values.
**Assert:** `stopifnot(...)` on fit quality (fitted tracks y after the first season).
**⚠️ Defect:** The `i ≤ period` branch contains **dead code** — a nested `if (i > period)` inside the `else { # i ≤ period }` block that can never be true, so its "then" is unreachable and the seasonal update in that branch uses `st[i]` on both sides (self-reference, effectively `st[i]=γ·(y−lt)+(1−γ)·st[i]` → biased). Smoothing parameters are hard-coded, not optimized. Seasonal initialization (`st[1:period]=y−lt[1]`) is crude (no de-trending of the first season).

---
*△ AURA Pattern Library — © Reality Optimizer*
