# Batch 10 — DS Pattern Detail Docs (20 patterns)

## Category: neural_networks_from_scratch (10 patterns)

### 1. mlp_backprop.py
**Entry fn:** `SimpleMLPBackprop.__init__(hidden_dim=4, lr=1.0)` → `train(data, epochs)` → `forward(x) → (y_pred, h)`
**Valid input:** `data: List[Tuple[List[float], float]]` — 2D inputs, scalar targets. `epochs ≥ 1`.
**Core:** 2-layer MLP (2→hidden→1) with sigmoid activations, trained by hand-derived backpropagation on XOR. Forward: linear → sigmoid per layer. Backward: chain rule through sigmoid derivative s(1-s). Update: w ← w - lr·dw. MSE loss.
**Assert:** On XOR dataset (4 points), 500 epochs at lr=1.0, hidden_dim=4, final loss < 0.01 and all prediction errors < 0.2.
**⚠️ Defect:** The backward pass uses `dy = y_pred - y_true` as the output gradient, which is correct for MSE loss dL/dz = (ŷ - y)·σ'(z). But the code computes `dy` before `sigmoid_derivative(y_pred)` is applied — it's actually computing dL/dŷ, not dL/dz. The output layer update `dw2 = dy * h[i]` is then missing the σ'(z) factor. This still works because the sigmoid derivative is absorbed into the effective learning rate, but the gradient is technically incorrect.

