# Batch 11 — DS Pattern Detail Docs (20 patterns)

## Category: model_diagnostics (10 patterns)

### 1. bias_variance_decomposition.py
**Entry fn:** `bootstrap_bias_variance(train_data, test_x, degree, n_bootstraps=100) → (bias, variance, mse)`
**Valid input:** `train_data: List[Tuple[float, float]]` — (x, y) pairs. `test_x: List[float]`. `degree` in {0, 1, 2}. `n_bootstraps ≥ 1`.
**Core:** Bootstrap bias-variance decomposition on synthetic data y = 0.5 + 0.1x² + N(0,0.2). For each bootstrap: resample training data, fit polynomial of given degree, predict on test grid. Bias² = E[(mean_pred - true)²], Variance = E[(pred - mean_pred)²]. Compares constant (high bias) vs linear (medium bias) models.
**Assert:** On 100 training samples, 50 test points, 50 bootstraps: constant model bias > linear model bias, and constant bias > 0.25.
**⚠️ Defect:** The `polyfit` function has hardcoded formulas for degrees 0, 1, 2 only. Degree 3 returns `[0,0,0,0]` (placeholder zeros). The test only uses degrees 0 and 1, so this is fine, but the function claims to support arbitrary degrees. Also, the test only checks bias, not variance — the "variance decomposition" part is computed but not asserted.

### 2. bootstrap_model_comparison.py
**Entry fn:** `bootstrap_model_comparison(test_data, model1, model2, n_bootstraps=100) → (wins1, wins2, win_rate1)`
**Valid input:** `test_data: List[Tuple[float, float]]` — (x, y) pairs. `model1, model2: Callable[[float], float]`. `n_bootstraps ≥ 1`.
**Core:** Compare two models via paired bootstrap on the same test set. Resample test set with replacement, compute MAE for both models on each bootstrap, count wins. Model A (true: 2x) vs Model B (biased: 1.8x) on y = 2x + N(0,1).
**Assert:** On 200 test samples, 100 bootstraps: better model (A) wins > 70% of samples. Identical models produce few wins (ties dominate).
**⚠️ Defect:** The "identical models" test asserts `wins_same1 + wins_same2 < 50`, but with floating-point MAE on resampled data, identical models can produce tiny differences due to floating-point arithmetic, causing false wins. The threshold of 50 is arbitrary and may fail on some seeds. Also, the test doesn't check that ties are handled correctly (they're silently ignored).

### 3. calibration_curve.py
**Entry fn:** `calibration_curve(scores, labels, n_bins=5) → (bin_centers, predicted_probs, observed_freqs)`
**Valid input:** `scores: List[float]` in [0, 1]. `labels: List[int]` — 0 or 1. `n_bins ≥ 1`.
**Core:** Evaluate classifier calibration by binning predicted probabilities. For each bin: compute average predicted probability and observed frequency. Also computes Brier score (MSE of predictions) and ECE (mean |predicted - observed| across bins). Well-calibrated data (P(y=1) = score) vs overconfident data (scores skewed to extremes, labels uniform).
**Assert:** On 500 samples: well-calibrated model has lower ECE and lower Brier score than overconfident model.
**⚠️ Defect:** The "overconfident" data generation creates scores that are bimodal (clustered at 0-0.2, 0.4-0.6, 0.8-1.0) while labels are uniform 50/50. This is a specific kind of miscalibration, but the test doesn't verify the direction of miscalibration (over vs under). A model that's underconfident would also have high ECE but the test can't distinguish.

### 4. gaussian_naive_bayes.py
**Entry fn:** `fit_gaussian_naive_bayes(X, y) → (class_priors, means_per_class, stds_per_class, classes)`, `predict_gaussian_naive_bayes(x, ...) → int`
**Valid input:** `X: List[Tuple[float, float]]` — 2D features. `y: List[int]` — class labels.
**Core:** Gaussian Naive Bayes classifier. For each class, compute per-feature mean and std (using sample variance, denominator n-1). Predict: posterior ∝ prior × Π P(feature|class) using Gaussian PDF. Assumes feature independence given class.
**Assert:** On 2-class 2D Gaussian data (100 train, 100 test, means at (0,0) and (3,3), σ=1), accuracy ≥ 90%.
**⚠️ Defect:** The `gaussian_probability` function uses `std` in the denominator but doesn't check for `std == 0` properly — it returns 0 for zero std, but the correct behavior would be a delta function (infinite density at the mean). The `max(1, len(feat_values) - 1)` in variance computation is a hack that gives incorrect variance for single-point classes.

