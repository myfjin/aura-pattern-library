# Batch 9 — DS Pattern Detail Docs (20 patterns)

## Category: core_ml (10 patterns)

### 1. kmeans_clustering.py
**Entry fn:** `kmeans(X, k, max_iterations=100, tolerance=1e-4) → (centroids, assignments)`
**Valid input:** `X: List[List[float]]` — at least k samples, all same length. `k: int` ≥ 2. `max_iterations` ≥ 1.
**Core:** Standard k-means: randomly initialize k centroids from data, assign each point to nearest centroid (Euclidean), recompute centroids as cluster means, repeat until centroid movement < tolerance or max iterations. Returns final centroids and assignments.
**Assert:** On 3 synthetic Gaussian clusters (20 pts each, well-separated at (0,0), (5,0), (2.5,4) with σ=0.5), intra-cluster distance < 2.0 and min centroid distance > 2.0.
**⚠️ Defect:** The test computes `correct` (line 121) but never uses it — the `for` loop body is `pass`. The test only checks cluster tightness and separation, not whether points are assigned to the correct cluster. A degenerate solution (all points in one cluster) could pass if centroids happened to be far apart.

### 2. knn_classifier.py
**Entry fn:** `knn_predict(x_test, X_train, y_train, k=3) → int`
**Valid input:** `x_test: List[float]` same length as X_train rows. `X_train: List[List[float]]` non-empty. `k: int` ≤ len(X_train).
**Core:** Lazy learner: no training phase. For a test point, compute Euclidean distance to all training points, sort by distance, take k nearest, return majority class label via `max(votes, key=votes.get)`.
**Assert:** On 2-class synthetic data (50 train, 20 test, Gaussian clusters at (0,0) and (5,5) with σ=1), k=5 accuracy ≥ 80%.
**⚠️ Defect:** No tie-breaking. `max(votes, key=votes.get)` returns the first key with max votes, which is arbitrary on ties. With even k, ties are possible (e.g., k=4 with 2 votes each). A proper implementation would use a tie-breaking rule (e.g., smallest class label or nearest-neighbor preference).

### 3. linear_regression_gd.py
**Entry fn:** `linear_regression_gd(X, y, learning_rate=0.01, iterations=100) → (weights, bias)`
**Valid input:** `X: List[List[float]]` non-empty, all same length. `y: List[float]` same length as X. `learning_rate > 0`.
**Core:** Batch gradient descent for linear regression. Initialize w=0, b=0. Each iteration: compute predictions ŷ = Xw + b, MSE loss, gradients dw = (1/n) Σ (ŷᵢ - yᵢ) xᵢ, db = (1/n) Σ (ŷᵢ - yᵢ), update w ← w - lr·dw, b ← b - lr·db.
**Assert:** On y = 2·x₁ + 3·x₂ + N(0,0.5) with 30 samples, 200 iterations, R² > 0.8, |w₀ - 2| < 0.5, |w₁ - 3| < 0.5.
**⚠️ Defect:** Fixed iteration count with no convergence check. If learning rate is too high, it may diverge; if too low, it may not converge in 100 iterations. No early stopping on gradient norm or loss plateau. The caller must tune lr and iterations together.

### 4. logistic_regression.py
**Entry fn:** `logistic_regression_fit(X, y, learning_rate=0.01, iterations=100) → (weights, bias)`
**Valid input:** `X: List[List[float]]` non-empty. `y: List[int]` with values 0 or 1. `learning_rate > 0`.
**Core:** Binary logistic regression via gradient descent. Sigmoid σ(z) = 1/(1+e⁻ᶻ) with overflow clamp (z > 100 → 1, z < -100 → 0). Binary cross-entropy loss. Initialize w=0, b=0. Each iteration: compute p = σ(Xw + b), gradients dw = (1/n) Σ (pᵢ - yᵢ) xᵢ, db = (1/n) Σ (pᵢ - yᵢ), update.
**Assert:** On 2-class synthetic data (2 features, 30 samples per class, Gaussian clusters at (2,2) and (5,5) with σ=1.5), accuracy > 80%.
**⚠️ Defect:** Same fixed-iteration issue as linear_regression_gd. No convergence check, no adaptive learning rate. The sigmoid clamp at ±100 is numerically safe but the fixed step count means the model may not have converged for harder separation boundaries.

