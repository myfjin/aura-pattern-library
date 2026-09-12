# Batch 19 — DS Pattern Detail Docs (20 patterns)

## Category: applied_ds_practice (10 patterns)

### 1. cohort_retention_analysis.py
**Entry fn:** `build_cohort_table(events: list[dict]) -> dict[str, dict[int, int]]`, `compute_retention_rates(cohort_table: dict[str, dict[int, int]]) -> dict[str, list[float]]`
**Valid input:** `events: list[dict]` — each with `user_id`, `cohort`, `period`. `cohort_table` — dict mapping cohort to dict of period→user_count.
**Core:** Cohort retention analysis. Groups users by cohort (e.g., signup month), tracks which users return in subsequent periods, and computes retention curves as `active_in_period_p / active_in_period_0`. Uses `defaultdict` of sets to deduplicate users per cohort-period. Tested on two cohorts with different retention rates (80% vs 50% exponential decay).
**Assert:** On synthetic data (200 users per cohort): Cohort A retention > Cohort B retention for every period p ≥ 1. Period 4 difference is large (A > 2× B).
**⚠️ Defect:** The `compute_retention_rates` function silently skips cohorts where period 0 is missing or zero — no warning. The synthetic data uses `random.random() < (0.8 ** period)` which is not a true retention model (users can "reappear" after dropping out). No handling for missing periods in the middle of a cohort's timeline.

### 2. cross_validation_leakage.py
**Entry fn:** `univariate_correlation(X: list[list[float]], y: list[int]) -> list[float]`, `select_top_features(X: list[list[float]], y: list[int], k: int) -> list[int]`, `knn_classify(X_train: list[list[float]], y_train: list[int], X_test: list[list[float]], k: int = 3) -> list[int]`, `accuracy(y_true: list[int], y_pred: list[int]) -> float`
**Valid input:** `X: list[list[float]]` — feature matrix. `y: list[int]` — binary labels. `k ≥ 1` for both feature selection and k-NN.
**Core:** Demonstrates CV leakage by comparing LEAKY (feature selection on full dataset before splitting) vs CORRECT (feature selection within each fold). Uses k-NN classifier and univariate correlation-based feature selection. Leakage inflates cross-validation scores.
**Assert:** On 200 samples with 100 noise features + 5 weak true features, 4-fold CV: mean_leaky > mean_correct, difference > 0.05.
**⚠️ Defect:** The `knn_classify` default `k=3` is overridden to `k=5` in the main block (inconsistent). The label generation is mostly random with slight signal, so the "correct" approach may show near-random accuracy. The `univariate_correlation` function uses population variance (divides by n, not n-1).

### 3. drift_detection_psi.py
**Entry fn:** `reference_bin_edges(ref_values: list[float], n_bins: int = 10) -> list[float]`, `bin_with_edges(values: list[float], edges: list[float]) -> list[int]`, `population_stability_index(ref_bins: list[int], curr_bins: list[int], n_bins: int = 10) -> float`, `kolmogorov_smirnov_statistic(ref_vals: list[float], curr_vals: list[float]) -> float`
**Valid input:** `ref_values, curr_vals: list[float]` — at least n_bins samples. `n_bins ≥ 2`.
**Core:** PSI (Population Stability Index) and KS-statistic for feature drift detection. PSI uses quantile bin edges from the reference window (warns against the common bug of binning each window on its own min/max). Laplace smoothing avoids log(0). KS computes max absolute CDF difference.
**Assert:** No-drift scenario: PSI < 0.25, KS < 0.1. Planted drift (mean +3 SD, increased variance): KS > 0.1, PSI > 0.25, PSI_drift > PSI_no_drift.
**⚠️ Defect:** The KS implementation is O(n×m) (iterates merged unique values) rather than O(n log n) via sorting. The KS threshold of 0.1 is hardcoded, not derived from a p-value. `reference_bin_edges` can produce duplicate bin edges when n is small relative to n_bins.

### 4. ewma_streaming_metrics.py
**Entry fn:** `EWMAMetric` class: `__init__(self, alpha: float = 0.3)`, `update(self, x: float) -> float`. `SMAMetric` class: `__init__(self, window_size: int = 10)`, `update(self, x: float) -> float`
**Valid input:** `alpha in (0, 1)`. `window_size ≥ 1`. `x: float` — any real number.
**Core:** EWMA (exponentially weighted moving average) and SMA (simple moving average) as online streaming metric trackers. EWMA: `value = α·x + (1-α)·value`. SMA: sliding window buffer. EWMA reacts faster to shifts than SMA.
**Assert:** On 50 steps with a mean shift at step 30: EWMA gap < SMA gap at step 35. Both EWMA and SMA are smoother than raw signal (lower MSE of step changes).
**⚠️ Defect:** `SMAMetric.update` uses `list.pop(0)` which is O(n) per call — `collections.deque` would be O(1). The smoothness metric penalizes SMA more than EWMA for the shift itself, not just noise. Only one time step is checked for responsiveness.

