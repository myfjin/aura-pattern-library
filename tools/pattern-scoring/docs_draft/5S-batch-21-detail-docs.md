# Batch 21 — DS Pattern Detail Docs (20 patterns)

Categories: `information_theory_and_probability` (10) + `recommenders_and_graph_sampling` (10).

---

## Category: information_theory_and_probability

### 1. bayes_diagnostic_test.py
**Entry fn:** `def bayes_diagnostic(sensitivity: float, specificity: float, prevalence: float) -> Tuple[float, float]:`
**Valid input:** `sensitivity`, `specificity`, `prevalence` are probabilities in [0, 1].
**Core:** Computes Positive Predictive Value (PPV) and Negative Predictive Value (NPV) from test sensitivity/specificity and disease prevalence using Bayes' theorem. Demonstrates that even highly accurate tests yield low PPV when prevalence is low.
**Assert:** At 1% prevalence, 90% sensitivity, 95% specificity, PPV ≈ 0.154; NPV > 0.99. Higher prevalence increases PPV; a perfect test gives PPV = NPV = 1.0.
**⚠️ Defect:** No validation that inputs lie in [0, 1]; invalid probabilities silently propagate through the arithmetic. When `prob_positive` or `prob_negative` is zero the function returns `0.0` rather than raising or returning a meaningful sentinel.

### 2. box_muller_gaussian.py
**Entry fn:** `def box_muller_pair() -> Tuple[float, float]:`, `def generate_gaussians(n: int) -> List[float]:`, `def empirical_mean(samples: List[float]) -> float:`, `def empirical_variance(samples: List[float]) -> float:`, `def empirical_skewness(samples: List[float]) -> float:`, `def coverage_percentile(samples: List[float], num_stds: float) -> float:`
**Valid input:** `n >= 1`; `num_stds >= 0`; samples are numeric.
**Core:** Box-Muller transform maps two independent Uniform(0,1) samples to two independent standard normal samples. The demo verifies mean ≈ 0, variance ≈ 1, skewness ≈ 0, and empirical-rule coverage for 1σ/2σ/3σ bands.
**Assert:** On 10,000 samples (seed 42), |mean| < 0.05, 0.95 < variance < 1.05, |skewness| < 0.1, and ~68%/95%/99.7% coverage within 1/2/3 standard deviations.
**⚠️ Defect:** `box_muller_pair` uses the global `random.random()` with no local seed argument, so reproducibility depends on external seed state. It also discards the second generated value when `n` is odd and clamps `u1` to `1e-10` by arbitrary substitution rather than resampling, slightly distorting the tail.

### 3. conjugate_priors.py
**Entry fn:** `def beta_binomial_posterior(alpha_prior: float, beta_prior: float, successes: int, failures: int) -> Tuple[float, float]:`, `def beta_mean_variance(alpha: float, beta: float) -> Tuple[float, float]:`, `def normal_normal_posterior_known_variance(mu_prior: float, sigma2_prior: float, sigma2_obs: float, observations: List[float]) -> Tuple[float, float]:`
**Valid input:** `alpha_prior`, `beta_prior`, `alpha`, `beta`, `sigma2_prior`, `sigma2_obs` > 0; `successes`, `failures` ≥ 0; `observations` non-empty for meaningful inference.
**Core:** Closed-form Bayesian updates: Beta-Binomial adds successes/failures to prior parameters; Normal-Normal (known variance) combines prior precision with observed data precision to update the posterior mean and variance. Includes sequential-update equivalence checks.
**Assert:** Batch and sequential updates produce identical posterior parameters within 1e-9; more data reduces posterior variance; a strong prior regularizes the posterior toward the prior mean.
**⚠️ Defect:** `normal_normal_posterior_known_variance` does not validate `observations` is non-empty: when empty it sets `obs_mean = 0.0` and `n = 0`, then divides by `precision_post` which is just `precision_prior`, so the result is the prior mean rather than an error. No validation that variances are positive.