### 5. naive_bayes_text.py
**Entry fn:** `naive_bayes_train(texts, labels) → (class_priors, word_probs)`, `naive_bayes_predict(text, class_priors, word_probs) → int`
**Valid input:** `texts: List[List[str]]` non-empty. `labels: List[int]` same length, values 0 or 1.
**Core:** Multinomial Naive Bayes for text. Train: compute P(class) from class frequencies, P(word|class) = (count(word in class) + 1) / (total words in class + V) with Laplace smoothing α=1. Predict: argmax_c log P(c) + Σ log P(word|c).
**Assert:** On synthetic 2-class documents (10 spam, 10 ham, 5-word vocab each), training accuracy ≥ 90%, and held-out test words classify correctly.
**⚠️ Defect:** The `naive_bayes_predict` function computes the unseen-word probability differently from training. For unseen words, it uses `1.0 / (sum(len(wp) for wp in word_probs.values()) + vocab_size)` inside the loop, which recomputes the denominator per word and uses a different formula than the training Laplace smoothing. This means the probability of unseen words doesn't match the generative model trained in `naive_bayes_train`.

### 6. perceptron.py
**Entry fn:** `perceptron_fit(X, y, learning_rate=1.0, max_iterations=100) → (weights, bias)`
**Valid input:** `X: List[List[float]]` non-empty. `y: List[int]` with values 0 or 1 (converted internally to {-1, +1}).
**Core:** Perceptron learning rule. Convert labels to {-1, +1}. Initialize w=0, b=0. For each misclassified sample: w ← w + lr·(yᵢ - ŷ)·xᵢ/2, b ← b + lr·(yᵢ - ŷ)/2. Converges in finite steps on separable data.
**Assert:** On linearly separable 2D data (2 classes, 20 pts each, separated by a margin of 0.5-2.5), accuracy ≥ 90%.
**⚠️ Defect:** The update rule uses `error = y_labels[i] - pred` divided by 2.0, which is non-standard. Classic perceptron: w ← w + yᵢ·xᵢ. This implementation uses w ← w + lr·(yᵢ - ŷ)·xᵢ/2, which is closer to a gradient descent update on squared error than the classic perceptron rule. It still converges on separable data but the convergence proof doesn't directly apply.

### 7. pca_power_iteration.py
**Entry fn:** `pca_power_iteration(X, n_components=1) → (eigenvectors, eigenvalues)`
**Valid input:** `X: List[List[float]]` — centered data (mean 0 per column). `n_components: int` ≤ n_features.
**Core:** PCA via power iteration. Center data (subtract column means). Compute covariance matrix. Find top eigenvector via power iteration: v ← (XᵀX)v / ||(XᵀX)v||. Deflate by subtracting eigenvalue·v·vᵀ. Repeat for n_components.
**Assert:** On 2D synthetic data (50 samples, variance mostly in first dimension: σ₁=3, σ₂=0.5), eigenvalue[0] > eigenvalue[1] and eigenvalue[0] > 2.0.
**⚠️ Defect:** The test only checks eigenvalue ordering and magnitude, not eigenvector orthogonality or reconstruction error. The deflation step may accumulate numerical error, and there's no verification that the recovered components are actually orthogonal or that the projection preserves variance as claimed.

### 8. ridge_regression_normal_eq.py
**Entry fn:** `ridge_regression_normal_eq(X, y, lambda_reg=0.01) → weights`
**Valid input:** `X: List[List[float]]` — n_samples × n_features. `y: List[float]` length n_samples. `lambda_reg ≥ 0`.
**Core:** Ridge regression (L2-regularized linear regression) solved via normal equations. Compute XᵀX + λI and Xᵀy, solve via Gaussian elimination with partial pivoting. Matrix ops (transpose, multiply, solve) implemented from scratch.
**Assert:** On y = 2·x₁ + 3·x₂ - 1·x₃ + N(0,0.5) with 30 samples, λ=0.01, R² > 0.8 and all weights within 1.0 of true.
**⚠️ Defect:** No bias/intercept term. The normal equations solve Xw = y without an augmented bias column. The return type is `List[float]` (weights only), not `(weights, bias)` as the docstring implies. This works when the true model has no intercept, but will produce biased estimates when one is needed.

