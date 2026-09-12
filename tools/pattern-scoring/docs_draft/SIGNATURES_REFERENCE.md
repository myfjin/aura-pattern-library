# AUTHORITATIVE SIGNATURE REFERENCE (auto-extracted, full multi-line sigs — COPY VERBATIM)
# Doc writers: use these EXACTLY as the Entry fn. Do not rename params, reorder, or add defaults.

## __pycache__

## applied_ds_practice
### cohort_retention_analysis.py
```python
def build_cohort_table(events: list[dict]) -> dict[str, dict[int, int]]:
def compute_retention_rates(cohort_table: dict[str, dict[int, int]]) -> dict[str, list[float]]:
```
### cross_validation_leakage.py
```python
def univariate_correlation(X: list[list[float]], y: list[int]) -> list[float]:
def select_top_features(X: list[list[float]], y: list[int], k: int) -> list[int]:
def knn_classify(X_train: list[list[float]], y_train: list[int],
                 X_test: list[list[float]], k: int = 3) -> list[int]:
def accuracy(y_true: list[int], y_pred: list[int]) -> float:
```
### drift_detection_psi.py
```python
def reference_bin_edges(ref_values: list[float], n_bins: int = 10) -> list[float]:
def bin_with_edges(values: list[float], edges: list[float]) -> list[int]:
def population_stability_index(ref_bins: list[int], curr_bins: list[int],
                               n_bins: int = 10) -> float:
def kolmogorov_smirnov_statistic(ref_vals: list[float], curr_vals: list[float]) -> float:
```
### ewma_streaming_metrics.py
```python
class EWMAMetric:
def __init__(self, alpha: float = 0.3):
def update(self, x: float) -> float:
class SMAMetric:
def __init__(self, window_size: int = 10):
def update(self, x: float) -> float:
```
### feature_hashing_trick.py
```python
def hash_feature(feature_name: str, n_dims: int) -> int:
def hash_vectorize_text(texts: list[str], n_dims: int = 128) -> list[list[float]]:
def dot_product(v1: list[float], v2: list[float]) -> float:
def simple_linear_classifier(X_train: list[list[float]], y_train: list[int],
                             X_test: list[list[float]],
                             iterations: int = 100) -> list[float]:
def accuracy(y_true: list[int], y_pred: list[float]) -> float:
def collision_rate(texts: list[str], n_dims: int) -> float:
```
### funnel_conversion_analysis.py
```python
def wilson_confidence_interval(successes: int, trials: int, confidence: float = 0.95) -> tuple[float, float]:
def build_funnel_events(events: list[dict]) -> dict[str, dict]:
def compute_conversion_rates(funnel: dict[str, dict], step_order: list[str]) -> dict[str, dict]:
```
### rfm_customer_segmentation.py
```python
def compute_rfm_metrics(transactions: list[dict]) -> dict[int, dict]:
def quartile_score(values: list[float], recency_flag: bool = False) -> dict[float, int]:
def segment_from_rfm(r: int, f: int, m: int) -> str:
```
### simpsons_paradox_demo.py
```python
def compute_rate(numerator: int, denominator: int) -> float:
```
### target_encoding_smoothing.py
```python
def fit_encoding(cats: List[str], targets: List[int],
                 alpha: float = 0.0) -> Dict[str, float]:
def apply_encoding(cats: List[str], enc: Dict[str, float],
                   default: float) -> List[float]:
def oof_encode_train(cats: List[str], targets: List[int], n_folds: int = 5,
                     alpha: float = 5.0) -> List[float]:
def abs_correlation(X: List[float], y: List[int]) -> float:
```
### welford_online_stats.py
```python
class WelfordStats:
def update(self, x: float) -> None:
def variance(self) -> float:
def std_dev(self) -> float:
def naive_variance(values: list[float]) -> float:
def batch_variance(values: list[float]) -> float:
```

## bayesian_iii_approximate_inference
### abc_rejection_sampler.py
```python
def prior_sample():
def simulate_data(theta: float, n: int = 20) -> List[float]:
def distance(simulated: List[float], observed: List[float]) -> float:
def abc_rejection(observed: List[float], n_samples: int, epsilon: float) -> Tuple[List[float], float]:
```
### bayes_factor_normal_means.py
```python
def bayes_factor_normal(data, prior_var_h1=1.0) -> float:
```
### elbo_monotone_vi.py
```python
def true_log_evidence(data, mu0=0.0, s0=10.0) -> float:
def _elbo(data, m, s, mu0=0.0, s0=10.0) -> float:
def cavi_elbo_sequence(data, mu0=0.0, s0=10.0, cycles=15) -> Tuple[List[float], float]:
```
### hierarchical_shrinkage_2level.py
```python
def no_pooling_estimates(groups: List[List[float]]) -> List[float]:
def james_stein_estimates(groups: List[List[float]]) -> List[float]:
```
### laplace_approximation_posterior.py
```python
def log_posterior(theta: float, data, prior_mu=0.0, prior_sigma=1.0) -> float:
def find_map(data, prior_mu=0.0, prior_sigma=1.0, max_iter=100) -> float:
def laplace_approximation(data, prior_mu=0.0, prior_sigma=1.0) -> Tuple[float, float]:
```
### meanfield_vi_gaussian.py
```python
def meanfield_vi_normal_gamma(data: List[float], mu0=0.0, lam0=0.01, a0=0.01, b0=0.01,
                              max_iter=100) -> Tuple[float, float, List[float]]:
```
### posterior_contraction_rate.py
```python
def posterior_std_gaussian(data, prior_mu=0.0, prior_sigma_sq=10.0) -> float:
```
### posterior_predictive_pvalue.py
```python
def posterior_predictive_pvalue(observed_stat: float, posterior_samples: List[float]) -> float:
```
### rhat_convergence_diagnostic.py
```python
def rhat(chains: List[List[float]]) -> float:
```
### sbc_rank_uniformity.py
```python
def simulate_and_rank(n_sims: int, seed_offset=0) -> List[int]:
def chi_sq_gof(ranks: List[int], n_samples: int) -> float:
```

## bayesian_iii_modeling_and_selection
### bayesian_changepoint_offline.py
```python
def detect_changepoint(data: List[float]) -> int:
```
### bayesian_linreg_conjugate.py
```python
def bayesian_linreg_posterior(x_vals: List[float], y_vals: List[float]) -> Tuple[float, float]:
```
### beta_binomial_overdispersion.py
```python
def beta_binomial_loglik(counts: List[int], n_trials: int, alpha: float, beta: float) -> float:
def binomial_loglik(counts: List[int], n_trials: int, p: float) -> float:
def moment_match_beta_binomial(counts: List[int], n_trials: int) -> Tuple[float, float]:
```
### bic_selects_true_degree.py
```python
def _solve(A: List[List[float]], b: List[float]) -> List[float]:
def polynomial_rss(x: List[float], y: List[float], degree: int) -> float:
def bic(rss: float, n: int, k: int) -> float:
```
### crp_table_growth.py
```python
def crp_sample_num_tables(n: int, alpha: float) -> int:
```
### dirichlet_multinomial_posterior.py
```python
def dirichlet_posterior_concentration(counts: List[int], prior_alpha: float = 1.0) -> List[float]:
```
### dirichlet_stick_breaking.py
```python
def stick_breaking_process(alpha: float, num_breaks: int = 100) -> List[float]:
def count_active_clusters(weights: List[float], threshold: float = 0.01) -> int:
```
### evidence_ranks_true_model.py
```python
def gaussian_bic(data: List[float]) -> float:
def exponential_bic(data: List[float]) -> float:
```
### gp_regression_marginal_likelihood.py
```python
def _rbf_matrix(x: List[float], ls: float, noise: float) -> List[List[float]]:
def _cholesky(A: List[List[float]]) -> List[List[float]]:
def gp_log_marginal_likelihood(x: List[float], y: List[float], ls: float, noise: float = 0.05) -> float:
```
### kalman_rts_smoother.py
```python
def kalman_filter(y: List[float], q: float, r: float) -> Tuple[List[float], List[float]]:
def rts_smoother(x_filt: List[float], p_filt: List[float], q: float) -> List[float]:
```

## causal_inference_and_experimentation
### ab_test_srm_check.py
```python
def chi_square_gof(observed: list, expected: list) -> Tuple[float, float]:
```
### cuped_variance_reduction.py
```python
def mean(values: List[float]) -> float:
def variance(values: List[float]) -> float:
def covariance(x: List[float], y: List[float]) -> float:
```
### difference_in_differences.py
```python
def simulate_did_data(
    n_per_group: int, treatment_effect: float, time_effect: float
) -> Tuple[List[float], List[float], List[float], List[float]]:
def mean(values: List[float]) -> float:
def estimate_did(
    pre_control: List[float],
    post_control: List[float],
    pre_treated: List[float],
    post_treated: List[float],
) -> float:
```
### instrumental_variable_lite.py
```python
def covariance(x: List[float], y: List[float]) -> float:
```
### interrupted_time_series.py
```python
def fit_segmented_regression(
    times: List[int], Y: List[float], cutoff: int
) -> Tuple[float, float, float, float]:
```
### placebo_test_causal.py
```python
def estimate_effect(T: List[int], Y: List[float]) -> float:
```
### propensity_score_matching.py
```python
def logistic(x: float) -> float:
def estimate_propensity_scores(
    X: List[float], T: List[int]
) -> List[float]:
def match_on_propensity(
    propensity_scores: List[float], T: List[int], caliper: float = 0.1
) -> Tuple[List[int], List[int]]:
def estimate_ate_naive(T: List[int], Y: List[float]) -> float:
def estimate_ate_matched(
    T: List[int], Y: List[float], matched_t: List[int], matched_c: List[int]
) -> float:
```
### regression_discontinuity.py
```python
def local_linear_fit(
    x_window: List[float], y_window: List[float]
) -> Tuple[float, float]:
```
### sequential_probability_ratio.py
```python
def sprt(
    data: list,
    p0: float,
    p1: float,
    alpha: float = 0.05,
    beta: float = 0.05,
) -> Tuple[str, int]:
def fixed_n_test(
    data: list,
    p0: float,
    p1: float,
    alpha: float = 0.05,
) -> str:
```
### synthetic_control_lite.py
```python
def fit_weights(
    pre_treated: List[float], pre_controls: List[List[float]]
) -> List[float]:
```

## causal_inference_ii
### backdoor_vs_collider_adjustment.py
```python
def fit_regression(x: List[float], y: List[float]) -> Tuple[float, float]:
```
### caliper_matching.py
```python
def euclidean_distance(x1: float, x2: float) -> float:
def nearest_neighbor_match(treated: List[float], control: List[float], caliper: float = float('inf')) -> Tuple[List[Tuple[int, int]], int]:
def estimate_bias(treated_vals: List[float], control_vals: List[float],
                  outcome_treated: List[float], outcome_control: List[float],
                  matches: List[Tuple[int, int]]) -> float:
```
### doubly_robust_aipw.py
```python
def logistic(x: float) -> float:
def fit_outcome_model(x: List[float], t: List[int], y: List[float]) -> Tuple[float, float, float]:
def estimate_propensity(x: List[float], t: List[int]) -> List[float]:
def aipw_ate(x: List[float], t: List[int], y: List[float]) -> float:
```
### e_value_sensitivity.py
```python
def risk_ratio_from_counts(t1_y1: int, t1_y0: int, t0_y1: int, t0_y0: int) -> float:
def e_value(rr: float) -> float:
def build_2x2_table(treatment: list, outcome: list) -> Tuple[int, int, int, int]:
```
### frontdoor_criterion_lite.py
```python
def simple_slope(x: List[float], y: List[float]) -> float:
def partial_slope_m(x: List[float], m: List[float], y: List[float]) -> float:
def frontdoor_lite(x, m, y) -> Tuple[float, float]:
```
### heterogeneous_effects_subgroups.py
```python
def subgroup_ate(t: List[int], y: List[float], subgroup: List[int], sg_val: int) -> float:
def pooled_ate(t: List[int], y: List[float]) -> float:
```
### ipw_ate.py
```python
def logistic(x: float) -> float:
def estimate_propensity(x_vals: List[float], t_vals: List[int]) -> List[float]:
def ipw_ate(t_vals: List[int], y_vals: List[float], propensity: List[float]) -> float:
def naive_ate(t_vals: List[int], y_vals: List[float]) -> float:
```
### mediation_effects_decomposition.py
```python
def fit_simple_slope(x_vals, y_vals) -> float:
def mediation_analysis(x, m, y) -> Tuple[float, float, float]:
```
### negative_control_outcome.py
```python
def fit_regression_coef(x: List[float], y: List[float]) -> float:
```
### stratification_subclassification.py
```python
def logistic(x: float) -> float:
def estimate_propensity(x: List[float], t: List[int]) -> List[float]:
def stratify_by_propensity(propensity: List[float], t: List[int], y: List[float], num_strata: int = 5) -> Tuple[float, float]:
```

## clustering_graph_and_anomaly
### betweenness_centrality.py
```python
def betweenness_centrality(graph: Dict[int, List[int]]) -> Dict[int, float]:
```
### classic_mds.py
```python
def euclidean_distance(p1: Tuple[float, ...], p2: Tuple[float, ...]) -> float:
def distance_matrix(points: List[Tuple[float, ...]]) -> List[List[float]]:
def gram_matrix_centered(points: List[Tuple[float, ...]]) -> List[List[float]]:
def classical_mds_2d(points: List[Tuple[float, ...]]) -> List[Tuple[float, float]]:
```
### dbscan_clustering.py
```python
def euclidean_distance(p1: Tuple[float, ...], p2: Tuple[float, ...]) -> float:
def region_query(points: List[Tuple[float, ...]], p: int, eps: float) -> Set[int]:
def dbscan(points: List[Tuple[float, ...]], eps: float, min_pts: int) -> List[int]:
def expand_cluster(
    points: List[Tuple[float, ...]],
    labels: List[int],
    p: int,
    cluster_id: int,
    eps: float,
    min_pts: int
) -> None:
```
### elbow_method_kmeans.py
```python
def euclidean_distance(p1: Tuple[float, ...], p2: Tuple[float, ...]) -> float:
def kmeans(
    points: List[Tuple[float, ...]],
    k: int,
    max_iterations: int = 100,
    seed: int = 42
) -> Tuple[List[int], List[Tuple[float, ...]], float]:
def elbow_knee(inertias: List[float]) -> int:
```
### hierarchical_agglomerative.py
```python
def euclidean_distance(p1: Tuple[float, ...], p2: Tuple[float, ...]) -> float:
def cluster_distance(
    cluster_a: List[int],
    cluster_b: List[int],
    points: List[Tuple[float, ...]],
    linkage: str
) -> float:
def hierarchical_agglomerative(
    points: List[Tuple[float, ...]],
    linkage: str = "complete"
) -> Tuple[List[List[int]], List[Tuple[int, int, float]]]:
def cut_dendrogram(
    points: List[Tuple[float, ...]],
    k: int,
    linkage: str = "complete"
) -> List[int]:
def most_common(lst):
```
### isolation_tree_anomaly.py
```python
class IsolationNode:
def __init__(self):
def build_isolation_tree(
    points: List[Tuple[float, ...]],
    indices: List[int],
    depth: int = 0,
    max_depth: int = 10,
) -> IsolationNode:
def path_length(tree: IsolationNode, point: Tuple[float, ...], depth: int = 0) -> int:
def isolation_forest_anomaly_score(
    points: List[Tuple[float, ...]],
    num_trees: int = 50,
    seed: int = 42,
) -> List[float]:
```
### label_propagation_communities.py
```python
def label_propagation(
    graph: Dict[int, List[int]],
    max_iterations: int = 100,
    seed: int = 42
) -> Dict[int, int]:
```
### linear_discriminant_analysis.py
```python
def matrix_inverse_2x2(m: List[List[float]]) -> List[List[float]]:
def matrix_multiply_2x2(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
def power_iteration_2x2(m: List[List[float]], iterations: int = 100) -> Tuple[float, List[float]]:
def lda_2d(
    points: List[Tuple[float, float]],
    labels: List[int]
) -> Tuple[List[float], float]:
```
### random_projection_jl.py
```python
def random_projection_matrix(
    original_dim: int,
    target_dim: int,
    seed: int = 42
) -> List[List[float]]:
def project_point(point: Tuple[float, ...], projection_matrix: List[List[float]]) -> Tuple[float, ...]:
def euclidean_distance(p1: Tuple[float, ...], p2: Tuple[float, ...]) -> float:
```
### silhouette_score.py
```python
def euclidean_distance(p1: Tuple[float, ...], p2: Tuple[float, ...]) -> float:
def silhouette_score(
    points: List[Tuple[float, ...]],
    labels: List[int]
) -> float:
```

