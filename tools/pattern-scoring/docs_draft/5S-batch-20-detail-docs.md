# Batch 20 — DS Pattern Detail Docs (20 patterns)

Categories: `applied_ds_practice` (10) + `data_wrangling_from_scratch` (10).

---

## Category: applied_ds_practice

### 1. cohort_retention_analysis.py
**Entry fn:** `def build_cohort_table(events: list[dict]) -> dict[str, dict[int, int]]`, `def compute_retention_rates(cohort_table: dict[str, dict[int, int]]) -> dict[str, list[float]]`
**Valid input:** `events` are dicts with keys `user_id`, `cohort`, `period`. `cohort_table` is the output of `build_cohort_table`.
**Core:** Builds a cohort retention table (cohort → {period: unique-user-count}) and computes period-by-period retention as `active_in_period / cohort_size_in_period_0`. Compares retention curves across cohorts.
**Assert:** On two planted cohorts (A with 80% per-period retention, B with 50%), cohort A has higher retention at every period p ≥ 1 and at least 2× the period-4 retention of cohort B.
**⚠️ Defect:** `compute_retention_rates` silently skips cohorts that have no period-0 record and computes rates only over observed periods. A user appearing in a later period without a period-0 event inflates that period's count and can produce retention > 100% or nonsensical curves. The demo seeds period 0 for everyone, so the guard is never exercised.

### 2. cross_validation_leakage.py
**Entry fn:** `def univariate_correlation(X: list[list[float]], y: list[int]) -> list[float]:`, `def select_top_features(X: list[list[float]], y: list[int], k: int) -> list[int]:`, `def knn_classify(X_train: list[list[float]], y_train: list[int], X_test: list[list[float]], k: int = 3) -> list[int]:`, `def accuracy(y_true: list[int], y_pred: list[int]) -> float:`
**Valid input:** `X` non-empty, rectangular; `y` same length as `X`; `k >= 1`. Feature selection and k-NN operate on binary labels {0, 1}.
**Core:** Demonstrates data leakage: univariate feature selection fit on the full dataset (including the test fold) inflates CV accuracy compared to fitting feature selection inside each train fold. Uses k-NN and accuracy as a downstream classifier.
**Assert:** On 200 samples with 100 noise + 5 weak signal features, leaky CV accuracy exceeds train-only CV accuracy by at least 0.05; both scores are reported and compared.
**⚠️ Defect:** `knn_classify` uses a biased tie-breaker (`sum(nearest_labels) > k / 2`) that always predicts the negative class on an exact tie (e.g., k=4 with two 0s and two 1s). It also applies Euclidean distance to unnormalized features, so distance is dominated by the 100 noise dimensions with larger variance, even after feature selection. The leakage contrast still holds, but the absolute accuracy is noisy and tie-handling is asymmetric.

### 3. drift_detection_psi.py
**Entry fn:** `def reference_bin_edges(ref_values: list[float], n_bins: int = 10) -> list[float]:`, `def bin_with_edges(values: list[float], edges: list[float]) -> list[int]:`, `def population_stability_index(ref_bins: list[int], curr_bins: list[int], n_bins: int = 10) -> float:`, `def kolmogorov_smirnov_statistic(ref_vals: list[float], curr_vals: list[float]) -> float:`
**Valid input:** `ref_values` and `curr_values` non-empty numeric lists; `n_bins >= 2`.
**Core:** Population Stability Index (PSI) and Kolmogorov-Smirnov statistic for distribution drift. Bins the reference window on its own quantile edges, then bins the current window on those same edges to avoid hiding drift. PSI uses Laplace-smoothed bin proportions; KS uses the maximum absolute CDF difference.
**Assert:** On 500 reference + 500 current samples from the same N(100, 15): PSI < 0.25 and KS < 0.1. On a shifted N(145, 25) current window: KS > 0.1 and PSI > 0.25, with drift PSI exceeding no-drift PSI.
**⚠️ Defect:** `reference_bin_edges` computes edges from `sorted(set(ref_values))` (unique values) rather than the full distribution, so duplicate values are discarded when choosing quantile boundaries. For heavy-tailed or highly discrete data this produces inaccurate or duplicate edges and can leave bins empty. `kolmogorov_smirnov_statistic` computes empirical CDFs with O(n²) nested loops, making it impractical for large windows, and evaluates the KS statistic only at the unique observed values rather than at all jump points.