### 4. entropy_estimators.py
**Entry fn:** `def true_entropy(probabilities: List[float]) -> float:`, `def naive_plugin_entropy(samples: List[int]) -> float:`, `def miller_madow_entropy(samples: List[int]) -> float:`
**Valid input:** `probabilities` is a valid distribution (sums to 1, non-negative); `samples` is a non-empty list of discrete symbol indices.
**Core:** Estimates Shannon entropy in bits. `true_entropy` computes ground truth from known probabilities. `naive_plugin_entropy` uses empirical frequencies as probabilities. `miller_madow_entropy` adds the standard bias correction `(k - 1)/(2N ln 2)` to reduce small-sample underestimation.
**Assert:** For uniform(4), true entropy = 2.0 bits. On N=20 samples, Miller-Madow is closer to the true entropy than naive plug-in; on N=10,000 both converge to ≈2.0 bits and the correction is small and positive.
**⚠️ Defect:** The estimators do not validate that `samples` is non-empty (empty input returns 0.0). `miller_madow_entropy` uses the number of *observed* symbols `k` rather than the true alphabet size, so the correction is wrong when some symbols are unseen but the alphabet size is known.

### 5. hmm_forward_backward.py
**Entry fn:** `def forward_backward(observations: List[int], initial_state: List[float], transition_matrix: List[List[float]], emission_matrix: List[List[float]]) -> Tuple[float, List[List[float]]]:`, `def brute_force_likelihood(observations: List[int], initial_state: List[float], transition_matrix: List[List[float]], emission_matrix: List[List[float]]) -> float:`, `def enumerate_paths(state_seq: List[int], obs_idx: int) -> float:`
**Valid input:** `initial_state` is a probability vector; `transition_matrix` and `emission_matrix` are stochastic matrices with compatible dimensions; `observations` indices are valid emission columns.
**Core:** Forward-backward algorithm for hidden Markov models: computes log sequence likelihood and smoothed state posteriors `P(state_t | all observations)`. A brute-force likelihood enumerates all state sequences for small verification examples.
**Assert:** Forward-backward likelihood matches brute-force likelihood within 1e-9 on a 2-state toy HMM; smoothed posteriors sum to 1.0 at each step and lie in [0, 1]; strong evidence sequences concentrate posterior mass on the favored state.
**⚠️ Defect:** No validation of matrix/vector dimensions or probability-row sums; malformed matrices raise opaque index errors later. Forward probabilities are stored as raw products, so long sequences can underflow to zero before the final `math.log(sum(...))`, making the reported likelihood `-inf` even when the model is valid.

### 6. inverse_transform_sampling.py
**Entry fn:** `def exponential_inverse_cdf(u: float, rate: float) -> float:`, `def piecewise_inverse_cdf(u: float) -> float:`, `def sample_from_inverse_transform(inverse_cdf: Callable[[float], float], n: int) -> List[float]:`, `def empirical_mean(samples: List[float]) -> float:`, `def empirical_variance(samples: List[float]) -> float:`, `def empirical_quantile(samples: List[float], q: float) -> float:`
**Valid input:** `u` ∈ (0, 1); `rate` > 0; `n > 0`; `q` ∈ [0, 1].
**Core:** Inverse-transform sampling: if `U ~ Uniform(0,1)`, then `X = F^{-1}(U)` follows the target distribution. Includes exponential inverse CDF, a custom piecewise CDF, and sample diagnostics (mean, variance, quantile).
**Assert:** Exponential samples with rate=2 have mean ≈ 0.5 and variance ≈ 0.25; all samples non-negative; median ≈ ln(2)/rate. Piecewise distribution puts ~2/3 of mass on [0,1] and ~1/3 on (1,2], with CDF at x=1 ≈ 2/3.
**⚠️ Defect:** `empirical_quantile` uses `sorted_samples[int(q * len(sorted_samples))]`, a crude nearest-rank estimator with no interpolation, so quantile estimates are coarse for small `n`. `piecewise_inverse_cdf` is hardcoded to a single distribution and cannot be reused for other piecewise CDFs.