## composed_tools
### broker_term_extraction.py
```python
def cooccurrence_graph(sentences: List[List[str]]) -> Dict[str, Set[str]]:
def betweenness(g: Dict[str, Set[str]]) -> Dict[str, float]:
```
### community_local_authority.py
```python
def label_propagation(g: Dict[str, Set[str]], iters: int = 30,
                      seed: int = 42) -> Dict[str, int]:
def pagerank(g: Dict[str, Set[str]], nodes: Set[str], damping: float = 0.85,
             iters: int = 100) -> Dict[str, float]:
def link(a: str, b: str):
```
### cross_domain_query_expansion.py
```python
def cooccurrence_graph(docs: List[List[str]]) -> Dict[str, Set[str]]:
def betweenness(g: Dict[str, Set[str]]) -> Dict[str, float]:
def tfidf_vectors(docs: List[List[str]]):
def cosine(a: Dict[str, float], b: Dict[str, float]) -> float:
def retrieve(query: List[str], docs: List[List[str]], k: int) -> List[int]:
def prf_expand(query: List[str], docs: List[List[str]], top_docs: int = 3,
               n_terms: int = 3) -> List[str]:
def broker_expand(query: List[str], docs: List[List[str]], n_terms: int = 3) -> List[str]:
```
### cross_domain_search_engine.py
```python
def stem(word: str) -> str:
def stem_doc(doc: List[str]) -> List[str]:
def cooccurrence_graph(docs: List[List[str]]) -> Dict[str, Set[str]]:
def betweenness(g: Dict[str, Set[str]]) -> Dict[str, float]:
def broker_terms(docs: List[List[str]], top: int = 3) -> List[str]:
def expand_query(query: List[str], brokers: List[str]) -> List[str]:
def bm25_rank(query: List[str], docs: List[List[str]], k1: float = 1.5,
              b: float = 0.75) -> List[Tuple[int, float]]:
```
### dedup_pipeline.py
```python
def shingles(text: str, k: int = 3) -> Set[str]:
def minhash_signature(sh: Set[str], num_hashes: int = 64) -> Tuple[int, ...]:
def estimated_jaccard(a: Tuple[int, ...], b: Tuple[int, ...]) -> float:
def edit_distance(a: str, b: str) -> int:
def word_diff(a: str, b: str) -> List[str]:
def dedup_pipeline(docs: List[str], cand_thresh: float = 0.5,
                   verify_ratio: float = 0.25):
```
### dtw_shape_drift_monitor.py
```python
def dtw_distance(a: List[float], b: List[float]) -> float:
def daily_profile(shift_hours: int, noise: float) -> List[float]:
def mean(v: List[float]) -> float:
def std(v: List[float]) -> float:
```
### forest_size_by_variance.py
```python
def gini(labels: List[int]) -> float:
def build_stump(X: List[Point], y: List[int], rng: random.Random) -> dict:
def predict_stump(x: Point, t: dict) -> int:
def random_forest(X: List[Point], y: List[int], n_trees: int, rng: random.Random) -> List[dict]:
def predict_forest(x: Point, forest: List[dict]) -> float:
def bias_variance_at_size(X, y, test_pts, truth, n_trees, n_boot, base_seed):
def _variance(v: List[float]) -> float:
```
### interleaving_significance.py
```python
def interleave_team_draft(ranking_a: List[str], ranking_b: List[str],
                          rng: random.Random) -> List[Tuple[str, str]]:
def query_credit(a_rank: List[str], b_rank: List[str], relevance: dict,
                 rng: random.Random) -> int:
def paired_bootstrap_ci(diffs: List[float], n_boot: int, rng: random.Random,
                        alpha: float = 0.05) -> Tuple[float, float, float]:
def run_experiment(a_better: bool, n_queries: int, rng: random.Random):
```
### kde_seeded_gmm.py
```python
def kde(values: List[float], grid: List[float]) -> List[float]:
def kde_modes(values: List[float], n_grid: int = 200) -> List[float]:
def em_gmm(values: List[float], means: List[float], iters: int = 200,
           tol: float = 1e-7) -> Tuple[List[float], List[float], List[float], float, int]:
def recovered(mu: List[float], truth: List[float], tol: float = 0.5) -> bool:
```
### knn_kdtree_accelerated.py
```python
class KDNode:
def __init__(self, point: Point, label: int, axis: int):
def build_kdtree(items: List[Tuple[Point, int]], depth: int = 0) -> Optional[KDNode]:
def sqdist(a: Point, b: Point, counter_key: str) -> float:
def knn_tree(root: KDNode, q: Point, k: int) -> List[Tuple[float, int]]:
def visit(node: Optional[KDNode]):
def knn_brute(items: List[Tuple[Point, int]], q: Point, k: int) -> List[Tuple[float, int]]:
def majority(neigh: List[Tuple[float, int]]) -> int:
```
### latency_percentile_monitor.py
```python
class P2Quantile:
def __init__(self, p: float):
def process(self, x: float) -> None:
def query(self) -> float:
class LatencyMonitor:
def __init__(self):
def record(self, service: str, latency_ms: float) -> None:
def snapshot(self, service: str) -> Dict[str, float]:
def lognormalish(base: float, tail: float) -> float:
```
### mutual_information_matrix.py
```python
def equal_frequency_bins(values: List[float], n_bins: int) -> List[int]:
def mutual_information(xb: List[int], yb: List[int], n_bins: int) -> float:
def normalized_mi(x: List[float], y: List[float], n_bins: int = 8) -> float:
def entropy(bins_: List[int]) -> float:
def abs_pearson(x: List[float], y: List[float]) -> float:
def dependence_matrices(features: Dict[str, List[float]]):
```
### queue_capacity_planner.py
```python
def simulate_queue(arrival_rate: float, service_rate: float, workers: int,
                   n_jobs: int, seed: int) -> Dict[str, float]:
def plan_capacity(arrival_rate: float, service_rate: float, sla_mean_wait: float,
                  n_jobs: int = 30000) -> Tuple[int, Dict[int, float]]:
```
### rare_event_option_pricing.py
```python
def norm_cdf(x: float) -> float:
def black_scholes_call() -> float:
def terminal_price(z: float) -> float:
def naive_mc(n: int, rng: random.Random) -> float:
def importance_sampled_mc(n: int, rng: random.Random) -> Tuple[float, float]:
```
### rolling_ols_update.py
```python
def naive_windowed_slope(xs: List[float], ys: List[float], w: int) -> List[Tuple[float, float]]:
class RollingCovariance:
def __init__(self) -> None:
def add(self, x: float, y: float) -> None:
def remove(self, x: float, y: float) -> None:
def slope_intercept(self) -> Tuple[float, float]:
def rolling_windowed_slope(xs: List[float], ys: List[float], w: int) -> List[Tuple[float, float]]:
```
### topic_aware_recommender.py
```python
def cooccurrence_graph(docs: List[List[str]]) -> Dict[str, Dict[str, float]]:
def label_propagation(g: Dict[str, Dict[str, int]], iters: int = 40, seed: int = 42) -> Dict[str, int]:
def pagerank(g: Dict[str, Dict[str, int]], nodes: Set[str], damping: float = 0.85,
             iters: int = 60) -> Dict[str, float]:
def topic_signatures(g, comms) -> Dict[int, Dict[str, float]]:
def real_communities(comms: Dict[str, int], min_size: int = 2) -> Set[int]:
def doc_topic_vector(doc: List[str], comms, sigs, real: Set[int]) -> Dict[int, float]:
def recommend(query_doc, docs, comms, sigs, real, k: int) -> List[int]:
def cos(a, b):
def flat_recommend(query_doc, docs, k: int) -> List[int]:
```
### walk_forward_early_stopping.py
```python
def fit_stump_to_residuals(X: List[List[float]], r: List[float]) -> Stump:
def predict_stump(x: List[float], s: Stump) -> float:
def predict_ensemble(x: List[float], stumps: List[Stump], lr: float) -> float:
def mae(y_true: List[float], y_pred: List[float]) -> float:
```

## core_ml
### decision_tree_id3.py
```python
def entropy(class_counts: Dict[int, int]) -> float:
def information_gain(
    parent_entropy: float,
    child_entropies: List[Tuple[int, float]]
) -> float:
class TreeNode:
def __init__(self):
def build_tree(
    X: List[List[float]],
    y: List[int],
    max_depth: int = 5,
    depth: int = 0
) -> TreeNode:
def predict_tree(x: List[float], node: TreeNode) -> int:
```
### gaussian_mixture_em.py
```python
def normal_pdf(x: float, mean: float, var: float) -> float:
def em_fit_1d(
    X: List[float],
    k: int,
    max_iterations: int = 100,
    tolerance: float = 1e-6
) -> Tuple[List[float], List[float], List[float]]:
def gmm_predict_responsibilities(
    X: List[float],
    means: List[float],
    variances: List[float],
    weights: List[float]
) -> List[List[float]]:
```
### kmeans_clustering.py
```python
def euclidean_distance(p1: List[float], p2: List[float]) -> float:
def kmeans(
    X: List[List[float]],
    k: int,
    max_iterations: int = 100,
    tolerance: float = 1e-4
) -> Tuple[List[List[float]], List[int]]:
def intra_cluster_distance(
    X: List[List[float]],
    centroids: List[List[float]],
    assignments: List[int]
) -> float:
```
### knn_classifier.py
```python
def euclidean_distance(p1: List[float], p2: List[float]) -> float:
def knn_predict(
    x_test: List[float],
    X_train: List[List[float]],
    y_train: List[int],
    k: int = 3
) -> int:
def knn_predict_batch(
    X_test: List[List[float]],
    X_train: List[List[float]],
    y_train: List[int],
    k: int = 3
) -> List[int]:
```
### linear_regression_gd.py
```python
def mean(values: List[float]) -> float:
def variance(values: List[float]) -> float:
def linear_regression_gd(
    X: List[List[float]],
    y: List[float],
    learning_rate: float = 0.01,
    iterations: int = 100
) -> Tuple[List[float], float]:
```
### logistic_regression.py
```python
def sigmoid(z: float) -> float:
def logistic_regression_fit(
    X: List[List[float]],
    y: List[int],
    learning_rate: float = 0.01,
    iterations: int = 100
) -> Tuple[List[float], float]:
def logistic_regression_predict(
    X: List[List[float]],
    weights: List[float],
    bias: float,
    threshold: float = 0.5
) -> List[int]:
```
### naive_bayes_text.py
```python
def naive_bayes_train(
    texts: List[List[str]],
    labels: List[int]
) -> Tuple[Dict[int, float], Dict[int, Dict[str, float]]]:
def naive_bayes_predict(
    text: List[str],
    class_priors: Dict[int, float],
    word_probs: Dict[int, Dict[str, float]]
) -> int:
```
### pca_power_iteration.py
```python
def matrix_mean_center(X: List[List[float]]) -> TupleType[List[List[float]], List[float]]:
def matrix_multiply(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
def matrix_transpose(A: List[List[float]]) -> List[List[float]]:
def covariance_matrix(X: List[List[float]]) -> List[List[float]]:
def vector_norm(v: List[float]) -> float:
def matrix_vector_multiply(A: List[List[float]], v: List[float]) -> List[float]:
def power_iteration(
    cov: List[List[float]],
    num_components: int = 1,
    max_iterations: int = 100
) -> Tuple[List[List[float]], List[float]]:
def pca_transform(X: List[List[float]], components: List[List[float]]) -> List[List[float]]:
```
### perceptron.py
```python
def perceptron_fit(
    X: List[List[float]],
    y: List[int],
    learning_rate: float = 1.0,
    max_iterations: int = 100
) -> Tuple[List[float], float]:
def perceptron_predict(
    X: List[List[float]],
    weights: List[float],
    bias: float
) -> List[int]:
```
### ridge_regression_normal_eq.py
```python
def matrix_transpose(A: List[List[float]]) -> List[List[float]]:
def matrix_multiply(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
def matrix_vector_multiply(A: List[List[float]], v: List[float]) -> List[float]:
def add_identity_scaled(A: List[List[float]], lambda_val: float) -> List[List[float]]:
def gaussian_elimination(A: List[List[float]], b: List[float]) -> List[float]:
def ridge_regression_normal_eq(
    X: List[List[float]],
    y: List[float],
    lambda_reg: float = 0.01
) -> List[float]:
def ridge_regression_predict(
    X: List[List[float]],
    weights: List[float]
) -> List[float]:
```

