# Batch 24 — DS Pattern Detail Docs (19 patterns)

Categories: `statistics_and_testing` (9) + `streaming_and_sketches` (10). True final batch of the Python DS sphere.

---

## Category: statistics_and_testing

### 1. ab_test_proportions.py
**Entry fn:** `def ab_test_proportions(conversions_a: int, trials_a: int, conversions_b: int, trials_b: int) -> Tuple[float, float, float]:`, `def normal_cdf(z):`
**Valid input:** Non-negative integer counts with `0 <= conversions_a <= trials_a`, same for group B, and at least some successes or failures so the pooled proportion is defined.
**Core:** Two-proportion z-test. Computes a pooled standard error under the null, the z-statistic, an approximate two-tailed p-value via a Hart/Abramowitz & Stegun normal CDF, and Cohen's h effect size.
**Assert:** On two roughly equal conversion rates (10/100 vs 11/100), the p-value is above 0.05; on a planted 15% vs 10% split (30/200 vs 15/200), the p-value is below 0.05 and Cohen's h is non-negligible.
**⚠️ Defect:** `normal_cdf` is nested inside `ab_test_proportions`, so it is not reusable or independently testable. Cohen's h formula divides the arcsin difference by 2, which is non-standard (the standard definition omits that final division by 2). No validation of zero trials; a `ZeroDivisionError` propagates rather than returning a controlled result.

### 2. benjamini_hochberg.py
**Entry fn:** `def benjamini_hochberg(p_values: List[float], alpha: float = 0.05) -> Tuple[List[bool], float]:`
**Valid input:** `p_values` is a list of floats in [0, 1]; `alpha` is a float in (0, 1].
**Core:** Benjamini-Hochberg FDR procedure. Sorts p-values, finds the largest rank where `p_i <= (i/m) * alpha`, and rejects all hypotheses up to that rank.
**Assert:** A uniform null set of 10 p-values yields very few rejections; a mixed set of small planted signals yields several rejections and the three smallest p-values are rejected; a large 1000-test scenario with 50 true effects detects most true effects while keeping total rejections bounded.
**⚠️ Defect:** The BH procedure assumes independent or positively-correlated tests; this is not verified or documented. The returned `threshold` is the last accepted p-value, which is BH-correct but the function does not enforce the standard "adjusted p-value" semantics.

### 3. bootstrap_confidence_interval.py
**Entry fn:** `def bootstrap_ci(data: List[float], n_boots: int = 10000, ci: float = 0.95) -> Tuple[float, float]:`
**Valid input:** `data` is a non-empty list of numbers; `n_boots` > 0; `ci` ∈ (0, 1).
**Core:** Non-parametric percentile bootstrap for the sample mean. Resamples the observed data with replacement many times, computes the mean of each resample, sorts the bootstrap means, and returns the quantile-based confidence interval.
**Assert:** For a seeded normal sample with true mean 100, the 95% CI contains 100, has positive width, and the width is reasonably small.
**⚠️ Defect:** Uses a fixed percentile method rather than bias-corrected or accelerated intervals, so skewed data can produce poor coverage. The quantile indices are computed with `int()` truncation, which can underestimate coverage for small `n_boots` and extreme `ci`.

### 4. chi_square_independence.py
**Entry fn:** `def chi_square_independence(contingency_table: List[List[int]]) -> Tuple[float, float, bool]:`
**Valid input:** `contingency_table` is a non-empty rectangular matrix of non-negative integers with non-zero grand total.
**Core:** Pearson chi-square test of independence. Computes expected cell counts from row and column marginals, sums `(observed - expected)^2 / expected`, and compares to a hardcoded critical-value table for alpha=0.05.
**Assert:** A balanced, independent 2×3 table is not significant; a diagonal-dominant 2×3 table is significant.
**⚠️ Defect:** The p-value is only a rough approximation (0.05 if significant, 0.95 otherwise) rather than a real chi-square CDF computation. The critical-value table covers df 1–10; tables outside that range use a default df=1 critical value, which is wrong for larger tables.

