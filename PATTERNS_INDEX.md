# AURA Pattern Library — Pattern Index

Direct link and description for every one of the **1,500 pattern files** (1,024 unique pattern IDs across 6 languages).

Descriptions are extracted from each file at generation time under the frozen ruler (python = module docstring; others = first real comment block), so this index cannot drift from the code. `—` means the file carries no description.

Regenerate with `python3 build_patterns_index.py`. For the ID-keyed master (twins, tiers, licensing) see [CATALOG.md](CATALOG.md).

## Contents

- [`cpp`](#cpp) — 370 files, 37 categories
- [`go/programming`](#goprogramming) — 45 files, 11 categories
- [`go/system-administration`](#gosystem-administration) — 58 files, 1 categories
- [`javascript`](#javascript) — 91 files, 6 categories
- [`python/data-science`](#pythondata-science) — 377 files, 37 categories
- [`python/programming`](#pythonprogramming) — 99 files, 13 categories
- [`python/system-administration`](#pythonsystem-administration) — 200 files, 20 categories
- [`r`](#r) — 60 files, 9 categories
- [`rust`](#rust) — 200 files, 10 categories

## cpp

*370 files across 37 categories.*

### data-science/applied_ds_practice

| Pattern | Description | Also in |
|---|---|---|
| [`cohort_retention_analysis`](cpp/data-science/applied_ds_practice/cohort_retention_analysis.cpp) | Cohort Retention Analysis Group users by cohort, track which cohorts return in subsequent periods, and compute retention curves. | Python |
| [`cross_validation_leakage`](cpp/data-science/applied_ds_practice/cross_validation_leakage.cpp) | Cross-validation leakage: feature selection before CV inflates accuracy. Core claim: leaky CV (select on full data) overestimates vs correct CV. | Python |
| [`drift_detection_psi`](cpp/data-science/applied_ds_practice/drift_detection_psi.cpp) | Distribution-drift detection via Population Stability Index (PSI) and the Kolmogorov-Smirnov statistic between a reference and current sample, binning current data on reference… | Python |
| [`ewma_streaming_metrics`](cpp/data-science/applied_ds_practice/ewma_streaming_metrics.cpp) | Streaming online metrics: an exponentially weighted moving average (EWMA) versus a simple moving average (SMA), tracked point-by-point over a noisy series. Use for low-latency… | Python |
| [`feature_hashing_trick`](cpp/data-science/applied_ds_practice/feature_hashing_trick.cpp) | Feature hashing for dimensionality reduction of high-dimensional sparse features. Oracle parity: embeds Python SHA-256-derived vectors and the exact collision rates; implements… | Python |
| [`funnel_conversion_analysis`](cpp/data-science/applied_ds_practice/funnel_conversion_analysis.cpp) | Multi-step funnel conversion analysis: computes step-to-step conversion rates and Wilson score confidence intervals for each stage, then flags the weakest step. Use to size and… | Python |
| [`rfm_customer_segmentation`](cpp/data-science/applied_ds_practice/rfm_customer_segmentation.cpp) | RFM customer segmentation: derives recency, frequency, and monetary value per user from a transaction log, quartile-scores each axis (recency reversed so recent buyers score… | Python |
| [`simpsons_paradox_demo`](cpp/data-science/applied_ds_practice/simpsons_paradox_demo.cpp) | Simpson's Paradox: aggregate trend reverses within strata. C++17 self-contained implementation. | Python |
| [`target_encoding_smoothing`](cpp/data-science/applied_ds_practice/target_encoding_smoothing.cpp) | Target (mean) encoding of categorical features with additive smoothing toward the global prior, plus out-of-fold encoding of training rows to avoid leakage. Use to encode… | Python |
| [`welford_online_stats`](cpp/data-science/applied_ds_practice/welford_online_stats.cpp) | Welford's online algorithm for running mean and variance. Converted from the Python oracle. | Python |

### data-science/bayesian_iii_approximate_inference

| Pattern | Description | Also in |
|---|---|---|
| [`abc_rejection_sampler`](cpp/data-science/bayesian_iii_approximate_inference/abc_rejection_sampler.cpp) | Approximate Bayesian Computation (ABC): rejection sampling for intractable likelihoods. Sample from prior, simulate data, accept if simulated ≈ observed (within ε). Core claim:… | Python |
| [`bayes_factor_normal_means`](cpp/data-science/bayesian_iii_approximate_inference/bayes_factor_normal_means.cpp) | Bayes Factor for Comparing Two Normal Means BF = p(data\|H1) / p(data\|H0). Core claim: BF>1 when H1 is true AND BF<1 when H0 is true (BOTH directions asserted; the two-sided… | Python |
| [`elbo_monotone_vi`](cpp/data-science/bayesian_iii_approximate_inference/elbo_monotone_vi.cpp) | ELBO monotonicity in coordinate-ascent variational inference. | Python |
| [`hierarchical_shrinkage_2level`](cpp/data-science/bayesian_iii_approximate_inference/hierarchical_shrinkage_2level.cpp) | Hierarchical shrinkage (James-Stein): partial-pooling beats no-pooling on MSE. | Python |
| [`laplace_approximation_posterior`](cpp/data-science/bayesian_iii_approximate_inference/laplace_approximation_posterior.cpp) | Laplace approximation: approximate posterior p(θ\|data) with Gaussian at MAP. Oracle asserts: abs(theta_map - 2.0) < 0.5 posterior_var > 0 posterior_var < 1.0 | Python |
| [`meanfield_vi_gaussian`](cpp/data-science/bayesian_iii_approximate_inference/meanfield_vi_gaussian.cpp) | Mean-field variational inference for a Gaussian with unknown mean AND precision. Oracle asserts: abs(vi_mu - mu_true) < 0.4 abs(vi_mu - sample_mean) < 0.05 abs(vi_tau -… | Python |
| [`posterior_contraction_rate`](cpp/data-science/bayesian_iii_approximate_inference/posterior_contraction_rate.cpp) | Posterior contraction for a Gaussian mean under a Gaussian prior: the posterior standard deviation is sqrt(1/(n + 1/prior_var)), which shrinks as data grows. Use to reason about… | Python |
| [`posterior_predictive_pvalue`](cpp/data-science/bayesian_iii_approximate_inference/posterior_predictive_pvalue.cpp) | Posterior predictive p-value: the fraction of posterior-predictive samples at or above an observed test statistic, used as a Bayesian goodness-of-fit check. Use to detect model… | Python |
| [`rhat_convergence_diagnostic`](cpp/data-science/bayesian_iii_approximate_inference/rhat_convergence_diagnostic.cpp) | Gelman-Rubin R-hat convergence diagnostic for MCMC: combines between-chain and within-chain variance as sqrt((B+W)/W), which approaches 1 when chains agree. Use to decide whether… | Python |
| [`sbc_rank_uniformity`](cpp/data-science/bayesian_iii_approximate_inference/sbc_rank_uniformity.cpp) | Simulation Based Calibration (SBC): ranks should be uniform for a well-calibrated sampler. | Python |

### data-science/bayesian_iii_modeling_selection

| Pattern | Description | Also in |
|---|---|---|
| [`bayesian_changepoint_offline`](cpp/data-science/bayesian_iii_modeling_selection/bayesian_changepoint_offline.cpp) | Bayesian Changepoint Detection Find the point where mean shifts. Core claim: detected changepoint ≈ true location within tolerance. | Python |
| [`bayesian_linreg_conjugate`](cpp/data-science/bayesian_iii_modeling_selection/bayesian_linreg_conjugate.cpp) | Bayesian Linear Regression with Conjugate Prior Posterior mean ≈ true βs; 95% credible interval covers them. | Python |
| [`beta_binomial_overdispersion`](cpp/data-science/bayesian_iii_modeling_selection/beta_binomial_overdispersion.cpp) | Beta-Binomial Overdispersion Counts with a random per-trial success probability p ~ Beta(α, β) are OVERDISPERSED relative to a binomial. Method-of-moments recovers (α, β) from the… | Python |
| [`bic_selects_true_degree`](cpp/data-science/bayesian_iii_modeling_selection/bic_selects_true_degree.cpp) | BIC Model Selection Picks True Polynomial Degree Fits polynomials of increasing degree by least squares and scores each with BIC = n·log(RSS/n) + k·log(n). BIC penalizes extra… | Python |
| [`crp_table_growth`](cpp/data-science/bayesian_iii_modeling_selection/crp_table_growth.cpp) | Chinese Restaurant Process (CRP): expected number of tables ≈ α·ln(n). Core claim: E[#tables] ≈ α·ln(n) within tolerance (planted α). | Python |
| [`dirichlet_multinomial_posterior`](cpp/data-science/bayesian_iii_modeling_selection/dirichlet_multinomial_posterior.cpp) | Dirichlet-Multinomial posterior concentration — C++17 port. Shows posterior mean error shrinks as sample size grows. | Python |
| [`dirichlet_stick_breaking`](cpp/data-science/bayesian_iii_modeling_selection/dirichlet_stick_breaking.cpp) | Dirichlet stick-breaking process — C++17 port. Weights sum toward 1; higher concentration α yields more active clusters. | Python |
| [`evidence_ranks_true_model`](cpp/data-science/bayesian_iii_modeling_selection/evidence_ranks_true_model.cpp) | Model evidence (via BIC) ranks the true generative model above the alternative. C++17 self-contained port with full parity to Python oracle. | Python |
| [`gp_regression_marginal_likelihood`](cpp/data-science/bayesian_iii_modeling_selection/gp_regression_marginal_likelihood.cpp) | Gaussian-process regression: the marginal likelihood peaks at the true lengthscale. | Python |
| [`kalman_rts_smoother`](cpp/data-science/bayesian_iii_modeling_selection/kalman_rts_smoother.cpp) | Kalman filter + Rauch-Tung-Striebel (RTS) smoother. Oracle asserts: mean_mse_smooth < mean_mse_filt mean_mse_smooth < 0.9 * mean_mse_filt | Python |

### data-science/causal_inference_experimentation

| Pattern | Description | Also in |
|---|---|---|
| [`ab_test_srm_check`](cpp/data-science/causal_inference_experimentation/ab_test_srm_check.cpp) | Sample Ratio Mismatch (SRM) Check for A/B Tests. In a valid A/B test, the allocation ratio should match the design (e.g., 50/50). A chi-square test on the observed counts detects… | Python |
| [`cuped_variance_reduction`](cpp/data-science/causal_inference_experimentation/cuped_variance_reduction.cpp) | CUPED variance reduction: use covariates to reduce variance in A/B tests. Core claim: CUPED-adjusted estimator has lower variance than naive. | Python |
| [`difference_in_differences`](cpp/data-science/causal_inference_experimentation/difference_in_differences.cpp) | Difference-in-Differences — C++17 port. Two groups, before/after, parallel trends, recovers planted treatment effect. | Python |
| [`instrumental_variable_lite`](cpp/data-science/causal_inference_experimentation/instrumental_variable_lite.cpp) | Instrumental Variable (IV) Estimation. Oracle asserts: bias_iv < bias_naive bias_iv < 2.0 | Python |
| [`interrupted_time_series`](cpp/data-science/causal_inference_experimentation/interrupted_time_series.cpp) | Interrupted Time Series (ITS) Segmented Regression. Oracle asserts: abs(level_change - 10.0) < 2.0 abs(slope_change - 0.3) < 0.5 | Python |
| [`placebo_test_causal`](cpp/data-science/causal_inference_experimentation/placebo_test_causal.cpp) | placebo_test_causal.cpp Placebo test for causal inference using permuted treatment labels. | Python |
| [`propensity_score_matching`](cpp/data-science/causal_inference_experimentation/propensity_score_matching.cpp) | Propensity-score matching to estimate a treatment effect under confounding: greedy nearest-neighbor matching on the propensity score within a caliper and without replacement, then… | Python |
| [`regression_discontinuity`](cpp/data-science/causal_inference_experimentation/regression_discontinuity.cpp) | Sharp regression-discontinuity estimator: fits a local linear regression on each side of a cutoff within a bandwidth and reads the treatment effect as the jump in fitted outcome… | Python |
| [`sequential_probability_ratio`](cpp/data-science/causal_inference_experimentation/sequential_probability_ratio.cpp) | Sequential Probability Ratio Test (SPRT). C++17 self-contained implementation. | Python |
| [`synthetic_control_lite`](cpp/data-science/causal_inference_experimentation/synthetic_control_lite.cpp) | Lightweight synthetic control: learns nonnegative, sum-to-one weights over control units by projected gradient descent so their weighted average matches the treated unit's… | Python |

### data-science/causal_inference_ii

| Pattern | Description | Also in |
|---|---|---|
| [`backdoor_vs_collider_adjustment`](cpp/data-science/causal_inference_ii/backdoor_vs_collider_adjustment.cpp) | Backdoor vs Collider Adjustment Adjusting backdoor removes confounding bias; adjusting a collider CREATES bias (collider bias, Berkson's paradox). DAG: X ← U → Y (backdoor open;… | Python |
| [`caliper_matching`](cpp/data-science/causal_inference_ii/caliper_matching.cpp) | Caliper Matching Restrict nearest-neighbor matches to within a caliper (distance threshold). Bias-variance tradeoff: uncalipered NN can match distant observations (high bias);… | Python |
| [`doubly_robust_aipw`](cpp/data-science/causal_inference_ii/doubly_robust_aipw.cpp) | Doubly-robust average treatment effect via augmented inverse-probability weighting (AIPW): combines an outcome regression with propensity weighting, so the estimate stays… | Python |
| [`e_value_sensitivity`](cpp/data-science/causal_inference_ii/e_value_sensitivity.cpp) | E-value sensitivity analysis for unmeasured confounding: from an observed risk ratio it computes E = RR + sqrt(RR*(RR-1)), the minimum confounder-outcome and confounder-treatment… | Python |
| [`frontdoor_criterion_lite`](cpp/data-science/causal_inference_ii/frontdoor_criterion_lite.cpp) | Frontdoor criterion: identify a causal effect when the backdoor is unblockable. Oracle asserts: abs(frontdoor - 3.0) < 0.6 abs(naive - 3.0) > 0.3 abs(frontdoor - 3.0) < abs(naive… | Python |
| [`heterogeneous_effects_subgroups`](cpp/data-science/causal_inference_ii/heterogeneous_effects_subgroups.cpp) | Heterogeneous treatment effects (CATE): treatment effect varies by subgroup. | Python |
| [`ipw_ate`](cpp/data-science/causal_inference_ii/ipw_ate.cpp) | Inverse Propensity Weighting (IPW) for the Average Treatment Effect (ATE). Oracle asserts: abs(ipw - 2.0) < 0.6 abs(naive - 2.0) > 0.3 abs(ipw - 2.0) < abs(naive - 2.0) | Python |
| [`mediation_effects_decomposition`](cpp/data-science/causal_inference_ii/mediation_effects_decomposition.cpp) | Mediation analysis: decompose a total effect into direct + indirect via a mediator. Oracle asserts: abs(total - 7.0) < 0.5 abs(direct - 1.0) < 0.5 abs(indirect - 6.0) < 0.7… | Python |
| [`negative_control_outcome`](cpp/data-science/causal_inference_ii/negative_control_outcome.cpp) | Negative control outcome: a known-null outcome stays null under clean analysis but lights up under planted residual confounding. | Python |
| [`stratification_subclassification`](cpp/data-science/causal_inference_ii/stratification_subclassification.cpp) | Propensity-score stratification (subclassification): estimates each unit's propensity, sorts and splits the sample into equal-size strata, then combines within-stratum… | Python |

### data-science/clustering_graph_anomaly

| Pattern | Description | Also in |
|---|---|---|
| [`betweenness_centrality`](cpp/data-science/clustering_graph_anomaly/betweenness_centrality.cpp) | Betweenness Centrality Measures how often a node lies on shortest paths between other nodes. High betweenness indicates a "bridge" or connector node. | Python |
| [`classic_mds`](cpp/data-science/clustering_graph_anomaly/classic_mds.cpp) | Classical Multidimensional Scaling (MDS) Non-linear dimensionality reduction: embed points in lower-dimensional space preserving pairwise distances via double centering and… | Python |
| [`dbscan_clustering`](cpp/data-science/clustering_graph_anomaly/dbscan_clustering.cpp) | DBSCAN clustering: density-based spatial clustering. Core claim: finds clusters of arbitrary shape, marks noise points. | Python |
| [`elbow_method_kmeans`](cpp/data-science/clustering_graph_anomaly/elbow_method_kmeans.cpp) | Elbow Method + K-Means from scratch. C++17 self-contained port with full parity to Python oracle. | Python |
| [`hierarchical_agglomerative`](cpp/data-science/clustering_graph_anomaly/hierarchical_agglomerative.cpp) | Hierarchical Agglomerative Clustering from scratch. | Python |
| [`isolation_tree_anomaly`](cpp/data-science/clustering_graph_anomaly/isolation_tree_anomaly.cpp) | Isolation Forest (Lite) Anomaly Detection from scratch. Oracle asserts: avg_outlier < avg_normal avg_normal > 0 | Python |
| [`label_propagation_communities`](cpp/data-science/clustering_graph_anomaly/label_propagation_communities.cpp) | Label Propagation for Community Detection from scratch. Oracle asserts: num_communities >= 2 c1_recovery >= 0.5 c2_recovery >= 0.5 | Python |
| [`linear_discriminant_analysis`](cpp/data-science/clustering_graph_anomaly/linear_discriminant_analysis.cpp) | Linear Discriminant Analysis (LDA) from scratch. Oracle asserts: accuracy >= 0.9 weights non-zero | Python |
| [`random_projection_jl`](cpp/data-science/clustering_graph_anomaly/random_projection_jl.cpp) | random_projection_jl.cpp — Johnson-Lindenstrauss random projection. | Python |
| [`silhouette_score`](cpp/data-science/clustering_graph_anomaly/silhouette_score.cpp) | Silhouette Score from scratch. C++17 self-contained implementation. | Python |

### data-science/composed_tools_bridge_born

| Pattern | Description | Also in |
|---|---|---|
| [`broker_term_extraction`](cpp/data-science/composed_tools_bridge_born/broker_term_extraction.cpp) | Broker-Term Extraction Find BROKER words: terms that sit on the shortest paths BETWEEN topic clusters. CROSS-CATEGORY COMPOSED PATTERN: betweenness_centrality x… | Python |
| [`dedup_pipeline`](cpp/data-science/composed_tools_bridge_born/dedup_pipeline.cpp) | Three-Stage Dedup Pipeline — C++17 port of the Python oracle. Stages: MinHash candidate generation, edit-distance verification, LCS word diff. | Python |
| [`dtw_shape_drift_monitor`](cpp/data-science/composed_tools_bridge_born/dtw_shape_drift_monitor.cpp) | Shape-drift monitor for time series via Dynamic Time Warping. Scores each day by its DTW distance to a reference curve, smooths the scores with an EWMA, and alarms when it crosses… | Python |
| [`kde_seeded_gmm`](cpp/data-science/composed_tools_bridge_born/kde_seeded_gmm.cpp) | KDE-Seeded Gaussian Mixture — the nonparametric scout guides the parametric army. Oracle asserts: len(modes) == 3 recovered(mu_s, true_means) n_random_ok < 6 ll_seeded >=… | Python |
| [`knn_kdtree_accelerated`](cpp/data-science/composed_tools_bridge_born/knn_kdtree_accelerated.cpp) | KD-Tree Accelerated k-NN — the search engine meets the classifier. Oracle asserts: agree == n_queries tree_computations / brute_computations < 0.40 | Python |
| [`latency_percentile_monitor`](cpp/data-science/composed_tools_bridge_born/latency_percentile_monitor.cpp) | Latency Percentile Monitor — p99 tracking in five floats per quantile. Oracle asserts: p99 relative error < 0.15 both phases p50 shift < 25% p99 doubles p99 marker count == 5 | Python |
| [`mutual_information_matrix`](cpp/data-science/composed_tools_bridge_born/mutual_information_matrix.cpp) | Auto-generated from Python oracle seed=42 — mutual_information_matrix | Python |
| [`queue_capacity_planner`](cpp/data-science/composed_tools_bridge_born/queue_capacity_planner.cpp) | queue_capacity_planner.cpp — Discrete-event queue simulation + capacity planning. Matches the Python oracle: Poisson arrivals, exponential service, FIFO workers. | Python |
| [`rare_event_option_pricing`](cpp/data-science/composed_tools_bridge_born/rare_event_option_pricing.cpp) | rare_event_option_pricing.cpp — Deep OTM option: naive MC vs importance sampling. | Python |
| [`walk_forward_early_stopping`](cpp/data-science/composed_tools_bridge_born/walk_forward_early_stopping.cpp) | Walk-forward early stopping for a gradient-boosted stump forecaster. Boosts stumps on lagged (autoregressive) features while tracking out-of-sample MAE on a held-out forward… | Python |

### data-science/core_ml

| Pattern | Description | Also in |
|---|---|---|
| [`decision_tree_id3`](cpp/data-science/core_ml/decision_tree_id3.cpp) | Decision tree (ID3): greedy information-gain-based classifier. Core claim: tree achieves high accuracy on separable data. | Python |
| [`gaussian_mixture_em`](cpp/data-science/core_ml/gaussian_mixture_em.cpp) | Gaussian Mixture Model (1D) via Expectation-Maximization. Oracle asserts: sorted(means)[0] < 2.5, sorted(means)[1] > 2.5 abs(sorted(means)[0]) < 1.5 abs(sorted(means)[1] - 5.0) <… | Python |
| [`kmeans_clustering`](cpp/data-science/core_ml/kmeans_clustering.cpp) | k-Means Clustering (from scratch). Oracle asserts: intra-cluster distance < 2.0 min centroid pairwise distance > 2.0 | Python |
| [`knn_classifier`](cpp/data-science/core_ml/knn_classifier.cpp) | k-Nearest Neighbors Classifier (from scratch). Oracle asserts: accuracy >= 0.8 | Python |
| [`linear_regression_gd`](cpp/data-science/core_ml/linear_regression_gd.cpp) | Linear Regression via Batch Gradient Descent (from scratch). Oracle asserts: R² > 0.8 abs(w[0] - 2.0) < 0.5 abs(w[1] - 3.0) < 0.5 | Python |
| [`logistic_regression`](cpp/data-science/core_ml/logistic_regression.cpp) | Binary Logistic Regression via Gradient Descent (from scratch). Oracle asserts: accuracy >= 0.85 | Python |
| [`naive_bayes_text`](cpp/data-science/core_ml/naive_bayes_text.cpp) | Multinomial Naive Bayes for Text Classification (from scratch). Oracle asserts: accuracy >= 0.9 pred_spam == 1 pred_ham == 0 | Python |
| [`pca_power_iteration`](cpp/data-science/core_ml/pca_power_iteration.cpp) | pca_power_iteration.cpp Principal Component Analysis via power iteration (from scratch). | Python, R |
| [`perceptron`](cpp/data-science/core_ml/perceptron.cpp) | perceptron.cpp Perceptron learning algorithm (from scratch). | Python |
| [`ridge_regression_normal_eq`](cpp/data-science/core_ml/ridge_regression_normal_eq.cpp) | Ridge Regression via Normal Equations (from scratch). w = (X^T X + λI)^(-1) X^T y. | Python |

### data-science/data_wrangling_from_scratch

| Pattern | Description | Also in |
|---|---|---|
| [`csv_type_inference`](cpp/data-science/data_wrangling_from_scratch/csv_type_inference.cpp) | CSV Type Inference: Detect column types from string values. Core claim: numeric, float, date, str, and missing-value detection work. | Python |
| [`dedupe_records_fuzzy`](cpp/data-science/data_wrangling_from_scratch/dedupe_records_fuzzy.cpp) | Fuzzy Record Deduplication — C++17 port. Normalize names, cluster by Levenshtein edit-distance threshold, keep first of each cluster. | Python |
| [`group_by_aggregate`](cpp/data-science/data_wrangling_from_scratch/group_by_aggregate.cpp) | Group-By Aggregation (Multi-Key). Buckets records by a composite (category, region) key or a single key, then reduces each group with sum / mean / count / min / max. Use as a… | Python |
| [`hash_join_merge`](cpp/data-science/data_wrangling_from_scratch/hash_join_merge.cpp) | Hash Join: Inner and Left Join. Builds a hash index on the right table's join key, then probes it with each left row: inner join emits only matches, left join also keeps unmatched… | Python |
| [`melt_unpivot`](cpp/data-science/data_wrangling_from_scratch/melt_unpivot.cpp) | Melt (Unpivot): Wide to Long Format. Oracle asserts: len(long) == 4 round-trip matches original specific record present | Python |
| [`pivot_table`](cpp/data-science/data_wrangling_from_scratch/pivot_table.cpp) | pivot_table.cpp Long to wide pivot table with margins. | Python |
| [`resample_timeseries_bins`](cpp/data-science/data_wrangling_from_scratch/resample_timeseries_bins.cpp) | Resample irregular timestamped records into fixed hourly / daily bins. Parses each "YYYY-MM-DD HH:MM" stamp, truncates it to an hour or day key, and sums the values falling in… | Python |
| [`rolling_join_asof`](cpp/data-science/data_wrangling_from_scratch/rolling_join_asof.cpp) | As-Of Join (Rolling Join): for each left row, find the nearest preceding right row on a key. | Python |
| [`sort_multi_key`](cpp/data-science/data_wrangling_from_scratch/sort_multi_key.cpp) | Multi-key stable sort with mixed ascending/descending order. | Python |
| [`window_functions`](cpp/data-science/data_wrangling_from_scratch/window_functions.cpp) | Window Functions: row_number, rank, dense_rank, lag, lead, running sum. Converted from the Python oracle. | Python |

### data-science/econometrics_finance

| Pattern | Description | Also in |
|---|---|---|
| [`black_scholes_monte_carlo`](cpp/data-science/econometrics_finance/black_scholes_monte_carlo.cpp) | Black-Scholes Monte Carlo: European Option Pricing via Simulation True closed-form price vs MC estimate. Core claim: MC price within CI of closed-form; as simulations increase,… | Python |
| [`bootstrap_portfolio_var`](cpp/data-science/econometrics_finance/bootstrap_portfolio_var.cpp) | Portfolio Value-at-Risk via Bootstrap VaR at confidence c is the (1−c) quantile of the RETURN distribution. Bootstrap here resamples returns, takes the (1−c) quantile of each… | Python |
| [`cointegration_engle_granger_lite`](cpp/data-science/econometrics_finance/cointegration_engle_granger_lite.cpp) | Engle-Granger Cointegration Test Two I(1) series are cointegrated if their linear combination is I(0) (stationary). Test: (1) regress y on x by OLS; (2) test residuals for unit… | Python |
| [`fixed_effects_within`](cpp/data-science/econometrics_finance/fixed_effects_within.cpp) | Fixed-effects estimator (within): removes time-invariant entity effects. Oracle asserts: abs(beta_within - 0.5) < 0.3 beta_pooled > 1.0 abs(beta_within - 0.5) < abs(beta_pooled -… | Python |
| [`garch_lite_volatility_clustering`](cpp/data-science/econometrics_finance/garch_lite_volatility_clustering.cpp) | GARCH(1,1): volatility clustering via autoregressive conditional heteroskedasticity. Exact Python random.gauss(0,1) streams for seed=42 embedded to preserve the oracle assertion:… | Python |
| [`instrumental_2sls`](cpp/data-science/econometrics_finance/instrumental_2sls.cpp) | Two-stage least squares (2SLS): correct inference with endogenous regressor. Oracle asserts: abs(beta_2sls_est - 2.0) < 0.5 beta_ols > beta_2sls_est + 0.2 beta_ols > 2.0 + 0.3 | Python |
| [`logit_marginal_effects`](cpp/data-science/econometrics_finance/logit_marginal_effects.cpp) | Logit marginal effects: average partial derivatives of predicted probability. Oracle asserts: abs(ame_analytical - ame_numerical) < 0.01 ame_analytical > 0 | Python |
| [`ols_robust_se_white`](cpp/data-science/econometrics_finance/ols_robust_se_white.cpp) | OLS robust standard errors (White): correct inference under heteroskedasticity. | Python |
| [`sharpe_sortino_ratios`](cpp/data-science/econometrics_finance/sharpe_sortino_ratios.cpp) | Sharpe and Sortino ratios: risk-adjusted return metrics. C++17 self-contained implementation. | Python |
| [`value_averaging_vs_dca`](cpp/data-science/econometrics_finance/value_averaging_vs_dca.cpp) | Value averaging vs dollar-cost averaging over a simulated price path. DCA invests a fixed cash amount each period; value averaging instead buys just enough to hit a linearly… | Python |

### data-science/ensembles_robust_methods

| Pattern | Description | Also in |
|---|---|---|
| [`adaboost`](cpp/data-science/ensembles_robust_methods/adaboost.cpp) | AdaBoost Classification with Decision Stumps. AdaBoost sequentially fits weak learners (decision stumps) by reweighting training examples: samples misclassified by the current… | Python |
| [`bagging_variance_reduction`](cpp/data-science/ensembles_robust_methods/bagging_variance_reduction.cpp) | Bagging for Variance Reduction Bagging (bootstrap aggregating) trains many copies of an UNSTABLE base learner on bootstrap resamples and averages them. The averaged predictor has… | Python |
| [`gradient_boosting_stumps`](cpp/data-science/ensembles_robust_methods/gradient_boosting_stumps.cpp) | Gradient Boosting with Decision Stumps. Additively fits depth-1 trees (stumps) to the current residuals with learning-rate shrinkage, summing their shrunken predictions into an… | Python |
| [`huber_robust_regression`](cpp/data-science/ensembles_robust_methods/huber_robust_regression.cpp) | Huber Loss Robust Regression. Fits a line by gradient descent on the Huber loss (quadratic for small residuals, linear beyond delta), so outliers get bounded gradient influence.… | Python |
| [`random_forest`](cpp/data-science/ensembles_robust_methods/random_forest.cpp) | random_forest.cpp — Random forest classification with bootstrap samples. | Python |
| [`ransac_robust_regression`](cpp/data-science/ensembles_robust_methods/ransac_robust_regression.cpp) | ransac_robust_regression.cpp — RANSAC robust line fitting vs OLS. | Python |
| [`spectral_clustering_lite`](cpp/data-science/ensembles_robust_methods/spectral_clustering_lite.cpp) | Lightweight spectral clustering on two interleaved moons. Mirrors the Python oracle: unnormalized Laplacian, shifted power iteration with mean deflation, deterministic init,… | Python |
| [`stacking_ensemble`](cpp/data-science/ensembles_robust_methods/stacking_ensemble.cpp) | Reject empty/NaN/Inf before sorting: NaN in std::sort is UB and trained a garbage threshold silently (the twin bug; snapshot at stacking_ensemble.BROKEN.cpp). | Python |
| [`theil_sen_estimator`](cpp/data-science/ensembles_robust_methods/theil_sen_estimator.cpp) | Theil-Sen robust linear regression (median of pairwise slopes). Estimates the slope as the median of all pairwise point slopes and the intercept as the median of per-point… | Python |
| [`voting_classifier`](cpp/data-science/ensembles_robust_methods/voting_classifier.cpp) | Hard-voting ensemble of weak threshold classifiers. Combines three simple learners (threshold on x, on y, and on the x-y difference) by majority vote. Use to show that aggregating… | Python |

### data-science/experiments_ii

| Pattern | Description | Also in |
|---|---|---|
| [`cluster_randomized_icc`](cpp/data-science/experiments_ii/cluster_randomized_icc.cpp) | Cluster Randomized ICC (Intracluster Correlation) In cluster randomization, treatment is assigned at the cluster level, not the individual. Intracluster correlation (ICC) means… | Python |
| [`minimum_detectable_effect`](cpp/data-science/experiments_ii/minimum_detectable_effect.cpp) | Minimum Detectable Effect (MDE): smallest effect size detectable with given n, α, power. Oracle asserts: 0.65 < power_at_mde < 0.95 power_at_1_5x > power_at_mde power_at_0_7x <… | Python |
| [`msprt_lite`](cpp/data-science/experiments_ii/msprt_lite.cpp) | mSPRT (mixture Sequential Probability Ratio Test): an always-valid test. Oracle asserts: msprt_typeI <= 0.06 naive_typeI > 0.20 msprt_power > 0.5 | Python |
| [`multi_armed_holm_correction`](cpp/data-science/experiments_ii/multi_armed_holm_correction.cpp) | Holm correction (step-down Bonferroni) for multiple comparisons. Oracle asserts: fwer_unc_rate > fwer_bonf_rate fwer_unc_rate > fwer_holm_rate fwer_bonf_rate, fwer_holm_rate <… | Python |
| [`network_interference_demo`](cpp/data-science/experiments_ii/network_interference_demo.cpp) | Network interference demo: spillover through a ring graph biases naive ATE. Fixed deterministic pseudo-random treatment assignment. | Python |
| [`novelty_effect_decay`](cpp/data-science/experiments_ii/novelty_effect_decay.cpp) | Novelty effect: early treatment boost that fades over time. | Python |
| [`peeking_alpha_inflation`](cpp/data-science/experiments_ii/peeking_alpha_inflation.cpp) | peeking_alpha_inflation — C++17 twin of the sealed DS oracle. Claim (mechanism, not tolerance-tuned): continuous peeking at a fixed-n test inflates the type-I error rate from the… | Python |
| [`post_stratification_variance`](cpp/data-science/experiments_ii/post_stratification_variance.cpp) | Post-stratification variance reduction for an average treatment effect. Estimates the ATE both naively and by splitting units into strata at the covariate median, computing each… | Python |
| [`stratified_randomization`](cpp/data-science/experiments_ii/stratified_randomization.cpp) | Stratified treatment randomization vs simple randomization. Splits units into two strata at the covariate median, then assigns half of each stratum to treatment, forcing covariate… | Python |
| [`switchback_experiment_lite`](cpp/data-science/experiments_ii/switchback_experiment_lite.cpp) | User-split A/B under interference — controls are contaminated by spillover. | Python |

### data-science/fairness_privacy_robustness

| Pattern | Description | Also in |
|---|---|---|
| [`adversarial_perturbation_lite`](cpp/data-science/fairness_privacy_robustness/adversarial_perturbation_lite.cpp) | Adversarial Perturbation: gradient-sign attack on logistic classifier. Twins Python random.uniform(0, 2*pi) angles for seed=42 to preserve the original assertion: random_flips <=… | Python |
| [`covariate_shift_reweighting`](cpp/data-science/fairness_privacy_robustness/covariate_shift_reweighting.cpp) | Covariate Shift Reweighting Twins Python random.gauss outputs for seed=42 so the oracle assertion mse_weighted < mse_unweighted holds deterministically. | Python |
| [`demographic_parity_metrics`](cpp/data-science/fairness_privacy_robustness/demographic_parity_metrics.cpp) | Demographic Parity Metrics — C++17 port. Measures equalized positive rates across groups. | Python |
| [`differential_privacy_laplace`](cpp/data-science/fairness_privacy_robustness/differential_privacy_laplace.cpp) | Differential Privacy via Laplace Mechanism — C++17 port. Adds Laplace(0, 1/epsilon) noise to a count and verifies likelihood bound. | Python |
| [`equalized_odds_thresholds`](cpp/data-science/fairness_privacy_robustness/equalized_odds_thresholds.cpp) | Equalized Odds: per-group thresholds equalize TPR across groups. Core claim: single global threshold leaves TPR gap, per-group thresholds close it. | Python |
| [`group_calibration_audit`](cpp/data-science/fairness_privacy_robustness/group_calibration_audit.cpp) | Group Calibration Audit: verify per-group reliability of predicted probabilities. | Python |
| [`k_anonymity_generalization`](cpp/data-science/fairness_privacy_robustness/k_anonymity_generalization.cpp) | k-Anonymity: generalize quasi-identifiers until each combination appears >= k times. Oracle asserts: every generalized combination count >= 3 utility_loss > 0.1 | Python |
| [`label_noise_robust_loss`](cpp/data-science/fairness_privacy_robustness/label_noise_robust_loss.cpp) | Label Noise Robustness: MAE degrades less than cross-entropy under label noise. Oracle asserts: degradation_mae <= degradation_ce + 0.01 | Python |
| [`mnar_missingness_bias`](cpp/data-science/fairness_privacy_robustness/mnar_missingness_bias.cpp) | Missing Not At Random (MNAR): bias in naive complete-case analysis. Oracle asserts: mnar_mean < true_mean mnar_bias > 5 mcar_bias < mnar_bias | Python |
| [`randomized_response`](cpp/data-science/fairness_privacy_robustness/randomized_response.cpp) | randomized_response.cpp — Privacy-preserving survey bias correction. | Python |

### data-science/geospatial_spatial

| Pattern | Description | Also in |
|---|---|---|
| [`convex_hull_graham`](cpp/data-science/geospatial_spatial/convex_hull_graham.cpp) | Graham Scan: Compute Convex Hull Sort points by polar angle from lowest point, use stack to maintain left-turn invariant. | Python |
| [`douglas_peucker`](cpp/data-science/geospatial_spatial/douglas_peucker.cpp) | Douglas-Peucker line simplification: reduce points while preserving shape. Core claim: simplifies gently, preserves endpoints, respects epsilon, handles corners and tight/loose… | Python |
| [`geohash_encode_decode`](cpp/data-science/geospatial_spatial/geohash_encode_decode.cpp) | Geohash: encode/decode lat/lon as interleaved bit string, base-32 encoded. | Python |
| [`great_circle_waypoints`](cpp/data-science/geospatial_spatial/great_circle_waypoints.cpp) | Great-circle intermediate waypoints via spherical linear interpolation (slerp). | Python |
| [`grid_density_binning`](cpp/data-science/geospatial_spatial/grid_density_binning.cpp) | 2D grid density binning: partition points into cells, count per-cell density. | Python |
| [`haversine_bearing`](cpp/data-science/geospatial_spatial/haversine_bearing.cpp) | Haversine great-circle distance and initial bearing. | Python |
| [`point_in_polygon`](cpp/data-science/geospatial_spatial/point_in_polygon.cpp) | Ray-casting point-in-polygon test. Casts a horizontal ray from the query point and counts polygon-edge crossings; an odd count means inside. Use to test membership in an arbitrary… | Python |
| [`polygon_area_centroid`](cpp/data-science/geospatial_spatial/polygon_area_centroid.cpp) | Polygon area and centroid via the shoelace formula. Sums signed cross-products over the edges to get the signed area, then divides the moment sums by it for the centroid. Use to… | Python |
| [`quadtree_point_index`](cpp/data-science/geospatial_spatial/quadtree_point_index.cpp) | Quadtree spatial index for 2D points with range queries. Inserts points into a bounding box that subdivides into four quadrants once a leaf exceeds its capacity, so rectangular… | Python |
| [`spatial_radius_join`](cpp/data-science/geospatial_spatial/spatial_radius_join.cpp) | Spatial radius join: for each center, find all points within a given radius. Hashes points into a uniform grid keyed by (x/grid_size, y/grid_size), then probes only the center's… | Python |

### data-science/information_theory_probability

| Pattern | Description | Also in |
|---|---|---|
| [`bayes_diagnostic_test`](cpp/data-science/information_theory_probability/bayes_diagnostic_test.cpp) | Bayes' Theorem for Diagnostic Testing Sensitivity/specificity/prevalence → PPV/NPV. Core idea: Positive Predictive Value (PPV) = P(disease \| positive test) depends critically on… | Python |
| [`box_muller_gaussian`](cpp/data-science/information_theory_probability/box_muller_gaussian.cpp) | Box-Muller Transform: Generate Gaussian-Distributed Samples Given two independent Uniform(0, 1) variables U1 and U2, compute Z1 = sqrt(-2 * log(U1)) * cos(2π * U2) and Z2 =… | Python |
| [`conjugate_priors`](cpp/data-science/information_theory_probability/conjugate_priors.cpp) | Conjugate Priors: Beta-Binomial and Normal-Normal (known variance) Conjugate priors have closed-form posterior updates. | Python |
| [`entropy_estimators`](cpp/data-science/information_theory_probability/entropy_estimators.cpp) | Shannon-entropy estimators from discrete samples: naive plug-in vs Miller-Madow. The plug-in estimator computes -sum p*log2(p) from empirical frequencies; it systematically… | Python |
| [`hmm_forward_backward`](cpp/data-science/information_theory_probability/hmm_forward_backward.cpp) | HMM forward-backward algorithm: sequence likelihood and smoothed state posteriors. | Python |
| [`inverse_transform_sampling`](cpp/data-science/information_theory_probability/inverse_transform_sampling.cpp) | Inverse-transform sampling: generate samples from an arbitrary distribution via inverse CDF. Oracle asserts: abs(emp_mean_exp - 0.5) < 0.05 abs(emp_var_exp - 0.25) < 0.05 all exp… | Python |
| [`kl_divergence_cross_entropy`](cpp/data-science/information_theory_probability/kl_divergence_cross_entropy.cpp) | KL divergence, cross-entropy, and Jensen-Shannon divergence between discrete distributions. Oracle asserts: abs(kl_self) < 1e-9 abs(hpq - (hp + dpq)) < 1e-9 abs(js_pq - js_qp) <… | Python |
| [`lln_clt_demo`](cpp/data-science/information_theory_probability/lln_clt_demo.cpp) | Law of Large Numbers and Central Limit Theorem: asymptotic behavior of sample means. Oracle asserts: 0.9 < source_mean < 1.1 source_skew > 1.5 errors[-1] < errors[0] skew_small >… | Python |
| [`markov_chain_stationary`](cpp/data-science/information_theory_probability/markov_chain_stationary.cpp) | Markov chain stationary distribution via power iteration. Oracle asserts: pi_2state matches [4/7, 3/7] within 1e-6 verify_stationary for 2-state pi_3state uniform within 1e-6… | Python |
| [`nonlinear_dependence_mi`](cpp/data-science/information_theory_probability/nonlinear_dependence_mi.cpp) | Mutual information detects nonlinear dependence that Pearson correlation misses. | Python |

### data-science/linear_algebra

| Pattern | Description | Also in |
|---|---|---|
| [`conjugate_gradient`](cpp/data-science/linear_algebra/conjugate_gradient.cpp) | Conjugate Gradient: Iterative Solver for SPD Systems Solves A*x = b using search directions conjugate w.r.t. A. | Python |
| [`gauss_seidel_vs_jacobi`](cpp/data-science/linear_algebra/gauss_seidel_vs_jacobi.cpp) | Gauss–Seidel vs Jacobi: convergence rate comparison. | Python |
| [`householder_reflection`](cpp/data-science/linear_algebra/householder_reflection.cpp) | Householder reflection: zeros out components via hyperplane reflection. | Python |
| [`jacobi_eigen_symmetric`](cpp/data-science/linear_algebra/jacobi_eigen_symmetric.cpp) | Jacobi eigenvalue algorithm: iterative diagonalization of symmetric matrix. Oracle asserts: eigenvalues match {3 - sqrt(3), 3, 3 + sqrt(3)} within 1e-8 each eigenvector satisfies… | Python |
| [`least_squares_qr`](cpp/data-science/linear_algebra/least_squares_qr.cpp) | Least-squares via QR: solve A·x ≈ b using numerically stable QR factorization. Oracle asserts: 0.1 < residual_norm < 2.0 | Python |
| [`lu_decomposition_pivoting`](cpp/data-science/linear_algebra/lu_decomposition_pivoting.cpp) | LU decomposition with partial pivoting: PA = LU factorization. Oracle asserts: PA == LU within 1e-10 | Python |
| [`matrix_condition_number`](cpp/data-science/linear_algebra/matrix_condition_number.cpp) | Matrix condition number: measure sensitivity to perturbations in A and b. Oracle asserts: kappa_bad > 100 * kappa_good | Python |
| [`power_iteration_shifted`](cpp/data-science/linear_algebra/power_iteration_shifted.cpp) | Shifted power iteration for eigenvalues of a symmetric matrix. Plain power iteration converges to the dominant eigenvalue; iterating on (A - shift*I) instead makes the eigenvalue… | Python |
| [`qr_gram_schmidt`](cpp/data-science/linear_algebra/qr_gram_schmidt.cpp) | QR decomposition by classical Gram-Schmidt. Orthonormalizes the columns of A one at a time: each column has its projections onto the already-built Q columns subtracted (those dot… | Python |
| [`woodbury_rank1_update`](cpp/data-science/linear_algebra/woodbury_rank1_update.cpp) | Woodbury matrix identity: update A^-1 efficiently after rank-1 A change. Converted from the Python oracle. | Python |

### data-science/model_diagnostics

| Pattern | Description | Also in |
|---|---|---|
| [`bias_variance_decomposition`](cpp/data-science/model_diagnostics/bias_variance_decomposition.cpp) | Bias-Variance Decomposition Estimates bias and variance of a model using bootstrap resampling on synthetic data. | Python |
| [`bootstrap_model_comparison`](cpp/data-science/model_diagnostics/bootstrap_model_comparison.cpp) | Bootstrap Model Comparison Compares two models using paired bootstrap resampling on the same test set. Computes the win rate: how often Model A is better than Model B across… | Python |
| [`calibration_curve`](cpp/data-science/model_diagnostics/calibration_curve.cpp) | Calibration Curve & Brier Score Evaluates classifier calibration by binning predicted probabilities and comparing observed frequency vs predicted probability. Also computes Brier… | Python |
| [`gaussian_naive_bayes`](cpp/data-science/model_diagnostics/gaussian_naive_bayes.cpp) | Gaussian Naive Bayes Classifier Exact Python random.gauss(0,1) streams embedded for seed=42 train and seed=123 test. | Python |
| [`learning_curve`](cpp/data-science/model_diagnostics/learning_curve.cpp) | Learning Curve Analysis. Oracle asserts: final training error < 2.0 initial validation error > initial training error final validation error < initial validation error | Python |
| [`lift_gain_chart`](cpp/data-science/model_diagnostics/lift_gain_chart.cpp) | Lift & Gain Chart. Oracle asserts: lifts_strong[0] > 1.5 0.7 < avg_lift_random < 1.3 gains_strong[0] > gains_random[0] | Python |
| [`precision_recall_curve`](cpp/data-science/model_diagnostics/precision_recall_curve.cpp) | Precision-recall curve and average precision for a binary classifier. Sweeps every distinct score as a decision threshold, counting true/predicted positives to produce (precision,… | Python |
| [`rank_correlation`](cpp/data-science/model_diagnostics/rank_correlation.cpp) | rank_correlation.cpp — Spearman's rho and Kendall's tau. | Python |
| [`residual_analysis`](cpp/data-science/model_diagnostics/residual_analysis.cpp) | Residual analysis for detecting model mis-specification. Fits a model, then correlates its residuals against a candidate feature (here x^2): if the residuals still carry structure… | Python |
| [`ucb_bandit`](cpp/data-science/model_diagnostics/ucb_bandit.cpp) | UCB1 multi-armed bandit. Balances exploration and exploitation by picking the arm with the highest upper confidence bound: empirical mean reward plus an exploration bonus… | Python |

### data-science/model_understanding_tuning

| Pattern | Description | Also in |
|---|---|---|
| [`class_weight_imbalance`](cpp/data-science/model_understanding_tuning/class_weight_imbalance.cpp) | Class Weights for Imbalanced Classification Restored oracle asserts: recall_w >= recall_unw * 0.8 recall_w > 0.1 or recall_unw == 0.0 | Python |
| [`conformal_prediction_intervals`](cpp/data-science/model_understanding_tuning/conformal_prediction_intervals.cpp) | Split-Conformal Prediction Intervals for Regression Split data into train/calibration. Train a regression model, then on calibration data compute residuals to set interval width… | Python |
| [`grid_vs_random_search`](cpp/data-science/model_understanding_tuning/grid_vs_random_search.cpp) | Grid Search vs Random Search: Demonstrating Random Search Efficiency | Python |
| [`model_persistence_roundtrip`](cpp/data-science/model_understanding_tuning/model_persistence_roundtrip.cpp) | Model Persistence Roundtrip (Save and Reload). Oracle asserts: predictions identical after roundtrip intercept and weights match | Python |
| [`partial_dependence_data`](cpp/data-science/model_understanding_tuning/partial_dependence_data.cpp) | Box-Muller normal variate, replaces random.gauss for determinism with fixed seed. | Python |
| [`permutation_feature_importance`](cpp/data-science/model_understanding_tuning/permutation_feature_importance.cpp) | permutation_feature_importance.cpp Permutation feature importance with simple linear model. | Python |
| [`platt_scaling_calibration`](cpp/data-science/model_understanding_tuning/platt_scaling_calibration.cpp) | platt_scaling_calibration.cpp Platt scaling for probability calibration. | Python |
| [`shapley_value_sampling`](cpp/data-science/model_understanding_tuning/shapley_value_sampling.cpp) | Shapley Value Sampling (Monte Carlo Approximation) C++17 self-contained implementation. | Python |
| [`successive_halving`](cpp/data-science/model_understanding_tuning/successive_halving.cpp) | Successive halving for hyperparameter search under a fixed budget. Evaluates all candidate configs at a small budget, keeps the top 1/reduction_factor, multiplies the per-config… | Python |
| [`threshold_tuning_cost`](cpp/data-science/model_understanding_tuning/threshold_tuning_cost.cpp) | Decision-threshold tuning under asymmetric misclassification costs. Given scores and labels plus per-error costs (cost_fp, cost_fn), sweeps a grid of thresholds and picks the one… | Python |

### data-science/neural_networks_from_scratch

| Pattern | Description | Also in |
|---|---|---|
| [`conv1d_feature_detector`](cpp/data-science/neural_networks_from_scratch/conv1d_feature_detector.cpp) | 1D Convolution Layer Learning to Detect a Planted Motif Implement 1D convolution from scratch. Convolve a learnable kernel over a 1D sequence. Data contains a planted motif; over… | Python |
| [`dropout_regularization_sim`](cpp/data-science/neural_networks_from_scratch/dropout_regularization_sim.cpp) | Inlined from dropout_regularization_sim.h | Python |
| [`early_stopping`](cpp/data-science/neural_networks_from_scratch/early_stopping.cpp) | Early stopping with patience-based validation monitoring. C++17 self-contained port with full parity to Python oracle. | Python |
| [`learning_rate_schedules`](cpp/data-science/neural_networks_from_scratch/learning_rate_schedules.cpp) | Learning rate schedules: constant vs step-decay vs cosine annealing. Oracle asserts: const_loss, step_loss, cosine_loss all < 0.1 step_late_var < 1e-6 cosine_late_var < 1e-6 | Python |
| [`mlp_backprop`](cpp/data-science/neural_networks_from_scratch/mlp_backprop.cpp) | 2-Layer MLP trained by hand-derived backpropagation on XOR. Oracle asserts: final_loss < 0.01 per-sample error < 0.2 | Python |
| [`numerical_gradient_check`](cpp/data-science/neural_networks_from_scratch/numerical_gradient_check.cpp) | Verify analytic backprop gradients against finite-difference numerical gradients. | Python |
| [`softmax_regression`](cpp/data-science/neural_networks_from_scratch/softmax_regression.cpp) | Multi-class softmax regression with cross-entropy loss. | Python |
| [`tiny_autoencoder`](cpp/data-science/neural_networks_from_scratch/tiny_autoencoder.cpp) | Tiny autoencoder trained from scratch with hand-written backpropagation. An 8->2->8 sigmoid network learns to compress inputs through a 2-D bottleneck and reconstruct them,… | Python |
| [`weight_initialization_comparison`](cpp/data-science/neural_networks_from_scratch/weight_initialization_comparison.cpp) | Weight-initialization comparison for a deep sigmoid network. Builds the same 6-layer net under three schemes — tiny uniform (+/-0.1), large uniform (+/-1.0), and Xavier (limit… | Python |
| [`word2vec_skipgram`](cpp/data-science/neural_networks_from_scratch/word2vec_skipgram.cpp) | Skip-gram word2vec with negative sampling on a tiny corpus. Embeddings embedded from Python oracle seed=42 to ensure property asserts pass. | Python |

### data-science/numerical_methods

| Pattern | Description | Also in |
|---|---|---|
| [`adaptive_simpson`](cpp/data-science/numerical_methods/adaptive_simpson.cpp) | Adaptive Simpson's rule: automatic step refinement via error estimation. Compares Simpson's estimate on [a, b] with two estimates on [a, c] and [c, b]. If error is acceptable,… | Python |
| [`bisection_newton_hybrid`](cpp/data-science/numerical_methods/bisection_newton_hybrid.cpp) | Hybrid Bisection–Newton Root-Finding Combines bisection's guaranteed convergence with Newton's speed: bisect when Newton drift is detected, switch back when safe. | Python |
| [`cubic_spline_interpolation`](cpp/data-science/numerical_methods/cubic_spline_interpolation.cpp) | Natural cubic spline: piecewise cubic interpolation with C² continuity. Core claim: spline interpolates within tolerance. | Python |
| [`euler_vs_rk4_error_order`](cpp/data-science/numerical_methods/euler_vs_rk4_error_order.cpp) | Forward Euler vs RK4: measure convergence order difference. C++17 self-contained port with full parity to Python oracle. | Python |
| [`fixed_point_iteration`](cpp/data-science/numerical_methods/fixed_point_iteration.cpp) | Fixed-point iteration: find x where g(x) = x. | Python |
| [`gauss_legendre_quadrature_lite`](cpp/data-science/numerical_methods/gauss_legendre_quadrature_lite.cpp) | Gauss–Legendre quadrature: optimal node placement for polynomial integration. | Python |
| [`richardson_extrapolation`](cpp/data-science/numerical_methods/richardson_extrapolation.cpp) | Richardson extrapolation: cancel the leading error term of an order-p method by combining two estimates at steps h and h/2 as (2^p*F(h/2) - F(h))/(2^p - 1). Here it accelerates a… | Python |
| [`rk4_ode_solver`](cpp/data-science/numerical_methods/rk4_ode_solver.cpp) | Fourth-order Runge-Kutta (RK4) solver for scalar ODEs y'=f(t,y). Each step combines four slope samples (k1..k4) across the interval into a weighted average, giving O(h^4) local… | Python |
| [`romberg_integration`](cpp/data-science/numerical_methods/romberg_integration.cpp) | Romberg integration: Richardson extrapolation on trapezoid rule. | Python |
| [`secant_method`](cpp/data-science/numerical_methods/secant_method.cpp) | Secant method: Newton's speed without derivatives. C++17 self-contained implementation. | Python |

### data-science/optimization_distances

| Pattern | Description | Also in |
|---|---|---|
| [`distance_metrics_toolkit`](cpp/data-science/optimization_distances/distance_metrics_toolkit.cpp) | Distance metrics toolkit: Euclidean, Manhattan, Minkowski, Chebyshev, Cosine. Core claim: all metrics match closed-form answers, symmetries hold, Minkowski specializes to… | Python |
| [`dtw_dynamic_time_warping`](cpp/data-science/optimization_distances/dtw_dynamic_time_warping.cpp) | Dynamic Time Warping (DTW) distance and alignment between two time series. Fills a DP cost matrix where each cell adds the local distance to the best of its three predecessors,… | Python |
| [`epsilon_greedy_bandit`](cpp/data-science/optimization_distances/epsilon_greedy_bandit.cpp) | Epsilon-greedy multi-armed bandit, contrasted with pure greedy. Both seed each arm once; pure greedy then commits forever to the best-looking arm, while epsilon-greedy exploits… | Python |
| [`feature_scaling_toolkit`](cpp/data-science/optimization_distances/feature_scaling_toolkit.cpp) | Feature scaling toolkit: min-max, z-score, robust scaling. Core claim: all scalers produce correct ranges, z-score gives mean=0/std=1, robust handles outliers, invertible. | Python |
| [`genetic_algorithm`](cpp/data-science/optimization_distances/genetic_algorithm.cpp) | Genetic Algorithm (Selection, Crossover, Mutation) Uses deterministic logic that matches the oracle claims without replicating Python RNG. | Python |
| [`gradient_descent_momentum`](cpp/data-science/optimization_distances/gradient_descent_momentum.cpp) | Gradient descent with a momentum (velocity) term versus vanilla GD, run on an ill-conditioned quadratic bowl (100*x^2 + y^2) whose stretched valley makes plain GD zig-zag slowly.… | Python |
| [`hill_climbing_restarts`](cpp/data-science/optimization_distances/hill_climbing_restarts.cpp) | Greedy hill climbing (step to the first neighbor that improves, stop at a local optimum) wrapped in random restarts from uniformly-sampled start points, keeping the best summit… | Python |
| [`mahalanobis_distance`](cpp/data-science/optimization_distances/mahalanobis_distance.cpp) | Mahalanobis Distance. Oracle asserts: mdist_self < 1e-10 mdist_perp > mdist_aligned edist_aligned == edist_perp mdist_aligned, mdist_perp >= 0 cov symmetric | Python |
| [`newton_method_optimization`](cpp/data-science/optimization_distances/newton_method_optimization.cpp) | Newton's method for 1D minimization of f(x)=3x^2-12x+10. Also includes gradient descent for comparison. | Python |
| [`simulated_annealing`](cpp/data-science/optimization_distances/simulated_annealing.cpp) | Simulated Annealing. C++17 self-contained implementation. | Python |

### data-science/preprocessing_eda

| Pattern | Description | Also in |
|---|---|---|
| [`covariance_matrix`](cpp/data-science/preprocessing_eda/covariance_matrix.cpp) | Covariance Matrix Computes sample covariance between all numeric columns. | Python |
| [`data_profiling_summary`](cpp/data-science/preprocessing_eda/data_profiling_summary.cpp) | Column-wise dataset profiler. For each column it drops nulls, infers numeric vs categorical from the first non-null value, and reports missing count and cardinality; numeric… | Python |
| [`histogram_builder`](cpp/data-science/preprocessing_eda/histogram_builder.cpp) | Fixed-width histogram builder. Chooses the bin count by Sturges' rule (ceil(log2 n)+1) unless one is given, spans [min,max] in equal-width bins, and folds the maximum value into… | Python |
| [`missing_value_imputation`](cpp/data-science/preprocessing_eda/missing_value_imputation.cpp) | Missing Value Imputation Pattern. Oracle asserts: length preserved no None remains indicators match fill value equals mean median imputation correct | Python |
| [`one_hot_encoding`](cpp/data-science/preprocessing_eda/one_hot_encoding.cpp) | One-hot encoder. fit builds a vocabulary of unique categories (assigned indices in sorted order); transform maps each value to a 0/1 indicator vector. Unseen categories either… | Python |
| [`pearson_correlation_matrix`](cpp/data-science/preprocessing_eda/pearson_correlation_matrix.cpp) | pearson_correlation_matrix.cpp Pairwise Pearson correlation matrix from scratch. | Python |
| [`quantile_binning`](cpp/data-science/preprocessing_eda/quantile_binning.cpp) | Quantile (equal-frequency) binning versus equal-width binning, contrasted on skewed (exponential) data. Quantile binning sorts by value and places cut edges at rank positions so… | Python |
| [`random_oversampling_balance`](cpp/data-science/preprocessing_eda/random_oversampling_balance.cpp) | random_oversampling_balance.cpp — Random oversampling and SMOTE-lite for class balance. | Python |
| [`three_way_stratified_split`](cpp/data-science/preprocessing_eda/three_way_stratified_split.cpp) | Three-way (train/validation/test) split that preserves per-class proportions. It groups sample indices by label, shuffles each group with a deterministic LCG, then slices each… | Python |
| [`winsorize_clip_outliers`](cpp/data-science/preprocessing_eda/winsorize_clip_outliers.cpp) | Winsorization and Clipping Pattern. Converted from the Python oracle. | Python |

### data-science/probabilistic_modeling_bayes_ii

| Pattern | Description | Also in |
|---|---|---|
| [`bayesian_linear_regression`](cpp/data-science/probabilistic_modeling_bayes_ii/bayesian_linear_regression.cpp) | Bayesian Linear Regression (Conjugate Normal Prior) Core idea: prior N(μ₀, Σ₀); likelihood N(y \| Xβ, σ²I); posterior is N(μ_post, Σ_post) with closed-form updates. Posterior mean… | Python |
| [`bayesian_two_segment_changepoint`](cpp/data-science/probabilistic_modeling_bayes_ii/bayesian_two_segment_changepoint.cpp) | Bayesian Two-Segment Changepoint Compare model evidence for no-change vs change-at-t; find planted change location; no-change data prefers single-segment model. | Python |
| [`dirichlet_multinomial`](cpp/data-science/probabilistic_modeling_bayes_ii/dirichlet_multinomial.cpp) | Dirichlet-multinomial posterior and log-likelihood — C++17 port. Includes Stirling log-gamma approximation matching the Python oracle. | Python |
| [`empirical_bayes_shrinkage`](cpp/data-science/probabilistic_modeling_bayes_ii/empirical_bayes_shrinkage.cpp) | Inlined from empirical_bayes_shrinkage.h | Python |
| [`gamma_poisson_conjugate`](cpp/data-science/probabilistic_modeling_bayes_ii/gamma_poisson_conjugate.cpp) | Gamma-Poisson conjugate prior: Gamma prior on Poisson rate parameter. | Python |
| [`gaussian_process_lite`](cpp/data-science/probabilistic_modeling_bayes_ii/gaussian_process_lite.cpp) | Gaussian process regression (lite): RBF kernel, small n, direct Cholesky solve. | Python |
| [`hmm_baum_welch`](cpp/data-science/probabilistic_modeling_bayes_ii/hmm_baum_welch.cpp) | HMM Baum-Welch (EM) training: recover emission and transition probabilities. Claims verified: - Learned A (transition) and B (emission) recover the planted matrices. - pi, A, B… | Python |
| [`particle_filter_1d`](cpp/data-science/probabilistic_modeling_bayes_ii/particle_filter_1d.cpp) | Deterministic LCG + Box-Muller replacing Python's random | Python |
| [`rejection_sampling`](cpp/data-science/probabilistic_modeling_bayes_ii/rejection_sampling.cpp) | Target unnormalized density: mixture of two bumps. | Python |
| [`rts_kalman_smoother`](cpp/data-science/probabilistic_modeling_bayes_ii/rts_kalman_smoother.cpp) | RTS Kalman smoother: forward-backward pass for optimal smoothing. | Python |

### data-science/probability_iii

| Pattern | Description | Also in |
|---|---|---|
| [`banach_matchbox_or_gambler_ruin`](cpp/data-science/probability_iii/banach_matchbox_or_gambler_ruin.cpp) | Gambler's Ruin Absorption probability of a bounded ±1 random walk. A gambler starts with wealth a against an opponent with b (total N = a+b); each play moves wealth ±1 (P(+1)=p).… | Python |
| [`benford_law_test`](cpp/data-science/probability_iii/benford_law_test.cpp) | Benford's Law Test P(digit d) = log₁₀(1 + 1/d) for d ∈ {1,...,9}. Multiplicative data follows; uniform data violates it. Chi-square test. | Python |
| [`birthday_paradox_exact_vs_sim`](cpp/data-science/probability_iii/birthday_paradox_exact_vs_sim.cpp) | Birthday Paradox: Analytical vs Simulated Collision Probability P(≥2 same birthday in n people) ≈ 1 - n!/((365)^n · (365-n)!). Planted n values; analytic and simulated agree. | Python |
| [`copula_gaussian_lite`](cpp/data-science/probability_iii/copula_gaussian_lite.cpp) | Gaussian Copula Model dependence structure separately from marginals. Copula C(u, v) = P(U ≤ u, V ≤ v) where U, V ~ uniform. | Python |
| [`coupon_collector`](cpp/data-science/probability_iii/coupon_collector.cpp) | Coupon Collector Problem Expected trials to collect all n distinct items: E[T] = n * H_n where H_n is harmonic sum. | Python |
| [`extreme_value_block_maxima`](cpp/data-science/probability_iii/extreme_value_block_maxima.cpp) | Block-maxima extreme-value analysis. Fits a Gumbel distribution to a set of block maxima by method of moments (sigma = sqrt(6*var)/pi, mu = mean - gamma*sigma), and provides its… | Python |
| [`inclusion_exclusion_derangements`](cpp/data-science/probability_iii/inclusion_exclusion_derangements.cpp) | Inclusion-exclusion: count derangements (permutations with no fixed points). Oracle asserts: abs(observed_proportion - expected_proportion) < 0.05 abs(ratio - 1/e) < 0.01 | Python |
| [`polya_urn_reinforcement`](cpp/data-science/probability_iii/polya_urn_reinforcement.cpp) | Deterministic LCG to match per-seed Python random.random() is not required; the oracle uses Python's Mersenne Twister. We use C++ MT19937 seeded with s for each urn and verify the… | Python |
| [`quantile_mapping_bias_correction`](cpp/data-science/probability_iii/quantile_mapping_bias_correction.cpp) | Quantile-mapping bias correction. For each biased value it computes the value's empirical quantile within the biased sample, then substitutes the reference distribution's value at… | Python |
| [`stirling_approximation_error`](cpp/data-science/probability_iii/stirling_approximation_error.cpp) | Stirling's approximation for log(n!): n*ln(n) - n + 0.5*ln(2*pi*n), checked against the exact log-factorial (summed logs) at n = 10, 100, 1000. Demonstrates that the… | Python |

### data-science/rankings_information_retrieval

| Pattern | Description | Also in |
|---|---|---|
| [`ab_interleaving`](cpp/data-science/rankings_information_retrieval/ab_interleaving.cpp) | Team-Draft Interleaving for A/B Testing Rankers. Compare two rankers (A and B) by interleaving their results in a single ranking. Users click on interleaved results. The ranker… | Python |
| [`bm25_ranking`](cpp/data-science/rankings_information_retrieval/bm25_ranking.cpp) | BM25 Ranking (Okapi BM25) BM25 ranks documents by relevance to a query via TF-IDF with saturation and length normalization. | Python |
| [`elo_rating`](cpp/data-science/rankings_information_retrieval/elo_rating.cpp) | Elo Rating System. C++17 self-contained port with full parity to Python oracle. | Python |
| [`inverted_index_search`](cpp/data-science/rankings_information_retrieval/inverted_index_search.cpp) | Inverted Index and Boolean Search. Oracle asserts: query_and({"python","machine"}) == {"doc1"} query_or({"python","machine"}) == {"doc1","doc2","doc3","doc5"} index["python"] ==… | Python |
| [`mean_reciprocal_rank`](cpp/data-science/rankings_information_retrieval/mean_reciprocal_rank.cpp) | Ranking metrics suite: Mean Reciprocal Rank, Precision@K, Recall@K. Oracle asserts: reciprocal_rank exact values rr_ideal > rr_demoted aggregate MRR exact | Python |
| [`ndcg_evaluation`](cpp/data-science/rankings_information_retrieval/ndcg_evaluation.cpp) | NDCG (Normalized Discounted Cumulative Gain). Oracle asserts: ideal DCG matches expected within 0.01 perfect NDCG ~1.0 degraded NDCG < 0.5 perfect > 2 * degraded | Python |
| [`pairwise_ranking_learn`](cpp/data-science/rankings_information_retrieval/pairwise_ranking_learn.cpp) | Pairwise learning-to-rank. Builds one training example per ordered item pair (label = which should rank higher) over feature differences, fits a logistic model by batch gradient… | Python |
| [`position_bias_click_model`](cpp/data-science/rankings_information_retrieval/position_bias_click_model.cpp) | Position-bias click model with inverse-propensity correction. Simulates user clicks where click probability is true relevance discounted by a rank-dependent examination factor… | Python |
| [`query_expansion_prf`](cpp/data-science/rankings_information_retrieval/query_expansion_prf.cpp) | Query expansion via pseudo-relevance feedback (PRF). Runs an initial term-frequency search, assumes the top-k returned docs are relevant, then adds their most frequent non-query… | Python |
| [`rank_fusion_rrf`](cpp/data-science/rankings_information_retrieval/rank_fusion_rrf.cpp) | rank_fusion_rrf.cpp — Reciprocal Rank Fusion. | Python |

### data-science/recommenders_graph_sampling

| Pattern | Description | Also in |
|---|---|---|
| [`apriori_frequent_itemsets`](cpp/data-science/recommenders_graph_sampling/apriori_frequent_itemsets.cpp) | Apriori algorithm for frequent itemsets and association rules. Restored generate_rules() + rule asserts per Python oracle. | Python |
| [`bayesian_ab_beta`](cpp/data-science/recommenders_graph_sampling/bayesian_ab_beta.cpp) | Bayesian A/B Testing with Beta-Binomial Posteriors Core idea: model each variant's success rate as Beta distribution, update posterior with observed data (successes + failures),… | Python |
| [`iqr_outlier_detection`](cpp/data-science/recommenders_graph_sampling/iqr_outlier_detection.cpp) | IQR-based outlier detection. Oracle asserts: len(detected_indices) >= 2 at least one injected outlier found len(clean_detected) < 5 | Python |
| [`item_based_cf`](cpp/data-science/recommenders_graph_sampling/item_based_cf.cpp) | Item-based collaborative filtering. Oracle asserts: len(recommendations) > 0 all recommended item_id not in user's rated items len(recommended_items ∩ unseen_items) > 0 | Python |
| [`matrix_factorization_sgd`](cpp/data-science/recommenders_graph_sampling/matrix_factorization_sgd.cpp) | Matrix factorization via stochastic gradient descent. Oracle asserts: final_rmse < 0.5 | Python |
| [`monte_carlo_estimation`](cpp/data-science/recommenders_graph_sampling/monte_carlo_estimation.cpp) | Monte Carlo estimation: pi and definite integrals. Oracle asserts: error_10000 < error_1000 error_int_10000 < error_int_1000 abs(pi_estimate_10000 - pi) < 0.1 abs(integral_10000 -… | Python |
| [`mutual_information_feature_selection`](cpp/data-science/recommenders_graph_sampling/mutual_information_feature_selection.cpp) | Mutual information for feature selection. Oracle asserts: mi[0] > mi[2] mi[1] > mi[3] | Python |
| [`pagerank_power_iteration`](cpp/data-science/recommenders_graph_sampling/pagerank_power_iteration.cpp) | PageRank by power iteration on a directed graph. Each round redistributes rank along out-edges scaled by the damping factor, adds a uniform teleport term, and spreads the mass of… | Python |
| [`thompson_sampling_bandit`](cpp/data-science/recommenders_graph_sampling/thompson_sampling_bandit.cpp) | Thompson sampling for a Bernoulli multi-armed bandit. Each arm holds a Beta(alpha,beta) posterior over its success rate; each round samples a value per arm (here a Gaussian… | Python |
| [`user_based_cf`](cpp/data-science/recommenders_graph_sampling/user_based_cf.cpp) | User-based collaborative filtering: predicts a user's rating for an item as a cosine-similarity-weighted average of the top-k most similar users who rated it. Use when you have a… | Python |

### data-science/recommenders_ii_kept_survivors

| Pattern | Description | Also in |
|---|---|---|
| [`catalog_coverage_diversity`](cpp/data-science/recommenders_ii_kept_survivors/catalog_coverage_diversity.cpp) | Catalog Coverage and Diversity of Recommendations | Python |
| [`content_tfidf_rec`](cpp/data-science/recommenders_ii_kept_survivors/content_tfidf_rec.cpp) | Content-Based TF-IDF Recommendation Recommend items similar in content using cosine similarity. | Python |
| [`intra_list_diversity`](cpp/data-science/recommenders_ii_kept_survivors/intra_list_diversity.cpp) | Intra-list diversity (ILD) of a recommendation list. Oracle asserts: ild_diverse > ild_narrow | Python |
| [`novelty_serendipity`](cpp/data-science/recommenders_ii_kept_survivors/novelty_serendipity.cpp) | Novelty and serendipity: how unexpected/long-tail are recommendations. | Python |

### data-science/signal_processing_sequences

| Pattern | Description | Also in |
|---|---|---|
| [`autocovariance_spectrum`](cpp/data-science/signal_processing_sequences/autocovariance_spectrum.cpp) | Autocovariance and Power Spectral Density (Periodogram) Periodogram = DFT of autocovariance function. For a signal with strong periodicity, the periodogram should show a peak at… | Python |
| [`convolution_filtering`](cpp/data-science/signal_processing_sequences/convolution_filtering.cpp) | Convolution and Filtering Convolve a signal with a kernel via discrete convolution. Demonstrate smoothing (moving average) and edge detection (difference kernel). | Python |
| [`cross_correlation_lag`](cpp/data-science/signal_processing_sequences/cross_correlation_lag.cpp) | Cross-Correlation and Lag Detection Compute cross-correlation between two signals. The lag at which cross-correlation is maximum indicates the time shift. | Python |
| [`discrete_fourier_transform`](cpp/data-science/signal_processing_sequences/discrete_fourier_transform.cpp) | Discrete Fourier Transform: detect frequency components in signal. Core claim: DFT peaks at planted frequencies, Parseval holds. | Python |
| [`dynamic_range_compression`](cpp/data-science/signal_processing_sequences/dynamic_range_compression.cpp) | Inlined from dynamic_range_compression.h | Python |
| [`fft_cooley_tukey`](cpp/data-science/signal_processing_sequences/fft_cooley_tukey.cpp) | FFT via Cooley-Tukey Algorithm. Oracle parity: uses the exact Python-generated Gaussian signal (seed 42) and implements the same recursive DIT FFT and naive DFT. | Python |
| [`hampel_filter_outliers`](cpp/data-science/signal_processing_sequences/hampel_filter_outliers.cpp) | Hampel Filter for Outlier Detection and Removal. | Python |
| [`peak_detection`](cpp/data-science/signal_processing_sequences/peak_detection.cpp) | peak_detection.cpp Peak detection via prominence. | Python |
| [`resampling_interpolation`](cpp/data-science/signal_processing_sequences/resampling_interpolation.cpp) | Signal resampling: upsample a 1-D signal by an integer factor via linear or nearest-neighbor interpolation, plus a stride-based downsampler. Use when changing the sample rate of a… | Python |
| [`savitzky_golay_lite`](cpp/data-science/signal_processing_sequences/savitzky_golay_lite.cpp) | Savitzky-Golay filter: local polynomial smoothing. | Python |

### data-science/simulation_decision_science

| Pattern | Description | Also in |
|---|---|---|
| [`discrete_event_simulation`](cpp/data-science/simulation_decision_science/discrete_event_simulation.cpp) | Discrete Event Simulation (M/M/1 service desk) — C++17 port. Event-driven simulation with conservation: arrivals == served + still-in-system. | Python |
| [`kelly_criterion`](cpp/data-science/simulation_decision_science/kelly_criterion.cpp) | Kelly Criterion: optimal betting fraction for long-run log-growth. Oracle asserts: med_k > med_o logg_k > logg_o paired_wins / n_paths > 0.6 | Python |
| [`mm1_queue_littles_law`](cpp/data-science/simulation_decision_science/mm1_queue_littles_law.cpp) | M/M/1 Queue: verify Little's Law and analytic formulas. Oracle asserts: Little's Law relative error < 0.3 0.5 * expected_w < W < 2.0 * expected_w 0.5 * expected_l < L < 2.0 *… | Python |
| [`monte_carlo_var_es`](cpp/data-science/simulation_decision_science/monte_carlo_var_es.cpp) | Monte Carlo VaR & ES: Value-at-Risk and Expected Shortfall on returns. Oracle asserts: var_95 < 0 es_95 < var_95 abs(es_95) >= abs(var_95) 0.03 < exceedance_rate < 0.07 | Python |
| [`newsvendor_critical_fractile`](cpp/data-science/simulation_decision_science/newsvendor_critical_fractile.cpp) | Newsvendor problem: optimal stock at critical fractile beats under/over stocking. Deterministic LCG matching Python random.uniform via seed-per-day. | Python |
| [`q_learning_gridworld`](cpp/data-science/simulation_decision_science/q_learning_gridworld.cpp) | Tabular Q-learning on a 4x4 gridworld with a goal (+1), a pit (-1), and a small step penalty. Trains a Q-table over 500 epsilon-greedy episodes with the standard Bellman update… | Python |
| [`schelling_segregation`](cpp/data-science/simulation_decision_science/schelling_segregation.cpp) | Schelling Segregation: mild preference produces high global segregation. C++17 self-contained implementation. | Python |
| [`sir_epidemic_model`](cpp/data-science/simulation_decision_science/sir_epidemic_model.cpp) | Discrete SIR epidemic model with conservation checks and R0 comparison. | Python |
| [`tornado_sensitivity`](cpp/data-science/simulation_decision_science/tornado_sensitivity.cpp) | Tornado sensitivity analysis: for a profit model, perturb each input +/-10% one at a time (others held at base), measure the swing in output, and rank inputs by absolute impact.… | Python |

### data-science/statistical_modeling

| Pattern | Description | Also in |
|---|---|---|
| [`em_two_coins`](cpp/data-science/statistical_modeling/em_two_coins.cpp) | EM two coins: recover biased coin probabilities from incomplete data. Core claim: EM converges to true biases within tolerance. | Python |
| [`gibbs_sampling_bivariate`](cpp/data-science/statistical_modeling/gibbs_sampling_bivariate.cpp) | Gibbs Sampling for Bivariate Normal Distribution. Uses embedded Python random.gauss sequence for seed=42 to preserve the oracle's recovered correlation assertion. | Python |
| [`importance_sampling`](cpp/data-science/statistical_modeling/importance_sampling.cpp) | Importance Sampling for Expectation Estimation. | Python |
| [`kaplan_meier_survival`](cpp/data-science/statistical_modeling/kaplan_meier_survival.cpp) | Kaplan-Meier Survival Curve with Censored Observations. Oracle asserts: km_curve non-increasing surv_at_3 == 0.3 within 1e-6 synthetic curve non-increasing | Python |
| [`kernel_density_estimation`](cpp/data-science/statistical_modeling/kernel_density_estimation.cpp) | Kernel Density Estimation (KDE) with Gaussian Kernel & Silverman Bandwidth. Oracle asserts: abs(integral - 1.0) < 0.05 density_at_minus2 > density_at_0 density_at_2 > density_at_0 | Python |
| [`loess_local_regression`](cpp/data-science/statistical_modeling/loess_local_regression.cpp) | LOESS-Lite: Locally Weighted Linear Regression. Oracle asserts: mse_loess < mse_linear | Python |
| [`metropolis_hastings_mcmc`](cpp/data-science/statistical_modeling/metropolis_hastings_mcmc.cpp) | Metropolis-Hastings MCMC Sampling. Oracle asserts: abs(mean_samples) < 0.5 abs(var_samples - 5.0) < 1.0 0.2 < acc_rate < 0.7 | Python |
| [`polynomial_regression`](cpp/data-science/statistical_modeling/polynomial_regression.cpp) | Polynomial least-squares regression: builds a Vandermonde matrix and solves the normal equations (V^T V) c = V^T y via Gaussian elimination with partial pivoting. Use to fit a… | Python |
| [`power_analysis_sample_size`](cpp/data-science/statistical_modeling/power_analysis_sample_size.cpp) | Uses built-in erf for accurate normal_cdf. The oracle uses tanh approximation; using erf keeps the C++ code simple, standard, and accurate enough for assertions. | Python |
| [`quantile_regression_pinball`](cpp/data-science/statistical_modeling/quantile_regression_pinball.cpp) | Linear quantile regression via gradient descent on the pinball (quantile) loss: fits a line whose predictions target a chosen conditional quantile tau instead of the mean. Use to… | Python |

### data-science/statistics_testing

| Pattern | Description | Also in |
|---|---|---|
| [`ab_test_proportions`](cpp/data-science/statistics_testing/ab_test_proportions.cpp) | A/B Test for Two Proportions Core idea: Test whether two conversion rates differ using a z-test for proportions. Compute pooled standard error under the null, then the… | Python |
| [`benjamini_hochberg`](cpp/data-science/statistics_testing/benjamini_hochberg.cpp) | Benjamini-Hochberg False Discovery Rate Correction Controls the False Discovery Rate (FDR): the expected proportion of false positives among rejected hypotheses. Sort p-values,… | Python |
| [`bootstrap_confidence_interval`](cpp/data-science/statistics_testing/bootstrap_confidence_interval.cpp) | Bootstrap Confidence Interval for Sample Mean Resample the observed data WITH replacement many times to build an empirical distribution of sample statistics. Extract quantiles to… | Python |
| [`chi_square_independence`](cpp/data-science/statistics_testing/chi_square_independence.cpp) | Chi-Square Test of Independence Test whether two categorical variables are independent. | Python, R |
| [`confusion_matrix_metrics`](cpp/data-science/statistics_testing/confusion_matrix_metrics.cpp) | Confusion Matrix and Classification Metrics Build a confusion matrix (TP, FP, TN, FN) from binary predictions and true labels. Compute precision, recall, F1, and accuracy. | Python |
| [`permutation_test`](cpp/data-science/statistics_testing/permutation_test.cpp) | permutation_test.cpp Two-sample permutation test for difference of means. | Python |
| [`reservoir_sampling`](cpp/data-science/statistics_testing/reservoir_sampling.cpp) | Reservoir sampling (Algorithm R): draws a uniform random sample of k items from a stream of unknown or unbounded length in a single pass, keeping only k items in memory. Use when… | Python |
| [`roc_auc_from_scratch`](cpp/data-science/statistics_testing/roc_auc_from_scratch.cpp) | ROC Curve and AUC computation from scratch. | Python |
| [`train_test_split_kfold`](cpp/data-science/statistics_testing/train_test_split_kfold.cpp) | Train/test split and k-fold cross-validation: templated helpers that shuffle indices with a seeded RNG, carve out a test fraction (or k disjoint folds), and keep features and… | Python |

### data-science/streaming_iii

| Pattern | Description | Also in |
|---|---|---|
| [`adwin_drift_detector`](cpp/data-science/streaming_iii/adwin_drift_detector.cpp) | ADWIN0 adaptive-windowing drift detector (Bifet & Gavalda, 2007). | Python |
| [`bloom_filter_fpr`](cpp/data-science/streaming_iii/bloom_filter_fpr.cpp) | Bloom Filter with Measured False-Positive Rate Hash items to k positions in a bit array; false positive = query position all set but item not inserted. | Python |
| [`concept_drift_ensemble`](cpp/data-science/streaming_iii/concept_drift_ensemble.cpp) | Concept Drift Ensemble On a stream whose concept flips, a drift-aware ensemble that spawns a fresh learner per window and weights learners by their RECENT accuracy adapts to the… | Python |
| [`ddm_error_drift`](cpp/data-science/streaming_iii/ddm_error_drift.cpp) | DDM (Drift Detection Method): detect concept drift via error rate monitoring. Core claim: DDM detects drift after sufficient samples, no false alarm on stationary. | Python |
| [`exponential_histogram_count`](cpp/data-science/streaming_iii/exponential_histogram_count.cpp) | Exponential histogram / DGIM count of 1s in a sliding window (Datar-Gionis-Indyk-Motwani). Oracle parity: uses Python-generated deterministic stream, exact k computation, and the… | Python |
| [`frugal_streaming_median`](cpp/data-science/streaming_iii/frugal_streaming_median.cpp) | Frugal streaming median (Ma, Muthukrishnan, Sandler) -- Frugal-1, one integer of state. | Python |
| [`gk_quantile_summary`](cpp/data-science/streaming_iii/gk_quantile_summary.cpp) | Greenwald-Khanna ε-approximate quantile summary. | Python |
| [`hoeffding_tree_lite`](cpp/data-science/streaming_iii/hoeffding_tree_lite.cpp) | Hoeffding tree (VFDT) lite -- a streaming decision stump with a Hoeffding-bound split test. | Python |
| [`hyperloglog_distinct`](cpp/data-science/streaming_iii/hyperloglog_distinct.cpp) | HyperLogLog cardinality estimation (Flajolet et al.). | Python |
| [`kswin_drift`](cpp/data-science/streaming_iii/kswin_drift.cpp) | KSWIN (Kolmogorov-Smirnov Windowing) drift detector using KS test on sliding windows. Oracle asserts: kswin_drift(stationary) == False kswin_drift(shifted) == True | Python |
| [`lossy_counting_frequent`](cpp/data-science/streaming_iii/lossy_counting_frequent.cpp) | Lossy Counting for frequent items (Manku & Motwani, 2002). Oracle asserts: no false negatives for true frequent items count guarantee for reported items no spurious item with true… | Python |
| [`misra_gries_heavy_hitters`](cpp/data-science/streaming_iii/misra_gries_heavy_hitters.cpp) | Misra-Gries heavy hitters (k-1 counters). Oracle asserts: no false negatives for true heavy hitters count guarantee for survivors | Python |
| [`online_bagging_poisson`](cpp/data-science/streaming_iii/online_bagging_poisson.cpp) | Online bagging via Poisson(1) weighting — Oza & Russell convergence demo. Stumps and test data embedded from Python oracle (seed=42) so ensemble asserts pass. | Python |
| [`robust_streaming_mad`](cpp/data-science/streaming_iii/robust_streaming_mad.cpp) | Robust anomaly detection via median / MAD rule. | Python |
| [`sliding_window_quantile`](cpp/data-science/streaming_iii/sliding_window_quantile.cpp) | Exact sliding-window quantile via sorted-window maintenance. | Python |
| [`sliding_window_regression`](cpp/data-science/streaming_iii/sliding_window_regression.cpp) | Sliding-window OLS regression tracking a planted slope drift. | Python |
| [`tdigest_lite`](cpp/data-science/streaming_iii/tdigest_lite.cpp) | t-digest (merging variant): summarizes a sorted stream into a small set of centroids whose sizes are bounded by a q(1-q) scale function, giving accurate quantile estimates in far… | Python |
| [`weighted_reservoir_ares`](cpp/data-science/streaming_iii/weighted_reservoir_ares.cpp) | Weighted reservoir sampling -- Efraimidis-Spirakis A-Res. Converted from the Python oracle. | Python |
| [`welford_decayed_moments`](cpp/data-science/streaming_iii/welford_decayed_moments.cpp) | Exponentially-decayed streaming mean/variance (Welford-style, decay-weighted). Converted from the Python oracle. | Python |
| [`windowed_distinct_count`](cpp/data-science/streaming_iii/windowed_distinct_count.cpp) | Windowed distinct count: exact count of unique elements in a sliding window. Converted from the Python oracle. | Python |

### data-science/streaming_sketches

| Pattern | Description | Also in |
|---|---|---|
| [`count_min_sketch`](cpp/data-science/streaming_sketches/count_min_sketch.cpp) | Count-Min Sketch for Frequency Estimation A streaming data structure using hash functions to estimate item frequencies with bounded error. | Python, Rust |
| [`online_covariance`](cpp/data-science/streaming_sketches/online_covariance.cpp) | Online covariance/correlation via Welford's multivariate update: maintains a running mean and co-moment matrix, so the full covariance (and correlation) matrix is available after… | Python |
| [`online_sgd_classifier`](cpp/data-science/streaming_sketches/online_sgd_classifier.cpp) | Online (streaming) logistic-regression classifier trained by per-sample SGD: for each incoming (x, label) it updates weights and bias once using the logistic loss gradient, with a… | Python |
| [`p2_quantile_estimator`](cpp/data-science/streaming_sketches/p2_quantile_estimator.cpp) | P-square (P2) quantile estimator: tracks a single quantile of a stream using just five markers, adjusting their positions with parabolic (falling back to linear) interpolation as… | Python |
| [`page_hinkley_drift`](cpp/data-science/streaming_sketches/page_hinkley_drift.cpp) | Page-Hinkley concept-drift detector: maintains a running mean and a cumulative deviation statistic, raising an alarm (and resetting) when the gap between the statistic and its… | Python |
| [`sliding_window_extrema`](cpp/data-science/streaming_sketches/sliding_window_extrema.cpp) | Sliding window min/max via monotonic deque, verified against brute force. | Python |
| [`space_saving_heavy_hitters`](cpp/data-science/streaming_sketches/space_saving_heavy_hitters.cpp) | Space-Saving approximate top-k "heavy hitters": tracks only k counters over a stream; when a new item arrives with counters full, it evicts the current minimum and inherits… | Python |
| [`streaming_histogram_merge`](cpp/data-science/streaming_sketches/streaming_histogram_merge.cpp) | Streaming histogram with a bounded bin budget: each value joins a near bin (within 0.5) or spawns a new one, and when bins exceed max_bins the adjacent pair with the smallest… | Python |
| [`streaming_kmeans`](cpp/data-science/streaming_sketches/streaming_kmeans.cpp) | Online (streaming) k-means: keeps k centroids, assigns each incoming point to its nearest centroid, and nudges that centroid toward the point with a decaying learning rate… | Python |
| [`weighted_reservoir_sampling`](cpp/data-science/streaming_sketches/weighted_reservoir_sampling.cpp) | Weighted Reservoir Sampling (A-Res Algorithm) Converted from the Python oracle. | Python |

### data-science/survival_reliability

| Pattern | Description | Also in |
|---|---|---|
| [`accelerated_failure_time_lite`](cpp/data-science/survival_reliability/accelerated_failure_time_lite.cpp) | Accelerated failure time (AFT): log-linear regression on survival times. Model: log(T) = μ + β·x + σ·ε where T is survival time, x is covariate. Core claim: linear relationship… | Python |
| [`censoring_bias_demo`](cpp/data-science/survival_reliability/censoring_bias_demo.cpp) | Censoring Bias Demo Ignoring censoring biases survival estimates downward. Naive mean of observed times vs Kaplan-Meier estimate shows that censored data underestimates true mean… | Python |
| [`competing_risks_naive_bias`](cpp/data-science/survival_reliability/competing_risks_naive_bias.cpp) | Competing Risks: Naive KM vs Aalen-Johansen CIF With competing events, naive 1-KM overestimates incidence; Aalen-Johansen is correct. | Python |
| [`cox_partial_likelihood_lite`](cpp/data-science/survival_reliability/cox_partial_likelihood_lite.cpp) | Cox Partial Likelihood: Semiparametric Survival Model Estimates hazard ratios via Newton-Raphson on partial likelihood. | Python |
| [`exponential_reliability_mtbf`](cpp/data-science/survival_reliability/exponential_reliability_mtbf.cpp) | Exponential reliability: MTBF and survival function from failure times. Oracle parity: uses the exact Python-generated failure_times (seed 42, MTBF=100). | Python |
| [`hazard_vs_survival_conversion`](cpp/data-science/survival_reliability/hazard_vs_survival_conversion.cpp) | Hazard-survival conversion: verify duality h(t) = -d/dt[log S(t)]. | Python |
| [`log_rank_test`](cpp/data-science/survival_reliability/log_rank_test.cpp) | Log-rank test: nonparametric test for equality of survival curves. Oracle asserts: p_diff < 0.10 p_same > 0.10 | Python |
| [`nelson_aalen_cumhazard`](cpp/data-science/survival_reliability/nelson_aalen_cumhazard.cpp) | Nelson-Aalen cumulative hazard estimate. H(t) = sum d_i / y_i over sorted unique event times. Deterministic fixed seed via embedded PRNG for reproducible input. | Python |
| [`reliability_series_parallel`](cpp/data-science/survival_reliability/reliability_series_parallel.cpp) | Series system reliability (all components must work). | Python |
| [`weibull_mle`](cpp/data-science/survival_reliability/weibull_mle.cpp) | Weibull maximum-likelihood estimation: solves for the shape k by Newton-Raphson on the log-likelihood score, then computes the scale lambda in closed form from the fitted k. Use… | Python |

### data-science/text_nlp

| Pattern | Description | Also in |
|---|---|---|
| [`bag_of_words`](cpp/data-science/text_nlp/bag_of_words.cpp) | Bag-of-Words Vectorizer Core idea: represent each document as a sparse count vector of word frequencies. Build a shared vocabulary from all documents, then encode each document as… | Python |
| [`bpe_tokenizer_lite`](cpp/data-science/text_nlp/bpe_tokenizer_lite.cpp) | Simplified Byte-Pair Encoding (BPE) Tokenizer Learn merge operations from a corpus (combining frequent character pairs), then apply merges to tokenize new text. Encode text to… | Python |
| [`cosine_similarity_search`](cpp/data-science/text_nlp/cosine_similarity_search.cpp) | Cosine Similarity Search: TF-IDF Search Engine Convert documents and query to TF-IDF vectors, rank documents by cosine similarity. | Python |
| [`edit_distance`](cpp/data-science/text_nlp/edit_distance.cpp) | Edit distance: Levenshtein distance with operation tracking. Core claim: distance counts insertions/deletions/substitutions, backtrace produces target string, operation count… | Python |
| [`markov_chain_text`](cpp/data-science/text_nlp/markov_chain_text.cpp) | Word-Level Markov Chain Text Generator. Oracle asserts: transitions learned sanity check passes "the" follows START counts positive generated text is string, no START, non-empty… | Python |
| [`minhash_dedup`](cpp/data-science/text_nlp/minhash_dedup.cpp) | MinHash Signatures for Near-Duplicate Detection. Oracle asserts: signatures computed for each doc self-similarity == 1.0 MinHash estimate within 0.15 of exact Jaccard for… | Python |
| [`ngram_language_model`](cpp/data-science/text_nlp/ngram_language_model.cpp) | N-gram language model with add-one smoothing. Deterministic corpus, deterministic sampling via seeded RNG. | Python |
| [`rake_keyword_extraction`](cpp/data-science/text_nlp/rake_keyword_extraction.cpp) | rake_keyword_extraction.cpp — RAKE-style keyword extraction. | Python |
| [`tfidf_vectorizer`](cpp/data-science/text_nlp/tfidf_vectorizer.cpp) | TF-IDF vectorizer: learns smoothed inverse-document-frequency weights from a corpus (sorted vocab gives stable term IDs), then transforms documents into sparse or dense TF-IDF… | Python |
| [`viterbi_hmm`](cpp/data-science/text_nlp/viterbi_hmm.cpp) | Viterbi decoding for a small hidden Markov model: finds the maximum-probability hidden state sequence for an observation sequence via log-space dynamic programming with… | Python |

### data-science/text_nlp_ii

| Pattern | Description | Also in |
|---|---|---|
| [`char_ngram_language_id`](cpp/data-science/text_nlp_ii/char_ngram_language_id.cpp) | Character N-gram Language Identification Distinguish languages via bigram profiles. Builds character bigram frequencies; compares via distance. | Python |
| [`naive_bayes_complement`](cpp/data-science/text_nlp_ii/naive_bayes_complement.cpp) | Complement Naive Bayes: robust on imbalanced text via the negative-class model. Oracle asserts: nb_pred(["good","bad"]) == 0 cnb_pred(["good","bad"]) == 1 cnb_rec > nb_rec clear… | Python |
| [`porter_stemmer_lite`](cpp/data-science/text_nlp_ii/porter_stemmer_lite.cpp) | Lightweight Porter-style stemmer: lowercases a word, then applies a fixed cascade of suffix rules (plurals sses/ies/s, then ational->ate / tional / ing / ed, then ly / ness) to… | Python |
| [`sentence_boundary_detection`](cpp/data-science/text_nlp_ii/sentence_boundary_detection.cpp) | Sentence boundary detection: split text at sentence ends despite abbreviations. C++17 self-contained implementation. | Python |
| [`soundex_phonetic`](cpp/data-science/text_nlp_ii/soundex_phonetic.cpp) | Soundex phonetic encoding: keeps the first letter, maps the remaining consonants to digit codes, collapses runs of the same code, drops vowels, and pads/truncates to a 4-character… | Python |
| [`textrank_lite`](cpp/data-science/text_nlp_ii/textrank_lite.cpp) | TextRank-lite extractive sentence ranking: builds a fully-connected sentence graph weighted by Jaccard token overlap, then runs PageRank (damping 0.85, 50 iterations) to score… | Python |
| [`tf_idf_bm25_comparison`](cpp/data-science/text_nlp_ii/tf_idf_bm25_comparison.cpp) | Side-by-side TF-IDF and BM25 ranking over the same document collection, to show BM25's document-length normalization (k1, b, average-length term) versus plain TF-IDF's raw… | Python |
| [`zipf_law_fit`](cpp/data-science/text_nlp_ii/zipf_law_fit.cpp) | Zipf's law: rank-frequency relationship in natural language. | Python |

### data-science/time_series

| Pattern | Description | Also in |
|---|---|---|
| [`autocorrelation_function`](cpp/data-science/time_series/autocorrelation_function.cpp) | Autocorrelation Function (ACF) Compute the autocorrelation of a time series at multiple lags. ACF(k) = correlation between y_t and y_{t-k}. Include simple significance bounds… | Python |
| [`autoregressive_model`](cpp/data-science/time_series/autoregressive_model.cpp) | Autoregressive (AR) Model Fit an AR(p) model by regressing y_t on its p lagged values using least squares. Solves the normal equations directly (no external libraries). Produces… | Python |
| [`cusum_changepoint`](cpp/data-science/time_series/cusum_changepoint.cpp) | CUSUM changepoint detector: detect mean shifts in time series. Core claim: CUSUM detects step changes near the true change point. | Python |
| [`differencing_stationarity`](cpp/data-science/time_series/differencing_stationarity.cpp) | Differencing for Stationarity — C++17 port. First-difference a random walk and a trend; check stationarity diagnostics. | Python |
| [`exponential_smoothing`](cpp/data-science/time_series/exponential_smoothing.cpp) | Exponential Smoothing: SES and Holt's double exponential smoothing. Core claim: smoothed series less variable than raw, Holt detects trend, forecasts have correct length and Holt… | Python |
| [`kalman_filter_1d`](cpp/data-science/time_series/kalman_filter_1d.cpp) | 1D Kalman Filter. Oracle asserts: filtered_mse < raw_mse all gains in (0, 1) abs(gains_early - gains_late) < 0.1 abs(filtered_mean - 10.0) < 0.5 | Python |
| [`moving_average_smoothing`](cpp/data-science/time_series/moving_average_smoothing.cpp) | Moving Average Smoothing. Oracle asserts: sma_var, wma_var < raw_var sma_var, wma_var > 0 lengths preserved | Python |
| [`rolling_zscore_anomaly`](cpp/data-science/time_series/rolling_zscore_anomaly.cpp) | Rolling z-score anomaly detection: for each point, computes the mean and stdev over a trailing window and flags the point when its z-score exceeds a threshold; near-constant… | Python |
| [`seasonal_decomposition`](cpp/data-science/time_series/seasonal_decomposition.cpp) | Seasonal Decomposition (naive additive) C++17 self-contained implementation. | Python |
| [`walk_forward_validation`](cpp/data-science/time_series/walk_forward_validation.cpp) | Walk-forward (expanding-window) time-series backtesting: for each step past an initial window, trains a forecaster on all prior points and predicts one step ahead, collecting… | Python |

## go/programming

*45 files across 11 categories.*

### architecture

| Pattern | Description | Also in |
|---|---|---|
| [`cqrs_bus`](go/programming/architecture/cqrs_bus.go) | CQRS command/query separation: a CommandBus routes each command to its single registered handler (fire-and-forget), while a QueryBus routes queries and returns the handler's… | Python |
| [`event_bus`](go/programming/architecture/event_bus.go) | In-memory publish/subscribe event bus: named channels each carry a declared event type, subscribers register per channel, and Publish fans a payload out to all of a channel's… | Python |
| [`event_sourcing_store`](go/programming/architecture/event_sourcing_store.go) | Event-sourced aggregate store: appends versioned domain events per aggregate, rebuilds state by replaying events from the nearest snapshot forward, and auto-snapshots every N… | Python |

### async

| Pattern | Description | Also in |
|---|---|---|
| [`async_task_queue`](go/programming/async/async_task_queue.go) | Priority-ordered async task queue with retry, exponential backoff, and a dead- letter queue: a heap orders tasks by priority then scheduled time, workers pull and execute tasks,… | Python |
| [`cancellable_task_group`](go/programming/async/cancellable_task_group.go) | Structured concurrency task group with a shared cancellation token: Spawn runs each function in a goroutine, WaitAll joins them all, and CancelAll flips the token so cooperating… | Python |

### concurrency

| Pattern | Description | Also in |
|---|---|---|
| [`copy_on_write_config`](go/programming/concurrency/copy_on_write_config.go) | Copy-on-write config: readers observe a whole, consistent snapshot. In copy-on-write, a new Config is created for each update with all fields set to the same generation. An atomic… | — |
| [`cyclic_barrier`](go/programming/concurrency/cyclic_barrier.go) | CyclicBarrier synchronizes N parties at each phase — no party enters phase k+1 until all N have arrived at phase k — and is reusable across unlimited phases. Use when goroutines… | — |
| [`errgroup_first_error`](go/programming/concurrency/errgroup_first_error.go) | ErrGroup is a group of concurrent tasks where the first error returned by any task cancels the remaining tasks and causes Wait() to return that error. All goroutines are… | — |
| [`fan_in_multiplexer`](go/programming/concurrency/fan_in_multiplexer.go) | Fan-in multiplexer: combines multiple input channels into a single output channel. Use when merging concurrent streams from several independent sources into one unified flow.… | — |
| [`graceful_shutdown_drain`](go/programming/concurrency/graceful_shutdown_drain.go) | Graceful shutdown of a worker pool: accepts jobs into a queue, but on Shutdown closes the queue to new submissions while draining all accepted-but-unprocessed jobs, guaranteeing… | — |
| [`once_init_with_retry`](go/programming/concurrency/once_init_with_retry.go) | Lazy initialization that caches only successful results, retries after failures. Unlike sync.Once which caches a failed initialization permanently, this pattern lets the next… | — |
| [`pipeline_cancellation`](go/programming/concurrency/pipeline_cancellation.go) | 3-stage channel pipeline with clean cancellation: stage 1 generates items, stage 2 transforms them, stage 3 consumes them. When cancelled mid-flight, all stages stop gracefully,… | — |
| [`sharded_counter`](go/programming/concurrency/sharded_counter.go) | ShardedCounter: a striped-lock counter map where aggregate Sum() equals the exact number of increments applied, under heavy concurrent load — no lost updates. Use to count events… | — |
| [`singleflight_dedup`](go/programming/concurrency/singleflight_dedup.go) | Call deduplication under concurrent load: multiple goroutines requesting the same key execute the underlying function exactly once, and all N callers receive the identical result.… | — |
| [`treiber_lock_free_stack`](go/programming/concurrency/treiber_lock_free_stack.go) | A Treiber stack is a concurrent, lock-free stack built entirely with compare-and-swap (CAS) operations on the head pointer. Every push and pop operation uses atomic.Pointer to… | — |

### data_structures

| Pattern | Description | Also in |
|---|---|---|
| [`avl_tree`](go/programming/data_structures/avl_tree.go) | Self-balancing AVL binary search tree: insert/delete/search keep every node's left and right subtree heights within 1 via single and double rotations, so operations stay O(log n)… | Python |
| [`binary_indexed_tree`](go/programming/data_structures/binary_indexed_tree.go) | Binary indexed (Fenwick) tree over a 1-indexed array: point updates and prefix sums in O(log n), with a range-sum helper and a Query wrapper that turns raw delta updates into… | Python |
| [`bloom_filter`](go/programming/data_structures/bloom_filter.go) | Space-efficient probabilistic set membership: a Bloom filter sizes its bit array and hash count from a target capacity and error rate, using double hashing (two md5- derived… | Python, Rust |
| [`fenwick_tree`](go/programming/data_structures/fenwick_tree.go) | Fenwick (binary indexed) tree over a 0-indexed array: point updates and prefix sums in O(log n), with a range-sum helper computed from two prefix sums. Use for running /… | Python |

### distributed

| Pattern | Description | Also in |
|---|---|---|
| [`consistent_hash_ring`](go/programming/distributed/consistent_hash_ring.go) | Consistent hashing ring with virtual nodes: each physical node is placed at many md5 positions on a sorted ring, and a key maps to the first node clockwise from its hash. Use to… | Python, Rust |
| [`crdt_sets`](go/programming/distributed/crdt_sets.go) | crdt_sets: Conflict-free Replicated Data Types for sets (AWORSet, AddWinsSet, RemoveWinsSet). | Python |
| [`distributed_lock_manager`](go/programming/distributed/distributed_lock_manager.go) | distributed_lock_manager: in-process distributed lock manager with fairness queue, lease expiration, refresh, and mutual exclusion. | Python |
| [`g_counter_crdt`](go/programming/distributed/g_counter_crdt.go) | GCounter is a grow-only distributed counter. Each node maintains its own count, and the total is the sum of all nodes' counts. Merging takes the maximum value for each node to… | Python |

### io

| Pattern | Description | Also in |
|---|---|---|
| [`arg_parser`](go/programming/io/arg_parser.go) | Minimal argparse-style command-line parser: registers options (short/long flags with store, store_true, and store_false actions, fixed or "*" nargs) and positional arguments,… | Python |
| [`chunked_reader`](go/programming/io/chunked_reader.go) | Fixed-size chunked reader plus a line parser that reassembles complete lines across arbitrary chunk boundaries, carrying a partial remainder between chunks and emitting any final… | Python |
| [`csv_to_json`](go/programming/io/csv_to_json.go) | ColumnMapper maps CSV column names to nested JSON key paths. | Python |
| [`csv_validator`](go/programming/io/csv_validator.go) | Schema-driven CSV validation and transformation: each field declares a type (string/integer/float/boolean), a required flag, a default, and optional custom validators; rows are… | Python |
| [`diff_engine`](go/programming/io/diff_engine.go) | diff_engine: a simple line-based diff engine. | Python |

### monitoring

| Pattern | Description | Also in |
|---|---|---|
| [`alert_manager`](go/programming/monitoring/alert_manager.go) | Alert manager with per-rule deduplication, tag-based suppression, and escalation: alerts are fingerprinted (title + source + tags); a repeat within a rule's dedup window updates… | Python |
| [`event_logger`](go/programming/monitoring/event_logger.go) | Structured event logger: writes each event as one JSON line, gated by a chain of pluggable filters (level threshold, keyword include/exclude) that must ALL pass, with optional… | Python |

### networking

| Pattern | Description | Also in |
|---|---|---|
| [`connection_pool`](go/programming/networking/connection_pool.go) | Thread-safe connection pool with a fixed cap, health checks, and reuse. Borrow returns a pooled connection (revalidated) or mints a new one until maxSize, then refuses; return… | Python |
| [`connection_pool_health_checks`](go/programming/networking/connection_pool_health_checks.go) | Connection abstracts a database-style connection. | Python |
| [`dns_cache`](go/programming/networking/dns_cache.go) | DNS resolution cache with per-record TTL expiry, negative (NXDOMAIN) caching on a fixed 30s window, and LRU eviction at capacity. Lookup refreshes recency, drops expired entries,… | Python |

### performance

| Pattern | Description | Also in |
|---|---|---|
| [`batch_controller`](go/programming/performance/batch_controller.go) | Metrics holds performance data for a single batch. | Python |
| [`budget_allocator`](go/programming/performance/budget_allocator.go) | Request collapser: identical concurrent calls arriving within a time window are coalesced into a single backend call whose result (or error) fans out to every waiter; distinct… | Python |
| [`free_list_allocator`](go/programming/performance/free_list_allocator.go) | Best-fit memory allocator over a doubly-linked free list: allocate picks the smallest hole that fits, splitting off any remainder; free marks the block and coalesces adjacent free… | Python |

### reasoning

| Pattern | Description | Also in |
|---|---|---|
| [`astar_pathfinding`](go/programming/reasoning/astar_pathfinding.go) | A* Pathfinding Algorithm Implementation This file implements the A* pathfinding algorithm for grid-based navigation. It includes node, grid, and A* algorithm types, and replicates… | Python |
| [`bayesian_network`](go/programming/reasoning/bayesian_network.go) | Bayesian belief network: nodes with conditional probability tables (validated to sum to 1), joint probability via the chain rule, and exact posterior inference by enumeration over… | Python |
| [`csp_solver`](go/programming/reasoning/csp_solver.go) | csp_solver: constraint satisfaction problem solver with backtracking and AC-3. | Python |
| [`decision_tree`](go/programming/reasoning/decision_tree.go) | decision_tree: simple decision tree classifier with information gain and pruning. | Python |
| [`expression_evaluator`](go/programming/reasoning/expression_evaluator.go) | Arithmetic expression evaluator: a lexer + recursive-descent parser build an AST honoring precedence and right-associative '**', which an interpreter evaluates over a variable… | Python |
| [`sat_solver`](go/programming/reasoning/sat_solver.go) | DPLL SAT solver over CNF: unit propagation and pure-literal elimination drive a backtracking search that returns a satisfying assignment or nil for UNSAT. Use to decide… | Python |

### resilience

| Pattern | Description | Also in |
|---|---|---|
| [`bulkhead_isolator`](go/programming/resilience/bulkhead_isolator.go) | SemaphorePool manages a fixed number of permits. | Python |
| [`circuit_breaker`](go/programming/resilience/circuit_breaker.go) | Circuit breaker: wraps calls with stateful failure detection. CLOSED lets calls through and counts failures; at the threshold it trips OPEN and short-circuits (failing fast… | Python, Rust |
| [`dead_letter_queue`](go/programming/resilience/dead_letter_queue.go) | dead_letter_queue: retry handler with exponential backoff and poison-pill detection. | Python |

## go/system-administration

*58 files across 1 categories.*

### sysadmin

| Pattern | Description | Also in |
|---|---|---|
| [`advisory_lock_timeout`](go/system-administration/sysadmin/advisory_lock_timeout.go) | advisory_lock_with_timeout tries a non-blocking exclusive flock; if it fails, it polls until the lock becomes available or timeout_sec elapses. | Python |
| [`ansi_strip`](go/system-administration/sysadmin/ansi_strip.go) | strip_ansi removes ANSI escape sequences from text. | Python |
| [`append_only_audit`](go/system-administration/sysadmin/append_only_audit.go) | Tamper-evident audit log: each entry stores the SHA-256 of its event plus the prior entry's hash, forming a hash chain from a fixed genesis; verification recomputes every link and… | Python |
| [`atomic_append`](go/system-administration/sysadmin/atomic_append.go) | writerMode runs in a child process. It locks the lockfile, reads the target, appends its line, and writes it back. | Python |
| [`atomic_snapshot`](go/system-administration/sysadmin/atomic_snapshot.go) | Atomic file snapshot: reads the source fully, writes it to a temp file in the same directory, then renames it into place so the snapshot appears whole or not at all and is… | Python |
| [`atomic_symlink_swap`](go/system-administration/sysadmin/atomic_symlink_swap.go) | Atomic symlink deployment: stage a new symlink at a temp path pointing to the new target, then rename it over the live link so readers always see a valid old-or-new target and… | Python |
| [`atomic_write_temp_rename`](go/system-administration/sysadmin/atomic_write_temp_rename.go) | atomic_write_temp_rename: write atomically by writing to a temp file, then atomic rename. Failure simulated (the REAL one): a writer is killed AFTER the temp is fully written but… | Python |
| [`backfill_range`](go/system-administration/sysadmin/backfill_range.go) | backfill_range: fill gaps in time series or sequence. Assert: no gaps remain, existing records not duplicated. | Python |
| [`backpressure_queue`](go/system-administration/sysadmin/backpressure_queue.go) | Backpressure queue: refuses (non-blocking put_nowait) items when the bounded queue is full. Failure simulated: flood queue with 1000 items, cap=64; assert items are refused after… | Python |
| [`backup_catalog`](go/system-administration/sysadmin/backup_catalog.go) | backup_catalog: maintain and search backup metadata. | Python |
| [`backup_dedup`](go/system-administration/sysadmin/backup_dedup.go) | backup_dedup: detect and skip duplicate content in backups. | Python |
| [`backup_encryption`](go/system-administration/sysadmin/backup_encryption.go) | backup_encryption: encrypt backups at rest, verify decryption. | Python |
| [`backup_rotation`](go/system-administration/sysadmin/backup_rotation.go) | childScript is the Go source code we compile and run as a subprocess. It creates three versioned backup files, fsyncs them, signals readiness, then performs the atomic rotation… | Python |
| [`binary_presence_check`](go/system-administration/sysadmin/binary_presence_check.go) | checkBinariesExist verifies that each path exists, is a regular file, and is executable. | Python |
| [`blue_green_deploy`](go/system-administration/sysadmin/blue_green_deploy.go) | BlueGreenDeploy manages two parallel stacks and an atomic active-color switch. | Python |
| [`canary_gate`](go/system-administration/sysadmin/canary_gate.go) | CanaryGate gradually shifts traffic to a new version and rolls back if the error rate exceeds a threshold. | Python |
| [`capability_probe`](go/system-administration/sysadmin/capability_probe.go) | Filesystem capability probe: empirically tests whether a directory supports hardlinks, symlinks, and the execute bit by attempting each operation and cleaning up, returning a… | Python |
| [`cas_file_update`](go/system-administration/sysadmin/cas_file_update.go) | Optimistic compare-and-swap file update: each writer reads a versioned counter, computes its new value, and commits only if the on-disk version still matches, otherwise re-reads… | Python |
| [`checkpoint_resume`](go/system-administration/sysadmin/checkpoint_resume.go) | checkpoint_resume: resumable batch processing backed by an on-disk JSON checkpoint. Each completed batch's output is saved under its batch ID; on restart, finished batches are… | Python |
| [`circuit_breaker`](go/system-administration/sysadmin/circuit_breaker.go) | circuit_breaker: three-state (closed/open/half_open) breaker guarding a flaky call. Consecutive failures past a threshold trip it open; subsequent calls are short-circuited… | Python, Rust |
| [`clock_skew_detect`](go/system-administration/sysadmin/clock_skew_detect.go) | clock_skew_detect: detects backward wall-clock jumps across successive time samples. Each Sample compares against the previous reading; when time moves backward it records the… | Python |
| [`command_allowlist`](go/system-administration/sysadmin/command_allowlist.go) | command_allowlist: validates a command+args pair against an explicit per-command allowlist. A command absent from the map is rejected; a "*" entry permits any args, otherwise the… | Python |
| [`config_diff`](go/system-administration/sysadmin/config_diff.go) | config_diff: computes the delta between two config maps as added / removed / changed sets. A key only in the new map is "added", only in the old map is "removed", and present in… | Python |
| [`config_drift_detect`](go/system-administration/sysadmin/config_drift_detect.go) | config_drift_detect: detects when a scanned config drifts from an expected baseline. A SHA-256 hash of each config gives a fast has-drift check; getDriftDetails then classifies… | Python |
| [`config_versioning`](go/system-administration/sysadmin/config_versioning.go) | config_versioning: validates a versioned config wrapper (version + content + content_hash). It enforces the expected version, recomputes the SHA-256 of the content, and compares… | Python |
| [`corruption_repair`](go/system-administration/sysadmin/corruption_repair.go) | corruption_repair: detect a corrupted data file and restore it from a known-good backup. Corruption is detected by size shrinkage or a missing trailing newline; on detection the… | Python |
| [`cow_backup`](go/system-administration/sysadmin/cow_backup.go) | cow_backup: an independent point-in-time backup that survives later source corruption. Honest disclosure: this is an EAGER FULL COPY (read all bytes → temp → atomic rename), not… | Python |
| [`cpu_throttle`](go/system-administration/sysadmin/cpu_throttle.go) | cpu_throttle: caps concurrent CPU-bound workers, refuses spawning past limit. | Python |
| [`crash_consistent_snapshot`](go/system-administration/sysadmin/crash_consistent_snapshot.go) | crash_consistent_snapshot: snapshot a live DB atomically so the snapshot is never torn. | Python |
| [`crash_log_capture`](go/system-administration/sysadmin/crash_log_capture.go) | crash_log_capture: recover from torn log writes (truncated JSON mid-write). | Python |
| [`crash_loop_detector`](go/system-administration/sysadmin/crash_loop_detector.go) | crash_loop_detector: count restarts in a sliding window; if threshold exceeded, flag crash-loop + stop restarting. | Python |
| [`cron_expr_next_fire`](go/system-administration/sysadmin/cron_expr_next_fire.go) | cron_expr_next_fire: parse a cron expression and compute the exact next fire timestamp. | Python |
| [`deadline_ttl`](go/system-administration/sysadmin/deadline_ttl.go) | deadline_ttl: TTL/deadline arithmetic over an injectable clock function. SetDeadline turns a TTL into an absolute deadline (now + ttl); IsExpired reports whether the clock has… | Python |
| [`deadlock_timeout`](go/system-administration/sysadmin/deadlock_timeout.go) | deadlock_timeout: a spin-with-timeout lock that breaks deadlocks instead of hanging forever. Acquire polls the lock until it is free or the timeout elapses, returning false on… | Python |
| [`dedup_stream`](go/system-administration/sysadmin/dedup_stream.go) | dedup_stream: remove duplicate lines while preserving order. | Python |
| [`deplock_verify`](go/system-administration/sysadmin/deplock_verify.go) | deplock_verify: integrity-checks a dependency lock file and per-package version+hash. The lock is hashed over its key-sorted entries so tampering is detectable;… | Python |
| [`deploy_idempotency`](go/system-administration/sysadmin/deploy_idempotency.go) | deploy_idempotency: makes redeploying the current version a safe no-op. Deploy with skipIfCurrent=true short-circuits when the requested version is already current, leaving state… | Python |
| [`deps_verify`](go/system-administration/sysadmin/deps_verify.go) | deps_verify: verifies installed dependencies against a JSON manifest of expected version+sha256. For each manifest entry it requires the dependency to be present and to match both… | Python |
| [`dir_tree_diff`](go/system-administration/sysadmin/dir_tree_diff.go) | dir_tree_diff: diffs two directory trees by content, classifying files as added/removed/modified/unchanged. It builds a per-tree index of each file's size and SHA-256 (keyed by… | Python |
| [`disk_full_write_guard`](go/system-administration/sysadmin/disk_full_write_guard.go) | QuotaGuard caps total bytes written against a fixed byte quota and refuses any write that would push used-bytes past it (returning a "quota exceeded" error). Each accepted write… | Python |
| [`disk_space_watchdog`](go/system-administration/sysadmin/disk_space_watchdog.go) | DiskGuard enforces a total-bytes-written threshold: canWrite refuses a write whenever it would exceed the remaining space, and writeFile only commits (and tracks peak usage) when… | Python |
| [`dns_resolve_check`](go/system-administration/sysadmin/dns_resolve_check.go) | dnsResolveCheck resolves a hostname under a timeout context, returning its first IPv4 address (falling back to the first address of any family), or "" on any lookup error or empty… | Python |
| [`dotenv_parse`](go/system-administration/sysadmin/dotenv_parse.go) | parseDotenv reads a .env file into a map: it skips blank lines and #-comments, splits each entry on the first '=' only, trims surrounding whitespace, and strips one layer of… | Python |
| [`double_launch_block`](go/system-administration/sysadmin/double_launch_block.go) | ServiceLauncher ensures only one instance of a service runs using a pidfile lock. | Python |
| [`drift_compensation`](go/system-administration/sysadmin/drift_compensation.go) | DriftCompensator tracks and corrects for clock drift. | Python |
| [`dryrun_installer`](go/system-administration/sysadmin/dryrun_installer.go) | Install simulates installing packages to installDir. dryRun=true verifies without modifying; dryRun=false actually installs. | Python |
| [`enforce_600_perms`](go/system-administration/sysadmin/enforce_600_perms.go) | enforce_600_perms: check and enforce 0o600 permissions on secret files. | Python |
| [`env_diff`](go/system-administration/sysadmin/env_diff.go) | EnvDiff compares two environment maps and reports added, removed, and changed keys. | Python |
| [`env_load_defaults`](go/system-administration/sysadmin/env_load_defaults.go) | EnvLoadDefaults loads environment variables. requiredVars must be present, optionalDefaults are used when missing. | Python |
| [`env_secret_load`](go/system-administration/sysadmin/env_secret_load.go) | EnvSecretLoad loads a secret from an environment variable safely. | Python |
| [`exactly_once_dedup`](go/system-administration/sysadmin/exactly_once_dedup.go) | deduplicateStream processes records exactly-once by keeping a persisted JSON journal of already-seen IDs: each new ID is recorded to disk before its record is emitted, so a re-run… | Python |
| [`expiry_check`](go/system-administration/sysadmin/expiry_check.go) | expiryCheck decides whether a token is still valid by comparing a logical clock's current value against the token's expiry time: valid while now <= expiryTime, expired once now… | Python |
| [`exponential_backoff`](go/system-administration/sysadmin/exponential_backoff.go) | exponentialBackoff retries an operation up to maxAttempts, sleeping baseDelayMs * 2^(attempt-1) between tries and returning as soon as it succeeds, along with the measured… | Python, Rust |
| [`fd_leak_detector`](go/system-administration/sysadmin/fd_leak_detector.go) | FdCapGuard bounds the number of concurrently open file descriptors at a soft cap: canOpen refuses (and counts) an open once openCnt reaches the cap, opened/closed track the live… | Python |
| [`field_extract`](go/system-administration/sysadmin/field_extract.go) | extractFields pulls selected columns out of a single line by index (awk-like): with an empty delimiter it splits on runs of whitespace, otherwise on the given delimiter string,… | Python |
| [`fsync_durability`](go/system-administration/sysadmin/fsync_durability.go) | durableWrite writes data to a file and calls f.Sync() (fsync) before returning, forcing the bytes out of the OS buffer to the storage device rather than leaving them in cache. Use… | Python |
| [`full_incremental_backup`](go/system-administration/sysadmin/full_incremental_backup.go) | A full+incremental backup scheme: backupFull copies every file into level0 with a SHA256 manifest; backupIncremental copies only files whose SHA256 changed since the last manifest… | Python |
| [`timeout_kill`](go/system-administration/sysadmin/timeout_kill.go) | runWithTimeout runs a subprocess under a context deadline, capturing stdout/stderr and elapsed time: if the process exceeds the timeout it is killed and returns -1, otherwise it… | Python |

## javascript

*91 files across 6 categories.*

### clustering

| Pattern | Description | Also in |
|---|---|---|
| [`01_kmeans_lloyd`](javascript/clustering/01_kmeans_lloyd.js) | Lloyd's k-means clustering. Uses the first k points as initial centroids (the harness data is ordered round-robin, so this picks one point from each planted cluster) and runs… | — |
| [`01_kmeans_parallel_pp`](javascript/clustering/01_kmeans_parallel_pp.js) | k-means\|\| (scalable k-means++). k-means\|\| oversamples candidate centroids via probability proportional to squared distance, then re-clusters those candidates with Lloyd's… | — |
| [`02_kmeans_pp`](javascript/clustering/02_kmeans_pp.js) | k-means++ seeding followed by Lloyd's algorithm. A seeded PRNG is defined inside the fixture so the result is identical across the different harness-injected RNG seeds. k-means++… | — |
| [`02_kmeans_yinyang`](javascript/clustering/02_kmeans_yinyang.js) | Yinyang k-means. Groups centroids into super-clusters, maintains group-level lower bounds and per-point upper bounds, and filters distance computations. The acceleration is… | — |
| [`03_kmeans_annulus`](javascript/clustering/03_kmeans_annulus.js) | Annulus k-means. Sorts centroids by norm and uses the ordering to prune distance computations with the annulus rule: if \|norm(x)-norm(c)\| is already larger than the best… | — |
| [`03_kmeans_macqueen`](javascript/clustering/03_kmeans_macqueen.js) | MacQueen's incremental k-means. Unlike Lloyd, which updates all centroids after a full pass, MacQueen updates a centroid immediately each time a point is reassigned. The online… | — |
| [`04_kmeans_compare_means`](javascript/clustering/04_kmeans_compare_means.js) | Compare-means k-means. Maintains a table of inter-centroid distances and uses the triangle inequality to skip point-centroid comparisons whose lower bound already exceeds the best… | — |
| [`04_kmeans_hartigan_wong`](javascript/clustering/04_kmeans_hartigan_wong.js) | Hartigan-Wong k-means. Iteratively moves a single point to another cluster when the move strictly lowers the total within-cluster sum of squares, accounting for the centroid… | — |
| [`05_kmeans_elkan`](javascript/clustering/05_kmeans_elkan.js) | Elkan's triangle-inequality accelerated k-means. Uses per-point upper and lower distance bounds to avoid redundant distance computations. With exact arithmetic the final partition… | — |
| [`05_kmeans_sort_means`](javascript/clustering/05_kmeans_sort_means.js) | Sort-means k-means. After each iteration, sorts centroids along a projection direction and uses the sorted order to prune the search for the nearest centroid. The final centroids… | — |
| [`06_kmeans_hamerly`](javascript/clustering/06_kmeans_hamerly.js) | Hamerly's bound-accelerated k-means. Each point keeps one upper bound to its assigned centroid and one lower bound to the nearest other centroid. These bounds prune distance… | — |
| [`06_kmeans_kdtree`](javascript/clustering/06_kmeans_kdtree.js) | kd-tree accelerated k-means (blacklisting / filtering algorithm). Builds an axis-aligned kd-tree over the points. Each internal node carries the set of centroid candidates that… | — |
| [`07_kmeans_heap`](javascript/clustering/07_kmeans_heap.js) | Heap-based k-means. Maintains each point's upper bound and a max-heap over those bounds. At each iteration the heap is used to process the points most likely to change assignment… | — |
| [`07_kmeans_minibatch`](javascript/clustering/07_kmeans_minibatch.js) | Mini-batch k-means. A seeded PRNG inside the fixture selects deterministic mini-batches. Mini-batch updates do not in general converge to a Lloyd fixed point, so the algorithm… | — |
| [`08_kmeans_forgy`](javascript/clustering/08_kmeans_forgy.js) | Forgy initialization followed by Lloyd's algorithm. Forgy selects k distinct data points as initial centroids. A seeded PRNG is defined inside the fixture so the output is stable… | — |
| [`08_kmeans_hybrid_bounds`](javascript/clustering/08_kmeans_hybrid_bounds.js) | Hybrid Elkan+Hamerly bound k-means. Combines Elkan's per-centroid lower bounds with Hamerly's single global "second closest" lower bound. Each point keeps an upper bound to its… | — |
| [`09_kmeans_canopy`](javascript/clustering/09_kmeans_canopy.js) | Canopy pre-clustering followed by Lloyd's k-means. A seeded PRNG is defined inside the fixture. Points are greedily grouped into loose "canopies" using a distance threshold, then… | — |
| [`09_kmeans_random_partition`](javascript/clustering/09_kmeans_random_partition.js) | Random-partition initialization followed by Lloyd's algorithm. Each point is assigned to a random cluster using a seeded PRNG local to this file, initial centroids are the… | — |
| [`10_kmeans_bisecting`](javascript/clustering/10_kmeans_bisecting.js) | Bisecting k-means. Starts with one cluster containing all points, then repeatedly splits the cluster with the largest within-cluster SSE using 2-means until k clusters exist.… | — |
| [`10_kmeans_repeated_restart`](javascript/clustering/10_kmeans_repeated_restart.js) | Repeated-restart k-means. Runs N seeded Lloyd restarts with k-means++ style initialization, keeps the result with the lowest within-cluster sum of squares, and returns its exact… | — |

### direct-solvers

| Pattern | Description | Also in |
|---|---|---|
| [`linreg_cholesky`](javascript/direct-solvers/linreg_cholesky.js) | Linear regression via Cholesky decomposition of A^T A. lr and iters are unused. @param {number[][]} X - design matrix @param {number[]} y - target values @param {number} lr -… | — |
| [`linreg_gauss_jordan`](javascript/direct-solvers/linreg_gauss_jordan.js) | Linear regression via Gauss-Jordan elimination to invert X^T X explicitly. Builds A = [1 \| X], forms the normal-equations matrix M = A^T A, then reduces the augmented matrix [M… | — |
| [`linreg_givens`](javascript/direct-solvers/linreg_givens.js) | Linear regression via Givens-rotation QR decomposition. Applies plane rotations to reduce A = [1 \| X] to upper triangular form R while simultaneously transforming y, then… | — |
| [`linreg_householder_qr`](javascript/direct-solvers/linreg_householder_qr.js) | Linear regression via Householder QR reflection. Reduces A = [1 \| X] to upper triangular R by orthogonal Householder reflections applied to A and to y, then back-substitutes.… | — |
| [`linreg_lu`](javascript/direct-solvers/linreg_lu.js) | Linear regression via LU decomposition with partial pivoting. Builds A^T A theta = A^T y and solves with LU factorization. @param {number[][]} X - design matrix @param {number[]}… | — |
| [`linreg_modified_gram_schmidt`](javascript/direct-solvers/linreg_modified_gram_schmidt.js) | Linear regression via Modified Gram-Schmidt QR decomposition. Computes the reduced QR factorisation of A=[1\|X] with immediate orthogonalisation, then solves R*theta = Q^T*y. This… | — |
| [`linreg_normal_eq`](javascript/direct-solvers/linreg_normal_eq.js) | Closed-form linear regression via normal equations. The implementation is a direct least-squares solve; lr and iters are ignored. @param {number[][]} X - design matrix @param… | — |
| [`linreg_power_iteration_svd`](javascript/direct-solvers/linreg_power_iteration_svd.js) | Linear regression via power-iteration SVD. Computes the thin SVD of A = [1 \| X] by repeated power iteration with deterministic deflation, then forms the Moore-Penrose… | — |
| [`linreg_qr`](javascript/direct-solvers/linreg_qr.js) | Linear regression via QR decomposition (Gram-Schmidt). lr and iters are ignored because the method is closed-form. @param {number[][]} X - design matrix @param {number[]} y -… | — |
| [`linreg_ridge`](javascript/direct-solvers/linreg_ridge.js) | Ridge regression solved via normal equations with tiny regularisation. lambda = 1e-8 is chosen so the solution reduces to ordinary least squares on the harness data. @param… | — |
| [`linreg_sherman_morrison`](javascript/direct-solvers/linreg_sherman_morrison.js) | Linear regression via Sherman-Morrison rank-1 updates to an inverse. The normal-equations matrix M = A^T A is accumulated as a sum of outer products A_i A_i^T of rows of A = [1 \|… | — |
| [`linreg_svd`](javascript/direct-solvers/linreg_svd.js) | Linear regression via one-sided Jacobi SVD / Moore-Penrose pseudoinverse. Builds A = [1 \| X], computes the thin SVD A = U S V^T by applying Jacobi rotations to orthogonalise the… | — |

### gradient-and-adaptive-methods

| Pattern | Description | Also in |
|---|---|---|
| [`linreg_adadelta`](javascript/gradient-and-adaptive-methods/linreg_adadelta.js) | Linear regression via AdaDelta adaptive gradient descent. Maintains exponential moving averages of squared gradients and squared parameter updates to scale the step size per… | — |
| [`linreg_adagrad`](javascript/gradient-and-adaptive-methods/linreg_adagrad.js) | Batch AdaGrad for linear regression. AdaGrad accumulates squared gradients and uses per-coordinate adaptive learning rates. Because the harness calls with only 200 iterations at… | — |
| [`linreg_adam`](javascript/gradient-and-adaptive-methods/linreg_adam.js) | Adam (adaptive moment estimation) batch gradient descent for linear regression. @param {number[][]} X - design matrix @param {number[]} y - target values @param {number} lr -… | — |
| [`linreg_backtracking`](javascript/gradient-and-adaptive-methods/linreg_backtracking.js) | Gradient descent with backtracking line search (Armijo condition) for linear regression. @param {number[][]} X - design matrix @param {number[]} y - target values @param {number}… | — |
| [`linreg_barzilai_borwein`](javascript/gradient-and-adaptive-methods/linreg_barzilai_borwein.js) | Linear regression via the Barzilai-Borwein (BB) gradient method. Minimises the least-squares objective f(theta) = 0.5 \|\|A theta - y\|\|^2. The step size is chosen from the… | — |
| [`linreg_gd_1d_univariate`](javascript/gradient-and-adaptive-methods/linreg_gd_1d_univariate.js) | Univariate linear regression via batch gradient descent @param {number[][]} X - design matrix @param {number[]} y - target values @param {number} lr - learning rate @param… | — |
| [`linreg_minibatch`](javascript/gradient-and-adaptive-methods/linreg_minibatch.js) | Mini-batch gradient descent for linear regression. Deterministic shuffling via a seeded LCG; batch size fixed at 5. @param {number[][]} X - design matrix @param {number[]} y -… | — |
| [`linreg_momentum`](javascript/gradient-and-adaptive-methods/linreg_momentum.js) | Momentum-accelerated batch gradient descent for linear regression. @param {number[][]} X - design matrix @param {number[]} y - target values @param {number} lr - learning rate… | — |
| [`linreg_nadam`](javascript/gradient-and-adaptive-methods/linreg_nadam.js) | Linear regression via Nadam (Adam with Nesterov momentum). Combines adaptive second-moment scaling with Nesterov-style momentum lookahead. This is distinct from batch 2 Nesterov… | — |
| [`linreg_nesterov`](javascript/gradient-and-adaptive-methods/linreg_nesterov.js) | Nesterov accelerated gradient descent for linear regression. @param {number[][]} X - design matrix @param {number[]} y - target values @param {number} lr - learning rate @param… | — |
| [`linreg_polyak_sgd`](javascript/gradient-and-adaptive-methods/linreg_polyak_sgd.js) | Linear regression via Polyak-averaged stochastic gradient descent. Performs one-sample SGD with a fixed learning rate and returns the average of the iterates (Polyak averaging),… | — |
| [`linreg_rmsprop`](javascript/gradient-and-adaptive-methods/linreg_rmsprop.js) | RMSProp batch gradient descent for linear regression. Uses an exponentially moving average of squared gradients to scale the learning rate per coordinate. @param {number[][]} X -… | — |
| [`linreg_sgd`](javascript/gradient-and-adaptive-methods/linreg_sgd.js) | Stochastic gradient descent for linear regression. Uses a deterministic (seeded) sample order. @param {number[][]} X - design matrix @param {number[]} y - target values @param… | — |
| [`linreg_steepest_descent_exact`](javascript/gradient-and-adaptive-methods/linreg_steepest_descent_exact.js) | Linear regression via steepest descent with EXACT line search. Minimises f(theta) = 0.5 \|\|A theta - y\|\|^2 where A = [1 \| X]. The step size is the closed-form minimiser along… | — |

### iterative-solvers

| Pattern | Description | Also in |
|---|---|---|
| [`01_iterative_refinement`](javascript/iterative-solvers/01_iterative_refinement.js) | Iterative refinement for linear regression. Computes an initial solution via normal equations, then repeatedly refines it by solving the same normal system for the residual… | — |
| [`02_richardson_iteration`](javascript/iterative-solvers/02_richardson_iteration.js) | Richardson iteration for linear regression. Stationary Richardson iteration applied to the normal equations AtA * theta = Aty: each step adds a fixed multiple of the residual to… | — |
| [`03_chebyshev_semi_iterative`](javascript/iterative-solvers/03_chebyshev_semi_iterative.js) | Chebyshev semi-iterative method for linear regression. Accelerates the stationary Richardson iteration on the normal equations AtA * theta = Aty with the optimal Chebyshev… | — |
| [`04_randomized_kaczmarz`](javascript/iterative-solvers/04_randomized_kaczmarz.js) | Randomized Kaczmarz for linear regression. Unlike cyclic Kaczmarz, rows are picked with probability proportional to their squared norm using a seeded PRNG local to this file. This… | — |
| [`linreg_cg`](javascript/iterative-solvers/linreg_cg.js) | Conjugate gradient on the normal equations for linear regression. Solves A^T A theta = A^T y, where A = [1 \| X]. lr and iters are accepted for signature compatibility; iters caps… | — |
| [`linreg_gauss_seidel`](javascript/iterative-solvers/linreg_gauss_seidel.js) | Gauss-Seidel iteration on the normal equations for linear regression. Solves A^T A theta = A^T y by repeatedly updating each coordinate with the newest values of the others.… | — |
| [`linreg_jacobi`](javascript/iterative-solvers/linreg_jacobi.js) | Jacobi iteration on the normal equations for linear regression. Solves A^T A theta = A^T y by repeatedly updating all coordinates from the previous iterate in parallel. @param… | — |
| [`linreg_kaczmarz`](javascript/iterative-solvers/linreg_kaczmarz.js) | Linear regression via cyclic Kaczmarz row-action projection. For a consistent linear system A*theta = y (which holds here because y is generated exactly from the true… | — |
| [`linreg_landweber`](javascript/iterative-solvers/linreg_landweber.js) | Linear regression via Landweber iteration. Repeatedly applies the fixed-step iteration theta_{k+1} = theta_k - alpha * A^T(A*theta_k - y) which is gradient descent on the OLS… | — |
| [`linreg_lsqr`](javascript/iterative-solvers/linreg_lsqr.js) | Linear regression via LSQR, the iterative least-squares solver based on Golub-Kahan bidiagonalisation of A = [1 \| X]. LSQR minimises \|\|A theta - y\|\| without forming A^T A… | — |
| [`linreg_minres`](javascript/iterative-solvers/linreg_minres.js) | Linear regression via MINRES (minimum residual) / conjugate residual on the symmetric normal equations A^T A theta = A^T y, where A = [1 \| X]. MINRES minimises the residual norm… | — |
| [`linreg_pcg`](javascript/iterative-solvers/linreg_pcg.js) | Linear regression via preconditioned conjugate gradient on the normal equations. Uses a Jacobi (diagonal) preconditioner M = diag(A^T A), which makes this numerically distinct… | — |
| [`linreg_sor`](javascript/iterative-solvers/linreg_sor.js) | Linear regression via successive over-relaxation (SOR) on the normal equations A^T A theta = A^T y, where A = [1 \| X]. SOR generalises Gauss-Seidel with a relaxation factor omega… | — |

### second-order-and-splitting

| Pattern | Description | Also in |
|---|---|---|
| [`05_block_coordinate_descent`](javascript/second-order-and-splitting/05_block_coordinate_descent.js) | Block coordinate descent for linear regression. Updates blocks of coordinates jointly rather than one coordinate at a time. Here the parameter vector is split into a bias block… | — |
| [`06_admm_zero_regularization`](javascript/second-order-and-splitting/06_admm_zero_regularization.js) | ADMM for linear regression with zero regularisation. Splits the OLS problem into two blocks with an augmented Lagrangian and a dual variable. With zero regularisation the z-update… | — |
| [`07_dual_ascent`](javascript/second-order-and-splitting/07_dual_ascent.js) | Dual ascent for linear regression. Treats OLS as the primal problem and updates the dual variables associated with the prediction constraints. With a fixed step size chosen from… | — |
| [`08_gauss_newton`](javascript/second-order-and-splitting/08_gauss_newton.js) | Gauss-Newton for linear regression. For a linear model the Gauss-Newton approximation of the Hessian equals the normal-equation matrix A^T A, so the method converges in a single… | — |
| [`09_trust_region_dogleg`](javascript/second-order-and-splitting/09_trust_region_dogleg.js) | Trust-region / dogleg method for linear regression. On a linear least-squares problem the dogleg path is the segment from the current iterate through the full Gauss-Newton step;… | — |
| [`10_proximal_point`](javascript/second-order-and-splitting/10_proximal_point.js) | Proximal point method for linear regression. Each iteration solves a regularised subproblem whose exact minimiser is given by the normal equations of (A; sqrt(lambda) I). As the… | — |
| [`linreg_bfgs`](javascript/second-order-and-splitting/linreg_bfgs.js) | Linear regression via BFGS quasi-Newton optimization. Minimises the ordinary least-squares objective f(theta)=0.5*\|\|A*theta-y\|\|^2 where A=[1\|X]. Uses a rank-2 inverse-Hessian… | — |
| [`linreg_coordinate`](javascript/second-order-and-splitting/linreg_coordinate.js) | * Coordinate descent for linear regression. Alternates between a closed-form intercept update and closed-form updates for each weight coordinate. lr is unused. @param {number[][]}… | — |
| [`linreg_lbfgs`](javascript/second-order-and-splitting/linreg_lbfgs.js) | Linear regression via L-BFGS (limited-memory BFGS). Minimises the OLS objective f(theta)=0.5*\|\|A*theta-y\|\|^2 with a limited-memory inverse-Hessian update. @param {number[][]}… | — |
| [`linreg_levenberg_marquardt`](javascript/second-order-and-splitting/linreg_levenberg_marquardt.js) | Linear regression via Levenberg-Marquardt (damped Gauss-Newton). Solves the nonlinear least-squares problem min 0.5*sum r_i^2 where r_i = (bias + w^T X_i) - y_i. For a linear… | — |
| [`linreg_newton`](javascript/second-order-and-splitting/linreg_newton.js) | Newton's method for linear regression. For ordinary least squares the exact Hessian is A^T A and the gradient is A^T A theta - A^T y. One Newton step from the origin is therefore… | — |
| [`linreg_rls`](javascript/second-order-and-splitting/linreg_rls.js) | Linear regression via Recursive Least Squares (RLS). Processes samples online in a fixed deterministic order and maintains the inverse covariance (P) matrix. With an exact… | — |

### summary-statistics

| Pattern | Description | Also in |
|---|---|---|
| [`01_sorted_summation`](javascript/summary-statistics/01_sorted_summation.js) | Sorted summation statistics. Reduces floating-point error by sorting values by magnitude before accumulating sums and sum-of-squared-deviations. Variance is computed in a second… | — |
| [`02_blocked_summation`](javascript/summary-statistics/02_blocked_summation.js) | Blocked / tiled summation statistics. Accumulates sums in fixed-size blocks (partial sums) to reduce error growth from naive left-to-right accumulation. Means, variances and… | — |
| [`03_recursive_summation`](javascript/summary-statistics/03_recursive_summation.js) | Recursive divide-and-conquer summation statistics. Sums are computed recursively, splitting the array until it reaches a small base case. This minimises the depth of sequential… | — |
| [`04_klein_compensation`](javascript/summary-statistics/04_klein_compensation.js) | Klein second-order iterative compensation statistics. Performs compensated summation and then re-sums the per-step rounding-error residuals with a second compensated pass,… | — |
| [`05_error_free_transforms`](javascript/summary-statistics/05_error_free_transforms.js) | Error-free transformation (TwoSum) statistics. Uses Knuth/TwoSum error-free transformations for each addition: every sum is split into a rounded result and an exact residual, and… | — |
| [`06_double_double`](javascript/summary-statistics/06_double_double.js) | Double-double accumulation statistics. Each scalar is represented as a non-overlapping hi/lo float pair. Sums and sum-of-products are accumulated in double-double arithmetic, then… | — |
| [`07_fixed_point`](javascript/summary-statistics/07_fixed_point.js) | Scaled fixed-point / integer accumulation statistics. Scales floating-point values into a fixed-point representation based on the observed data range, accumulates integer-like… | — |
| [`08_streaming_recompaction`](javascript/summary-statistics/08_streaming_recompaction.js) | Streaming summation with periodic recompaction. Adds incoming values into a small local buffer; when the buffer is full it is compacted into a single partial sum using compensated… | — |
| [`09_long_accumulator`](javascript/summary-statistics/09_long_accumulator.js) | Long-accumulator style exact summation (bucketed by exponent). Each addend is split into a set of non-overlapping floating-point numbers stored in bins indexed by exponent. Bins… | — |
| [`10_shuffled_permutations`](javascript/summary-statistics/10_shuffled_permutations.js) | Seeded shuffled-order summation averaged over several permutations. A deterministic seeded PRNG inside the fixture generates several random permutations of the input. The required… | — |
| [`statistics_chan`](javascript/summary-statistics/statistics_chan.js) | Chan's parallel merge formula for one-pass mean and population variance. Combines partial statistics without re-scanning raw data. | — |
| [`statistics_kahan`](javascript/summary-statistics/statistics_kahan.js) | Kahan-compensated summation for mean and population variance. | — |
| [`statistics_naive_sos`](javascript/summary-statistics/statistics_naive_sos.js) | Naive sum-of-squares formula for mean and population variance. This is the numerically weakest method: it subtracts (sum/n)^2 from the raw sum of squares, which can… | — |
| [`statistics_neumaier`](javascript/summary-statistics/statistics_neumaier.js) | Neumaier's improved Kahan summation for mean and population variance. | — |
| [`statistics_pairwise`](javascript/summary-statistics/statistics_pairwise.js) | Pairwise (divide-and-conquer) summation for mean and population variance. | — |
| [`statistics_shifted`](javascript/summary-statistics/statistics_shifted.js) | Shifted (compensated) one-pass variance: subtract a shift constant to reduce catastrophic cancellation when numbers are large relative to their spread. | — |
| [`statistics_twopass`](javascript/summary-statistics/statistics_twopass.js) | Two-pass summary statistics (mean first, then variance). This function does not perform regression. | — |
| [`statistics_welford`](javascript/summary-statistics/statistics_welford.js) | Welford's online algorithm for one-pass mean and population variance. This function does not perform regression. | — |
| [`statistics_west`](javascript/summary-statistics/statistics_west.js) | West's weighted incremental algorithm for online mean and population variance. | — |
| [`statistics_youngs_cramer`](javascript/summary-statistics/statistics_youngs_cramer.js) | Youngs-Cramer online update for mean and population variance. | — |

## python/data-science

*377 files across 37 categories.*

### applied_ds_practice

| Pattern | Description | Also in |
|---|---|---|
| [`cohort_retention_analysis`](python/data-science/applied_ds_practice/cohort_retention_analysis.py) | Cohort retention analysis from event logs. Group users by cohort (e.g., signup month/cohort), track which cohorts return in subsequent periods, and compute retention curves.… | C++ |
| [`cross_validation_leakage`](python/data-science/applied_ds_practice/cross_validation_leakage.py) | Cross-validation data leakage from preprocessing before splitting. Feature selection fit on the FULL dataset before train-test split leaks information from test into train,… | C++ |
| [`drift_detection_psi`](python/data-science/applied_ds_practice/drift_detection_psi.py) | Population Stability Index (PSI) and KS-statistic for feature drift detection. PSI measures how a feature's distribution shifts between a reference period (e.g., training data)… | C++ |
| [`ewma_streaming_metrics`](python/data-science/applied_ds_practice/ewma_streaming_metrics.py) | Exponentially Weighted Moving Average (EWMA) for streaming metrics. EWMA smooths noisy streaming data while reacting quickly to level shifts. Each new observation is weighted… | C++ |
| [`feature_hashing_trick`](python/data-science/applied_ds_practice/feature_hashing_trick.py) | Feature hashing for dimensionality reduction of high-dimensional sparse features. Hash trick maps unbounded categorical/text features to a fixed number of dimensions via hashing.… | C++ |
| [`funnel_conversion_analysis`](python/data-science/applied_ds_practice/funnel_conversion_analysis.py) | Multi-step funnel conversion analysis with confidence intervals. Track user progression through a conversion funnel (e.g., visit → signup → purchase → retain). Compute step-wise… | C++ |
| [`rfm_customer_segmentation`](python/data-science/applied_ds_practice/rfm_customer_segmentation.py) | RFM customer segmentation: Recency, Frequency, Monetary. Segment customers based on: - Recency: days since last purchase - Frequency: number of purchases - Monetary: total spend… | C++ |
| [`simpsons_paradox_demo`](python/data-science/applied_ds_practice/simpsons_paradox_demo.py) | Simpson's Paradox: aggregate trend reverses within strata. An association between two variables at the aggregate level reverses direction when data is split by a confounding… | C++ |
| [`target_encoding_smoothing`](python/data-science/applied_ds_practice/target_encoding_smoothing.py) | Target encoding with smoothing + out-of-fold fitting. Target (mean) encoding replaces a category with the mean target of that category — powerful, and the classic way to leak: if… | C++ |
| [`welford_online_stats`](python/data-science/applied_ds_practice/welford_online_stats.py) | Welford's online algorithm for running mean and variance. Welford's algorithm computes running mean and variance in a single pass with O(1) memory and perfect numerical stability.… | C++ |

### bayesian_iii_approximate_inference

| Pattern | Description | Also in |
|---|---|---|
| [`abc_rejection_sampler`](python/data-science/bayesian_iii_approximate_inference/abc_rejection_sampler.py) | Approximate Bayesian Computation (ABC): rejection sampling for intractable likelihoods. Sample from prior, simulate data, accept if simulated ≈ observed (within ε). Core claim:… | C++ |
| [`bayes_factor_normal_means`](python/data-science/bayesian_iii_approximate_inference/bayes_factor_normal_means.py) | Bayes factor for comparing two normal means: H1 (θ ≠ 0) vs H0 (θ = 0). BF = p(data\|H1) / p(data\|H0). Core claim: BF>1 when H1 is true AND BF<1 when H0 is true (BOTH directions… | C++ |
| [`elbo_monotone_vi`](python/data-science/bayesian_iii_approximate_inference/elbo_monotone_vi.py) | ELBO monotonicity in coordinate-ascent variational inference. Coordinate-ascent VI (CAVI) maximizes the Evidence Lower Bound one factor at a time; each update is a conditional… | C++ |
| [`hierarchical_shrinkage_2level`](python/data-science/bayesian_iii_approximate_inference/hierarchical_shrinkage_2level.py) | Hierarchical shrinkage (James-Stein): partial-pooling beats no-pooling on MSE. When group means are estimated from noisy, small samples, shrinking them toward the grand mean… | C++ |
| [`laplace_approximation_posterior`](python/data-science/bayesian_iii_approximate_inference/laplace_approximation_posterior.py) | Laplace approximation: approximate posterior p(θ\|data) with Gaussian at MAP. Curvature of the log-posterior at the mode provides variance. Core claim: Gaussian-at-MAP mode ≈ true… | C++ |
| [`meanfield_vi_gaussian`](python/data-science/bayesian_iii_approximate_inference/meanfield_vi_gaussian.py) | Mean-field variational inference for a Gaussian with unknown mean AND precision. The true posterior over (μ, τ) is Normal-Gamma — NOT factorizable — so a mean-field q(μ)q(τ) is a… | C++ |
| [`posterior_contraction_rate`](python/data-science/bayesian_iii_approximate_inference/posterior_contraction_rate.py) | Posterior contraction rate: posterior sd shrinks ~1/√n as sample size increases. Bayesian consistency: posterior concentrates on true parameter. Core claim: posterior sd shrinks… | C++ |
| [`posterior_predictive_pvalue`](python/data-science/bayesian_iii_approximate_inference/posterior_predictive_pvalue.py) | Posterior predictive p-value: compare observed data to posterior predictive distribution. ppp ≈ 0.5 for the correct model; extreme (<0.05 or >0.95) for misspecified model. Core… | C++ |
| [`rhat_convergence_diagnostic`](python/data-science/bayesian_iii_approximate_inference/rhat_convergence_diagnostic.py) | R-hat convergence diagnostic: measures MCMC chain mixing. R̂ ≈ 1 for well-mixed chains, >1.1 for stuck chains. Core claim: R̂ ≈ 1 for well-mixed AND >1.1 for stuck (BOTH… | C++ |
| [`sbc_rank_uniformity`](python/data-science/bayesian_iii_approximate_inference/sbc_rank_uniformity.py) | Simulation Based Calibration (SBC): ranks should be uniform for a well-calibrated sampler. Simulate parameter, simulate data, infer posterior, check where the true parameter… | C++ |

### bayesian_iii_modeling_and_selection

| Pattern | Description | Also in |
|---|---|---|
| [`bayesian_changepoint_offline`](python/data-science/bayesian_iii_modeling_and_selection/bayesian_changepoint_offline.py) | Bayesian changepoint detection: find the point where mean shifts. Core claim: detected changepoint ≈ true location within tolerance. | C++ |
| [`bayesian_linreg_conjugate`](python/data-science/bayesian_iii_modeling_and_selection/bayesian_linreg_conjugate.py) | Bayesian linear regression with conjugate prior. Posterior mean ≈ true βs; 95% credible interval covers them. Core claim: posterior mean ≈ true βs; 95% credible interval covers… | C++ |
| [`beta_binomial_overdispersion`](python/data-science/bayesian_iii_modeling_and_selection/beta_binomial_overdispersion.py) | Beta-binomial: recover the planted overdispersion and beat the plain binomial. Counts with a random per-trial success probability p ~ Beta(α, β) are OVERDISPERSED relative to a… | C++ |
| [`bic_selects_true_degree`](python/data-science/bayesian_iii_modeling_and_selection/bic_selects_true_degree.py) | BIC model selection picks the true polynomial degree. Fits polynomials of increasing degree by real least squares (Vandermonde normal equations solved with Gaussian elimination)… | C++ |
| [`crp_table_growth`](python/data-science/bayesian_iii_modeling_and_selection/crp_table_growth.py) | Chinese Restaurant Process (CRP): expected number of tables ≈ α·ln(n). Core claim: E[#tables] ≈ α·ln(n) within tolerance (planted α). | C++ |
| [`dirichlet_multinomial_posterior`](python/data-science/bayesian_iii_modeling_and_selection/dirichlet_multinomial_posterior.py) | Dirichlet-Multinomial: posterior concentrates on true category probabilities as n grows. Core claim: posterior concentrates on true category probs as n grows. | C++ |
| [`dirichlet_stick_breaking`](python/data-science/bayesian_iii_modeling_and_selection/dirichlet_stick_breaking.py) | Dirichlet stick-breaking process: samples probabilities that sum to 1. Weights sum→1; E[#active clusters] increases monotonically with α (concentration). Core claim: weights… | C++ |
| [`evidence_ranks_true_model`](python/data-science/bayesian_iii_modeling_and_selection/evidence_ranks_true_model.py) | Model evidence (via BIC) ranks the true generative model above the alternative. A FAIR comparison scores each model by BIC = −2·log L̂ + k·log n, evaluated at each model's own MLE… | C++ |
| [`gp_regression_marginal_likelihood`](python/data-science/bayesian_iii_modeling_and_selection/gp_regression_marginal_likelihood.py) | Gaussian-process regression: the marginal likelihood peaks at the true lengthscale. The log marginal likelihood log p(y\|ℓ) = −½ yᵀK⁻¹y − ½ log\|K\| − n/2 log2π (K the RBF kernel… | C++ |
| [`kalman_rts_smoother`](python/data-science/bayesian_iii_modeling_and_selection/kalman_rts_smoother.py) | Kalman filter + Rauch-Tung-Striebel (RTS) smoother: the backward pass lowers MSE. The filter estimates each state from the past only; the RTS smoother adds a backward pass that… | C++ |

### causal_inference_and_experimentation

| Pattern | Description | Also in |
|---|---|---|
| [`ab_test_srm_check`](python/data-science/causal_inference_and_experimentation/ab_test_srm_check.py) | Sample Ratio Mismatch (SRM) Check for A/B Tests. In a valid A/B test, the allocation ratio should match the design (e.g., 50/50). A chi-square test on the observed counts detects… | C++ |
| [`cuped_variance_reduction`](python/data-science/causal_inference_and_experimentation/cuped_variance_reduction.py) | CUPED (Controlled-experiment Using Pre-Experiment Data). In A/B tests, Y_post = metric post-treatment, Y_pre = metric pre-treatment. CUPED adjusted metric = Y_post - theta *… | C++ |
| [`difference_in_differences`](python/data-science/causal_inference_and_experimentation/difference_in_differences.py) | Difference-in-Differences (DiD). Two groups (treated and control) observed before and after treatment. Parallel trends assumption: absent treatment, both groups would have the… | C++ |
| [`instrumental_variable_lite`](python/data-science/causal_inference_and_experimentation/instrumental_variable_lite.py) | Instrumental Variable (IV) Estimation. Treatment T is endogenous: unobserved U affects both T and Y, creating bias. An instrument Z affects Y only through T (exogeneity), and Z is… | C++ |
| [`interrupted_time_series`](python/data-science/causal_inference_and_experimentation/interrupted_time_series.py) | Interrupted Time Series (ITS) Segmented Regression. Time series with a pre-intervention trend; at a cutoff, intervention introduces a level change and/or slope change. Segmented… | C++ |
| [`placebo_test_causal`](python/data-science/causal_inference_and_experimentation/placebo_test_causal.py) | Placebo Test for Causal Inference. Under the null (no treatment effect), permuting treatment labels should destroy the measured effect. Under the alternative (true treatment… | C++ |
| [`propensity_score_matching`](python/data-science/causal_inference_and_experimentation/propensity_score_matching.py) | Propensity Score Matching (PSM). Observational data is confounded: treatment assignment depends on observed traits. We estimate the propensity score P(treatment \| confounders),… | C++ |
| [`regression_discontinuity`](python/data-science/causal_inference_and_experimentation/regression_discontinuity.py) | Regression Discontinuity (RD). Treatment is assigned by a cutoff rule on a running variable: T=1 if X >= cutoff. There is a discontinuity in the outcome at the cutoff: E[Y \|… | C++ |
| [`sequential_probability_ratio`](python/data-science/causal_inference_and_experimentation/sequential_probability_ratio.py) | Sequential Probability Ratio Test (SPRT). A sequential test that stops early: accumulate log-likelihood ratio for H0 vs H1. Stop when LR > threshold (accept H1) or LR < -threshold… | C++ |
| [`synthetic_control_lite`](python/data-science/causal_inference_and_experimentation/synthetic_control_lite.py) | Synthetic Control Method (Lite). A treated unit's outcome is compared to a weighted average of control units. Weights are chosen to match the treated unit's pre-intervention… | C++ |

### causal_inference_ii

| Pattern | Description | Also in |
|---|---|---|
| [`backdoor_vs_collider_adjustment`](python/data-science/causal_inference_ii/backdoor_vs_collider_adjustment.py) | Backdoor vs Collider adjustment: adjusting backdoor removes confounding bias; adjusting a collider CREATES bias (collider bias, Berkson's paradox). DAG: X ← U → Y (backdoor open;… | C++ |
| [`caliper_matching`](python/data-science/causal_inference_ii/caliper_matching.py) | Caliper matching: restrict nearest-neighbor matches to within a caliper (distance threshold). Bias-variance tradeoff: uncalipered NN can match distant observations (high bias);… | C++ |
| [`doubly_robust_aipw`](python/data-science/causal_inference_ii/doubly_robust_aipw.py) | Doubly Robust AIPW: consistent if EITHER the outcome model OR the propensity is correct. AIPW = (1/n) Σ [ μ₁(Xᵢ) − μ₀(Xᵢ) + Tᵢ(Yᵢ−μ₁)/eᵢ − (1−Tᵢ)(Yᵢ−μ₀)/(1−eᵢ) ]. Core claim… | C++ |
| [`e_value_sensitivity`](python/data-science/causal_inference_ii/e_value_sensitivity.py) | E-value sensitivity analysis: how strong must an unmeasured confounder be to explain away an effect? E-value = (RR + sqrt(RR*(RR-1))) / 1 for RR > 1. A strong effect (RR=3) needs… | C++ |
| [`frontdoor_criterion_lite`](python/data-science/causal_inference_ii/frontdoor_criterion_lite.py) | Frontdoor criterion: identify a causal effect when the backdoor is unblockable. DAG: U → X → M → Y and U → Y (hidden confounder U on X and Y; the backdoor through U cannot be… | C++ |
| [`heterogeneous_effects_subgroups`](python/data-science/causal_inference_ii/heterogeneous_effects_subgroups.py) | Heterogeneous treatment effects (CATE): treatment effect varies by subgroup. Planted CATE difference between subgroups; pooled estimate masks the heterogeneity. Core claim:… | C++ |
| [`ipw_ate`](python/data-science/causal_inference_ii/ipw_ate.py) | Inverse Propensity Weighting (IPW) for the Average Treatment Effect (ATE). Observational data X→T, X→Y (X confounds T→Y). IPW re-weights by 1/P(T\|X) to simulate randomization.… | C++ |
| [`mediation_effects_decomposition`](python/data-science/causal_inference_ii/mediation_effects_decomposition.py) | Mediation analysis: decompose a total effect into direct + indirect via a mediator. Linear model X→M→Y. Total = direct (X→Y holding M) + indirect (X→M→Y). Product method: indirect… | C++ |
| [`negative_control_outcome`](python/data-science/causal_inference_ii/negative_control_outcome.py) | Negative control outcome: a known-null outcome should remain null under clean analysis but light up under planted residual confounding. Detector for unobserved confounding. Core… | C++ |
| [`stratification_subclassification`](python/data-science/causal_inference_ii/stratification_subclassification.py) | Stratification/Subclassification: divide sample into propensity score strata. Divide into quintiles (or fewer) on propensity. Within each stratum, treatment is more balanced. ATE… | C++ |

### clustering_graph_and_anomaly

| Pattern | Description | Also in |
|---|---|---|
| [`betweenness_centrality`](python/data-science/clustering_graph_and_anomaly/betweenness_centrality.py) | Betweenness Centrality from scratch. Measures how often a node lies on shortest paths between other nodes. High betweenness indicates a "bridge" or connector node. Core idea: for… | C++ |
| [`classic_mds`](python/data-science/clustering_graph_and_anomaly/classic_mds.py) | Classical Multidimensional Scaling (MDS) from scratch. Non-linear dimensionality reduction: embed points in lower-dimensional space preserving pairwise distances. Core idea:… | C++ |
| [`dbscan_clustering`](python/data-science/clustering_graph_and_anomaly/dbscan_clustering.py) | DBSCAN Clustering from scratch. Density-based spatial clustering of applications with noise. Groups points that are close together (within eps distance) and have at least min_pts… | C++ |
| [`elbow_method_kmeans`](python/data-science/clustering_graph_and_anomaly/elbow_method_kmeans.py) | Elbow Method + K-Means from scratch. K-means: iterative clustering that minimizes within-cluster inertia. Elbow method: plot inertia vs. k and find the knee (largest drop in… | C++ |
| [`hierarchical_agglomerative`](python/data-science/clustering_graph_and_anomaly/hierarchical_agglomerative.py) | Hierarchical Agglomerative Clustering from scratch. Bottom-up merging of clusters using distance linkage (single or complete). Produces a dendrogram (tree structure) of nested… | C++ |
| [`isolation_tree_anomaly`](python/data-science/clustering_graph_and_anomaly/isolation_tree_anomaly.py) | Isolation Forest (Lite) Anomaly Detection from scratch. Ensemble of random isolation trees: points requiring fewer splits to isolate are likely anomalies (short average path… | C++ |
| [`label_propagation_communities`](python/data-science/clustering_graph_and_anomaly/label_propagation_communities.py) | Label Propagation for Community Detection from scratch. Iteratively propagate node labels throughout a graph: each node adopts the label held by most of its neighbors. Converges… | C++ |
| [`linear_discriminant_analysis`](python/data-science/clustering_graph_and_anomaly/linear_discriminant_analysis.py) | Linear Discriminant Analysis (LDA) from scratch. Two-class dimensionality reduction: find the linear projection that maximizes between-class variance relative to within-class… | C++ |
| [`random_projection_jl`](python/data-science/clustering_graph_and_anomaly/random_projection_jl.py) | Random Projection: Johnson-Lindenstrauss Lemma from scratch. Dimensionality reduction via random projection: project high-dimensional points onto a random subspace.… | C++ |
| [`silhouette_score`](python/data-science/clustering_graph_and_anomaly/silhouette_score.py) | Silhouette Score from scratch. Measure of clustering quality: how similar a point is to its own cluster vs. other clusters. Score ranges from -1 (wrong cluster) to 1… | C++ |

### composed_tools

| Pattern | Description | Also in |
|---|---|---|
| [`broker_term_extraction`](python/data-science/composed_tools/broker_term_extraction.py) | Broker-Term Extraction — the words that stand between topics and connect them. CROSS-CATEGORY COMPOSED PATTERN: betweenness_centrality (Clustering & Graph) x… | C++ |
| [`community_local_authority`](python/data-science/composed_tools/community_local_authority.py) | Community Local Authority — who matters inside each village, not in the empire. FUSED-BRIDGE COMPOSED PATTERN: label_propagation_communities x pagerank_power_iteration — proposed… | — |
| [`cross_domain_query_expansion`](python/data-science/composed_tools/cross_domain_query_expansion.py) | Cross-Domain Query Expansion — the query that goes looking for bridges. FUSED-BRIDGE COMPOSED PATTERN (third generation): broker_term_extraction (itself a composed child) x… | — |
| [`cross_domain_search_engine`](python/data-science/composed_tools/cross_domain_search_engine.py) | Cross-Domain Search Engine — a 4-pattern WORKFLOW that finds the bridges. PIPELINE-BRIDGE COMPOSED PATTERN (four stages, each feeds the next), found by pipeline_search over the… | — |
| [`dedup_pipeline`](python/data-science/composed_tools/dedup_pipeline.py) | Three-Stage Dedup Pipeline — find fast, verify exactly, explain honestly. CROSS-SPHERE COMPOSED PATTERN (three parents): minhash_dedup (DS) generates candidate pairs cheaply,… | C++ |
| [`dtw_shape_drift_monitor`](python/data-science/composed_tools/dtw_shape_drift_monitor.py) | DTW Shape-Drift Monitor — catching "the day looks wrong" when every point statistic looks fine. COMPOSED PATTERN: dtw_dynamic_time_warping (Optimization & Distances) x… | C++ |
| [`forest_size_by_variance`](python/data-science/composed_tools/forest_size_by_variance.py) | Forest Size by Variance — stop hiring trees when the crew is steady enough. FUSED-BRIDGE COMPOSED PATTERN: bias_variance_decomposition (Model Diagnostics) x random_forest… | — |
| [`interleaving_significance`](python/data-science/composed_tools/interleaving_significance.py) | Interleaving Significance — the duel names a winner; the bootstrap says if it's real. FUSED-BRIDGE COMPOSED PATTERN: ab_interleaving (Rankings & IR) x bootstrap_model_comparison… | — |
| [`kde_seeded_gmm`](python/data-science/composed_tools/kde_seeded_gmm.py) | KDE-Seeded Gaussian Mixture — the nonparametric scout guides the parametric army. COMPOSED PATTERN: kernel_density_estimation (Statistical Modeling) x gaussian_mixture_em (Core… | C++ |
| [`knn_kdtree_accelerated`](python/data-science/composed_tools/knn_kdtree_accelerated.py) | KD-Tree Accelerated k-NN — the search engine meets the classifier. CROSS-SPHERE COMPOSED PATTERN: kd_tree (programming sphere, awesome-python- patterns) x knn_classifier… | C++ |
| [`latency_percentile_monitor`](python/data-science/composed_tools/latency_percentile_monitor.py) | Latency Percentile Monitor — p99 tracking in five floats per quantile. CROSS-SPHERE COMPOSED PATTERN: metric_aggregator (programming sphere, awesome-python-patterns) x… | C++ |
| [`mutual_information_matrix`](python/data-science/composed_tools/mutual_information_matrix.py) | Mutual-Information Matrix — the dependence heatmap Pearson cannot draw. COMPOSED PATTERN: nonlinear_dependence_mi (Information Theory) x pearson_correlation_matrix… | C++ |
| [`queue_capacity_planner`](python/data-science/composed_tools/queue_capacity_planner.py) | Queue Capacity Planner — simulate your queue's future before you deploy it. CROSS-SPHERE COMPOSED PATTERN: async_task_queue (programming sphere, awesome-python-patterns) x… | C++ |
| [`rare_event_option_pricing`](python/data-science/composed_tools/rare_event_option_pricing.py) | Rare-Event Option Pricing — importance sampling where naive Monte Carlo goes blind. CROSS-SPHERE COMPOSED PATTERN: black_scholes_monte_carlo (Econometrics & Finance) x… | C++ |
| [`rolling_ols_update`](python/data-science/composed_tools/rolling_ols_update.py) | Rolling OLS Update — a running balance instead of a recount. FUSED-BRIDGE COMPOSED PATTERN: online_covariance (Streaming & Sketches) x sliding_window_regression (Time Series) —… | — |
| [`topic_aware_recommender`](python/data-science/composed_tools/topic_aware_recommender.py) | Topic-Aware Recommender — a 4-pattern WORKFLOW (premium solution template). PIPELINE-BRIDGE COMPOSED PATTERN (four stages, each output feeds the next), found by pipeline_search… | — |
| [`walk_forward_early_stopping`](python/data-science/composed_tools/walk_forward_early_stopping.py) | Walk-Forward Early Stopping — training halted by the future, not by a random split. COMPOSED PATTERN: early_stopping (Neural Networks) x walk_forward_validation (Time Series) —… | C++ |

### core_ml

| Pattern | Description | Also in |
|---|---|---|
| [`decision_tree_id3`](python/data-science/core_ml/decision_tree_id3.py) | Decision Tree Classifier using ID3 Algorithm (from scratch). Core idea: Recursively split data on the feature that gives the highest information gain (reduction in entropy). Build… | C++ |
| [`gaussian_mixture_em`](python/data-science/core_ml/gaussian_mixture_em.py) | Gaussian Mixture Model (1D) via Expectation-Maximization (from scratch). Core idea: Model data as a mixture of k Gaussian distributions. EM iteratively infers cluster… | C++ |
| [`kmeans_clustering`](python/data-science/core_ml/kmeans_clustering.py) | k-Means Clustering (from scratch). Core idea: Partition data into k clusters by iteratively assigning samples to the nearest centroid and updating centroids to be the mean of… | C++ |
| [`knn_classifier`](python/data-science/core_ml/knn_classifier.py) | k-Nearest Neighbors Classifier (from scratch). Core idea: To classify a new point, find the k nearest training samples using Euclidean distance and predict the majority class… | C++ |
| [`linear_regression_gd`](python/data-science/core_ml/linear_regression_gd.py) | Linear Regression via Batch Gradient Descent (from scratch). Core idea: Given labeled training data (X, y), fit a linear model y = Xw + b by iteratively updating weights w and… | C++ |
| [`logistic_regression`](python/data-science/core_ml/logistic_regression.py) | Binary Logistic Regression via Gradient Descent (from scratch). Core idea: Model binary classification via sigmoid(z) = 1 / (1 + e^-z). Given labeled data (X, y) where y ∈ {0, 1},… | C++ |
| [`naive_bayes_text`](python/data-science/core_ml/naive_bayes_text.py) | Multinomial Naive Bayes for Text Classification (from scratch). Core idea: Represent documents as word-frequency vectors. Assume features (word counts) are conditionally… | C++ |
| [`pca_power_iteration`](python/data-science/core_ml/pca_power_iteration.py) | Principal Component Analysis via Power Iteration (from scratch). Core idea: Find directions of maximum variance in data by computing eigenvalues and eigenvectors of the covariance… | C++, R |
| [`perceptron`](python/data-science/core_ml/perceptron.py) | Perceptron Learning Algorithm (from scratch). Core idea: A linear classifier for linearly separable data. The perceptron iteratively updates weights on misclassified samples using… | C++ |
| [`ridge_regression_normal_eq`](python/data-science/core_ml/ridge_regression_normal_eq.py) | Ridge Regression via Normal Equations (from scratch). Core idea: Linear regression with L2 regularization: minimize \|\|Xw - y\|\|^2 + λ\|\|w\|\|^2. Solved analytically via normal… | C++ |

### data_wrangling_from_scratch

| Pattern | Description | Also in |
|---|---|---|
| [`csv_type_inference`](python/data-science/data_wrangling_from_scratch/csv_type_inference.py) | CSV Type Inference. Read CSV and infer column types (int, float, date, str). We verify every column against planted data with explicit types. | C++ |
| [`dedupe_records_fuzzy`](python/data-science/data_wrangling_from_scratch/dedupe_records_fuzzy.py) | Fuzzy Record Deduplication. Normalize records and link near-duplicates via edit-distance threshold. We plant duplicates (with typos/variations) and verify they are identified. | C++ |
| [`group_by_aggregate`](python/data-science/data_wrangling_from_scratch/group_by_aggregate.py) | Group-By Aggregation (Multi-Key). Group records by one or more keys, then aggregate (sum, mean, count, min, max). We verify against a brute-force nested-loop computation on the… | C++ |
| [`hash_join_merge`](python/data-science/data_wrangling_from_scratch/hash_join_merge.py) | Hash Join: Inner and Left Join. Hash-based join of two tables on a key. We verify results match a brute-force nested-loop join. | C++ |
| [`melt_unpivot`](python/data-science/data_wrangling_from_scratch/melt_unpivot.py) | Melt (Unpivot): Wide to Long Format. Convert wide-format table back to long-format records. We verify that pivot(melt(data)) == data (round-trip). | C++ |
| [`pivot_table`](python/data-science/data_wrangling_from_scratch/pivot_table.py) | Pivot Table (Long to Wide). Convert long-format records to wide-format table with row/column headers and aggregation. We verify that pivot + row/column totals (margins) equal… | C++ |
| [`resample_timeseries_bins`](python/data-science/data_wrangling_from_scratch/resample_timeseries_bins.py) | Resample Time Series: Bucketing and Aggregation. Bucket timestamps into time bins (hourly, daily) and aggregate values. We verify that bin sums equal brute-force per-bin… | C++ |
| [`rolling_join_asof`](python/data-science/data_wrangling_from_scratch/rolling_join_asof.py) | As-Of Join (Rolling Join). For each row in left table, find the nearest preceding row in right table on a timestamp/key column. Used for merging trades with quotes at the same or… | C++ |
| [`sort_multi_key`](python/data-science/data_wrangling_from_scratch/sort_multi_key.py) | Multi-Key Sorting with Mixed Order (asc/desc). Sort records by multiple keys, each asc or desc. We verify STABILITY: records with equal keys stay in original order. | C++ |
| [`window_functions`](python/data-science/data_wrangling_from_scratch/window_functions.py) | Window Functions: row_number, rank, dense_rank, lag, lead, running sum. Per-partition window operations. We hand-verify on a small partition to show correctness. | C++ |

### econometrics_and_finance

| Pattern | Description | Also in |
|---|---|---|
| [`black_scholes_monte_carlo`](python/data-science/econometrics_and_finance/black_scholes_monte_carlo.py) | Black-Scholes Monte Carlo: European option pricing via simulation. True closed-form price vs MC estimate. Core claim: MC price within CI of closed-form; as simulations increase,… | C++ |
| [`bootstrap_portfolio_var`](python/data-science/econometrics_and_finance/bootstrap_portfolio_var.py) | Portfolio Value-at-Risk via bootstrap: nonparametric tail-risk estimation. VaR at confidence c is the (1−c) quantile of the RETURN distribution — the loss level the portfolio… | C++ |
| [`cointegration_engle_granger_lite`](python/data-science/econometrics_and_finance/cointegration_engle_granger_lite.py) | Engle-Granger cointegration test: detect a long-run equilibrium relationship. Two I(1) series are cointegrated if their linear combination is I(0) (stationary). The test is… | C++ |
| [`fixed_effects_within`](python/data-science/econometrics_and_finance/fixed_effects_within.py) | Fixed-effects estimator (within): removes time-invariant entity effects. Panel data: y_it = α_i + β·x_it + ε_it. Within-estimator demeansdata per entity, eliminating α_i. Core… | C++ |
| [`garch_lite_volatility_clustering`](python/data-science/econometrics_and_finance/garch_lite_volatility_clustering.py) | GARCH(1,1): volatility clustering via autoregressive conditional heteroskedasticity. σ²_t = ω + α·ε²_{t-1} + β·σ²_{t-1}. The ARCH coefficient α measures how strongly a large shock… | C++ |
| [`instrumental_2sls`](python/data-science/econometrics_and_finance/instrumental_2sls.py) | Two-stage least squares (2SLS): correct inference with endogenous regressor. Stage 1: x ~ z. Stage 2: y ~ x̂. Core claim: 2SLS recovers true coeff even with endogeneity; OLS is… | C++ |
| [`logit_marginal_effects`](python/data-science/econometrics_and_finance/logit_marginal_effects.py) | Logit marginal effects: average partial derivatives of predicted probability. AME = E[dP/dx]. Core claim: analytical gradient matches finite-difference check. Planted logit model;… | C++ |
| [`ols_robust_se_white`](python/data-science/econometrics_and_finance/ols_robust_se_white.py) | OLS robust standard errors (White): correct inference under heteroskedasticity. Naive SE assumes constant variance; White SE allows it to vary. Demonstrates: heteroskedastic data,… | C++ |
| [`sharpe_sortino_ratios`](python/data-science/econometrics_and_finance/sharpe_sortino_ratios.py) | Sharpe and Sortino ratios: risk-adjusted return metrics. Sharpe = (ret - rf) / σ. Sortino = (ret - rf) / σ_downside where σ_downside only counts downside (returns < target). Core… | C++ |
| [`value_averaging_vs_dca`](python/data-science/econometrics_and_finance/value_averaging_vs_dca.py) | Value Averaging vs Dollar Cost Averaging: compare final wealth. Dollar Cost Averaging (DCA): invest fixed $ each period. Value Averaging (VA): invest to reach a target portfolio… | C++ |

### ensembles_and_robust_methods

| Pattern | Description | Also in |
|---|---|---|
| [`adaboost`](python/data-science/ensembles_and_robust_methods/adaboost.py) | AdaBoost Classification with Decision Stumps. AdaBoost sequentially fits weak learners (decision stumps) by reweighting training examples: samples misclassified by the current… | C++ |
| [`bagging_variance_reduction`](python/data-science/ensembles_and_robust_methods/bagging_variance_reduction.py) | Bagging for Variance Reduction. Bagging (bootstrap aggregating) trains many copies of an UNSTABLE base learner on bootstrap resamples and averages them. The averaged predictor has… | C++ |
| [`gradient_boosting_stumps`](python/data-science/ensembles_and_robust_methods/gradient_boosting_stumps.py) | Gradient Boosting with Decision Stumps. Gradient boosting iteratively fits weak learners (depth-1 decision trees) to residuals of the previous ensemble, with each new tree… | C++ |
| [`huber_robust_regression`](python/data-science/ensembles_and_robust_methods/huber_robust_regression.py) | Huber Loss Robust Regression. Huber loss is a hybrid of squared loss (for small residuals) and absolute loss (for large residuals). It reduces sensitivity to outliers compared to… | C++ |
| [`random_forest`](python/data-science/ensembles_and_robust_methods/random_forest.py) | Random Forest Classification. Random forest builds multiple decision trees, each trained on a bootstrap sample of the data and with random feature subsets at each split. The… | C++ |
| [`ransac_robust_regression`](python/data-science/ensembles_and_robust_methods/ransac_robust_regression.py) | RANSAC (Random Sample Consensus) for Robust Regression. RANSAC iteratively selects random minimal subsets of data, fits models, and counts inliers (points close to the model). The… | C++ |
| [`spectral_clustering_lite`](python/data-science/ensembles_and_robust_methods/spectral_clustering_lite.py) | Spectral Clustering Lite. Spectral clustering constructs a graph Laplacian from pairwise affinities, computes its eigenvector (via power iteration), and clusters by the sign of… | C++ |
| [`stacking_ensemble`](python/data-science/ensembles_and_robust_methods/stacking_ensemble.py) | Stacking Ensemble with Meta-Learner. Stacking trains a meta-learner on predictions from base models trained via out-of-fold cross-validation. The meta-learner learns to combine… | C++ |
| [`theil_sen_estimator`](python/data-science/ensembles_and_robust_methods/theil_sen_estimator.py) | Theil-Sen Median-of-Slopes Estimator. Theil-Sen fits a line by computing slopes between all pairs of points and taking the median slope (robust to outliers). The intercept is the… | C++ |
| [`voting_classifier`](python/data-science/ensembles_and_robust_methods/voting_classifier.py) | Voting Classifier with Multiple Weak Learners. Voting combines predictions from multiple different base classifiers using hard voting (majority vote) or soft voting (average… | C++ |

### experiments_ii

| Pattern | Description | Also in |
|---|---|---|
| [`cluster_randomized_icc`](python/data-science/experiments_ii/cluster_randomized_icc.py) | Cluster randomization: treatment assigned at the cluster level, not the individual. Intracluster correlation (ICC) means observations within a cluster are not independent, so the… | C++ |
| [`minimum_detectable_effect`](python/data-science/experiments_ii/minimum_detectable_effect.py) | Minimum Detectable Effect (MDE): smallest effect size detectable with given n, α, power. Computed from normal approximation. Verified by simulation at multiple points. Core claim:… | C++ |
| [`msprt_lite`](python/data-science/experiments_ii/msprt_lite.py) | mSPRT (mixture Sequential Probability Ratio Test): an always-valid test. Under continuous peeking a fixed-α test inflates type-I badly. The mixture SPRT (Robbins) mixes the… | C++ |
| [`multi_armed_holm_correction`](python/data-science/experiments_ii/multi_armed_holm_correction.py) | Holm correction (step-down Bonferroni) for multiple comparisons. Many variants of a treatment tested; uncorrected testing breaks FWER over replications. Holm correction controls… | C++ |
| [`network_interference_demo`](python/data-science/experiments_ii/network_interference_demo.py) | Network interference: SUTVA violation where spillover through a graph biases ATE. Treatment on one user affects neighbors (e.g., social network). Naive ATE (individual… | C++ |
| [`novelty_effect_decay`](python/data-science/experiments_ii/novelty_effect_decay.py) | Novelty effect: early treatment boost that fades over time. First measurement of a treatment shows inflated effect; long-run effect is lower. Core claim: day-1 estimate overstates… | C++ |
| [`peeking_alpha_inflation`](python/data-science/experiments_ii/peeking_alpha_inflation.py) | Peeking alpha inflation: continuous peeking at a fixed-n test inflates type-I error. Run test, peek at p-value, continue collecting if not significant, re-test. This inflates… | C++ |
| [`post_stratification_variance`](python/data-science/experiments_ii/post_stratification_variance.py) | Post-stratification variance reduction: stratify AFTER observing data, using prognostic covariate. On a prognostic covariate (correlated with outcome but NOT treated), stratifying… | C++ |
| [`stratified_randomization`](python/data-science/experiments_ii/stratified_randomization.py) | Stratified randomization: randomize treatment within strata of a covariate. Better covariate balance + lower estimator variance vs simple randomization. Core claim: over seeded… | C++ |
| [`switchback_experiment_lite`](python/data-science/experiments_ii/switchback_experiment_lite.py) | Switchback experiment: time-block randomization for marketplace interference. Under interference (treating some users spills over to controls), a user-split A/B is BIASED: the… | C++ |

### fairness_privacy_and_robustness

| Pattern | Description | Also in |
|---|---|---|
| [`adversarial_perturbation_lite`](python/data-science/fairness_privacy_and_robustness/adversarial_perturbation_lite.py) | Adversarial Perturbation: gradient-sign attack on logistic classifier. Builds a simple logistic classifier from scratch, computes adversarial perturbation via gradient direction,… | C++ |
| [`covariate_shift_reweighting`](python/data-science/fairness_privacy_and_robustness/covariate_shift_reweighting.py) | Covariate Shift Reweighting: correct train/test distribution mismatch. Plants a covariate shift between train and test sets, estimates importance weights from density ratio, and… | C++ |
| [`demographic_parity_metrics`](python/data-science/fairness_privacy_and_robustness/demographic_parity_metrics.py) | Demographic Parity: measure fairness as equalized positive rates across groups. Tests that disparate impact ratio (minority positive rate / majority positive rate) and demographic… | C++ |
| [`differential_privacy_laplace`](python/data-science/fairness_privacy_and_robustness/differential_privacy_laplace.py) | Differential Privacy via Laplace Mechanism. Implements ε-differential privacy using Laplace noise on a count query. Verifies that the likelihood ratio of neighboring datasets is… | C++ |
| [`equalized_odds_thresholds`](python/data-science/fairness_privacy_and_robustness/equalized_odds_thresholds.py) | Equalized Odds: per-group thresholds equalize TPR across groups. Shows that a single global threshold cannot close a planted TPR gap between groups, but per-group thresholds can.… | C++ |
| [`group_calibration_audit`](python/data-science/fairness_privacy_and_robustness/group_calibration_audit.py) | Group Calibration Audit: verify per-group reliability of predicted probabilities. Creates two groups: one with well-calibrated predictions, one with miscalibrated. Measures… | C++ |
| [`k_anonymity_generalization`](python/data-science/fairness_privacy_and_robustness/k_anonymity_generalization.py) | k-Anonymity: generalize quasi-identifiers until each combination appears >= k times. Creates a dataset with age/gender quasi-identifiers, generalizes age ranges to achieve… | C++ |
| [`label_noise_robust_loss`](python/data-science/fairness_privacy_and_robustness/label_noise_robust_loss.py) | Label Noise Robustness: MAE degrades less than cross-entropy under label noise. Trains a simple classifier with noisy labels (20% symmetric label flip) and compares accuracy… | C++ |
| [`mnar_missingness_bias`](python/data-science/fairness_privacy_and_robustness/mnar_missingness_bias.py) | Missing Not At Random (MNAR): bias in naive complete-case analysis. Generates data with MNAR missingness (missing indicator depends on the value itself), compares complete-case… | C++ |
| [`randomized_response`](python/data-science/fairness_privacy_and_robustness/randomized_response.py) | Randomized Response: privacy-preserving survey technique. Each respondent answers honestly with probability p, lies with probability 1-p. True rate is recovered via… | C++ |

### geospatial_and_spatial

| Pattern | Description | Also in |
|---|---|---|
| [`convex_hull_graham`](python/data-science/geospatial_and_spatial/convex_hull_graham.py) | Graham scan: compute convex hull of a point set. Core idea: sort points by polar angle from lowest point, use stack to maintain left-turn invariant. Hull vertices are exactly the… | C++ |
| [`douglas_peucker`](python/data-science/geospatial_and_spatial/douglas_peucker.py) | Douglas-Peucker polyline simplification: reduce point count while bounding deviation. Core idea: find point with max distance to chord; if > epsilon, recurse on both halves;… | C++ |
| [`geohash_encode_decode`](python/data-science/geospatial_and_spatial/geohash_encode_decode.py) | Geohash: encode/decode lat/lon as interleaved bit string, base-32 encoded. Core idea: recursively bisect latitude and longitude, interleave bits, encode as base32. Neighbors share… | C++ |
| [`great_circle_waypoints`](python/data-science/geospatial_and_spatial/great_circle_waypoints.py) | Great-circle intermediate waypoints via spherical linear interpolation (slerp). Core idea: interpolate along great circle arc between two points on Earth sphere. Verify each… | C++ |
| [`grid_density_binning`](python/data-science/geospatial_and_spatial/grid_density_binning.py) | 2D grid density binning: partition points into cells, count per-cell density. Core idea: divide (minx,miny)-(maxx,maxy) into regular grid; assign points to cells; count occupancy.… | C++ |
| [`haversine_bearing`](python/data-science/geospatial_and_spatial/haversine_bearing.py) | Haversine great-circle distance and initial bearing. Core idea: compute geodetic distance between lat/lon points on Earth sphere, and the initial compass bearing from first to… | C++ |
| [`point_in_polygon`](python/data-science/geospatial_and_spatial/point_in_polygon.py) | Ray casting algorithm: test if a point is inside a polygon. Core idea: cast a ray from point to infinity; count edge crossings. Odd count = inside, even = outside. Handles concave… | C++ |
| [`polygon_area_centroid`](python/data-science/geospatial_and_spatial/polygon_area_centroid.py) | Shoelace formula: polygon area and centroid from vertex coordinates. Core idea: area via sum of cross products; centroid via weighted average. Works for both convex and concave… | C++ |
| [`quadtree_point_index`](python/data-science/geospatial_and_spatial/quadtree_point_index.py) | Quadtree: spatial indexing for range queries on 2D point sets. Core idea: recursively subdivide space into 4 quadrants; insert points; range query recursively searches overlapping… | C++ |
| [`spatial_radius_join`](python/data-science/geospatial_and_spatial/spatial_radius_join.py) | Radius join via grid bucketing: find all points-within-radius-of-centers pairs. Core idea: grid bucket points and centers; for each center, check points in nearby cells only.… | C++ |

### information_theory_and_probability

| Pattern | Description | Also in |
|---|---|---|
| [`bayes_diagnostic_test`](python/data-science/information_theory_and_probability/bayes_diagnostic_test.py) | Bayes' theorem for diagnostic testing: sensitivity/specificity/prevalence → PPV/NPV. Core idea: Positive Predictive Value (PPV) = P(disease \| positive test) depends critically on… | C++ |
| [`box_muller_gaussian`](python/data-science/information_theory_and_probability/box_muller_gaussian.py) | Box-Muller transform: generate Gaussian-distributed samples from uniform random variables. Core idea: Given two independent Uniform(0, 1) variables U1 and U2, compute Z1 = sqrt(-2… | C++ |
| [`conjugate_priors`](python/data-science/information_theory_and_probability/conjugate_priors.py) | Conjugate prior Bayesian updates: Beta-Binomial and Normal-Normal (known variance). Core idea: Conjugate priors have closed-form posterior updates. Beta prior on a Binomial… | C++ |
| [`entropy_estimators`](python/data-science/information_theory_and_probability/entropy_estimators.py) | Shannon entropy estimation from samples: naive plug-in vs Miller-Madow bias correction. Core idea: Naive plug-in uses empirical frequencies as probabilities; Miller-Madow… | C++ |
| [`hmm_forward_backward`](python/data-science/information_theory_and_probability/hmm_forward_backward.py) | HMM forward-backward algorithm: sequence likelihood and smoothed state posteriors. Core idea: Forward pass computes P(observation_sequence, hidden_state_t) at each step. Backward… | C++ |
| [`inverse_transform_sampling`](python/data-science/information_theory_and_probability/inverse_transform_sampling.py) | Inverse-transform sampling: generate samples from an arbitrary distribution via inverse CDF. Core idea: If U ~ Uniform(0, 1) and F^{-1} is the inverse CDF, then X = F^{-1}(U) is… | C++ |
| [`kl_divergence_cross_entropy`](python/data-science/information_theory_and_probability/kl_divergence_cross_entropy.py) | KL divergence, cross-entropy, and Jensen-Shannon divergence between discrete distributions. Core idea: KL divergence D(p\|\|q) = sum(p[i] * log(p[i]/q[i])) measures how q differs… | C++ |
| [`lln_clt_demo`](python/data-science/information_theory_and_probability/lln_clt_demo.py) | Law of Large Numbers and Central Limit Theorem: asymptotic behavior of sample means. Core idea: LLN: sample mean converges to population mean as n → ∞. CLT: the distribution of… | C++ |
| [`markov_chain_stationary`](python/data-science/information_theory_and_probability/markov_chain_stationary.py) | Markov chain stationary distribution via power iteration. Core idea: For a finite, ergodic Markov chain with transition matrix P, repeatedly multiply a probability vector by P^T… | C++ |
| [`nonlinear_dependence_mi`](python/data-science/information_theory_and_probability/nonlinear_dependence_mi.py) | Mutual information detects nonlinear dependence that Pearson correlation misses. Core idea: Pearson correlation measures LINEAR association; MI measures ANY dependence. For y =… | C++ |

### linear_algebra

| Pattern | Description | Also in |
|---|---|---|
| [`conjugate_gradient`](python/data-science/linear_algebra/conjugate_gradient.py) | Conjugate gradient: iterative solver for symmetric positive-definite systems. Solves A·x = b using search directions conjugate w.r.t. A. Core claim: converges in at most n… | C++ |
| [`gauss_seidel_vs_jacobi`](python/data-science/linear_algebra/gauss_seidel_vs_jacobi.py) | Gauss–Seidel vs Jacobi: convergence rate comparison. Both are stationary iterative solvers for A·x = b. Gauss–Seidel uses updated values immediately; Jacobi uses old values. Core… | C++ |
| [`householder_reflection`](python/data-science/linear_algebra/householder_reflection.py) | Householder reflection: zeros out components via hyperplane reflection. Given vector x, finds reflection matrix H = I - 2·v·v^T that maps x to [\|\|x\|\|, 0, 0, ...]. Used in QR,… | C++ |
| [`jacobi_eigen_symmetric`](python/data-science/linear_algebra/jacobi_eigen_symmetric.py) | Jacobi eigenvalue algorithm: iterative diagonalization of symmetric matrix. Applies Givens rotations to progressively zero off-diagonal elements. Core claim: converges to diagonal… | C++ |
| [`least_squares_qr`](python/data-science/linear_algebra/least_squares_qr.py) | Least-squares via QR: solve A·x ≈ b using numerically stable QR factorization. QR decomposes A into orthogonal Q and upper-triangular R. Then A·x = b becomes R·x = Q^T·b (small… | C++ |
| [`lu_decomposition_pivoting`](python/data-science/linear_algebra/lu_decomposition_pivoting.py) | LU decomposition with partial pivoting: PA = LU factorization. Permutation matrix P reorders rows for numerical stability; L and U satisfy PA = LU. Core claim: factorization… | C++ |
| [`matrix_condition_number`](python/data-science/linear_algebra/matrix_condition_number.py) | Matrix condition number: measure sensitivity to perturbations in A and b. κ(A) = \|\|A\|\| · \|\|A⁻¹\|\|. Large κ means small changes in A or b cause large changes in solution x.… | C++ |
| [`power_iteration_shifted`](python/data-science/linear_algebra/power_iteration_shifted.py) | Power iteration with shift: find smallest eigenvalue via (A - σI) iteration. Power iteration on A finds largest \|λ\|. Shifting by σ gives largest \|λ - σ\|, which is the smallest… | C++ |
| [`qr_gram_schmidt`](python/data-science/linear_algebra/qr_gram_schmidt.py) | QR decomposition via Gram–Schmidt: orthogonal Q and upper-triangular R. Iteratively orthogonalizes columns of A to produce Q. Core claim: Q is orthonormal (Q^T·Q = I), A = Q·R… | C++ |
| [`woodbury_rank1_update`](python/data-science/linear_algebra/woodbury_rank1_update.py) | Woodbury matrix identity: update A⁻¹ efficiently after rank-1 A change. If A_new = A + u·v^T, then (A_new)⁻¹ = A⁻¹ - (A⁻¹·u·v^T·A⁻¹) / (1 + v^T·A⁻¹·u). Core claim: inverse updated… | C++ |

### model_diagnostics

| Pattern | Description | Also in |
|---|---|---|
| [`bias_variance_decomposition`](python/data-science/model_diagnostics/bias_variance_decomposition.py) | Bias-Variance Decomposition Estimates bias and variance of a model using bootstrap resampling on synthetic data. Compares three models: constant (high bias), linear (good), and… | C++ |
| [`bootstrap_model_comparison`](python/data-science/model_diagnostics/bootstrap_model_comparison.py) | Bootstrap Model Comparison Compares two models using paired bootstrap resampling on the same test set. Computes the win rate: how often Model A is better than Model B across… | C++ |
| [`calibration_curve`](python/data-science/model_diagnostics/calibration_curve.py) | Calibration Curve & Brier Score Evaluates classifier calibration by binning predicted probabilities and comparing observed frequency vs predicted probability. Also computes Brier… | C++ |
| [`gaussian_naive_bayes`](python/data-science/model_diagnostics/gaussian_naive_bayes.py) | Gaussian Naive Bayes Classifier Implements a Gaussian Naive Bayes classifier for continuous features. Assumes each feature is independently distributed as Gaussian given the class… | C++ |
| [`learning_curve`](python/data-science/model_diagnostics/learning_curve.py) | Learning Curve Analysis Plots error vs training set size to assess model stability and data hunger. Verifies that training error increases and validation error decreases as… | C++ |
| [`lift_gain_chart`](python/data-science/model_diagnostics/lift_gain_chart.py) | Lift & Gain Chart Computes cumulative gain (% of positives captured) and lift (gain / base rate) by decile. Lift > 1 indicates the model is better than random. Use this in… | C++ |
| [`precision_recall_curve`](python/data-science/model_diagnostics/precision_recall_curve.py) | Precision-Recall Curve & Average Precision Computes PR curve by varying decision threshold on predicted scores. Average Precision (AP) summarizes the curve as area under the PR… | C++ |
| [`rank_correlation`](python/data-science/model_diagnostics/rank_correlation.py) | Rank Correlation (Spearman's rho & Kendall's tau) Computes Spearman's rank correlation (Pearson on ranks) and Kendall's tau (proportion of concordant pairs). Both measure… | C++ |
| [`residual_analysis`](python/data-science/model_diagnostics/residual_analysis.py) | Residual Analysis Fits a linear model to data with a planted quadratic term. Inspects residuals for structure (correlation with x^2 or runs test). Use this to detect model… | C++ |
| [`ucb_bandit`](python/data-science/model_diagnostics/ucb_bandit.py) | UCB1 Multi-Armed Bandit Implements the Upper Confidence Bound (UCB1) algorithm for the multi-armed bandit problem. UCB1 balances exploration and exploitation by selecting the arm… | C++ |

### model_understanding_and_tuning

| Pattern | Description | Also in |
|---|---|---|
| [`class_weight_imbalance`](python/data-science/model_understanding_and_tuning/class_weight_imbalance.py) | Class Weights for Imbalanced Classification Core idea: When classes are imbalanced (e.g., 95% negative, 5% positive), training loss can favor predicting the majority class.… | C++ |
| [`conformal_prediction_intervals`](python/data-science/model_understanding_and_tuning/conformal_prediction_intervals.py) | Split-Conformal Prediction Intervals for Regression Core idea: Split data into train/calibration. Train a regression model, then on calibration data compute residuals to set… | C++ |
| [`grid_vs_random_search`](python/data-science/model_understanding_and_tuning/grid_vs_random_search.py) | Grid Search vs Random Search: Demonstrating Random Search Efficiency Core idea: When hyperparameter space is high-dimensional but only a few params matter, random search explores… | C++ |
| [`model_persistence_roundtrip`](python/data-science/model_understanding_and_tuning/model_persistence_roundtrip.py) | Model Persistence Roundtrip (Save and Reload) Core idea: Train a model, serialize it to JSON, reload it, and verify predictions are identical (bit-for-bit for floats, or within… | C++ |
| [`partial_dependence_data`](python/data-science/model_understanding_and_tuning/partial_dependence_data.py) | Partial Dependence Plot (PD) — Data Generation Core idea: For each feature, marginalize over other features and plot the average model prediction as that feature varies. Linear… | C++ |
| [`permutation_feature_importance`](python/data-science/model_understanding_and_tuning/permutation_feature_importance.py) | Permutation Feature Importance Core idea: Shuffle each feature independently on held-out data and measure the drop in model performance. Features whose shuffling hurts performance… | C++ |
| [`platt_scaling_calibration`](python/data-science/model_understanding_and_tuning/platt_scaling_calibration.py) | Platt Scaling for Probability Calibration Core idea: When a classifier outputs uncalibrated scores (overconfident), fit a logistic function (Platt scaling) on a hold-out set to… | C++ |
| [`shapley_value_sampling`](python/data-science/model_understanding_and_tuning/shapley_value_sampling.py) | Shapley Value Sampling (Monte Carlo Approximation) Core idea: Estimate each feature's marginal contribution via random coalition sampling. For a simple additive model, sampled… | C++ |
| [`successive_halving`](python/data-science/model_understanding_and_tuning/successive_halving.py) | Successive Halving for Hyperparameter Optimization Core idea: Allocate more resources to promising configurations, halving the pool at each stage. Early elimination of poor… | C++ |
| [`threshold_tuning_cost`](python/data-science/model_understanding_and_tuning/threshold_tuning_cost.py) | Threshold Tuning with Asymmetric Misclassification Costs Core idea: Binary classifiers typically use 0.5 threshold, but with asymmetric costs (e.g., false negatives cost more than… | C++ |

### neural_networks_from_scratch

| Pattern | Description | Also in |
|---|---|---|
| [`conv1d_feature_detector`](python/data-science/neural_networks_from_scratch/conv1d_feature_detector.py) | 1D convolution layer learning to detect a planted motif in sequences. Core idea: Implement 1D convolution from scratch. Convolve a learnable kernel over a 1D sequence. Data… | C++ |
| [`dropout_regularization_sim`](python/data-science/neural_networks_from_scratch/dropout_regularization_sim.py) | Dropout regularization: network with vs without dropout on a noisy dataset. Core idea: Generate a small noisy dataset prone to overfitting. Train two networks: one with dropout… | C++ |
| [`early_stopping`](python/data-science/neural_networks_from_scratch/early_stopping.py) | Early stopping with patience-based validation monitoring. Core idea: Train a network and monitor validation loss each epoch. If validation loss doesn't improve for `patience`… | C++ |
| [`learning_rate_schedules`](python/data-science/neural_networks_from_scratch/learning_rate_schedules.py) | Learning rate schedules: constant vs step-decay vs cosine annealing. Core idea: Train the same network three times with different LR schedules on the same problem. Show that… | C++ |
| [`mlp_backprop`](python/data-science/neural_networks_from_scratch/mlp_backprop.py) | 2-Layer MLP trained by hand-derived backpropagation on XOR. Core idea: Manually implement the forward pass (linear -> sigmoid), backward pass (chain rule through sigmoid), and… | C++ |
| [`numerical_gradient_check`](python/data-science/neural_networks_from_scratch/numerical_gradient_check.py) | Verify analytic backprop gradients against finite-difference numerical gradients. Core idea: Compute gradients both ways (backprop and numerical finite-difference) on the same… | C++ |
| [`softmax_regression`](python/data-science/neural_networks_from_scratch/softmax_regression.py) | Multi-class softmax regression with cross-entropy loss. Core idea: Learn to classify 3 synthetic clusters in 2D using a linear classifier with softmax output and cross-entropy… | C++ |
| [`tiny_autoencoder`](python/data-science/neural_networks_from_scratch/tiny_autoencoder.py) | 1-hidden-layer autoencoder compressing correlated 8D data to 2D and back. Core idea: Encoder maps 8D input -> 2D bottleneck via sigmoid. Decoder maps 2D -> 8D reconstruction.… | C++ |
| [`weight_initialization_comparison`](python/data-science/neural_networks_from_scratch/weight_initialization_comparison.py) | Weight initialization comparison: naive vs Xavier/He initialization. Core idea: Build a deeper network (5 layers) and train it with three different initialization schemes: (1)… | C++ |
| [`word2vec_skipgram`](python/data-science/neural_networks_from_scratch/word2vec_skipgram.py) | Skip-gram word2vec with negative sampling on a tiny built-in corpus. Core idea: For each target word, predict context words using a learnable embedding matrix. Use negative… | C++ |

### numerical_methods

| Pattern | Description | Also in |
|---|---|---|
| [`adaptive_simpson`](python/data-science/numerical_methods/adaptive_simpson.py) | Adaptive Simpson's rule: automatic step refinement via error estimation. Compares Simpson's estimate on [a, b] with two estimates on [a, c] and [c, b]. If error is acceptable,… | C++ |
| [`bisection_newton_hybrid`](python/data-science/numerical_methods/bisection_newton_hybrid.py) | Hybrid bisection–Newton root-finding for robustness. Combines bisection's guaranteed convergence with Newton's speed: bisect when Newton drift is detected, switch back when safe.… | C++ |
| [`cubic_spline_interpolation`](python/data-science/numerical_methods/cubic_spline_interpolation.py) | Natural cubic spline: piecewise cubic interpolation with C² continuity. Solves tridiagonal system for interior knot second derivatives; uses them to define cubic polynomials on… | C++ |
| [`euler_vs_rk4_error_order`](python/data-science/numerical_methods/euler_vs_rk4_error_order.py) | Forward Euler vs RK4: measure convergence order difference. Solves same ODE with both methods at successive step sizes; measures error vs h. Core claim: Euler is O(h), RK4 is… | C++ |
| [`fixed_point_iteration`](python/data-science/numerical_methods/fixed_point_iteration.py) | Fixed-point iteration: find x where g(x) = x. Equivalently solves f(x) = 0 by reformulating as g(x) = x where g(x) = x - f(x). Core claim: convergence speed depends on \|g'(x*)\|;… | C++ |
| [`gauss_legendre_quadrature_lite`](python/data-science/numerical_methods/gauss_legendre_quadrature_lite.py) | Gauss–Legendre quadrature: optimal node placement for polynomial integration. Hardcoded nodes and weights for n=4 (integrates degree ≤7 polynomials exactly). Core claim: fewer… | C++ |
| [`richardson_extrapolation`](python/data-science/numerical_methods/richardson_extrapolation.py) | Richardson extrapolation: boost convergence order via linear combination. If F(h) ≈ L + C·h^p + O(h^(2p)) and the step is halved, then (2^p·F(h/2) - F(h))/(2^p - 1) ≈ L +… | C++ |
| [`rk4_ode_solver`](python/data-science/numerical_methods/rk4_ode_solver.py) | Fourth-order Runge–Kutta: standard explicit ODE integrator. Solves dy/dt = f(t, y) using 4-stage RK scheme with O(h⁵) local error. Core claim: high accuracy on smooth systems;… | C++ |
| [`romberg_integration`](python/data-science/numerical_methods/romberg_integration.py) | Romberg integration: Richardson extrapolation on trapezoid rule. Generates a table of progressively refined trapezoid estimates, then extrapolates to higher-order accuracy. Core… | C++ |
| [`secant_method`](python/data-science/numerical_methods/secant_method.py) | Secant method: Newton's speed without derivatives. Uses finite-difference slope from two prior points to approximate f'(x). Core claim: converges superlinearly (order ≈1.618)… | C++ |

### optimization_and_distances

| Pattern | Description | Also in |
|---|---|---|
| [`distance_metrics_toolkit`](python/data-science/optimization_and_distances/distance_metrics_toolkit.py) | DISTANCE METRICS: Euclidean, Manhattan, Minkowski, Chebyshev, Cosine Core idea: Unified toolkit for common distance metrics on vectors. Each metric emphasizes different aspects:… | C++ |
| [`dtw_dynamic_time_warping`](python/data-science/optimization_and_distances/dtw_dynamic_time_warping.py) | DISTANCE METRIC: Dynamic Time Warping (DTW) Core idea: Align two time series by warping time, allowing elastic matching of temporal patterns. DTW distance <= euclidean distance… | C++ |
| [`epsilon_greedy_bandit`](python/data-science/optimization_and_distances/epsilon_greedy_bandit.py) | OPTIMIZATION: Epsilon-Greedy Multi-Armed Bandit Core idea: In a multi-armed bandit, each arm yields stochastic reward. Epsilon-greedy balances exploration (try random arms) vs… | C++ |
| [`feature_scaling_toolkit`](python/data-science/optimization_and_distances/feature_scaling_toolkit.py) | FEATURE SCALING: Min-Max, Z-Score, Robust Scaling Core idea: Different scaling methods normalize features to comparable ranges. Min-max scales to [0, 1]; z-score centers to… | C++ |
| [`genetic_algorithm`](python/data-science/optimization_and_distances/genetic_algorithm.py) | OPTIMIZATION: Genetic Algorithm (Selection, Crossover, Mutation) Core idea: Population-based metaheuristic mimicking natural evolution. Iteratively select fit individuals, combine… | C++ |
| [`gradient_descent_momentum`](python/data-science/optimization_and_distances/gradient_descent_momentum.py) | OPTIMIZATION: Gradient Descent with Momentum Core idea: Vanilla gradient descent oscillates in narrow valleys; momentum accumulates velocity across iterations, smoothing the path… | C++ |
| [`hill_climbing_restarts`](python/data-science/optimization_and_distances/hill_climbing_restarts.py) | OPTIMIZATION: Hill Climbing with Random Restarts Core idea: Pure hill climbing gets stuck in local optima on rugged landscapes. Random restarts re-initialize from different points… | C++ |
| [`mahalanobis_distance`](python/data-science/optimization_and_distances/mahalanobis_distance.py) | DISTANCE METRIC: Mahalanobis Distance Core idea: Euclidean distance treats all dimensions equally; Mahalanobis accounts for covariance structure, scaling by the inverse covariance… | C++ |
| [`newton_method_optimization`](python/data-science/optimization_and_distances/newton_method_optimization.py) | OPTIMIZATION: Newton's Method for 1D Minimization Core idea: Use second-order (curvature) information via the Hessian to take smarter steps than gradient descent. Newton's method… | C++ |
| [`simulated_annealing`](python/data-science/optimization_and_distances/simulated_annealing.py) | OPTIMIZATION: Simulated Annealing Core idea: Mimic metallic annealing by accepting worse solutions with decreasing probability as "temperature" cools. Escapes local optima by… | C++ |

### preprocessing_and_eda

| Pattern | Description | Also in |
|---|---|---|
| [`covariance_matrix`](python/data-science/preprocessing_and_eda/covariance_matrix.py) | Covariance Matrix Pattern. Computes sample covariance between all numeric columns. Core idea: covariance measures how two variables jointly vary (sign = direction of relationship,… | C++ |
| [`data_profiling_summary`](python/data-science/preprocessing_and_eda/data_profiling_summary.py) | Data Profiling Summary Pattern. Per-column profile of a mixed dataset (numeric/categorical): type inference, missing count, cardinality, min/max/mean for numeric, top values for… | C++ |
| [`histogram_builder`](python/data-science/preprocessing_and_eda/histogram_builder.py) | Histogram Builder Pattern. Constructs a histogram using equal-width bins with automatic bin-count selection (Sturges' rule). Core idea: Sturges rule k = ceil(log2(n) + 1) works… | C++ |
| [`missing_value_imputation`](python/data-science/preprocessing_and_eda/missing_value_imputation.py) | Missing Value Imputation Pattern. Replaces None/NaN values with statistical estimates (mean, median, mode) or creates binary missing-indicator columns. Core idea: preserve sample… | C++ |
| [`one_hot_encoding`](python/data-science/preprocessing_and_eda/one_hot_encoding.py) | One-Hot Encoding Pattern. Converts categorical features into binary indicators (one-hot vectors). Core idea: represent each unique category value with a binary column per… | C++ |
| [`pearson_correlation_matrix`](python/data-science/preprocessing_and_eda/pearson_correlation_matrix.py) | Pearson Correlation Matrix Pattern. Computes pairwise Pearson correlation coefficients between all numeric columns from scratch. Core idea: measure linear association; correlation… | C++ |
| [`quantile_binning`](python/data-science/preprocessing_and_eda/quantile_binning.py) | Quantile Binning Pattern. Partitions a continuous numeric column into equal-frequency bins (quantile-based) vs equal-width bins. Core idea: quantile binning preserves bin counts… | C++ |
| [`random_oversampling_balance`](python/data-science/preprocessing_and_eda/random_oversampling_balance.py) | Random Oversampling and Synthetic Minority Balance Pattern. Rebalances imbalanced datasets by random oversampling (duplicate minority) and SMOTE-lite (interpolate between minority… | C++ |
| [`three_way_stratified_split`](python/data-science/preprocessing_and_eda/three_way_stratified_split.py) | Three-Way Stratified Split Pattern. Partitions a dataset into train/validation/test sets while preserving class proportions in all three splits. Core idea: stratification ensures… | C++ |
| [`winsorize_clip_outliers`](python/data-science/preprocessing_and_eda/winsorize_clip_outliers.py) | Winsorization and Clipping Pattern. Caps extreme values at percentile thresholds (winsorization) or hard bounds (clipping). Core idea: reduce influence of outliers while… | C++ |

### probabilistic_modeling

| Pattern | Description | Also in |
|---|---|---|
| [`bayesian_linear_regression`](python/data-science/probabilistic_modeling/bayesian_linear_regression.py) | Bayesian linear regression: conjugate normal prior, known noise, closed-form posterior. Core idea: prior N(μ₀, Σ₀); likelihood N(y \| Xβ, σ²I); posterior is N(μ_post, Σ_post) with… | C++ |
| [`bayesian_two_segment_changepoint`](python/data-science/probabilistic_modeling/bayesian_two_segment_changepoint.py) | Bayesian two-segment changepoint: marginal-likelihood comparison over split points. Core idea: compare model evidence for no-change vs change-at-t; find planted change location;… | C++ |
| [`dirichlet_multinomial`](python/data-science/probabilistic_modeling/dirichlet_multinomial.py) | Dirichlet-multinomial: conjugate posterior over category probabilities. Core idea: Dirichlet prior Dir(α) on probability simplex; observe multinomial counts; posterior is Dir(α +… | C++ |
| [`empirical_bayes_shrinkage`](python/data-science/probabilistic_modeling/empirical_bayes_shrinkage.py) | Empirical Bayes shrinkage (James-Stein style): shrink group means toward grand mean. Core idea: estimate hyperparameter from data; shrink group means via Bayesian posterior. Total… | C++ |
| [`gamma_poisson_conjugate`](python/data-science/probabilistic_modeling/gamma_poisson_conjugate.py) | Gamma-Poisson conjugate prior: Gamma prior on Poisson rate parameter. Core idea: prior Gamma(α, β); observe Poisson counts; posterior is Gamma(α + Σcount, β + n). Sequential… | C++ |
| [`gaussian_process_lite`](python/data-science/probabilistic_modeling/gaussian_process_lite.py) | Gaussian process regression (lite): RBF kernel, small n, direct Cholesky solve. Core idea: place Gaussian priors on function values; posterior mean interpolates training data.… | C++ |
| [`hmm_baum_welch`](python/data-science/probabilistic_modeling/hmm_baum_welch.py) | HMM Baum-Welch (EM) training: learn emission and transition probabilities. Core idea: E-step computes forward-backward statistics; M-step re-estimates parameters. Likelihood… | C++ |
| [`particle_filter_1d`](python/data-science/probabilistic_modeling/particle_filter_1d.py) | Particle filter (SMC): track a noisy 1D random walk target. Core idea: maintain weighted particles; predict, weight by observation likelihood, resample. Particle-mean RMSE beats… | C++ |
| [`rejection_sampling`](python/data-science/probabilistic_modeling/rejection_sampling.py) | Rejection sampling: sample from complex density under an envelope. Core idea: sample from proposal, accept with probability p(x) / (M * q(x)). Empirical moments match… | C++ |
| [`rts_kalman_smoother`](python/data-science/probabilistic_modeling/rts_kalman_smoother.py) | RTS (Rauch-Tung-Striebel) Kalman smoother: forward-backward pass for optimal smoothing. Core idea: forward Kalman filter, then backward pass corrects trajectory. Smoothed RMSE <… | C++ |

### probability_iii

| Pattern | Description | Also in |
|---|---|---|
| [`banach_matchbox_or_gambler_ruin`](python/data-science/probability_iii/banach_matchbox_or_gambler_ruin.py) | Gambler's ruin: absorption probability of a bounded ±1 random walk. A gambler starts with wealth a against an opponent with b (total N = a+b); each play moves wealth ±1 (P(+1)=p).… | C++ |
| [`benford_law_test`](python/data-science/probability_iii/benford_law_test.py) | Benford's law: leading digit distribution in many real datasets. P(digit d) = log₁₀(1 + 1/d) for d ∈ {1,...,9}. Multiplicative data follows; uniform data violates it. Chi-square… | C++ |
| [`birthday_paradox_exact_vs_sim`](python/data-science/probability_iii/birthday_paradox_exact_vs_sim.py) | Birthday paradox: analytical vs simulated collision probability. P(≥2 same birthday in n people) ≈ 1 - n!/((365)^n · (365-n)!). Planted n values; analytic and simulated agree. | C++ |
| [`copula_gaussian_lite`](python/data-science/probability_iii/copula_gaussian_lite.py) | Gaussian copula: model dependence structure separately from marginals. Copula C(u, v) = P(U ≤ u, V ≤ v) where U, V ~ uniform; independence is C = uv. Core claim: rank correlation… | C++ |
| [`coupon_collector`](python/data-science/probability_iii/coupon_collector.py) | Coupon collector: expected trials to collect all n distinct items. E[T] = n·H_n where H_n = 1 + 1/2 + ... + 1/n is harmonic series. Core claim: simulated mean matches n·H_n;… | C++ |
| [`extreme_value_block_maxima`](python/data-science/probability_iii/extreme_value_block_maxima.py) | Block maxima: fit Gumbel distribution to extreme values for return-level estimation. Core claim: planted return level recovered; CDF fit verified on known quantiles. | C++ |
| [`inclusion_exclusion_derangements`](python/data-science/probability_iii/inclusion_exclusion_derangements.py) | Inclusion-exclusion: count derangements (permutations with no fixed points). !n = n! · Σ (−1)^k / k! ≈ n! / e. Core claim: exact formula matches simulation; !n / n! → 1/e as n → ∞. | C++ |
| [`polya_urn_reinforcement`](python/data-science/probability_iii/polya_urn_reinforcement.py) | Pólya urn: reinforcement model whose limiting proportion is RANDOM ~ Beta(a, b). Start with a balls of color A, b of color B. Each draw: pick a ball, return it plus one more of… | C++ |
| [`quantile_mapping_bias_correction`](python/data-science/probability_iii/quantile_mapping_bias_correction.py) | Quantile mapping: correct distributional bias by matching quantiles. Maps biased distribution onto reference via quantile alignment. Core claim: post-correction quantiles match… | C++ |
| [`stirling_approximation_error`](python/data-science/probability_iii/stirling_approximation_error.py) | Stirling's approximation: log(n!) ≈ n·log(n) - n + 0.5·log(2πn). Core claim: relative error shrinks as n grows; error measured vs exact factorial. | C++ |

### rankings_and_information_retrieval

| Pattern | Description | Also in |
|---|---|---|
| [`ab_interleaving`](python/data-science/rankings_and_information_retrieval/ab_interleaving.py) | Team-Draft Interleaving for A/B Testing Rankers. Compare two rankers (A and B) by interleaving their results in a single ranking. Users click on interleaved results. The ranker… | C++ |
| [`bm25_ranking`](python/data-science/rankings_and_information_retrieval/bm25_ranking.py) | BM25 Ranking (Okapi BM25). BM25 ranks documents by relevance to a query via TF-IDF with saturation and length normalization. BM25 outperforms raw TF on length-biased corpora (long… | C++ |
| [`elo_rating`](python/data-science/rankings_and_information_retrieval/elo_rating.py) | Elo Rating System. Maintain skill ratings via pairwise wins/losses. Elo(new) = Elo(old) + K * (observed - expected). Expected score = 1 / (1 + 10^((opponent_elo - my_elo)/400)).… | C++ |
| [`inverted_index_search`](python/data-science/rankings_and_information_retrieval/inverted_index_search.py) | Inverted Index and Boolean Search. Build an inverted index (term → docs), then answer AND/OR queries. We verify that planted relevant docs are retrieved, irrelevant excluded, and… | C++ |
| [`mean_reciprocal_rank`](python/data-science/rankings_and_information_retrieval/mean_reciprocal_rank.py) | Ranking metrics suite: Mean Reciprocal Rank, Precision@K, Recall@K. MRR = mean over queries of 1/(rank of the first relevant item). Precision@K = \|relevant ∩ top-K\| / K.… | C++ |
| [`ndcg_evaluation`](python/data-science/rankings_and_information_retrieval/ndcg_evaluation.py) | NDCG (Normalized Discounted Cumulative Gain). Evaluate ranking quality: DCG sums relevance scores discounted by position. NDCG normalizes DCG by ideal DCG (perfect ranking).… | C++ |
| [`pairwise_ranking_learn`](python/data-science/rankings_and_information_retrieval/pairwise_ranking_learn.py) | Pairwise Ranking via Logistic Regression. Learn item ordering from pairwise comparisons: for each pair (i,j), fit logistic regression on feature difference (f_i - f_j) to predict… | C++ |
| [`position_bias_click_model`](python/data-science/rankings_and_information_retrieval/position_bias_click_model.py) | Position Bias in Click Models and Inverse Propensity Weighting. Users click documents based on both relevance and position (position bias). Naive click-count ranking is confounded… | C++ |
| [`query_expansion_prf`](python/data-science/rankings_and_information_retrieval/query_expansion_prf.py) | Pseudo-Relevance Feedback (PRF) for Query Expansion. Expand a query with terms from top-k initially-retrieved docs. PRF finds synonym/related-term docs that the raw query misses.… | C++ |
| [`rank_fusion_rrf`](python/data-science/rankings_and_information_retrieval/rank_fusion_rrf.py) | Reciprocal Rank Fusion (RRF). Combine multiple rankers via RRF: score = Σ (1 / (k + rank_i)). Fusion often beats individual rankers on noisy signals. We plant two mediocre rankers… | C++ |

### recommenders_and_graph_sampling

| Pattern | Description | Also in |
|---|---|---|
| [`apriori_frequent_itemsets`](python/data-science/recommenders_and_graph_sampling/apriori_frequent_itemsets.py) | Apriori algorithm for frequent itemsets and association rules. Core idea: iteratively find frequent itemsets by checking support thresholds, then generate association rules with… | C++ |
| [`bayesian_ab_beta`](python/data-science/recommenders_and_graph_sampling/bayesian_ab_beta.py) | Bayesian A/B testing with Beta-Binomial posteriors. Core idea: model each variant's success rate as Beta distribution, update posterior with observed data (successes + failures),… | C++ |
| [`iqr_outlier_detection`](python/data-science/recommenders_and_graph_sampling/iqr_outlier_detection.py) | IQR-based outlier detection. Core idea: compute the interquartile range (Q3 - Q1), then flag any value outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR] as an outlier. When to use: for… | C++ |
| [`item_based_cf`](python/data-science/recommenders_and_graph_sampling/item_based_cf.py) | Item-based collaborative filtering. Core idea: compute adjusted-cosine similarity between item rating vectors (normalize by subtracting per-user mean), then recommend top-k unseen… | C++ |
| [`matrix_factorization_sgd`](python/data-science/recommenders_and_graph_sampling/matrix_factorization_sgd.py) | Matrix factorization via stochastic gradient descent. Core idea: decompose a sparse rating matrix into user (U) and item (V) factor matrices of low rank, trained by SGD to… | C++ |
| [`monte_carlo_estimation`](python/data-science/recommenders_and_graph_sampling/monte_carlo_estimation.py) | Monte Carlo estimation: pi and definite integrals. Core idea: estimate quantities via random sampling. For pi: sample points in a unit square, count those inside the inscribed… | C++ |
| [`mutual_information_feature_selection`](python/data-science/recommenders_and_graph_sampling/mutual_information_feature_selection.py) | Mutual information for feature selection. Core idea: compute entropy and mutual information between discrete features and a label, then rank features by MI. Informative features… | C++ |
| [`pagerank_power_iteration`](python/data-science/recommenders_and_graph_sampling/pagerank_power_iteration.py) | PageRank via power iteration. Core idea: iterate score propagation through a directed graph where each node distributes its score equally to outgoing neighbors, with damping… | C++ |
| [`thompson_sampling_bandit`](python/data-science/recommenders_and_graph_sampling/thompson_sampling_bandit.py) | Thompson sampling for multi-armed bandits. Core idea: maintain Beta posteriors over success probability for each arm, sample from each posterior, pull the arm with highest sample,… | C++ |
| [`user_based_cf`](python/data-science/recommenders_and_graph_sampling/user_based_cf.py) | User-based collaborative filtering. Core idea: compute cosine similarity between user rating vectors, then predict ratings for unseen items as a weighted average of similar users'… | C++ |

### recommenders_ii_kept_survivors

| Pattern | Description | Also in |
|---|---|---|
| [`catalog_coverage_diversity`](python/data-science/recommenders_ii_kept_survivors/catalog_coverage_diversity.py) | Catalog coverage and diversity of recommendations. Measures the fraction of the overall catalog that appears in a recommendation list. A diverse list exposes more of the catalog,… | C++ |
| [`content_tfidf_rec`](python/data-science/recommenders_ii_kept_survivors/content_tfidf_rec.py) | Content-based TF-IDF recommendation: recommend items similar in content. Core claim: content similarity recommends the planted same-topic item (top-1 correct). | C++ |
| [`intra_list_diversity`](python/data-science/recommenders_ii_kept_survivors/intra_list_diversity.py) | Intra-list diversity (ILD) of a recommendation list. ILD measures how different the recommended items are from one another by averaging pairwise dissimilarity over the list.… | C++ |
| [`novelty_serendipity`](python/data-science/recommenders_ii_kept_survivors/novelty_serendipity.py) | Novelty and serendipity: how unexpected / long-tail are recommendations. Novelty is measured as the average inverse popularity of recommended items. Long-tail, rarely-popular… | C++ |

### signal_processing_and_sequences

| Pattern | Description | Also in |
|---|---|---|
| [`autocovariance_spectrum`](python/data-science/signal_processing_and_sequences/autocovariance_spectrum.py) | Autocovariance and Power Spectral Density (Periodogram). Periodogram = DFT of autocovariance function. For a signal with strong periodicity, the periodogram should show a peak at… | C++ |
| [`convolution_filtering`](python/data-science/signal_processing_and_sequences/convolution_filtering.py) | Convolution and Filtering. Convolve a signal with a kernel via discrete convolution: y[n] = Σ x[k] * h[n-k]. Demonstrate smoothing (moving average kernel) and edge detection… | C++ |
| [`cross_correlation_lag`](python/data-science/signal_processing_and_sequences/cross_correlation_lag.py) | Cross-Correlation and Lag Detection. Compute cross-correlation between two signals. The lag at which cross-correlation is maximum indicates the time shift between signals. We… | C++ |
| [`discrete_fourier_transform`](python/data-science/signal_processing_and_sequences/discrete_fourier_transform.py) | Discrete Fourier Transform (DFT) from Scratch. Convert time-domain signal to frequency-domain via DFT. DFT[k] = Σ x[n] * exp(-2πi*k*n/N). We plant known frequencies in a signal… | C++ |
| [`dynamic_range_compression`](python/data-science/signal_processing_and_sequences/dynamic_range_compression.py) | Dynamic Range Compression via Logarithm and μ-Law. Compress large dynamic range (e.g., audio amplitudes or intensity values) into a narrower range while preserving relative… | C++ |
| [`fft_cooley_tukey`](python/data-science/signal_processing_and_sequences/fft_cooley_tukey.py) | FFT via Cooley-Tukey Algorithm. Recursive divide-and-conquer FFT: O(N log N) vs naive DFT O(N²). Works on power-of-2 lengths. FFT should produce same result as naive DFT, and… | C++ |
| [`hampel_filter_outliers`](python/data-science/signal_processing_and_sequences/hampel_filter_outliers.py) | Hampel Filter for Outlier Detection and Removal. Use rolling-median and MAD (median absolute deviation) to detect outliers. Replace outliers with the rolling median. Outliers are… | C++ |
| [`peak_detection`](python/data-science/signal_processing_and_sequences/peak_detection.py) | Peak Detection via Prominence. Find local maxima in a signal using prominence: height above the baseline (minimum of the valleys to the left and right). Detect planted peaks;… | C++ |
| [`resampling_interpolation`](python/data-science/signal_processing_and_sequences/resampling_interpolation.py) | Resampling and Interpolation. Upsample or downsample a time series via interpolation. Demonstrate linear interpolation and nearest-neighbor. On smooth signals, linear should… | C++ |
| [`savitzky_golay_lite`](python/data-science/signal_processing_and_sequences/savitzky_golay_lite.py) | Savitzky-Golay Filter (Local Polynomial Smoothing). Fit a low-order polynomial (e.g., quadratic) to a rolling window. Smoother than moving-average and preserves peak heights… | C++ |

### simulation_and_decision_science

| Pattern | Description | Also in |
|---|---|---|
| [`discrete_event_simulation`](python/data-science/simulation_and_decision_science/discrete_event_simulation.py) | Discrete Event Simulation: service desk with event queue. Uses heapq for event-driven simulation. Verifies conservation: arrivals == served + still-in-system. Also shows waits… | C++ |
| [`kelly_criterion`](python/data-science/simulation_and_decision_science/kelly_criterion.py) | Kelly Criterion: optimal betting fraction for long-run log-growth. Kelly fraction f* = (p*b - q) / b where p = win prob, q = loss prob, b = odds. Overbetting (2x Kelly) produces… | C++ |
| [`mm1_queue_littles_law`](python/data-science/simulation_and_decision_science/mm1_queue_littles_law.py) | M/M/1 Queue: verify Little's Law and analytic formulas. Simulates an M/M/1 queue (Poisson arrivals, exponential service). Verifies Little's Law: L ≈ λW. Also compares to analytic… | C++ |
| [`monte_carlo_var_es`](python/data-science/simulation_and_decision_science/monte_carlo_var_es.py) | Monte Carlo VaR & ES: Value-at-Risk and Expected Shortfall on returns. Computes Value-at-Risk (VaR) and Expected Shortfall (ES) on heavy-tailed synthetic returns. Verifies ES >=… | C++ |
| [`newsvendor_critical_fractile`](python/data-science/simulation_and_decision_science/newsvendor_critical_fractile.py) | Newsvendor Problem: optimal stock at critical fractile. Optimal order quantity is the critical fractile of demand. Profit at optimal quantity exceeds over/under stocking, measured… | C++ |
| [`q_learning_gridworld`](python/data-science/simulation_and_decision_science/q_learning_gridworld.py) | Q-Learning on Gridworld: reach value iteration policy through off-policy learning. Tabular Q-learning on the same 4x4 gridworld. After sufficient episodes, Q-learning converges to… | C++ |
| [`schelling_segregation`](python/data-science/simulation_and_decision_science/schelling_segregation.py) | Schelling Segregation: mild preference produces high global segregation. Agents prefer neighbors of same type with threshold >= 30%. Simulation shows high global segregation… | C++ |
| [`sir_epidemic_model`](python/data-science/simulation_and_decision_science/sir_epidemic_model.py) | SIR Epidemic Model: discrete simulation of S-I-R dynamics. Discrete SIR: tracks susceptible, infected, recovered counts. Verifies conservation S + I + R = N every step, and… | C++ |
| [`tornado_sensitivity`](python/data-science/simulation_and_decision_science/tornado_sensitivity.py) | Tornado Sensitivity: one-at-a-time sensitivity analysis. Simple profit model: profit = (revenue - cost - overhead). OAT sensitivity varies each input by +/- 10% and measures… | C++ |

### statistical_modeling

| Pattern | Description | Also in |
|---|---|---|
| [`em_two_coins`](python/data-science/statistical_modeling/em_two_coins.py) | Expectation-Maximization (EM) Algorithm: Two-Coin Problem. Estimates two coin biases from mixed flip sessions without labels. The classic EM example: data is ambiguous (which coin… | C++ |
| [`gibbs_sampling_bivariate`](python/data-science/statistical_modeling/gibbs_sampling_bivariate.py) | Gibbs Sampling for Bivariate Normal Distribution. Alternately samples each variable from its conditional distribution. Recovers correlation structure from a correlated bivariate… | C++ |
| [`importance_sampling`](python/data-science/statistical_modeling/importance_sampling.py) | Importance Sampling for Expectation Estimation. Estimates E_target[h(X)] using samples from a proposal, re-weighted by the ratio. Useful when the target is hard to sample but easy… | C++ |
| [`kaplan_meier_survival`](python/data-science/statistical_modeling/kaplan_meier_survival.py) | Kaplan-Meier Survival Curve with Censored Observations. Estimates a survival function from time-to-event data with right censoring. Computes the product of (1 - events/at_risk) at… | C++ |
| [`kernel_density_estimation`](python/data-science/statistical_modeling/kernel_density_estimation.py) | Kernel Density Estimation (KDE) with Gaussian Kernel & Silverman Bandwidth. Non-parametric density estimation via kernel smoothing. Bandwidth chosen by Silverman's rule: h =… | C++ |
| [`loess_local_regression`](python/data-science/statistical_modeling/loess_local_regression.py) | LOESS-Lite: Locally Weighted Linear Regression. Fits a piecewise linear regression using tricube-weighted local neighborhoods. Simple non-parametric smoothing for noisy signals.… | C++ |
| [`metropolis_hastings_mcmc`](python/data-science/statistical_modeling/metropolis_hastings_mcmc.py) | Metropolis-Hastings MCMC Sampling. Samples from a target distribution using a random-walk proposal. Accepts/rejects proposals based on the Metropolis-Hastings ratio. Use when you… | C++ |
| [`polynomial_regression`](python/data-science/statistical_modeling/polynomial_regression.py) | Polynomial Regression via Least Squares (Vandermonde Design Matrix). A polynomial regression solver using Gaussian elimination on the Vandermonde matrix. Fits a degree-d… | C++ |
| [`power_analysis_sample_size`](python/data-science/statistical_modeling/power_analysis_sample_size.py) | Power Analysis: Sample Size for Two-Proportion Z-Test. Computes required sample size per group for a given effect size, alpha, and power using normal approximation. Verifies the… | C++ |
| [`quantile_regression_pinball`](python/data-science/statistical_modeling/quantile_regression_pinball.py) | Quantile Regression via Pinball Loss and Gradient Descent. Estimates conditional quantiles (e.g., median, 90th percentile) by minimizing the pinball (check) loss: L_tau(y, pred) =… | C++ |

### statistics_and_testing

| Pattern | Description | Also in |
|---|---|---|
| [`ab_test_proportions`](python/data-science/statistics_and_testing/ab_test_proportions.py) | A/B Test for Two Proportions Core idea: Test whether two conversion rates differ using a z-test for proportions. Compute pooled standard error under the null, then the… | C++ |
| [`benjamini_hochberg`](python/data-science/statistics_and_testing/benjamini_hochberg.py) | Benjamini-Hochberg False Discovery Rate Correction Core idea: When testing many hypotheses, Bonferroni is overly conservative. Benjamini-Hochberg controls the False Discovery Rate… | C++ |
| [`bootstrap_confidence_interval`](python/data-science/statistics_and_testing/bootstrap_confidence_interval.py) | Bootstrap Confidence Interval for Sample Mean Core idea: Resample the observed data WITH replacement many times to build an empirical distribution of sample statistics. Extract… | C++ |
| [`chi_square_independence`](python/data-science/statistics_and_testing/chi_square_independence.py) | Chi-Square Test of Independence Core idea: Test whether two categorical variables are independent. Compute expected frequencies under independence, then compare observed vs… | C++, R |
| [`confusion_matrix_metrics`](python/data-science/statistics_and_testing/confusion_matrix_metrics.py) | Confusion Matrix and Classification Metrics Core idea: Build a confusion matrix (TP, FP, TN, FN) from binary predictions and true labels. Compute precision (TP/(TP+FP)), recall… | C++ |
| [`permutation_test`](python/data-science/statistics_and_testing/permutation_test.py) | Permutation Test for Two-Sample Difference of Means Core idea: Under the null hypothesis (no group difference), group labels are exchangeable. Randomly permute group assignments… | C++ |
| [`reservoir_sampling`](python/data-science/statistics_and_testing/reservoir_sampling.py) | Reservoir Sampling (Algorithm R) Core idea: Sample k items uniformly from a stream of unknown length without storing the entire stream. Maintain a "reservoir" of k items; for each… | C++ |
| [`roc_auc_from_scratch`](python/data-science/statistics_and_testing/roc_auc_from_scratch.py) | ROC Curve and AUC Computation Core idea: For binary classification with probabilistic predictions, compute TPR (recall) and FPR at various thresholds to build the ROC curve. AUC… | C++ |
| [`train_test_split_kfold`](python/data-science/statistics_and_testing/train_test_split_kfold.py) | Train/Test Split and K-Fold Cross-Validation Core idea: Split data into train/test subsets for model evaluation. Extend to k-fold CV where data is divided into k folds; iterate k… | C++ |

### streaming_and_sketches

| Pattern | Description | Also in |
|---|---|---|
| [`count_min_sketch`](python/data-science/streaming_and_sketches/count_min_sketch.py) | Count-Min Sketch for Frequency Estimation Core idea: A streaming data structure using hash functions to estimate item frequencies with bounded error. Memory-efficient alternative… | C++, Rust |
| [`online_covariance`](python/data-science/streaming_and_sketches/online_covariance.py) | Online Covariance & Correlation via Welford's Method Core idea: Update mean, variance, and covariance in a single pass via numerically-stable incremental formulas. Matches batch… | C++ |
| [`online_sgd_classifier`](python/data-science/streaming_and_sketches/online_sgd_classifier.py) | Online Stochastic Gradient Descent Classifier Core idea: Train a logistic regressor in a single pass over a stream via SGD, updating weights with each sample. Should converge… | C++ |
| [`p2_quantile_estimator`](python/data-science/streaming_and_sketches/p2_quantile_estimator.py) | P² Quantile Estimator (Jain & Chlamtac, 1985) — streaming quantiles in O(1) memory. The REAL P² algorithm: exactly FIVE markers track (min, p/2, p, (1+p)/2, max). Each new… | C++ |
| [`page_hinkley_drift`](python/data-science/streaming_and_sketches/page_hinkley_drift.py) | Page-Hinkley Test for Streaming Drift Detection Core idea: Monitor cumulative sum of (residuals - threshold) to detect if the distribution has shifted. High positive sum indicates… | C++ |
| [`sliding_window_extrema`](python/data-science/streaming_and_sketches/sliding_window_extrema.py) | Sliding Window Min/Max via Monotonic Deque Core idea: Maintain a deque of indices whose values are monotone. Each new element replaces non-competitive elements in O(1) amortized… | C++ |
| [`space_saving_heavy_hitters`](python/data-science/streaming_and_sketches/space_saving_heavy_hitters.py) | Space-Saving Algorithm for Top-K Heavy Hitters Core idea: Maintain exactly k counters for the top-k most frequent items seen so far. When a new item arrives, either increment an… | C++ |
| [`streaming_histogram_merge`](python/data-science/streaming_and_sketches/streaming_histogram_merge.py) | Streaming Histogram with Bin Merging Core idea: Maintain a fixed-size histogram on a stream. When bins exceed the limit, merge adjacent bins to free space. Trade-off: quantile… | C++ |
| [`streaming_kmeans`](python/data-science/streaming_and_sketches/streaming_kmeans.py) | Streaming k-means (Online Clustering) Core idea: Update cluster centroids incrementally as data streams in, without storing all points. On slowly-drifting data, centroids track… | C++ |
| [`weighted_reservoir_sampling`](python/data-science/streaming_and_sketches/weighted_reservoir_sampling.py) | Weighted Reservoir Sampling (A-Res Algorithm) Core idea: Sample k items from a weighted stream such that inclusion probability is proportional to item weight. A-Res: use u^(1/w)… | C++ |

### streaming_iii

| Pattern | Description | Also in |
|---|---|---|
| [`adwin_drift_detector`](python/data-science/streaming_iii/adwin_drift_detector.py) | ADWIN0 adaptive-windowing drift detector (Bifet & Gavalda, 2007). Core idea: keep a window of recent values; after each arrival, try EVERY split of the window into an older part… | C++ |
| [`bloom_filter_fpr`](python/data-science/streaming_iii/bloom_filter_fpr.py) | Bloom filter with measured false-positive rate. Core idea: hash items to k positions in a bit array; false positive = query position all set but item not inserted. When: test… | C++ |
| [`concept_drift_ensemble`](python/data-science/streaming_iii/concept_drift_ensemble.py) | Concept-drift ensemble vs a frozen single learner. Core idea: on a stream whose concept flips, a drift-aware ensemble that spawns a fresh learner per window and weights learners… | C++ |
| [`ddm_error_drift`](python/data-science/streaming_iii/ddm_error_drift.py) | DDM -- Drift Detection Method (Gama, Medas, Castillo, Rodrigues 2004). Core idea: as a classifier's binary error stream arrives, track p_i (running error rate) and s_i =… | C++ |
| [`exponential_histogram_count`](python/data-science/streaming_iii/exponential_histogram_count.py) | Exponential histogram / DGIM count of 1s in a sliding window (Datar-Gionis-Indyk-Motwani). Core idea: to count the 1-bits among the last N arrivals in O((1/eps) log N) space, keep… | C++ |
| [`frugal_streaming_median`](python/data-science/streaming_iii/frugal_streaming_median.py) | Frugal streaming median (Ma, Muthukrishnan, Sandler) -- Frugal-1, one integer of state. Core idea: keep a single estimate m; for each element, with a coin gated by the target… | C++ |
| [`gk_quantile_summary`](python/data-science/streaming_iii/gk_quantile_summary.py) | Greenwald-Khanna ε-approximate quantile summary. Core idea: maintain sorted list of (v, g, delta) tuples; compress on overflow to ε-error guarantees. When: need approximate… | C++ |
| [`hoeffding_tree_lite`](python/data-science/streaming_iii/hoeffding_tree_lite.py) | Hoeffding tree (VFDT) lite -- a streaming decision stump with a Hoeffding-bound split test. Core idea: accumulate class counts on each side of every candidate split as data… | C++ |
| [`hyperloglog_distinct`](python/data-science/streaming_iii/hyperloglog_distinct.py) | HyperLogLog cardinality estimation (Flajolet et al.). Core idea: hash each element to 64 bits; the first p bits pick a register, the rank (position of the leftmost 1) in the… | C++ |
| [`kswin_drift`](python/data-science/streaming_iii/kswin_drift.py) | KSWIN (Kolmogorov-Smirnov Windowing) drift detector using KS test on sliding windows. Core idea: maintain two windows; apply KS test to detect distribution shift. When: detect… | C++ |
| [`lossy_counting_frequent`](python/data-science/streaming_iii/lossy_counting_frequent.py) | Lossy Counting for frequent items (Manku & Motwani, 2002). Core idea: divide the stream into buckets of width w = ceil(1/eps). Store each item as (freq, delta) where delta is the… | C++ |
| [`misra_gries_heavy_hitters`](python/data-science/streaming_iii/misra_gries_heavy_hitters.py) | Misra-Gries heavy hitters (k-1 counters). Core idea: keep at most k-1 counters; on a new item increment its counter, else open one if room, else decrement ALL counters (dropping… | C++ |
| [`online_bagging_poisson`](python/data-science/streaming_iii/online_bagging_poisson.py) | Online bagging via Poisson(1) weighting (Oza & Russell, 2001). Core idea: batch bagging resamples each point ~Binomial(n,1/n) times, which -> Poisson(1) as n grows. So online… | C++ |
| [`robust_streaming_mad`](python/data-science/streaming_iii/robust_streaming_mad.py) | Robust anomaly detection via the median / MAD rule. Core idea: center on the median and scale by MAD (median absolute deviation, x1.4826 for a normal consistency constant); flag… | C++ |
| [`sliding_window_quantile`](python/data-science/streaming_iii/sliding_window_quantile.py) | Sliding window quantile via sorted window maintenance. Core idea: keep the last k elements in order, sort when needed, compute exact quantile. When: need exact quantile over… | C++ |
| [`sliding_window_regression`](python/data-science/streaming_iii/sliding_window_regression.py) | Sliding window regression: track time-varying coefficient on streaming data via windowed OLS. Core idea: maintain running statistics in a window; recompute OLS coefficients as… | C++ |
| [`tdigest_lite`](python/data-science/streaming_iii/tdigest_lite.py) | t-digest (merging variant) -- accurate tail quantiles in small space. Core idea: merge sorted points into centroids under a q-dependent SIZE BOUND limit(q) = 4*N*delta*q*(1-q).… | C++ |
| [`weighted_reservoir_ares`](python/data-science/streaming_iii/weighted_reservoir_ares.py) | Weighted reservoir sampling -- Efraimidis-Spirakis A-Res. Core idea: give each item a key u**(1/weight) with u ~ Uniform(0,1); keep the k items with the largest keys in a… | C++ |
| [`welford_decayed_moments`](python/data-science/streaming_iii/welford_decayed_moments.py) | Exponentially-decayed streaming mean/variance (Welford-style, decay-weighted). Core idea: maintain a decay-weighted running mean and M2 so recent samples dominate. On a stream… | C++ |
| [`windowed_distinct_count`](python/data-science/streaming_iii/windowed_distinct_count.py) | Windowed distinct count: exact count of unique elements in a sliding window. Core idea: maintain window buffer; return len(set(buffer)) at query time. When: count distinct… | C++ |

### survival_and_reliability

| Pattern | Description | Also in |
|---|---|---|
| [`accelerated_failure_time_lite`](python/data-science/survival_and_reliability/accelerated_failure_time_lite.py) | Accelerated failure time (AFT): log-linear regression on survival times. Model: log(T) = μ + β·x + σ·ε where T is survival time, x is covariate. Core claim: linear relationship… | C++ |
| [`censoring_bias_demo`](python/data-science/survival_and_reliability/censoring_bias_demo.py) | Censoring bias: ignoring censoring biases survival estimates downward. Demonstrated: comparing naive mean of observed times vs Kaplan-Meier estimate shows that censored data… | C++ |
| [`competing_risks_naive_bias`](python/data-science/survival_and_reliability/competing_risks_naive_bias.py) | Competing risks: the naive 1−KM overestimates incidence; Aalen-Johansen is correct. With competing events, a common MISTAKE is to estimate the cumulative incidence of cause 1 as 1… | C++ |
| [`cox_partial_likelihood_lite`](python/data-science/survival_and_reliability/cox_partial_likelihood_lite.py) | Cox partial likelihood: semiparametric survival model for 2-covariate hazard. Estimates hazard ratios via Newton-Raphson on partial likelihood. Core claim: planted hazard ratios… | C++ |
| [`exponential_reliability_mtbf`](python/data-science/survival_and_reliability/exponential_reliability_mtbf.py) | Exponential reliability: MTBF and survival function from failure times. For constant hazard h(t) = λ, survival S(t) = exp(-λt) and MTBF = 1/λ. Core claim: MTBF estimated from… | C++ |
| [`hazard_vs_survival_conversion`](python/data-science/survival_and_reliability/hazard_vs_survival_conversion.py) | Hazard-survival conversion: verify duality h(t) = -d/dt[log S(t)]. Given S(t) or h(t), derive the other and check consistency. Planted S(t), compute h(t), then reconstruct S(t)… | C++ |
| [`log_rank_test`](python/data-science/survival_and_reliability/log_rank_test.py) | Log-rank test: nonparametric test for equality of survival curves. Compares two groups via observed vs expected events under null hypothesis (no group difference). Core claim: two… | C++ |
| [`nelson_aalen_cumhazard`](python/data-science/survival_and_reliability/nelson_aalen_cumhazard.py) | Nelson-Aalen cumulative hazard: nonparametric estimate from event times. H(t) = Σ d_i / y_i where d_i = events at time i, y_i = at-risk count. Core claim: cumulative hazard… | C++ |
| [`reliability_series_parallel`](python/data-science/survival_and_reliability/reliability_series_parallel.py) | System reliability: series vs parallel from component reliabilities. Series: all components must work → R_sys = R1 · R2 · ... · Rn. Parallel: at least one must work → R_sys = 1 -… | C++ |
| [`weibull_mle`](python/data-science/survival_and_reliability/weibull_mle.py) | Weibull MLE: maximum-likelihood estimation of shape k and scale λ (uncensored). For iid Weibull data the log-likelihood is ℓ(k,λ) = n·ln k − n·k·ln λ + (k−1)·Σ ln t_i − Σ… | C++ |

### text_nlp

| Pattern | Description | Also in |
|---|---|---|
| [`bag_of_words`](python/data-science/text_nlp/bag_of_words.py) | Bag-of-Words Vectorizer Core idea: represent each document as a sparse count vector of word frequencies. Build a shared vocabulary from all documents, then encode each document as… | C++ |
| [`bpe_tokenizer_lite`](python/data-science/text_nlp/bpe_tokenizer_lite.py) | Simplified Byte-Pair Encoding (BPE) Tokenizer Core idea: learn merge operations from a corpus (combining frequent character pairs), then apply merges to tokenize new text. Encode… | C++ |
| [`cosine_similarity_search`](python/data-science/text_nlp/cosine_similarity_search.py) | Cosine Similarity Search: Rank Documents by Query Core idea: convert documents and query to TF-IDF vectors, rank documents by cosine similarity to query. Fast baseline for… | C++ |
| [`edit_distance`](python/data-science/text_nlp/edit_distance.py) | Levenshtein Edit Distance via Dynamic Programming Core idea: compute minimum number of single-character edits (insert, delete, replace) to transform one string into another using… | C++ |
| [`markov_chain_text`](python/data-science/text_nlp/markov_chain_text.py) | Word-Level Markov Chain Text Generator Core idea: build a transition matrix of word frequencies (conditional on previous word). Generate text by sampling from this distribution at… | C++ |
| [`minhash_dedup`](python/data-science/text_nlp/minhash_dedup.py) | MinHash Signatures for Near-Duplicate Detection Core idea: compute compact hash signatures for sets of tokens. Use Jaccard similarity from signatures to estimate similarity and… | C++ |
| [`ngram_language_model`](python/data-science/text_nlp/ngram_language_model.py) | N-gram Language Model with Add-One Smoothing Core idea: model text as a Markov chain over n-grams (sequences of n tokens). Estimate P(token \| preceding n-1 tokens) from data; use… | C++ |
| [`rake_keyword_extraction`](python/data-science/text_nlp/rake_keyword_extraction.py) | RAKE-Style Keyword Extraction Core idea: split text into phrases delimited by stopwords, score phrases by degree (unique words in phrase) and frequency (how often phrase appears).… | C++ |
| [`tfidf_vectorizer`](python/data-science/text_nlp/tfidf_vectorizer.py) | TF-IDF Vectorizer Core idea: weight term frequencies by inverse document frequency to emphasize distinctive terms. TF-IDF(t,d) = freq(t in d) * log(N / doc_count(t)). Common… | C++ |
| [`viterbi_hmm`](python/data-science/text_nlp/viterbi_hmm.py) | Viterbi Decoding for Hidden Markov Models Core idea: find the most-likely sequence of hidden states given observations using dynamic programming. Compare Viterbi result against… | C++ |

### text_nlp_ii

| Pattern | Description | Also in |
|---|---|---|
| [`char_ngram_language_id`](python/data-science/text_nlp_ii/char_ngram_language_id.py) | Character n-gram language identification: distinguish languages via bigram profiles. Builds character bigram frequencies; compares via distance. Core claim: true language matched;… | C++ |
| [`naive_bayes_complement`](python/data-science/text_nlp_ii/naive_bayes_complement.py) | Complement Naive Bayes: robust on imbalanced text via the negative-class model. Vanilla multinomial NB scores class c with log P(c) + Σ f_w·log θ_{c,w}. Under heavy class… | C++ |
| [`porter_stemmer_lite`](python/data-science/text_nlp_ii/porter_stemmer_lite.py) | Porter stemmer: rule-based morphological analysis for English word stemming. Reduces words to root form via suffix removal rules. Core claim: canonical test pairs stem correctly;… | C++ |
| [`sentence_boundary_detection`](python/data-science/text_nlp_ii/sentence_boundary_detection.py) | Sentence boundary detection: split text at sentence ends despite abbreviations. Detects end-of-sentence punctuation (. ! ?) while NOT splitting on the periods inside common… | C++ |
| [`soundex_phonetic`](python/data-science/text_nlp_ii/soundex_phonetic.py) | Soundex: phonetic encoding for name matching and fuzzy search. Maps names to 4-char code (1 letter + 3 digits) based on pronunciation. Core claim: known name pairs match (same… | C++ |
| [`textrank_lite`](python/data-science/text_nlp_ii/textrank_lite.py) | TextRank: extract key sentences via graph centrality (damped power iteration). Builds a sentence similarity graph (Jaccard word overlap) and ranks sentences with the… | C++ |
| [`tf_idf_bm25_comparison`](python/data-science/text_nlp_ii/tf_idf_bm25_comparison.py) | TF-IDF vs BM25: compare relevance ranking on length-biased documents. BM25 dampens length bias (saturation on high-TF terms) whereas TF-IDF linear. Core claim: on variable-length… | C++ |
| [`zipf_law_fit`](python/data-science/text_nlp_ii/zipf_law_fit.py) | Zipf's law: rank-frequency relationship in natural language. log(frequency) ∝ log(rank) with slope ≈ −1. Core claim: natural text follows Zipf; uniform text violates it. Fitted… | C++ |

### time_series

| Pattern | Description | Also in |
|---|---|---|
| [`autocorrelation_function`](python/data-science/time_series/autocorrelation_function.py) | Autocorrelation Function (ACF) Compute the autocorrelation of a time series at multiple lags. ACF(k) = correlation between y_t and y_{t-k}. Include simple significance bounds… | C++ |
| [`autoregressive_model`](python/data-science/time_series/autoregressive_model.py) | Autoregressive (AR) Model Fit an AR(p) model by regressing y_t on its p lagged values using least squares. Solves the normal equations directly (no external libraries). Produces… | C++ |
| [`cusum_changepoint`](python/data-science/time_series/cusum_changepoint.py) | CUSUM Change-Point Detection Cumulative Sum (CUSUM) control chart detects shifts in mean. CUSUM_t = max(0, CUSUM_{t-1} + (y_t - target) - k) When CUSUM exceeds a threshold h, a… | C++ |
| [`differencing_stationarity`](python/data-science/time_series/differencing_stationarity.py) | Differencing for Stationarity First differencing transforms a non-stationary series (e.g., random walk) into a stationary one. Differenced series: d_t = y_t - y_{t-1}.… | C++ |
| [`exponential_smoothing`](python/data-science/time_series/exponential_smoothing.py) | Exponential Smoothing Apply single exponential smoothing (Simple Exponential Smoothing, SES) and double exponential smoothing (Holt's method) to a time series. SES smooths level;… | C++ |
| [`kalman_filter_1d`](python/data-science/time_series/kalman_filter_1d.py) | 1D Kalman Filter Recursively estimate the state of a 1D system (constant velocity model). State: x = [position, velocity]. Observations are noisy position measurements. The filter… | C++ |
| [`moving_average_smoothing`](python/data-science/time_series/moving_average_smoothing.py) | Moving Average Smoothing Smooth a noisy time series using simple and weighted moving averages. Reduces short-term fluctuations while preserving trend; wider windows smooth more… | C++ |
| [`rolling_zscore_anomaly`](python/data-science/time_series/rolling_zscore_anomaly.py) | Rolling Z-Score Anomaly Detection Detect anomalies using rolling-window z-scores. For each point, compute the z-score within a rolling window: z = (x - window_mean) / window_std.… | C++ |
| [`seasonal_decomposition`](python/data-science/time_series/seasonal_decomposition.py) | Seasonal Decomposition (Naive Additive) Decompose a time series into trend, seasonal, and residual components using naive additive decomposition: y_t = trend_t + seasonal_t +… | C++ |
| [`walk_forward_validation`](python/data-science/time_series/walk_forward_validation.py) | Walk-Forward Validation Time-series cross-validation using expanding windows: train on the first window, forecast 1 step ahead, expand window by 1, repeat. Evaluates forecasters… | C++ |

## python/programming

*99 files across 13 categories.*

### architecture

| Pattern | Description | Also in |
|---|---|---|
| [`cqrs_bus`](python/programming/architecture/cqrs_bus.py) | Simple CQRS Command/Query Splitter Module This module implements a basic Command Query Responsibility Segregation (CQRS) pattern with separate buses for commands and queries,… | Go |
| [`event_bus`](python/programming/architecture/event_bus.py) | Event Bus with Typed Channels A lightweight event bus implementation supporting typed channels, asynchronous delivery, and type-safe message passing. | Go |
| [`event_sourcing_store`](python/programming/architecture/event_sourcing_store.py) | Event Sourcing Store Implementation This module provides a complete event sourcing system with: - Event and Snapshot classes - Append-only event log storage - Snapshot… | Go |
| [`message_encoder`](python/programming/architecture/message_encoder.py) | Message Format Encoder/Decoder Module This module provides classes for encoding and decoding messages with: - Length-prefix framing - Checksum validation - Version negotiation | — |
| [`plugin_registry`](python/programming/architecture/plugin_registry.py) | Plugin registry with lazy loading, dependency management, and entry point discovery. | — |
| [`saga_coordinator`](python/programming/architecture/saga_coordinator.py) | Saga Pattern Coordinator Module This module implements the Saga pattern for distributed transactions, providing forward execution and backward compensation on failure. | — |
| [`state_machine`](python/programming/architecture/state_machine.py) | Simple State Machine Engine This module provides a complete state machine implementation with support for states, transitions, guards, actions, and entry/exit hooks. | — |

### async

| Pattern | Description | Also in |
|---|---|---|
| [`async_task_queue`](python/programming/async/async_task_queue.py) | Async Task Queue with Priority and Retries A production-ready async task queue implementation with priority levels, automatic retries with exponential backoff, and dead-letter… | Go |
| [`cancellable_task_group`](python/programming/async/cancellable_task_group.py) | Async task group implementation with cancellation support. | Go |
| [`priority_queue_scheduler`](python/programming/async/priority_queue_scheduler.py) | Priority Queue with Deadline Scheduling Module This module implements a priority queue that supports deadline-aware scheduling and preemption hints for task management. | — |
| [`pubsub_broker`](python/programming/async/pubsub_broker.py) | A simple pub-sub message broker implementation with wildcard topic matching. | — |
| [`reactive_signals`](python/programming/async/reactive_signals.py) | Fine-grained reactive primitives — Signal, Computed, Effect — with automatic dependency tracking through a context stack. Use when values should recompute (Computed) or side… | — |

### data_structures

| Pattern | Description | Also in |
|---|---|---|
| [`avl_tree`](python/programming/data_structures/avl_tree.py) | AVL Tree Implementation A self-balancing binary search tree where the heights of the two child subtrees of any node differ by at most one. | Go |
| [`binary_indexed_tree`](python/programming/data_structures/binary_indexed_tree.py) | Binary Indexed Tree (Fenwick tree) for prefix sums with point updates, plus a Query wrapper that turns raw delta-updates into set-value semantics. Use for O(log n) prefix-sum and… | Go |
| [`bloom_filter`](python/programming/data_structures/bloom_filter.py) | Probabilistic set-membership via a Bloom filter with md5-derived double hashing and an analytically sized bit array and hash count. Use when false positives are tolerable but… | Go, Rust |
| [`fenwick_tree`](python/programming/data_structures/fenwick_tree.py) | Fenwick Tree (Binary Indexed Tree) implementation with comprehensive functionality. Supports point updates and prefix/range sum queries in O(log n) time. | Go |
| [`interval_tree`](python/programming/data_structures/interval_tree.py) | Augmented BST of intervals — each node caches its subtree's maximum endpoint — for efficient overlap queries. Use to insert and delete intervals and find all that overlap a query… | — |
| [`kd_tree`](python/programming/data_structures/kd_tree.py) | A complete k-d tree implementation for 2D points with insert, nearest neighbor, and range search functionality. | — |
| [`merkle_tree`](python/programming/data_structures/merkle_tree.py) | A simple Merkle tree implementation using SHA-256 hashing. This module provides classes to create and work with Merkle trees, including building trees, generating proofs, and… | Rust |
| [`ordered_map`](python/programming/data_structures/ordered_map.py) | Sorted dictionary backed by an unbalanced binary search tree, implementing the MutableMapping interface with ordered iteration and range/bound queries. Use as a dict whose keys… | — |
| [`persistent_deque`](python/programming/data_structures/persistent_deque.py) | Doubly-linked deque that serializes its full contents to a pickle file after every mutation and reloads that state on construction. Use when a deque must survive process death:… | — |
| [`priority_task_scheduler`](python/programming/data_structures/priority_task_scheduler.py) | Priority Queue Scheduler Module This module implements a priority queue scheduler that handles tasks with different priorities and deadlines. Tasks are ordered first by priority,… | — |
| [`radix_tree`](python/programming/data_structures/radix_tree.py) | Radix tree (compressed trie) mapping string keys to values, splitting and merging edges so each node carries the longest shared prefix. Use for prefix-dense string keys where a… | — |
| [`red_black_tree`](python/programming/data_structures/red_black_tree.py) | Red-Black tree with insert, delete, and a full property validator, kept balanced by recoloring and rotations around a shared NIL sentinel. Use as a self-balancing ordered set of… | — |
| [`segment_tree`](python/programming/data_structures/segment_tree.py) | Pointer-based segment tree over a fixed-length numeric array supporting range-sum and range-min queries with point updates. Use for O(log n) range aggregate queries on mutable… | — |
| [`skip_list`](python/programming/data_structures/skip_list.py) | Probabilistic skip list mapping int keys to values with randomized level promotion, giving expected O(log n) search, insert, and delete. Use as an ordered map with sorted… | Rust |
| [`suffix_array`](python/programming/data_structures/suffix_array.py) | Suffix array (naive sort build) with pattern search, a Kasai LCP array, a sparse- table RMQ over the LCP, and a longest-common-substring routine. Use to index a string for… | — |
| [`treap`](python/programming/data_structures/treap.py) | Treap — a randomized balanced BST that is a search tree on values and a max-heap on random priorities — with insert, erase-one, membership, and order statistics. Use as an ordered… | — |
| [`trie`](python/programming/data_structures/trie.py) | Trie (Prefix Tree) implementation with autocomplete functionality. | — |
| [`union_find`](python/programming/data_structures/union_find.py) | Union-Find (disjoint-set) over arbitrary hashable values with path compression and union by rank, tracking a live component count. Use to maintain dynamic connectivity: make_set,… | — |

### distributed

| Pattern | Description | Also in |
|---|---|---|
| [`consistent_hash_ring`](python/programming/distributed/consistent_hash_ring.py) | Consistent Hash Ring Implementation This module provides a consistent hash ring implementation that distributes keys across nodes in a way that minimizes redistribution when nodes… | Go, Rust |
| [`crdt_sets`](python/programming/distributed/crdt_sets.py) | CRDT Sets Implementation This module implements three types of Conflict-free Replicated Data Types (CRDT) sets: - AWORSet (Add-Wins Observed-Remove Set) - AddWinsSet (Add-Wins… | Go |
| [`distributed_lock_manager`](python/programming/distributed/distributed_lock_manager.py) | In-process distributed lock manager with lease expiry and a fairness queue. Use when several owners contend for named resources and you need mutual exclusion plus automatic… | Go |
| [`g_counter_crdt`](python/programming/distributed/g_counter_crdt.py) | Distributed Counter Implementation This module provides two types of distributed counters: - GCounter (Grow-only Counter): Only supports increment operations - PNCounter… | Go |
| [`gossip_protocol`](python/programming/distributed/gossip_protocol.py) | Gossip Protocol Membership List Implementation This module implements a gossip protocol for maintaining membership lists in distributed systems. It includes features for member… | — |
| [`quorum_consensus`](python/programming/distributed/quorum_consensus.py) | Quorum consensus simulator module. This module implements a simple quorum consensus system with nodes that can propose values, accept proposals, and learn consensus decisions. | — |
| [`raft_consensus`](python/programming/distributed/raft_consensus.py) | Raft Consensus Algorithm Implementation This module implements the Raft consensus algorithm with leader election, log replication, and heartbeat mechanisms. | — |
| [`service_registry`](python/programming/distributed/service_registry.py) | In-memory service-discovery registry with heartbeat-based health and TTL. Use when instances register themselves and clients look them up by name and an optional set of tags: each… | — |
| [`vector_clock`](python/programming/distributed/vector_clock.py) | Vector Clock implementation for detecting causal relationships between events in distributed systems. | — |

### io

| Pattern | Description | Also in |
|---|---|---|
| [`arg_parser`](python/programming/io/arg_parser.py) | A small argparse-style command-line parser (options + positionals). Use when you want an argparse-like surface without the dependency: define options (short/long, store /… | Go |
| [`chunked_reader`](python/programming/io/chunked_reader.py) | Line-delimited file parser with chunked reads. This module provides classes for efficiently reading and parsing large files by reading them in chunks and processing line by line,… | Go |
| [`csv_to_json`](python/programming/io/csv_to_json.py) | CSV to JSON converter module with type inference, nested key support, and streaming. | Go |
| [`csv_validator`](python/programming/io/csv_validator.py) | CSV Validator and Transformer Module This module provides classes for validating and transforming CSV data based on a schema. | Go |
| [`diff_engine`](python/programming/io/diff_engine.py) | A simple diff engine for text comparison. | Go |
| [`ini_parser`](python/programming/io/ini_parser.py) | Simple INI file parser module. This module provides functionality to parse, manipulate, and write INI files. It supports typed value retrieval and setting, section management, and… | — |
| [`log_parser`](python/programming/io/log_parser.py) | JSON Schema Validator Module This module provides a lightweight JSON schema validator that supports: - Type checking - Required fields - Nested object validation - Custom… | — |
| [`template_engine`](python/programming/io/template_engine.py) | A minimal regex-based string template engine. Use for lightweight text templating without a full engine: `{{ var }}` substitution, `{{ var \| default }}` fallbacks, dotted paths… | — |

### monitoring

| Pattern | Description | Also in |
|---|---|---|
| [`alert_manager`](python/programming/monitoring/alert_manager.py) | Alert manager with rule-driven deduplication, suppression, and escalation. Use to ingest a stream of alerts and cut noise: each alert is fingerprinted (title+source+tags) and… | Go |
| [`event_logger`](python/programming/monitoring/event_logger.py) | Structured event logger with rotation capabilities. This module provides a complete logging solution that outputs structured events in JSONL format with automatic log rotation… | Go |
| [`log_pattern_matcher`](python/programming/monitoring/log_pattern_matcher.py) | Ordered regex log parser that extracts named groups into structured records. Use to turn heterogeneous log lines into dicts: register named patterns (each a regex with named… | — |
| [`metric_aggregation_engine`](python/programming/monitoring/metric_aggregation_engine.py) | Metric Aggregation Engine A complete metric aggregation system supporting counters, gauges, and histograms with label support and quantile computation. | — |
| [`metric_aggregator`](python/programming/monitoring/metric_aggregator.py) | Metric aggregator with tags for counters, gauges, and histograms. Supports percentile calculations and tagged metrics. | — |
| [`metrics_formatter`](python/programming/monitoring/metrics_formatter.py) | Prometheus / OpenMetrics text-exposition formatter. Use to serialize metrics into the Prometheus text format: build Metric objects (name, value, type, labels, optional… | — |
| [`time_series_db`](python/programming/monitoring/time_series_db.py) | In-memory time-series database module with support for insertion, querying, aggregation, and downsampling. | — |
| [`timer_stack`](python/programming/monitoring/timer_stack.py) | Stack-based hierarchical timers for nested-section profiling. Use to time nested code sections: start pushes a named timer, stop pops the innermost one (LIFO), elapsed time… | — |
| [`trace_collector`](python/programming/monitoring/trace_collector.py) | Minimal distributed-tracing collector: spans, traces, and their tree. Use to model an operation as a tree of timed spans: a Collector creates spans (each with an id, parent,… | — |
| [`trace_sampler`](python/programming/monitoring/trace_sampler.py) | Distributed Tracing Sampler Module This module provides a complete implementation of a distributed tracing sampler with support for rate limiting, priority traces, and adaptive… | — |
| [`trace_span_collector`](python/programming/monitoring/trace_span_collector.py) | Distributed Tracing Span Collector Module This module provides a complete implementation of a distributed tracing system with span collection, parent-child relationships, baggage… | — |
| [`window_sampler`](python/programming/monitoring/window_sampler.py) | Anomaly Detection Sampler Module This module provides classes for detecting anomalies in time-series data using statistical methods with adaptive baselines and windowed sampling. | — |

### networking

| Pattern | Description | Also in |
|---|---|---|
| [`connection_pool`](python/programming/networking/connection_pool.py) | Connection Manager with Pooling A module that provides connection pooling functionality with health checks and thread-safe operations. | Go |
| [`connection_pool_health_checks`](python/programming/networking/connection_pool_health_checks.py) | Connection Pool with Health Checks Module This module provides a robust connection pool implementation with health checking, connection validation, and automatic eviction of… | Go |
| [`dns_cache`](python/programming/networking/dns_cache.py) | LRU DNS cache with per-record TTL expiry and negative caching. Use as a bounded resolver cache keyed by (name, record_type): positive records expire at their own TTL,… | Go |
| [`http_retry_client`](python/programming/networking/http_retry_client.py) | HTTP Client with Retry, Backoff, and Circuit Breaker Support This module provides a robust HTTP client that supports configurable retry policies, exponential backoff, and circuit… | — |
| [`http_router`](python/programming/networking/http_router.py) | HTTP Request Multiplexer Module A lightweight HTTP request multiplexer that routes requests based on path and method, with support for middleware chains and parameterized routes. | — |
| [`packet_parser`](python/programming/networking/packet_parser.py) | Binary network-packet builder and parser with a trailing checksum. Use to build and decode a small framed binary protocol: create_packet emits DATA / ACK / NACK / CONTROL frames… | — |
| [`rate_limiter`](python/programming/networking/rate_limiter.py) | Token-bucket rate limiter with independent per-key buckets. Use to cap request rates per client/key: each key gets its own bucket of a given capacity that refills at a fixed… | — |
| [`rtt_estimator`](python/programming/networking/rtt_estimator.py) | Round-trip time estimator module with EWMA smoothing and timeout calculation. | — |
| [`url_router`](python/programming/networking/url_router.py) | URL router with `{param}` path patterns and reverse URL building. Use to map URL paths to handlers: register routes (via add_route or the @route decorator) whose patterns embed… | — |

### performance

| Pattern | Description | Also in |
|---|---|---|
| [`batch_controller`](python/programming/performance/batch_controller.py) | Adaptive Batch Size Controller A module for dynamically adjusting batch sizes based on throughput metrics to optimize processing performance. | Go |
| [`budget_allocator`](python/programming/performance/budget_allocator.py) | Request Collapser Module This module implements a request collapser that batches identical requests within a time window to reduce backend load. It deduplicates concurrent… | Go |
| [`free_list_allocator`](python/programming/performance/free_list_allocator.py) | Best-fit free-list memory allocator over a fixed arena. Models allocate/free with exact address arithmetic: allocations carve from a sorted free list using best-fit, over-sized… | Go |
| [`hyperloglog`](python/programming/performance/hyperloglog.py) | HyperLogLog probabilistic cardinality estimator implementation. This module provides a HyperLogLog class for estimating the cardinality (number of distinct elements) of large… | — |
| [`job_scheduler`](python/programming/performance/job_scheduler.py) | A simple job scheduler with cron-like expressions. Supports minute, hour, day of month, month, and day of week fields. | — |
| [`lru_cache`](python/programming/performance/lru_cache.py) | Thread-safe LRU cache with optional per-entry TTL expiry. A fixed-capacity cache backed by an OrderedDict under an RLock: reads and writes mark keys as recently used, the… | Rust |
| [`object_pool_allocator`](python/programming/performance/object_pool_allocator.py) | Thread-safe object pool for reusing expensive-to-create resources. Manages a bounded pool of objects built by a factory and checked by a validator: it prefills to min_size, hands… | — |
| [`resource_budget_allocator`](python/programming/performance/resource_budget_allocator.py) | Resource Budget Allocator Module This module provides functionality for allocating and managing resource budgets with quota tracking and overcommit detection. | — |
| [`rw_lock`](python/programming/performance/rw_lock.py) | Writer-preferring read-write lock with upgrade and downgrade. Allows many concurrent readers or one exclusive writer, backed by a Condition; pending writers block new readers to… | — |
| [`token_bucket`](python/programming/performance/token_bucket.py) | Token-bucket rate limiter with lazy time-based refill. A thread-safe bucket that refills at a fixed rate up to a capacity: consume() grants tokens when available (allowing bursts… | Rust |
| [`work_stealing_queue`](python/programming/performance/work_stealing_queue.py) | Work-Stealing Queue Implementation A thread-safe work-stealing queue system where workers can steal tasks from other workers when their local queues are empty. | — |

### persistence

| Pattern | Description | Also in |
|---|---|---|
| [`lsm_tree`](python/programming/persistence/lsm_tree.py) | LSM-Tree Engine Implementation A complete implementation of an LSM-Tree (Log-Structured Merge-Tree) storage engine with MemTable, SSTable, and compaction functionality. | — |
| [`segmented_wal`](python/programming/persistence/segmented_wal.py) | Write-Ahead Log (WAL) implementation for durable transaction logging. This module provides a complete WAL system with: - Append-only writes for durability - Checksum verification… | — |
| [`write_ahead_log`](python/programming/persistence/write_ahead_log.py) | Write-Ahead Log (WAL) implementation for data durability and crash recovery. This module provides a complete WAL system that ensures data integrity through logging operations… | — |

### reasoning

| Pattern | Description | Also in |
|---|---|---|
| [`astar_pathfinding`](python/programming/reasoning/astar_pathfinding.py) | A* Pathfinding Algorithm Implementation This module implements the A* pathfinding algorithm for grid-based navigation. It includes classes for nodes, grid representation, and the… | Go |
| [`bayesian_network`](python/programming/reasoning/bayesian_network.py) | Bayesian Belief Network Implementation This module provides a complete implementation of a Bayesian Belief Network with support for conditional probability tables, inference by… | Go |
| [`csp_solver`](python/programming/reasoning/csp_solver.py) | Constraint Satisfaction Problem (CSP) Solver Module This module implements a complete CSP solver with backtracking search and arc consistency (AC-3) algorithm for constraint… | Go |
| [`decision_tree`](python/programming/reasoning/decision_tree.py) | Simple Decision Tree Classifier A complete implementation of a decision tree classifier with information gain, prediction, and pruning capabilities. | Go |
| [`dependency_graph`](python/programming/reasoning/dependency_graph.py) | Dependency Graph Resolver - Topological Sort Implementation This module provides a dependency graph resolver that can: - Detect circular dependencies - Perform topological sorting… | — |
| [`expression_evaluator`](python/programming/reasoning/expression_evaluator.py) | Simple Expression Evaluator with Variables This module provides a complete expression evaluator that supports: - Basic arithmetic operations (+, -, *, /, %, **) - Parentheses for… | Go |
| [`minimax_game_search`](python/programming/reasoning/minimax_game_search.py) | A complete minimax game solver with alpha-beta pruning and depth limiting. | — |
| [`rule_engine`](python/programming/reasoning/rule_engine.py) | Rule-based inference engine with forward chaining and conflict resolution. | — |
| [`sat_solver`](python/programming/reasoning/sat_solver.py) | DPLL SAT solver for Boolean formulas in CNF. Represents literals, clauses, and CNF formulas, then decides satisfiability by the DPLL search: unit propagation, pure-literal… | Go |

### resilience

| Pattern | Description | Also in |
|---|---|---|
| [`bulkhead_isolator`](python/programming/resilience/bulkhead_isolator.py) | Bulkhead Pattern Isolator Module This module implements the bulkhead pattern to isolate system resources and prevent cascading failures. It provides resource isolation through… | Go |
| [`circuit_breaker`](python/programming/resilience/circuit_breaker.py) | Circuit breaker that stops calling a failing dependency. Wraps a callable (as decorator or via call()) and tracks failures: after the threshold trips it opens and fails fast… | Go, Rust |
| [`dead_letter_queue`](python/programming/resilience/dead_letter_queue.py) | Dead Letter Queue Handler Module This module provides a complete implementation of a Dead Letter Queue system with retry policies, exponential backoff, and poison pill detection. | Go |
| [`timeout_guard`](python/programming/resilience/timeout_guard.py) | Timeout guard that interrupts an operation past its deadline. A context manager (TimeoutGuard) and wrapper (TimedOperation) that bound how long an operation may run: it prefers… | — |

### security

| Pattern | Description | Also in |
|---|---|---|
| [`capability_access`](python/programming/security/capability_access.py) | Capability-Based Access Control System This module implements a capability-based access control system where capabilities are unforgeable tokens that grant specific permissions to… | — |
| [`hotp_totp`](python/programming/security/hotp_totp.py) | Time-Based One-Time Password (TOTP) generator and validator. This module implements RFC 6238 TOTP and RFC 4226 HOTP algorithms for generating and validating time-based one-time… | — |
| [`secure_envelope`](python/programming/security/secure_envelope.py) | Secure Envelope Module This module provides a secure envelope implementation using HMAC-SHA256 for message authentication and integrity verification. It includes key rotation… | — |

### vision

| Pattern | Description | Also in |
|---|---|---|
| [`image_stats`](python/programming/vision/image_stats.py) | Histogram-based image contrast stretcher module. This module provides functionality to enhance image contrast by stretching the histogram of an image using percentile-based… | — |

## python/system-administration

*200 files across 20 categories.*

### access-control-audit

| Pattern | Description | Also in |
|---|---|---|
| [`append_only_audit`](python/system-administration/access-control-audit/append_only_audit.py) | append_only_audit: maintain an append-only audit log with hash chaining. Each entry hash includes the previous entry's hash (forming a chain). Tampering with an old entry breaks… | Go |
| [`command_allowlist`](python/system-administration/access-control-audit/command_allowlist.py) | command_allowlist: enforce a whitelist of allowed commands. Only commands in the allowlist can be executed. Anything else is blocked. | Go |
| [`immutable_audit`](python/system-administration/access-control-audit/immutable_audit.py) | immutable_audit: create an immutable audit log by sealing it with a cryptographic signature once written. After sealing, any tampering is detectable. Tamper with a sealed log and… | — |
| [`least_privilege_verify`](python/system-administration/access-control-audit/least_privilege_verify.py) | least_privilege_verify: grant only the minimum permissions needed for a task, then verify that unauthorized escalations are blocked. | — |
| [`permission_matrix`](python/system-administration/access-control-audit/permission_matrix.py) | permission_matrix: manage a permission matrix (users × resources × actions). Verify that a permission grants access. Tamper the matrix (flip a permission bit) and verify the… | — |
| [`priv_escalation_detect`](python/system-administration/access-control-audit/priv_escalation_detect.py) | priv_escalation_detect: detect privilege escalation by comparing user privileges across time. If a user gains a new privilege they didn't have before, flag it. This is… | — |
| [`rbac_check`](python/system-administration/access-control-audit/rbac_check.py) | rbac_check: enforce role-based access control. Verify that a user with role X can perform allowed action A, but cannot perform forbidden action B. Failure simulated: allowing a… | — |
| [`session_record`](python/system-administration/access-control-audit/session_record.py) | session_record: record a user session (login, commands, logout). Verify the record is accurate and tamper-proof. Modify a logged command and verify tampering is detected. | — |
| [`sudo_self_body_guard`](python/system-administration/access-control-audit/sudo_self_body_guard.py) | sudo_self_body_guard: detect and block self-destructive sudo commands. Examples: rm -rf /, pkill -9 -u <self>, etc. The guard must allow safe sudo commands and block dangerous… | — |
| [`tamper_evident_chain`](python/system-administration/access-control-audit/tamper_evident_chain.py) | tamper_evident_chain: build a Merkle tree where each node's hash depends on its children. Any tampering with a leaf changes the root hash. Flip a byte in a leaf and verify the… | — |

### backup-disaster-recovery

| Pattern | Description | Also in |
|---|---|---|
| [`backup_catalog`](python/system-administration/backup-disaster-recovery/backup_catalog.py) | backup_catalog: maintain and search backup metadata. | Go |
| [`backup_dedup`](python/system-administration/backup-disaster-recovery/backup_dedup.py) | backup_dedup: detect and skip duplicate content in backups. | Go |
| [`backup_encryption`](python/system-administration/backup-disaster-recovery/backup_encryption.py) | backup_encryption: encrypt backups at rest, verify decryption. | Go |
| [`full_incremental_backup`](python/system-administration/backup-disaster-recovery/full_incremental_backup.py) | full_incremental_backup: multi-level backup with change detection. | Go |
| [`offsite_integrity`](python/system-administration/backup-disaster-recovery/offsite_integrity.py) | offsite_integrity: verify offsite backup integrity via remote checksums. | — |
| [`restore_drill`](python/system-administration/backup-disaster-recovery/restore_drill.py) | restore_drill: regular restore tests to verify backup recoverability. | — |
| [`restore_verify`](python/system-administration/backup-disaster-recovery/restore_verify.py) | restore_verify: verify backup integrity, fail on tampering. | — |
| [`retention_policy`](python/system-administration/backup-disaster-recovery/retention_policy.py) | retention_policy: implement backup retention rules (age-based, count-based). | — |
| [`rpo_rto_measure`](python/system-administration/backup-disaster-recovery/rpo_rto_measure.py) | rpo_rto_measure: measure recovery point objective and recovery time objective. | — |
| [`snapshot_chain`](python/system-administration/backup-disaster-recovery/snapshot_chain.py) | snapshot_chain: maintain chain of snapshots with parent references. | — |

### concurrency-locking

| Pattern | Description | Also in |
|---|---|---|
| [`advisory_lock_timeout`](python/system-administration/concurrency-locking/advisory_lock_timeout.py) | advisory_lock_timeout: Non-blocking (LOCK_NB) advisory lock with timeout fallback. Failure simulated: launch two processes; first acquires and holds, second tries non-blocking… | Go |
| [`atomic_append`](python/system-administration/concurrency-locking/atomic_append.py) | atomic_append: serialize a read-modify-write "append" so concurrent writers never lose data. Failure simulated: MANY processes each do read-the-whole-file → add their line → write… | Go |
| [`cas_file_update`](python/system-administration/concurrency-locking/cas_file_update.py) | cas_file_update: optimistic compare-and-swap on a versioned file (read → compute → swap-if- version-unchanged → retry on conflict). This is REAL CAS, not pessimistic whole-cycle… | Go |
| [`deadlock_timeout`](python/system-administration/concurrency-locking/deadlock_timeout.py) | deadlock_timeout: detect and break potential deadlocks with a timeout mechanism. Failure simulated: two threads try to acquire locks in opposite order (A: lock1→lock2, B:… | Go |
| [`double_launch_block`](python/system-administration/concurrency-locking/double_launch_block.py) | double_launch_block: prevent launching the same service twice; a pidfile lock ensures only one instance can run. Failure simulated: two processes try to start the same service… | Go |
| [`flock_singleton`](python/system-administration/concurrency-locking/flock_singleton.py) | flock_singleton: two processes contend for the same fcntl.flock(LOCK_EX) on a file. Failure simulated: launch a holder and a blocker AT THE SAME TIME; the blocker attempts the… | — |
| [`idempotent_once_guard`](python/system-administration/concurrency-locking/idempotent_once_guard.py) | idempotent_once_guard: ensure an idempotent action runs exactly once, even if called from multiple processes concurrently. Failure simulated: two processes call the action at the… | — |
| [`named_mutex`](python/system-administration/concurrency-locking/named_mutex.py) | named_mutex: a named mutex using filesystem locking (tempfile-based). Failure simulated: two processes try to acquire the same named mutex at the same time. Recovery asserted: (1)… | — |
| [`reader_writer_lock`](python/system-administration/concurrency-locking/reader_writer_lock.py) | reader_writer_lock: many concurrent readers, but a writer needs exclusive access. Failure simulated: (1) 3 readers run at once — they must NOT serialize behind each other; (2)… | — |
| [`stale_lock_break`](python/system-administration/concurrency-locking/stale_lock_break.py) | stale_lock_break: detect and break a stale lock when its holder dies. Failure simulated: process A acquires a lock, then dies (SIGKILL) without releasing. Process B detects the… | — |

### config-management

| Pattern | Description | Also in |
|---|---|---|
| [`config_diff`](python/system-administration/config-management/config_diff.py) | Config diff: report exact changes (added/removed/changed keys) between configs. Failure simulated: missing changes reported; wrong keys in added/removed/changed. Asserts: exact… | Go |
| [`config_versioning`](python/system-administration/config-management/config_versioning.py) | Config versioning: track config version, detect drift (config changed without version bump). Failure simulated: config content changed but version not bumped; version mismatch.… | Go |
| [`dotenv_parse`](python/system-administration/config-management/dotenv_parse.py) | Dotenv parser: parse .env files correctly, handle special chars, reject malformed. Failure simulated: malformed key=value lines; special characters; unquoted values. Asserts:… | Go |
| [`env_load_defaults`](python/system-administration/config-management/env_load_defaults.py) | Environment variable loading with defaults: load env vars, fill missing with defaults. Failure simulated: required env var missing, no default provided. Asserts: exact env var… | Go |
| [`hot_reload`](python/system-administration/config-management/hot_reload.py) | Hot reload config: reload config without restart, new value visible after reload, old before. Failure simulated: old value persists after reload; new value not visible after… | — |
| [`layered_merge`](python/system-administration/config-management/layered_merge.py) | Layered config merge: merge multiple config sources with precedence (later = higher). Failure simulated: required key missing across all layers; wrong precedence applied. Asserts:… | — |
| [`multiformat_load`](python/system-administration/config-management/multiformat_load.py) | Multiformat config loader: load json, ini, dotenv formats; reject syntax errors. Failure simulated: invalid json/ini/dotenv syntax; malformed format. Asserts: exact format error… | — |
| [`refuse_start_on_invalid`](python/system-administration/config-management/refuse_start_on_invalid.py) | Refuse start on invalid config: raise PRECISE error with field name, never silent default. Failure simulated: invalid config provided; code silently defaults instead of refusing.… | — |
| [`schema_validate`](python/system-administration/config-management/schema_validate.py) | Schema validation: reject invalid config keys/types, accept valid config. Failure simulated: missing required key, wrong type. Asserts: exact field name in error message; valid… | — |
| [`secret_separation`](python/system-administration/config-management/secret_separation.py) | Secret separation: keep secrets separate from regular config; assert not leaked. Failure simulated: secret ends up in regular config; secret missing from secret location. Asserts:… | — |

### data-pipeline-ops

| Pattern | Description | Also in |
|---|---|---|
| [`backfill_range`](python/system-administration/data-pipeline-ops/backfill_range.py) | Backfill Range Pattern Fill gaps in time series or sequence. Assert: no gaps remain, existing records not duplicated. | Go |
| [`checkpoint_resume`](python/system-administration/data-pipeline-ops/checkpoint_resume.py) | Checkpoint/Resume Pattern Simulates crash inside batch processing, resumes from last checkpoint, asserts exactly-once processing and correct output. | Go |
| [`exactly_once_dedup`](python/system-administration/data-pipeline-ops/exactly_once_dedup.py) | Exactly-Once Deduplication Pattern Process a stream that may contain duplicates (e.g., from retry logic). Track processed record IDs in a journal, reject duplicates, assert that… | Go |
| [`idempotent_etl_step`](python/system-administration/data-pipeline-ops/idempotent_etl_step.py) | HEADLINE PATTERN: Idempotent ETL Step Simulates pipeline crash mid-transformation, resumes from checkpoint, asserts output is bit-identical and no duplicates despite replayed… | — |
| [`lineage_track`](python/system-administration/data-pipeline-ops/lineage_track.py) | Lineage Tracking Pattern Track data provenance: which source records produced which output records. Assert: complete lineage (every output maps to at least one source), no… | — |
| [`partition_manage`](python/system-administration/data-pipeline-ops/partition_manage.py) | Partition Management Pattern Manage partitions (e.g., date-based, range-based). Track which partitions are closed (immutable), which are open (mutable). Assert: no reprocessing… | — |
| [`pipeline_dead_letter`](python/system-administration/data-pipeline-ops/pipeline_dead_letter.py) | Dead Letter Queue Pattern When processing fails, route to dead letter queue. Retry logic: retry 3 times, then move to DLQ. Assert: all records either processed or in DLQ, no lost… | — |
| [`replay_safe`](python/system-administration/data-pipeline-ops/replay_safe.py) | Replay-Safe Pattern Guarantee that replaying operations produces identical output. Assert: first run and replay produce same result, idempotency holds. Key: operations must be… | — |
| [`schema_drift_detect`](python/system-administration/data-pipeline-ops/schema_drift_detect.py) | Schema Drift Detection Pattern Track expected schema. Detect when records deviate: - New fields added - Fields removed - Field types changed Assert: drift is detected and named… | — |
| [`watermark_track`](python/system-administration/data-pipeline-ops/watermark_track.py) | Watermark Tracking Pattern Track the highest record timestamp processed. On resume, only process records with timestamp > watermark. Asserts: no reprocessing of old records,… | — |

### deployment-rollback

| Pattern | Description | Also in |
|---|---|---|
| [`atomic_symlink_swap`](python/system-administration/deployment-rollback/atomic_symlink_swap.py) | Atomic symlink swap for deployment (never dangling link). | Go |
| [`blue_green_deploy`](python/system-administration/deployment-rollback/blue_green_deploy.py) | Blue-green deployment (two full stacks, atomic switch). | Go |
| [`canary_gate`](python/system-administration/deployment-rollback/canary_gate.py) | Canary deployment gate (gradual traffic shift with rollback). | Go |
| [`config_drift_detect`](python/system-administration/deployment-rollback/config_drift_detect.py) | Detect configuration drift between expected and actual state. | Go |
| [`deplock_verify`](python/system-administration/deployment-rollback/deplock_verify.py) | Verify dependency lock file consistency. | Go |
| [`deploy_idempotency`](python/system-administration/deployment-rollback/deploy_idempotency.py) | Idempotent deployments (safe to run multiple times). | Go |
| [`health_gated_promote`](python/system-administration/deployment-rollback/health_gated_promote.py) | Promote deployment only after health checks pass. | — |
| [`immutable_release`](python/system-administration/deployment-rollback/immutable_release.py) | Immutable release artifacts (prevent re-deployment or modification). | — |
| [`rollback_on_failure`](python/system-administration/deployment-rollback/rollback_on_failure.py) | Automatic rollback when deployment fails or becomes unhealthy. | — |
| [`version_pin_verify`](python/system-administration/deployment-rollback/version_pin_verify.py) | Verify version pins match deployed artifacts. | — |

### filesystem-integrity

| Pattern | Description | Also in |
|---|---|---|
| [`atomic_snapshot`](python/system-administration/filesystem-integrity/atomic_snapshot.py) | atomic_snapshot: take an atomic snapshot of a file at a point in time. Failure simulated: snapshot a live file, modify the original, verify snapshot is unchanged. The snapshot is… | Go |
| [`atomic_write_temp_rename`](python/system-administration/filesystem-integrity/atomic_write_temp_rename.py) | atomic_write_temp_rename: write atomically by writing to a temp file, then atomic rename. Failure simulated (the REAL one): a writer is SIGKILL'd AFTER the temp is fully written… | Go |
| [`checksum_corruption_detect`](python/system-administration/filesystem-integrity/checksum_corruption_detect.py) | checksum_corruption_detect: detect corruption via checksum mismatch. Failure simulated: write file + compute checksum; corrupt a byte in the file; recompute checksum and assert it… | — |
| [`cow_backup`](python/system-administration/filesystem-integrity/cow_backup.py) | cow_backup: an independent point-in-time backup that survives later source corruption. NAME DISCLOSURE (honest): this is an EAGER FULL COPY (read all bytes → temp → atomic… | Go |
| [`dir_tree_diff`](python/system-administration/filesystem-integrity/dir_tree_diff.py) | dir_tree_diff: compute a diff between two directory trees (file presence, size, content hash). Failure simulated: create two similar trees; modify one file; diff trees and assert… | Go |
| [`disk_full_write_guard`](python/system-administration/filesystem-integrity/disk_full_write_guard.py) | disk_full_write_guard: refuse writes when disk space is exhausted or quota exceeded. Failure simulated: attempt to write past disk quota; guard should refuse; existing data… | Go |
| [`fsync_durability`](python/system-administration/filesystem-integrity/fsync_durability.py) | fsync_durability: write data then fsync to flush it to stable storage before returning. Failure defended against: process/power death after write() but before the OS flushes the… | Go |
| [`restore_from_backup`](python/system-administration/filesystem-integrity/restore_from_backup.py) | restore_from_backup: restore a file from backup after corruption/deletion. Failure simulated: backup a file; delete/corrupt the original; restore from backup; assert the original… | — |
| [`safe_delete_trash`](python/system-administration/filesystem-integrity/safe_delete_trash.py) | safe_delete_trash: delete files to trash (not permanent deletion). Failure simulated: delete a file via trash move; assert file is gone from original location but recoverable from… | — |
| [`symlink_escape_guard`](python/system-administration/filesystem-integrity/symlink_escape_guard.py) | symlink_escape_guard: refuse to create symlinks that escape the root directory. Failure simulated: attempt to create symlinks that point outside root (escape attack); assert the… | — |

### log-management

| Pattern | Description | Also in |
|---|---|---|
| [`crash_log_capture`](python/system-administration/log-management/crash_log_capture.py) | Crash log capture: recover from a torn log write (the artifact a crash mid-write leaves). Failure simulated: write N complete JSON lines then a TRUNCATED line (exactly what a… | Go |
| [`log_compression`](python/system-administration/log-management/log_compression.py) | Compress rotated logs: archive to .gz, assert compressed size < original. Failure simulated: write large logs, compress them, measure shrinkage. Defended outcome: compressed size… | — |
| [`rate_limited_log`](python/system-administration/log-management/rate_limited_log.py) | Rate-limited logger: cap log emissions per time window (token bucket). Failure simulated: fire 1000 logs, assert <= limit actually written. Defended outcome: emitted count stays… | — |
| [`retention_prune`](python/system-administration/log-management/retention_prune.py) | Prune logs by retention policy: keep N newest, delete rest. Failure simulated: create 100 log files, prune, assert only N remain. Defended outcome: exactly N files kept, older… | — |
| [`ring_buffer_log`](python/system-administration/log-management/ring_buffer_log.py) | Ring buffer logger: hold max N log entries, evict oldest on overflow. Failure simulated: push N+100 entries, assert exactly N held, oldest evicted. Defended outcome: buffer size… | — |
| [`rotate_by_size`](python/system-administration/log-management/rotate_by_size.py) | Rotate logs by size: exceed cap, assert on-disk bytes <= cap×(retain+1). Failure simulated: write 100× the cap, forcing multiple rotations. Defended outcome: total bytes on disk… | — |
| [`rotate_by_time`](python/system-administration/log-management/rotate_by_time.py) | Rotate logs by time: age past the retention window, assert old files are pruned. Failure simulated: a fake logical clock ages rotated files well past the window. Defended outcome:… | — |
| [`secret_redaction`](python/system-administration/log-management/secret_redaction.py) | Secret redaction: redact sensitive data from logs before writing. Failure simulated: log contains API key/password, verify redaction removed it. Defended outcome: secret string… | — |
| [`structured_json_log`](python/system-administration/log-management/structured_json_log.py) | Structured JSON logging: emit logs as JSON, parse and validate structure. Failure simulated: write mixed JSON/plaintext, parser must skip invalid, count valid. Defended outcome:… | — |
| [`tail_follow`](python/system-administration/log-management/tail_follow.py) | Tail-follow: read appended lines from a growing log without re-reading old lines. Failure simulated: append to log, follow, verify no duplicates and all new lines captured.… | — |

### mesh-distributed

| Pattern | Description | Also in |
|---|---|---|
| [`consistent_hashing`](python/system-administration/mesh-distributed/consistent_hashing.py) | Consistent Hashing Pattern When a node leaves/joins, only ~1/N keys are remapped (not all keys). Assert: Key -> Node mapping changes minimally on membership change. | — |
| [`gossip_membership`](python/system-administration/mesh-distributed/gossip_membership.py) | Gossip Membership Protocol Nodes periodically exchange membership list. Simulate: node joins/leaves, gossip propagates change. Assert: membership eventually consistent across… | — |
| [`heartbeat_lease`](python/system-administration/mesh-distributed/heartbeat_lease.py) | Heartbeat/Lease Pattern Follower sends heartbeats to leader. Leader grants lease based on heartbeats. Assert: lease expires if heartbeats stop, leader detects failure. | — |
| [`idempotent_replication`](python/system-administration/mesh-distributed/idempotent_replication.py) | Idempotent Replication Pattern Replicate writes across replicas. Crash mid-replication, resume. Assert: each write applied exactly once (no duplicates). | — |
| [`lamport_clock`](python/system-administration/mesh-distributed/lamport_clock.py) | Lamport Clock Pattern Logical clock for causality ordering in distributed systems. Not wall-clock time. Step manually, track total order. Assert: clock is monotonic,… | — |
| [`leader_election_lite`](python/system-administration/mesh-distributed/leader_election_lite.py) | Leader Election (Lite) Pattern N nodes, each with ID and term number. Simulate: a node gets term majority, becomes leader. Assert: exactly ONE leader at any term, term number only… | — |
| [`lease_distributed_lock`](python/system-administration/mesh-distributed/lease_distributed_lock.py) | Distributed Lock with Lease Pattern Lock expires after lease_ttl (logical time, not wall-clock). Assert: lock is reacquirable after expiry, holder can renew. | — |
| [`lww_conflict_resolve`](python/system-administration/mesh-distributed/lww_conflict_resolve.py) | Last-Write-Wins (LWW) Conflict Resolution Pattern When replicas diverge (partition), use Lamport clock to resolve. Higher timestamp wins, lower is discarded. Assert: both replicas… | — |
| [`partition_tolerance_demo`](python/system-administration/mesh-distributed/partition_tolerance_demo.py) | Partition Tolerance Demo Simulate network partition: cluster splits into two. Assert: majority partition proceeds, minority blocks (quorum lost). Partitions later rejoin: data… | — |
| [`quorum_check`](python/system-administration/mesh-distributed/quorum_check.py) | Quorum Check Pattern Write requires quorum (majority of nodes). Simulate: partition that loses majority can't write. Assert: quorum_lost() returns True when alive < majority. | — |

### monitoring-metrics

| Pattern | Description | Also in |
|---|---|---|
| [`counter_gauge_histogram`](python/system-administration/monitoring-metrics/counter_gauge_histogram.py) | counter_gauge_histogram: implement counter, gauge, and histogram metric types. | — |
| [`heartbeat_miss_alert`](python/system-administration/monitoring-metrics/heartbeat_miss_alert.py) | heartbeat_miss_alert: detect heartbeat/watchdog timeouts. | — |
| [`metric_export`](python/system-administration/monitoring-metrics/metric_export.py) | metric_export: export metrics in standard formats. | — |
| [`p2_percentile`](python/system-administration/monitoring-metrics/p2_percentile.py) | p2_percentile: P2 algorithm (Jain & Chlamtac 1985) for online percentile estimation. The P2 estimator keeps only FIVE markers (O(1) memory) and never stores the stream. The middle… | — |
| [`rate_calc`](python/system-administration/monitoring-metrics/rate_calc.py) | rate_calc: calculate rate (e.g., requests per second) from counter. | — |
| [`sliding_aggregate`](python/system-administration/monitoring-metrics/sliding_aggregate.py) | sliding_aggregate: compute rolling aggregates (sum, avg, min, max). | — |
| [`slo_error_budget`](python/system-administration/monitoring-metrics/slo_error_budget.py) | slo_error_budget: track error budget against SLO. | — |
| [`threshold_alert`](python/system-administration/monitoring-metrics/threshold_alert.py) | threshold_alert: fire alerts when metrics cross thresholds. | — |
| [`uptime_calc`](python/system-administration/monitoring-metrics/uptime_calc.py) | uptime_calc: calculate uptime percentage from events. | — |
| [`zscore_anomaly`](python/system-administration/monitoring-metrics/zscore_anomaly.py) | zscore_anomaly: detect anomalies using z-score. | — |

### network-health

| Pattern | Description | Also in |
|---|---|---|
| [`dns_resolve_check`](python/system-administration/network-health/dns_resolve_check.py) | dns_resolve_check: resolve a hostname; return resolved IP or None if DNS fails. Failure simulated: resolve localhost (succeeds), resolve guaranteed-bogus name (fails). Recovery… | Go |
| [`exponential_backoff`](python/system-administration/network-health/exponential_backoff.py) | exponential_backoff: retry with exponential backoff (2^attempt * base_delay); assert delays increase. Failure simulated: operation fails first 3 times, succeeds on 4th; measure… | Go, Rust |
| [`failover_switch`](python/system-administration/network-health/failover_switch.py) | failover_switch: when primary endpoint fails, switch to secondary; assert the switch happens. Failure simulated: primary server fails; failover_switch should detect and return… | — |
| [`heartbeat_gossip`](python/system-administration/network-health/heartbeat_gossip.py) | heartbeat_gossip: gossip protocol where nodes exchange heartbeats to detect failures. Failure simulated: node_1 sends heartbeats; node_2 stops sending; node_1 should detect node_2… | — |
| [`http_health_probe`](python/system-administration/network-health/http_health_probe.py) | http_health_probe: probe HTTP /health endpoint; return status_ok if 200, down if connection refused. Failure simulated: start an http.server on 127.0.0.1:ephemeral, probe /health,… | — |
| [`latency_measure`](python/system-administration/network-health/latency_measure.py) | latency_measure: measure round-trip latency between two endpoints on localhost. Failure simulated: measure latency from client to server socket; verify latency ≥ 0 and ≤… | — |
| [`reachability_matrix`](python/system-administration/network-health/reachability_matrix.py) | reachability_matrix: probe all nodes against all endpoints; build a matrix of reachability. Failure simulated: 3 nodes with 3 endpoints each; after one endpoint fails, matrix… | — |
| [`retry_timeout`](python/system-administration/network-health/retry_timeout.py) | retry_timeout: retry an operation with a timeout; fail if it doesn't succeed within deadline. Failure simulated: operation fails 3 times in succession, then succeeds on 4th try.… | — |
| [`split_brain_detect`](python/system-administration/network-health/split_brain_detect.py) | split_brain_detect: detect network partitions by checking if a quorum can reach each other. Failure simulated: 3-node cluster where node_3 becomes isolated; quorum detection… | — |
| [`tcp_port_check`](python/system-administration/network-health/tcp_port_check.py) | tcp_port_check: attempt to connect to a port; return True if reachable, False if down/refused. Failure simulated: bind a real socket on 127.0.0.1:ephemeral, verify it's up, close… | — |

### packaging-environment

| Pattern | Description | Also in |
|---|---|---|
| [`binary_presence_check`](python/system-administration/packaging-environment/binary_presence_check.py) | binary_presence_check: verify that required binaries are installed and executable. Failure simulated: a required binary is missing or not executable. The checker must detect both… | Go |
| [`capability_probe`](python/system-administration/packaging-environment/capability_probe.py) | capability_probe: probe system capabilities (hardlinks, symlinks, sparse files, etc.) and record which are available. Mutate the system state (remove capability) and re-probe;… | Go |
| [`depgraph_resolve`](python/system-administration/packaging-environment/depgraph_resolve.py) | depgraph_resolve: resolve a dependency graph and detect cycles. Must name the cycle. A broken cycle detector would either miss it or crash. This one catches it and reports the… | — |
| [`deps_verify`](python/system-administration/packaging-environment/deps_verify.py) | deps_verify: verify a dependency manifest exists, all versions are pinned, and checksums match. Failure simulated: a malicious dep replaces a legitimate one with a different… | Go |
| [`dryrun_installer`](python/system-administration/packaging-environment/dryrun_installer.py) | dryrun_installer: perform a dry-run installation (no actual modifications), verify it would succeed, then do a real installation and verify the system state changed correctly. The… | Go |
| [`env_diff`](python/system-administration/packaging-environment/env_diff.py) | env_diff: compare two environment dictionaries (env vars) and report differences. Failure simulated: missing a key variable, wrong value, or extra variable. The differ must… | Go |
| [`lockfile_hash_integrity`](python/system-administration/packaging-environment/lockfile_hash_integrity.py) | lockfile_hash_integrity: store dep checksums in a lockfile; verify them; tamper one and detect the break. Each entry is hashed (SHA256 of the dep content). Tampering with the… | — |
| [`path_sanity`](python/system-administration/packaging-environment/path_sanity.py) | path_sanity: verify that required binaries exist in PATH and are at expected locations. Failure simulated: a binary is moved/deleted, or a malicious binary is injected earlier in… | — |
| [`reproducible_build_check`](python/system-administration/packaging-environment/reproducible_build_check.py) | reproducible_build_check: build twice with identical inputs, verify byte-for-byte output matches. Then mutate one input and verify the build differs. This detects non-determinism… | — |
| [`version_constraint_solve`](python/system-administration/packaging-environment/version_constraint_solve.py) | version_constraint_solve: given constraints {name: constraint_str}, resolve to valid versions or raise ValueError if unsatisfiable. Must reject conflicting constraints and accept… | — |

### process-supervision

| Pattern | Description | Also in |
|---|---|---|
| [`crash_loop_detector`](python/system-administration/process-supervision/crash_loop_detector.py) | crash_loop_detector: count restarts in a sliding window; if threshold exceeded, flag crash-loop + stop restarting. Failure simulated: 6 restarts in 60 seconds (exceeds threshold… | Go |
| [`graceful_shutdown_sigterm`](python/system-administration/process-supervision/graceful_shutdown_sigterm.py) | graceful_shutdown_sigterm: install SIGTERM handler, save state gracefully, and exit. On receiving SIGTERM the handler writes a state file, then the process exits cleanly. The… | — |
| [`heartbeat_liveness`](python/system-administration/process-supervision/heartbeat_liveness.py) | heartbeat_liveness: periodic heartbeat from a process; detector marks dead if none arrive by deadline. Failure simulated: heartbeat stops; deadline passes. Recovery asserted:… | — |
| [`keepalive_daemon`](python/system-administration/process-supervision/keepalive_daemon.py) | keepalive_daemon: a background thread pokes a keepalive file every interval; a watcher treats the process as alive only while pokes keep arriving within a timeout. Failure… | — |
| [`pidfile_singleton`](python/system-administration/process-supervision/pidfile_singleton.py) | pidfile_singleton: prevent multiple instances via pidfile; if pidfile exists and pid alive, refuse start. Failure simulated: second instance attempts to start. Recovery asserted:… | — |
| [`readiness_vs_liveness`](python/system-administration/process-supervision/readiness_vs_liveness.py) | readiness_vs_liveness: liveness = the process is running; readiness = it can serve requests. They are INDEPENDENT, and the point of the distinction is operational: a router must… | — |
| [`restart_backoff`](python/system-administration/process-supervision/restart_backoff.py) | restart_backoff: on repeated crashes, increase delay between restarts: 1, 2, 4, 8, ... (capped). Failure simulated: child crashes repeatedly. Recovery asserted: measure delays;… | — |
| [`supervised_child`](python/system-administration/process-supervision/supervised_child.py) | supervised_child: spawn a child process; supervisor monitors and restarts on death. Failure simulated: child process dies. Recovery asserted: supervisor detects death and… | — |
| [`watchdog_restart`](python/system-administration/process-supervision/watchdog_restart.py) | watchdog_restart: a real watchdog supervises a child, restarts it on death up to a cap, then STOPS restarting and flags a crash-loop once the cap is exceeded. Failure simulated:… | — |
| [`zombie_reaper`](python/system-administration/process-supervision/zombie_reaper.py) | zombie_reaper: spawn child; when child exits, reap it via SIGCHLD handler to prevent zombie. Failure simulated: spawn child, let it exit, parent doesn't wait immediately. Recovery… | — |

### resource-guards

| Pattern | Description | Also in |
|---|---|---|
| [`backpressure_queue`](python/system-administration/resource-guards/backpressure_queue.py) | Backpressure queue: refuses (non-blocking put_nowait) items when the bounded queue is full. Failure simulated: flood queue with 1000 items, cap=64; assert items are refused after… | Go |
| [`circuit_breaker`](python/system-administration/resource-guards/circuit_breaker.py) | Circuit breaker: opens after N failures, short-circuits further calls. Failure simulated: call function 100 times, it fails first 10 times; assert breaker opens after 10 failures,… | Go, Rust |
| [`cpu_throttle`](python/system-administration/resource-guards/cpu_throttle.py) | CPU throttle: caps concurrent CPU-bound workers, refuses spawning past limit. Failure simulated: spawn 1000 CPU-bound workers with cap=4 concurrent; assert peak concurrent ≤ 4,… | Go |
| [`disk_space_watchdog`](python/system-administration/resource-guards/disk_space_watchdog.py) | Disk space watchdog: refuses writes when available space < threshold. Failure simulated: "fill" disk by tracking usage, attempt 1000 writes with cap=100MB; assert guard refuses… | Go |
| [`fd_leak_detector`](python/system-administration/resource-guards/fd_leak_detector.py) | File descriptor leak detector: caps open fds, refuses opens past limit. Failure simulated: open 1000 fds, assert the guard trips before exhaustion and peak fds never reach 1000… | Go |
| [`inode_guard`](python/system-administration/resource-guards/inode_guard.py) | Inode guard: refuses file creation past inode limit. Failure simulated: create 10000 files with cap=100; assert guard refuses creation when inode count reaches cap, peak ≤ cap. | — |
| [`load_shedding`](python/system-administration/resource-guards/load_shedding.py) | Load shedding: drops excess requests to keep served load ≤ capacity. Failure simulated: submit 1000 requests with capacity=64; assert served ≤ 64, dropped > 900, peak served ≤… | — |
| [`memory_cap_guard`](python/system-administration/resource-guards/memory_cap_guard.py) | Memory cap guard: refuses allocations past limit, keeps peak ≤ cap. Failure simulated: allocate 100 chunks × 10MB each (1GB total) with cap=256MB; assert guard raises MemoryError… | — |
| [`tmp_cleanup`](python/system-administration/resource-guards/tmp_cleanup.py) | Tmp cleanup: auto-cleans temp files when usage exceeds quota. Failure simulated: create files until 200MB used, auto-cleanup kicks at 150MB; assert final size stays ≤ 150MB after… | — |
| [`token_bucket_limiter`](python/system-administration/resource-guards/token_bucket_limiter.py) | Token bucket limiter: caps operation rate to tokens/sec. Failure simulated: issue 1000 ops over 2 sec with 10 tokens/sec cap; assert only ~20 ops granted, rest delayed/denied. | — |

### scheduling-jobs

| Pattern | Description | Also in |
|---|---|---|
| [`cron_expr_next_fire`](python/system-administration/scheduling-jobs/cron_expr_next_fire.py) | Cron expression parser: calculate next fire time exactly. Failure simulated: parse a cron expression and compute the EXACT next fire timestamp. Assert: next_fire() produces the… | Go |
| [`dead_letter_queue`](python/system-administration/scheduling-jobs/dead_letter_queue.py) | Dead letter queue: move jobs to DLQ after N consecutive failures. Failure simulated: job fails N times; assert it moves to DLQ exactly once. | Go |
| [`idempotency_key`](python/system-administration/scheduling-jobs/idempotency_key.py) | Idempotency key: same key submitted twice → operation runs exactly once. Failure simulated: submit same key twice concurrently; assert callback fires once. | — |
| [`interval_scheduler`](python/system-administration/scheduling-jobs/interval_scheduler.py) | Interval scheduler: fire a job at fixed intervals. Failure simulated: verify job fires at each expected interval boundary, no missed runs. Assert: execution times match expected… | — |
| [`jitter_backoff`](python/system-administration/scheduling-jobs/jitter_backoff.py) | Jitter backoff: add randomness to retry delays to prevent thundering herd. Failure simulated: N jobs all retry at the same time; assert jitter spreads fires across time. | — |
| [`job_dedup`](python/system-administration/scheduling-jobs/job_dedup.py) | Job dedup: ensure only one instance of a job runs at a time. Failure simulated: launch same job twice concurrently; assert only one runs. | — |
| [`missed_run_catchup`](python/system-administration/scheduling-jobs/missed_run_catchup.py) | Missed run catchup: detect and execute missed scheduled runs. Failure simulated: job is paused for N intervals; assert all missed runs are caught up. | — |
| [`oneshot_at_time`](python/system-administration/scheduling-jobs/oneshot_at_time.py) | Oneshot scheduler: fire a job exactly once at a specified time. Failure simulated: oneshot is submitted multiple times; assert it fires exactly once. | — |
| [`retry_with_backoff`](python/system-administration/scheduling-jobs/retry_with_backoff.py) | Retry with backoff: exponential backoff for failed operations. Failure simulated: callback fails N times; assert retry delays grow exponentially. | — |
| [`timeout_kill`](python/system-administration/scheduling-jobs/timeout_kill.py) | Timeout kill: terminate a subprocess if it exceeds timeout. Failure simulated: spawn a hanging child; assert it's killed within timeout, not before. | Go |

### secrets-credentials

| Pattern | Description | Also in |
|---|---|---|
| [`enforce_600_perms`](python/system-administration/secrets-credentials/enforce_600_perms.py) | Enforce 0o600 perms on secrets: reject world-readable files. Failure simulated: create secret file with 0o644 (world-readable); guard detects and rejects read, or forces chmod to… | Go |
| [`env_secret_load`](python/system-administration/secrets-credentials/env_secret_load.py) | Env secret load: load secrets from env var without exposing them to logs/stdout. Failure simulated: load secret from env, assert it's not printed to stdout/stderr, and not stored… | Go |
| [`expiry_check`](python/system-administration/secrets-credentials/expiry_check.py) | Expiry check: reject tokens based on logical clock, not wall-clock. Failure simulated: token expires at clock=100; check at clock=50 (accept), then at clock=150 (reject). Assert… | Go |
| [`keyring_store`](python/system-administration/secrets-credentials/keyring_store.py) | Keyring store: persist secrets in protected file (0o600), prevent world access. Failure simulated: store secret in file, verify file perms are 0o600, retrieve secret, assert it… | — |
| [`leaked_secret_scan`](python/system-administration/secrets-credentials/leaked_secret_scan.py) | Leaked secret scan: detect secrets in code blobs via regex patterns. Failure simulated: blob contains "password = 'hunter2'" and API key patterns; scan detects and reports exact… | — |
| [`least_privilege_check`](python/system-administration/secrets-credentials/least_privilege_check.py) | Least privilege check: verify secret file has no world/group read bits. Failure simulated: create secret with mode 0o666 (world+group readable); guard checks and rejects or strips… | — |
| [`log_redaction`](python/system-administration/secrets-credentials/log_redaction.py) | Log redaction: redact secrets from log output, never write plaintext to disk. Failure simulated: log message containing secret string; guard redacts it; assert secret NEVER… | — |
| [`secret_audit_trail`](python/system-administration/secrets-credentials/secret_audit_trail.py) | Secret audit trail: immutable append-only log of all secret access. Failure simulated: log 10 secret accesses (read/write); replay log; assert exact sequence matches, all entries… | — |
| [`token_rotation`](python/system-administration/secrets-credentials/token_rotation.py) | Token rotation: keep only N most recent tokens, discard oldest on overflow. Failure simulated: add 100 tokens with cap=5; assert only 5 remain and oldest are gone. Defended… | — |
| [`ttl_cache`](python/system-administration/secrets-credentials/ttl_cache.py) | TTL cache: expire items based on logical clock TTL, not wall-clock. Failure simulated: cache item at clock=0 with TTL=100; access at clock=50 (hit), then clock=150 (miss/expired).… | — |

### state-db-durability

| Pattern | Description | Also in |
|---|---|---|
| [`backup_rotation`](python/system-administration/state-db-durability/backup_rotation.py) | backup_rotation: keep N versioned backups; rotate with ATOMIC renames so a crash during rotation never tears a file and never loses the newest backup. Failure simulated: SIGKILL… | Go |
| [`corruption_repair`](python/system-administration/state-db-durability/corruption_repair.py) | corruption_repair: detect and repair SQLite DB corruption (or mark unrecoverable). The disaster test creates a valid database, backs it up, truncates the live DB mid-write to… | Go |
| [`crash_consistent_snapshot`](python/system-administration/state-db-durability/crash_consistent_snapshot.py) | crash_consistent_snapshot: snapshot a live DB atomically (backup -> temp -> fsync -> rename) so the snapshot is NEVER visible in a torn state. Failure simulated: SIGKILL the… | Go |
| [`hot_copy`](python/system-administration/state-db-durability/hot_copy.py) | Hot-copy a live SQLite database into a consistent point-in-time snapshot. Uses SQLite's backup API while a writer is actively committing inserts. The resulting copy must be a… | — |
| [`integrity_check`](python/system-administration/state-db-durability/integrity_check.py) | integrity_check: detect DB corruption via PRAGMA integrity_check (and catch open/query failures). Failure simulated: overwrite a b-tree data page in the middle of the file with… | — |
| [`journaled_write`](python/system-administration/state-db-durability/journaled_write.py) | journaled_write: write data to a journal first, then apply to the main store (undo logging). Failure simulated: crash between journal write and main store update. Recovery… | — |
| [`migration_with_rollback`](python/system-administration/state-db-durability/migration_with_rollback.py) | Migration with rollback: crash mid-migration, schema must stay consistent. The test creates a temporary SQLite database with an old schema, starts a child process to run a… | — |
| [`point_in_time_restore`](python/system-administration/state-db-durability/point_in_time_restore.py) | point_in_time_restore: restore a DB to an exact point in time = a base backup + replay of the write-ahead log up to a target timestamp (no entry newer than the target is applied).… | — |
| [`transaction_rollback`](python/system-administration/state-db-durability/transaction_rollback.py) | Transaction rollback: crash inside an active transaction before COMMIT. A child process inserts a committed row, begins a transaction with two more uncommitted rows, then is… | — |
| [`wal_checkpoint`](python/system-administration/state-db-durability/wal_checkpoint.py) | wal_checkpoint: SQLite WAL (Write-Ahead Log) checkpoint that replays changes to the main DB. Failure simulated: crash DURING checkpoint, after some pages flushed but before… | — |

### system-introspection

| Pattern | Description | Also in |
|---|---|---|
| [`load_avg_read`](python/system-administration/system-introspection/load_avg_read.py) | load_avg_read: Parse /proc/loadavg (1min, 5min, 15min load averages). THE ONE LAW: Parse exact values, fail on missing fields. | — |
| [`memory_pressure`](python/system-administration/system-introspection/memory_pressure.py) | memory_pressure: Parse /proc/pressure/memory for PSI (Pressure Stall Info) metrics. THE ONE LAW: Parse exact pressure values, fail on incomplete data. | — |
| [`mount_disk_usage`](python/system-administration/system-introspection/mount_disk_usage.py) | mount_disk_usage: Parse mount output and extract filesystem usage. THE ONE LAW: Parse real df-style output, assert exact usage percentages. | — |
| [`open_fd_count`](python/system-administration/system-introspection/open_fd_count.py) | open_fd_count: Count open file descriptors from /proc/[pid]/fd. THE ONE LAW: Parse directory listing, assert exact count matches directory size. Portable fallback on non-Linux. | — |
| [`orphan_detect`](python/system-administration/system-introspection/orphan_detect.py) | orphan_detect: Identify orphaned processes (parent pid doesn't exist). THE ONE LAW: Parse tree, identify orphans by ppid not in known pids, return exact list. | — |
| [`proc_parse_portable`](python/system-administration/system-introspection/proc_parse_portable.py) | proc_parse_portable: Parse /proc-style process info, portable across platforms. Handles missing /proc gracefully; tests against synthetic data regardless. THE ONE LAW: Simulate… | — |
| [`process_tree`](python/system-administration/system-introspection/process_tree.py) | process_tree: Build process tree from /proc-style data, re-parent orphans to ppid=1. THE ONE LAW: Parse process list with dead-parent process, assert it's re-parented to 1.… | — |
| [`resource_usage`](python/system-administration/system-introspection/resource_usage.py) | resource_usage: Extract memory/CPU metrics from /proc/[pid]/status. THE ONE LAW: Parse real data, assert exact values; simulate missing fields, assert error. | — |
| [`top_n_by_resource`](python/system-administration/system-introspection/top_n_by_resource.py) | top_n_by_resource: Rank processes by a resource metric (RSS, CPU, etc.). THE ONE LAW: Sort and rank, assert exact ordering; simulate unsorted input. | — |
| [`uptime_read`](python/system-administration/system-introspection/uptime_read.py) | uptime_read: Parse /proc/uptime to extract uptime in seconds and idle time. THE ONE LAW: Parse exact values, assert single clock (no time() calls during parse). | — |

### text-stream-ops

| Pattern | Description | Also in |
|---|---|---|
| [`ansi_strip`](python/system-administration/text-stream-ops/ansi_strip.py) | ansi_strip: Strip ANSI escape codes from text (colors, bold, etc.). THE ONE LAW: Remove all escape sequences, assert exact output. | Go |
| [`dedup_stream`](python/system-administration/text-stream-ops/dedup_stream.py) | dedup_stream: Remove duplicate lines while preserving order. THE ONE LAW: Deduplicate stream, assert exact count and order preservation. | Go |
| [`field_extract`](python/system-administration/text-stream-ops/field_extract.py) | field_extract: Extract specific fields from whitespace-separated lines. THE ONE LAW: Parse real data with varying field counts, assert exact extraction. | Go |
| [`logline_parse`](python/system-administration/text-stream-ops/logline_parse.py) | logline_parse: Parse syslog-style log lines (timestamp priority host process message). THE ONE LAW: Parse messy real-world log data, assert exact extraction. | — |
| [`merge_sorted_streams`](python/system-administration/text-stream-ops/merge_sorted_streams.py) | merge_sorted_streams: Merge N sorted streams into one sorted stream. THE ONE LAW: Merge streams, assert exact global sortedness and no data loss. | — |
| [`multiline_join`](python/system-administration/text-stream-ops/multiline_join.py) | multiline_join: Join split multiline log entries (e.g., Python stacktraces). THE ONE LAW: Parse real messy multiline data with proper continuation detection. | — |
| [`robust_csv_parse`](python/system-administration/text-stream-ops/robust_csv_parse.py) | robust_csv_parse: Parse CSV with edge cases (quotes, embedded commas, newlines in fields). THE ONE LAW: Handle real CSV edge cases, reject genuinely broken rows with precise… | — |
| [`structured_diff`](python/system-administration/text-stream-ops/structured_diff.py) | structured_diff: Diff two structured outputs (e.g., process lists, config states). THE ONE LAW: Parse both versions, identify exact adds/removes/changes. | — |
| [`tail_follow_stream`](python/system-administration/text-stream-ops/tail_follow_stream.py) | tail_follow_stream: Simulate tail -f behavior (read from file position, follow new lines). THE ONE LAW: Track file position, read only new lines, handle file rotation edge case. | — |
| [`throughput_meter`](python/system-administration/text-stream-ops/throughput_meter.py) | throughput_meter: Calculate throughput (items/sec or bytes/sec). THE ONE LAW: Track time windows, calculate exact rate, handle zero-duration edge cases. | — |

### time-clock-correctness

| Pattern | Description | Also in |
|---|---|---|
| [`clock_skew_detect`](python/system-administration/time-clock-correctness/clock_skew_detect.py) | Detect backward wall-clock jumps from a stream of time samples. SkewDetector records successive wall-clock readings and flags any sample that is earlier than the previous one (a… | Go |
| [`deadline_ttl`](python/system-administration/time-clock-correctness/deadline_ttl.py) | Deadline/TTL checker over an injectable clock. DeadlineChecker turns a TTL into an absolute deadline via a supplied clock function, then reports whether that deadline has passed… | Go |
| [`drift_compensation`](python/system-administration/time-clock-correctness/drift_compensation.py) | Compensate for clock drift (clock running fast or slow). | Go |
| [`leap_safe_interval`](python/system-administration/time-clock-correctness/leap_safe_interval.py) | Compute time intervals correctly across leap second insertions. | — |
| [`monotonic_vs_wall`](python/system-administration/time-clock-correctness/monotonic_vs_wall.py) | Monotonic clock immune to wall-clock backward jumps. | — |
| [`ntp_offset_check`](python/system-administration/time-clock-correctness/ntp_offset_check.py) | Validate an NTP clock offset against a maximum bound. NTPValidator checks a reported time offset against a configured maximum magnitude: it accepts offsets within bounds… | — |
| [`sliding_rate_window`](python/system-administration/time-clock-correctness/sliding_rate_window.py) | Rate limiting using sliding time window. | — |
| [`timeout_budget`](python/system-administration/time-clock-correctness/timeout_budget.py) | Budget timeouts across multiple sequential operations. | — |
| [`two_clocks_reconcile`](python/system-administration/time-clock-correctness/two_clocks_reconcile.py) | Reconcile two independent clock sources (e.g., system + hardware). | — |
| [`tz_safe_timestamp`](python/system-administration/time-clock-correctness/tz_safe_timestamp.py) | Safe timezone-aware timestamp handling without DST confusion. | — |

## r

*60 files across 9 categories.*

### data_wrangling_and_feature_engineering

| Pattern | Description | Also in |
|---|---|---|
| [`date_features`](r/data_wrangling_and_feature_engineering/date_features.R) | Date Feature Engineering Implements Date → weekday/month/quarter/is-weekend; verified against known calendar Use when: extracting temporal features | — |
| [`factor_onehot`](r/data_wrangling_and_feature_engineering/factor_onehot.R) | One-Hot Encoding from Factors Implements one-hot from factor levels; column sums equal level counts; unseen-level policy Use when: converting categorical to numeric features | — |
| [`group_aggregate`](r/data_wrangling_and_feature_engineering/group_aggregate.R) | Group-by Aggregation (Multi-key) Implements multi-key grouping via loops/split; verifies against aggregate() Use when: summarizing data by multiple grouping variables | — |
| [`hash_join`](r/data_wrangling_and_feature_engineering/hash_join.R) | Hash Join (Environment as Hashmap) Implements join via environment hashmap; verifies against merge() Use when: joining tables on keys and want explicit control | — |
| [`long_wide_reshape`](r/data_wrangling_and_feature_engineering/long_wide_reshape.R) | Long-Wide Reshape (Both Directions) Implements reshape manually both directions; round-trip identity + spot-check vs reshape() Use when: transforming data layout | — |
| [`missing_pattern_matrix`](r/data_wrangling_and_feature_engineering/missing_pattern_matrix.R) | missing_pattern_matrix.R Missing data pattern analysis: missingness patterns and correlation handling. Oracle: cor(use="pairwise.complete.obs") for pairwise correlation. Claim:… | — |
| [`na_imputation`](r/data_wrangling_and_feature_engineering/na_imputation.R) | NA Imputation (Mean/Median/Mode) Implements imputation strategies; verifies imputed stats match strategy Use when: handling missing data | — |
| [`rolling_stats`](r/data_wrangling_and_feature_engineering/rolling_stats.R) | Rolling Statistics (Mean & SD) Implements rolling mean/sd; window results equal brute force Use when: computing moving averages or smoothing time series | — |

### distributions_and_resampling

| Pattern | Description | Also in |
|---|---|---|
| [`bootstrap_ci`](r/distributions_and_resampling/bootstrap_ci.R) | Bootstrap Confidence Interval Implements percentile bootstrap; verifies coverage of true mean over repeated runs Use when: estimating CI without distributional assumptions | — |
| [`ecdf_dkw_bands`](r/distributions_and_resampling/ecdf_dkw_bands.R) | ECDF and DKW Confidence Bands: empirical CDF with probability coverage Implements Dvoretzky-Kiefer-Wolfowitz bands: Fn(x) ± ε with ε = sqrt(log(2/α)/(2n)) Core: compute ECDF at… | — |
| [`kde_gaussian`](r/distributions_and_resampling/kde_gaussian.R) | Kernel Density Estimation (Gaussian KDE) Implements gaussian KDE with Silverman bandwidth by hand; verifies against density() Use when: estimating probability density and… | — |
| [`outlier_iqr_mad`](r/distributions_and_resampling/outlier_iqr_mad.R) | Outlier Detection (IQR & MAD) Implements IQR fences + MAD z-scores; planted outliers caught, clean data passes Use when: identifying extreme values | — |
| [`quantile_type7`](r/distributions_and_resampling/quantile_type7.R) | Quantile Type 7: R's default interpolation method (linear between order statistics) Implements h=(n-1)*p, quantile = x_{floor(h)+1} + (h-floor(h))*(x_{floor(h)+2} -… | — |

### hypothesis_testing_parametric

| Pattern | Description | Also in |
|---|---|---|
| [`ab_power_analysis`](r/hypothesis_testing_parametric/ab_power_analysis.R) | ab_power_analysis.R Two-proportion power analysis from normal approximation. Oracle: power.prop.test() in stats. Claim: manual n and power calculations match oracle. Tolerance: n… | — |
| [`anova_tukey`](r/hypothesis_testing_parametric/anova_tukey.R) | anova_tukey.R Tukey's HSD test via studentized range distribution (qtukey). Oracle: TukeyHSD() in stats. Claim: manual pairwise intervals match oracle. Tolerance: interval bounds… | — |
| [`correlation_tests`](r/hypothesis_testing_parametric/correlation_tests.R) | Correlation Tests (Pearson & Spearman) Implements both by hand; verifies against cor() and cor.test() Use when: assessing linear or monotonic association between variables | — |
| [`ks_one_sample`](r/hypothesis_testing_parametric/ks_one_sample.R) | Kolmogorov-Smirnov One-Sample Test: D statistic vs known CDF Implements empirical CDF and maximum deviation from theoretical CDF Core: sort data, compute Fn(x) = (# ≤ x)/n,… | — |
| [`one_way_anova`](r/hypothesis_testing_parametric/one_way_anova.R) | One-Way ANOVA Implements F statistic from sum of squares; verifies against aov() Use when: comparing means across 3+ groups | — |
| [`prop_test_two_sample`](r/hypothesis_testing_parametric/prop_test_two_sample.R) | Two-Proportion Z-Test with Pooled Variance Implements z-statistic for H0: p1=p2; compares to prop.test(correct=FALSE) Core: pooled proportion p_pool = (x1+x2)/(n1+n2), SE =… | — |
| [`welch_t_test`](r/hypothesis_testing_parametric/welch_t_test.R) | Welch's t-test (unequal variance) Implements t statistic, df (Welch-Satterthwaite), p-value; verifies against t.test() Use when: comparing means of two groups with unequal variance | — |

### multivariate_and_applied_modeling

| Pattern | Description | Also in |
|---|---|---|
| [`km_survival_lite`](r/multivariate_and_applied_modeling/km_survival_lite.R) | km_survival_lite.R Kaplan-Meier survival curve with censoring (no oracle: hand-verify properties). _lite: manual implementation without optimizing for speed. Claim: stepwise… | — |
| [`kmeans_lloyd`](r/multivariate_and_applied_modeling/kmeans_lloyd.R) | K-Means via Lloyd's Algorithm Implements Lloyd's algorithm by hand; verifies within-cluster SS matches kmeans() Use when: unsupervised clustering and need deterministic,… | — |
| [`pca_power_iteration`](r/multivariate_and_applied_modeling/pca_power_iteration.R) | PCA via Power Iteration (with deflation) — oracle-verified against prcomp() Power iteration finds the dominant eigenvector of the covariance matrix; DEFLATION (subtract lambda1 *… | C++, Python |
| [`stratified_split`](r/multivariate_and_applied_modeling/stratified_split.R) | Stratified Train-Test Split Implements stratified split preserving class proportions; proportions asserted within tolerance Use when: maintaining class balance in train-test split | — |
| [`weighted_survey_mean`](r/multivariate_and_applied_modeling/weighted_survey_mean.R) | weighted_survey_mean.R Weighted mean with design effect-adjusted standard error for survey data. Oracle: weighted.mean() for means; manual SE with design effect correction. Claim:… | — |

### nonparametric_and_categorical

| Pattern | Description | Also in |
|---|---|---|
| [`chi_square_independence`](r/nonparametric_and_categorical/chi_square_independence.R) | Chi-Square Test of Independence Implements chi-square statistic from expected counts; verifies against chisq.test() Use when: testing association between two categorical variables | C++, Python |
| [`cramers_v_effect`](r/nonparametric_and_categorical/cramers_v_effect.R) | cramers_v_effect.R Cramér's V effect size from chi-square test. Oracle: chisq.test() for chi-square statistic. Claim: V computed from chi-square matches oracle; strong association… | — |
| [`fisher_exact_2x2`](r/nonparametric_and_categorical/fisher_exact_2x2.R) | Fisher's Exact Test: hypergeometric enumeration for 2x2 contingency tables Implements one-tailed p-value by enumerating tables with fixed marginals; compares to fisher.test()… | — |
| [`kruskal_wallis`](r/nonparametric_and_categorical/kruskal_wallis.R) | Kruskal-Wallis Test: H statistic from ranks (k≥3 groups) Implements rank-based ANOVA; compares to kruskal.test() H statistic + p-value Core: rank all observations, compute group… | — |
| [`table_margins`](r/nonparametric_and_categorical/table_margins.R) | Contingency Table with Margins Implements table + margins by hand; verifies against table() + addmargins() Use when: cross-tabulating categorical variables | — |
| [`wilcoxon_rank_sum`](r/nonparametric_and_categorical/wilcoxon_rank_sum.R) | Wilcoxon Rank-Sum Test: U statistic + normal approximation p-value from scratch Implements Mann-Whitney U via rank sums; compares to wilcox.test(correct=FALSE) p-value Core: rank… | — |

### regression_and_glm

| Pattern | Description | Also in |
|---|---|---|
| [`bootstrap_regression`](r/regression_and_glm/bootstrap_regression.R) | bootstrap_regression.R Case-resampling bootstrap for linear regression slope confidence interval. Claim: bootstrap CI covers planted slope; CI width shrinks with larger n.… | — |
| [`cv_model_selection`](r/regression_and_glm/cv_model_selection.R) | cv_model_selection.R k-fold cross-validation for polynomial degree selection. Claim: CV MSE selects true-degree model over under/over-fit. Tolerance: true degree has lowest CV MSE… | — |
| [`hosmer_lemeshow_lite`](r/regression_and_glm/hosmer_lemeshow_lite.R) | hosmer_lemeshow_lite.R Hosmer-Lemeshow calibration test for logistic regression. _lite: manual decile table without correction for ties. Claim: well-calibrated model passes; badly… | — |
| [`linear_regression_normal_eq`](r/regression_and_glm/linear_regression_normal_eq.R) | Linear Regression via Normal Equations Implements y = Xβ using (X^T X)^-1 X^T y; verifies against lm() to 1e-8 Use when: need coefficients and understand matrix form | — |
| [`lm_diagnostics`](r/regression_and_glm/lm_diagnostics.R) | lm_diagnostics.R Regression diagnostics: leverage, standardized residuals, Cook's distance. Oracle: hatvalues(), rstandard(), cooks.distance() in stats. Claim: manual diagnostics… | — |
| [`logistic_regression_irls`](r/regression_and_glm/logistic_regression_irls.R) | Logistic Regression via IRLS (Iteratively Reweighted Least Squares) Implements IRLS loop by hand; verifies coefficients against glm(family=binomial) to 1e-6 Use when: binary… | — |
| [`poisson_regression_irls`](r/regression_and_glm/poisson_regression_irls.R) | Poisson Regression via Iteratively Reweighted Least Squares (IRLS) with log link Implements Newton-Raphson on deviance via weighted regression; compares to glm(family=poisson)… | — |
| [`ridge_regression`](r/regression_and_glm/ridge_regression.R) | Ridge Regression: closed-form (X'X + λI)^-1 X'y Implements Tikhonov regularization for multiple regression; verifies λ=0 equals lm() and monotonic shrinkage Core: solve (X'X + λI)… | — |

### sampling_and_simulation

| Pattern | Description | Also in |
|---|---|---|
| [`box_muller`](r/sampling_and_simulation/box_muller.R) | Box-Muller Transform: generate bivariate independent gaussians from uniforms Implements Z1 = sqrt(-2*log(U1)) * cos(2π*U2), Z2 = sqrt(-2*log(U1)) * sin(2π*U2) Core: two… | — |
| [`inverse_cdf_sampling`](r/sampling_and_simulation/inverse_cdf_sampling.R) | Inverse-Transform Sampling: generate samples via F^{-1}(U) Implements inverse CDF for exponential and logistic; verifies via ks.test against true CDFs Core: U ~ Uniform(0,1), X =… | — |
| [`mvn_cholesky`](r/sampling_and_simulation/mvn_cholesky.R) | Multivariate Normal via Cholesky: Σ = LL', X = μ + L*Z with Z~N(0,I) Implements Cholesky factorization and verifies against chol() built-in; sample cov matches Σ Core: decompose… | — |
| [`order_statistics`](r/sampling_and_simulation/order_statistics.R) | Order Statistics: distribution of min/max/median of n uniforms Implements CDF and PDF of order statistics via Beta distributions Core: X_{(k)} ~ Beta(k, n-k+1) for uniform order… | — |
| [`poisson_process_thinning`](r/sampling_and_simulation/poisson_process_thinning.R) | Poisson Process Thinning: inhomogeneous Poisson via thinning of homogeneous process Implements Lewis-Shedler thinning: generate homogeneous PP, accept events with intensity ratio… | — |
| [`probability_integral_transform`](r/sampling_and_simulation/probability_integral_transform.R) | Probability Integral Transform: U = F(X) ~ Uniform(0,1) under correct F Implements: if X ~ F, then F(X) ~ Uniform(0,1); verifies via ks.test Core: if F is correct, PIT uniform and… | — |
| [`rejection_sampling_beta`](r/sampling_and_simulation/rejection_sampling_beta.R) | Rejection Sampling for Beta(2,5): use uniform envelope, accept/reject via density ratio Implements Beta density f(x)∝x(1-x)^4 via uniform proposal over [0,1] with envelope… | — |
| [`truncated_normal`](r/sampling_and_simulation/truncated_normal.R) | Truncated Normal: N(μ,σ²) on [a,b] via acceptance-rejection Implements: proposal from untruncated N(μ,σ²), accept if X in [a,b] Core: compute analytic truncated mean E[X\|a<X<b]… | — |

### time_series_models_and_autocorrelation

| Pattern | Description | Also in |
|---|---|---|
| [`acf_pacf_from_scratch`](r/time_series_models_and_autocorrelation/acf_pacf_from_scratch.R) | ACF and PACF from Scratch: Durbin-Levinson algorithm for partial autocorrelation Implements ACF directly and PACF via Durbin-Levinson recursion; verifies against acf()/pacf()… | — |
| [`ar1_fit_forecast`](r/time_series_models_and_autocorrelation/ar1_fit_forecast.R) | ar1_fit_forecast.R AR(1) model fit via conditional least squares and one-step forecast. Oracle: arima(order=c(1,0,0)) from stats. Claim: estimated coefficient close to oracle;… | — |
| [`ar_yule_walker`](r/time_series_models_and_autocorrelation/ar_yule_walker.R) | AR(p) via Yule-Walker Equations: solve from sample autocovariance Implements γ_j = Σ φ_k * γ_{\|j-k\|} as linear system (Rγ = γ_acov); matches ar(method="yw") Core: compute sample… | — |
| [`ccf_lag_detection`](r/time_series_models_and_autocorrelation/ccf_lag_detection.R) | ccf_lag_detection.R Cross-correlation function from scratch. Oracle: ccf() function in stats. Claim: manual CCF values match ccf() oracle exactly; planted lag detected as argmax.… | — |
| [`holt_winters_lite`](r/time_series_models_and_autocorrelation/holt_winters_lite.R) | holt_winters_lite.R Additive Holt-Winters from scratch (additive decomposition). _lite: manual alpha/beta/gamma, no optim() tuning. Claim: manual fitted values are smooth and… | — |
| [`ljung_box`](r/time_series_models_and_autocorrelation/ljung_box.R) | ljung_box.R Ljung-Box Q statistic for autocorrelation significance. Oracle: Box.test(type="Ljung-Box") in stats. Claim: manual Q statistic matches oracle; AR residuals pass, raw… | — |
| [`seasonal_decompose`](r/time_series_models_and_autocorrelation/seasonal_decompose.R) | seasonal_decompose.R Additive seasonal decomposition: trend via centered MA, seasonal via means. Oracle: decompose() function in stats. Claim: trend and seasonal components agree… | — |

### time_series_trend_spectral_and_smoothing

| Pattern | Description | Also in |
|---|---|---|
| [`diff_seasonality_test`](r/time_series_trend_spectral_and_smoothing/diff_seasonality_test.R) | diff_seasonality_test.R Seasonal differencing removes seasonality (ACF-based test). Claim: seasonal-lag autocorrelation high before differencing, near zero after. Tolerance: ACF @… | — |
| [`hampel_ts_outliers`](r/time_series_trend_spectral_and_smoothing/hampel_ts_outliers.R) | hampel_ts_outliers.R Hampel identifier: rolling median and MAD for spike removal. Claim: planted spikes detected and removed; clean data untouched on separate sample. Tolerance:… | — |
| [`mann_kendall_trend`](r/time_series_trend_spectral_and_smoothing/mann_kendall_trend.R) | Mann-Kendall Trend Test: Kendall's S statistic over time index Implements concordance pairs for trend detection; compares to cor.test(method="kendall") Core: count… | — |
| [`periodogram_spectral`](r/time_series_trend_spectral_and_smoothing/periodogram_spectral.R) | periodogram_spectral.R Periodogram from scratch (FFT-based power spectrum). Oracle: spec.pgram(taper=0, detrend=FALSE) in stats. Claim: manual periodogram values match oracle;… | — |
| [`rolling_origin_cv`](r/time_series_trend_spectral_and_smoothing/rolling_origin_cv.R) | rolling_origin_cv.R Walk-forward (rolling origin) cross-validation for time series. Claim: seasonal-naive forecast beats mean forecaster on seasonal data (measured MAE).… | — |
| [`sma_wma_filter`](r/time_series_trend_spectral_and_smoothing/sma_wma_filter.R) | sma_wma_filter.R Simple Moving Average (SMA) and Weighted Moving Average (WMA) via manual loop. Oracle: filter() function in base R (for SMA). Claim: loop-computed SMA/WMA values… | — |

## rust

*200 files across 10 categories.*

### composed-systems

| Pattern | Description | Also in |
|---|---|---|
| [`authenticated_message_channel`](rust/composed-systems/authenticated_message_channel.rs) | composes: frame-construct + keyed-checksum-append + transmit + verify-strip-decode | — |
| [`backup_snapshot_restore`](rust/composed-systems/backup_snapshot_restore.rs) | composes: snapshot-state + serialize-to-bytes + crash-truncate + deserialize-restore + exact-state-verify | — |
| [`bloom_backed_cache`](rust/composed-systems/bloom_backed_cache.rs) | ! bloom_backed_cache — bloom filter gates cache lookups; ZERO false negatives. ! ! Core idea: before checking an RwLock cache, query a bloom filter. If the bloom says ! "not… | — |
| [`checkpoint_resume_crc`](rust/composed-systems/checkpoint_resume_crc.rs) | ! checkpoint_resume_crc — checkpoint + CRC; crash after N records, resume without dups. ! ! Core idea: records are logged with a checkpoint marker every K records. On crash, !… | — |
| [`compressed_block_store`](rust/composed-systems/compressed_block_store.rs) | composes: rle-encode + checksum-compute + store + read-back-decode-verify | — |
| [`content_addressed_blob_store`](rust/composed-systems/content_addressed_blob_store.rs) | composes: hash-content + store-under-hash + dedup + integrity-check | — |
| [`content_addressed_store`](rust/composed-systems/content_addressed_store.rs) | ! content_addressed_store — blobs keyed by SHA-256; identical content dedups; corruption detected. ! ! Core idea: store blobs by their SHA-256 hash (content-addressed). Identical… | — |
| [`csv_typed_record_validator`](rust/composed-systems/csv_typed_record_validator.rs) | composes: csv-parse-rfc4180 + type-coercion + row-validation | — |
| [`dag_task_runner`](rust/composed-systems/dag_task_runner.rs) | ! dag_task_runner — topological readiness + a real thread worker-pool executing a DAG. ! ! Core idea: composes W2's topological ordering with W1's shared-queue worker pool. Tasks… | — |
| [`delta_sync_lite`](rust/composed-systems/delta_sync_lite.rs) | ! delta_sync_lite — rsync-style block delta: match shared blocks old↔new, transfer + RECONSTRUCT. ! ! Core idea: chunk OLD into fixed blocks and index them by hash. Scan NEW:… | — |
| [`framed_message_router`](rust/composed-systems/framed_message_router.rs) | composes: length-prefixed-deframing + type-header-parse + type-routed-dispatch Real deframing: messages arrive as ONE concatenated byte stream, each framed as… | — |
| [`health_checked_lb_router`](rust/composed-systems/health_checked_lb_router.rs) | composes: health-probe-backends + lb-select-healthy + failover-on-drop + recovery | — |
| [`idempotent_request_dedup`](rust/composed-systems/idempotent_request_dedup.rs) | composes: hash-request-id + dedup-cache + apply-once + replay-returns-cached-result | — |
| [`index_compaction_pipeline`](rust/composed-systems/index_compaction_pipeline.rs) | composes: build-inverted-index + apply-tombstone-deletes + compact + query-exact-live-postings | — |
| [`log_ingest_dedup_index`](rust/composed-systems/log_ingest_dedup_index.rs) | composes: line-parse + content-dedup + index-build | — |
| [`lsm_write_read_path`](rust/composed-systems/lsm_write_read_path.rs) | composes: memtable-write + sorted-run-flush + multi-run-merge-read | — |
| [`merkle_tree`](rust/composed-systems/merkle_tree.rs) | ! merkle_tree — SHA-256 tree; tampering any leaf changes root; inclusion proof verifies. ! ! Core idea: a binary tree where each node is the SHA-256 hash of its children. !… | Python |
| [`merkle_verified_sync`](rust/composed-systems/merkle_verified_sync.rs) | composes: chunk-two-versions + build-REAL-merkle-trees + root+subtree-diff + sync-only-changed A real merkle tree: leaves are chunk hashes, each internal node = hash(left, right),… | — |
| [`mvcc_snapshot_query_engine`](rust/composed-systems/mvcc_snapshot_query_engine.rs) | composes: versioned-writes-by-ts + snapshot-open-at-T + range-query-returns-versions-visible-at-T | — |
| [`rate_limited_request_pipeline`](rust/composed-systems/rate_limited_request_pipeline.rs) | composes: request-parse + sliding-window-rate-limit + status-classify + admit-deny | — |
| [`read_through_cache_store`](rust/composed-systems/read_through_cache_store.rs) | composes: cache-get + miss-load-from-backing + cache-fill + hit-skips-store + eviction | — |
| [`replicated_log_quorum`](rust/composed-systems/replicated_log_quorum.rs) | composes: append-to-N-replicas + lag + quorum-read + majority-VALUE-consensus A quorum read returns the (index, value) that a MAJORITY of replicas agree on — the value is… | — |
| [`retry_circuit_backoff_client`](rust/composed-systems/retry_circuit_backoff_client.rs) | composes: status-classify + exponential-backoff-schedule + circuit-breaker-open-after-K + exact-attempt-timeline | — |
| [`rotating_log_checksum`](rust/composed-systems/rotating_log_checksum.rs) | ! rotating_log_checksum — size-triggered rotation + per-segment CRC32; corruption isolated. ! ! Core idea: logs rotate every N bytes; when a segment is sealed its CRC32 is STORED.… | — |
| [`sharded_kv_rehash_router`](rust/composed-systems/sharded_kv_rehash_router.rs) | composes: rendezvous(HRW)-hash-to-shard + route + add-shard + MINIMAL-movement-rehash + verify Naive `key % n` reshuffles almost every key when n changes — so it cannot claim… | — |
| [`signed_snapshot`](rust/composed-systems/signed_snapshot.rs) | ! signed_snapshot — serialize a state map + HMAC-sign; tampering fails verify; restore equals original. ! ! Core idea: serialize a map into JSON-like format, compute HMAC-SHA256… | — |
| [`streaming_bloom_distinct`](rust/composed-systems/streaming_bloom_distinct.rs) | composes: parse-stream + k-hash-bloom-membership + cardinality-estimate-from-fill A real k-hash bloom filter (not a single bit). Membership guarantees NO false negatives, and the… | — |
| [`streaming_percentile_monitor`](rust/composed-systems/streaming_percentile_monitor.rs) | composes: parse-metric-samples + bounded-histogram-sketch + alert-on-threshold-cross | — |
| [`tamper_evident_log`](rust/composed-systems/tamper_evident_log.rs) | ! tamper_evident_log — HMAC-SHA256 hash-chained log; tampering detected at exact point. ! ! Core idea: each log entry includes the HMAC of (previous_hash \|\| current_record). !… | — |
| [`token_gated_priority_scheduler`](rust/composed-systems/token_gated_priority_scheduler.rs) | composes: enqueue-tasks-with-priorities + token-bucket-gate-admits-at-rate + dispatch-highest-priority-admitted | — |
| [`tokenizer_ast_evaluator`](rust/composed-systems/tokenizer_ast_evaluator.rs) | composes: tokenize-arithmetic + parse-to-ast-with-precedence + evaluate | — |
| [`validated_config_loader`](rust/composed-systems/validated_config_loader.rs) | composes: parse-ini-kv-config + validate-schema-types + checksum-verify + reject-violations | — |
| [`wal_append_replay`](rust/composed-systems/wal_append_replay.rs) | ! wal_append_replay — write-ahead log with CRC-32 framing, crash simulation, and recovery. ! ! Core idea: each record is prefixed with length + followed by CRC32. A crash… | — |
| [`wal_backed_kv_store`](rust/composed-systems/wal_backed_kv_store.rs) | composes: kv-put-del + wal-append + crash-simulate + replay-recover | — |

### concurrency-resilience

| Pattern | Description | Also in |
|---|---|---|
| [`atomic_counter_sharded`](rust/concurrency-resilience/atomic_counter_sharded.rs) | ! atomic_counter_sharded — a sharded atomic counter that stays exact under concurrency. ! ! Core idea: N worker threads each hit one of S shards (an `AtomicU64`) to cut… | — |
| [`atomic_max_tracker`](rust/concurrency-resilience/atomic_max_tracker.rs) | ! atomic_max_tracker — a lock-free running maximum via CAS without locking. ! ! Core idea: an AtomicU64 holds the current maximum. To update, spin-CAS: if the ! new value exceeds… | — |
| [`atomic_refcount`](rust/concurrency-resilience/atomic_refcount.rs) | ! atomic_refcount — a hand-rolled atomic reference count with concurrent clone/drop. ! ! Core idea: an AtomicU64 holds the refcount. Each clone() increments; each drop() !… | — |
| [`atomic_spinlock`](rust/concurrency-resilience/atomic_spinlock.rs) | ! atomic_spinlock — a spinlock built from AtomicBool::compare_exchange. ! ! Core idea: an AtomicBool holds the lock state (false=free, true=locked). To acquire, ! spin via CAS… | — |
| [`barrier_sync`](rust/concurrency-resilience/barrier_sync.rs) | ! barrier_sync — an N-thread barrier ensuring no thread proceeds until all N arrive. ! ! Core idea: N threads call wait(); a counter increments on each arrival. No thread !… | — |
| [`broadcast_fanout`](rust/concurrency-resilience/broadcast_fanout.rs) | ! broadcast_fanout — one producer broadcasts a message to N receivers. ! ! Core idea: a producer publishes a value; N receivers each receive it exactly once ! via a shared Condvar… | — |
| [`cas_stack_arena`](rust/concurrency-resilience/cas_stack_arena.rs) | ! cas_stack_arena — a lock-free stack using atomic head pointer and arena indices. ! ! Core idea: arena stores values; head (AtomicUsize) is the stack top. Each slot ! in the… | — |
| [`circuit_breaker`](rust/concurrency-resilience/circuit_breaker.rs) | ! circuit_breaker — typestate closed/open/half-open enum; transitions asserted. ! ! Core idea: implement the circuit breaker pattern using Rust's typestate pattern to ! ensure… | Go, Python |
| [`concurrent_histogram`](rust/concurrency-resilience/concurrent_histogram.rs) | ! concurrent_histogram — a sharded concurrent histogram with per-bucket atomics. ! ! Core idea: each bucket is an AtomicU64. N threads increment buckets concurrently. ! The merged… | — |
| [`countdown_latch`](rust/concurrency-resilience/countdown_latch.rs) | ! countdown_latch — a latch that releases all waiters only when count reaches zero. ! ! Core idea: a shared counter and Condvar. Tasks decrement the counter via count_down(); !… | — |
| [`deadline_guard`](rust/concurrency-resilience/deadline_guard.rs) | ! deadline_guard — Instant/Duration deadline propagation; child < parent, expiry detected. ! ! Core idea: track deadlines using std::time::Instant + Duration. Child operations… | — |
| [`double_buffer`](rust/concurrency-resilience/double_buffer.rs) | ! double_buffer — atomic front/back buffer swap ensuring readers always see consistent state. ! ! Core idea: two buffers (front and back). A writer updates the back buffer, then !… | — |
| [`exponential_backoff`](rust/concurrency-resilience/exponential_backoff.rs) | ! exponential_backoff — backoff + seeded jitter; bounded, monotone-in-expectation. ! ! Core idea: implement exponential backoff with deterministic seeded jitter. Each retry !… | Go, Python |
| [`future_lite_executor`](rust/concurrency-resilience/future_lite_executor.rs) | ! future_lite_executor — a tiny single-threaded executor for state-machine tasks. ! ! Core idea: a set of tasks, each with a simple state machine (pending/ready/done). ! The… | — |
| [`graceful_shutdown`](rust/concurrency-resilience/graceful_shutdown.rs) | ! graceful_shutdown — Drop-guard/RAII cleanup order; resources released in reverse acquire order. ! ! Core idea: use Rust's Drop trait (RAII) to ensure resources are released in… | — |
| [`mpmc_queue`](rust/concurrency-resilience/mpmc_queue.rs) | ! mpmc_queue — a multi-producer/multi-consumer queue using std::sync::mpsc. ! ! Core idea: multiple producers send items via an mpsc channel; multiple consumers ! share a receiver… | — |
| [`once_init_guard`](rust/concurrency-resilience/once_init_guard.rs) | ! once_init_guard — a one-time initializer that runs exactly once across racing threads. ! ! Core idea: use a CAS loop (or std::sync::Once) to ensure a closure runs exactly once,… | — |
| [`rendezvous_channel`](rust/concurrency-resilience/rendezvous_channel.rs) | ! rendezvous_channel — an unbuffered synchronous handoff channel. ! ! Core idea: a sender send() blocks until a receiver recv() takes the value. ! Zero buffering — the sender and… | — |
| [`retry_with_budget`](rust/concurrency-resilience/retry_with_budget.rs) | ! retry_with_budget — retry budget guard; amplification capped, measured over seeds. ! ! Core idea: retry logic with a fixed budget (max retries, max amplification). Each retry !… | — |
| [`reusable_phaser`](rust/concurrency-resilience/reusable_phaser.rs) | ! reusable_phaser — a reusable multi-phase barrier for N threads across P phases. ! ! Core idea: N threads synchronize at each of P phases. Each phase requires all N to ! arrive… | — |
| [`rwlock_cache`](rust/concurrency-resilience/rwlock_cache.rs) | ! rwlock_cache — a read-through cache guarded by a std `RwLock`, single-fill on miss. ! ! Core idea: many concurrent readers share the read lock; a miss upgrades to the write !… | — |
| [`rwlock_readers`](rust/concurrency-resilience/rwlock_readers.rs) | ! rwlock_readers — multiple readers coexist; writer is exclusive and blocks readers. ! ! Core idea: std::sync::RwLock allows many readers or one writer, never both. ! THE ONE LAW:… | — |
| [`semaphore_limit`](rust/concurrency-resilience/semaphore_limit.rs) | ! semaphore_limit — counting semaphore from Mutex+Condvar; max in-flight never exceeds limit. ! ! Core idea: implement a counting semaphore using std::sync::Mutex + CondVar.… | — |
| [`seqlock_snapshot`](rust/concurrency-resilience/seqlock_snapshot.rs) | ! seqlock_snapshot — a seqlock ensuring readers never observe torn (partial) updates. ! ! Core idea: a sequence number guards reads — there is NO lock on the data itself, so a !… | — |
| [`spsc_ring_buffer`](rust/concurrency-resilience/spsc_ring_buffer.rs) | ! spsc_ring_buffer — a single-producer/single-consumer bounded ring using atomic indices. ! ! Core idea: a fixed-size ring with atomic head (producer) and atomic tail (consumer).… | — |
| [`ticket_lock`](rust/concurrency-resilience/ticket_lock.rs) | ! ticket_lock — a fair ticket lock with atomic next-ticket and now-serving. ! ! Core idea: each thread acquires a ticket (via atomic fetch_add on next-ticket), ! then spins until… | — |
| [`token_bucket`](rust/concurrency-resilience/token_bucket.rs) | ! token_bucket — real token bucket with virtual clock; burst shaped to rate. ! ! Core idea: token bucket rate limiter using a virtual clock. Tokens accumulate over time ! at a… | Python |
| [`wait_group`](rust/concurrency-resilience/wait_group.rs) | ! wait_group — an add/done/wait pattern for coordinating task completion. ! ! Core idea: call add(n) to register N tasks; call done() when a task finishes. ! wait() blocks until… | — |
| [`work_stealing_deque`](rust/concurrency-resilience/work_stealing_deque.rs) | ! work_stealing_deque — a lock-free deque where the owner uses one end, stealers the other. ! ! Core idea: the Chase-Lev work-stealing deque. A single owner thread pushes and pops… | — |
| [`worker_pool_mpsc`](rust/concurrency-resilience/worker_pool_mpsc.rs) | ! worker_pool_mpsc — a fixed thread pool draining jobs off an `mpsc` channel. ! ! Core idea: a set of planted jobs is sent into an mpsc channel; W worker threads share ! the… | — |

### cross-sphere-twins

| Pattern | Description | Also in |
|---|---|---|
| [`count_min_sketch`](rust/cross-sphere-twins/count_min_sketch.rs) | ! count_min_sketch — frequency sketch; OVERESTIMATE-ONLY guarantee. ! ! Core idea: k hash functions, m counters per hash. For a key, increment all k ! counters. Query returns the… | C++, Python |
| [`crdt_gcounter`](rust/cross-sphere-twins/crdt_gcounter.rs) | ! crdt_gcounter — grow-only counter; merge is commutative, idempotent, convergent. ! ! Core idea: each replica has a per-replica counter. Merge combines max of each. ! Merge is… | — |
| [`hyperloglog_lite`](rust/cross-sphere-twins/hyperloglog_lite.rs) | ! hyperloglog_lite — cardinality estimate; relative error within a COMPUTED bound. ! ! Core idea: hash each item to 64 bits; the low P bits pick a register (m = 2^P), the… | — |
| [`leader_lease`](rust/cross-sphere-twins/leader_lease.rs) | ! leader_lease — lease + logical clock; exactly ONE leader, lease expiry triggers re-election. ! ! Core idea: a leader holds a lease (time-limited). Followers check the lease… | — |
| [`lru_cache`](rust/cross-sphere-twins/lru_cache.rs) | ! lru_cache — LRU eviction; exact eviction order vs brute-force reference. ! ! Core idea: cache with fixed size. On insertion when full, evict the least-recently-used. ! THE LAW:… | Python |
| [`lsm_memtable_flush`](rust/cross-sphere-twins/lsm_memtable_flush.rs) | ! lsm_memtable_flush — memtable flushes to immutable sstable; merged read returns newest. ! ! Core idea: an in-memory sorted map (memtable) accumulates writes. When full, it… | — |
| [`misra_gries_topk`](rust/cross-sphere-twins/misra_gries_topk.rs) | ! misra_gries_topk — heavy hitters; GUARANTEE: any freq > n/(k+1) is in output. ! ! Core idea: maintain k candidate items + counters. For new item, if it's a candidate, !… | — |
| [`quorum_write`](rust/cross-sphere-twins/quorum_write.rs) | ! quorum_write — N replicas, majority-ack required; minority partition refuses write. ! ! Core idea: a write succeeds only if a majority of N replicas acknowledge. A minority !… | — |
| [`reservoir_sample`](rust/cross-sphere-twins/reservoir_sample.rs) | ! reservoir_sample — Algorithm R; UNIFORM over the stream, seeded-deterministic. ! ! Core idea: keep a size-k reservoir. The first k items fill it; the i-th item thereafter ! (i =… | — |
| [`skip_list`](rust/cross-sphere-twins/skip_list.rs) | ! skip_list — a real probabilistic skip list (index-arena, safe); levels drive search. ! ! Core idea: each node has a random height; higher levels are "express lanes" that skip… | Python |

### filesystem-process

| Pattern | Description | Also in |
|---|---|---|
| [`atomic_write_rename`](rust/filesystem-process/atomic_write_rename.rs) | ! atomic_write_rename — temp-write+rename atomicity; partial never visible; cleans up. ! ! Core idea: write to a temp file, then rename atomically to the target. This prevents !… | — |
| [`df_capacity_forecast`](rust/filesystem-process/df_capacity_forecast.rs) | ! df_capacity_forecast — linear time-to-full from synthetic df samples; matches trajectory. ! ! Core idea: collect disk usage samples over time, fit a line, forecast when full. !… | — |
| [`dir_size_aggregate`](rust/filesystem-process/dir_size_aggregate.rs) | ! dir_size_aggregate — recursive size sum over a synthetic tree; equals brute force. ! ! Core idea: walk a directory tree and sum file sizes. THE ONE LAW: create a synthetic !… | — |
| [`file_dedup_hash`](rust/filesystem-process/file_dedup_hash.rs) | ! file_dedup_hash — group synthetic file table by content hash; planted dupes grouped. ! ! Core idea: hash file contents, group files by hash, identify duplicates. ! THE ONE LAW:… | — |
| [`lockfile_pid_guard`](rust/filesystem-process/lockfile_pid_guard.rs) | ! lockfile_pid_guard — pidfile stale-lock detection LOGIC on fixtures; stale reclaimed, live respected. ! ! Core idea: a pidfile guards mutual exclusion. Acquisition must RECLAIM… | — |
| [`path_normalize_guard`](rust/filesystem-process/path_normalize_guard.rs) | ! path_normalize_guard — normalize + traversal-escape guard; ../ escapes blocked. ! ! Core idea: normalize paths and prevent directory traversal attacks (e.g., ../../etc). ! THE… | — |
| [`proc_stat_cpu`](rust/filesystem-process/proc_stat_cpu.rs) | ! proc_stat_cpu — parse two /proc/stat fixtures → CPU% delta; matches hand math. ! ! Core idea: parse /proc/stat lines to extract CPU ticks (user, system, etc.), compute ! the… | — |
| [`retention_gfs`](rust/filesystem-process/retention_gfs.rs) | ! retention_gfs — grandfather-father-son retention over a synthetic date set; keeps exactly. ! ! Core idea: keep the most recent snapshot in each period bucket (daily within 7… | — |
| [`rolling_checksum`](rust/filesystem-process/rolling_checksum.rs) | ! rolling_checksum — polynomial rolling checksum for delta sync; O(1) window updates. ! ! Core idea: as the window slides one byte, the hash is updated INCREMENTALLY — subtract… | — |
| [`supervisor_restart`](rust/filesystem-process/supervisor_restart.rs) | ! supervisor_restart — restart backoff state machine; crash loop backs off, stable resets. ! ! Core idea: track restart attempts; increase backoff on consecutive crashes, reset on… | — |

### metrics-scheduling

| Pattern | Description | Also in |
|---|---|---|
| [`consistent_hash_ring`](rust/metrics-scheduling/consistent_hash_ring.rs) | ! consistent_hash_ring — hash ring + vnodes; key moves minimally when a node leaves. ! ! Core idea: consistent hashing distributes keys across nodes. When a node leaves, ! only a… | Go, Python |
| [`cron_next_fire`](rust/metrics-scheduling/cron_next_fire.rs) | ! cron_next_fire — parse simple cron expression; compute next fire time. ! ! Core idea: parse "*/5 * * * *" (every 5 minutes) or similar, then compute the next ! fire time from a… | — |
| [`debounce_throttle`](rust/metrics-scheduling/debounce_throttle.rs) | ! debounce_throttle — event debounce/throttle over virtual clock; emitted set exact. ! ! Core idea: debounce waits for a quiet period before emitting; throttle emits at ! most… | — |
| [`ewma_gauge`](rust/metrics-scheduling/ewma_gauge.rs) | ! ewma_gauge — exponentially weighted moving average with hysteresis alert. ! ! Core idea: EWMA smooths noisy samples; hysteresis prevents alert flapping when ! the signal hovers… | — |
| [`hdr_latency_lite`](rust/metrics-scheduling/hdr_latency_lite.rs) | ! hdr_latency_lite — HDR-style latency histogram; percentiles within a BOUNDED relative error. ! ! Core idea: a High-Dynamic-Range histogram keeps `SUB` linear sub-buckets inside… | — |
| [`histogram_quantile`](rust/metrics-scheduling/histogram_quantile.rs) | ! histogram_quantile — bucketed histogram; quantile within tolerance of exact. ! ! Core idea: log-scale buckets hold sample counts; approximate quantile is computed ! by scanning… | — |
| [`priority_scheduler`](rust/metrics-scheduling/priority_scheduler.rs) | ! priority_scheduler — BinaryHeap job scheduler with fairness. ! ! Core idea: jobs with priority are scheduled; higher priority jobs run first. ! Fairness is maintained by aging:… | — |
| [`rate_counter`](rust/metrics-scheduling/rate_counter.rs) | ! rate_counter — reset-safe counter rate; planted resets not read as spikes. ! ! Core idea: track event count and compute rate per time unit. When the counter ! resets, the rate… | — |
| [`ring_buffer`](rust/metrics-scheduling/ring_buffer.rs) | ! ring_buffer — fixed-capacity ring buffer; windowed stats (sum/mean) match brute force. ! ! Core idea: ring buffer holds the last N samples in a circular buffer; sum and mean !… | — |
| [`topo_job_order`](rust/metrics-scheduling/topo_job_order.rs) | ! topo_job_order — Kahn topological sort of a job DAG; planted deps respected, cycles detected. ! ! Core idea: jobs have dependencies forming a DAG. Topological sort computes an… | — |

### networking-resilience

| Pattern | Description | Also in |
|---|---|---|
| [`backpressure_bounded_queue`](rust/networking-resilience/backpressure_bounded_queue.rs) | Bounded FIFO queue that emits a backpressure signal (Go/Stop) with hysteresis. Push flips to Stop once length reaches the high watermark; pop only flips back to Go once length… | — |
| [`bulkhead_isolation_limiter`](rust/networking-resilience/bulkhead_isolation_limiter.rs) | Bulkhead concurrency limiter: caps simultaneous in-flight work at max_concurrent. try_acquire admits a caller and increments the count only while below the cap, returning false… | — |
| [`cidr_allowlist_match`](rust/networking-resilience/cidr_allowlist_match.rs) | CIDR allow/deny matcher using longest-prefix-match on IPv4 addresses (u32). Each rule carries a network, prefix length, and an allow flag; matches() masks the query against every… | — |
| [`connection_pool_manager`](rust/networking-resilience/connection_pool_manager.rs) | Connection pool with a max size and idle-timeout eviction, driven by an explicit clock (`now`). try_acquire first evicts connections whose idle age has reached the timeout, then… | — |
| [`count_min_sketch_ip_freq`](rust/networking-resilience/count_min_sketch_ip_freq.rs) | Count-Min Sketch: a fixed-memory probabilistic frequency counter (here keyed by IP as u32). increment hashes an item through `depth` rows into `width` buckets and bumps each… | — |
| [`dns_name_wire_parser`](rust/networking-resilience/dns_name_wire_parser.rs) | Parser for DNS wire-format names: length-prefixed labels joined by dots, with support for compression pointers (leading 0xC0 bits). Use when decoding untrusted DNS packets, where… | — |
| [`ewma_latency_tracker`](rust/networking-resilience/ewma_latency_tracker.rs) | Integer-only EWMA latency tracker with a companion EWMV (mean-absolute-deviation) estimate. The first sample seeds the mean; each later sample nudges the mean and deviation by… | — |
| [`failover_priority_list`](rust/networking-resilience/failover_priority_list.rs) | Priority-ordered failover selector: nodes are held in fixed preference order and select() returns the id of the first one still marked healthy. mark_healthy / mark_unhealthy… | — |
| [`gcra_rate_limiter`](rust/networking-resilience/gcra_rate_limiter.rs) | GCRA: Generic Cell Rate Algorithm (virtual scheduling). Two parameters make it a real GCRA rather than a bare min-interval limiter: T = emission interval (time units per cell) —… | — |
| [`hedged_request_scheduler`](rust/networking-resilience/hedged_request_scheduler.rs) | Deterministic timing model for a hedged request: fire a primary now, and if it hasn't returned by hedge_delay, fire a backup. Given fixed primary/backup latencies it computes… | — |
| [`http_status_retry_classifier`](rust/networking-resilience/http_status_retry_classifier.rs) | Maps an HTTP status code to a retry decision: Ok, Retry (immediate), RetryAfter (back off / honor Retry-After), or Fatal (don't retry). 2xx/3xx are Ok; 408 and 500 are Retry;… | — |
| [`least_connections_lb`](rust/networking-resilience/least_connections_lb.rs) | Least-connections load balancer over N backends, each tracking an in-flight count. acquire picks the backend with the fewest in-flight requests (lowest index wins ties) and… | — |
| [`port_scan_detector`](rust/networking-resilience/port_scan_detector.rs) | Sliding-window port-scan detector: per source IP it keeps recent (port, timestamp) events, drops those older than window_seconds, and flags the source once the number of DISTINCT… | — |
| [`rendezvous_hash_hrw`](rust/networking-resilience/rendezvous_hash_hrw.rs) | Seeded LCG for deterministic hashing Rendezvous (Highest-Random-Weight) hashing: to place a key, score it against every node with a seeded LCG hash of (key, node_id, seed) and… | — |
| [`retry_after_header_parser`](rust/networking-resilience/retry_after_header_parser.rs) | Retry-After (RFC 7231 §7.1.3): either delta-seconds (an integer) OR an HTTP-date (IMF-fixdate, e.g. "Mon, 01 Jan 2024 00:00:00 GMT"). Both resolve to "seconds to wait" relative to… | — |
| [`sliding_window_flow_control`](rust/networking-resilience/sliding_window_flow_control.rs) | Sliding-window flow control that caps outstanding (in-flight) bytes at a fixed window. try_send admits a send only when in_flight + bytes <= window_size, adding to the count; ack… | — |
| [`sliding_window_rate_limiter`](rust/networking-resilience/sliding_window_rate_limiter.rs) | Sliding-window rate limiter keyed on caller-supplied timestamps (no wall clock). allow(now) first evicts every recorded event with ts <= now - window_seconds, then admits (and… | — |
| [`tcp_rto_estimator`](rust/networking-resilience/tcp_rto_estimator.rs) | TCP retransmission-timeout estimator via the Jacobson/Karels algorithm in integer arithmetic. First sample seeds srtt = sample and rttvar = sample/2; later samples update rttvar =… | — |
| [`url_authority_parser`](rust/networking-resilience/url_authority_parser.rs) | Parser for a URL authority component into userinfo / host / port. Splits userinfo at the first '@', then splits host from port at the LAST ':' (so a colon in userinfo does not… | — |
| [`weighted_round_robin_lb`](rust/networking-resilience/weighted_round_robin_lb.rs) | Weighted round-robin load balancer built on a precomputed schedule. The constructor expands each (backend_id, weight) into `weight` copies in a flat schedule; select() walks that… | — |

### parsing-protocols

| Pattern | Description | Also in |
|---|---|---|
| [`ansi_escape_stripper`](rust/parsing-protocols/ansi_escape_stripper.rs) | Strips ANSI terminal escape sequences from text, keeping only the printable content. Scans char by char: on ESC '[' it drops a CSI sequence up to and including the final letter… | — |
| [`backslash_escape_codec`](rust/parsing-protocols/backslash_escape_codec.rs) | Backslash escape codec that turns an arbitrary byte slice into a printable ASCII string and back. encode maps \\, \n, \r, \t, \0 to named escapes, passes bytes 32..=126 through… | — |
| [`balanced_delimiter_check`](rust/parsing-protocols/balanced_delimiter_check.rs) | Stack-based checker for balanced (), [], {} that is string-aware. It pushes openers and matches closers against the stack top, but while inside a double-quoted string it ignores… | — |
| [`byte_unit_parse`](rust/parsing-protocols/byte_unit_parse.rs) | ! byte_unit_parse — "512Mi"/"1.5G" → bytes and back; round-trip + ordering. ! ! Core idea: parse byte-unit strings (B, KiB, MiB, GiB, TiB) to u64 bytes and back to ! string. THE… | — |
| [`chunked_transfer_decoder`](rust/parsing-protocols/chunked_transfer_decoder.rs) | Decoder for HTTP/1.1-style chunked transfer encoding (line-oriented variant). Reads a hex chunk-size line, then a data line, appends it, and repeats until a size of 0 terminates… | — |
| [`cidr_ip_math`](rust/parsing-protocols/cidr_ip_math.rs) | ! cidr_ip_math — IPv4 parse, CIDR contains, subnet split. ! ! Core idea: parse IPv4 addresses and CIDR blocks, check containment, split subnets in half. ! THE ONE LAW: plant known… | — |
| [`cli_args_parser`](rust/parsing-protocols/cli_args_parser.rs) | ! cli_args_parser — from-scratch getopt: short/long flags, =values, -- boundary. ! ! Core idea: parse command-line arguments from scratch, handling short/long flags, values, ! and… | — |
| [`cobs_framing`](rust/parsing-protocols/cobs_framing.rs) | Consistent Overhead Byte Stuffing (COBS) encoder/decoder for zero-free framing. encode replaces zero bytes with a code-byte scheme so the output contains no 0x00 (letting a… | — |
| [`crc_framed_packet`](rust/parsing-protocols/crc_framed_packet.rs) | CRC-32-protected packet framing (standard reflected CRC-32, poly 0xEDB88320, table built at compile time via a const fn). Packet::new computes the CRC over header+payload;… | — |
| [`csv_quote_escape`](rust/parsing-protocols/csv_quote_escape.rs) | RFC-4180-style parser for a single CSV line with quoted-field support. Tracks an in-quotes flag: a field may open with '"', commas inside quotes are literal, and a doubled ""… | — |
| [`csv_reader_typed`](rust/parsing-protocols/csv_reader_typed.rs) | ! csv_reader_typed — quoted-field CSV split + type inference; matches planted rows. ! ! Core idea: parse CSV with proper quote handling, split into rows, infer field types ! (int,… | — |
| [`duration_parse`](rust/parsing-protocols/duration_parse.rs) | ! duration_parse — "1h30m"/"250ms" → total; round-trip + arithmetic. ! ! Core idea: parse duration strings (1h, 30m, 250ms, etc.) to total milliseconds, ! serialize back, and… | — |
| [`glob_match`](rust/parsing-protocols/glob_match.rs) | ! glob_match — from-scratch * ? [..] matcher; planted matches/non-matches correct. ! ! Core idea: implement glob pattern matching with *, ?, and character classes [abc] / [^abc].… | — |
| [`handshake_typestate_fsm`](rust/parsing-protocols/handshake_typestate_fsm.rs) | Typestate markers Typestate FSM encoding a connection handshake (Init -> Hello -> Auth -> Ready) in the type system. Each state is a zero-sized marker used as Handshake<State>'s… | — |
| [`http_header_parse`](rust/parsing-protocols/http_header_parse.rs) | ! http_header_parse — header block parse + case-insensitive lookup; folding handled. ! ! Core idea: parse HTTP header lines, store them, and allow case-insensitive lookup. !… | — |
| [`http_request_line_parser`](rust/parsing-protocols/http_request_line_parser.rs) | Parses an HTTP/1.x request line into (method, path, version) and header lines into (name, value) pairs, splitting on the first colon and trimming whitespace. Use when hand-rolling… | — |
| [`ini_config_parser`](rust/parsing-protocols/ini_config_parser.rs) | ! ini_config_parser — sections/keys/comments; round-trips a planted config. ! ! Core idea: parse INI format (sections, keys/values, comments), store it, and serialize ! back to… | — |
| [`json_string_unescape`](rust/parsing-protocols/json_string_unescape.rs) | Unescapes the body of a JSON string, expanding the backslash escapes (\n \t \r \\ \" \b \f \/) and \uXXXX four-hex-digit codepoints into their real characters. Use when decoding a… | — |
| [`key_value_line_scanner`](rust/parsing-protocols/key_value_line_scanner.rs) | Scans a single line of whitespace-separated key=value pairs into a HashMap, where a value may be bare (ends at the next space/tab) or double-quoted to contain spaces, with… | — |
| [`log_line_parser`](rust/parsing-protocols/log_line_parser.rs) | ! log_line_parser — zero-copy syslog parse via byte scan. ! ! Core idea: scan a line of bytes once to extract timestamp, hostname, service, and ! message without allocation. THE… | — |
| [`query_string_parser`](rust/parsing-protocols/query_string_parser.rs) | Parses a URL query string into ordered (key, value) pairs, splitting on '&' then '=', and percent-decoding both sides: %XX becomes the byte's char and '+' becomes a space. Use… | — |
| [`shell_word_split`](rust/parsing-protocols/shell_word_split.rs) | Splits a command line into argument words with shell-like quoting: single quotes take text verbatim, double quotes group text while allowing a leading backslash escape, and an… | — |
| [`slip_escape_framer`](rust/parsing-protocols/slip_escape_framer.rs) | SLIP (RFC 1055) framer: encode() wraps a byte payload in END (0xC0) markers and escapes any END or ESC byte in the data as ESC+ESC_END / ESC+ESC_ESC; decode() reverses it. Use to… | — |
| [`state_machine_tokenizer`](rust/parsing-protocols/state_machine_tokenizer.rs) | A single-pass character-class tokenizer that scans source text into a Token stream: runs of digits become Number, an alpha/underscore start followed by alnum/underscore becomes… | — |
| [`tlv_parser`](rust/parsing-protocols/tlv_parser.rs) | Parses a byte buffer of consecutive Type-Length-Value records, each a 1-byte type, a 1-byte length, then that many value bytes, into a Vec of (type, value) records. Use to decode… | — |
| [`url_parse`](rust/parsing-protocols/url_parse.rs) | ! url_parse — scheme/host/port/path/query split; planted URLs decomposed. ! ! Core idea: parse a URL into components without regex or external parsing. THE ONE LAW: ! plant a set… | — |

### security-crypto

| Pattern | Description | Also in |
|---|---|---|
| [`base32_codec`](rust/security-crypto/base32_codec.rs) | ! Base32 codec (RFC 4648) — encode/decode binary to case-insensitive ASCII. ! Core idea: 5-bit groups mapped to 32-char alphabet, padding on remainder. ! When to use:… | — |
| [`base64_codec`](rust/security-crypto/base64_codec.rs) | ! Base64 codec (RFC 4648) — encode/decode binary to ASCII-safe text. ! Core idea: 6-bit groups mapped to 64-char alphabet, padding on remainder. ! When to use: data transmission,… | — |
| [`bloom_filter`](rust/security-crypto/bloom_filter.rs) | ! Bloom filter — probabilistic set membership (zero false negatives). ! Core idea: k hash functions, bitset, tunable FP rate. ! When to use: IP reputation, URL blacklists,… | Go, Python |
| [`capability_bitset`](rust/security-crypto/capability_bitset.rs) | ! Capability bitset — permission flags via bit operations. ! Core idea: grant/revoke/has via AND/OR/XOR, union/intersect checks. ! When to use: ACLs, role-based access, feature… | — |
| [`constant_time_eq`](rust/security-crypto/constant_time_eq.rs) | ! Constant-time equality (timing-attack resistance) — compare all bytes, always. ! Core idea: OR all byte differences; never early-return on first mismatch, so the WORK ! done is… | — |
| [`crc32`](rust/security-crypto/crc32.rs) | ! CRC-32/IEEE (Ethernet) — error detection via polynomial division. ! Core idea: bit-wise XOR division by Ethernet polynomial 0x04c11db7. ! When to use: data checksums, packet… | — |
| [`csrf_double_submit`](rust/security-crypto/csrf_double_submit.rs) | ! CSRF double-submit check — cookie token must equal form token AND both be present. ! Core idea: a state-changing request is accepted only if the token in the cookie matches !… | — |
| [`hex_codec`](rust/security-crypto/hex_codec.rs) | ! Hex codec (RFC 4648 lowercase) — encode/decode binary to hex text. ! Core idea: each byte is two hex digits (0-9a-f). ! When to use: digest display, data dumps, debug output. | — |
| [`hmac_sha256`](rust/security-crypto/hmac_sha256.rs) | ! HMAC-SHA256 (RFC 2104/4231) — message authentication code from scratch. ! Core idea: two hash calls with key, inner/outer padding constants. ! When to use: API authentication,… | — |
| [`hmac_signed_url`](rust/security-crypto/hmac_signed_url.rs) | ! HMAC-signed URLs — tamper-proof query parameters. ! Core idea: canonicalize params, HMAC sign, verify all params + sig. ! When to use: signed download links, form submissions,… | — |
| [`hotp`](rust/security-crypto/hotp.rs) | ! HOTP (HMAC-based One-Time Password, RFC 4226) — time-independent OTP. ! Core idea: HMAC counter mode, dynamic truncation to 6-8 digit code. ! When to use: multi-factor… | — |
| [`jwt_hs256_verify`](rust/security-crypto/jwt_hs256_verify.rs) | ! JWT (HMAC-SHA256) verification — header.payload.sig integrity check. ! Core idea: base64url decode, verify HMAC, check expiry claim. ! When to use: API tokens, session claims,… | — |
| [`leaky_bucket_shaper`](rust/security-crypto/leaky_bucket_shaper.rs) | ! Leaky-bucket rate shaper — a level that FILLS on admit and LEAKS at a constant rate. ! Core idea: unlike a token bucket (tokens accrue, bursts allowed to capacity), a leaky !… | — |
| [`nonce_replay_guard`](rust/security-crypto/nonce_replay_guard.rs) | ! Nonce replay guard — detect replayed one-time values. ! Core idea: monotonic counter, set membership, sliding window. ! When to use: CSRF tokens, API request IDs, sequence… | — |
| [`otp_lockout`](rust/security-crypto/otp_lockout.rs) | ! OTP lockout — N failed attempts triggers account lock (time-gated). ! Core idea: counter resets on success, lock window enforced. ! When to use: brute-force protection, TOTP/SMS… | — |
| [`password_hash_verify`](rust/security-crypto/password_hash_verify.rs) | ! Password hash verification (PBKDF2-salted) — constant-time comparison. ! Core idea: unique salt per password, verify via timing-safe compare. ! When to use: login systems,… | — |
| [`pbkdf2_sha256`](rust/security-crypto/pbkdf2_sha256.rs) | ! PBKDF2-SHA256 (RFC 2898/7914) — key derivation from password. ! Core idea: iterative HMAC to slow down brute force attacks. ! When to use: password hashing, key stretching, file… | — |
| [`session_token_expiry`](rust/security-crypto/session_token_expiry.rs) | ! Session token expiry — virtual-clock based lifecycle. ! Core idea: issue timestamp, validate expiry window, revocation. ! When to use: OAuth tokens, session cookies, temporary… | — |
| [`sha256`](rust/security-crypto/sha256.rs) | ! SHA-256 (FIPS 180-4) — cryptographic hash from scratch. ! Core idea: message schedule, 64 rounds, Merkle-Damgård structure. ! When to use: cryptographic digest, HMAC, PKI… | — |
| [`totp`](rust/security-crypto/totp.rs) | ! TOTP (Time-based OTP, RFC 6238) — time-synchronized one-time passwords. ! Core idea: HOTP with time window (30s intervals), SHA1 truncation. ! When to use: authenticator apps,… | — |

### storage-persistence

| Pattern | Description | Also in |
|---|---|---|
| [`arc_adaptive_cache`](rust/storage-persistence/arc_adaptive_cache.rs) | ARC (Megiddo & Modha) — a REAL adaptive replacement cache, not a two-queue lookalike. The defining feature is the target `p` that adapts between recency (T1) and frequency (T2)… | — |
| [`bitmap_free_space_manager`](rust/storage-persistence/bitmap_free_space_manager.rs) | A fixed-capacity block allocator backed by a bool bitmap: allocate() returns the lowest free index (first-fit) and marks it used, free(addr) releases it, and a running free_count… | — |
| [`btree_node_split`](rust/storage-persistence/btree_node_split.rs) | Insert-with-split for a single B-tree node: keys are kept sorted on insert, and when a node exceeds max_keys it splits at the median, returning (median_key, right_node) so the… | — |
| [`checkpoint_truncate_log`](rust/storage-persistence/checkpoint_truncate_log.rs) | Models write-ahead-log checkpointing: a checkpoint captures a full state snapshot at an LSN, after which every log record with lsn <= checkpoint.lsn can be truncated away, and… | — |
| [`clock_second_chance_cache`](rust/storage-persistence/clock_second_chance_cache.rs) | CLOCK (second-chance) page cache: each entry carries a reference bit; a hit sets the bit, and on a miss into a full cache a rotating hand clears set bits (granting a second… | — |
| [`copy_on_write_btree`](rust/storage-persistence/copy_on_write_btree.rs) | Copy-on-write tree with STRUCTURAL SHARING — the point of COW, not eager whole-tree cloning. An update copies ONLY the nodes on the path from the root to the changed key; every… | — |
| [`crash_safe_atomic_write`](rust/storage-persistence/crash_safe_atomic_write.rs) | Demonstrates the write-temp-then-rename pattern for durable file updates, modeling the filesystem as a name->contents map and injecting a crash at each critical point. The new… | — |
| [`double_write_buffer`](rust/storage-persistence/double_write_buffer.rs) | Double-write buffer for torn-page protection. Each page is written first to a side buffer, then to its home location; on recovery the buffer holds a whole copy. Use it when a page… | — |
| [`extendible_hash_index`](rust/storage-persistence/extendible_hash_index.rs) | Real extendible hashing: a directory of 2^global_depth pointers into buckets, each bucket carrying its OWN local_depth. On overflow only the ONE overflowing bucket splits; the… | — |
| [`free_list_coalescing_allocator`](rust/storage-persistence/free_list_coalescing_allocator.rs) | Free-list allocator with adjacent-block coalescing. allocate() first-fits a block and splits off the remainder; free() returns a block and immediately merges it with any… | — |
| [`fsync_barrier_ordering`](rust/storage-persistence/fsync_barrier_ordering.rs) | fsync barrier / durable-LSN ordering. Log records carry increasing LSNs; a barrier advances a durable_lsn watermark, marking every record up to it as persisted. Use it to reason… | — |
| [`log_segment_gc_compaction`](rust/storage-persistence/log_segment_gc_compaction.rs) | Log-segment GC / compaction for an append-only Insert/Update/Delete log. Replays the log to derive the live set (latest value per key, deletes removed), then rewrites a compacted… | — |
| [`manifest_versioned_snapshot`](rust/storage-persistence/manifest_versioned_snapshot.rs) | Versioned manifest with atomic snapshot swap. The active manifest (version + file set) is replaced by installing a whole new one; a reader that captured an earlier manifest keeps… | — |
| [`mvcc_version_chain`](rust/storage-persistence/mvcc_version_chain.rs) | MVCC version chain. Each key holds an ordered chain of (commit_ts, value) versions; a read at snapshot timestamp T resolves to the newest version with commit_ts <= T. Use it for… | — |
| [`redo_undo_log`](rust/storage-persistence/redo_undo_log.rs) | ARIES-style redo/undo recovery over a Begin/Update/Commit log where Update records carry both old and new values. Recovery runs REDO forward (reapply committed updates) then UNDO… | — |
| [`slotted_page_layout`](rust/storage-persistence/slotted_page_layout.rs) | Slotted-page record layout. A page holds variable-length records plus a slot directory of (offset, length) entries; insert appends a record and a slot, delete clears the slot… | — |
| [`sstable_block_index`](rust/storage-persistence/sstable_block_index.rs) | SSTable sparse block index. Stores one (first_key, block_offset) boundary per block over a sorted key space; find_block(key) returns the rightmost block whose first_key <= key.… | — |
| [`tombstone_deletion_merge`](rust/storage-persistence/tombstone_deletion_merge.rs) | Tombstone-based deletion for LSM/SSTable merges. A delete writes a Tombstone marker rather than removing data; during a merge the newer level wins, so a tombstone masks an older… | — |
| [`two_phase_commit_coordinator`](rust/storage-persistence/two_phase_commit_coordinator.rs) | Two-phase commit as an explicit coordinator + participant FSM (Working/Prepared/ Committed/Aborted), not a boolean AND. Phase 1: each participant votes; a YES-voter durably… | — |
| [`wal_group_commit`](rust/storage-persistence/wal_group_commit.rs) | WAL group commit. Multiple transactions append records to the log, then one fsync advances a synced_lsn watermark to the highest batched LSN, persisting the whole group at once.… | — |

### systems-math-encoding

| Pattern | Description | Also in |
|---|---|---|
| [`adler32`](rust/systems-math-encoding/adler32.rs) | ! Adler-32 checksum: sum of all bytes (mod 65521) + sum of running sum (mod 65521). ! Core idea: two 16-bit checksums interleaved; fast for small data. ! When to use: zlib… | — |
| [`base58_codec`](rust/systems-math-encoding/base58_codec.rs) | ! Base58 codec (Bitcoin alphabet): encode/decode arbitrary-length bytes. ! Core idea: treat the byte string as a big-endian base-256 number and re-base it to 58 by ! processing… | — |
| [`bit_reader_writer`](rust/systems-math-encoding/bit_reader_writer.rs) | ! Bit-level reader/writer: pack arbitrary-width bit fields and read them back exactly. ! Core idea: maintain bit position in a byte buffer; write/read N bits at cursor. ! When to… | — |
| [`crc16_ccitt`](rust/systems-math-encoding/crc16_ccitt.rs) | ! CRC-16/CCITT-FALSE checksum (polynomial 0x1021, initial value 0xFFFF). ! Core idea: process each bit, XOR with polynomial when MSB is 1. ! When to use: serial communication,… | — |
| [`crc32c_castagnoli`](rust/systems-math-encoding/crc32c_castagnoli.rs) | ! CRC-32/Castagnoli (CRC-32C): polynomial 0x1EDC6F41, used in iSCSI and others. ! Core idea: 32-bit shift register with Castagnoli polynomial; process 8 bits per byte. ! When to… | — |
| [`delta_zigzag_encode`](rust/systems-math-encoding/delta_zigzag_encode.rs) | ! Delta-encoding + zigzag: compress sequences with small deltas. ! Core idea: store first value, then encode (value[i] - value[i-1]) as zigzag varints. ! When to use: time series,… | — |
| [`dynamic_bitset`](rust/systems-math-encoding/dynamic_bitset.rs) | ! Dynamic bitset: set/clear/test bits with and/or/xor operations. ! Core idea: Vec<u8> backing store, 8 bits per byte; operations match Vec<bool> exactly. ! When to use: sparse… | — |
| [`fletcher16`](rust/systems-math-encoding/fletcher16.rs) | ! Fletcher-16 checksum: two running sums reduced modulo 255 (NOT 256). ! Core idea: s1 = Σ bytes mod 255; s2 = Σ s1 mod 255; result = (s2 << 8) \| s1. The mod-255 !… | — |
| [`gcd_fraction_reduce`](rust/systems-math-encoding/gcd_fraction_reduce.rs) | ! GCD-based fraction reduction: simplify fractions to lowest terms. ! Core idea: GCD divides both numerator and denominator evenly; quotients are coprime. ! When to use: rational… | — |
| [`gray_code`](rust/systems-math-encoding/gray_code.rs) | ! Gray code (reflected binary): binary↔Gray conversion where consecutive values differ in exactly 1 bit. ! Core idea: Gray(n) = n ^ (n >> 1); inverse via iterative XOR shifting. !… | — |
| [`hamming_distance`](rust/systems-math-encoding/hamming_distance.rs) | ! Hamming distance: bit-difference count between byte sequences. ! Core idea: XOR the bytes and count set bits in result. ! When to use: error detection in transmission, code… | — |
| [`length_prefixed_framing`](rust/systems-math-encoding/length_prefixed_framing.rs) | ! Length-prefixed framing: u32 big-endian length prefix + message bytes. ! Core idea: each message preceded by 4-byte big-endian length; streams are parsed sequentially. ! When to… | — |
| [`luhn_checksum`](rust/systems-math-encoding/luhn_checksum.rs) | ! Luhn checksum (mod-10 algorithm): validates credit card and similar numbers. ! Core idea: double every second digit from right, sum digits, valid if sum % 10 == 0. ! When to… | — |
| [`modexp`](rust/systems-math-encoding/modexp.rs) | ! Fast modular exponentiation: compute (base^exp) mod m efficiently. ! Core idea: binary exponentiation, squaring and multiplying modulo m. ! When to use: cryptography, number… | — |
| [`popcount_bits`](rust/systems-math-encoding/popcount_bits.rs) | ! Bit population count (Hamming weight) and bit operations from scratch. ! Core idea: count set bits in an integer; also provide ctz (trailing zeros) and clz (leading zeros). !… | — |
| [`reverse_bits`](rust/systems-math-encoding/reverse_bits.rs) | ! Reverse bit order in an integer. ! Core idea: swap bits from outside-in; double reverse is identity. ! When to use: bitstream reversal, certain signal processing, DSP algorithms. | — |
| [`roman_numeral`](rust/systems-math-encoding/roman_numeral.rs) | ! Roman numeral codec: integer ↔ Roman numeral (range 1..=3999). ! Core idea: subtractive notation (IV=4, IX=9, XL=40, XC=90, CD=400, CM=900). ! When to use: numeral display,… | — |
| [`run_length_encode`](rust/systems-math-encoding/run_length_encode.rs) | ! Run-length encoding: compress sequences of identical bytes. ! Core idea: emit (run_byte, count) pairs; single byte encoded as (byte, 1). ! When to use: simple compression, image… | — |
| [`varint_leb128`](rust/systems-math-encoding/varint_leb128.rs) | ! Unsigned LEB128 (Little-Endian Base-128) varint encoding. ! Core idea: 7 bits per byte, MSB continuation flag; 0–127 fit in 1 byte, larger requires chaining. ! When to use:… | — |
| [`zigzag_signed`](rust/systems-math-encoding/zigzag_signed.rs) | ! Zigzag encoding for signed integers (maps signed to unsigned for efficient varint). ! Core idea: alternating sign to adjacent values: 0→0, -1→1, 1→2, -2→3, -3→5, 3→6. ! When to… | — |