### 9. decision_tree_id3.py
**Entry fn:** `decision_tree_id3(X, y, max_depth=5) → tree (nested dict)`
**Valid input:** `X: List[List[float]]` non-empty. `y: List[int]` class labels. `max_depth ≥ 1`.
**Core:** ID3-style decision tree. Compute Gini impurity (not entropy despite "ID3" name). For each feature, find best split threshold maximizing information gain = Gini(parent) - Σ (nᵢ/n)·Gini(childᵢ). Recurse until pure leaf, max depth, or min_samples. Tree as nested dicts with 'feature', 'threshold', 'left', 'right', 'value' keys.
**Assert:** On 2-class synthetic data (2 features, 30 per class, Gaussian clusters at (3,3) and (7,7) with σ=2), accuracy > 80%.
**⚠️ Defect:** The tree uses Gini impurity for splitting, not entropy — despite being called "ID3" (which traditionally uses entropy/information gain). The docstring says "information gain (reduction in entropy)" but the code uses Gini. Also, the test only checks training accuracy, not held-out generalization, so overfitting is undetected.

### 10. gaussian_mixture_em.py
**Entry fn:** `em_fit_1d(X, k, max_iterations=100, tolerance=1e-6) → (means, variances, weights)`
**Valid input:** `X: List[float]` — 1D data, non-empty. `k: int` ≥ 1. `max_iterations ≥ 1`.
**Core:** 1D Gaussian Mixture Model via EM. E-step: compute responsibilities γᵢⱼ = πⱼ·N(xᵢ|μⱼ,σⱼ²) / Σ πₖ·N(xᵢ|μₖ,σₖ²). M-step: update πⱼ, μⱼ, σⱼ². Initialize with random data points as means, equal variances/weights. Converges when log-likelihood change < tolerance.
**Assert:** On 2-component mixture (μ=0, μ=5, σ=1 each, 25 pts each), recovered means within 1.5 of true, variances positive, weights sum to 1.
**⚠️ Defect:** Random initialization with no multiple restarts. EM is highly sensitive to initialization and can converge to a local optimum (e.g., both components collapsing to the same mean). The test uses well-separated components (Δμ=5) so it works, but with closer components or unbalanced weights, a single random init is unreliable.

---

## Category: ensembles_and_robust_methods (10 patterns)

### 11. adaboost.py
**Entry fn:** `adaboost(X, y, n_rounds=10) → list of (stump, alpha)`
**Valid input:** `X: List[Tuple[float, float]]` — 2D features. `y: List[int]` with values 0 or 1. `n_rounds ≥ 1`.
**Core:** AdaBoost with decision stumps. Initialize sample weights wᵢ = 1/n. For each round: fit weighted stump (minimize weighted error), compute ε, set α = ½·ln((1-ε)/ε), reweight misclassified samples by exp(α), renormalize. Final prediction = sign(Σ αₜ·hₜ(x)).
**Assert:** On 2-class 2D synthetic data (40 per class, overlapping Gaussians at (4,4) and (6,6) with σ=2.5), ensemble accuracy > single stump accuracy.
**⚠️ Defect:** The `predict_ensemble` function converts stump predictions {0,1} to {-1,+1} for the weighted sum, but the conversion `1 if pred == 1 else -1` is fragile — if a stump ever returns a value other than 0 or 1 (e.g., due to a bug or extension), the sign flips silently. Also, the test only checks that AdaBoost beats a single stump, not that it achieves a meaningful accuracy level.

### 12. bagging_variance_reduction.py
**Entry fn:** `bagging_predict(X_train, y_train, X_test, n_bags=50) → list of float`
**Valid input:** `X_train, y_train` from `make_training_set`. `n_bags ≥ 1`.
**Core:** Bootstrap aggregating. Generate n_bags bootstrap resamples of training data. Fit a decision stump (depth-1 tree, minimizing SSE) on each. Average predictions across all bags. Key claim: bagging reduces prediction variance across retrainings compared to a single stump.
**Assert:** On y = 2x + N(0,3) with 60 training points, measured over 30 independent retrainings at 5 fixed test points, bagging (25 stumps) variance < 50% of single stump variance.
**⚠️ Defect:** The test uses R=30 retrainings, which is small for variance estimation (variance of variance is high with small R). The assertion `bagged_var < 0.5 * single_var` is a strong claim that may not hold on every random seed. A more robust test would use R ≥ 100 or a statistical test.

