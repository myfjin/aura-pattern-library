# fisher exact 2x2

**Language:** R · **Sphere:** R · **Category:** Nonparametric & Categorical

**Signature:** `(a_val: ?, m1: ?, m2: ?, n1: ?, N: ?) → ?`

## What it does

Fisher's Exact Test: hypergeometric enumeration for 2x2 contingency tables
Implements one-tailed p-value by enumerating tables with fixed marginals; compares to fisher.test()
Core: given a 2x2 table with marginals (m1,m2,n1,n2), enumerate all valid a values,
compute hypergeometric probability for each, sum tail probability
Planted: association between rows/cols with planted extreme cell value

## Guarantee

When it runs, fisher exact 2x2 guarantees all.equal(p_one_tail, oracle_result$p.value, tolerance = 1e-06) (proven by run).

**Checkable constraints:**

- `all.equal(p_one_tail, oracle_result$p.value, tolerance = 1e-06)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `hypergeo_prob <- function(a_val, m1, m2, n1, N)`
**Valid input:** Integer hypergeometric parameters satisfying `0 <= a_val <= min(m1, n1)`, `n1 - a_val <= m2`, and `N = m1 + m2 = n1 + n2`. The top-level demo uses a `2x2` table with cell `a = 12`, marginals `m1=15, m2=19, n1=16, n2=18, N=34`.
**Core:** Computes the log-scale hypergeometric probability mass for a candidate top-left cell, enumerates all valid cell values, and sums the one-tailed tail probability `P(A >= a_obs)`. Verifies against `fisher.test(..., alternative="greater")`.
**Assert:** `p_one_tail` matches the oracle p-value within `1e-6`.
**⚠️ Defect:** `hypergeo_prob` only computes a single probability mass; it does not perform the full Fisher exact test, check table dimensions, or return a two-tailed p-value. No parameter validation. The overall test logic is a top-level script, so the table and alternative are hardcoded and not reusable as a function.

---
*△ AURA Pattern Library — © Reality Optimizer*