### 5. feature_hashing_trick.py
**Entry fn:** `hash_feature(feature_name: str, n_dims: int) -> int`, `hash_vectorize_text(texts: list[str], n_dims: int = 128) -> list[list[float]]`, `dot_product(v1: list[float], v2: list[float]) -> float`, `simple_linear_classifier(X_train: list[list[float]], y_train: list[int], X_test: list[list[float]], iterations: int = 100) -> list[float]`, `accuracy(y_true: list[int], y_pred: list[float]) -> float`, `collision_rate(texts: list[str], n_dims: int) -> float`
**Valid input:** `texts: list[str]` — at least 1 document. `n_dims ≥ 1`. `iterations ≥ 1`.
**Core:** Maps text words to fixed-dimensional feature vectors via SHA-256 hashing modulo n_dims. Trains logistic regression via SGD on hash vectors. Demonstrates the dimension-collision tradeoff: lower dimensions → more collisions → worse accuracy.
**Assert:** On synthetic spam/ham data: deterministic (same seed → same accuracy). Accuracy > 0.5 at 64 dimensions. Collision rate at 32 dims > collision rate at 128 dims.
**⚠️ Defect:** The `simple_linear_classifier` hardcodes `2.718281828` instead of `math.exp`, with fragile z-clipping. The `accuracy` function uses a confusing boolean comparison `(yp > 0.5) == (yt == 1)`. The test set is tiny (4 samples), making accuracy noisy.

### 6. funnel_conversion_analysis.py
**Entry fn:** `wilson_confidence_interval(successes: int, trials: int, confidence: float = 0.95) -> tuple[float, float]`, `build_funnel_events(events: list[dict]) -> dict[str, dict]`, `compute_conversion_rates(funnel: dict[str, dict], step_order: list[str]) -> dict[str, dict]`
**Valid input:** `successes ≤ trials`. `confidence in (0, 1)`. `events: list[dict]` — each with `user_id` and `step`.
**Core:** Aggregates user progression through a multi-step funnel (visit → signup → trial → purchase). Computes step-wise conversion rates with Wilson score confidence intervals. Identifies the weakest step.
**Assert:** On 1000 visitors (80% signup, 75% trial, 20% purchase): weakest step = 'purchase'. Trial CI lower bound > purchase CI upper bound (non-overlapping).
**⚠️ Defect:** The `wilson_confidence_interval` only handles `confidence=0.95` and `0.90` explicitly; other values silently use z=1.96 (incorrect). The funnel assumes strict linear progression; users who skip steps are not handled.

### 7. rfm_customer_segmentation.py
**Entry fn:** `compute_rfm_metrics(transactions: list[dict]) -> dict[int, dict]`, `quartile_score(values: list[float], recency_flag: bool = False) -> dict[float, int]`, `segment_from_rfm(r: int, f: int, m: int) -> str`
**Valid input:** `transactions: list[dict]` — each with `user_id`, `amount`, `purchase_date`. `values: list[float]` — at least 4 samples for quartiles.
**Core:** Computes Recency (days since last purchase), Frequency (purchase count), and Monetary (total spend). Maps each metric to quartile scores [1-4] (inverted for recency). Segments customers into "whale", "frequent", "regular", "at_risk", or "churned".
**Assert:** On synthetic data (20 whales, 40 regular, 40 churned): >10 whales and >10 churned detected. Average whale frequency > average churned frequency.
**⚠️ Defect:** The `quartile_score` function uses `sorted(set(values))` which deduplicates values before computing boundaries, skewing quartiles for shared values. The `segment_from_rfm` hierarchy is arbitrary with overlapping conditions. The `purchase_date` field uses integer days-ago values, making some dates negative.

### 8. simpsons_paradox_demo.py
**Entry fn:** `compute_rate(numerator: int, denominator: int) -> float`
**Valid input:** `denominator > 0`. `0 ≤ numerator ≤ denominator`.
**Core:** Demonstrates Simpson's Paradox: Treatment B beats A in both strata (easy: 90% vs 80%; hard: 12% vs 10%), but A wins in aggregate (81.8% vs 11.8%) because A was applied mostly to easy cases (1000/1100) while B was applied mostly to hard cases (1000/1100).
**Assert:** B wins stratum 1, B wins stratum 2, A wins aggregate, paradox is detected.
**⚠️ Defect:** All data is hardcoded in `__main__` — no reusable functions beyond `compute_rate`. The paradox detection only checks the specific pattern "B wins both strata but loses aggregate" (or reverse). No statistical significance test.