### 5. confusion_matrix_metrics.py
**Entry fn:** `def confusion_matrix(y_true: List[int], y_pred: List[int]) -> Tuple[int, int, int, int]:`, `def precision(tp: int, fp: int) -> float:`, `def recall(tp: int, fn: int) -> float:`, `def f1_score(precision_val: float, recall_val: float) -> float:`, `def accuracy(tp: int, tn: int, total: int) -> float:`
**Valid input:** `y_true` and `y_pred` are equal-length lists of binary labels (0 or 1); metric denominators are handled with zero-guard returns.
**Core:** Computes TP, FP, TN, FN for binary classification, then precision, recall, F1, and accuracy from those counts.
**Assert:** Perfect predictions yield (3, 0, 3, 0) and all metrics equal 1.0; a planted imperfect case yields the expected confusion counts and intermediate metric values between 0 and 1.
**⚠️ Defect:** No validation that `y_true` and `y_pred` have the same length or that labels are binary, so mismatched/invalid inputs silently produce nonsensical counts. The function signature takes pre-aggregated counts for metrics, so callers must separately compute TP/FP/TN/FN; this is error-prone.

### 6. permutation_test.py
**Entry fn:** `def permutation_test(group_a: List[float], group_b: List[float], n_perms: int = 10000) -> Tuple[float, float]:`
**Valid input:** Both groups are non-empty lists of numbers.
**Core:** Two-sample permutation test for the difference of means. Shuffles the pooled data, splits at the original group-A size, recomputes the mean difference, and estimates a two-tailed p-value by the fraction of permutations with absolute difference at least as large as observed.
**Assert:** Two samples from the same normal distribution produce a high p-value; a sample shifted by +5 produces a low p-value.
**⚠️ Defect:** The exact permutation distribution is only approximated by random shuffling; the p-value can vary noticeably across runs for borderline cases. The function recomputes `len(group_b)` inside the loop unnecessarily but this is minor.

### 7. reservoir_sampling.py
**Entry fn:** `def reservoir_sample(stream, k: int) -> List:`, `def verify_uniformity(samples_per_run: List[List], item_count: int) -> bool:`, `def simple_stream():`, `def stream():`, `def tiny_stream():`
**Valid input:** `stream` is any iterable; `k` is a positive integer.
**Core:** Algorithm R reservoir sampling: keeps a reservoir of size `k`; the i-th item (0-indexed) replaces a random reservoir element with probability `k/(i+1)`.
**Assert:** Sampling 5 from 20 yields 5 unique in-range items; 50 runs of 10 from 100 pass a uniformity check; sampling more than the stream length returns all available items.
**⚠️ Defect:** The `verify_uniformity` helper expects `item_count` distinct IDs and declares success if at least 70% of observed counts fall within a factor of 2 of expected — this is a weak statistical test. The helper stream generators are defined in the main block and are not generally reusable.

### 8. roc_auc_from_scratch.py
**Entry fn:** `def roc_curve_points(y_true: List[int], y_scores: List[float]) -> List[Tuple[float, float]]:`, `def auc_from_ranks(y_true: List[int], y_scores: List[float]) -> float:`, `def auc_trapezoid(roc_points: List[Tuple[float, float]]) -> float:`
**Valid input:** `y_true` and `y_scores` are equal-length lists; `y_true` is binary.
**Core:** Computes ROC curve points (FPR, TPR) by sorting scores descending, then computes AUC either via the Mann-Whitney U rank statistic or the trapezoid rule over the ROC points.
**Assert:** Perfectly separable scores yield AUC ≈ 1 by both methods; weak and strong signal cases produce moderate/high AUC within expected ranges.
**⚠️ Defect:** `auc_from_ranks` uses a double loop, so it is O(n²) and impractical for large datasets. `roc_curve_points` does not include explicit threshold values in its output, and the degenerate cases (no positives or no negatives) return hardcoded `(0,0),(1,1)` or 0.5 without warning.