### 4. ewma_streaming_metrics.py
**Entry fn:** `class EWMAMetric` with `def __init__(self, alpha: float = 0.3):` and `def update(self, x: float) -> float:`, `class SMAMetric` with `def __init__(self, window_size: int = 10):` and `def update(self, x: float) -> float:`
**Valid input:** `alpha` in [0, 1]; `window_size >= 1`; observations are numeric.
**Core:** Online EWMA (`value_t = alpha * x_t + (1 - alpha) * value_{t-1}`) and simple moving average for streaming metrics. EWMA is more responsive to level shifts than SMA; both are smoother than raw values.
**Assert:** On a planted step change from 100 to 120 at step 30 (with seed 42), EWMA is closer to the new level at step 35 than SMA, and both estimators have lower step-change variance than the raw series.
**⚠️ Defect:** `EWMAMetric` initializes the EWMA to the first observed value instead of a neutral prior (e.g., 0 or a user-supplied baseline). For small `alpha` this creates a long warm-up bias toward whatever value happens to arrive first. `SMAMetric` uses `list.pop(0)` to maintain its window, so each update is O(window_size) rather than O(1); for high-throughput streams this is a real bottleneck.

### 5. feature_hashing_trick.py
**Entry fn:** `def hash_feature(feature_name: str, n_dims: int) -> int:`, `def hash_vectorize_text(texts: list[str], n_dims: int = 128) -> list[list[float]]:`, `def dot_product(v1: list[float], v2: list[float]) -> float:`, `def simple_linear_classifier(X_train: list[list[float]], y_train: list[int], X_test: list[list[float]], iterations: int = 100) -> list[float]:`, `def accuracy(y_true: list[int], y_pred: list[float]) -> float:`, `def collision_rate(texts: list[str], n_dims: int) -> float:`
**Valid input:** `texts` non-empty list of strings; `n_dims > 0`; `iterations > 0`; binary labels in `y_train`.
**Core:** Feature hashing (hashing trick): maps words to a fixed-size dimension via SHA-256, builds count vectors, then trains a simple SGD logistic classifier. Collision rate measures how many unique words share hash bins.
**Assert:** On a tiny spam/ham dataset, classification accuracy beats chance; hash vectors are deterministic under the same input; collision rate is higher for 32 dims than for 128 dims.
**⚠️ Defect:** `simple_linear_classifier` divides the per-sample gradient by `len(X_train)` inside the SGD loop, so the effective step size scales inversely with training-set size — it is not standard SGD and the learning rate is hardcoded at 0.01. It also uses a literal `2.718281828` for Euler's number instead of `math.e` or `math.exp`, and caps only the negative exponent, so the sigmoid is fragile for large negative `z`. `hash_vectorize_text` performs no token normalization (punctuation, stemming), so "WINNER!" and "winner" hash to different bins.

### 6. funnel_conversion_analysis.py
**Entry fn:** `def wilson_confidence_interval(successes: int, trials: int, confidence: float = 0.95) -> tuple[float, float]:`, `def build_funnel_events(events: list[dict]) -> dict[str, dict]:`, `def compute_conversion_rates(funnel: dict[str, dict], step_order: list[str]) -> dict[str, dict]:`
**Valid input:** `events` are dicts with `user_id` and `step`. `funnel` is the output of `build_funnel_events`. `step_order` lists steps in progression order.
**Core:** Multi-step funnel analysis. Aggregates unique users per step, computes step-to-step conversion rates, and adds Wilson score confidence intervals. Identifies the weakest step by minimum conversion rate.
**Assert:** On a planted funnel (visit→signup 80%, signup→trial 75%, trial→purchase 20%), the weakest step is "purchase" and the trial conversion CI lies entirely above the purchase conversion CI.
**⚠️ Defect:** `wilson_confidence_interval` hardcodes `z` only for `confidence == 0.95` or `0.90`; any other confidence level silently falls back to 1.96, producing wrong intervals. `compute_conversion_rates` skips missing steps via `continue` (so they are absent from the result) and assigns the final step a CI of `(0, 0)`, which is not a valid Wilson interval. The function also cannot report conversion from a step to a non-adjacent next step.