### 9. target_encoding_smoothing.py
**Entry fn:** `fit_encoding(cats: List[str], targets: List[int], alpha: float = 0.0) -> Dict[str, float]`, `apply_encoding(cats: List[str], enc: Dict[str, float], default: float) -> List[float]`, `oof_encode_train(cats: List[str], targets: List[int], n_folds: int = 5, alpha: float = 5.0) -> List[float]`, `abs_correlation(X: List[float], y: List[int]) -> float`
**Valid input:** `cats: List[str]` — categorical feature. `targets: List[int]` — binary labels. `alpha ≥ 0`. `n_folds ≥ 2`.
**Core:** Target (mean) encoding with two defenses against leakage: (1) smoothing shrinks rare-category means toward the global prior via `(sum + α·prior) / (count + α)`, and (2) out-of-fold fitting encodes each training row using an encoding fit without its own fold. Leaky encoding fabricates test-set skill on pure-noise targets; proper encoding shows near-zero correlation.
**Assert:** On 80 categories × 5 rows, pure-noise targets: leaky test correlation > 0.30, proper test correlation < 0.15, OOF train correlation < 0.15. Smoothing pulls rare category toward prior.
**⚠️ Defect:** The `abs_correlation` function uses population covariance (divides by n, not n-1). OOF uses `i % n_folds` for fold assignment (not randomized). The prior is recomputed from the full training set in each fold rather than from the fold's training data.

### 10. welford_online_stats.py
**Entry fn:** `WelfordStats` class: `update(self, x: float) -> None`, `variance(self) -> float`, `std_dev(self) -> float`. `naive_variance(values: list[float]) -> float`, `batch_variance(values: list[float]) -> float`
**Valid input:** `x: float` — any real number. `values: list[float]` — at least 2 samples.
**Core:** Welford's online algorithm for running mean and variance with O(1) memory and numerical stability. Recurrence: `δ = x - mean; mean += δ / count; δ₂ = x - mean; m₂ += δ·δ₂`. Compares against naive `E[X²] - E[X]²` (catastrophic cancellation with large offsets) and batch sum-of-squared-deviations (reference truth).
**Assert:** Normal data: Welford variance matches batch variance within 1e-10. Large offset (1e10): Welford matches batch within 1e-6, naive variance error > 1.0 (naive fails catastrophically).
**⚠️ Defect:** The `naive_variance` function returns 0.0 when computed variance is negative (masks failure). The `WelfordStats` dataclass has no reset or merge method for distributed settings. No overflow handling for `count` in extremely long streams.

---

## Category: data_wrangling_from_scratch (10 patterns)

### 11. csv_type_inference.py
**Entry fn:** `infer_type(value: str) -> str`, `infer_column_types(rows: List[Dict[str, str]]) -> Dict[str, str]`
**Valid input:** `value: str` — any string. `rows: List[Dict[str, str]]` — at least 1 row.
**Core:** Type inference for CSV columns. `infer_type` tries `int` → `float` → date regex (`YYYY-MM-DD`) → `str`. Empty strings and `"none"` → `"missing"`. `infer_column_types` picks the most common non-missing type per column.
**Assert:** On 5-column test data: `id` → int, `age` → int, `salary` → float, `date` → date, `name` → str. Planted empty string in `age` is present.
**⚠️ Defect:** Date regex only matches `YYYY-MM-DD`. No boolean, `None` object, or scientific notation handling. The "most common type" heuristic can misclassify mixed-type columns. No handling of quoted CSV values or escaped characters.

### 12. dedupe_records_fuzzy.py
**Entry fn:** `normalize(s: str) -> str`, `edit_distance(s1: str, s2: str) -> int`, `find_duplicates(records: List[Dict[str, Any]], match_key: str, threshold: int = 2) -> List[List[int]]`, `dedupe(records: List[Dict[str, Any]], match_key: str, threshold: int = 2) -> List[Dict[str, Any]]`
**Valid input:** `records: List[Dict[str, Any]]` — at least 1 record. `match_key: str` — key in each record. `threshold ≥ 0`.
**Core:** Fuzzy deduplication via Levenshtein edit distance. `normalize` lowercases and strips whitespace. `edit_distance` uses DP matrix (O(mn)). `find_duplicates` greedily clusters records within threshold distance. `dedupe` keeps the first record of each cluster.
**Assert:** On 5 records with planted near-duplicates: 3 clusters found, 2 clusters have 2 records each, Alice cluster contains indices [0, 1]. Deduped result has 3 records with IDs [1, 3, 5].
**⚠️ Defect:** Greedy clustering is order-dependent. O(n²) pairwise edit distance — no blocking/keying. Threshold is a flat integer, not normalized by string length (2-char diff on a 3-char string is very different from 2 on a 20-char string).

