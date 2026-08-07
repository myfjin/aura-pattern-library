# Python data-science lane — input robustness (PARTIAL COVERAGE)

**Measured 2026-08-07 over 73 patterns. Every cell below is an observed result, not an estimate.**

## ⛔ READ THE DENOMINATOR FIRST

This file covers **73 patterns**. The python lane holds **676**. It is NOT a lane-wide result and must never be quoted as one.

The probe calls a pattern's entry function with synthetic input. It can only do that when every required parameter is a matrix or a vector it knows how to build. A function needing a `k`, a `labels` array, a prior or a callable cannot be driven, and **an undriven function appears nowhere in this file** — it is absent, not passing.

How the number falls out, measured at each step:

```
676  python patterns
172  entry point derivable AND numeric-matrix domain
213  functions judged drivable from their signatures
106  functions the probe COULD ACTUALLY CALL at runtime
 73  patterns with at least one genuinely driven function  <- this file
```

⚠️ Static signature analysis over-predicted callability by roughly 2x (213 judged drivable, 106 driven). Treat any future "we can sweep N patterns" claim as a hypothesis until the calls actually run.

## ⛔ NOT COMPARABLE WITH `javascript/ROBUSTNESS.md`

Two structural reasons:

1. **Divergence threshold differs — this lane `1e15`, the JavaScript lane `1e6`.** A value flagged DIVERGED there may read FINITE here.
2. **The `uncentred` construction differs.** Measured on the shipped `linear_regression_gd`: FINITE up to an offset of ~5.0, DIVERGED from ~6.0. This lane uses offset 10.0 — above that boundary. The JavaScript reference recorded the same pattern FINITE, so it used a smaller offset.

Do not build a cross-lane table until both lanes are re-run under one declared configuration.

## What this file is, and what it is not

Each pattern carries a self-test that passes on its own fixture. This answers a different question: **what does it do on data its fixture does not contain?**

A non-FINITE cell is a **documented limit, not a defect**. Gradient descent that overflows on a column scaled 1e30 is behaving the way gradient descent behaves. The failure worth avoiding is not that limits exist — it is nobody knowing where they are.

⭐ **This reports; it does not judge.** `DIVERGED` is an observation, never a verdict on quality.

## Method

| setting | value |
|---|---|
| seed | `20260804` (fixed; two runs byte-identical) |
| divergence threshold | `1e15` |
| uncentred offset | `10.0` |
| wildly-scaled | ladder: 1e3, 1e6, 1e12, 1e30, 1e155 |
| probe | `probe_robustness.py` — built by 4Q, tested by 5S |

Reported per pattern: the most severe outcome across every function that could be driven, per class.

## Summary

**8 of 73 measured patterns are FINITE on all ten classes.**

⚠️ A further **1** (`topic_aware_recommender`) is FINITE on every class it was measured on, but was NOT measured on all ten — `single-row`, `constant-column` could not be driven. It is counted in neither figure above.

⛔ That distinction is the point of this file. An earlier draft counted it as clean by defaulting unmeasured cells to FINITE — absence read as a pass. 5S caught it.

| class | FINITE | NaN-Inf | DIVERGED | THREW | measured |
|---|---|---|---|---|---|
| `uncentred` | 64 | 1 | 2 | 4 | 71/73 |
| `near-collinear` | 64 | 0 | 2 | 5 | 71/73 |
| `rank-deficient` | 65 | 0 | 1 | 5 | 71/73 |
| `single-row` | 60 | 1 | 1 | 9 | 71/73 |
| `constant-column` | 63 | 0 | 2 | 5 | 70/73 |
| `wildly-scaled 1e+03` | 64 | 1 | 1 | 6 | 72/73 |
| `wildly-scaled 1e+06` | 60 | 1 | 4 | 7 | 72/73 |
| `wildly-scaled 1e+12` | 49 | 1 | 15 | 7 | 72/73 |
| `wildly-scaled 1e+30` | 26 | 1 | 39 | 6 | 72/73 |
| `wildly-scaled 1e+155` | 10 | 9 | 16 | 38 | 73/73 |