### 7. rfm_customer_segmentation.py
**Entry fn:** `def compute_rfm_metrics(transactions: list[dict]) -> dict[int, dict]:`, `def quartile_score(values: list[float], recency_flag: bool = False) -> dict[float, int]:`, `def segment_from_rfm(r: int, f: int, m: int) -> str:`
**Valid input:** `transactions` are dicts with `user_id`, `purchase_date` (numeric), `amount`. At least one transaction.
**Core:** RFM segmentation: recency (days since last purchase), frequency (count), monetary (total spend). Each metric is mapped to quartile scores 1–4, with recency inverted so lower recency scores higher. Combined R, F, M scores produce segments such as "whale", "churned", "at_risk".
**Assert:** On planted archetypes (whales: frequent/recent/high spend; churned: old/low/low), the whale segment contains more than 10 customers, the churned segment contains more than 10, and whale average frequency exceeds churned average frequency.
**⚠️ Defect:** `quartile_score` builds quartile boundaries from `sorted(set(values))` — it removes duplicates before computing quartiles, so the boundaries reflect unique-value ranks rather than true count quartiles. A value repeated many times can be assigned to different score buckets across runs or relative to its actual percentile. The function also has no guard for empty input and uses arbitrary 1/2/3/4 cutoffs in `segment_from_rfm` that are not validated against business semantics.

### 8. simpsons_paradox_demo.py
**Entry fn:** `def compute_rate(numerator: int, denominator: int) -> float:`
**Valid input:** `denominator > 0`; `0 <= numerator <= denominator`.
**Core:** Demonstrates Simpson's paradox: treatment B can beat treatment A within every stratum yet lose in the aggregate because the strata have different base rates and unequal treatment allocation.
**Assert:** On the planted two-strata example, B wins stratum 1 (90% vs 80%), B wins stratum 2 (12% vs 10%), but A wins aggregate (73% vs 19%). The paradox is detected and asserted.
**⚠️ Defect:** The paradox detector is hardcoded for exactly two strata and only recognizes the "wins both / loses aggregate" (or reverse) pattern. It does not generalize to more strata, partial reversals, or continuous confounders. `compute_rate` returns `0` for a zero denominator and does not validate `numerator <= denominator`, so malformed inputs silently produce rates outside [0, 1].

### 9. target_encoding_smoothing.py
**Entry fn:** `def fit_encoding(cats: List[str], targets: List[int], alpha: float = 0.0) -> Dict[str, float]:`, `def apply_encoding(cats: List[str], enc: Dict[str, float], default: float) -> List[float]:`, `def oof_encode_train(cats: List[str], targets: List[int], n_folds: int = 5, alpha: float = 5.0) -> List[float]:`, `def abs_correlation(X: List[float], y: List[int]) -> float:`
**Valid input:** `cats` and `targets` same-length lists; binary targets in `targets`; `n_folds >= 2`; `alpha >= 0`.
**Core:** Target (mean) encoding with smoothing and true out-of-fold (OOF) fitting. The demo plants pure-noise targets to show that leakage (encoding fit on train+test) fabricates test-set "skill" while OOF and proper train-only encoding show near-zero correlation.
**Assert:** On 80 categories × 5 rows of pure-noise binary targets, leaky test-set |correlation| > 0.30, proper test |correlation| < 0.15, OOF train |correlation| < 0.15, and smoothing pulls a rare category toward the global prior.
**⚠️ Defect:** `oof_encode_train` assigns folds by simple modulo over row index (`i % n_folds`), which does not stratify by category. If a rare category's rows happen to share the same index residue, that category is absent from the fit folds for those rows, so those rows receive the global prior instead of a category-smoothed value. `fit_encoding` also silently truncates if `cats` and `targets` have different lengths because it zips them without validation. `abs_correlation` uses population (biased) variances.