### 13. group_by_aggregate.py
**Entry fn:** `group_by_aggregate(records: List[Dict[str, Any]], group_keys: List[str], agg_col: str, agg_func: str) -> Dict[tuple, float]`, `brute_force_aggregate(records: List[Dict[str, Any]], group_keys: List[str], agg_col: str, agg_func: str) -> Dict[tuple, float]`
**Valid input:** `records: List[Dict[str, Any]]` — at least 1 record. `group_keys: List[str]` — at least 1 key. `agg_func` in {"sum", "mean", "count", "min", "max"}.
**Core:** Group-by aggregation from scratch. Groups records by a tuple of `group_keys`, collects values of `agg_col`, then applies `agg_func`. `brute_force_aggregate` is a reference implementation that recomputes aggregates by scanning all records per group.
**Assert:** On test data: group_by_aggregate matches brute_force_aggregate for sum (multi-key), mean, count, and min.
**⚠️ Defect:** Only supports numeric aggregation columns. `mean` accumulates all values in a list then divides (memory-inefficient for large groups). No handling of empty groups or missing values. `agg_func` is a string, not validated.

### 14. hash_join_merge.py
**Entry fn:** `hash_join_inner(left_table: List[Dict[str, Any]], right_table: List[Dict[str, Any]], join_key: str) -> List[Dict[str, Any]]`, `hash_join_left(left_table: List[Dict[str, Any]], right_table: List[Dict[str, Any]], join_key: str) -> List[Dict[str, Any]]`, `nested_loop_inner_join(left_table: List[Dict[str, Any]], right_table: List[Dict[str, Any]], join_key: str) -> List[Dict[str, Any]]`
**Valid input:** `left_table, right_table: List[Dict[str, Any]]` — at least 1 row each. `join_key: str` — key present in both tables.
**Core:** Hash join implementation. Builds a hash table from the right table keyed by `join_key`, then probes with the left table. Inner join emits only matching rows. Left join emits all left rows (unmatched rows have no right columns). Merged rows use `{**left_row, **right_row}`.
**Assert:** On test data: hash inner join matches brute-force inner join. Inner join has 2 rows. Left join has 3 rows. Unmatched left row has no `salary` key.
**⚠️ Defect:** Only supports single-key join. Left join doesn't pad unmatched rows with `None` (inconsistent with SQL). Right-column overwrite on key collision. No outer, anti-, or semi-join variants.

### 15. melt_unpivot.py
**Entry fn:** `melt(wide_data: Dict[Any, Dict[Any, float]], row_key_name: str, col_key_name: str, val_key_name: str) -> List[Dict[str, Any]]`, `pivot_table(records: List[Dict[str, Any]], row_key: str, col_key: str, val_key: str) -> Dict[Any, Dict[Any, float]]`
**Valid input:** `wide_data: Dict[Any, Dict[Any, float]]` — nested dict. `records: List[Dict[str, Any]]` — at least 1 record.
**Core:** Melt (unpivot) converts a nested dict `{row: {col: value}}` into a list of flat records. The local `pivot_table` helper reverses the operation (no aggregation — last value wins on duplicates). Round-trip test verifies `pivot(melt(wide)) == wide`.
**Assert:** Melt produces 4 records (2 rows × 2 columns). Round-trip preserves original data. Specific melted record `{"category": "A", "region": "US", "amount": 150}` exists.
**⚠️ Defect:** The local `pivot_table` does no aggregation — duplicates silently overwrite. Only handles a single value column. Input is a nested dict, not a list-of-dicts wide format.

### 16. pivot_table.py
**Entry fn:** `pivot_table(records: List[Dict[str, Any]], row_key: str, col_key: str, val_key: str, agg_func: str = "sum") -> Dict[Any, Dict[Any, float]]`, `compute_margins(pivot: Dict[Any, Dict[Any, float]]) -> Dict[str, Dict[Any, float]]`
**Valid input:** `records: List[Dict[str, Any]]` — at least 1 record. `agg_func` in {"sum", "count"}.
**Core:** Pivot table with aggregation. Groups records by `(row_key, col_key)` and aggregates values using `agg_func` ("sum" or "count"). `compute_margins` computes row and column totals.
**Assert:** Row totals and column totals each equal grand sum. Specific cells verified: A/US=150, B/EU=125. Row totals: A=225, B=155.
**⚠️ Defect:** Only "sum" and "count" are implemented — "min", "max", "mean" collect lists but never reduce them. No handling of missing combinations. `compute_margins` doesn't include a grand total.