## data_wrangling_from_scratch
### csv_type_inference.py
```python
def infer_type(value: str) -> str:
def infer_column_types(
    rows: List[Dict[str, str]]
) -> Dict[str, str]:
```
### dedupe_records_fuzzy.py
```python
def normalize(s: str) -> str:
def edit_distance(s1: str, s2: str) -> int:
def find_duplicates(
    records: List[Dict[str, Any]],
    match_key: str,
    threshold: int = 2,
) -> List[List[int]]:
def dedupe(
    records: List[Dict[str, Any]],
    match_key: str,
    threshold: int = 2,
) -> List[Dict[str, Any]]:
```
### group_by_aggregate.py
```python
def group_by_aggregate(
    records: List[Dict[str, Any]],
    group_keys: List[str],
    agg_col: str,
    agg_func: str,  # "sum", "mean", "count", "min", "max"
) -> Dict[tuple, float]:
def brute_force_aggregate(
    records: List[Dict[str, Any]],
    group_keys: List[str],
    agg_col: str,
    agg_func: str,
) -> Dict[tuple, float]:
```
### hash_join_merge.py
```python
def hash_join_inner(
    left_table: List[Dict[str, Any]],
    right_table: List[Dict[str, Any]],
    join_key: str,
) -> List[Dict[str, Any]]:
def hash_join_left(
    left_table: List[Dict[str, Any]],
    right_table: List[Dict[str, Any]],
    join_key: str,
) -> List[Dict[str, Any]]:
def nested_loop_inner_join(
    left_table: List[Dict[str, Any]],
    right_table: List[Dict[str, Any]],
    join_key: str,
) -> List[Dict[str, Any]]:
```
### melt_unpivot.py
```python
def melt(
    wide_data: Dict[Any, Dict[Any, float]],
    row_key_name: str,
    col_key_name: str,
    val_key_name: str,
) -> List[Dict[str, Any]]:
def pivot_table(
    records: List[Dict[str, Any]],
    row_key: str,
    col_key: str,
    val_key: str,
) -> Dict[Any, Dict[Any, float]]:
```
### pivot_table.py
```python
def pivot_table(
    records: List[Dict[str, Any]],
    row_key: str,
    col_key: str,
    val_key: str,
    agg_func: str = "sum",
) -> Dict[Any, Dict[Any, float]]:
def compute_margins(pivot: Dict[Any, Dict[Any, float]]) -> Dict[str, Dict[Any, float]]:
```
### resample_timeseries_bins.py
```python
def parse_timestamp(ts: str) -> tuple:
def bucket_hourly(records: List[Dict[str, Any]]) -> Dict[tuple, float]:
def bucket_daily(records: List[Dict[str, Any]]) -> Dict[tuple, float]:
def brute_force_hourly(records: List[Dict[str, Any]]) -> Dict[tuple, float]:
```
### rolling_join_asof.py
```python
def asof_join(
    left: List[Dict[str, Any]],
    right: List[Dict[str, Any]],
    key: str,  # Timestamp key to join on
) -> List[Dict[str, Any]]:
def brute_force_asof(
    left: List[Dict[str, Any]],
    right: List[Dict[str, Any]],
    key: str,
) -> List[Dict[str, Any]]:
```
### sort_multi_key.py
```python
def multi_key_sort(
    records: List[Dict[str, Any]],
    keys: List[tuple],  # [(key_name, is_asc), ...]
) -> List[Dict[str, Any]]:
def sort_key(record):
```
### window_functions.py
```python
def apply_window_functions(
    records: List[Dict[str, Any]],
    partition_key: str,
    order_key: str,
) -> List[Dict[str, Any]]:
```

## econometrics_and_finance
### black_scholes_monte_carlo.py
```python
def black_scholes_call(S: float, K: float, T: float, r: float, sigma: float) -> float:
def norm_cdf(x: float) -> float:
def monte_carlo_call(S: float, K: float, T: float, r: float, sigma: float, num_sim: int) -> Tuple[float, float]:
```
### bootstrap_portfolio_var.py
```python
def _quantile(sorted_vals: List[float], q: float) -> float:
def portfolio_var_bootstrap(
    returns: List[float],
    confidence_level: float = 0.95,
    num_bootstrap: int = 1000,
) -> Tuple[float, float]:
```
### cointegration_engle_granger_lite.py
```python
def _ols_residuals(y: List[float], x: List[float]) -> List[float]:
def _adf_tstat(e: List[float]) -> float:
def engle_granger_test(y: List[float], x: List[float]) -> Tuple[float, bool]:
```
### fixed_effects_within.py
```python
def pooled_ols(y: List[float], x: List[float]) -> float:
def within_estimator(y: List[List[float]], x: List[List[float]]) -> float:
```
### garch_lite_volatility_clustering.py
```python
def garch11_fit(returns: List[float], max_pass: int = 200) -> Tuple[float, float, float]:
def neg_loglik(omega: float, alpha: float, beta: float) -> float:
```
### instrumental_2sls.py
```python
def ols_simple(y: List[float], x: List[float]) -> float:
def tsls(y: List[float], x: List[float], z: List[float]) -> float:
```
### logit_marginal_effects.py
```python
def logit_predict(x: float, beta: float) -> float:
def logit_marginal_effect(x: float, beta: float) -> float:
def average_marginal_effect(x_values: List[float], beta: float) -> float:
def numerical_gradient(x: float, beta: float, eps: float = 1e-6) -> float:
```
### ols_robust_se_white.py
```python
def ols_fit(y: List[float], X: List[List[float]]) -> Tuple[List[float], List[float], List[float]]:
```
### sharpe_sortino_ratios.py
```python
def sharpe_ratio(returns: List[float], risk_free_rate: float = 0.0) -> float:
def sortino_ratio(returns: List[float], target_return: float = 0.0) -> float:
```
### value_averaging_vs_dca.py
```python
def dollar_cost_averaging(prices: list, invest_per_period: float) -> float:
def value_averaging(prices: list, target_growth_rate: float) -> float:
```

## ensembles_and_robust_methods
### adaboost.py
```python
def fit_stump_binary(X: List[Tuple[float, float]], y: List[int],
                     sample_weights: List[float]) -> Tuple[int, float, int, int]:
def predict_stump(x: Tuple[float, float], feature: int, threshold: float,
                  left_label: int, right_label: int) -> int:
def adaboost(X: List[Tuple[float, float]], y: List[int], n_rounds: int = 10) -> List[Tuple]:
def predict_ensemble(x: Tuple[float, float], ensemble: List[Tuple]) -> int:
```
### bagging_variance_reduction.py
```python
def true_fn(x: float) -> float:
def make_training_set(n: int) -> Tuple[List[float], List[float]]:
def fit_stump(X: List[float], y: List[float]) -> Stump:
def predict_stump(x: float, s: Stump) -> float:
def fit_bagged(X: List[float], y: List[float], n_models: int = 25) -> List[Stump]:
def predict_bagged(x: float, models: List[Stump]) -> float:
```
### gradient_boosting_stumps.py
```python
def gini_split(y: List[float]) -> Tuple[float, float]:
def fit_stump(X: List[Tuple[float, float]], y: List[float]) -> Tuple[int, float, float, float]:
def predict_stump(x: Tuple[float, float], feature: int, threshold: float,
                  left_val: float, right_val: float) -> float:
def gradient_boost(X: List[Tuple[float, float]], y: List[float], n_rounds: int = 10,
                   learning_rate: float = 0.1) -> Tuple[List[Tuple[int, float, float, float, float]], float]:
```
### huber_robust_regression.py
```python
def huber_loss(residual: float, delta: float = 1.0) -> float:
def huber_gradient(residual: float, delta: float = 1.0) -> float:
def fit_line_huber(X: List[float], y: List[float], delta: float = 1.5,
                   learning_rate: float = 0.05, iterations: int = 300) -> Tuple[float, float]:
def ordinary_least_squares(X: List[float], y: List[float]) -> Tuple[float, float]:
def squared_loss_error(y_true: List[float], y_pred: List[float]) -> float:
```
### random_forest.py
```python
def build_tree(X: List[Tuple[float, float]], y: List[int], depth: int = 0,
               max_depth: int = 5, min_samples: int = 2) -> dict:
def gini(labels):
def predict_tree(x: Tuple[float, float], tree: dict) -> int:
def bootstrap_sample(X: List[Tuple[float, float]], y: List[int]) -> Tuple[List, List, List, List]:
def random_forest(X: List[Tuple[float, float]], y: List[int], n_trees: int = 10) -> List[dict]:
def predict_forest(x: Tuple[float, float], forest: List[dict]) -> int:
```
### ransac_robust_regression.py
```python
def fit_line_2point(p1: Tuple[float, float], p2: Tuple[float, float]) -> Tuple[float, float]:
def predict_line(x: float, m: float, b: float) -> float:
def residual_distance(y_true: float, y_pred: float) -> float:
def ransac_regression(X: List[float], y: List[float], n_iterations: int = 100,
                      threshold: float = 1.0) -> Tuple[float, float]:
def ordinary_least_squares(X: List[float], y: List[float]) -> Tuple[float, float]:
```
### spectral_clustering_lite.py
```python
def euclidean_distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
def build_affinity_matrix(X: List[Tuple[float, float]], sigma: float = 1.0) -> List[List[float]]:
def compute_degree_matrix_diag(W: List[List[float]]) -> List[float]:
def graph_laplacian(W: List[List[float]]) -> List[List[float]]:
def power_iteration(L: List[List[float]], num_iter: int = 300) -> List[float]:
def knn_sparsify(W: List[List[float]], k: int = 6) -> List[List[float]]:
def spectral_cluster_two_moons(X: List[Tuple[float, float]]) -> List[int]:
def kmeans_baseline(X: List[Tuple[float, float]], k: int = 2, n_iter: int = 20) -> List[int]:
def clustering_accuracy(pred: List[int], truth: List[int]) -> float:
```
### stacking_ensemble.py
```python
def fit_linear_model(X_base: List[List[float]], y: List[float]) -> Tuple[float, float]:
def predict_linear(X: List[float], b0: float, coef: List[float]) -> float:
class BaseModel1:
def __init__(self):
def fit(self, X: List[Tuple[float, float]], y: List[int]):
def predict(self, X: List[Tuple[float, float]]) -> List[float]:
class BaseModel2:
def __init__(self):
def fit(self, X: List[Tuple[float, float]], y: List[int]):
def predict(self, X: List[Tuple[float, float]]) -> List[float]:
def generate_base_predictions(X: List[Tuple[float, float]], y: List[int],
                              base_models: List, k_folds: int = 5) -> List[List[float]]:
def fit_stacking(X: List[Tuple[float, float]], y: List[int],
                 base_models: List, k_folds: int = 5) -> Tuple[List, float, List[float]]:
def predict_stacking(X: List[Tuple[float, float]], base_models: List,
                     b0: float, coef: List[float]) -> List[int]:
```
### theil_sen_estimator.py
```python
def theil_sen_estimator(X: List[float], y: List[float]) -> Tuple[float, float]:
def ordinary_least_squares(X: List[float], y: List[float]) -> Tuple[float, float]:
```
### voting_classifier.py
```python
def threshold_classifier_x(X: List[Tuple[float, float]], y: List[int],
                          split_dim: int) -> float:
def predict_classifier_x(x: Tuple[float, float], threshold: float, split_dim: int) -> int:
class WeakClassifier1:
def __init__(self, X: List[Tuple[float, float]], y: List[int]):
def predict(self, x: Tuple[float, float]) -> int:
class WeakClassifier2:
def __init__(self, X: List[Tuple[float, float]], y: List[int]):
def predict(self, x: Tuple[float, float]) -> int:
class WeakClassifier3:
def __init__(self, X: List[Tuple[float, float]], y: List[int]):
def predict(self, x: Tuple[float, float]) -> int:
def hard_voting(X: List[Tuple[float, float]], classifiers: List) -> List[int]:
def soft_voting(X: List[Tuple[float, float]], classifiers: List) -> List[int]:
```

## experiments_ii
### cluster_randomized_icc.py
```python
def _var(z: List[float]) -> float:
def naive_ci_covers(t_obs: List[float], c_obs: List[float], true_effect: float) -> bool:
def cluster_ci_covers(t_means: List[float], c_means: List[float], true_effect: float) -> bool:
def make_dataset(seed: int, n_clusters: int, m: int, icc: float, true_effect: float) -> Tuple[list, list, list, list]:
def arm(base: float):
```
### minimum_detectable_effect.py
```python
def mde_normal_approx(n_per_arm: int, alpha: float = 0.05, power: float = 0.8, sigma: float = 1.0) -> float:
def simulate_power(n_per_arm: int, true_effect: float, reps: int = 500) -> float:
```
### msprt_lite.py
```python
def msprt_reject(diff_gen: Callable[[], float], alpha: float, tau2: float, v: float, max_n: int) -> bool:
def naive_peek_reject(diff_gen: Callable[[], float], alpha: float, v: float, max_n: int) -> bool:
```
### multi_armed_holm_correction.py
```python
def bonferroni_threshold(alpha: float, num_tests: int) -> float:
def holm_thresholds(alpha: float, num_tests: int) -> List[float]:
def run_multiple_tests(p_values: List[float], method: str = "uncorrected") -> List[bool]:
```
### network_interference_demo.py
```python
def simulate_spillover_network(n: int, treatment: List[int], effect_direct: float, effect_spillover: float) -> List[float]:
def naive_ate(treatment: List[int], outcomes: List[float]) -> float:
```
### novelty_effect_decay.py
```python
def simulate_novelty_decay(n_users: int, true_long_run_effect: float, novelty_boost: float, decay_rate: float) -> List[List[float]]:
def time_sliced_ate(control_outcomes: List[List[float]], treatment_outcomes: List[List[float]], day: int) -> float:
```
### peeking_alpha_inflation.py
```python
def t_test_pvalue(mean_treatment: float, mean_control: float, var_t: float, var_c: float,
                 n_t: int, n_c: int) -> float:
def fixed_n_no_peeking(n_per_arm: int, reps: int, null: bool = True) -> float:
def peeking_strategy(n_per_arm_initial: int, n_looks: int, reps: int) -> float:
```
### post_stratification_variance.py
```python
def simple_ate(t: List[int], y: List[float]) -> Tuple[float, float]:
def post_stratified_ate(t: List[int], y: List[float], x: List[float]) -> Tuple[float, float]:
```
### stratified_randomization.py
```python
def simple_randomization(n: int, seed: int) -> List[int]:
def stratified_randomization(x: List[float], seed: int) -> List[int]:
def covariate_balance(x: List[float], t: List[int]) -> float:
def ate_variance(t: List[int], y: List[float]) -> float:
```
### switchback_experiment_lite.py
```python
def user_split_ab(n_users: int, true_effect: float, spillover: float) -> float:
def switchback(n_blocks: int, block_size: int, true_effect: float) -> float:
```