### 7. kl_divergence_cross_entropy.py
**Entry fn:** `def kl_divergence(p: List[float], q: List[float]) -> float:`, `def cross_entropy(p: List[float], q: List[float]) -> float:`, `def shannon_entropy(p: List[float]) -> float:`, `def jensen_shannon_distance(p: List[float], q: List[float]) -> float:`
**Valid input:** `p` and `q` are valid, equal-length discrete probability distributions.
**Core:** Information-theoretic divergences: KL divergence `D(p||q)`, cross-entropy `H(p,q)`, Shannon entropy `H(p)`, and symmetric Jensen-Shannon distance (square root of JS divergence). Verifies identities and hand-computed examples.
**Assert:** `KL(p||p) = 0`; `H(p,q) = H(p) + D(p||q)`; JS distance is symmetric and bounded in [0, 1]; hand-computed 2-point example matches within 1e-9.
**⚠️ Defect:** No validation that inputs are valid probability distributions (non-negative and sum to 1). If `q[i] = 0` while `p[i] > 1e-10`, the code raises `ZeroDivisionError` rather than returning `+inf` or a clean error. The `1e-10` threshold is arbitrary and can silently drop mass from near-zero probabilities.

### 8. lln_clt_demo.py
**Entry fn:** `def sample_means(source_distribution: List[float], sample_size: int, num_samples: int) -> List[float]:`, `def empirical_mean(samples: List[float]) -> float:`, `def empirical_std(samples: List[float]) -> float:`, `def coverage_percentile(samples: List[float], true_mean: float, num_stds: float) -> float:`, `def skewness(samples: List[float]) -> float:`
**Valid input:** `source_distribution` non-empty; `sample_size`, `num_samples` ≥ 1; `true_mean` numeric.
**Core:** Demonstrates the Law of Large Numbers (sample mean converges to population mean as `n` grows) and the Central Limit Theorem (distribution of sample means becomes normal, satisfying the empirical rule, regardless of skewed source). Uses an exponential source distribution.
**Assert:** Final error across `n = 10, 50, 100, 500` decreases (LLN); skewness of sample means decreases as `n` increases (CLT); for `n=500`, 1σ coverage ≈ 68%, 2σ ≈ 95%, 3σ ≈ 99.7%.
**⚠️ Defect:** `sample_means` draws with replacement from a finite empirical pool rather than from the true distribution, so it reuses the same tail events and is not an independent-sample CLT demo. `coverage_percentile` uses the *sample* standard deviation, not the known population standard deviation, which mixes sampling error into the coverage check.

### 9. markov_chain_stationary.py
**Entry fn:** `def matrix_multiply(v: List[float], P: List[List[float]]) -> List[float]:`, `def power_iteration_stationary(P: List[List[float]], max_iter: int = 1000, tol: float = 1e-9) -> List[float]:`, `def verify_stationary(pi: List[float], P: List[List[float]], tol: float = 1e-9) -> bool:`
**Valid input:** `P` is a square, row-stochastic transition matrix (rows sum to 1); `max_iter` ≥ 1; `tol` > 0.
**Core:** Computes the stationary distribution π of an ergodic Markov chain via power iteration (repeated left multiplication π ← πP) and verifies πP ≈ π. Also shows that different starting distributions converge to the same π.
**Assert:** For the 2-state chain `[[0.7,0.3],[0.4,0.6]]`, computed π matches analytical `[4/7, 3/7]` within 1e-6 and satisfies `verify_stationary`. Symmetric 3-state chain converges to uniform; arbitrary 4-state chain produces a valid stationary distribution.
**⚠️ Defect:** No validation that `P` is square, non-negative, or row-stochastic; malformed inputs produce silent wrong results or `RuntimeError` after `max_iter`. The function raises `RuntimeError` on non-convergence but does not report the final residual, making diagnosis harder.