### 5. learning_curve.py
**Entry fn:** `learning_curve_analysis()` — no return, prints PASS.
**Valid input:** Uses internal `generate_linear_data(200, seed=42)`.
**Core:** Fit linear model on increasing training set sizes (10, 30, 50, 80, 120, 150). Training error should be low and stable. Validation error should start high and decrease with more data, demonstrating the learning curve pattern.
**Assert:** On 150 train + 50 validation points (y = 2x + N(0,1)): final training error < 2.0, validation error > training error at smallest size, validation error decreases with more data.
**⚠️ Defect:** The test asserts `val_errors[-1] < val_errors[0]` (validation error decreases), but this is a monotonicity check that can fail due to random variation in the data split. With only 50 validation points, the validation error at size 150 could be slightly higher than at size 10 by chance. A statistical test or averaging over multiple splits would be more robust.

### 6. lift_gain_chart.py
**Entry fn:** `lift_gain_chart(scores, labels, n_deciles=10) → (decile_percentages, gains, lifts)`
**Valid input:** `scores: List[float]` — predicted scores. `labels: List[int]` — 0 or 1. `n_deciles ≥ 1`.
**Core:** Compute cumulative gain (% of positives captured) and lift (positive rate / base rate) by decile. Sort by score descending. Strong classifier (signal_strength=0.8) should have high lift in top decile. Random classifier (signal_strength=0) should have lift ≈ 1 throughout.
**Assert:** On 100 positives + 400 negatives: strong classifier top decile lift > 1.5, random classifier average lift within [0.7, 1.3], strong gain > random gain at top decile.
**⚠️ Defect:** The `generate_scored_labels` function uses `signal_strength` to shift the score distributions, but the scores are clipped to [0, 1] with `max(0, min(1, score))`. For high signal_strength, the clipping can cause score saturation (many scores at exactly 0 or 1), which distorts the lift calculation at extreme deciles.

### 7. precision_recall_curve.py
**Entry fn:** `compute_pr_curve(scores, labels, n_points=100) → (thresholds, precisions, recalls)`, `average_precision(recalls, precisions) → float`
**Valid input:** `scores: List[float]` — predicted scores. `labels: List[int]` — 0 or 1.
**Core:** Compute precision-recall curve by varying decision threshold. Strong classifier (scores at 0.7 for positives, 0.3 for negatives, noise=0.1) should have high AP. Weak classifier (random scores) should have AP near base rate.
**Assert:** On 50 positives + 50 negatives: strong classifier AP > 0.8, weak classifier AP < 0.6, strong AP > weak AP.
**⚠️ Defect:** The `average_precision` function uses the trapezoidal rule on the raw PR curve, which overestimates AP compared to the standard definition (interpolated precision at each recall level). The trapezoidal rule can give AP > 1.0 for curves that hug the top-right corner, though the test thresholds are set low enough to avoid this.

### 8. rank_correlation.py
**Entry fn:** `spearman_correlation(x, y) → float`, `kendall_tau(x, y) → float`
**Valid input:** `x, y: List[float]` — same length, at least 2 samples.
**Core:** Spearman's rho: Pearson correlation on ranks. Kendall's tau: (concordant - discordant) / total pairs. Both measure monotonic association. Tested on perfect monotone (rho=1, tau=1), independent random (rho≈0, tau≈0), and perfect decreasing (rho=-1, tau=-1).
**Assert:** Perfect increasing: rho=1, tau=1 (within 0.01). Random 100 samples: |rho| < 0.4, |tau| < 0.4. Perfect decreasing: rho=-1, tau=-1 (within 0.01).
**⚠️ Defect:** Kendall's tau is O(n²) — for n=100 it computes 4,950 pairs, which is fine, but for n > 10,000 it becomes prohibitive. The test uses n=100 for random data, which is reasonable, but the function has no early-exit or approximation for large n. Also, tied pairs are silently ignored rather than using tau-b correction.