## fairness_privacy_and_robustness
### adversarial_perturbation_lite.py
```python
def adversarial_perturbation_lite() -> None:
def sigmoid(z: float) -> float:
def predict(x: Tuple[float, float], weights: List[float] = None) -> float:
```
### covariate_shift_reweighting.py
```python
def covariate_shift_reweighting() -> None:
def linear_regression(X: List[float], y: List[float], weights: List[float] = None) -> Tuple[float, float]:
def mse(X: List[float], y: List[float], slope: float, intercept: float) -> float:
```
### demographic_parity_metrics.py
```python
def demographic_parity_metrics() -> None:
def dp_metrics(predictions: list[int], groups_list: list[int]) -> Tuple[float, float]:
```
### differential_privacy_laplace.py
```python
def differential_privacy_laplace() -> None:
```
### equalized_odds_thresholds.py
```python
def equalized_odds_thresholds() -> None:
def tpr_per_group(preds: list[int], true: list[int], groups: list[int]) -> Tuple[float, float]:
```
### group_calibration_audit.py
```python
def group_calibration_audit() -> None:
def expected_calibration_error(probs: List[float], labels: List[int], bins: int = 5) -> float:
```
### k_anonymity_generalization.py
```python
def k_anonymity_generalization() -> None:
def generalize_age(age: int) -> str:
```
### label_noise_robust_loss.py
```python
def label_noise_robust_loss() -> None:
def train_and_eval(labels: List[int], loss_type: str) -> float:
def sigmoid(z: float) -> float:
def predict(x: Tuple[float, float]) -> float:
```
### mnar_missingness_bias.py
```python
def mnar_missingness_bias() -> None:
def complete_case_mean(observed: List) -> float:
```
### randomized_response.py
```python
def randomized_response() -> None:
```

## geospatial_and_spatial
### convex_hull_graham.py
```python
def cross_product(o: Tuple[float, float], a: Tuple[float, float],
                  b: Tuple[float, float]) -> float:
def convex_hull_graham(points: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
def polar_angle_key(p: Tuple[float, float]) -> float:
```
### douglas_peucker.py
```python
def point_line_distance(point: Tuple[float, float],
                        line_start: Tuple[float, float],
                        line_end: Tuple[float, float]) -> float:
def douglas_peucker(points: List[Tuple[float, float]], epsilon: float) -> List[Tuple[float, float]]:
```
### geohash_encode_decode.py
```python
def encode(lat: float, lon: float, precision: int = 6) -> str:
def decode(geohash: str) -> Tuple[float, float, float, float]:
```
### great_circle_waypoints.py
```python
def haversine_dist(lat1: float, lon1: float, lat2: float, lon2: float,
                   radius_km: float = 6371.0) -> float:
def great_circle_waypoints(lat1: float, lon1: float, lat2: float, lon2: float,
                           n_waypoints: int = 5) -> List[Tuple[float, float]]:
```
### grid_density_binning.py
```python
def grid_density_binning(points: List[Tuple[float, float]],
                         grid_size: float) -> Tuple[Dict[Tuple[int, int], int], float, float]:
```
### haversine_bearing.py
```python
def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float,
                       radius_km: float = 6371.0) -> float:
def initial_bearing(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
```
### point_in_polygon.py
```python
def point_in_polygon(point: Tuple[float, float],
                     polygon: List[Tuple[float, float]]) -> bool:
```
### polygon_area_centroid.py
```python
def polygon_area_centroid(vertices: List[Tuple[float, float]]) -> Tuple[float, Tuple[float, float]]:
```
### quadtree_point_index.py
```python
class QuadTree:
def __init__(self, bounds: Tuple[float, float, float, float], max_points: int = 4):
def insert(self, point: Tuple[float, float]) -> bool:
def _subdivide(self):
def range_query(self, bounds: Tuple[float, float, float, float],
                    node_count: List[int]) -> List[Tuple[float, float]]:
```
### spatial_radius_join.py
```python
def spatial_radius_join(points: List[Tuple[float, float]],
                        centers: List[Tuple[float, float]],
                        radius: float,
                        grid_size: float) -> Tuple[List[Tuple[int, int]], int]:
def bucket_key(p: Tuple[float, float]) -> Tuple[int, int]:
```

## information_theory_and_probability
### bayes_diagnostic_test.py
```python
def bayes_diagnostic(
    sensitivity: float,
    specificity: float,
    prevalence: float
) -> Tuple[float, float]:
```
### box_muller_gaussian.py
```python
def box_muller_pair() -> Tuple[float, float]:
def generate_gaussians(n: int) -> List[float]:
def empirical_mean(samples: List[float]) -> float:
def empirical_variance(samples: List[float]) -> float:
def empirical_skewness(samples: List[float]) -> float:
def coverage_percentile(samples: List[float], num_stds: float) -> float:
```
### conjugate_priors.py
```python
def beta_binomial_posterior(
    alpha_prior: float,
    beta_prior: float,
    successes: int,
    failures: int
) -> Tuple[float, float]:
def beta_mean_variance(alpha: float, beta: float) -> Tuple[float, float]:
def normal_normal_posterior_known_variance(
    mu_prior: float,
    sigma2_prior: float,
    sigma2_obs: float,
    observations: List[float]
) -> Tuple[float, float]:
```
### entropy_estimators.py
```python
def true_entropy(probabilities: List[float]) -> float:
def naive_plugin_entropy(samples: List[int]) -> float:
def miller_madow_entropy(samples: List[int]) -> float:
```
### hmm_forward_backward.py
```python
def forward_backward(
    observations: List[int],
    initial_state: List[float],
    transition_matrix: List[List[float]],
    emission_matrix: List[List[float]]
) -> Tuple[float, List[List[float]]]:
def brute_force_likelihood(
    observations: List[int],
    initial_state: List[float],
    transition_matrix: List[List[float]],
    emission_matrix: List[List[float]]
) -> float:
def enumerate_paths(state_seq: List[int], obs_idx: int) -> float:
```
### inverse_transform_sampling.py
```python
def exponential_inverse_cdf(u: float, rate: float) -> float:
def piecewise_inverse_cdf(u: float) -> float:
def sample_from_inverse_transform(
    inverse_cdf: Callable[[float], float],
    n: int
) -> List[float]:
def empirical_mean(samples: List[float]) -> float:
def empirical_variance(samples: List[float]) -> float:
def empirical_quantile(samples: List[float], q: float) -> float:
```
### kl_divergence_cross_entropy.py
```python
def kl_divergence(p: List[float], q: List[float]) -> float:
def cross_entropy(p: List[float], q: List[float]) -> float:
def shannon_entropy(p: List[float]) -> float:
def jensen_shannon_distance(p: List[float], q: List[float]) -> float:
```
### lln_clt_demo.py
```python
def sample_means(source_distribution: List[float], sample_size: int, num_samples: int) -> List[float]:
def empirical_mean(samples: List[float]) -> float:
def empirical_std(samples: List[float]) -> float:
def coverage_percentile(samples: List[float], true_mean: float, num_stds: float) -> float:
def skewness(samples: List[float]) -> float:
```
### markov_chain_stationary.py
```python
def matrix_multiply(v: List[float], P: List[List[float]]) -> List[float]:
def power_iteration_stationary(P: List[List[float]], max_iter: int = 1000, tol: float = 1e-9) -> List[float]:
def verify_stationary(pi: List[float], P: List[List[float]], tol: float = 1e-9) -> bool:
```
### nonlinear_dependence_mi.py
```python
def empirical_mean(samples: List[float]) -> float:
def empirical_std(samples: List[float]) -> float:
def pearson_correlation(x: List[float], y: List[float]) -> float:
def binned_entropy(samples: List[float], num_bins: int = 10) -> float:
def binned_mutual_information(x: List[float], y: List[float], num_bins: int = 10) -> float:
def independent_mutual_information_baseline(x_dist: List[float], y_dist: List[float], num_bins: int = 10) -> float:
```

## linear_algebra
### conjugate_gradient.py
```python
def conjugate_gradient(
    A: list,
    b: list,
    x0: list,
    tol: float = 1e-8,
    max_iter: int = None
) -> list:
```
### gauss_seidel_vs_jacobi.py
```python
def jacobi_iteration(
    A: list,
    b: list,
    x0: list,
    max_iter: int = 100,
    tol: float = 1e-8
) -> Tuple[list, int]:
def gauss_seidel_iteration(
    A: list,
    b: list,
    x0: list,
    max_iter: int = 100,
    tol: float = 1e-8
) -> Tuple[list, int]:
```
### householder_reflection.py
```python
def householder_reflection(
    x: list
) -> Tuple[list, float]:
def apply_householder(H_vector: list, beta: float, x: list) -> list:
```
### jacobi_eigen_symmetric.py
```python
def jacobi_eigen(A: list, max_iter: int = 100, tol: float = 1e-10) -> Tuple[list, list]:
```
### least_squares_qr.py
```python
def qr_gram_schmidt_tall(A: list) -> Tuple[list, list]:
def least_squares_qr(A: list, b: list) -> list:
```
### lu_decomposition_pivoting.py
```python
def lu_decomposition_pivoting(A: list) -> Tuple[list, list, list]:
def matrix_mult(A: list, B: list) -> list:
```
### matrix_condition_number.py
```python
def matrix_norm_frobenius(A: list) -> float:
def matrix_inverse_lu(A: list) -> list:
def condition_number(A: list) -> float:
```
### power_iteration_shifted.py
```python
def power_iteration_shifted(
    A: list,
    shift: float,
    max_iter: int = 100,
    tol: float = 1e-8
) -> Tuple[float, list]:
```
### qr_gram_schmidt.py
```python
def qr_gram_schmidt(A: list) -> Tuple[list, list]:
def matrix_mult(A: list, B: list) -> list:
def matrix_transpose(A: list) -> list:
```
### woodbury_rank1_update.py
```python
def matrix_inverse_lu(A: list) -> list:
def vector_outer_product(u: list, v: list) -> list:
def matrix_add(A: list, B: list) -> list:
def woodbury_update(
    A_inv: list,
    u: list,
    v: list
) -> list:
```

## model_diagnostics
### bias_variance_decomposition.py
```python
def generate_synthetic_data(n: int, seed: int) -> List[Tuple[float, float]]:
def polyfit(x_list: List[float], y_list: List[float], degree: int) -> List[float]:
def evaluate_poly(x: float, coeffs: List[float]) -> float:
def bootstrap_bias_variance(
    train_data: List[Tuple[float, float]],
    test_x: List[float],
    degree: int,
    n_bootstraps: int = 100,
) -> Tuple[float, float, float]:
def test_bias_variance() -> None:
```
### bootstrap_model_comparison.py
```python
def generate_test_data(n: int, seed: int) -> List[Tuple[float, float]]:
def model_a(x: float) -> float:
def model_b(x: float) -> float:
def mean_absolute_error(
    y_true: List[float], y_pred: List[float]
) -> float:
def bootstrap_model_comparison(
    test_data: List[Tuple[float, float]],
    model1: Callable[[float], float],
    model2: Callable[[float], float],
    n_bootstraps: int = 100,
) -> Tuple[int, int, float]:
def test_bootstrap_comparison() -> None:
```
### calibration_curve.py
```python
def generate_well_calibrated_data(n: int, seed: int) -> Tuple[List[float], List[int]]:
def generate_overconfident_data(n: int, seed: int) -> Tuple[List[float], List[int]]:
def calibration_curve(
    scores: List[float], labels: List[int], n_bins: int = 5
) -> Tuple[List[float], List[float], List[float]]:
def brier_score(scores: List[float], labels: List[int]) -> float:
def calibration_error(
    predicted_probs: List[float], observed_freqs: List[float]
) -> float:
def test_calibration() -> None:
```
### gaussian_naive_bayes.py
```python
def generate_gaussian_data(
    n_per_class: int, seed: int
) -> Tuple[List[Tuple[float, float]], List[int]]:
def fit_gaussian_naive_bayes(
    X: List[Tuple[float, float]], y: List[int]
) -> Tuple[List[float], List[List[float]], List[List[float]], List[float]]:
def gaussian_probability(x: float, mean: float, std: float) -> float:
def predict_gaussian_naive_bayes(
    x_sample: Tuple[float, float],
    class_priors: List[float],
    means_per_class: List[List[float]],
    stds_per_class: List[List[float]],
    classes: List[int],
) -> int:
def test_gaussian_naive_bayes() -> None:
```
### learning_curve.py
```python
def generate_linear_data(n: int, seed: int) -> List[Tuple[float, float]]:
def mean_squared_error(y_true: List[float], y_pred: List[float]) -> float:
def fit_constant_model(y_train: List[float]) -> float:
def fit_linear_model(x_train: List[float], y_train: List[float]) -> Tuple[float, float]:
def predict_linear(x_list: List[float], m: float, b: float) -> List[float]:
def learning_curve_analysis() -> None:
```
### lift_gain_chart.py
```python
def generate_scored_labels(
    n_positive: int, n_negative: int, signal_strength: float, seed: int
) -> List[Tuple[float, int]]:
def lift_gain_chart(scores: List[float], labels: List[int], n_deciles: int = 10) -> Tuple[List[float], List[float], List[float]]:
def test_lift_gain() -> None:
```
### precision_recall_curve.py
```python
def generate_scored_labels(
    n_positive: int, n_negative: int, noise: float, seed: int
) -> List[Tuple[float, int]]:
def compute_pr_curve(
    scores: List[float], labels: List[int], n_points: int = 100
) -> Tuple[List[float], List[float], List[float]]:
def average_precision(recalls: List[float], precisions: List[float]) -> float:
def test_precision_recall() -> None:
```
### rank_correlation.py
```python
def rank_data(data: List[float]) -> List[float]:
def spearman_correlation(x: List[float], y: List[float]) -> float:
def kendall_tau(x: List[float], y: List[float]) -> float:
def test_rank_correlation() -> None:
```
### residual_analysis.py
```python
def generate_quadratic_data(n: int, seed: int) -> List[Tuple[float, float]]:
def fit_linear_model(x_list: List[float], y_list: List[float]) -> Tuple[float, float]:
def fit_quadratic_model(
    x_list: List[float], y_list: List[float]
) -> Tuple[float, float, float]:
def compute_residuals(
    x_list: List[float], y_list: List[float], a: float, b: float
) -> List[float]:
def pearson_correlation(u: List[float], v: List[float]) -> float:
def residual_analysis_test() -> None:
```
### ucb_bandit.py
```python
class BernoulliArm:
def __init__(self, success_prob: float):
def draw(self) -> int:
def ucb1_select_arm(counts: List[int], rewards: List[float], c: float = 1.0) -> int:
def run_ucb1_experiment(
    arms: List[BernoulliArm], n_pulls: int, c: float = 1.0
) -> Tuple[List[int], List[float]]:
def test_ucb1() -> None:
```

