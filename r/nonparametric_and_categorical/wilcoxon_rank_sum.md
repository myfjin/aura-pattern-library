# wilcoxon rank sum

**Language:** R · **Sphere:** R · **Category:** Nonparametric & Categorical

## What it does

Wilcoxon Rank-Sum Test: U statistic + normal approximation p-value from scratch
Implements Mann-Whitney U via rank sums; compares to wilcox.test(correct=FALSE) p-value
Core: rank observations, sum ranks per group, compute U, apply normal approx (z-score from mean/sd)
Planted: two skewed groups (exponential + offset) with definite separation; oracle U-statistic expected

## Guarantee

When it runs, wilcoxon rank sum guarantees all.equal(U, n1 * n2 - U_alt); all.equal(p_approx, oracle$p.value, tolerance = 1e-06); all.equal(W, unname(oracle$statistic), tolerance = 1e-06) (proven by run).

**Checkable constraints:**

- `all.equal(U, n1 * n2 - U_alt)`
- `all.equal(p_approx, oracle$p.value, tolerance = 1e-06)`
- `all.equal(W, unname(oracle$statistic), tolerance = 1e-06)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Two numeric vectors `x` and `y` representing independent samples. The demo uses `x <- rexp(12,1)` and `y <- rexp(10,1) + 2.5`.
**Core:** Ranks the combined sample, computes group rank sums, derives the Mann-Whitney U statistic, takes `W = min(U, n1*n2 - U)`, and computes a normal-approximation z-score and two-tailed p-value. Verifies against `wilcox.test(..., correct=FALSE, exact=FALSE)`.
**Assert:** `W` and `p_approx` match the oracle within `1e-6`; `U` and its complement satisfy the identity checked in the script.
**⚠️ Defect:** Uses the normal approximation only; no exact test and no continuity correction. Ties are handled by average ranks but the variance is not tie-corrected. No input validation (empty vectors, all ties, non-numeric values). Hardcoded two-tailed. No function wrapper.

---

**R-sphere batch 3: 6/6 patterns documented.** Verifier should check source at `/home/au/aura-pattern-library/r/nonparametric_and_categorical/` (canonical) or `/tmp/aura-review/aura-pattern-library/r/nonparametric_and_categorical/` (review copy). No Rscript on `.8`, so verification is doc-accuracy only: signatures, top-level script vs function, and defect claims vs source.

---
*△ AURA Pattern Library — © Reality Optimizer*