### 10. nonlinear_dependence_mi.py
**Entry fn:** `def empirical_mean(samples: List[float]) -> float:`, `def empirical_std(samples: List[float]) -> float:`, `def pearson_correlation(x: List[float], y: List[float]) -> float:`, `def binned_entropy(samples: List[float], num_bins: int = 10) -> float:`, `def binned_mutual_information(x: List[float], y: List[float], num_bins: int = 10) -> float:`, `def independent_mutual_information_baseline(x_dist: List[float], y_dist: List[float], num_bins: int = 10) -> float:`
**Valid input:** `x` and `y` are equal-length numeric lists; `num_bins` ≥ 2.
**Core:** Compares Pearson correlation (linear) against binned mutual information (any dependence). Shows that for `y = x² + noise` with symmetric `x`, Pearson ≈ 0 while MI is high; both are high for linear dependence; both are low for independent noise.
**Assert:** For `y = x²`, |Pearson| < 0.15 and MI > 1.0 bits; for `y = 2x + noise`, Pearson > 0.95 and MI > 1.0; shuffled baseline MI < 0.2.
**⚠️ Defect:** Bin edges are derived from sample min/max, so a single outlier can compress the binning of the bulk and distort MI. `binned_mutual_information` returns `max(mi, 0.0)`, which hides negative numerical artifacts but also masks genuine implementation errors. Pearson correlation uses population denominator for the third moment but sample denominator for the standard deviation.

---

## Category: recommenders_and_graph_sampling

### 11. apriori_frequent_itemsets.py
**Entry fn:** `def apriori(transactions: List[Set[int]], min_support: float = 0.3,) -> Dict[FrozenSet[int], float]:`, `def generate_rules(frequent_itemsets: Dict[FrozenSet[int], float], min_confidence: float = 0.6,) -> List[Tuple[FrozenSet[int], FrozenSet[int], float]]:`
**Valid input:** `transactions` non-empty list of non-empty item sets; `0 <= min_support <= 1`; `0 <= min_confidence <= 1`.
**Core:** Apriori algorithm: counts 1-itemsets, iteratively joins frequent `(k-1)`-itemsets to form candidate `k`-itemsets, filters by minimum support, then generates association rules with confidence ≥ `min_confidence`.
**Assert:** Planted itemset `{0,1}` appears in the frequent itemsets at min_support 0.3; at least one rule is generated; rules involving the planted itemset are found.
**⚠️ Defect:** Candidate generation joins *all* pairs of frequent itemsets (O(|F|²)) and does not prune using the downward-closure property before the expensive support-counting pass. `generate_rules` computes confidence from antecedent support but never checks that the consequent itself is frequent, so it can emit rules for itemsets that did not pass the support threshold.

### 12. bayesian_ab_beta.py
**Entry fn:** `def bayesian_ab_test(successes_a: int, trials_a: int, successes_b: int, trials_b: int, prior_alpha: float = 1.0, prior_beta: float = 1.0, num_samples: int = 10000,) -> Tuple[float, float, float]:`
**Valid input:** `0 <= successes_a <= trials_a`, `0 <= successes_b <= trials_b`; `trials_a`, `trials_b`, `num_samples` > 0; `prior_alpha`, `prior_beta` > 0.
**Core:** Bayesian A/B testing with Beta-Binomial posteriors. Updates Beta priors with observed successes/failures, then estimates `P(B > A)`, and posterior mean rates via sampling.
**Assert:** When B has higher observed rate (65/100 vs 60/100), `P(B > A) > 0.5`, posterior mean B > posterior mean A, and with the planted gap `P(B > A) > 0.7`.
**⚠️ Defect:** Posterior sampling uses `random.gauss(alpha/(alpha+beta), 0.05)` clamped to [0,1] instead of drawing from the actual Beta distribution, so uncertainty estimates and `P(B>A)` can be inaccurate, especially for small samples. No validation that `successes <= trials` or that counts are non-negative.

### 13. iqr_outlier_detection.py
**Entry fn:** `def iqr_outliers(data: List[float]) -> Tuple[List[int], float, float, float]:`
**Valid input:** `data` is a numeric list.
**Core:** Flags values outside `[Q1 - 1.5*IQR, Q3 + 1.5*IQR]` as outliers. Returns indices of flagged points plus Q1, Q3, and IQR.
**Assert:** Injected extreme outliers (`-50`, `250`) in a Gaussian centered at 100 are detected; clean Gaussian data yields fewer than 5 detections.
**⚠️ Defect:** Q1 and Q3 are computed using simple nearest-rank indices (`n//4` and `3*n//4`) rather than standard interpolation methods, so quartile boundaries can be off by one or more bins. The function returns `(Q1=0, Q3=0, IQR=0)` for fewer than 4 points instead of raising or returning `None`, which hides the "not enough data" condition.