## model_understanding_and_tuning
### class_weight_imbalance.py
```python
def logistic(z: float) -> float:
def binary_cross_entropy(y: float, pred: float) -> float:
def weighted_binary_cross_entropy(y: float, pred: float, weight: float) -> float:
def train_logistic_classifier(
    X: List[List[float]],
    y: List[float],
    class_weights: Tuple[float, float] = (1.0, 1.0),
    epochs: int = 50
) -> Tuple[float, float]:
def precision_recall(y_true: List[float], y_pred: List[float]) -> Tuple[float, float]:
```
### conformal_prediction_intervals.py
```python
def simple_linear_model(X: List[float], y: List[float]) -> Tuple[float, float]:
def predict(x: float, params: Tuple[float, float]) -> float:
def split_conformal_intervals(
    X_train: List[float],
    y_train: List[float],
    X_cal: List[float],
    y_cal: List[float],
    confidence: float = 0.9
) -> Tuple[float, float]:
def predict_interval(x: float, params: Tuple[float, float], half_width: float) -> Tuple[float, float]:
```
### grid_vs_random_search.py
```python
def evaluate_model(params: Dict[str, float]) -> float:
def grid_search(
    param_ranges: Dict[str, Tuple[float, float]],
    num_values: int = 3
) -> Tuple[Dict[str, float], float, int]:
def grid_enumerate(idx, current_params):
def random_search(
    param_ranges: Dict[str, Tuple[float, float]],
    num_samples: int = 20
) -> Tuple[Dict[str, float], float, int]:
```
### model_persistence_roundtrip.py
```python
class SimpleLinearModel:
def __init__(self, intercept: float = 0.0, weights: List[float] = None):
def predict(self, X: List[List[float]]) -> List[float]:
def to_dict(self) -> Dict[str, Any]:
def from_dict(cls, data: Dict[str, Any]) -> "SimpleLinearModel":
def fit_linear_model(X: List[List[float]], y: List[float]) -> SimpleLinearModel:
```
### partial_dependence_data.py
```python
def train_linear_model(X: List[List[float]], y: List[float]) -> Tuple[float, List[float]]:
def predict(x1: float, x2: float, intercept: float, weights: List[float]) -> float:
def partial_dependence(
    X: List[List[float]],
    intercept: float,
    weights: List[float],
    feat_idx: int,
    x_range: List[float]
) -> List[float]:
def is_monotone_increasing(values: List[float], tolerance: float = 0.1) -> bool:
def is_flat(values: List[float], tolerance: float = 0.5) -> bool:
```
### permutation_feature_importance.py
```python
def train_simple_model(X: List[List[float]], y: List[float]) -> Tuple[float, float, float]:
def predict(X: List[List[float]], coeffs: Tuple[float, float, float]) -> List[float]:
def mse(y_true: List[float], y_pred: List[float]) -> float:
def permutation_importance(
    X_test: List[List[float]], y_test: List[float], coeffs: Tuple[float, float, float]
) -> Tuple[float, float]:
```
### platt_scaling_calibration.py
```python
def logistic(z: float) -> float:
def fit_platt_scaling(scores: List[float], labels: List[float], max_iter: int = 100) -> Tuple[float, float]:
def brier_score(y_true: List[float], y_pred: List[float]) -> float:
def calibration_error(y_true: List[float], y_pred: List[float], n_bins: int = 5) -> float:
```
### shapley_value_sampling.py
```python
def additive_model(features: List[float]) -> float:
def coalition_value(features: List[float], coalition_idx: List[int], baseline: List[float]) -> float:
def shapley_value_sample(
    feature_idx: int,
    num_features: int,
    num_samples: int,
    feature_values: List[float]
) -> float:
def analytic_shapley(feature_idx: int, feature_values: List[float]) -> float:
```
### successive_halving.py
```python
def evaluate_config(config: Dict[str, float], budget: int) -> float:
def successive_halving(
    initial_configs: List[Dict[str, float]],
    initial_budget: int = 10,
    reduction_factor: int = 2
) -> Tuple[Dict[str, float], float]:
```
### threshold_tuning_cost.py
```python
def compute_total_cost(
    y_true: List[float],
    y_scores: List[float],
    threshold: float,
    cost_fp: float = 1.0,
    cost_fn: float = 5.0
) -> float:
def find_optimal_threshold(
    y_true: List[float],
    y_scores: List[float],
    cost_fp: float = 1.0,
    cost_fn: float = 5.0,
    grid_size: int = 100
) -> Tuple[float, float]:
```

## neural_networks_from_scratch
### conv1d_feature_detector.py
```python
def mse_loss(pred: float, target: float) -> float:
class Conv1D:
def __init__(self, kernel_size: int = 3, lr: float = 0.01):
def convolve(self, x: List[float]) -> List[float]:
def backward(self, x: List[float], conv_out: List[float],
                 target_responses: List[float]) -> float:
```
### dropout_regularization_sim.py
```python
def sigmoid(x: float) -> float:
def sigmoid_derivative(s: float) -> float:
class SimpleNetwork:
def __init__(self, hidden_dim: int = 8, use_dropout: bool = False, dropout_rate: float = 0.3):
def forward(self, x: List[float], training: bool = True) -> Tuple[float, List[float], List[bool]]:
def backward(self, x: List[float], y_true: float, y_pred: float, h: List[float], mask: List[bool], lr: float):
def train(self, train_data: List[Tuple[List[float], float]], epochs: int, lr: float) -> float:
def evaluate(self, data: List[Tuple[List[float], float]]) -> Tuple[float, int]:
```
### early_stopping.py
```python
def sigmoid(x: float) -> float:
def sigmoid_derivative(s: float) -> float:
class NetworkWithEarlyStopping:
def __init__(self):
def forward(self, x: List[float]) -> Tuple[float, List[float]]:
def backward(self, x: List[float], y_true: float, y_pred: float, h: List[float], lr: float):
def save_weights(self) -> Tuple[List[List[float]], List[float], List[float], float]:
def restore_weights(self, weights: Tuple[List[List[float]], List[float], List[float], float]):
def train_with_early_stopping(self, train_data: List[Tuple[List[float], float]],
                                   val_data: List[Tuple[List[float], float]],
                                   max_epochs: int = 100, patience: int = 10, lr: float = 0.1) -> Tuple[int, float]:
```
### learning_rate_schedules.py
```python
def sigmoid(x: float) -> float:
def sigmoid_derivative(s: float) -> float:
class SimpleNet:
def __init__(self):
def forward(self, x: List[float]) -> Tuple[float, List[float]]:
def backward(self, x: List[float], y_true: float, y_pred: float, h: List[float], lr: float):
def train(self, data: List[Tuple[List[float], float]], epochs: int,
              lr_schedule: Callable[[int, int], float]) -> Tuple[float, List[float]]:
def constant_lr(epoch: int, total_epochs: int) -> float:
def step_decay_lr(epoch: int, total_epochs: int) -> float:
def cosine_annealing_lr(epoch: int, total_epochs: int) -> float:
```
### mlp_backprop.py
```python
def sigmoid(x: float) -> float:
def sigmoid_derivative(s: float) -> float:
class SimpleMLPBackprop:
def __init__(self, hidden_dim: int = 4, lr: float = 1.0):
def forward(self, x: List[float]) -> Tuple[float, List[float]]:
def backward(self, x: List[float], y_true: float, y_pred: float, h: List[float]):
def train(self, data: List[Tuple[List[float], float]], epochs: int) -> float:
```
### numerical_gradient_check.py
```python
def sigmoid(x: float) -> float:
def sigmoid_derivative(s: float) -> float:
class TinyNetwork:
def __init__(self):
def forward(self, x: List[float]) -> Tuple[float, List[float], List[float]]:
def loss(self, x: List[float], y_true: float) -> float:
def analytic_gradients(self, x: List[float], y_true: float) -> Tuple[List[List[float]], List[float], List[float], float]:
def numerical_gradient(self, x: List[float], y_true: float, param_name: str, param_indices: Tuple[int, ...], eps: float = 1e-5) -> float:
def relative_error(self, analytic: float, numerical: float) -> float:
```
### softmax_regression.py
```python
def softmax(logits: List[float]) -> List[float]:
def cross_entropy(probs: List[float], target_class: int) -> float:
class SoftmaxRegression:
def __init__(self, input_dim: int = 2, num_classes: int = 3, lr: float = 0.01):
def forward(self, x: List[float]) -> Tuple[List[float], List[float]]:
def backward(self, x: List[float], probs: List[float], target_class: int):
def train(self, data: List[Tuple[List[float], int]], epochs: int) -> float:
def predict(self, x: List[float]) -> int:
```
### tiny_autoencoder.py
```python
def sigmoid(x: float) -> float:
def sigmoid_derivative(s: float) -> float:
class TinyAutoencoder:
def __init__(self, input_dim: int = 8, bottleneck_dim: int = 2, lr: float = 0.1):
def encode(self, x: List[float]) -> List[float]:
def decode(self, h: List[float]) -> List[float]:
def forward(self, x: List[float]) -> Tuple[List[float], List[float]]:
def backward(self, x: List[float], h: List[float], recon: List[float]):
def train(self, data: List[List[float]], epochs: int) -> float:
```
### weight_initialization_comparison.py
```python
def sigmoid(x: float) -> float:
def sigmoid_derivative(s: float) -> float:
class DeepNetwork:
def __init__(self, init_scheme: str = "xavier"):
def forward(self, x: List[float]) -> Tuple[float, List[List[float]], List[List[float]]]:
def backward(self, x: List[float], y_true: float, y_pred: float, activations: List[List[float]], preactivations: List[List[float]], lr: float):
def train(self, train_data: List[Tuple[List[float], float]], epochs: int, lr: float) -> Tuple[float, List[float]]:
```
### word2vec_skipgram.py
```python
def sigmoid(x: float) -> float:
def cosine_similarity(v1: List[float], v2: List[float]) -> float:
class SkipgramNegativeSampling:
def __init__(self, vocab_size: int, embedding_dim: int = 8, lr: float = 0.1):
def forward(self, target_word: int, context_word: int) -> float:
def update(self, target_word: int, context_word: int, label: float):
def train_pair(self, target_word: int, context_word: int, negatives: List[int]):
```

## numerical_methods
### adaptive_simpson.py
```python
def simpson_basic(f: Callable[[float], float], a: float, b: float) -> float:
def adaptive_simpson_recursive(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float,
    whole: float,
    depth: int = 0
) -> float:
def adaptive_simpson(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-6
) -> float:
def f_planted(x: float) -> float:
```
### bisection_newton_hybrid.py
```python
def bisection_newton_hybrid(
    f: Callable[[float], float],
    df: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-8,
    max_iter: int = 100
) -> float:
def f_planted(x: float) -> float:
def df_planted(x: float) -> float:
```
### cubic_spline_interpolation.py
```python
def natural_cubic_spline(
    x_data: list,
    y_data: list,
    x_eval: list
) -> list:
```
### euler_vs_rk4_error_order.py
```python
def euler_step(f: Callable[[float, float], float], t: float, y: float, h: float) -> float:
def rk4_step(f: Callable[[float, float], float], t: float, y: float, h: float) -> float:
def solve_to_t_final(
    method: Callable, f: Callable, t0: float, y0: float, t_final: float, h: float
) -> float:
def f_planted(t: float, y: float) -> float:
```
### fixed_point_iteration.py
```python
def fixed_point_iteration(
    g: Callable[[float], float],
    x0: float,
    tol: float = 1e-8,
    max_iter: int = 100
) -> float:
def g_planted(x: float) -> float:
```
### gauss_legendre_quadrature_lite.py
```python
def gauss_legendre_4(f: Callable[[float], float], a: float, b: float) -> float:
def f_planted(x: float) -> float:
```
### richardson_extrapolation.py
```python
def richardson_extrapolate(
    F: Callable[[float], float],
    h: float,
    p: int
) -> float:
def midpoint_rule(f: Callable[[float], float], a: float, b: float, h: float) -> float:
def f_planted(x: float) -> float:
def make_integrator(h: float) -> float:
```
### rk4_ode_solver.py
```python
def rk4_step(
    f: Callable[[float, float], float],
    t: float,
    y: float,
    h: float
) -> float:
def rk4_ode_solver(
    f: Callable[[float, float], float],
    t0: float,
    y0: float,
    t_final: float,
    num_steps: int
) -> Tuple[list, list]:
def f_planted(t: float, y: float) -> float:
```
### romberg_integration.py
```python
def romberg_integration(
    f: Callable[[float], float],
    a: float,
    b: float,
    n: int = 5
) -> float:
def f_planted(x: float) -> float:
```
### secant_method.py
```python
def secant_method(
    f: Callable[[float], float],
    x0: float,
    x1: float,
    tol: float = 1e-8,
    max_iter: int = 100
) -> float:
def f_planted(x: float) -> float:
```

## optimization_and_distances
### distance_metrics_toolkit.py
```python
def euclidean(p: List[float], q: List[float]) -> float:
def manhattan(p: List[float], q: List[float]) -> float:
def minkowski(p: List[float], q: List[float], p_order: float = 2.0) -> float:
def chebyshev(p: List[float], q: List[float]) -> float:
def cosine_similarity(p: List[float], q: List[float]) -> float:
def cosine_distance(p: List[float], q: List[float]) -> float:
```
### dtw_dynamic_time_warping.py
```python
def euclidean_distance(a: float, b: float) -> float:
def dtw_distance(series1: List[float], series2: List[float]) -> Tuple[float, List[Tuple[int, int]]]:
```
### epsilon_greedy_bandit.py
```python
class MultiArmedBandit:
def __init__(self, arm_means: List[float], arm_stds: List[float] = None):
def pull(self, arm: int) -> float:
def run_pure_greedy(self, num_pulls: int = 1000) -> Tuple[float, List[int]]:
def run_epsilon_greedy(
        self, epsilon: float = 0.1, num_pulls: int = 1000
    ) -> Tuple[float, List[int]]:
```
### feature_scaling_toolkit.py
```python
def min_max_scale(data: List[float]) -> Tuple[List[float], float, float]:
def z_score_scale(data: List[float]) -> Tuple[List[float], float, float]:
def robust_scale(data: List[float]) -> Tuple[List[float], float, float]:
def verify_properties(scaled: List[float], name: str, target_mean: float = 0.0, target_std: float = 1.0, allow_mean_tol: float = 1e-10, allow_std_tol: float = 0.05):
```
### genetic_algorithm.py
```python
def bitstring_fitness_onemax(bitstring: List[int]) -> int:
def bitstring_fitness_deceptive(bitstring: List[int]) -> int:
class GeneticAlgorithm:
def __init__(
        self,
        pop_size: int,
        bitstring_length: int,
        fitness_func: Callable[[List[int]], int],
        mutation_rate: float = 0.01,
        generations: int = 100,
    ):
def initialize_population(self):
def evaluate_fitness(self, individual: List[int]) -> int:
def selection_roulette_wheel(self) -> List[int]:
def crossover(self, parent1: List[int], parent2: List[int]) -> List[int]:
def mutate(self, individual: List[int]) -> List[int]:
def evolve(self) -> Tuple[List[int], int]:
```
### gradient_descent_momentum.py
```python
def quadratic_bowl(x: float, y: float) -> float:
def gradient_bowl(x: float, y: float) -> Tuple[float, float]:
def vanilla_gd(
    x: float,
    y: float,
    learning_rate: float = 0.005,
    tolerance: float = 1e-6,
    max_iters: int = 10000,
) -> Tuple[int, float]:
def momentum_gd(
    x: float,
    y: float,
    learning_rate: float = 0.005,
    momentum: float = 0.9,
    tolerance: float = 1e-6,
    max_iters: int = 10000,
) -> Tuple[int, float]:
```
### hill_climbing_restarts.py
```python
def rugged_landscape(x: float, y: float) -> float:
def hill_climbing(
    x: float,
    y: float,
    step_size: float = 0.05,
    tolerance: float = 1e-4,
    max_iters: int = 1000,
) -> Tuple[float, float, float]:
def hill_climbing_with_restarts(
    num_restarts: int = 10,
    step_size: float = 0.05,
    bounds: Tuple[float, float] = (-1.0, 1.0),
) -> Tuple[float, float, float]:
```
### mahalanobis_distance.py
```python
def matrix_multiply_2x2(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
def matrix_invert_2x2(M: List[List[float]]) -> List[List[float]]:
def compute_covariance_2d(points: List[Tuple[float, float]]) -> List[List[float]]:
def mahalanobis_distance(
    point: Tuple[float, float],
    mean: Tuple[float, float],
    cov_inv: List[List[float]],
) -> float:
def euclidean_distance(p: Tuple[float, float], q: Tuple[float, float]) -> float:
```
### newton_method_optimization.py
```python
def quadratic_function(x: float) -> float:
def gradient(x: float) -> float:
def hessian(x: float) -> float:
def newton_method(
    x_init: float, tolerance: float = 1e-10, max_iters: int = 100
) -> Tuple[int, float]:
def gradient_descent(
    x_init: float, learning_rate: float = 0.1, tolerance: float = 1e-10, max_iters: int = 1000
) -> Tuple[int, float]:
```
### simulated_annealing.py
```python
def rastrigin_1d(x: float) -> float:
def rastrigin_2d(x: float, y: float) -> float:
def simulated_annealing(
    x_init: float,
    y_init: float,
    func,
    bounds: Tuple[float, float],
    initial_temp: float = 10.0,
    cooling_rate: float = 0.95,
    max_iters: int = 5000,
) -> Tuple[float, float, float]:
```