### 17. resample_timeseries_bins.py
**Entry fn:** `parse_timestamp(ts: str) -> tuple`, `bucket_hourly(records: List[Dict[str, Any]]) -> Dict[tuple, float]`, `bucket_daily(records: List[Dict[str, Any]]) -> Dict[tuple, float]`, `brute_force_hourly(records: List[Dict[str, Any]]) -> Dict[tuple, float]`
**Valid input:** `ts: str` — format `"YYYY-MM-DD HH:MM"`. `records: List[Dict[str, Any]]` — each with `timestamp` and `value`.
**Core:** Time series resampling. `parse_timestamp` parses `"YYYY-MM-DD HH:MM"` into `(year, month, day, hour)`. `bucket_hourly` groups by hour and sums values. `bucket_daily` groups by day and sums values. Verified against brute-force O(n²) reference.
**Assert:** Hourly buckets match brute-force. Specific hourly and daily bucket sums verified. Daily sum equals total record sum.
**⚠️ Defect:** Only supports `"YYYY-MM-DD HH:MM"` format — no timezone handling. Only `sum` aggregation. No custom bin widths (15-min, weekly, monthly). Brute-force reference is O(n²).

### 18. rolling_join_asof.py
**Entry fn:** `asof_join(left: List[Dict[str, Any]], right: List[Dict[str, Any]], key: str) -> List[Dict[str, Any]]`, `brute_force_asof(left: List[Dict[str, Any]], right: List[Dict[str, Any]], key: str) -> List[Dict[str, Any]]`
**Valid input:** `left, right: List[Dict[str, Any]]` — at least 1 row each. `key: str` — timestamp key to join on.
**Core:** As-of join: for each left row, find the nearest right row with `key ≤ left_key`. Sorts right table by key, then scans in reverse. Merges left row with right row's columns (skipping the `"time"` key from right). Verified against brute-force reference.
**Assert:** On trade/quote data: time 100 → bid 49, time 150 → bid 50, time 200 → bid 51. Joined times/bids match brute-force.
**⚠️ Defect:** The nearest-preceding scan is O(n×m) worst-case — should use binary search (`bisect`) for O(log m). The merge condition `k not in merged or k == "time"` is confusingly written. No `by` group key support. No forward-looking as-of variant.

### 19. sort_multi_key.py
**Entry fn:** `multi_key_sort(records: List[Dict[str, Any]], keys: List[tuple]) -> List[Dict[str, Any]]`
**Valid input:** `records: List[Dict[str, Any]]` — at least 1 record. `keys: List[tuple]` — `[(key_name, is_asc), ...]`.
**Core:** Multi-key sorting from scratch. Builds a composite sort key from `(key_name, is_asc)` tuples. For descending order, numeric values are negated; string values are wrapped in `(1, val)` to reverse lexicographic order. Uses Python's stable `sorted()`.
**Assert:** Category order is [A, A, A, B, B]. A values are descending [20, 20, 10]. Stability: records 2 and 4 (both A/20) preserve original order.
**⚠️ Defect:** The string-reversal trick `(1, val)` is fragile — breaks if the ascending key is also a tuple. No support for `None`/missing values. No custom comparators or nulls-first/nulls-last semantics.

### 20. window_functions.py
**Entry fn:** `apply_window_functions(records: List[Dict[str, Any]], partition_key: str, order_key: str) -> List[Dict[str, Any]]`
**Valid input:** `records: List[Dict[str, Any]]` — at least 1 record. `partition_key, order_key: str` — keys in each record.
**Core:** Window functions from scratch. Groups records by `partition_key`, sorts each partition by `order_key`, then computes: `row_number`, `rank`, `dense_rank` (all simplified to sequential integers), `lag_value`, `lead_value`, and `running_sum`.
**Assert:** Category A has 3 records with row_numbers [1, 2, 3]. Lag/lead values verified for first and last rows. Running sums for A are [5, 15, 35].
**⚠️ Defect:** `rank` and `dense_rank` are both implemented as simple sequential counters — only correct when there are no ties (real `rank` skips numbers, `dense_rank` does not). No window frame support (ROWS BETWEEN). No `ntile`, `first_value`, `last_value`. Lag/lead hardcoded to offset 1.