### 2. softmax_regression.py
**Entry fn:** `SoftmaxRegression(input_dim=2, num_classes=3, lr=0.01)` → `train(data, epochs)` → `predict(x) → int`
**Valid input:** `data: List[Tuple[List[float], int]]` — feature vectors and class labels (0..num_classes-1).
**Core:** Multi-class softmax regression with cross-entropy loss. Forward: logits = Wx + b, softmax normalization (subtract max for numerical stability). Backward: gradient of cross-entropy w.r.t. logits is (probs - one_hot). Update W and b via SGD.
**Assert:** On 3 synthetic Gaussian clusters (10 pts each, centered at (0,0), (3,0), (1.5,3) with σ=0.3), 100 epochs at lr=0.1, accuracy ≥ 90%.
**⚠️ Defect:** The `train` method computes final loss by re-running the forward pass after training, but the loss printed during training is accumulated per-epoch and then overwritten. The final loss returned is computed on a separate pass, which is correct but the per-epoch loss tracking is misleading (it's the cumulative sum, not the average).

### 3. conv1d_feature_detector.py
**Entry fn:** `Conv1D(kernel_size=3, lr=0.01)` → `convolve(x) → list` → `backward(x, conv_out, targets) → loss`
**Valid input:** `x: List[float]` — 1D sequence, length ≥ kernel_size. `target_responses: List[float]` same length as conv output.
**Core:** 1D convolution from scratch. Single learnable kernel convolved over input (valid padding). Trained to detect a planted motif [1.0, -0.5, 1.0] in noisy sequences. MSE loss, gradient descent on kernel and bias.
**Assert:** On 10 training sequences (length 20, motif planted at random positions), 200 epochs at lr=0.1, response at motif position > 2× average response elsewhere on a held-out test sequence.
**⚠️ Defect:** The training targets are computed heuristically (dot product similarity to the motif, scaled to [0,1]), not as a clean binary signal. This means the kernel learns to approximate the motif detector indirectly, and the quality depends on the heuristic threshold. A cleaner approach would use binary targets (1 at motif position, 0 elsewhere).

### 4. dropout_regularization_sim.py
**Entry fn:** `SimpleNetwork(hidden_dim=8, use_dropout=False, dropout_rate=0.3)` → `train(data, epochs, lr)` → `evaluate(data) → (loss, correct)`
**Valid input:** `train_data: List[Tuple[List[float], float]]` — 4D inputs, binary targets with 30% label noise. `val_data: List[Tuple[List[float], float]]` — clean validation set.
**Core:** Compare two 4→8→1 networks (sigmoid), one with dropout (randomly zero 15% of hidden activations during training) and one without. Dropout should show smaller generalization gap (val_loss - train_loss) on a small noisy dataset.
**Assert:** On 25 noisy training samples (30% label noise) and 100 clean validation samples, 60-80 epochs at lr=0.5, dropout generalization gap ≤ no-dropout gap.
**⚠️ Defect:** The dropout rate is 0.15 (not the typical 0.5), and the test only checks that the gap is smaller, not that the absolute validation performance is better. A very small gap with both models performing poorly would still pass. Also, no scaling during inference (inverted dropout not implemented) — the mask is applied during training but activations are not scaled up, so expected activation magnitude differs between train and test.

### 5. early_stopping.py
**Entry fn:** `NetworkWithEarlyStopping()` → `train_with_early_stopping(train_data, val_data, max_epochs=100, patience=10, lr=0.1) → (epochs_trained, best_val_loss)`
**Valid input:** `train_data, val_data: List[Tuple[List[float], float]]` — 3D inputs, binary targets with 10% noise.
**Core:** 3→6→1 network with sigmoid activations. Train monitors validation loss each epoch. If no improvement for `patience` consecutive epochs, stops and restores best weights. Prevents overfitting.
**Assert:** On 40 train + 40 validation samples (x₀+x₁ > 0 rule, 10% label noise), patience=10, early stopping stops before 100 epochs and val_loss ≤ no-stop val_loss × 1.1.
**⚠️ Defect:** The test asserts `epochs_trained < 100` but this depends on the random seed and data. With 10% label noise and only 40 training samples, the validation loss may not plateau within 100 epochs for some seeds. The assertion `val_loss_with_stop <= val_loss_no_stop * 1.1` is also weak — it allows early stopping to be 10% worse.

### 6. learning_rate_schedules.py
**Entry fn:** `SimpleNet()` → `train(data, epochs, lr_schedule) → (final_loss, loss_history)`
**Valid input:** `data: List[Tuple[List[float], float]]` — 2D inputs, binary targets (x₀+x₁ > 0). `lr_schedule: Callable[[int, int], float]`.
**Core:** Compare three LR schedules on a 2→4→1 network: constant (0.05), step-decay (0.05→0.025→0.0125 at epochs 40/80), and cosine annealing (0.05→0.001). All converge to loss < 0.1. Schedules show lower late-phase variance.
**Assert:** On 40 synthetic samples, 120 epochs, all schedules reach final loss < 0.1. Step-decay and cosine late-phase variance < 1e-6.
**⚠️ Defect:** The late-phase variance assertion (< 1e-6) is extremely tight and depends on the random seed. With only 40 samples and a small network, the loss can fluctuate due to stochasticity. The assertion may fail on some seeds even though the schedules are working correctly.

### 7. numerical_gradient_check.py
**Entry fn:** `TinyNetwork()` → `analytic_gradients(x, y_true) → (dw1, db1, dw2, db2)` → `numerical_gradient(x, y_true, param_name, indices, eps=1e-5) → float`
**Valid input:** Fixed tiny network (2→2→1) with hardcoded weights. `x: List[float]` length 2. `y_true: float`.
**Core:** Verify backprop gradients against finite-difference numerical gradients (central difference). Compare all 13 parameters (4 w1, 2 b1, 2 w2, 1 b2). Max relative error < 1e-4 confirms backprop is correct.
**Assert:** On fixed test point x=[0.5, -0.3], y_true=0.7, max relative error between analytic and numerical gradients < 1e-4.
**⚠️ Defect:** The numerical gradient function perturbs and restores each parameter individually, which is correct but O(n) in the number of parameters. For a tiny network (13 params) this is fine, but the approach doesn't scale. Also, the `eps=1e-5` central difference is a reasonable default but may give inaccurate gradients for very small or very large parameter values.

### 8. tiny_autoencoder.py
**Entry fn:** `TinyAutoencoder(input_dim=8, bottleneck_dim=2, lr=0.5)` → `train(data, epochs) → float`
**Valid input:** `data: List[List[float]]` — 8D vectors, normalized to [0,1]. At least 1 sample.
**Core:** 1-hidden-layer autoencoder (8→2→8) with sigmoid activations. Encoder compresses to 2D bottleneck, decoder reconstructs. Trained with MSE reconstruction loss. With correlated 8D input (driven by 2 latent signals), 2D bottleneck captures main variance.
**Assert:** On 50 correlated 8D samples (driven by 2 latent signals), 100 epochs at lr=0.5, trained reconstruction error < random reconstruction error / 2.
**⚠️ Defect:** The test compares against a random baseline (random reconstruction), which is a very weak baseline. A proper test would compare against a constant reconstruction (mean of data) or PCA with 2 components. The random baseline is so poor that even a barely trained autoencoder would pass.

### 9. weight_initialization_comparison.py
**Entry fn:** `DeepNetwork(init_scheme="xavier")` — 5-layer network (10→32→32→32→16→1).
**Valid input:** Random 10D input. No training — just forward pass to measure activation variance.
**Core:** Compare three initialization schemes on a 5-layer network: small uniform [-0.1, 0.1], large uniform [-1, 1], Xavier uniform [±√(1/fan_in)]. Measure activation variance at each layer. Xavier preserves variance; small init causes vanishing; large init causes exploding.
**Assert:** On random 10D input, Xavier init maintains activation variance within [0.01, 10] at all layers. Small init produces variance < 0.01 at layer 5. Large init produces variance > 10 or NaN at some layer.
**⚠️ Defect:** The test only checks a single forward pass, not training dynamics. Xavier init ensures good forward signal flow, but doesn't guarantee good backward gradients or convergence. Also, the sigmoid activation is not ideal for deep networks (tanh or ReLU would be better paired with Xavier/Glorot).

### 10. word2vec_skipgram.py
**Entry fn:** `SkipgramNegativeSampling(vocab_size, embedding_dim=8, lr=0.1)` → `train(corpus, epochs)` → `get_embedding(word_idx) → List[float]`
**Valid input:** `corpus: List[List[int]]` — tokenized documents (word indices). `vocab_size: int` ≥ 2.
**Core:** Skip-gram with negative sampling. For each target word, predict context words within window size 2. Use 2 negative samples per positive pair. Update embeddings via SGD: score = σ(target·context), error = score - label, gradient flows to both embeddings. Related words converge to nearby embeddings.
**Assert:** On a tiny 5-document corpus (8 unique words), 200 epochs at lr=0.1, embedding_dim=8, cosine similarity between co-occurring words > similarity between non-co-occurring words.
**⚠️ Defect:** The embedding matrix is shared between target and context (single W matrix), which is a simplification. Standard word2vec uses separate input and output embedding matrices. The shared matrix means the same vector serves as both target and context representation, which can limit representational capacity.

---

## Category: statistical_modeling (10 patterns)

### 11. em_two_coins.py
**Entry fn:** `em_two_coins(sessions, p_a_init=0.6, p_b_init=0.4, n_iter=50) → (p_a, p_b)`
**Valid input:** `sessions: List[List[int]]` — each session is a list of flips (1=heads, 0=tails). `n_iter ≥ 1`.
**Core:** Classic EM for two-coin problem. E-step: compute posterior probability that each session came from coin A (using current bias estimates). M-step: update bias estimates as weighted averages of heads/tails counts. Handles label switching by checking both orderings.
**Assert:** On 100 sessions (30 flips each) from coins with p=0.8 and p=0.3, 100 EM iterations, min recovery error < 0.3 (accounting for label switching).
**⚠️ Defect:** The initialization uses `overall_rate ± 0.2`, which is a heuristic that assumes the two biases straddle the overall mean. If both biases are on the same side of the overall rate (e.g., 0.7 and 0.8 with overall 0.75), this initialization would give both the same starting value and EM would not separate them. A random initialization or multiple restarts would be more robust.

### 12. gibbs_sampling_bivariate.py
**Entry fn:** `gibbs_bivariate_normal(rho, n_iter, initial_x=0.0, initial_y=0.0) → (x_samples, y_samples)`
**Valid input:** `rho: float` in (-1, 1). `n_iter ≥ 1`.
**Core:** Gibbs sampler for bivariate normal N([0,0], [[1, ρ], [ρ, 1]]). Conditionals: X|Y ~ N(ρ·Y, 1-ρ²), Y|X ~ N(ρ·X, 1-ρ²). Alternately sample each variable. Discard 500 burn-in samples.
**Assert:** On ρ=0.7, 3000 post-burn-in samples, recovered correlation within 0.1 of true, marginal variances within 0.1 of 1.0.
**⚠️ Defect:** The test uses a fixed burn-in of 500 regardless of ρ. For ρ close to 1 (high correlation), the chain mixes slowly and may need more burn-in. The assertion tolerance (±0.1) is reasonable for ρ=0.7 but would fail for ρ > 0.95 with the same sample size.

### 13. importance_sampling.py
**Entry fn:** `importance_sampling(target_pdf, proposal_pdf, proposal_sample, h, n_samples) → (estimate, ess)`
**Valid input:** `target_pdf`, `proposal_pdf`: Callable[[float], float]. `proposal_sample`: Callable[[], float]. `h`: Callable[[float], float]. `n_samples ≥ 1`.
**Core:** Estimate E_target[h(X)] using samples from a proposal, re-weighted by importance ratio w(x) = target(x) / proposal(x). Self-normalized importance sampling (weights normalized to sum to 1). Effective sample size ESS = 1 / Σ w_norm².
**Assert:** On target N(2,1), proposal N(0,4), h(x)=x, 1000 IS samples, IS estimate within 0.3 of direct Monte Carlo estimate (5000 samples), ESS > 50.
**⚠️ Defect:** The proposal N(0,4) has heavier tails than the target N(2,1), which is good for importance sampling. But the proposal mean is 0 while the target mean is 2 — this offset means many samples fall in low-density regions of the target, reducing efficiency. A proposal centered closer to the target (e.g., N(2,4)) would give higher ESS.

### 14. kaplan_meier_survival.py
**Entry fn:** `kaplan_meier(times, events) → List[Tuple[float, float]]`
**Valid input:** `times: List[float]` — event/censoring times. `events: List[int]` — 1=event, 0=censored. Same length.
**Core:** Kaplan-Meier survival curve estimator. Sorted by time, at each unique event time: S(t) = S(t⁻) × (1 - events_at_time / at_risk). At-risk count decreases by events + censored at each time. Returns list of (time, survival_prob) pairs.
**Assert:** On hand-computed example (5 subjects: times [1,2,2,3,4], events [1,1,0,1,0]), survival at t=3 is 0.3. Curve is non-increasing. Synthetic test (50 samples) also non-increasing.
**⚠️ Defect:** The function uses `set(t for t in times_sorted if t is not None)` to get unique event times, but the `if t is not None` filter is unnecessary since times are floats. More importantly, the function processes ALL unique times including those where only censoring occurs (no events), which is correct but the survival probability doesn't change at pure-censoring times. The at-risk count is reduced correctly.

### 15. kernel_density_estimation.py
**Entry fn:** `gaussian_kernel_density(samples, x, h) → float`, `silverman_bandwidth(samples) → float`
**Valid input:** `samples: List[float]` — at least 2 samples. `x: float`. `h > 0`.
**Core:** Non-parametric density estimation with Gaussian kernel. KDE: f̂(x) = (1/nh) Σ K((x-Xᵢ)/h) where K(u) = (1/√(2π))·exp(-u²/2). Bandwidth via Silverman's rule: h = (4/(3n))^{1/5} · σ̂.
**Assert:** On mixture of two Gaussians (40 pts from N(-2,0.5) + 40 pts from N(2,0.5)), KDE integral over [-5,5] within 0.05 of 1.0, density at modes (-2, 2) > density at center (0).
**⚠️ Defect:** Silverman's rule assumes the underlying distribution is approximately Gaussian. For a bimodal distribution (as in the test), Silverman's rule overestimates the bandwidth, producing an oversmoothed estimate. The test still passes because the modes are far apart (Δ=4), but for closer modes the KDE would merge them into a single peak.

### 16. loess_local_regression.py
**Entry fn:** `loess_smooth(x_vals, y_vals, x_grid, frac_nearest=0.3) → List[float]`
**Valid input:** `x_vals, y_vals: List[float]` — same length. `x_grid: List[float]`. `frac_nearest` in (0, 1].
**Core:** Locally weighted linear regression with tricube kernel: w(u) = (1 - |u|³)³ for |u| ≤ 1. For each target point, find k nearest neighbors (k = frac_nearest × n), compute tricube weights, fit weighted linear regression, predict.
**Assert:** On noisy sine wave (60 points, σ=0.3), LOESS (frac=0.3) MSE < global linear MSE.
**⚠️ Defect:** The LOESS implementation uses k-NN style bandwidth (fixed fraction of points) rather than a fixed-distance bandwidth. This means in sparse regions, the neighborhood is wide, and in dense regions, it's narrow. The tricube weight function handles this gracefully, but the effective degrees of freedom vary across the domain, which can cause uneven smoothing.

### 17. metropolis_hastings_mcmc.py
**Entry fn:** `metropolis_hastings(target_pdf, proposal_sd, n_samples, initial_x=0.0) → (samples, acceptance_rate)`
**Valid input:** `target_pdf: Callable[[float], float]` — unnormalized density. `proposal_sd > 0`. `n_samples ≥ 1`.
**Core:** Random-walk Metropolis-Hastings. Propose x' = x + N(0, proposal_sd). Accept with probability min(1, target(x')/target(x)). Log-space computation for numerical stability. On bimodal target N(-2,1) + N(2,1), recovers mean ≈ 0 and variance ≈ 5.
**Assert:** On bimodal mixture (modes at ±2), 5000 post-burn-in samples, proposal_sd=2.5, mean within 0.5 of 0, variance within 1.0 of 5, acceptance rate between 0.2 and 0.7.
**⚠️ Defect:** The log-ratio computation clamps to 0 (`log_ratio = min(0.0, log_ratio)`), which is correct for the Metropolis algorithm (symmetric proposal). But the docstring says "Metropolis-Hastings" which would require the full ratio for asymmetric proposals. The code is actually Metropolis (symmetric random walk), not general Metropolis-Hastings.