## preprocessing_and_eda
### covariance_matrix.py
```python
def covariance_matrix(data: List[List[float]]) -> List[List[float]]:
```
### data_profiling_summary.py
```python
def infer_type(value: Any) -> str:
def profile_column(data: List[Any]) -> Dict[str, Any]:
def profile_dataset(data: List[List[Any]], column_names: List[str] = None) -> Dict[str, Dict]:
```
### histogram_builder.py
```python
def sturges_bin_count(n: int) -> int:
def histogram(data: List[float], n_bins: int = None) -> Tuple[List[int], List[float]]:
```
### missing_value_imputation.py
```python
class MissingValueImputer:
def __init__(self, strategy: str = "mean"):
def fit(self, data: List[Optional[float]]) -> "MissingValueImputer":
def transform(self, data: List[Optional[float]]) -> Tuple[List[float], List[int]]:
def fit_transform(
        self, data: List[Optional[float]]
    ) -> Tuple[List[float], List[int]]:
```
### one_hot_encoding.py
```python
class OneHotEncoder:
def fit(self, data: List[str]) -> "OneHotEncoder":
def transform(self, data: List[str]) -> List[List[int]]:
def fit_transform(self, data: List[str]) -> List[List[int]]:
```
### pearson_correlation_matrix.py
```python
def mean_variance(data: List[float]) -> Tuple[float, float]:
def pearson_correlation(x: List[float], y: List[float]) -> float:
def correlation_matrix(data: List[List[float]]) -> List[List[float]]:
```
### quantile_binning.py
```python
def quantile_binning(data: List[float], n_bins: int) -> List[int]:
def equal_width_binning(data: List[float], n_bins: int) -> List[int]:
```
### random_oversampling_balance.py
```python
def random_oversample(
    X: List[List[float]], y: List[int]
) -> Tuple[List[List[float]], List[int]]:
def smote_lite(
    X: List[List[float]], y: List[int], k: int = 3, alpha_range: Tuple[float, float] = (0.0, 1.0)
) -> Tuple[List[List[float]], List[int]]:
```
### three_way_stratified_split.py
```python
def stratified_split(
    data: List[tuple], labels: List[int], splits: Tuple[float, float, float] = (0.6, 0.2, 0.2)
) -> Tuple[List[tuple], List[tuple], List[tuple], List[int], List[int], List[int]]:
def class_proportion(labels: List[int]) -> dict:
```
### winsorize_clip_outliers.py
```python
def percentile(data: List[float], p: float) -> float:
def winsorize(data: List[float], limits: tuple = (0.05, 0.05)) -> List[float]:
def clip(data: List[float], min_val: float, max_val: float) -> List[float]:
```

## probabilistic_modeling
### bayesian_linear_regression.py
```python
def bayesian_linreg_conjugate(X: List[float], y: List[float],
                              mu0: float = 0.0, sigma0_sq: float = 100.0,
                              sigma_sq: float = 1.0) -> Tuple[float, float]:
```
### bayesian_two_segment_changepoint.py
```python
def log_normal_likelihood(data: List[float], mean: float = None, var: float = 1.0) -> float:
def model_evidence_1seg(data: List[float], var: float = 1.0) -> float:
def model_evidence_2seg(data: List[float], split: int, var: float = 1.0) -> float:
def changepoint_detection(data: List[float], var: float = 1.0) -> Tuple[int, float]:
```
### dirichlet_multinomial.py
```python
def log_gamma(x: float) -> float:
def dirichlet_multinomial_posterior(counts: List[int], alpha_prior: List[float]) -> List[float]:
def dirichlet_multinomial_ll(counts: List[int], alpha_prior: List[float]) -> float:
```
### empirical_bayes_shrinkage.py
```python
def empirical_bayes_shrinkage(groups: List[List[float]]) -> Tuple[List[float], List[float], float]:
```
### gamma_poisson_conjugate.py
```python
def log_gamma_func(x: float) -> float:
def gamma_poisson_posterior(counts: List[int], alpha_prior: float,
                            beta_prior: float) -> Tuple[float, float]:
def gamma_posterior_mean(alpha: float, beta: float) -> float:
def gamma_posterior_var(alpha: float, beta: float) -> float:
def gamma_poisson_ll(counts: List[int], alpha: float, beta: float) -> float:
def poisson_sample(lam: float) -> int:
```
### gaussian_process_lite.py
```python
def rbf_kernel(x1: float, x2: float, length_scale: float = 1.0, sigma: float = 1.0) -> float:
def cholesky_solve_simple(A: List[List[float]], b: List[float]) -> List[float]:
def gp_posterior(X_train: List[float], y_train: List[float],
                 X_test: List[float], noise: float = 0.1,
                 length_scale: float = 1.0) -> Tuple[List[float], List[float]]:
```
### hmm_baum_welch.py
```python
def forward_pass(obs_seq: List[int], pi: List[float], A: List[List[float]],
                 B: List[List[float]]) -> Tuple[List[List[float]], float, List[float]]:
def backward_pass(obs_seq: List[int], A: List[List[float]], B: List[List[float]],
                  scales: List[float]) -> List[List[float]]:
def baum_welch(obs_sequences: List[List[int]], N: int, M: int,
               max_iter: int = 10, seed: int = 7) -> Tuple[List[float], List[List[float]], List[List[float]]]:
def _perturbed_row(size: int) -> List[float]:
def generate_sequence(length: int) -> List[int]:
def perm_error(perm):
```
### particle_filter_1d.py
```python
def particle_filter_step(particles: List[float], weights: List[float],
                         observation: float, process_noise: float = 0.2,
                         obs_noise: float = 0.5) -> Tuple[List[float], List[float], float]:
```
### rejection_sampling.py
```python
def rejection_sample_1d(target_density, proposal_sample, proposal_density,
                       M: float, n_samples: int) -> Tuple[List[float], float]:
def target_density(x: float) -> float:
def proposal_sample() -> float:
def proposal_density(x: float) -> float:
```
### rts_kalman_smoother.py
```python
def kf_forward(observations: List[float], process_var: float = 0.1,
               meas_var: float = 1.0) -> Tuple[List[float], List[float], List[float], List[float]]:
def rts_backward_pass(x_filt: List[float], P_filt: List[float],
                      process_var: float = 0.1) -> Tuple[List[float], List[float]]:
```

## probability_iii
### banach_matchbox_or_gambler_ruin.py
```python
def gamblers_ruin_exact(a: int, b: int, p: float = 0.5) -> float:
def gamblers_ruin_simulate(a: int, b: int, p: float = 0.5, num_sim: int = 1000) -> float:
```
### benford_law_test.py
```python
def benford_expected_frequencies(n: int) -> List[float]:
def leading_digit(x: float) -> int:
def benford_chi_square_test(data: List[float]) -> float:
```
### birthday_paradox_exact_vs_sim.py
```python
def birthday_probability_exact(n: int, days: int = 365) -> float:
def birthday_probability_sim(n: int, days: int = 365, num_sim: int = 10000) -> float:
```
### copula_gaussian_lite.py
```python
def gaussian_copula_sample(rho: float, n: int) -> Tuple[List[float], List[float]]:
def rank_correlation(x: List[float], y: List[float]) -> float:
```
### coupon_collector.py
```python
def harmonic_sum(n: int) -> float:
def coupon_collector_expected(n: int) -> float:
def coupon_collector_simulate(n: int, num_sim: int = 1000) -> float:
```
### extreme_value_block_maxima.py
```python
def fit_gumbel(block_maxima: List[float]) -> Tuple[float, float]:
def gumbel_cdf(x: float, mu: float, sigma: float) -> float:
def gumbel_return_level(T: float, mu: float, sigma: float) -> float:
```
### inclusion_exclusion_derangements.py
```python
def derangements_exact(n: int) -> int:
def derangements_simulate(n: int, num_sim: int = 1000) -> int:
```
### polya_urn_reinforcement.py
```python
def polya_urn_final_proportion(a: int, b: int, num_draws: int = 1000) -> float:
def beta_mean(a: float, b: float) -> float:
def beta_variance(a: float, b: float) -> float:
```
### quantile_mapping_bias_correction.py
```python
def quantile_mapping_correct(data_biased: List[float], data_reference: List[float]) -> List[float]:
```
### stirling_approximation_error.py
```python
def stirling_log_factorial(n: int) -> float:
def exact_log_factorial(n: int) -> float:
```

## rankings_and_information_retrieval
### ab_interleaving.py
```python
def interleave_team_draft(ranking_a: List[str], ranking_b: List[str]) -> List[tuple]:
def simulate_clicks_on_interleaving(
    interleaved: List[tuple],
    relevant_docs: set,
    click_prob_relevant: float = 0.8,
) -> Dict[str, int]:
```
### bm25_ranking.py
```python
def bm25_score(
    query_terms: List[str],
    all_docs: List[List[str]],
    doc_idx: int,
    k1: float = 1.5,
    b: float = 0.75,
) -> float:
def tf_score(query_terms: List[str], doc_terms: List[str]) -> float:
```
### elo_rating.py
```python
def expected_score(elo1: float, elo2: float) -> float:
def update_elo(elo: float, opponent_elo: float, observed_score: float, k: float = 32.0) -> float:
```
### inverted_index_search.py
```python
def build_inverted_index(docs: Dict[str, str]) -> Dict[str, Set[str]]:
def query_and(index: Dict[str, Set[str]], terms: List[str]) -> Set[str]:
def query_or(index: Dict[str, Set[str]], terms: List[str]) -> Set[str]:
```
### mean_reciprocal_rank.py
```python
def reciprocal_rank(ranking: List[int], relevant: Set[int]) -> float:
def mean_reciprocal_rank(rankings: List[List[int]], relevant_sets: List[Set[int]]) -> float:
def precision_at_k(ranking: List[int], relevant: Set[int], k: int) -> float:
def recall_at_k(ranking: List[int], relevant: Set[int], k: int) -> float:
```
### ndcg_evaluation.py
```python
def dcg(relevances: List[float]) -> float:
def ndcg(predicted_relevances: List[float], ideal_relevances: List[float]) -> float:
```
### pairwise_ranking_learn.py
```python
def sigmoid(x: float) -> float:
def fit_logistic_pairwise(
    items: List[str],
    features: List[float],
    true_order: List[str],
) -> Tuple[float, float]:
def kendall_tau(ranking1: List[str], ranking2: List[str]) -> float:
```
### position_bias_click_model.py
```python
def generate_clicks_with_position_bias(
    ranking: List[str],
    true_relevances: Dict[str, float],
    position_bias: float = 2.0,
) -> Dict[str, int]:
def inverse_propensity_weighting(
    clicks: Dict[str, int],
    ranking: List[str],
    position_bias: float = 0.5,
) -> Dict[str, float]:
```
### query_expansion_prf.py
```python
def tf_search(query_terms: List[str], docs: Dict[str, str]) -> List[str]:
def expand_query_prf(
    query_terms: List[str],
    docs: Dict[str, str],
    k: int = 2,
    expansion_terms: int = 3,
) -> List[str]:
```
### rank_fusion_rrf.py
```python
def rrf_score(item: str, rankings: List[List[str]], k: int = 60) -> float:
def rrf_fusion(rankings: List[List[str]], k: int = 60) -> List[str]:
def ndcg_simple(ranking: List[str], ideal_order: List[str]) -> float:
```

## recommenders_and_graph_sampling
### apriori_frequent_itemsets.py
```python
def apriori(
    transactions: List[Set[int]],
    min_support: float = 0.3,
) -> Dict[FrozenSet[int], float]:
def generate_rules(
    frequent_itemsets: Dict[FrozenSet[int], float],
    min_confidence: float = 0.6,
) -> List[Tuple[FrozenSet[int], FrozenSet[int], float]]:
```
### bayesian_ab_beta.py
```python
def bayesian_ab_test(
    successes_a: int,
    trials_a: int,
    successes_b: int,
    trials_b: int,
    prior_alpha: float = 1.0,
    prior_beta: float = 1.0,
    num_samples: int = 10000,
) -> Tuple[float, float, float]:
```
### iqr_outlier_detection.py
```python
def iqr_outliers(data: List[float]) -> Tuple[List[int], float, float, float]:
```
### item_based_cf.py
```python
def adjusted_cosine_similarity(
    item_a: Dict[int, float],
    item_b: Dict[int, float],
    user_means: Dict[int, float],
) -> float:
def recommend_items(
    user_id: int,
    ratings_by_user: Dict[int, Dict[int, float]],
    ratings_by_item: Dict[int, Dict[int, float]],
    k: int = 3,
) -> List[Tuple[int, float]]:
```
### matrix_factorization_sgd.py
```python
def matrix_factorization_sgd(
    ratings: Dict[Tuple[int, int], float],
    num_users: int,
    num_items: int,
    rank: int = 2,
    learning_rate: float = 0.01,
    lambda_reg: float = 0.1,
    epochs: int = 500,
) -> Tuple[Dict[int, Dict[int, float]], Dict[int, Dict[int, float]], float]:
```
### monte_carlo_estimation.py
```python
def estimate_pi(num_samples: int) -> float:
def estimate_integral(
    func: Callable[[float], float],
    a: float,
    b: float,
    num_samples: int,
) -> float:
def quadratic(x: float) -> float:
```
### mutual_information_feature_selection.py
```python
def entropy(values: List[int]) -> float:
def mutual_information(feature: List[int], label: List[int]) -> float:
```
### pagerank_power_iteration.py
```python
def pagerank_power_iteration(
    graph: Dict[int, List[int]],
    damping: float = 0.85,
    tol: float = 1e-6,
    max_iter: int = 100,
) -> Dict[int, float]:
```
### thompson_sampling_bandit.py
```python
def sample_beta(alpha: float, beta: float) -> float:
def thompson_sampling_bandit(
    num_arms: int,
    num_rounds: int,
    true_probabilities: List[float],
) -> Dict[str, float]:
```
### user_based_cf.py
```python
def cosine_similarity(vec_a: Dict[int, float], vec_b: Dict[int, float]) -> float:
def predict_rating(
    user_id: int,
    item_id: int,
    ratings: Dict[int, Dict[int, float]],
    k: int = 3,
) -> float:
```

