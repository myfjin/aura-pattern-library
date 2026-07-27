# km survival lite

**Language:** R · **Sphere:** R · **Category:** Multivariate & Applied Modeling

## What it does

km_survival_lite.R
Kaplan-Meier survival curve with censoring (no oracle: hand-verify properties).
_lite: manual implementation without optimizing for speed.
Claim: stepwise non-increasing survival curve; starts at 1; censoring handled correctly.
Tolerance: properties verified exactly; no tolerance (categorical properties).

## Guarantee

When it runs, km survival lite guarantees all(diffs <= 1e-10); all(n_risk_diffs <= 0); total_events == expected_events (proven by run).

**Checkable constraints:**

- `!is.na(km_table$survival[1])`
- `all(diffs <= 1e-10)`
- `all(km_table$survival >= 0 & km_table$survival <= 1)`
- `all(n_risk_diffs <= 0)`
- `all(km_table$se >= 0)`
- `total_events == expected_events`
- `abs(first_row$survival - expected_survival) < 1e-10`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; n=100, survival ~ Exp(0.02), censoring ~ Exp(0.01), fixed seed.
**Core:** Kaplan-Meier product-limit survival estimator from right-censored data: at each event time computes n-at-risk, n-events, `S_i = S_{i-1}·(1 − d/n)`, and Greenwood standard error with a *separate* running sum (comments note this fixes two prior bugs: compounding the S² factor, and the infinite term when n==d).
**Assert:** `stopifnot(...)` on the KM table (survival monotone-decreasing in [0,1], Greenwood SE finite).
**⚠️ Defect:** O(#event-times × n) double loop (recomputes at-risk set each step) — slow for large n. Ties are handled only by exact `time == t` equality (floating survival times rarely tie). Greenwood SE is undefined once S reaches 0 (last event) — handled by skipping the term, but the final SE understates uncertainty there.

---
*△ AURA Pattern Library — © Reality Optimizer*