### 13. gradient_boosting_stumps.py
**Entry fn:** `gradient_boost(X, y, n_rounds=10, learning_rate=0.1) → (stumps, final_mse)`
**Valid input:** `X: List[Tuple[float, float]]` — 2D features. `y: List[float]` continuous. `learning_rate > 0`.
**Core:** Gradient boosting for regression. Initialize F₀(x) = 0. For m=1..M: compute residuals rᵢ = yᵢ - Fₘ₋₁(xᵢ), fit stump to residuals (minimize MSE), scale by learning rate, update Fₘ(x) = Fₘ₋₁(x) + lr·hₘ(x). Stump splits on gini criterion (minimize weighted MSE of residuals).
**Assert:** On 4-quadrant piecewise constant function (100 points in [0,10]², 4 regions with values 1,2,3,4 + N(0,0.2)), 50 rounds at lr=0.25, boosting MSE < single stump MSE / 1.15.
**⚠️ Defect:** The learning rate is baked into the stump values at storage time (`lr * left_val`), then the stored values are used directly at prediction time. This is correct but the naming is confusing — the stored `left_val`/`right_val` are already scaled by lr, so the predict function should NOT apply lr again. The code is consistent but a reader expecting standard gradient boosting (store raw values, apply lr at prediction) would find this surprising.

### 14. huber_robust_regression.py
**Entry fn:** `fit_line_huber(X, y, delta=1.5, learning_rate=0.05, iterations=300) → (m, b)`
**Valid input:** `X: List[float]` non-empty. `y: List[float]` same length. `delta > 0`. `learning_rate > 0`.
**Core:** Huber loss regression via gradient descent. Huber loss: L(r) = ½r² for |r| ≤ δ, δ(|r| - ½δ) for |r| > δ. Gradient: g(r) = r for |r| ≤ δ, δ·sign(r) for |r| > δ. Initialized with OLS estimate. Adaptive learning rate: lr / (1 + iter/100).
**Assert:** On y = 2x + 1 with 50 points (80% N(0,0.5), 20% heavy-tailed outliers ±[5,20]), Huber slope error < OLS slope error.
**⚠️ Defect:** The test only checks that Huber's slope error is less than OLS's, not that Huber actually recovers a good slope. If both are bad (e.g., too many outliers), the assertion still passes. Also, the adaptive learning rate schedule is a simple heuristic — it may not converge optimally for all data shapes.

### 15. ransac_robust_regression.py
**Entry fn:** `ransac_regression(X, y, n_iterations=100, threshold=1.0) → (m, b)`
**Valid input:** `X: List[float]` non-empty. `y: List[float]` same length. `n_iterations ≥ 1`. `threshold > 0`.
**Core:** RANSAC: randomly sample 2 points, fit line y = mx + b, count inliers (|y - (mx+b)| < threshold). Repeat n_iterations. Return model with most inliers. Robust to > 30% outliers.
**Assert:** On y = 2x + 1 with 50 inliers + 15 outliers (uniform ±[10,30]), RANSAC slope error < OLS slope error.
**⚠️ Defect:** No re-fit on all inliers. Standard RANSAC re-fits the model on all inliers of the best iteration, but this implementation returns the model from the random 2-point sample directly. This means the final model is based on only 2 points, not the full inlier set, reducing accuracy. Also, the threshold is hardcoded and not adaptive to data scale.

### 16. theil_sen_estimator.py
**Entry fn:** `theil_sen_estimator(X, y) → (m, b)`
**Valid input:** `X: List[float]` non-empty. `y: List[float]` same length.
**Core:** Theil-Sen: compute slope mᵢⱼ = (yⱼ - yᵢ) / (xⱼ - xᵢ) for all i < j. Take median slope. Intercept = median(yᵢ - m·xᵢ). Non-parametric, robust to outliers (breakdown point ~29%).
**Assert:** On y = 1.5x + 2 with 50 inliers + 12 outliers (uniform ±[20,40]), Theil-Sen slope error < OLS slope error.
**⚠️ Defect:** O(n²) pairwise slope computation. For n=62 (50+12), that's ~1,891 pairs, which is fine. But the doc doesn't mention the O(n²) cost, which becomes prohibitive for n > 10,000. A production implementation would use the Kendall-Theil median polish or subsampling.