## recommenders_ii_kept_survivors
### catalog_coverage_diversity.py
```python
def catalog_coverage(recommendations: Iterable[int], catalog_size: int) -> float:
def main() -> None:
```
### content_tfidf_rec.py
```python
def tfidf_similarity(doc1: list, doc2: list) -> float:
```
### intra_list_diversity.py
```python
def intra_list_diversity(items: Sequence[Sequence[float]]) -> float:
def main() -> None:
```
### novelty_serendipity.py
```python
def novelty_score(recommendations: Iterable[int], popularity: Mapping[int, float]) -> float:
def inv_pop(item: int) -> float:
def main() -> None:
```

## signal_processing_and_sequences
### autocovariance_spectrum.py
```python
def autocovariance(signal: List[float], max_lag: int) -> List[float]:
def periodogram_from_acov(acov: List[float]) -> List[float]:
```
### convolution_filtering.py
```python
def convolve(signal: List[float], kernel: List[float]) -> List[float]:
def moving_average_kernel(window_size: int) -> List[float]:
def difference_kernel() -> List[float]:
def mse(x: List[float], y: List[float]) -> float:
```
### cross_correlation_lag.py
```python
def cross_correlation(signal1: List[float], signal2: List[float]) -> List[float]:
```
### discrete_fourier_transform.py
```python
def dft(signal: List[float]) -> List[Tuple[float, float]]:
def magnitude(complex_num: Tuple[float, float]) -> float:
```
### dynamic_range_compression.py
```python
def log_compress(values: List[float], offset: float = 1.0) -> List[float]:
def log_decompress(compressed: List[float], offset: float = 1.0) -> List[float]:
def mu_law_compress(values: List[float], mu: float = 255.0) -> List[float]:
def mu_law_decompress(compressed: List[float], mu: float = 255.0) -> List[float]:
def dynamic_range(values: List[float]) -> float:
```
### fft_cooley_tukey.py
```python
def dft_naive(signal: List[float]) -> List[Tuple[float, float]]:
def fft_cooley_tukey(signal: List[float]) -> List[Tuple[float, float]]:
def count_ops_naive(N: int) -> int:
def count_ops_fft(N: int) -> int:
```
### hampel_filter_outliers.py
```python
def hampel_filter(signal: List[float], window_size: int = 5, k: float = 3.0) -> List[float]:
def mse(x: List[float], y: List[float]) -> float:
```
### peak_detection.py
```python
def find_peaks_prominence(signal: List[float], prominence_threshold: float = 1.0) -> List[int]:
```
### resampling_interpolation.py
```python
def linear_interpolation(signal: List[float], factor: int) -> List[float]:
def nearest_neighbor_interpolation(signal: List[float], factor: int) -> List[float]:
def downsample(signal: List[float], factor: int) -> List[float]:
def rmse(x: List[float], y: List[float]) -> float:
```
### savitzky_golay_lite.py
```python
def fit_polynomial_window(
    window: List[float], poly_order: int = 2
) -> Tuple[float, float, float]:
def savitzky_golay_filter(signal: List[float], window_size: int = 5) -> List[float]:
def moving_average_filter(signal: List[float], window_size: int = 5) -> List[float]:
```

## simulation_and_decision_science
### discrete_event_simulation.py
```python
def discrete_event_simulation() -> None:
```
### kelly_criterion.py
```python
def kelly_criterion() -> None:
def simulate_wealth(fraction: float, n_bets: int, seed_offset: int = 0) -> list[float]:
```
### mm1_queue_littles_law.py
```python
def mm1_queue_littles_law() -> None:
```
### monte_carlo_var_es.py
```python
def monte_carlo_var_es() -> None:
```
### newsvendor_critical_fractile.py
```python
def newsvendor_critical_fractile() -> None:
def profit(order_qty: float, demand: float) -> float:
```
### q_learning_gridworld.py
```python
def q_learning_gridworld() -> None:
def get_neighbors(state: tuple[int, int]) -> list[tuple[int, int]]:
def get_reward(state: tuple[int, int]) -> float:
def state_to_action(state: tuple[int, int], action_idx: int) -> tuple[int, int]:
```
### schelling_segregation.py
```python
def schelling_segregation() -> None:
def get_neighbors(r: int, c: int) -> list[int]:
def is_satisfied(r: int, c: int) -> bool:
def measure_segregation() -> float:
```
### sir_epidemic_model.py
```python
def sir_epidemic_model() -> None:
def simulate_sir(beta: float, gamma: float, n_steps: int = 100) -> tuple[list[int], list[int], list[int]]:
```
### tornado_sensitivity.py
```python
def tornado_sensitivity() -> None:
def profit(price: float, volume: float, cost: float, overhead: float) -> float:
```

## statistical_modeling
### em_two_coins.py
```python
def e_step(
    sessions: List[List[int]],  # 1=heads, 0=tails
    p_a: float,
    p_b: float,
    p_coin_a: float,
) -> Tuple[List[float], List[float]]:
def m_step(
    sessions: List[List[int]],
    posteriors_a: List[float],
    posteriors_b: List[float],
) -> Tuple[float, float]:
def em_two_coins(
    sessions: List[List[int]],
    p_a_init: float = 0.6,
    p_b_init: float = 0.4,
    n_iter: int = 50,
) -> Tuple[float, float]:
```
### gibbs_sampling_bivariate.py
```python
def gibbs_bivariate_normal(
    rho: float,
    n_iter: int,
    initial_x: float = 0.0,
    initial_y: float = 0.0,
) -> Tuple[List[float], List[float]]:
def compute_correlation(x_samples: List[float], y_samples: List[float]) -> float:
```
### importance_sampling.py
```python
def importance_sampling(
    target_pdf: Callable[[float], float],
    proposal_pdf: Callable[[float], float],
    proposal_sample: Callable[[], float],
    h: Callable[[float], float],
    n_samples: int,
) -> Tuple[float, float]:
def target_pdf(x):
def proposal_pdf(x):
def proposal_sample():
def h(x):
```
### kaplan_meier_survival.py
```python
def kaplan_meier(times: List[float], events: List[int]) -> List[Tuple[float, float]]:
def check_kaplan_meier_properties(km_curve: List[Tuple[float, float]]) -> bool:
```
### kernel_density_estimation.py
```python
def silverman_bandwidth(samples: List[float]) -> float:
def gaussian_kernel_density(samples: List[float], x: float, h: float) -> float:
def numeric_integral_kde(samples: List[float], x_min: float, x_max: float, n_grid: int) -> float:
```
### loess_local_regression.py
```python
def tricube_weight(u: float) -> float:
def loess_point(
    x_vals: List[float],
    y_vals: List[float],
    x_target: float,
    frac_nearest: float = 0.3,
) -> float:
def loess_smooth(
    x_vals: List[float],
    y_vals: List[float],
    x_grid: List[float],
    frac_nearest: float = 0.3,
) -> List[float]:
def mean_squared_error(y_true: List[float], y_pred: List[float]) -> float:
```
### metropolis_hastings_mcmc.py
```python
def metropolis_hastings(
    target_pdf: Callable[[float], float],
    proposal_sd: float,
    n_samples: int,
    initial_x: float = 0.0,
) -> Tuple[List[float], float]:
def mixture_target(x: float) -> float:
def gauss(x, mu, sd):
```
### polynomial_regression.py
```python
def gaussian_elimination(A: List[List[float]], b: List[float]) -> List[float]:
def vandermonde_matrix(x_vals: List[float], degree: int) -> List[List[float]]:
def fit_polynomial(x_vals: List[float], y_vals: List[float], degree: int) -> List[float]:
def eval_poly(coeffs: List[float], x: float) -> float:
def mse(y_true: List[float], y_pred: List[float]) -> float:
```
### power_analysis_sample_size.py
```python
def normal_quantile(p: float) -> float:
def normal_cdf_approx(z: float) -> float:
def two_proportion_power(n: int, p1: float, p2: float, alpha: float = 0.05) -> float:
def sample_size_two_proportion(
    p1: float, p2: float, alpha: float = 0.05, target_power: float = 0.80
) -> int:
```
### quantile_regression_pinball.py
```python
def pinball_loss(y: float, pred: float, tau: float) -> float:
def pinball_loss_gradient(y: float, pred: float, tau: float) -> float:
def quantile_regression_linear(
    x_vals: List[float],
    y_vals: List[float],
    tau: float,
    learning_rate: float = 0.01,
    n_iter: int = 1000,
) -> Tuple[float, float]:
def count_below_line(x_vals: List[float], y_vals: List[float], a: float, b: float) -> float:
```

## statistics_and_testing
### ab_test_proportions.py
```python
def ab_test_proportions(conversions_a: int, trials_a: int, conversions_b: int, trials_b: int) -> Tuple[float, float, float]:
def normal_cdf(z):
```
### benjamini_hochberg.py
```python
def benjamini_hochberg(p_values: List[float], alpha: float = 0.05) -> Tuple[List[bool], float]:
```
### bootstrap_confidence_interval.py
```python
def bootstrap_ci(data: List[float], n_boots: int = 10000, ci: float = 0.95) -> Tuple[float, float]:
```
### chi_square_independence.py
```python
def chi_square_independence(contingency_table: List[List[int]]) -> Tuple[float, float, bool]:
```
### confusion_matrix_metrics.py
```python
def confusion_matrix(y_true: List[int], y_pred: List[int]) -> Tuple[int, int, int, int]:
def precision(tp: int, fp: int) -> float:
def recall(tp: int, fn: int) -> float:
def f1_score(precision_val: float, recall_val: float) -> float:
def accuracy(tp: int, tn: int, total: int) -> float:
```
### permutation_test.py
```python
def permutation_test(group_a: List[float], group_b: List[float], n_perms: int = 10000) -> Tuple[float, float]:
```
### reservoir_sampling.py
```python
def reservoir_sample(stream, k: int) -> List:
def verify_uniformity(samples_per_run: List[List], item_count: int) -> bool:
def simple_stream():
def stream():
def tiny_stream():
```
### roc_auc_from_scratch.py
```python
def roc_curve_points(y_true: List[int], y_scores: List[float]) -> List[Tuple[float, float]]:
def auc_from_ranks(y_true: List[int], y_scores: List[float]) -> float:
def auc_trapezoid(roc_points: List[Tuple[float, float]]) -> float:
```
### train_test_split_kfold.py
```python
def train_test_split(data: List, labels: List, test_size: float = 0.2) -> Tuple[List, List, List, List]:
def kfold_split(data: List, labels: List, k: int = 5) -> List[Tuple[List, List, List, List]]:
def simple_mean_predictor(X_train: List, y_train: List) -> float:
def mean_squared_error(y_true: List, y_pred: List) -> float:
```

## streaming_and_sketches
### count_min_sketch.py
```python
class CountMinSketch:
def __init__(self, width: int = 100, depth: int = 5, epsilon: float = 0.01):
def _hash(self, item: str, seed: int) -> int:
def increment(self, item: str, count: int = 1) -> None:
def query(self, item: str) -> int:
def find_heavy_hitters(self, threshold: int) -> List[str]:
```
### online_covariance.py
```python
class OnlineCovarianceEstimator:
def __init__(self, n_vars: int = 2):
def process(self, point: List[float]) -> None:
def get_covariance(self, unbiased: bool = True) -> List[List[float]]:
def get_correlation(self) -> List[List[float]]:
def batch_covariance(data: List[List[float]]) -> List[List[float]]:
```
### online_sgd_classifier.py
```python
def logistic(z: float) -> float:
def online_sgd_classifier(
    stream: List[Tuple[List[float], float]],
    learning_rate: float = 0.01,
    epochs: int = 1
) -> Tuple[List[float], float]:
def batch_sgd_classifier(
    X: List[List[float]],
    y: List[float],
    learning_rate: float = 0.01,
    epochs: int = 10
) -> Tuple[List[float], float]:
```
### p2_quantile_estimator.py
```python
class P2Quantile:
def __init__(self, p: float):
def process(self, x: float) -> None:
def _parabolic(self, i: int, s: int) -> float:
def _linear(self, i: int, s: int) -> float:
def query(self) -> float:
def memory_markers(self) -> int:
```
### page_hinkley_drift.py
```python
class PageHinkleyDrift:
def __init__(self, threshold: float = 50.0, delta: float = 0.005, min_instances: int = 30):
def process(self, value: float) -> bool:
```
### sliding_window_extrema.py
```python
class MonotonicDequeMinMax:
def __init__(self, window_size: int):
def process(self, value: float) -> Tuple[float, float]:
def sliding_window_min_max_bruteforce(data: List[float], window_size: int) -> List[Tuple[float, float]]:
def sliding_window_min_max_deque(data: List[float], window_size: int) -> List[Tuple[float, float]]:
```
### space_saving_heavy_hitters.py
```python
class SpaceSavingTopK:
def __init__(self, k: int = 5):
def process(self, item: str) -> None:
def get_top_k(self) -> List[Tuple[str, int]]:
```
### streaming_histogram_merge.py
```python
class StreamingHistogram:
def __init__(self, max_bins: int = 20):
def process(self, value: float) -> None:
def _merge_adjacent(self) -> None:
def query_quantile(self, p: float) -> float:
def get_bins(self) -> List[Tuple[float, int]]:
```
### streaming_kmeans.py
```python
class StreamingKMeans:
def __init__(self, k: int = 3):
def initialize(self, first_points: List[List[float]]) -> None:
def nearest_centroid(self, point: List[float]) -> int:
def process(self, point: List[float]) -> None:
def get_centroids(self) -> List[List[float]]:
```
### weighted_reservoir_sampling.py
```python
class WeightedReservoirSampler:
def __init__(self, k: int = 5):
def process(self, item: str, weight: float) -> None:
def get_sample(self) -> List[Tuple[str, float]]:
def get_inclusion_freq(self, item: str, total_samples: int) -> float:
```