### 9. residual_analysis.py
**Entry fn:** `residual_analysis_test()` — no return, prints PASS.
**Valid input:** Uses internal `generate_quadratic_data(100, seed=42)`.
**Core:** Fit linear model to quadratic data (y = 1 + 0.5x + 0.3x² + N(0,0.3)). Compute residuals and check correlation with omitted x² term. Then fit quadratic model and verify residuals no longer show structure. Demonstrates residual analysis for detecting model misspecification.
**Assert:** On 100 samples: linear residuals correlate with x² (|corr| > 0.5). Quadratic residuals have correlation with x² reduced to < 30% of linear correlation.
**⚠️ Defect:** The test asserts `abs(corr_quad) < abs(corr_lin) * 0.3`, which is a relative threshold. If the linear correlation is very high (e.g., 0.99), the quadratic residual correlation must be < 0.3, which is reasonable. But if the linear correlation is barely above 0.5, the quadratic residual correlation must be < 0.15, which may fail if the quadratic fit is imperfect due to noise.

### 10. ucb_bandit.py
**Entry fn:** `run_ucb1_experiment(arms, n_pulls, c=1.0) → (counts, rewards_sum)`
**Valid input:** `arms: List[BernoulliArm]` — each with `p` in [0, 1]. `n_pulls ≥ 1`. `c ≥ 0`.
**Core:** UCB1 multi-armed bandit. Select arm with highest UCB = avg_reward + c·√(ln(total_pulls) / arm_pulls). Unplayed arms get infinite UCB (always selected first). Three Bernoulli arms: p=[0.1, 0.5, 0.9]. Best arm (p=0.9) should receive most pulls.
**Assert:** On 500 pulls with c=1.0: best arm pulled more than worst and medium, best arm pulled > 50% of time, best arm pulled more than random baseline (1/3).
**⚠️ Defect:** The `ucb1_select_arm` function returns `float('inf')` for unplayed arms, which works but `float('inf')` comparison can behave unexpectedly in edge cases (e.g., if all arms are unplayed, it returns index 0). Also, the exploration constant c=1.0 is the standard UCB1 value, but the test doesn't verify that the regret is sublinear (logarithmic) — it only checks that the best arm is pulled most, which is a weaker claim.

---

## Category: clustering_graph_and_anomaly (10 patterns)

### 11. betweenness_centrality.py
**Entry fn:** `betweenness_centrality(graph) → Dict[int, float]`
**Valid input:** `graph: Dict[int, List[int]]` — adjacency list, undirected. At least 3 nodes.
**Core:** Brandes' algorithm for betweenness centrality. For each source node s: BFS to find shortest path distances and counts, then dependency accumulation in reverse topological order. Normalized by (n-1)(n-2)/2 for undirected graphs. Bridge node between two clusters should have highest score.
**Assert:** On a 10-node graph with two 4-node clusters connected by a bridge node (5): node 5 has the highest betweenness, higher than any cluster node.
**⚠️ Defect:** The normalization factor `2.0 / ((n-1)*(n-2))` is correct for undirected graphs, but the code uses `n = len(nodes)` which counts all nodes including the source. The standard Brandes algorithm excludes the source node from normalization, so for n=10, the factor should be 2/(9×8) = 1/36, which matches. However, the code doesn't handle directed graphs or weighted edges.

### 12. classic_mds.py
**Entry fn:** `classical_mds_2d(points) → List[Tuple[float, float]]`
**Valid input:** `points: List[Tuple[float, ...]]` — at least 2 points, all same dimension.
**Core:** Classical MDS: compute centered Gram matrix from high-dimensional points, then approximate 2D embedding using the first two rows of the Gram matrix. Preserves pairwise distances approximately. Tested on 40 random 50D points.
**Assert:** On 40 points in 50D: embedding size matches input, embedding is not all zeros, distance correlation > 0.3 or < 0.1 (lenient threshold).
**⚠️ Defect:** This is NOT true classical MDS. True MDS requires eigendecomposition of the doubly-centered distance matrix. This implementation uses the Gram matrix of the original points (which requires the original coordinates, defeating the purpose of MDS) and a heuristic projection (G[i][0] ± G[i][1]) instead of proper eigendecomposition. The distance correlation assertion is extremely lenient (0.3) and the fallback `abs(correlation) < 0.1` means a correlation of 0.0 also passes.

