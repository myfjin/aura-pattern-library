# JavaScript lane — input robustness

**Measured 2026-08-04 by `forge-gate/tests/verify_input_robustness.sh` over all 91 patterns in this lane. Every cell below is an observed result, not an estimate.**

## ⭐ What this file is, and what it is not

Each pattern here carries a self-test that passes on its own fixture. This appendix answers a different question: **what does the pattern do on data its fixture does not contain?**

A non-FINITE cell is a **documented limit, not a defect**. A k-means that diverges when one feature is scaled 10^6 larger than another is behaving the way k-means behaves — nobody centred or scaled the data for it. The failure worth avoiding is not that these limits exist; it is nobody knowing where they are.

⚠️ **This is the first lane in the library measured this way.** The same probe was run against the library's already-shipped, signed Python `linear_regression_gd`: it threw `OverflowError` on wildly-scaled input and diverged to `-4.55e+71` on near-collinear input, and its documentation records neither. The JavaScript lane is not more fragile than the rest of the library — it is the part that has been looked at.

## Method

Six input classes are generated beyond each pattern's own fixture:

| class | construction |
|---|---|
| `uncentred` | features with a large non-zero mean |
| `wildly_scaled` | one column many orders of magnitude larger than another |
| `near_collinear` | two columns almost linearly dependent |
| `rank_deficient` | one column an exact duplicate of another |
| `single_row` | only one sample |
| `constant_column` | one feature constant across all samples |

Reported per input is the most severe outcome in any numeric leaf of the returned value:

| outcome | meaning |
|---|---|
| `FINITE` | every numeric leaf finite and below the divergence threshold |
| `NaN-Inf` | at least one leaf is NaN or Infinity |
| `DIVERGED` | at least one leaf exceeds the threshold |
| `THREW` | the call raised — often a legitimate rejection |

**Divergence threshold: 1e6.** Correct coefficients and centroid coordinates for these deliberately small perturbation datasets are O(1) to O(100). A value past 1e6 signals unbounded growth — Jacobi on uncentred data reaches ~1e53 — rather than a legitimate large-but-finite answer.

⭐ **The gate reports; it does not judge.** It exits non-zero only when a pattern could not be exercised at all. `DIVERGED` is an observation, never a verdict on the pattern's quality.

## Summary

**54 of 91 patterns are FINITE on all six classes.**

| class | FINITE | NaN-Inf | DIVERGED | THREW |
|---|---|---|---|---|
| `uncentred` | 83 | 7 | 1 | 0 |
| `wildly_scaled` | 56 | 11 | 24 | 0 |
| `near_collinear` | 89 | 0 | 2 | 0 |
| `rank_deficient` | 86 | 4 | 1 | 0 |
| `single_row` | 71 | 3 | 1 | 16 |
| `constant_column` | 86 | 4 | 1 | 0 |

### The patterns that need the most care

- **`linreg_jacobi`** — the only pattern non-FINITE on *all six* classes. Jacobi converges only when `AtA` is diagonally dominant; this lane's fixture is centred on [-1,1], which happens to produce a dominant `AtA`. On uncentred features — the ordinary case — it diverges to ~1e51–1e57 with no error and no warning. **Centre your features, or use `linreg_gauss_seidel`, which is FINITE on every class.**
- **the gradient family** — `NaN-Inf` on uncentred and wildly-scaled input. A fixed step size that is stable for O(1) features overflows when features are O(1e3).
- **`linreg_lu` and `linreg_normal_eq`** — `NaN-Inf` on rank-deficient input; neither guards a zero pivot. Prefer `linreg_svd` or `linreg_ridge`, which return the minimum-norm solution.
- **`linreg_cholesky`** — returns a *finite wrong answer* on a non-SPD matrix rather than failing, because its pivot fallback substitutes `1e-8`. A plausible-looking wrong number propagates further than a NaN does.

## Full results