### 17. spectral_clustering_lite.py
**Entry fn:** `spectral_cluster_two_moons(X) → list of int (cluster labels)`
**Valid input:** `X: List[Tuple[float, float]]` — 2D points. At least 2 samples.
**Core:** Build affinity matrix W[i,j] = exp(-||xᵢ - xⱼ||² / 2σ²). Sparsify to kNN graph (k=6). Compute graph Laplacian L = D - W. Find Fiedler vector (2nd smallest eigenvector) via shifted power iteration on (cI - L) with all-ones deflation. Cluster by sign of Fiedler vector.
**Assert:** On two-moons synthetic data (40 pts per moon, interleaved, noise=0.12), spectral accuracy ≥ 95% and beats k-means by ≥ 5%.
**⚠️ Defect:** The power iteration shift `c = 2.0 * max(L[i,i]) + 1.0` is a heuristic based on Gershgorin's theorem. If the Laplacian's spectrum is wider than expected (e.g., due to very tight clusters with large degree), the shift may not be sufficient to make the Fiedler vector the dominant eigenvector of (cI - L). The fixed 150 iterations may also not converge for poorly conditioned graphs.

### 18. stacking_ensemble.py
**Entry fn:** `fit_stacking(X, y, base_models, k_folds=5) → (base_models, b0, coef)`
**Valid input:** `X: List[Tuple[float, float]]` — 2D features. `y: List[int]` binary. `k_folds ≥ 2`.
**Core:** Stacking with out-of-fold meta-features. Split data into k_folds. For each fold: train base models (threshold classifiers on x[0] and x[1]) on out-of-fold data, predict on held-out fold. Collect meta-features. Train linear meta-learner on meta-features. Final: retrain base models on full data.
**Assert:** On 2-class synthetic data (50 per class, Gaussians at (2,2) and (8,8) with σ=2.5), stacking accuracy > average base model accuracy.
**⚠️ Defect:** The meta-learner's `fit_linear_model` only uses `X_base[i][0]` (line 28) — it fits the slope using only the first base model's predictions. The second coefficient is always 0.0. So stacking effectively only uses one base model, defeating the purpose of combining diverse models. The test still passes because the single base model is good enough, but the ensemble isn't actually stacking.

### 19. voting_classifier.py
**Entry fn:** `hard_voting(X, classifiers) → list of int`
**Valid input:** `X: List[Tuple[float, float]]` — 2D features. `classifiers: List` of trained weak classifiers.
**Core:** Hard voting classifier. Train multiple threshold-based weak classifiers (each splits on a different feature: x₁, x₂, x₁-x₂). Predict by majority vote across all classifiers. Ensemble accuracy exceeds average individual accuracy.
**Assert:** On 2-class 2D synthetic data (40 per class, Gaussians at (2,2) and (8,8) with σ=1.5), voting accuracy > average individual accuracy.
**⚠️ Defect:** The `hard_voting` and `soft_voting` functions are identical — both use `sum(votes) / len(votes)` thresholded at 0.5 on binary predictions. True soft voting would average probability estimates, not binary votes. The "soft voting" here is just hard voting with a different name. Also, the test only checks that voting beats the average, not that it achieves a meaningful accuracy level.

### 20. random_forest.py
**Entry fn:** `random_forest(X, y, n_trees=10) → list of trees (dicts)`
**Valid input:** `X: List[Tuple[float, float]]` — 2D features. `y: List[int]` class labels. `n_trees ≥ 1`.
**Core:** Random forest: train n_trees decision trees (max_depth=5, min_samples=2), each on a bootstrap sample of the data. At each split, consider a random subset of features (size ≈ √p). Each tree grown to max_depth. Prediction = majority vote across trees.
**Assert:** On 2-class 2D synthetic data (40 per class, Gaussians at (3,3) and (7,7) with σ=2), 10 trees, forest accuracy ≥ single tree accuracy.
**⚠️ Defect:** The test only checks training accuracy, not generalization. Forest ≥ single tree on training data is almost guaranteed because the forest has more capacity (10 trees × bootstrap diversity). A proper test would check held-out accuracy or OOB error. Also, the forest doesn't track OOB samples for unbiased evaluation, and the random feature subset is always `sqrt(n_features)` with no configurability.