## streaming_iii
### adwin_drift_detector.py
```python
def _e_cut(n0: int, n1: int, var_w: float, n: int, delta: float) -> float:
def adwin_drift_detector(stream: List[float], delta: float = 0.05) -> Tuple[bool, int]:
```
### bloom_filter_fpr.py
```python
def bloom_filter_fpr(stream: list, size: int = 1000, k: int = 3) -> float:
```
### concept_drift_ensemble.py
```python
def _majority(labels: List[int]) -> int:
def concept_drift_ensemble(y: List[int], window: int = 50):
```
### ddm_error_drift.py
```python
def ddm_error_drift(error_stream: List[int], min_samples: int = 30) -> Tuple[bool, int]:
```
### exponential_histogram_count.py
```python
def dgim_count(stream: List[int], window: int, eps: float = 0.1) -> int:
def _bucket_count(s, w, e):
```
### frugal_streaming_median.py
```python
def frugal_streaming_median(stream: List[float], step: float = 1.0) -> float:
```
### gk_quantile_summary.py
```python
def gk_quantile_summary(stream: List[float], epsilon: float, q: float) -> float:
```
### hoeffding_tree_lite.py
```python
def _entropy(counts: Dict[int, int]) -> float:
def _gain(left: Dict[int, int], right: Dict[int, int]) -> float:
def hoeffding_tree_lite(X, y, thresholds, delta: float = 1e-6):
def make(n):
def stump_acc(f, thr, lp, rp, X, y):
```
### hyperloglog_distinct.py
```python
def _hash64(x) -> int:
def hyperloglog_distinct(stream: List, p: int = 12) -> int:
```
### kswin_drift.py
```python
def kswin_drift(stream: List[float], window_size: int = 100, alpha: float = 0.05) -> bool:
def ks_statistic(w1: List[float], w2: List[float]) -> float:
```
### lossy_counting_frequent.py
```python
def lossy_counting_frequent(stream: list, support: float, eps: float = None) -> Tuple[Set, Dict]:
```
### misra_gries_heavy_hitters.py
```python
def misra_gries_heavy_hitters(stream: list, k: int) -> Dict:
```
### online_bagging_poisson.py
```python
def _poisson1() -> int:
def _new_counts(n_feat, thresholds):
def _add(wc, x, y, w):
def _best_stump(wc, total):
def _predict(stump, x):
def _epred(stumps, x):
def _eacc(stumps, X, y):
def online_bagging_poisson(Xtr, ytr, thresholds, n_models: int = 75):
def make(n, noise):
```
### robust_streaming_mad.py
```python
def robust_streaming_mad(stream: List[float], outlier_idx: set, k: float = 3.5) -> Tuple[int, int, int]:
```
### sliding_window_quantile.py
```python
def sliding_window_quantile(stream: List[float], window_size: int, q: float) -> float:
```
### sliding_window_regression.py
```python
def sliding_window_regression(stream: List[Tuple[float, float]], window_size: int) -> float:
def compute_slope(pairs: List[Tuple]) -> float:
```
### tdigest_lite.py
```python
def _build(sorted_vals: List[float], compression: float) -> List[Tuple[float, int]]:
def tdigest_quantile(centroids: List[Tuple[float, int]], q: float) -> float:
def tdigest_lite(stream: List[float], compression: float = 200.0) -> Tuple[float, float]:
```
### weighted_reservoir_ares.py
```python
def weighted_reservoir_ares(stream: List[Tuple], k: int) -> List:
```
### welford_decayed_moments.py
```python
def welford_decayed_moments(stream: list, decay: float = 0.98) -> Tuple[float, float]:
```
### windowed_distinct_count.py
```python
def windowed_distinct_count(stream: List, window_size: int) -> int:
```

## survival_and_reliability
### accelerated_failure_time_lite.py
```python
def aft_fit(log_times: List[float], x: List[float]) -> Tuple[float, float, float]:
```
### censoring_bias_demo.py
```python
def kaplan_meier_mean(times: List[float], events: List[int]) -> float:
```
### competing_risks_naive_bias.py
```python
def naive_km_cif(times: List[float], events: List[int], event_type: int) -> Tuple[List[float], List[float]]:
def aalen_johansen_cif(times: List[float], events: List[int], event_type: int) -> Tuple[List[float], List[float]]:
```
### cox_partial_likelihood_lite.py
```python
def cox_partial_likelihood_2cov(
    times: List[float],
    events: List[int],
    x1: List[float],
    x2: List[float],
    max_iter: int = 20,
    tol: float = 1e-6
) -> Tuple[float, float]:
```
### exponential_reliability_mtbf.py
```python
def exponential_mtbf(failure_times: List[float]) -> float:
def exponential_survival(t: float, mtbf: float) -> float:
```
### hazard_vs_survival_conversion.py
```python
def hazard_from_survival(
    S: Callable[[float], float],
    t: float,
    eps: float = 1e-6
) -> float:
def survival_from_cumhazard(
    H: Callable[[float], float],
    t: float
) -> float:
def S_planted(t: float) -> float:
def H_planted(t: float) -> float:
```
### log_rank_test.py
```python
def log_rank_test(
    times_g1: List[float],
    events_g1: List[int],
    times_g2: List[float],
    events_g2: List[int]
) -> Tuple[float, float]:
```
### nelson_aalen_cumhazard.py
```python
def nelson_aalen_cumhazard(
    times: List[float],
    events: List[int]
) -> Tuple[List[float], List[float]]:
```
### reliability_series_parallel.py
```python
def reliability_series(component_reliabilities: List[float]) -> float:
def reliability_parallel(component_reliabilities: List[float]) -> float:
def simulate_series(component_reliabilities: List[float], num_sim: int) -> float:
def simulate_parallel(component_reliabilities: List[float], num_sim: int) -> float:
```
### weibull_mle.py
```python
def weibull_mle(times: List[float], max_iter: int = 100, tol: float = 1e-10) -> Tuple[float, float]:
```

## text_nlp
### bag_of_words.py
```python
class BagOfWordsVectorizer:
def __init__(self):
def _tokenize(self, text: str) -> List[str]:
def build_vocabulary(self, documents: List[str]) -> None:
def vectorize(self, text: str) -> Dict[int, int]:
def get_vector_dense(self, text: str) -> List[int]:
def cosine_similarity(vec1: List[int], vec2: List[int]) -> float:
```
### bpe_tokenizer_lite.py
```python
class BPETokenizer:
def __init__(self, vocab_size: int = 100):
def _get_word_frequencies(self, text: str) -> Dict[Tuple[str, ...], int]:
def learn_merges(self, text: str, num_merges: int = None) -> None:
def encode(self, text: str) -> List[int]:
def decode(self, token_ids: List[int]) -> str:
```
### cosine_similarity_search.py
```python
class SimpleSearchEngine:
def __init__(self):
def _tokenize(self, text: str) -> List[str]:
def index(self, documents: List[str]) -> None:
def _get_tfidf_vector(self, text: str) -> Dict[int, float]:
def _cosine_similarity(self, vec1: Dict[int, float], vec2: Dict[int, float]) -> float:
def search(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:
```
### edit_distance.py
```python
class EditDistanceDP:
def distance(s1: str, s2: str) -> int:
def backtrace(s1: str, s2: str) -> List[Tuple[str, str, str]]:
```
### markov_chain_text.py
```python
class MarkovChainText:
def __init__(self, order: int = 1):
def _tokenize(self, text: str) -> List[str]:
def fit(self, documents: List[str]) -> None:
def generate(self, max_length: int = 20, seed_context: Tuple[str, ...] = None) -> str:
def get_transition_counts(self) -> Dict[Tuple[str, ...], Dict[str, int]]:
def sanity_check(self) -> Tuple[bool, str]:
```
### minhash_dedup.py
```python
class MinHashDedup:
def __init__(self, num_hashes: int = 256):
def _tokenize(self, text: str) -> Set[str]:
def _hash_shingle(self, shingle: str, seed: int) -> int:
def compute_signature(self, text: str) -> Tuple[int, ...]:
def fit_signatures(self, documents: List[str]) -> None:
def estimated_jaccard(self, sig1: Tuple[int, ...], sig2: Tuple[int, ...]) -> float:
def exact_jaccard(set1: Set[str], set2: Set[str]) -> float:
def find_similar_pairs(self, threshold: float = 0.5) -> List[Tuple[int, int, float]]:
```
### ngram_language_model.py
```python
class NGramLanguageModel:
def __init__(self, n: int = 2):
def _tokenize(self, text: str) -> List[str]:
def fit(self, documents: List[str]) -> None:
def get_probability(self, context: Tuple[str, ...], token: str) -> float:
def perplexity(self, text: str) -> float:
def sample(self, num_tokens: int = 10, seed_context: Tuple[str, ...] = None) -> str:
```
### rake_keyword_extraction.py
```python
class RAKEExtractor:
def __init__(self, stopwords: Set[str] = None):
def _tokenize(self, text: str) -> List[str]:
def extract_phrases(self, text: str) -> List[List[str]]:
def compute_word_scores(self, phrases: List[List[str]]) -> Dict[str, float]:
def score_phrases(self, phrases: List[List[str]], word_scores: Dict[str, float]) -> List[Tuple[str, float]]:
def extract_keywords(self, text: str, top_k: int = 5) -> List[Tuple[str, float]]:
```
### tfidf_vectorizer.py
```python
class TFIDFVectorizer:
def __init__(self, smooth_idf: bool = True):
def _tokenize(self, text: str) -> List[str]:
def fit(self, documents: List[str]) -> None:
def transform(self, text: str) -> Dict[int, float]:
def get_dense_vector(self, text: str) -> List[float]:
def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
```
### viterbi_hmm.py
```python
class SimpleHMM:
def __init__(self):
def viterbi(self, observations: List[str]) -> Tuple[float, List[str]]:
def brute_force_best_path(self, observations: List[str]) -> Tuple[float, List[str]]:
def enumerate_paths(obs_idx: int, current_seq: List[str], current_log_prob: float):
```

## text_nlp_ii
### char_ngram_language_id.py
```python
def char_bigrams(text: str) -> Dict[str, int]:
def ngram_distance(bigrams1: Dict[str, int], bigrams2: Dict[str, int]) -> float:
```
### naive_bayes_complement.py
```python
class imbalance the log-prior term drags ambiguous documents toward the majority class.
Complement NB (Rennie et al. 2003) scores each class by how POORLY the document fits that
class's COMPLEMENT (all other classes) and assigns to the class with the weakest complement
match — no majority-prior term. Core claim: on imbalanced data CNB is less majority-biased;
it recovers minority documents that vanilla NB misclassifies. Measured accuracy gain.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import List, Tuple, Dict
from collections import defaultdict

def naive_bayes_fit(docs: List[List[str]], labels: List[int]):
def naive_bayes_predict(doc, loglik, logprior, vocab) -> int:
def complement_nb_fit(docs: List[List[str]], labels: List[int]):
def complement_nb_predict(doc, comp_weights, vocab) -> int:
def minority_recall(predict) -> float:
```
### porter_stemmer_lite.py
```python
def porter_stem_lite(word: str) -> str:
```
### sentence_boundary_detection.py
```python
def split_sentences(text: str) -> List[str]:
```
### soundex_phonetic.py
```python
def soundex(name: str) -> str:
```
### textrank_lite.py
```python
def jaccard_similarity(sent1: List[str], sent2: List[str]) -> float:
def textrank_sentences(sentences: List[List[str]], damping: float = 0.85, iterations: int = 50) -> List[float]:
```
### tf_idf_bm25_comparison.py
```python
def tf_idf(docs: List[List[str]], query: List[str]) -> List[float]:
def bm25(docs: List[List[str]], query: List[str], k1: float = 1.5, b: float = 0.75) -> List[float]:
```
### zipf_law_fit.py
```python
def fit_zipf(word_frequencies: List[int]) -> float:
```

## time_series
### autocorrelation_function.py
```python
def acf(series: List[float], nlags: int) -> List[float]:
def significance_bounds(n: int) -> float:
def identify_significant_lags(acf_vals: List[float], n: int) -> List[int]:
```
### autoregressive_model.py
```python
def solve_2x2(a: float, b: float, c: float, d: float, e: float, f: float) -> Tuple[float, float]:
def ar_fit(series: List[float], p: int) -> List[float]:
def ar_forecast_one_step(series: List[float], coeffs: List[float]) -> List[float]:
def compute_mae(actual: List[float], predicted: List[float]) -> float:
```
### cusum_changepoint.py
```python
def cusum_detector(
    series: List[float], target: float, k: float, h: float
) -> Tuple[List[float], List[int]]:
def estimate_mean(series: List[float]) -> float:
```
### differencing_stationarity.py
```python
def first_difference(series: List[float]) -> List[float]:
def augmented_dickey_fuller_simple(series: List[float]) -> float:
def compute_mean_drift(series: List[float], window: int) -> float:
```
### exponential_smoothing.py
```python
def simple_exponential_smoothing(series: List[float], alpha: float) -> List[float]:
def holt_exponential_smoothing(
    series: List[float], alpha: float, beta: float
) -> Tuple[List[float], List[float]]:
def forecast_ses(smoothed: List[float], horizon: int) -> List[float]:
def forecast_holt(level: float, trend: float, horizon: int) -> List[float]:
```
### kalman_filter_1d.py
```python
def kalman_filter_1d(
    observations: List[float],
    process_variance: float,
    measurement_variance: float,
    initial_state: float,
    initial_estimate_error: float,
) -> Tuple[List[float], List[float]]:
def compute_mse(actual: List[float], estimated: List[float]) -> float:
```
### moving_average_smoothing.py
```python
def simple_moving_average(series: List[float], window: int) -> List[float]:
def weighted_moving_average(series: List[float], window: int) -> List[float]:
def compute_variance(series: List[float]) -> float:
```
### rolling_zscore_anomaly.py
```python
def rolling_zscore(series: List[float], window: int, threshold: float = 3.0) -> Tuple[List[float], List[int]]:
```
### seasonal_decomposition.py
```python
def centered_moving_average(series: List[float], window: int) -> List[float]:
def naive_seasonal_decomposition(
    series: List[float], period: int
) -> Tuple[List[float], List[float], List[float]]:
def compute_variance_excluding_none(values: List[float]) -> float:
```
### walk_forward_validation.py
```python
def naive_mean_forecast(train: List[float], steps_ahead: int = 1) -> List[float]:
def naive_last_value_forecast(train: List[float], steps_ahead: int = 1) -> List[float]:
def walk_forward_validation(
    series: List[float],
    initial_window: int,
    forecast_func: Callable[[List[float]], List[float]],
) -> Tuple[List[float], List[float]]:
def compute_mae(actual: List[float], predicted: List[float]) -> float:
```

