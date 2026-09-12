# Fable R Batch — multivariate_and_applied_modeling Detail Docs (5 patterns)

Categories: `multivariate_and_applied_modeling` (5). Documented directly by Fable (mesh offline); verified against source.

## Category: multivariate_and_applied_modeling

### 1. km_survival_lite.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; n=100, survival ~ Exp(0.02), censoring ~ Exp(0.01), fixed seed.
**Core:** Kaplan-Meier product-limit survival estimator from right-censored data: at each event time computes n-at-risk, n-events, `S_i = S_{i-1}·(1 − d/n)`, and Greenwood standard error with a *separate* running sum (comments note this fixes two prior bugs: compounding the S² factor, and the infinite term when n==d).
**Assert:** `stopifnot(...)` on the KM table (survival monotone-decreasing in [0,1], Greenwood SE finite).
**⚠️ Defect:** O(#event-times × n) double loop (recomputes at-risk set each step) — slow for large n. Ties are handled only by exact `time == t` equality (floating survival times rarely tie). Greenwood SE is undefined once S reaches 0 (last event) — handled by skipping the term, but the final SE understates uncertainty there.

### 2. kmeans_lloyd.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; 3 Gaussian blobs (n=25 each, 2-D), k=3, 20 iterations fixed.
**Core:** Lloyd's k-means: random init from data points, assign each point to nearest center (Euclidean via `dist`), recompute centers as cluster means, iterate to convergence (`max|Δcenter|<1e-8`). Cross-checks total within-cluster SS against base `kmeans()` seeded with the same centers.
**Assert:** `all.equal(wss_manual, kmeans()$tot.withinss, tol=1e-4)`.
**⚠️ Defect:** Distances via `as.matrix(dist(rbind(X, centers)))` builds a full (n+k)² matrix each iteration then slices it — quadratic waste vs. a direct point-to-center loop. Empty-cluster case returns the old center (no re-seeding), which can stall convergence on degenerate data. Correctness depends on the well-separated planted blobs.

### 3. pca_power_iteration.R
**Entry fn:** `power_iterate(C, iters = 1000, tol = 1e-12)` → `list(vector, value)`; helper `align(v, oracle)`.
**Valid input:** `C` a symmetric (covariance) matrix; `iters` positive; `tol` small positive. In-script: n=300, 5 correlated features.
**Core:** Top eigenvector/eigenvalue via power iteration (normalize `w = Cv/‖Cv‖` to convergence), then Hotelling deflation `C − λ₁v₁v₁ᵀ` to get PC2. Compares vectors/eigenvalues to `prcomp` (sign-aligned).
**Assert:** `max|v − oracle| < 1e-3` for PC1 & PC2; relative eigenvalue error `< 1e-3`.
**⚠️ Defect:** Only the top-2 components are extracted; deflation accumulates numerical error for later PCs (fine at 2, degrades if extended). Power iteration converges slowly when the top two eigenvalues are close (near-degenerate spectra) — the fixed `iters=1000` cap could return an unconverged vector without erroring. Random init means run-to-run iteration count varies.

### 4. stratified_split.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; y = factor(60 pos / 40 neg), split_prop=0.8 fixed.
**Core:** Stratified train/test split: within each class level, sample `floor(n_level·0.8)` for train, remainder to test — preserving class proportions in both splits.
**Assert:** `all.equal` of train & test class proportions to the original, tol=0.05.
**⚠️ Defect:** `floor` rounding can drift proportions for small/odd strata (exact here, not guaranteed generally). Final index vectors are built class-by-class (`c()`-growth) and **not shuffled**, so train/test rows come out grouped by class — order-dependent downstream code could be affected. No handling for a class too small to split.

### 5. weighted_survey_mean.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; 2 strata (pop 1000 @μ50 / 4000 @μ100), survey oversamples stratum 1 (200) vs stratum 2 (100).
**Core:** Design-weighted (Horvitz-Thompson-style) survey mean: inverse-inclusion weights `w = N_stratum/n_stratum`, `weighted.mean`, plus a design-adjusted variance/SE using normalized weights and Kish effective sample size `n_eff = (Σw)²/Σw²`.
**Assert:** weighted mean closer to the true population mean than the naïve mean; `|weighted − true| < 5`; design-adjusted and naïve SE both > 0.
**⚠️ Defect:** Sampling is without replacement but the variance uses no **finite-population correction**, so the design SE is slightly conservative. Only two strata, weights hard-coded to the planted design; no guard for a stratum with zero surveyed units (division by zero in the weight).