### 14. item_based_cf.py
**Entry fn:** `def adjusted_cosine_similarity(item_a: Dict[int, float], item_b: Dict[int, float], user_means: Dict[int],) -> float:`, `def recommend_items(user_id: int, ratings_by_user: Dict[int, Dict[int, float]], ratings_by_item: Dict[int, Dict[int, float]], k: int = 3,) -> List[Tuple[int, float]]:`
**Valid input:** `ratings_by_user` and `ratings_by_item` are consistent views of the same rating matrix; `user_id` present in `ratings_by_user`; `k >= 1`.
**Core:** Item-based collaborative filtering with adjusted cosine similarity. Normalizes ratings by subtracting per-user means, computes similarity between item rating vectors, and recommends top-k unseen items weighted by similarity to the user's rated items.
**Assert:** For a small synthetic rating matrix, recommendations are generated, no already-rated item is recommended, and at least one unseen item appears in the top-k list.
**⚠️ Defect:** `adjusted_cosine_similarity` returns 0.0 when items have no common raters, giving them no chance to be recommended even if global popularity would be a sensible fallback. `recommend_items` can return an empty list for users with no similarity to any unseen item, and there is no cold-start default.

### 15. matrix_factorization_sgd.py
**Entry fn:** `def matrix_factorization_sgd(ratings: Dict[Tuple[int, int], float], num_users: int, num_items: int, rank: int = 2, learning_rate: float = 0.01, lambda_reg: float = 0.1, epochs: int = 500,) -> Tuple[Dict[int, Dict[int, float]], Dict[int, Dict[int, float]], float]:`
**Valid input:** `ratings` maps `(user, item)` → rating; `num_users`, `num_items`, `rank`, `epochs` > 0; `learning_rate`, `lambda_reg` > 0; all user/item IDs in `ratings` are within declared ranges.
**Core:** Stochastic gradient descent matrix factorization: learns user and item latent factor matrices to minimize squared reconstruction error on observed ratings plus L2 regularization. Returns final user factors, item factors, and training RMSE.
**Assert:** On a synthetic rank-2 rating matrix with small noise, final RMSE < 0.5 after 500 epochs.
**⚠️ Defect:** The SGD pass iterates over `ratings.items()` in insertion order with no shuffling, so the update trajectory is deterministic and can converge slowly or to a suboptimal ordering-sensitive minimum. There are no user/item bias terms, so global rating shifts must be absorbed into the latent factors. The returned RMSE is training RMSE, not a held-out metric.

### 16. monte_carlo_estimation.py
**Entry fn:** `def estimate_pi(num_samples: int) -> float:`, `def estimate_integral(func: Callable[[float], float], a: float, b: float, num_samples: int,) -> float:`, `def quadratic(x: float) -> float:`
**Valid input:** `num_samples` > 0; `a < b`; `func` defined on `[a, b]`.
**Core:** Monte Carlo estimation: `estimate_pi` samples points in the unit square and counts those inside the quarter circle; `estimate_integral` averages function values over `[a,b]` scaled by interval width.
**Assert:** Error for pi decreases as samples increase from 1,000 to 10,000; 10,000-sample estimate is within 0.1 of π. Integral of `x²` on [0,1] is within 0.05 of 1/3 with 10,000 samples and error decreases with more samples.
**⚠️ Defect:** `estimate_pi` only covers the first quadrant of the unit circle, so it estimates π/4 and multiplies by 4; this is correct but restricts the method to that geometry. There is no validation that `num_samples > 0` or `a < b`; invalid inputs can raise or return nonsensical values. Random state is shared globally, so repeated calls are not independent unless seeded externally.