| pattern | `uncentred` | `wildly_scaled` | `near_collinear` | `rank_deficient` | `single_row` | `constant_column` |
|---|---|---|---|---|---|---|
| `01_iterative_refinement` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `01_kmeans_lloyd` | FINITE | **DIVERGED** | FINITE | FINITE | **THREW** | FINITE |
| `01_kmeans_parallel_pp` | FINITE | **DIVERGED** | FINITE | FINITE | FINITE | FINITE |
| `01_sorted_summation` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `02_blocked_summation` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `02_kmeans_pp` | FINITE | **DIVERGED** | FINITE | FINITE | FINITE | FINITE |
| `02_kmeans_yinyang` | FINITE | **DIVERGED** | FINITE | FINITE | **THREW** | FINITE |
| `02_richardson_iteration` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `03_chebyshev_semi_iterative` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `03_kmeans_annulus` | FINITE | **DIVERGED** | FINITE | FINITE | **THREW** | FINITE |
| `03_kmeans_macqueen` | FINITE | **DIVERGED** | FINITE | FINITE | **THREW** | FINITE |
| `03_recursive_summation` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `04_klein_compensation` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `04_kmeans_compare_means` | FINITE | **DIVERGED** | FINITE | FINITE | **THREW** | FINITE |
| `04_kmeans_hartigan_wong` | FINITE | **DIVERGED** | FINITE | FINITE | **THREW** | FINITE |
| `04_randomized_kaczmarz` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `05_block_coordinate_descent` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `05_error_free_transforms` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `05_kmeans_elkan` | FINITE | **DIVERGED** | FINITE | FINITE | **THREW** | FINITE |
| `05_kmeans_sort_means` | FINITE | **DIVERGED** | FINITE | FINITE | **THREW** | FINITE |
| `06_admm_zero_regularization` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `06_double_double` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `06_kmeans_hamerly` | FINITE | **DIVERGED** | FINITE | FINITE | **THREW** | FINITE |
| `06_kmeans_kdtree` | FINITE | **DIVERGED** | FINITE | FINITE | **THREW** | FINITE |
| `07_dual_ascent` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `07_fixed_point` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `07_kmeans_heap` | FINITE | **DIVERGED** | FINITE | FINITE | **THREW** | FINITE |
| `07_kmeans_minibatch` | FINITE | **DIVERGED** | FINITE | FINITE | FINITE | FINITE |
| `08_gauss_newton` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `08_kmeans_forgy` | FINITE | **DIVERGED** | FINITE | FINITE | **THREW** | FINITE |
| `08_kmeans_hybrid_bounds` | FINITE | **DIVERGED** | FINITE | FINITE | **THREW** | FINITE |
| `08_streaming_recompaction` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `09_kmeans_canopy` | FINITE | **DIVERGED** | FINITE | FINITE | FINITE | FINITE |
| `09_kmeans_random_partition` | FINITE | **DIVERGED** | FINITE | FINITE | FINITE | FINITE |
| `09_long_accumulator` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `09_trust_region_dogleg` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `10_kmeans_bisecting` | FINITE | **DIVERGED** | FINITE | FINITE | **THREW** | FINITE |
| `10_kmeans_repeated_restart` | FINITE | **DIVERGED** | FINITE | FINITE | FINITE | FINITE |
| `10_proximal_point` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `10_shuffled_permutations` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_adadelta` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_adagrad` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_adam` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_backtracking` | FINITE | **NaN-Inf** | FINITE | FINITE | FINITE | FINITE |
| `linreg_barzilai_borwein` | **NaN-Inf** | **NaN-Inf** | FINITE | FINITE | FINITE | FINITE |
| `linreg_bfgs` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_cg` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_cholesky` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_coordinate` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_gauss_jordan` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_gauss_seidel` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_gd_1d_univariate` | **NaN-Inf** | **NaN-Inf** | FINITE | FINITE | FINITE | FINITE |
| `linreg_givens` | FINITE | FINITE | FINITE | **NaN-Inf** | **THREW** | **NaN-Inf** |
| `linreg_householder_qr` | FINITE | FINITE | FINITE | FINITE | **THREW** | FINITE |
| `linreg_jacobi` | **DIVERGED** | **DIVERGED** | **DIVERGED** | **DIVERGED** | **DIVERGED** | **DIVERGED** |
| `linreg_kaczmarz` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_landweber` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_lbfgs` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_levenberg_marquardt` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_lsqr` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_lu` | FINITE | **NaN-Inf** | **DIVERGED** | **NaN-Inf** | **NaN-Inf** | **NaN-Inf** |
| `linreg_minibatch` | **NaN-Inf** | **NaN-Inf** | FINITE | FINITE | FINITE | FINITE |
| `linreg_minres` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_modified_gram_schmidt` | FINITE | **DIVERGED** | FINITE | FINITE | FINITE | FINITE |
| `linreg_momentum` | **NaN-Inf** | **NaN-Inf** | FINITE | FINITE | FINITE | FINITE |
| `linreg_nadam` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_nesterov` | **NaN-Inf** | **NaN-Inf** | FINITE | FINITE | FINITE | FINITE |
| `linreg_newton` | FINITE | **NaN-Inf** | FINITE | **NaN-Inf** | **NaN-Inf** | **NaN-Inf** |
| `linreg_normal_eq` | FINITE | **NaN-Inf** | FINITE | **NaN-Inf** | **NaN-Inf** | **NaN-Inf** |
| `linreg_pcg` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_polyak_sgd` | **NaN-Inf** | **NaN-Inf** | FINITE | FINITE | FINITE | FINITE |
| `linreg_power_iteration_svd` | FINITE | **DIVERGED** | FINITE | FINITE | FINITE | FINITE |
| `linreg_qr` | FINITE | **DIVERGED** | FINITE | FINITE | FINITE | FINITE |
| `linreg_ridge` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_rls` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_rmsprop` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_sgd` | **NaN-Inf** | **NaN-Inf** | FINITE | FINITE | FINITE | FINITE |
| `linreg_sherman_morrison` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_sor` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_steepest_descent_exact` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `linreg_svd` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `statistics_chan` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `statistics_kahan` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `statistics_naive_sos` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `statistics_neumaier` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `statistics_pairwise` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `statistics_shifted` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `statistics_twopass` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `statistics_welford` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `statistics_west` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |
| `statistics_youngs_cramer` | FINITE | FINITE | FINITE | FINITE | FINITE | FINITE |

---
*△ AURA Pattern Library — © Reality Optimizer*