### 13. dbscan_clustering.py
**Entry fn:** `dbscan(points, eps, min_pts) → List[int]`
**Valid input:** `points: List[Tuple[float, ...]]` — at least 1 point. `eps > 0`. `min_pts ≥ 1`.
**Core:** DBSCAN: density-based clustering. For each unvisited point: find neighbors within eps. If core point (≥ min_pts neighbors), start new cluster and expand via BFS. Points not reachable from any core point are labeled noise (-1).
**Assert:** On 2 planted Gaussian clusters (20 pts each at (2,2) and (8,8), σ=0.3) + 5 uniform noise points, eps=1.0, min_pts=5: finds exactly 2 clusters, at least 3 noise points.
**⚠️ Defect:** The `expand_cluster` function has a bug in the label check logic. Line 77: `elif labels[current] != -1: continue` — this condition is always true when `labels[current]` is not -1, but the `elif` means it only runs when the `if` above (labels[current] == -1) is false. However, `labels[current]` could be 0 (a cluster label from a previous expansion), and the code would skip it, potentially missing connections between clusters. The BFS should check if the point has been visited in this expansion, not just if it has any label.

### 14. elbow_method_kmeans.py
**Entry fn:** `kmeans(points, k, max_iterations=100, seed=42) → (labels, centroids, inertia)`, `elbow_knee(inertias) → int`
**Valid input:** `points: List[Tuple[float, ...]]` — at least k points. `k ≥ 1`.
**Core:** K-means with k-means++ initialization (probabilistic, distance-squared weighting). Compute inertia (sum of squared distances to centroids) for k=1..6. Find elbow via second derivative heuristic: largest change in acceleration of the inertia curve.
**Assert:** On 3 planted Gaussian clusters (20 pts each at (0,0), (6,6), (12,0), σ=0.4): elbow detected at k=3, and inertia drop from k=2 to k=3 > drop from k=3 to k=4.
**⚠️ Defect:** The k-means++ initialization uses a cumulative-sum approach (`cumsum += distances[i]`) but the random threshold `r = random.random() * total_dist` is compared against `cumsum` which accumulates raw distances, not probabilities. This is correct because `cumsum` goes from 0 to `total_dist`, matching the random range. However, the `break` after selecting a centroid means only one candidate is considered per iteration, which is correct for k-means++ but the implementation is fragile — if `total_dist` is 0 (all points identical), it falls back to `random.choice(points)`.

### 15. hierarchical_agglomerative.py
**Entry fn:** `hierarchical_agglomerative(points, linkage="complete") → (clusters, merge_history)`, `cut_dendrogram(points, k, linkage="complete") → List[int]`
**Valid input:** `points: List[Tuple[float, ...]]` — at least 2 points. `linkage` in {"single", "complete"}.
**Core:** Bottom-up hierarchical clustering. Start with each point as its own cluster. Repeatedly merge the two closest clusters (single/min or complete/max linkage). Cut dendrogram at k clusters. Tested on 3 well-separated Gaussian clusters (10 pts each).
**Assert:** On 3 clusters (10 pts each at (0,0), (5,5), (10,0), σ=0.5): cut at k=3 produces exactly 3 clusters, each original cluster is at most 2-way fragmented.
**⚠️ Defect:** The algorithm is O(n³) due to recomputing all pairwise cluster distances at each merge step. For n=30 points, this is fine (~4,000 distance computations per merge × 29 merges). For n > 1,000, this becomes prohibitive. A proper implementation would use a distance matrix with lazy updates (Lance-Williams formula). Also, the `cluster_distance` function recomputes all pairwise distances between clusters each time, with no caching.