### 17. mutual_information_feature_selection.py
**Entry fn:** `def entropy(values: List[int]) -> float:`, `def mutual_information(feature: List[int], label: List[int]) -> float:`
**Valid input:** `feature` and `label` are equal-length lists of discrete integer class labels; at least one feature value and one label value.
**Core:** Ranks discrete features by mutual information with the target label. Computes `I(X;Y) = H(Y) - H(Y|X)` using frequency-based entropy; informative features score higher than noise.
**Assert:** A feature with 80% agreement with the label has higher MI than a random-noise feature; a feature with 60% agreement beats an independent noise feature.
**⚠️ Defect:** Only handles discrete integer features; continuous features must be binned externally. No smoothing is applied, so feature values that appear only once contribute zero conditional entropy and can inflate MI. No length-check between `feature` and `label`; silent truncation could occur if the caller passes mismatched lists.

### 18. pagerank_power_iteration.py
**Entry fn:** `def pagerank_power_iteration(graph: Dict[int, List[int]], damping: float = 0.85, tol: float = 1e-6, max_iter: int = 100,) -> Dict[int, float]:`
**Valid input:** `graph` is a non-empty adjacency list of outgoing neighbors; `0 <= damping <= 1`; `tol` > 0; `max_iter` > 0.
**Core:** PageRank via power iteration: each node distributes its score uniformly to outgoing neighbors, with damping factor teleportation to all nodes and special handling of dangling nodes (nodes with no out-edges).
**Assert:** Ranks sum to ≈1; all ranks positive; the hub node with multiple inbound links ranks above the mean in the planted graph.
**⚠️ Defect:** Dangling-node mass is redistributed equally to all nodes, which is one valid convention, but the code does not document or validate this choice. `max_iter=100` may be insufficient for some graphs, and the function silently returns the last iterate without indicating non-convergence.

### 19. thompson_sampling_bandit.py
**Entry fn:** `def sample_beta(alpha: float, beta: float) -> float:`, `def thompson_sampling_bandit(num_arms: int, num_rounds: int, true_probabilities: List[float],) -> Dict[str, float]:`
**Valid input:** `num_arms` > 0; `len(true_probabilities) == num_arms`; each true probability in [0, 1]; `num_rounds` > 0.
**Core:** Thompson sampling for multi-armed bandits: maintains Beta posteriors over each arm's success probability, samples each posterior, pulls the arm with the highest sample, and performs a Bayesian update. Balances exploration and exploitation online.
**Assert:** On a three-arm bandit with true probabilities [0.8, 0.6, 0.4] over 1,000 rounds, the best arm is pulled more often than the worst arm, and cumulative reward exceeds a random policy.
**⚠️ Defect:** `sample_beta` approximates Beta sampling with a Gaussian `random.gauss(alpha/(alpha+beta), 0.1)` clamped to [0,1], which is not a true Beta distribution and can be very wrong for small `alpha`, `beta`. No validation that `num_arms` matches `len(true_probabilities)` or that probabilities are in [0,1]; invalid probabilities silently produce deterministic or clipped behavior.

### 20. user_based_cf.py
**Entry fn:** `def cosine_similarity(vec_a: Dict[int, float], vec_b: Dict[int, float]) -> float:`, `def predict_rating(user_id: int, item_id: int, ratings: Dict[int, Dict[int, float]], k: int = 3,) -> float:`
**Valid input:** `ratings` is a non-empty user×item rating matrix; `user_id` and `item_id` are keys (or at least `user_id` is present); `k >= 1`; ratings are numeric.
**Core:** User-based collaborative filtering: predicts a rating for `(user_id, item_id)` as a similarity-weighted average of the ratings of the `k` most similar users who rated that item. Cosine similarity is computed on sparse user rating vectors.
**Assert:** For a held-out planted rating, the predicted value is within 1.5 of the true rating in the synthetic example.
**⚠️ Defect:** Cosine similarity treats missing ratings as 0 rather than as unknown, so a user with few ratings can appear artificially similar to another sparse user. No mean-centering of ratings, so users with different base rates are compared on raw scale. If no neighbor has rated the item, the function returns a hardcoded default 2.5 with no indication of confidence or cold-start.
