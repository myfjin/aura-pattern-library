# Batch 1 — R Pattern Detail Docs (13 patterns)

Categories: `data_wrangling_and_feature_engineering` (8) + `distributions_and_resampling` (5). First batch of the R data-science sphere.

**R-sphere note:** most patterns in this batch are top-level scripts rather than wrapped functions. Where the source defines an Entry function, its signature is shown verbatim; where it does not, the Entry field records `top-level script` and the Valid-input contract describes the expected top-level variables. Defects are sourced from the actual source.

---

## Category: data_wrangling_and_feature_engineering

### 1. date_features.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A `Date` vector named `dates` must exist in the global environment. The script generates 100 consecutive days starting from `2025-01-01` as a demo if `dates` is not pre-loaded, so results depend on whether `dates` is caller-supplied.
**Core:** Extracts weekday (`%w`, 0 = Sunday), month, quarter, and weekend flag from a date vector using base R `format()` and arithmetic.
**Assert:** Spot-checks known calendar dates (2025-01-01 is Wednesday, Q1); verifies all quarters are in 1–4 and all weekend flags are 0/1.
**⚠️ Defect:** No input validation: a non-Date vector or `NA` dates produce silently wrong or `NA` results. The `%w` Sunday-zero convention is undocumented in the script. Because it is a top-level script, it cannot be reused as a function and it mutates/replaces the extracted vectors in the global environment.

### 2. factor_onehot.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A `factor` named `f` with explicit `levels`. The script constructs its own demo factor if `f` is absent.
**Core:** Builds a one-hot matrix by looping over factor levels and setting the matching column to 1 for each observation.
**Assert:** Column sums equal the level counts from `table(f)`; every row sums to exactly 1; an unseen level is represented by an all-zero row.
**⚠️ Defect:** No input validation: if `f` is not a factor, `levels(f)` may return `NULL` or character levels and the loop will silently produce an empty or wrong matrix. `NA` factor values cause `which(levels(f) == f[i])` to return `integer(0)`, so the corresponding row becomes all zeros without warning. The unseen-level "policy" is only demonstrated with a manually zeroed vector, not actually enforced by a reusable function.

### 3. group_aggregate.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A `data.frame` named `df` with columns `group1` (character), `group2` (numeric/coercible), and `value` (numeric).
**Core:** Creates a composite key `group1-group2`, loops over unique keys, and computes the mean of `value` per key using `rbind` accumulation. Verifies against `aggregate(value ~ group1 + group2, data=df, mean)`.
**Assert:** Manual aggregation values match the `aggregate()` oracle within tolerance.
**⚠️ Defect:** `rbind` inside a loop is quadratic and slow for many groups. No input validation: missing columns or wrong types raise uncontrolled errors. `as.numeric(parts[2])` silently coerces `group2` to numeric, which can introduce `NA` if the original values were not coercible without warning. It computes only the mean; no extensibility for other aggregations.

### 4. hash_join.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Two `data.frame`s named `df1` (left) and `df2` (right), each with a column `key`.
**Core:** Builds an R `environment` hashmap from `df2$key` → `df2$value2`, then loops over `df1` rows and appends matches to a result data frame. Verifies against `merge(df1, df2, by="key")`.
**Assert:** Result row count and matched values equal the `merge()` oracle.
**⚠️ Defect:** Performs an inner join only: keys present only in `df1` are silently dropped with no indication. Duplicate keys in `df2` are silently overwritten in the environment hashmap, so the join is not duplicate-key-safe. No input validation on column existence or type. No function wrapper, so it cannot be parameterized.

### 5. long_wide_reshape.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A `data.frame` named `long_df` with columns `id`, `time`, and `value`, where `time` takes exactly two distinct values.
**Core:** Manually reshapes long→wide by filling a matrix with `long_df$value` indexed by `id` and `time`, then reshapes wide→long by iterating rows and columns.
**Assert:** Round-trip long→wide→long reproduces the original `value` column within tolerance.
**⚠️ Defect:** `names(wide_manual) <- c("time_1")` is shorter than the number of columns (2), so R recycles the name with a warning, leaving the second column also named `time_1`. Hardcoded to exactly two time points; any other cardinality will fail or silently produce `NA`s. No input validation. The round-trip test does not verify the wide format itself is semantically correct, only that values can be recovered.

### 6. missing_pattern_matrix.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Three numeric vectors named `x1`, `x2`, `x3` must exist in the global environment. The script plants its own MAR missingness mechanism as a demo if they are absent.
**Core:** Builds a binary missingness pattern matrix, counts unique patterns, and computes pairwise-complete correlations using `cor(use="pairwise.complete.obs")` as an oracle.
**Assert:** Pattern `(0,0,0)` is the most common; pattern `(0,1,x)` exists; pairwise correlations agree with the oracle within `1e-10`.
**⚠️ Defect:** Two sanity checks are commented out: `sum(pattern_df$count) == n` and one of the correlation agreement checks. This means the script does not actually enforce that all rows are accounted for or that all pairwise correlations match. Hardcoded to three variables. No input validation. No function wrapper.