⭐ The ladder degrades monotonically — 64 FINITE at 1e3 down to 10 at 1e155 — which is what a working instrument looks like. A class returning the same answer at every magnitude would be measuring nothing.

## Per pattern

`·` FINITE · `DIV` diverged · `NaN` NaN/Inf · `THR` threw · **blank = NOT MEASURED, which is not a pass**

| pattern | unc | coll | rank | 1row | const | 1e3 | 1e6 | 1e12 | 1e30 | 1e155 |
|---|---|---|---|---|---|---|---|---|---|---|
| `backdoor_vs_collider_adjustment` | · | · | · | · | · | · | · | · | · | THR |
| `bagging_variance_reduction` | · | · | · | · | · | · | · | · | DIV | DIV |
| `bayes_factor_normal_means` | NaN | · | · | · | DIV | NaN | NaN | NaN | NaN | NaN |
| `bayesian_changepoint_offline` | · | · | · | · | · | · | · | · | · | THR |
| `bayesian_linear_regression` | · | · | · | · | · | · | · | · | · | THR |
| `bayesian_two_segment_changepoint` | · | THR | · | NaN | · | · | THR | THR | DIV | THR |
| `benford_law_test` | · | · | · | · | · | · | · | · | · | · |
| `bootstrap_confidence_interval` | · | · | · | · | · | · | · | · | DIV | DIV |
| `bootstrap_model_comparison` | · | · | · | · | · | · | · | · | DIV | DIV |
| `chi_square_independence` | · | · | · | · | · | · | · | · | · | NaN |
| `class_weight_imbalance` | THR | THR | THR | · | THR | THR | THR | THR | THR | THR |
| `conformal_prediction_intervals` | · | · | · | · | · | · | · | · | · | THR |
| `convolution_filtering` | · | · | · | · | · | · | · | DIV | DIV | THR |
| `copula_gaussian_lite` | · | · | · | · | · | · | · | · | · | · |
| `covariance_matrix` | · | · | · | · | · | · | · | DIV | DIV | NaN |
| `cross_domain_query_expansion` | · | · | · | · | · | · | · | · | · | · |
| `cross_domain_search_engine` | · | · | · | · | · | · | · | · | DIV | DIV |
| `cross_validation_leakage` | · | · | · | · | · | · | · | · | · | THR |
| `cuped_variance_reduction` | · | · | · | THR | · | · | · | · | DIV | DIV |
| `data_profiling_summary` | · | · | · | · | · | · | · | · | DIV | DIV |
| `elbo_monotone_vi` | · | · | · | · | · | · | · | DIV | DIV | THR |
| `em_two_coins` |  |  |  | · |  | THR | THR | THR | THR | THR |
| `empirical_bayes_shrinkage` | · | · | · | THR | · | · | · | · | DIV | THR |
| `evidence_ranks_true_model` | · | · | THR | THR | THR | · | · | · | · | THR |
| `feature_hashing_trick` | · | · | · | · | · | · | · | · | · | · |
| `feature_scaling_toolkit` | · | · | · | · | · | · | · | · | DIV | THR |
| `frontdoor_criterion_lite` | · | · | · | · | · | · | · | · | · | THR |
| `gp_regression_marginal_likelihood` | THR | THR | THR | · | THR | THR | THR | THR | THR | THR |
| `gradient_descent_momentum` | · | · | · | · | · | · | · | · | DIV | DIV |
| `hampel_filter_outliers` | · | · | · | · | · | · | · | DIV | DIV | THR |
| `hierarchical_shrinkage_2level` | · | · | · | · | · | · | · | · | DIV | THR |
| `histogram_builder` | · | · | · | · | · | · | · | · | DIV | DIV |
| `householder_reflection` | · | · | · | · | · | · | · | · | · | THR |
| `huber_robust_regression` | · | · | · | · | · | · | · | · | DIV | THR |
| `hyperloglog_distinct` | DIV | DIV | DIV | DIV | DIV | DIV | DIV | DIV | DIV | DIV |
| `instrumental_variable_lite` | · | · | · | THR | · | · | · | · | DIV | DIV |
| `iqr_outlier_detection` | · | · | · | · | · | · | · | · | DIV | DIV |
| `laplace_approximation_posterior` | · | · | · | · | · | · | · | · | DIV | DIV |
| `linear_discriminant_analysis` | · | · | · | THR | · | · | · | · | DIV | THR |
| `linear_regression_gd` | DIV | DIV | · | · | · | THR | THR | THR | THR | NaN |
| `logistic_regression` | · | · | · | · | · | · | DIV | DIV | DIV | THR |
| `mahalanobis_distance` | · | · | · | THR | · | · | · | · | · | · |
| `markov_chain_stationary` | THR | THR | THR | · | THR | THR | THR | THR | THR | THR |
| `meanfield_vi_gaussian` | · | · | · | · | · | · | · | · | DIV | THR |
| `model_persistence_roundtrip` |  |  |  |  |  |  |  |  |  | THR |
| `mutual_information_matrix` | · | · | · | · | · | · | · | · | · | THR |
| `negative_control_outcome` | · | · | · | · | · | · | · | · | · | THR |
| `newton_method_optimization` | · | · | · | · | · | · | · | · | · | · |
| `nonlinear_dependence_mi` | · | · | · | THR | · | · | · | · | · | THR |
| `online_covariance` | · | · | · | THR | · | · | · | DIV | DIV | NaN |
| `online_sgd_classifier` | · | · | · | · | · | · | DIV | DIV | DIV | THR |
| `partial_dependence_data` | · | · | · | · | · | · | · | DIV | DIV | THR |
| `pca_power_iteration` | · | · | · | · | · | · | · | DIV | DIV | NaN |
| `pearson_correlation_matrix` | · | · | · | THR | · | · | · | DIV | DIV | THR |
| `perceptron` | · | · | · | · | · | · | DIV | DIV | DIV | NaN |
| `permutation_feature_importance` | · | · | · | · | · | · | · | DIV | DIV | THR |
| `posterior_contraction_rate` | · | · | · | · | · | · | · | · | · | · |
| `random_forest` | · | · | · | · | · | · | · | · | DIV | DIV |
| `random_oversampling_balance` | · | · | · | · | · | · | · | DIV | DIV | NaN |
| `rank_correlation` | · | · | · | · | · | · | · | · | · | · |
| `rank_fusion_rrf` | · | · | · | · | · | · | · | · | DIV | DIV |
| `ransac_robust_regression` | · | · | · | · | · | · | · | · | · | THR |
| `resampling_interpolation` | · | · | · | · | · | · | · | · | DIV | THR |
| `rhat_convergence_diagnostic` | · | · | · | · | · | · | · | · | · | THR |
| `ridge_regression_normal_eq` | · | · | · | · | · | · | · | · | DIV | NaN |
| `shapley_value_sampling` | · | · | · | · | · | · | · | · | DIV | DIV |
| `spectral_clustering_lite` | THR | THR | THR | · | THR | THR | THR | THR | THR | THR |
| `stacking_ensemble` | · | · | · | · | · | · | · | DIV | DIV | THR |
| `target_encoding_smoothing` | · | · | · | · | · | · | · | · | · | THR |
| `textrank_lite` | · | · | · | · | · | · | · | · | · | · |
| `theil_sen_estimator` | · | · | · | · | · | · | · | · | · | THR |
| `topic_aware_recommender` | · | · | · |  |  | · | · | · | · | · |
| `winsorize_clip_outliers` | · | · | · | · | · | · | · | · | DIV | DIV |

---
*△ AURA Pattern Library — © Reality Optimizer*