### 9. train_test_split_kfold.py
**Entry fn:** `def train_test_split(data: List, labels: List, test_size: float = 0.2) -> Tuple[List, List, List, List]:`, `def kfold_split(data: List, labels: List, k: int = 5) -> List[Tuple[List, List, List, List]]:`, `def simple_mean_predictor(X_train: List, y_train: List) -> float:`, `def mean_squared_error(y_true: List, y_pred: List) -> float:`
**Valid input:** `data` and `labels` are equal-length lists; `0 < test_size < 1`; `k` is a positive integer dividing the dataset reasonably.
**Core:** Random train/test split and k-fold cross-validation split, plus a trivial mean predictor and MSE helper used for the demo assertions.
**Assert:** Train and test sizes match requested fractions; each fold partitions the full dataset; 5-fold CV runs without error and yields a positive, reasonable MSE.
**⚠️ Defect:** `kfold_split` does not stratify by label, so imbalanced classes may end up with folds lacking some classes. `simple_mean_predictor` ignores features entirely and will be a poor baseline for any real task. The last fold greedily absorbs the remainder indices, which can make fold sizes unbalanced.

---

## Category: streaming_and_sketches

### 10. count_min_sketch.py
**Entry fn:** `class CountMinSketch:`, `def __init__(self, width: int = 100, depth: int = 5, epsilon: float = 0.01):`, `def _hash(self, item: str, seed: int) -> int:`, `def increment(self, item: str, count: int = 1) -> None:`, `def query(self, item: str) -> int:`, `def find_heavy_hitters(self, threshold: int) -> List[str]:`
**Valid input:** `item` is a string; `count` is a positive integer; `width`, `depth` are positive integers; `epsilon` is a small positive float.
**Core:** Streaming Count-Min Sketch with `depth` independent MD5 hash functions over a `width × depth` counter table. Provides frequency upper bounds and a heavy-hitter scan.
**Assert:** Estimated counts for planted heavy hitters are at least their true counts and within the claimed epsilon error bound; total stream length is tracked implicitly.
**⚠️ Defect:** `find_heavy_hitters` scans raw cell counts rather than querying known keys, so it returns integer counts instead of item identifiers. The class stores `epsilon` but does not use it to size the table automatically. MD5 hashing is overkill for a non-cryptographic frequency sketch.

### 11. online_covariance.py
**Entry fn:** `class OnlineCovarianceEstimator:`, `def __init__(self, n_vars: int = 2):`, `def process(self, point: List[float]) -> None:`, `def get_covariance(self, unbiased: bool = True) -> List[List[float]]:`, `def get_correlation(self) -> List[List[float]]:`, `def batch_covariance(data: List[List[float]]) -> List[List[float]:`
**Valid input:** `point` is a list of length `n_vars`; `data` is a list of such points; `n_vars` ≥ 1.
**Core:** One-pass online covariance and correlation via Welford's method. Maintains mean and an `M2` accumulator matrix that is divided by `n` or `n-1` to recover covariance.
**Assert:** Online covariance matches a batch two-pass computation to machine precision for 500 bivariate normal points; the resulting correlation is positive and in a reasonable range.
**⚠️ Defect:** `get_correlation` replaces zero/negative variances with `std = 1.0`, which silently produces nonsensical correlations when some variables are constant. The class does not validate that each incoming `point` has length `n_vars`, so short rows cause an index error and long rows are silently ignored.

### 12. online_sgd_classifier.py
**Entry fn:** `def logistic(z: float) -> float:`, `def online_sgd_classifier(stream: List[Tuple[List[float], float]], learning_rate: float = 0.01, epochs: int = 1) -> Tuple[List[float], float]:`, `def batch_sgd_classifier(X: List[List[float]], y: List[float], learning_rate: float = 0.01, epochs: int = 10) -> Tuple[List[float], float]:`
**Valid input:** `stream` is a list of `(feature_vector, binary_label)` tuples; all feature vectors have the same dimension; labels are 0 or 1.
**Core:** Logistic-regression training via online SGD (single pass) and batch SGD (multiple epochs). Uses a clamped sigmoid and binary cross-entropy loss.
**Assert:** Online SGD on seeded separable 2D data achieves >70% accuracy; online loss is within 3× of batch loss.
**⚠️ Defect:** `online_sgd_classifier` assumes the stream is finite and small enough to store; true streaming would process an iterator. The sigmoid clamp `max(-100, min(100, z))` is defensive but can hide numerical issues. Learning rate, epochs, and loss clipping are hardcoded defaults; no regularization.

