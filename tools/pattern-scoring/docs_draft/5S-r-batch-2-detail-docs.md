# Batch 2 — R Pattern Detail Docs (7 patterns): `hypothesis_testing_parametric`

First half of the second batch of the R data-science sphere. The remaining `nonparametric_and_categorical` patterns will follow in batch 3.

**R-sphere note:** most patterns are top-level scripts. Where the source defines an Entry function, its signature is copied verbatim from `SIGNATURES_REFERENCE_R.md`; otherwise the Entry field records `top-level script` and the Valid-input contract describes the expected top-level variables. Defects are sourced from the actual source.

---

## Category: hypothesis_testing_parametric

### 1. ab_power_analysis.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Numeric scalars `p1`, `p2` (proportions in `(0,1)`), `alpha` (significance level in `(0,1)`), and `beta_risk` (type-II risk in `(0,1)`). The demo sets `p1 = 0.40`, `p2 = 0.50`, `alpha = 0.05`, `beta_risk = 0.20`.
**Core:** Computes a two-proportion sample size via the Fleiss normal approximation and then computes achieved power at that sample size. Compares both to `power.prop.test()`.
**Assert:** `n_manual` is within 3 samples of the oracle `n`; the oracle's achieved power is at least `0.95 * power_target`; `abs(power_manual - power_oracle) < 0.05`.
**⚠️ Defect:** No input validation: invalid proportions or negative/≥1 alpha/beta produce uncontrolled or nonsensical results. Uses a normal approximation without continuity correction. Hardcoded two-sided alternative. No function wrapper, so parameters cannot be passed in.

### 2. anova_tukey.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Hardcoded four-group normal demo with `groups = 4`, `n_per_group = 20`, and `group_means = c(10, 12, 11.5, 14)`. For reuse, a numeric response vector `y` and an integer grouping factor `group_factor` of equal length must exist.
**Core:** Fits one-way ANOVA with `aov()`, extracts MSE and residual df, then computes all pairwise Tukey HSD confidence intervals and adjusted p-values using `qtukey`/`ptukey`. Verifies against `TukeyHSD()`.
**Assert:** Manual pairwise CIs are the mirror of the oracle intervals within `1e-6`; adjusted p-values match `TukeyHSD` within `1e-6`; number of pairs equals `choose(groups, 2)`; all adjusted p-values are in `[0,1]`.
**⚠️ Defect:** Assumes equal sample sizes per group (`n_each` is used for every pair). Assumes homoscedasticity because it uses the common MSE. No input validation (empty groups, unequal n, non-numeric values). No function wrapper.

### 3. correlation_tests.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Two numeric vectors `x` and `y` of equal length.
**Core:** Computes Pearson correlation via `cov(x,y)/(sd(x)*sd(y))`, derives the t-statistic and two-tailed p-value, and computes Spearman correlation as the Pearson correlation of ranks. Verifies against `cor()` and `cor.test()`.
**Assert:** Pearson and Spearman coefficients match `cor()` within `1e-8`; the Pearson t-statistic matches `cor.test()` within `1e-8`.
**⚠️ Defect:** No input validation: unequal lengths silently recycle or error later, constant vectors cause division by zero / NaN, and non-numeric inputs raise uncontrolled errors. Spearman uses `cor(rank(x), rank(y))` rather than the exact permutation distribution; tie handling is average ranks but not documented. No function wrapper.

### 4. ks_one_sample.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric sample `x` to be tested against the standard normal CDF `pnorm(0,1)`. The demo creates `x_normal <- rnorm(50,0,1)` and `x_exp <- rexp(50,1)`.
**Core:** Computes the ECDF at order statistics (`i/n` and `(i-1)/n`), forms `D+` and `D-`, and compares the D statistic to `ks.test()`. Also checks that the normal sample is accepted and the exponential sample is rejected at `alpha = 0.05`.
**Assert:** `D_normal` and `D_exp` match the `ks.test()` statistic within `1e-6`; normal sample p-value `> 0.05`; exponential sample p-value `< 0.05`.
**⚠️ Defect:** Tests only against fixed `pnorm(0,1)` parameters. If the true distribution has different mean/variance or is not normal, the test is not the Lilliefors-corrected version and may be invalid. No input validation. No function wrapper.

### 5. one_way_anova.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric response vector `y` and an integer grouping vector `groups` of equal length with at least two groups.
**Core:** Computes total, between-group, and within-group sum of squares, derives the F statistic and p-value, and verifies against `aov()`/`anova()`.
**Assert:** Manual F statistic and p-value match the `aov()` summary within `1e-8`.
**⚠️ Defect:** Assumes groups are coded as consecutive integers starting at 1; missing groups or non-integer labels are not handled. No post-hoc tests. No input validation (empty groups, non-numeric response). No function wrapper.

### 6. prop_test_two_sample.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Counts `x1`, `n1`, `x2`, `n2` with `0 <= x_i <= n_i` and `n_i > 0`. The demo uses `x1=20, n1=50` and `x2=36, n2=60`.
**Core:** Computes pooled proportion, z-statistic, two-tailed p-value, and chi-square `z^2`, then compares to `prop.test(..., correct=FALSE)`.
**Assert:** Chi-square statistic and p-value match the oracle within `1e-6`.
**⚠️ Defect:** No validation that `x_i <= n_i` or that `n_i > 0`; impossible counts silently produce invalid proportions or division by zero. No continuity correction. Hardcoded two-tailed. No function wrapper.

### 7. welch_t_test.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Two numeric vectors `x1` and `x2` representing independent samples.
**Core:** Computes the Welch-Satterthwaite t-statistic, approximate degrees of freedom, and two-tailed p-value, then verifies against `t.test()`.
**Assert:** Manual t-statistic and p-value match `t.test()` within `1e-8`.
**⚠️ Defect:** No input validation: empty vectors, one-element vectors, or constant/zero-variance groups make the denominator zero or produce `NaN`/`Inf`; non-numeric inputs error uncontrolled. Hardcoded two-tailed alternative. No function wrapper.

---

**R-sphere batch 2: 7/7 patterns documented.** Verifier should check source at `/home/au/aura-pattern-library/r/hypothesis_testing_parametric/` (canonical) or `/tmp/aura-review/aura-pattern-library/r/hypothesis_testing_parametric/` (review copy). No Rscript on `.8`, so verification is doc-accuracy only: signatures, top-level script vs function, and defect claims vs source.
