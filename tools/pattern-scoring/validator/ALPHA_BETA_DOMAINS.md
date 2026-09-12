# alpha / beta parameter domains — the written-down judgment

`alpha` and `beta` are polymorphic ACROSS patterns (a Beta shape, a significance level, a
smoothing weight, a regression coefficient — never the same domain twice), so the validation
tool cannot blanket-guard them. This registry writes down each pattern's actual domain so it is
documented AND enforceable per-pattern. Ruling: Illia, 2026-07-21.

## Domain classes

### SIGNIFICANCE / ERROR-RATE — `alpha ∈ (0, 1)`
A probability of a Type-I error / false-discovery rate. Must be strictly inside (0,1).
- `statistics_and_testing/benjamini_hochberg.py` — alpha = FDR level
- `experiments_ii/minimum_detectable_effect.py` — alpha = significance level
- `experiments_ii/multi_armed_holm_correction.py` — alpha = family-wise error rate
- `causal_inference_and_experimentation/sequential_probability_ratio.py` — alpha = Type-I rate
- `statistical_modeling/power_analysis_sample_size.py` — alpha = significance (EXAM pattern)

### SHAPE / CONCENTRATION — `alpha > 0`, `beta > 0`
A Beta/Gamma/Dirichlet shape or a CRP/Dirichlet concentration. Must be strictly positive.
- `bayesian_iii_modeling_and_selection/beta_binomial_overdispersion.py` — alpha, beta = Beta shape
- `bayesian_iii_modeling_and_selection/crp_table_growth.py` — alpha = CRP concentration
- `bayesian_iii_modeling_and_selection/dirichlet_multinomial_posterior.py` — prior_alpha = Dirichlet conc.
- `bayesian_iii_modeling_and_selection/dirichlet_stick_breaking.py` — alpha = Beta(1,α) conc. (EXAM PASS)
- `information_theory_and_probability/conjugate_priors.py` — alpha_prior/beta_prior = Beta/Gamma prior
- `probabilistic_modeling/gamma_poisson_conjugate.py` — alpha, beta = Gamma prior shape/rate
- `recommenders_and_graph_sampling/bayesian_ab_beta.py` — prior_alpha/prior_beta (EXAM PASS, guarded)
- `recommenders_and_graph_sampling/thompson_sampling_bandit.py` — alpha, beta = Beta posterior counts

### SMOOTHING WEIGHT — `alpha >= 0`
An additive-smoothing / regularization strength. 0 = no smoothing (a valid boundary), grows upward.
- `applied_ds_practice/target_encoding_smoothing.py` — alpha = smoothing strength

### COEFFICIENT (real-valued) — any sign, but FINITE
A regression coefficient / reflection scalar: every real value is mathematically valid, but a
NaN/Inf silently poisons the output. Guarded FINITE-only (no false bound — that would be a lie).
- `econometrics_and_finance/logit_marginal_effects.py` — beta = logit coefficient (any finite real) [ENFORCED]
- `linear_algebra/householder_reflection.py` — beta = reflection scalar in apply_householder (any finite real) [ENFORCED]

## Enforcement
Bounded non-EXAM patterns get an accumulate-then-raise guard for their domain (added 2026-07-21).
EXAM patterns hardened WITHOUT flipping their verdict (verified: exam held 67/67) — dirichlet_stick_breaking (alpha>0, stays PASS), power_analysis (alpha in (0,1), stays FLAG), bayesian_ab (prior>0, stays PASS). UNBOUNDED patterns carry only
this documented note — a runtime guard there would falsely reject valid input.