### 10. welford_online_stats.py
**Entry fn:** `class WelfordStats` with `def update(self, x: float) -> None:`, `def variance(self) -> float:`, `def std_dev(self) -> float:`, `def naive_variance(values: list[float]) -> float:`, `def batch_variance(values: list[float]) -> float:`
**Valid input:** `values` is a list of numbers with at least two elements for meaningful variance.
**Core:** Welford's online algorithm for stable one-pass mean and sample variance, compared against a naive sum-of-squares formula and a batch reference. The demo shows catastrophic cancellation in the naive formula for large-offset data.
**Assert:** On 1,000 N(0,1) samples, Welford variance matches batch variance within 1e-10. On 1,000 samples with offset 1e10, Welford variance still matches batch variance within 1e-6 while naive variance diverges by more than 1.0.
**⚠️ Defect:** `naive_variance` can return `0.0` when the population formula `E[X²] - E[X]²` yields a tiny negative number due to floating-point cancellation, hiding the numerical instability. The function returns `var * n/(n-1)` only when `var > 0`, otherwise `0.0`. `WelfordStats.variance()` returns `0.0` for `count < 2`, which is a sensible sentinel but not an error, and the class does not expose the running mean as a public accessor.

---

## Category: data_wrangling_from_scratch

### 11. csv_type_inference.py
**Entry fn:** `def infer_type(value: str) -> str:`, `def infer_column_types(rows: List[Dict[str, str]]) -> Dict[str, str]:`
**Valid input:** `rows` is a non-empty list of dicts representing CSV rows. Values are strings.
**Core:** Infers a column type from the most common non-missing type among its string values: int (parses as int), float (parses as float), date (`YYYY-MM-DD`), or str (fallback). Missing/"none" values are ignored.
**Assert:** On planted rows with id→int, age→int (with one missing), salary→float, date→date, name→str, the inferred types match the planted expectations.
**⚠️ Defect:** `infer_type` tries `int()` before the date regex, so a column of ISO dates without hyphens (e.g., "20240115") or a column of integer-like IDs is inferred as int, not date. The date regex is strictly `YYYY-MM-DD` and ignores times, time zones, and other separators. `infer_column_types` assumes every row has exactly the keys of `rows[0]` and does not validate consistency; rows with missing or extra columns silently shift column inference.

### 12. dedupe_records_fuzzy.py
**Entry fn:** `def normalize(s: str) -> str:`, `def edit_distance(s1: str, s2: str) -> int:`, `def find_duplicates(records: List[Dict[str, Any]], match_key: str, threshold: int = 2) -> List[List[int]]:`, `def dedupe(records: List[Dict[str, Any]], match_key: str, threshold: int = 2) -> List[Dict[str, Any]]:`
**Valid input:** `records` non-empty list of dicts; `match_key` present in every record; `threshold >= 0`.
**Core:** Fuzzy deduplication via Levenshtein edit distance on a single string field. Normalizes strings, greedily clusters records whose key distance is within the threshold, then keeps the first record of each cluster.
**Assert:** On planted records with two 1-character typos (Alice Johnson/Alice Jonson, Bob Smith/Bob Smyth) and one distinct record, `find_duplicates` returns three clusters with two two-record clusters, and `dedupe` keeps ids [1, 3, 5].
**⚠️ Defect:** The greedy clustering performs transitive chaining: if A is within threshold of B and B is within threshold of C, A and C are forced into the same cluster even when their direct distance exceeds the threshold. This can merge genuinely distinct records through a middle typo. The algorithm also only compares a single `match_key`; typos in other fields or swapped name order are ignored.

### 13. group_by_aggregate.py
**Entry fn:** `def group_by_aggregate(records: List[Dict[str, Any]], group_keys: List[str], agg_col: str, agg_func: str) -> Dict[tuple, float]:`, `def brute_force_aggregate(records: List[Dict[str, Any]], group_keys: List[str], agg_col: str, agg_func: str) -> Dict[tuple, float]:`
**Valid input:** `records` non-empty; `group_keys` and `agg_col` exist in every record; `agg_func` is one of `"sum"`, `"mean"`, `"count"`, `"min"`, `"max"`.
**Core:** Multi-key group-by aggregation. Collects values per group key tuple and applies the requested aggregation function. A brute-force reference implementation is provided for parity checks.
**Assert:** On planted records grouped by `(category, region)` and `(category)`, the function matches the brute-force reference for sum, mean, count, and min.
**⚠️ Defect:** `group_by_aggregate` silently returns `None` for every group if `agg_func` is not one of the five supported strings, instead of raising an error. It also does not validate that `group_keys` or `agg_col` exist in a record, so a missing key raises an unhelpful `KeyError` only at access time. The return type claims `Dict[tuple, float]`, but for unsupported functions the values are lists or `None`.