### 13. p2_quantile_estimator.py
**Entry fn:** `class P2Quantile:`, `def __init__(self, p: float):`, `def process(self, x: float) -> None:`, `def _parabolic(self, i: int, s: int) -> float:`, `def _linear(self, i: int, s: int) -> float:`, `def query(self) -> float:`, `def memory_markers(self) -> int:`
**Valid input:** `p` ∈ [0, 1]; input stream eventually contains at least 5 values.
**Core:** Jain-Chlamtac P² quantile estimator. Maintains five markers (min, p/2, p, (1+p)/2, max) and adjusts their heights by piecewise-parabolic interpolation, falling back to linear interpolation when ordering would break.
**Assert:** Memory stays at exactly five markers; median and p90 estimates on 5000 normal samples are within a small fraction of the true standard deviation of the exact quantiles.
**⚠️ Defect:** The first five observations are buffered before the algorithm starts; if the stream ends before five values, `query()` falls back to a crude median-of-buffer rule. The `_parabolic` and `_linear` helpers are private and not validated independently. Marker adjustment depends on integer rounding and can be unstable for adversarial streams.

### 14. page_hinkley_drift.py
**Entry fn:** `class PageHinkleyDrift:`, `def __init__(self, threshold: float = 50.0, delta: float = 0.005, min_instances: int = 30):`, `def process(self, value: float) -> bool:`
**Valid input:** `threshold` > 0; `delta` ≥ 0; `min_instances` ≥ 0; `value` is a number.
**Core:** Page-Hinkley drift detector. Updates the streaming mean, accumulates `m_t = Σ(x_i - mean - delta)`, tracks the running minimum, and fires when `m_t - m_min` exceeds the threshold.
**Assert:** A stable Gaussian stream produces at most one false alarm; a planted mean shift at step 100 is detected before step 150.
**⚠️ Defect:** On detection the detector resets its statistics using the current value as the new mean, which can cause a second alarm immediately after a weak shift. The `min_instances` guard prevents early alarms but also delays detection. The test for the drifting stream has a soft `pass` branch if the detector never fires, so the assert does not strictly enforce detection.

### 15. sliding_window_extrema.py
**Entry fn:** `class MonotonicDequeMinMax:`, `def __init__(self, window_size: int):`, `def process(self, value: float) -> Tuple[float, float]:`, `def sliding_window_min_max_bruteforce(data: List[float], window_size: int) -> List[Tuple[float, float]]:`, `def sliding_window_min_max_deque(data: List[float], window_size: int) -> List[Tuple[float, float]:`
**Valid input:** `window_size` is a positive integer; `data` is a list of numbers with `len(data) >= window_size`.
**Core:** Provides both a brute-force O(n·w) sliding-window min/max and an efficient deque-based O(n) implementation using two monotonic deques.
**Assert:** The deque solution matches brute-force exactly for a 200-point random stream with window size 10; operation counts show the deque approach is more efficient.
**⚠️ Defect:** `MonotonicDequeMinMax` is described as a streaming class but its implementation simply appends to a single deque and computes `min`/`max` over the deque contents in `O(w)` per step — it is not the efficient monotonic-deque algorithm. The actual efficient implementation is the standalone `sliding_window_min_max_deque` function, which is unrelated to the class.

