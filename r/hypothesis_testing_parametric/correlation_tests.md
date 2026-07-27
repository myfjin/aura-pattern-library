# correlation tests

**Language:** R · **Sphere:** R · **Category:** Hypothesis Testing — Parametric

## What it does

Correlation Tests (Pearson & Spearman)
Implements both by hand; verifies against cor() and cor.test()
Use when: assessing linear or monotonic association between variables

## Guarantee

When it runs, correlation tests guarantees all.equal(r_pearson, r_pearson_oracle, tolerance = 1e-08); all.equal(r_spearman, r_spearman_oracle, tolerance = 1e-08); all.equal(as.numeric(t_pearson), as.numeric(test_pearson$statistic), tolerance = 1e-08) (proven by run).

**Checkable constraints:**

- `all.equal(r_pearson, r_pearson_oracle, tolerance = 1e-08)`
- `all.equal(r_spearman, r_spearman_oracle, tolerance = 1e-08)`
- `all.equal(as.numeric(t_pearson), as.numeric(test_pearson$statistic), tolerance = 1e-08)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Two numeric vectors `x` and `y` of equal length.
**Core:** Computes Pearson correlation via `cov(x,y)/(sd(x)*sd(y))`, derives the t-statistic and two-tailed p-value, and computes Spearman correlation as the Pearson correlation of ranks. Verifies against `cor()` and `cor.test()`.
**Assert:** Pearson and Spearman coefficients match `cor()` within `1e-8`; the Pearson t-statistic matches `cor.test()` within `1e-8`.
**⚠️ Defect:** No input validation: unequal lengths silently recycle or error later, constant vectors cause division by zero / NaN, and non-numeric inputs raise uncontrolled errors. Spearman uses `cor(rank(x), rank(y))` rather than the exact permutation distribution; tie handling is average ranks but not documented. No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
