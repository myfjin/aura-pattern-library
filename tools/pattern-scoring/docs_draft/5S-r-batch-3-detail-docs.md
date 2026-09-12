# Batch 3 — R Pattern Detail Docs (6 patterns): `nonparametric_and_categorical`

Second half of the second batch of the R data-science sphere. Complements batch 2 (`hypothesis_testing_parametric`).

**R-sphere note:** most patterns are top-level scripts. Where the source defines an Entry function, its signature is copied verbatim from `SIGNATURES_REFERENCE_R.md`; otherwise the Entry field records `top-level script` and the Valid-input contract describes the expected top-level variables. Defects are sourced from the actual source.

---

## Category: nonparametric_and_categorical

### 1. chi_square_independence.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric contingency matrix `obs_table` with strictly positive expected counts under independence. The demo uses a `2x3` matrix `matrix(c(20, 15, 10, 25, 30, 5), nrow=2, ncol=3)`.
**Core:** Computes row and column totals, expected counts via `outer(row_totals, col_totals) / n_total`, the chi-square statistic, df, and p-value, then verifies against `chisq.test()`.
**Assert:** Chi-square statistic and p-value match `chisq.test()` within `1e-8`.
**⚠️ Defect:** No check for expected counts below 5 or for small-sample validity. Negative or non-numeric entries cause errors or `NaN` silently. No input validation. No function wrapper.

### 2. cramers_v_effect.R
**Entry fn:** `cramers_v <- function(contingency_table)`
**Valid input:** A numeric matrix or table representing a contingency table with at least 2 rows and 2 columns and all non-negative entries.
**Core:** Computes the chi-square statistic from expected counts, then Cramér's V = `sqrt(chi_sq / (n_total * (min_dim - 1)))`. Verifies against V recomputed from `chisq.test(..., correct=FALSE)`.
**Assert:** Strong-association V and weak-association V match the oracle within relative error `1e-10`; strong V exceeds weak V; weak V is `< 0.15`; both V values are in `[0,1]`.
**⚠️ Defect:** No input validation inside the function: empty table, `1x1` table, negative entries, or non-numeric inputs will fail or return garbage. Uses uncorrected Pearson chi-square (explicitly sets `correct=FALSE` in the oracle comparison but the function itself has no correction option). One sanity check (`v_strong_manual > 0.4`) is commented out. The function returns a scalar and does not validate dimensions.

### 3. fisher_exact_2x2.R
**Entry fn:** `hypergeo_prob <- function(a_val, m1, m2, n1, N)`
**Valid input:** Integer hypergeometric parameters satisfying `0 <= a_val <= min(m1, n1)`, `n1 - a_val <= m2`, and `N = m1 + m2 = n1 + n2`. The top-level demo uses a `2x2` table with cell `a = 12`, marginals `m1=15, m2=19, n1=16, n2=18, N=34`.
**Core:** Computes the log-scale hypergeometric probability mass for a candidate top-left cell, enumerates all valid cell values, and sums the one-tailed tail probability `P(A >= a_obs)`. Verifies against `fisher.test(..., alternative="greater")`.
**Assert:** `p_one_tail` matches the oracle p-value within `1e-6`.
**⚠️ Defect:** `hypergeo_prob` only computes a single probability mass; it does not perform the full Fisher exact test, check table dimensions, or return a two-tailed p-value. No parameter validation. The overall test logic is a top-level script, so the table and alternative are hardcoded and not reusable as a function.

### 4. kruskal_wallis.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A list of numeric vectors `groups` (the demo uses three groups named `group1`, `group2`, `group3`). All groups must be non-empty and numeric.
**Core:** Ranks all observations across groups, computes group rank sums, forms the H statistic `12/(N(N+1)) * sum(Ri^2/ni) - 3(N+1)`, and derives a chi-square p-value. Verifies against `kruskal.test()`.
**Assert:** H statistic and p-value match `kruskal.test()` within `1e-6` and `1e-5` respectively.
**⚠️ Defect:** Manual rank-sum extraction is hardcoded to three groups (`idx1`, `idx2`, `idx3`), so a different number of groups would require rewriting the script. No tie correction. No input validation (empty groups, non-numeric values). No function wrapper.

### 5. table_margins.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Two factor vectors `x` and `y` of equal length with explicit levels.
**Core:** Builds a contingency table by incrementing counts for each level combination, then computes row margins, column margins, and total by hand. Verifies against `table(x, y)` and `addmargins()`.
**Assert:** Manual table equals `table(x, y)` exactly; row and column margins equal the marginal tables; total equals sum of all counts.
**⚠️ Defect:** `which(levels_x == x[i])` fails silently when `x[i]` is `NA` or an unseen level, causing that observation to be dropped or mis-assigned. No validation that `x` and `y` are factors/characters of equal length. No function wrapper.

### 6. wilcoxon_rank_sum.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Two numeric vectors `x` and `y` representing independent samples. The demo uses `x <- rexp(12,1)` and `y <- rexp(10,1) + 2.5`.
**Core:** Ranks the combined sample, computes group rank sums, derives the Mann-Whitney U statistic, takes `W = min(U, n1*n2 - U)`, and computes a normal-approximation z-score and two-tailed p-value. Verifies against `wilcox.test(..., correct=FALSE, exact=FALSE)`.
**Assert:** `W` and `p_approx` match the oracle within `1e-6`; `U` and its complement satisfy the identity checked in the script.
**⚠️ Defect:** Uses the normal approximation only; no exact test and no continuity correction. Ties are handled by average ranks but the variance is not tie-corrected. No input validation (empty vectors, all ties, non-numeric values). Hardcoded two-tailed. No function wrapper.

---

**R-sphere batch 3: 6/6 patterns documented.** Verifier should check source at `/home/au/aura-pattern-library/r/nonparametric_and_categorical/` (canonical) or `/tmp/aura-review/aura-pattern-library/r/nonparametric_and_categorical/` (review copy). No Rscript on `.8`, so verification is doc-accuracy only: signatures, top-level script vs function, and defect claims vs source.