### 14. hash_join_merge.py
**Entry fn:** `def hash_join_inner(left_table: List[Dict[str, Any]], right_table: List[Dict[str, Any]], join_key: str) -> List[Dict[str, Any]]:`, `def hash_join_left(left_table: List[Dict[str, Any]], right_table: List[Dict[str, Any]], join_key: str) -> List[Dict[str, Any]]:`, `def nested_loop_inner_join(left_table: List[Dict[str, Any]], right_table: List[Dict[str, Any]], join_key: str) -> List[Dict[str, Any]]:`
**Valid input:** `left_table` and `right_table` non-empty lists of dicts; `join_key` present in every row.
**Core:** Hash-based inner and left joins on a single key. The inner join result is verified against a nested-loop inner join. Left join preserves all left rows.
**Assert:** On planted left table [1,2,3] and right table [1,2,4], inner join returns rows 1 and 2; left join returns three rows and row 3 has no `salary` value.
**⚠️ Defect:** `hash_join_left` returns the original left row unchanged when there is no right match, so missing right columns are simply absent rather than explicitly set to `None`. This creates a schema-inconsistent output: matched rows have right columns, unmatched rows do not. The demo's assertion passes only because it uses `.get("salary")`. Both joins use `{**left_row, **right_row}`, so any non-key column collision is silently resolved by overwriting left with right. There is no validation for missing `join_key`.

### 15. melt_unpivot.py
**Entry fn:** `def melt(wide_data: Dict[Any, Dict[Any, float]], row_key_name: str, col_key_name: str, val_key_name: str) -> List[Dict[str, Any]]:`, `def pivot_table(records: List[Dict[str, Any]], row_key: str, col_key: str, val_key: str) -> Dict[Any, Dict[Any, float]]:`
**Valid input:** `wide_data` is a nested dict `{row: {col: value}}`; key-name strings are non-empty.
**Core:** Melt (unpivot): converts a wide nested-dict table into long-format records. Includes a simple pivot function for the reverse direction to verify round-trip equality.
**Assert:** On a 2×2 wide table, `melt` produces 4 records and `pivot_table(melt(...))` recovers the original wide table exactly.
**⚠️ Defect:** `pivot_table` in this module silently overwrites duplicate `(row, col)` pairs instead of aggregating. If the long input contains repeated row/column combinations, information is lost. The round-trip assertion passes only because the demo has unique cells.

### 16. pivot_table.py
**Entry fn:** `def pivot_table(records: List[Dict[str, Any]], row_key: str, col_key: str, val_key: str, agg_func: str = "sum") -> Dict[Any, Dict[Any, float]]:`, `def compute_margins(pivot: Dict[Any, Dict[Any, float]]) -> Dict[str, Dict[Any, float]]:`
**Valid input:** `records` non-empty; `row_key`, `col_key`, `val_key` exist; `val_key` values are numeric; `agg_func` is `"sum"` or `"count"`.
**Core:** Pivot long-format records into a wide table, supporting sum and count aggregation, plus row and column margin totals.
**Assert:** On planted records, pivot cells match hand-computed values (A/US = 150, B/EU = 125), row totals equal the record sum, and column totals equal the record sum.
**⚠️ Defect:** For any `agg_func` other than `"sum"` or `"count"` (e.g., `"mean"`, `"min"`, `"max"`), `pivot_table` stores values in a list but never computes the final aggregation, returning a list in the cell instead of a float. This is a silent failure for unsupported aggregations. The docstring does not warn that only sum and count are implemented.

