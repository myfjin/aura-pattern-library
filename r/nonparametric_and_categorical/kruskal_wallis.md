# kruskal wallis

**Language:** R · **Sphere:** R · **Category:** Nonparametric & Categorical

## What it does

Kruskal-Wallis Test: H statistic from ranks (k≥3 groups)
Implements rank-based ANOVA; compares to kruskal.test() H statistic + p-value
Core: rank all observations, compute group rank sums Ri, form H = 12/(N(N+1)) * sum(Ri²/ni) - 3(N+1)
Planted: 3 groups with clear stochastic ordering; H significant under H1

## Guarantee

When it runs, kruskal wallis guarantees all.equal(H, unname(oracle_result$statistic), tolerance = 1e-06); all.equal(p_approx, oracle_result$p.value, tolerance = 1e-05) (proven by run).

**Checkable constraints:**

- `all.equal(H, unname(oracle_result$statistic), tolerance = 1e-06)`
- `all.equal(p_approx, oracle_result$p.value, tolerance = 1e-05)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A list of numeric vectors `groups` (the demo uses three groups named `group1`, `group2`, `group3`). All groups must be non-empty and numeric.
**Core:** Ranks all observations across groups, computes group rank sums, forms the H statistic `12/(N(N+1)) * sum(Ri^2/ni) - 3(N+1)`, and derives a chi-square p-value. Verifies against `kruskal.test()`.
**Assert:** H statistic and p-value match `kruskal.test()` within `1e-6` and `1e-5` respectively.
**⚠️ Defect:** Manual rank-sum extraction is hardcoded to three groups (`idx1`, `idx2`, `idx3`), so a different number of groups would require rewriting the script. No tie correction. No input validation (empty groups, non-numeric values). No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