### 16. space_saving_heavy_hitters.py
**Entry fn:** `class SpaceSavingTopK:`, `def __init__(self, k: int = 5):`, `def process(self, item: str) -> None:`, `def get_top_k(self) -> List[Tuple[str, int]:`
**Valid input:** `k` is a positive integer; `item` is hashable.
**Core:** Space-Saving top-k heavy-hitter algorithm. Maintains at most `k` counters; on a new unseen item when full, it evicts the item with the smallest count and assigns the new item `min_count + 1`, preserving the error bound `exact <= estimate <= exact + N/k`.
**Assert:** On a Zipfian 8-item stream with `k=6`, the top-3 identities and order match the exact top-3, and every estimate lies within the Space-Saving error bound.
**⚠️ Defect:** The guarantee only holds when the number of counters is strictly larger than the number of items of interest; with `k` equal to the desired top-k size, tail churn can erode accuracy. The stream generation in the demo uses `max(1, 100 // (i+1))`, which is not a true Zipf distribution.

### 17. streaming_histogram_merge.py
**Entry fn:** `class StreamingHistogram:`, `def __init__(self, max_bins: int = 20):`, `def process(self, value: float) -> None:`, `def _merge_adjacent(self) -> None:`, `def query_quantile(self, p: float) -> float:`, `def get_bins(self) -> List[Tuple[float, int]:`
**Valid input:** `max_bins` is a positive integer; `value` is a float; `p` ∈ [0, 1].
**Core:** Streaming histogram that assigns incoming values to bins within a fixed tolerance. When the number of bins exceeds `max_bins`, it merges the adjacent pair with the smallest combined count, keeping a weighted-average center.
**Assert:** On a planted bimodal normal stream, quantile estimates for p25, median, and p75 are within a loose tolerance, and the final number of bins respects the budget.
**⚠️ Defect:** Bin assignment uses a hardcoded tolerance of 0.5, which only works well for data with similar scale; values far apart can create many singleton bins and force premature merging. Quantile estimation uses bin centers as proxies, not proper interpolation within bins, so accuracy is limited.

### 18. streaming_kmeans.py
**Entry fn:** `class StreamingKMeans:`, `def __init__(self, k: int = 3):`, `def initialize(self, first_points: List[List[float]]) -> None:`, `def nearest_centroid(self, point: List[float]) -> int:`, `def process(self, point: List[float]) -> None:`, `def get_centroids(self) -> List[List[float]:`
**Valid input:** `k` is a positive integer; `point` is a numeric vector of consistent dimension.
**Core:** Online k-means variant. Initializes centroids from the first `k` points, then incrementally updates the nearest centroid toward each new point using a learning rate `1/(count + 1)`.
**Assert:** After processing a seeded, slowly-drifting 3-cluster stream, the final centroids are on average within 2 units of the expected drifting centers.
**⚠️ Defect:** Initialization from the first `k` points is fragile — if those points are outliers or all from one cluster, the algorithm never recovers. There is no forgetting factor, so early data can dominate later drift. `nearest_centroid` is not exposed as a required top-level entry point in the signature reference but is part of the public class API.

### 19. weighted_reservoir_sampling.py
**Entry fn:** `class WeightedReservoirSampler:`, `def __init__(self, k: int = 5):`, `def process(self, item: str, weight: float) -> None:`, `def get_sample(self) -> List[Tuple[str, float]]:`, `def get_inclusion_freq(self, item: str, total_samples: int) -> float:`
**Valid input:** `k` is a positive integer; `weight` is a positive float; `item` is a string.
**Core:** A-Res weighted reservoir sampling. Assigns each item a key `u^(1/weight)` where `u` is uniform; keeps the top `k` keys in a sorted list, giving higher-weight items larger inclusion probability.
**Assert:** Over many runs, high-weight "rare" items have a higher empirical inclusion frequency than low-weight "common" items, and rare-item frequency exceeds 30%.
**⚠️ Defect:** The implementation uses a plain sorted list instead of a heap, so insertion is `O(k)` rather than `O(log k)`. `get_inclusion_freq` is semantically odd: it returns `count_in_current_reservoir / total_samples`, which is not the standard definition of inclusion probability over runs. Items with weight ≤ 0 are silently skipped rather than raising. The demo inflates the stream by adding each item `int(weight)` times, conflating weight with multiplicity.
