# prop test two sample

**Language:** R · **Sphere:** R · **Category:** Hypothesis Testing — Parametric

## What it does

Two-Proportion Z-Test with Pooled Variance
Implements z-statistic for H0: p1=p2; compares to prop.test(correct=FALSE)
Core: pooled proportion p_pool = (x1+x2)/(n1+n2), SE = sqrt(p_pool*(1-p_pool)*(1/n1 + 1/n2)),
z = (p1 - p2) / SE, χ² = z² for comparison to prop.test
Planted: two groups with different proportions (p1=0.4, p2=0.6), clear signal

## Guarantee

When it runs, prop test two sample guarantees all.equal(chi_sq, unname(oracle_result$statistic), tolerance = 1e-06); all.equal(p_value, oracle_result$p.value, tolerance = 1e-06) (proven by run).

**Checkable constraints:**

- `all.equal(chi_sq, unname(oracle_result$statistic), tolerance = 1e-06)`
- `all.equal(p_value, oracle_result$p.value, tolerance = 1e-06)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Counts `x1`, `n1`, `x2`, `n2` with `0 <= x_i <= n_i` and `n_i > 0`. The demo uses `x1=20, n1=50` and `x2=36, n2=60`.
**Core:** Computes pooled proportion, z-statistic, two-tailed p-value, and chi-square `z^2`, then compares to `prop.test(..., correct=FALSE)`.
**Assert:** Chi-square statistic and p-value match the oracle within `1e-6`.
**⚠️ Defect:** No validation that `x_i <= n_i` or that `n_i > 0`; impossible counts silently produce invalid proportions or division by zero. No continuity correction. Hardcoded two-tailed. No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