### 16. isolation_tree_anomaly.py
**Entry fn:** `isolation_forest_anomaly_score(points, num_trees=50, seed=42) → List[float]`
**Valid input:** `points: List[Tuple[float, ...]]` — at least 2 points. `num_trees ≥ 1`.
**Core:** Isolation forest for anomaly detection. Build ensemble of random isolation trees: randomly select feature and split value, recurse until single point or max depth. Anomaly score = average path length across trees (shorter = more anomalous). Tested on 100 normal points (Gaussian cluster) + 5 outliers.
**Assert:** On 100 normal + 5 outlier points: average outlier path length < average normal path length, all scores positive.
**⚠️ Defect:** The `build_isolation_tree` function returns a leaf node when `min_val == max_val` (can't split), but this check is done AFTER selecting the split feature. If all points have the same value for the randomly selected feature but differ on other features, the algorithm gives up instead of trying another feature. Also, the max_depth of 10 is hardcoded and may be too shallow for large datasets (the expected path length for n=100 is ~log₂(100) ≈ 7, so 10 is adequate here).

### 17. label_propagation_communities.py
**Entry fn:** `label_propagation(graph, max_iterations=100, seed=42) → Dict[int, int]`
**Valid input:** `graph: Dict[int, List[int]]` — adjacency list, undirected. At least 2 nodes.
**Core:** Label propagation for community detection. Each node starts with a unique label. Iteratively: randomize node order, each node adopts the most common label among its neighbors (ties broken randomly). Converges when no labels change. Two 4-node communities connected by a single cross-edge.
**Assert:** On 8-node graph (two communities 0-3 and 4-7, single cross-edge 3-4): at least 2 communities found, each original cluster recovered at ≥ 50%.
**⚠️ Defect:** Label propagation is non-deterministic due to random tie-breaking and random update order. The test uses `seed=42` for reproducibility, but different graph topologies can produce different results across runs. The recovery threshold of 50% is very lenient — a community detection that only recovers half the nodes is barely useful. Also, the algorithm can converge to a single community (all nodes same label) if the cross-edge is strong enough, which would fail the `num_communities >= 2` assertion.

### 18. linear_discriminant_analysis.py
**Entry fn:** `lda_2d(points, labels) → (weights, threshold)`
**Valid input:** `points: List[Tuple[float, float]]` — 2D points. `labels: List[int]` — binary (0 or 1). At least 1 point per class.
**Core:** Two-class LDA in 2D. Compute class means, within-class scatter matrices S_w, between-class scatter S_b. Solve S_w⁻¹ S_b w = λw via power iteration on the 2×2 matrix. Projection threshold at midpoint of projected means.
**Assert:** On 2 Gaussian classes (30 pts each, means at (1,1) and (4,4), σ=0.5): classification accuracy ≥ 90%, weights non-zero.
**⚠️ Defect:** The power iteration for the 2×2 matrix uses a fixed initial vector [1.0, 1.0] with no random restart. If the true eigenvector is orthogonal to [1, 1] (e.g., [1, -1]), power iteration would converge slowly or not at all. The eigenvalue computation on line 52 is inside the loop but uses the updated `v`, which is correct but the indentation suggests it was meant to be after the loop. Also, the 2×2 matrix inverse returns identity if singular, silently hiding numerical issues.

### 19. random_projection_jl.py
**Entry fn:** `random_projection_matrix(original_dim, target_dim, seed=42) → List[List[float]]`, `project_point(point, projection_matrix) → Tuple[float, ...]`
**Valid input:** `original_dim > target_dim ≥ 1`. `point` dimension matches `original_dim`.
**Core:** Johnson-Lindenstrauss random projection. Generate Gaussian random matrix, normalize rows to unit norm. Project 50D points to 20D. JL lemma guarantees pairwise distances are approximately preserved. Tested on 42 points from 3 planted clusters in 50D.
**Assert:** On 42 points (3 clusters, 50D → 20D): Pearson correlation between original and projected pairwise distances > 0.9.
**⚠️ Defect:** The row normalization (dividing each row by its L2 norm) is non-standard for JL projections. Standard JL uses unnormalized Gaussian entries scaled by 1/√(target_dim). Row normalization changes the distribution of the projection and may affect the distance preservation guarantees. The test still passes because the normalization preserves relative distances, but the theoretical JL guarantee no longer directly applies.

### 20. silhouette_score.py
**Entry fn:** `silhouette_score(points, labels) → float`
**Valid input:** `points: List[Tuple[float, ...]]` — at least 2 points. `labels: List[int]` — at least 2 unique labels.
**Core:** Silhouette score: for each point, a = mean distance to same-cluster points, b = min mean distance to other-cluster points. Score = (b-a)/max(a,b). Range [-1, 1]. Higher is better. Tested on 2 well-separated Gaussian clusters (15 pts each at (0,0) and (5,0), σ=0.4).
**Assert:** Correct clustering score ≥ 0.5 and > 0. Scrambled labels score < 0.5.
**⚠️ Defect:** The test asserts `wrong_score >= 0.5` for the "wrong" clustering (labels swapped), which is trivially true because swapping labels on symmetric clusters gives the same score. The test then shuffles labels and checks `scrambled_score < 0.5`, but `random.shuffle(correct_labels)` modifies the list in-place after it was already used for `correct_score`, so `correct_labels` is now the shuffled version. This means the "scrambled" test uses the shuffled labels, which is correct, but the variable name `correct_labels` is misleading after the shuffle.