### 17. resample_timeseries_bins.py
**Entry fn:** `def parse_timestamp(ts: str) -> tuple:`, `def bucket_hourly(records: List[Dict[str, Any]]) -> Dict[tuple, float]:`, `def bucket_daily(records: List[Dict[str, Any]]) -> Dict[tuple, float]:`, `def brute_force_hourly(records: List[Dict[str, Any]]) -> Dict[tuple, float]:`
**Valid input:** `records` are dicts with keys `"timestamp"` (`"YYYY-MM-DD HH:MM"`) and `"value"` (numeric).
**Core:** Buckets timestamped records by hour or day and sums their values. A brute-force reference recomputes each bucket from the full dataset.
**Assert:** On five planted records, hourly and daily bucket sums match the brute-force reference and the hand-computed totals (Jan 15 = 35, Jan 16 = 23; hour bins sum correctly).
**⚠️ Defect:** `parse_timestamp` has no error handling for malformed timestamps and assumes the exact `"YYYY-MM-DD HH:MM"` format. It also discards minutes, so all records within the same hour are binned together regardless of minute. `brute_force_hourly` is O(n²) because it re-parses every timestamp for every record; it is only usable for tiny demos. There is no generic frequency parameter.

### 18. rolling_join_asof.py
**Entry fn:** `def asof_join(left: List[Dict[str, Any]], right: List[Dict[str, Any]], key: str) -> List[Dict[str, Any]]:`, `def brute_force_asof(left: List[Dict[str, Any]], right: List[Dict[str, Any]], key: str) -> List[Dict[str, Any]]:`
**Valid input:** `left` and `right` non-empty lists of dicts; `key` present and comparable in every row; right rows are sortable by `key`.
**Core:** As-of join (rolling join): for each left row, find the right row with the largest `key` less than or equal to the left `key`, then merge the rows. The result is verified against a brute-force reference.
**Assert:** On planted trades [100, 150, 200] and quotes [80, 120, 180], each trade matches the preceding quote, and the as-of join output matches the brute-force output exactly.
**⚠️ Defect:** `asof_join` sorts the right table but then performs a linear scan (`for right_row in reversed(right_sorted)`) for every left row, giving O(n·m) time instead of the O(n log n + m log n) binary-search solution the docstring mentions. There is no validation that `key` exists or that the key values are comparable, and no handling for duplicate right keys (the last duplicate wins).

### 19. sort_multi_key.py
**Entry fn:** `def multi_key_sort(records: List[Dict[str, Any]], keys: List[tuple]) -> List[Dict[str, Any]]:`, `def sort_key(record):`
**Valid input:** `records` non-empty; each `key` tuple is `(key_name: str, is_asc: bool)`; sortable values for the requested keys.
**Core:** Stable multi-key sort with per-key ascending/descending direction. Uses Python's `sorted` with a generated sort key.
**Assert:** On planted records with ties, sorting by `(category, asc)` then `(value, desc)` yields categories [A, A, A, B, B], A values [20, 20, 10], and tied rows preserve their original order (stability check: A/20 records keep order [2, 4]).
**⚠️ Defect:** For descending string keys, the sort key is `(1, val)`, which does **not** reverse string order — the leading `1` is constant for all strings, so comparison falls back to ascending string order. Only descending numeric keys work correctly because they are negated. The demo uses a descending numeric key, so the string bug is hidden. Also `sort_key` is exposed as a module-level function despite being an internal helper.

### 20. window_functions.py
**Entry fn:** `def apply_window_functions(records: List[Dict[str, Any]], partition_key: str, order_key: str) -> List[Dict[str, Any]]:`
**Valid input:** `records` non-empty; `partition_key` and `order_key` exist in every record; values under `order_key` are comparable.
**Core:** Per-partition window functions: adds `row_number`, `rank`, `dense_rank`, `lag_value`, `lead_value`, and `running_sum` after sorting each partition by `order_key`.
**Assert:** On planted records partitioned by category and ordered by value, category A gets row numbers [1, 2, 3], lag/lead values are correct at the boundaries, and running sums are [5, 15, 35] for sorted A values 5, 10, 20.
**⚠️ Defect:** `rank` and `dense_rank` ignore ties entirely: they are computed as `i + 1` rather than using the actual rank semantics for equal `order_key` values. The docstring names rank and dense_rank, but the implementation is wrong for tied values. The function also hardcodes the value column as `"value"`; it cannot compute lag/lead on any other column. Output records are returned in sorted-by-partition order, not the original input order, which breaks the natural expectation for row_number over a dataset.

---

*5S · Batch 20 detail docs · 2026-07-21*