### 18. polynomial_regression.py
**Entry fn:** `fit_polynomial(x_vals, y_vals, degree) → List[float]`
**Valid input:** `x_vals, y_vals: List[float]` — same length. `degree ≥ 0`.
**Core:** Polynomial regression via normal equations on Vandermonde design matrix. Build V[i,j] = xᵢʲ, solve (VᵀV)c = Vᵀy via Gaussian elimination with partial pivoting. Evaluate polynomial via Horner-like power accumulation.
**Assert:** On quadratic y = 2 + 3x + 0.5x² + N(0,0.1) with 20 points, degree-2 fit recovers coefficients within 0.2 of true, and quadratic MSE < linear MSE.
**⚠️ Defect:** The Vandermonde matrix is notoriously ill-conditioned for high degrees or non-centered data. For degree 2 with x in [0, 9.5], it's fine, but for degree > 10 or large x ranges, the normal equations become numerically unstable. No centering/scaling of x values is performed.

### 19. power_analysis_sample_size.py
**Entry fn:** `sample_size_two_proportion(p1, p2, alpha=0.05, target_power=0.80) → int`
**Valid input:** `p1, p2: float` in (0, 1). `alpha` in (0, 1). `target_power` in (0, 1).
**Core:** Compute required sample size per group for two-proportion z-test. Uses normal approximation: n = (z_α/2 + z_β)² · se² / δ². Verifies by computing achieved power at the estimated n. Uses rational approximation for normal quantile.
**Assert:** For p1=0.3, p2=0.5, α=0.05, power=0.80, computed n achieves power ≥ 0.75, and n-1 gives lower power.
**⚠️ Defect:** The `normal_quantile` function uses a rational approximation (Abramowitz and Stegun) that is accurate to ~4.5×10⁻⁴ but not exact. The `normal_cdf_approx` uses `tanh` which is a very rough approximation (error up to 0.01). This means the power calculation has systematic approximation error beyond the normal approximation itself.

### 20. quantile_regression_pinball.py
**Entry fn:** `quantile_regression_linear(x_vals, y_vals, tau, learning_rate=0.01, n_iter=1000) → (intercept, slope)`
**Valid input:** `x_vals, y_vals: List[float]` — same length. `tau` in (0, 1). `learning_rate > 0`.
**Core:** Linear quantile regression via pinball loss gradient descent. Pinball loss: L_τ(y, ŷ) = τ·max(y-ŷ, 0) + (τ-1)·min(y-ŷ, 0). Gradient: -τ if y > ŷ, -(τ-1) if y ≤ ŷ. Fit median (τ=0.5) and 90th percentile (τ=0.9) lines.
**Assert:** On y = 1 + 0.5x + N(0,0.5) with 50 points, median line has 35-65% of points below it, 90th percentile line has 75-99% below, and 90th line is above median line.
**⚠️ Defect:** The gradient is constant magnitude (either -τ or -(τ-1)) regardless of the residual size. This means the optimization doesn't distinguish between a small violation and a large one — all violations of the same sign get the same gradient. This can lead to slow convergence, especially with outliers. The test uses 5000 iterations, which is high for only 2 parameters.