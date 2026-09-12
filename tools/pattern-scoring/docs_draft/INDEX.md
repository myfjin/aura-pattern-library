# AURA Pattern Library — Detail Docs Index

**Phase 1:** ~20 audited patterns. One-line description + link per pattern, grouped by language → sphere.

---

## Python — Data Science

### Bayesian III: Approximate Inference
- [bayes_factor_normal_means](python/data-science/bayesian_iii_approximate_inference/bayes_factor_normal_means.md) — Bayesian evidence for an effect: BF comparing H1 (θ≠0) vs H0 (θ=0) under normal likelihood. ⚠️ Shipped math is WRONG (AURA-E010); retrofit corrects it.

### Bayesian III: Modeling and Selection
- [dirichlet_stick_breaking](python/data-science/bayesian_iii_modeling_and_selection/dirichlet_stick_breaking.md) — Probability weights for infinite mixture models: break a stick of probability into random pieces, controlled by concentration α.

### Composed Tools
- [dedup_pipeline](python/data-science/composed_tools/dedup_pipeline.md) — Three-stage near-dup detection: MinHash candidates → edit-distance verify → word-diff explain. Covers each stage's weakness with the next.
- [walk_forward_early_stopping](python/data-science/composed_tools/walk_forward_early_stopping.md) — Stop training when the future says stop: walk-forward validation + patience-based early stopping for time-ordered iterative models.

### Ensembles and Robust Methods
- [gradient_boosting_stumps](python/data-science/ensembles_and_robust_methods/gradient_boosting_stumps.md) — Prediction by committee of dumb rules: 50 stumps, each fixing the last one's residuals, beat one stump 8×.
- [stacking_ensemble](python/data-science/ensembles_and_robust_methods/stacking_ensemble.md) — Two mediocre models can beat one good one: meta-learner trained on out-of-fold base predictions. ⚠️ NaN poison trains silently (AURA-E008); retrofit fixes it.

### Information Theory and Probability
- [inverse_transform_sampling](python/data-science/information_theory_and_probability/inverse_transform_sampling.md) — Generate samples from any distribution with a tractable inverse CDF, using only a uniform random generator.

### Recommenders and Graph Sampling
- [bayesian_ab_beta](python/data-science/recommenders_and_graph_sampling/bayesian_ab_beta.md) — Bayesian A/B test: P(B > A) via Beta-Binomial posterior sampling. ⚠️ Fake-robust on impossible data (AURA-E004/E005); retrofit fixes it.

### Statistical Modeling
- [power_analysis_sample_size](python/data-science/statistical_modeling/power_analysis_sample_size.md) — Minimum sample size per group to detect a proportion difference at target power. Self-check proves n is sufficient and not padded.

### Survival and Reliability
- [log_rank_test](python/data-science/survival_and_reliability/log_rank_test.md) — Nonparametric test for equal survival curves between two groups, handling censored observations.

---

## Python — System Administration

### Resource Guards
- [token_bucket_limiter](python/system-administration/resource-guards/token_bucket_limiter.md) — Rate-limit access to a resource: tokens drip at fixed rate, empty bucket denies. ⚠️ No burst capacity cap — unbounded accumulation after idle (functional defect).

### Secrets and Credentials
- [ttl_cache](python/system-administration/secrets-credentials/ttl_cache.md) — Time-limited cache with logical clock: deterministic expiry for testable secrets management. ⚠️ `size()` lies (returns raw len, not non-expired count); lazy expiry leaks memory.

### Text Stream Operations
- [robust_csv_parse](python/system-administration/text-stream-ops/robust_csv_parse.md) — Parse dirty CSV with detection, not guessing: strict mode raises precise errors, non-strict skips broken rows. Unicode-clean.

---

## R — Regression and GLM

- [linear_regression_normal_eq](r/regression_and_glm/linear_regression_normal_eq.md) — Ordinary least squares via normal equations β = (XᵀX)⁻¹Xᵀy, self-checked against R's `lm()` to 1e-8. ⚠️ NA in y propagates silently through matrix ops.