### 7. na_imputation.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric vector named `x` containing some `NA` values.
**Core:** Creates two imputed copies: mean-imputed and median-imputed, plus a missingness indicator vector.
**Assert:** The number of missing values matches the planted count (2 in the demo); all imputed vectors are `NA`-free; imputed mean/median statistics stay close to the imputation strategy values.
**⚠️ Defect:** Despite the file name and header mentioning "Mean/Median/Mode", no mode imputation is implemented. No input validation: `mean(x, na.rm=TRUE)` on a non-numeric or all-`NA` vector raises uncontrolled errors. Mean imputation deflates variance and distorts correlations; the script does not document this statistical bias. No function wrapper.

### 8. rolling_stats.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric vector named `x` and a positive integer `window_size` such that `window_size <= length(x)`.
**Core:** Computes rolling mean and rolling sample standard deviation over a fixed window using explicit loops.
**Assert:** Rolling mean and rolling SD match brute-force per-window calculations within tolerance.
**⚠️ Defect:** No input validation: if `window_size > length(x)`, the loop range becomes negative/empty and results are silently empty or invalid. `NA` values in `x` silently propagate through `mean()` and `sd()`, making entire windows `NA` without warning. Edge windows and partial windows are not handled. No function wrapper.

---

## Category: distributions_and_resampling

### 9. bootstrap_ci.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric vector named `y` and a scalar `true_mean`. The script generates its own demo sample if `y` is absent.
**Core:** Draws `B = 1000` bootstrap resamples with replacement, computes the mean of each, and returns the 2.5th and 97.5th percentile intervals.
**Assert:** The planted `true_mean` falls inside the percentile CI; the bootstrap SE approximates the analytical sample SE within 10%.
**⚠️ Defect:** Hardcoded `B = 1000` and `alpha = 0.05`; no parameterization. Uses the percentile method only — no BCa or bias correction. `NA` values in `y` silently contaminate bootstrap means. No input validation. No function wrapper.

### 10. ecdf_dkw_bands.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric sample named `x` and a significance level `alpha` in `(0, 1)`. Default demo uses `n = 100`, `alpha = 0.05`, and `N(0,1)`.
**Core:** Computes the empirical CDF at order statistics and adds/subtracts the DKW epsilon `sqrt(log(2/alpha)/(2*n))`, clipping to `[0, 1]`.
**Assert:** Single-sample coverage of the true CDF is > 0.9; average coverage over 100 repeated samples exceeds `1 - alpha - 0.05`.
**⚠️ Defect:** No input validation: `alpha <= 0` or `alpha >= 1` produces `NaN`/`Inf` epsilon silently. The script evaluates coverage only at sample order statistics, not over a dense grid, so bands between order statistics are not verified. No function wrapper.

### 11. kde_gaussian.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric vector named `x`. The script generates a bimodal demo sample if `x` is absent.
**Core:** Computes Silverman's rule-of-thumb bandwidth and evaluates a Gaussian KDE on a regular grid using `dnorm()`.
**Assert:** Manual KDE values match the `density()` oracle (with the same bandwidth) within tolerance on the grid.
**⚠️ Defect:** Silverman's bandwidth assumes the data are roughly unimodal and Gaussian; it can oversmooth multimodal data. No input validation: `NA` values in `x` silently propagate through `var()` and `dnorm()`. `var(x)` uses the sample variance (denominator `n-1`), but Silverman's rule typically uses sample standard deviation with an adjusted constant — the script conflates the two. No function wrapper.

### 12. outlier_iqr_mad.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric vector named `x`. The script plants two extreme outliers in a standard-normal sample if `x` is absent.
**Core:** Computes IQR fences (`Q1 - 1.5*IQR`, `Q3 + 1.5*IQR`) and MAD z-scores (`|x - median| / MAD > 2.5`), then flags outliers.
**Assert:** The planted outliers are flagged by IQR; at most 3 of 200 clean N(0,1) observations are flagged by chance.
**⚠️ Defect:** Hardcoded thresholds (1.5*IQR, 2.5*MAD) with no parameterization. `NA` values are silently dropped by `quantile()` and `median()`, changing the computed fences without warning. The MAD method uses the constant 2.5, which is not the standard 3.5×MAD convention and is not justified in the script. No function wrapper.

### 13. quantile_type7.R
**Entry fn:** `quantile_type7 <- function(x, p)`
**Valid input:** `x` is a numeric vector of length at least 2; `p` is a probability in `[0, 1]` (the function is demonstrated with `p_vals = c(0.25, 0.5, 0.75, 0.95)`).
**Core:** Sorts `x` and computes R's type-7 quantile by linear interpolation between order statistics using `h = (n - 1) * p`.
**Assert:** Manual quantiles match `quantile(x, p, type=7)` within `1e-6`.
**⚠️ Defect:** No input validation: `p` outside `[0, 1]` causes out-of-bounds indexing silently or with a confusing subscript error; empty `x` or `length(x) == 1` can return `NA` or crash. `NA` values in `x` are sorted to the end and can produce `NA` quantiles without warning. The source sorts `x` both at top level and inside the function, doing redundant work. The function returns a single scalar even when called via `sapply`, so vectorized `p` is only supported by the caller, not the function itself.

---

**R-sphere batch 1: 13/13 patterns documented.** Verifier should check source at `/home/au/aura-pattern-library/r/` (canonical) or `/tmp/aura-review/aura-pattern-library/r/` (review copy). No Rscript on `.8`, so verification is doc-accuracy only: signatures, top-level script vs function, and defect claims vs source.
