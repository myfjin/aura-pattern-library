# Part B — Illia's hands-on abuse session: 15 candidates

For each: the function to attack, its declared inputs, and garbage ideas per his rule (wrong numbers · letters-for-numbers · wrong-language strings). Three-way verdict: errors ✅ · handled-per-contract ✅ · silent-wrong ❌ INVALID.

## `python/data-science/statistical_modeling/power_analysis_sample_size.py`
- attack function: `normal_quantile(p: float)`
- garbage ideas: numbers→ -1, 0, 1e18, float('nan'); letters→ 'abc' where a number belongs; language→ 'сорок два', '四十二'; empty→ [], ''
- run card: `python3 utility_score.py ~/aura-pattern-library/python/data-science/statistical_modeling/power_analysis_sample_size.py --abuse`

## `python/data-science/ensembles_and_robust_methods/stacking_ensemble.py`
- attack function: `fit_linear_model(X_base: List[List[float]], y: List[float])`
- garbage ideas: numbers→ -1, 0, 1e18, float('nan'); letters→ 'abc' where a number belongs; language→ 'сорок два', '四十二'; empty→ [], ''
- run card: `python3 utility_score.py ~/aura-pattern-library/python/data-science/ensembles_and_robust_methods/stacking_ensemble.py --abuse`

## `python/data-science/ensembles_and_robust_methods/gradient_boosting_stumps.py`
- attack function: `gini_split(y: List[float])`
- garbage ideas: numbers→ -1, 0, 1e18, float('nan'); letters→ 'abc' where a number belongs; language→ 'сорок два', '四十二'; empty→ [], ''
- run card: `python3 utility_score.py ~/aura-pattern-library/python/data-science/ensembles_and_robust_methods/gradient_boosting_stumps.py --abuse`

## `python/data-science/bayesian_iii_approximate_inference/bayes_factor_normal_means.py`
- attack function: `bayes_factor_normal(data: ?, prior_var_h1: ?)`
- garbage ideas: numbers→ -1, 0, 1e18, float('nan'); letters→ 'abc' where a number belongs; language→ 'сорок два', '四十二'; empty→ [], ''
- run card: `python3 utility_score.py ~/aura-pattern-library/python/data-science/bayesian_iii_approximate_inference/bayes_factor_normal_means.py --abuse`

## `python/data-science/recommenders_and_graph_sampling/bayesian_ab_beta.py`
- attack function: `bayesian_ab_test(successes_a: int, trials_a: int, successes_b: int, trials_b: int, prior_alpha: float, prior_beta: float, num_samples: int)`
- garbage ideas: numbers→ -1, 0, 1e18, float('nan'); letters→ 'abc' where a number belongs; language→ 'сорок два', '四十二'; empty→ [], ''
- run card: `python3 utility_score.py ~/aura-pattern-library/python/data-science/recommenders_and_graph_sampling/bayesian_ab_beta.py --abuse`

## `python/data-science/bayesian_iii_modeling_and_selection/dirichlet_stick_breaking.py`
- attack function: `stick_breaking_process(alpha: float, num_breaks: int)`
- garbage ideas: numbers→ -1, 0, 1e18, float('nan'); letters→ 'abc' where a number belongs; language→ 'сорок два', '四十二'; empty→ [], ''
- run card: `python3 utility_score.py ~/aura-pattern-library/python/data-science/bayesian_iii_modeling_and_selection/dirichlet_stick_breaking.py --abuse`

## `python/data-science/composed_tools/walk_forward_early_stopping.py`
- attack function: `fit_stump_to_residuals(X: List[List[float]], r: List[float])`
- garbage ideas: numbers→ -1, 0, 1e18, float('nan'); letters→ 'abc' where a number belongs; language→ 'сорок два', '四十二'; empty→ [], ''
- run card: `python3 utility_score.py ~/aura-pattern-library/python/data-science/composed_tools/walk_forward_early_stopping.py --abuse`

## `python/data-science/composed_tools/dedup_pipeline.py`
- attack function: `shingles(text: str, k: int)`
- garbage ideas: numbers→ -1, 0, 1e18, float('nan'); letters→ 'abc' where a number belongs; language→ 'сорок два', '四十二'; empty→ [], ''
- run card: `python3 utility_score.py ~/aura-pattern-library/python/data-science/composed_tools/dedup_pipeline.py --abuse`

## `python/data-science/model_understanding_and_tuning/partial_dependence_data.py`
- attack function: `train_linear_model(X: List[List[float]], y: List[float])`
- garbage ideas: numbers→ -1, 0, 1e18, float('nan'); letters→ 'abc' where a number belongs; language→ 'сорок два', '四十二'; empty→ [], ''
- run card: `python3 utility_score.py ~/aura-pattern-library/python/data-science/model_understanding_and_tuning/partial_dependence_data.py --abuse`

## `python/data-science/signal_processing_and_sequences/savitzky_golay_lite.py`
- attack function: `fit_polynomial_window(window: List[float], poly_order: int)`
- garbage ideas: numbers→ -1, 0, 1e18, float('nan'); letters→ 'abc' where a number belongs; language→ 'сорок два', '四十二'; empty→ [], ''
- run card: `python3 utility_score.py ~/aura-pattern-library/python/data-science/signal_processing_and_sequences/savitzky_golay_lite.py --abuse`

## `python/data-science/streaming_and_sketches/online_sgd_classifier.py`
- attack function: `logistic(z: float)`
- garbage ideas: numbers→ -1, 0, 1e18, float('nan'); letters→ 'abc' where a number belongs; language→ 'сорок два', '四十二'; empty→ [], ''
- run card: `python3 utility_score.py ~/aura-pattern-library/python/data-science/streaming_and_sketches/online_sgd_classifier.py --abuse`

## `python/data-science/model_diagnostics/learning_curve.py`
- attack function: `generate_linear_data(n: int, seed: int)`
- garbage ideas: numbers→ -1, 0, 1e18, float('nan'); letters→ 'abc' where a number belongs; language→ 'сорок два', '四十二'; empty→ [], ''
- run card: `python3 utility_score.py ~/aura-pattern-library/python/data-science/model_diagnostics/learning_curve.py --abuse`

## `python/data-science/information_theory_and_probability/inverse_transform_sampling.py`
- attack function: `exponential_inverse_cdf(u: float, rate: float)`
- garbage ideas: numbers→ -1, 0, 1e18, float('nan'); letters→ 'abc' where a number belongs; language→ 'сорок два', '四十二'; empty→ [], ''
- run card: `python3 utility_score.py ~/aura-pattern-library/python/data-science/information_theory_and_probability/inverse_transform_sampling.py --abuse`

## `python/data-science/experiments_ii/cluster_randomized_icc.py`
- attack function: `_var(z: List[float])`
- garbage ideas: numbers→ -1, 0, 1e18, float('nan'); letters→ 'abc' where a number belongs; language→ 'сорок два', '四十二'; empty→ [], ''
- run card: `python3 utility_score.py ~/aura-pattern-library/python/data-science/experiments_ii/cluster_randomized_icc.py --abuse`

## `python/data-science/survival_and_reliability/log_rank_test.py`
- attack function: `log_rank_test(times_g1: List[float], events_g1: List[int], times_g2: List[float], events_g2: List[int])`
- garbage ideas: numbers→ -1, 0, 1e18, float('nan'); letters→ 'abc' where a number belongs; language→ 'сорок два', '四十二'; empty→ [], ''
- run card: `python3 utility_score.py ~/aura-pattern-library/python/data-science/survival_and_reliability/log_rank_test.py --abuse`

