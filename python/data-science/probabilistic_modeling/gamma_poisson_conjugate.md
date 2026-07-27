# gamma poisson conjugate

**Language:** Python · **Sphere:** data-science · **Category:** Probabilistic Modeling

**Signature:** `(x: float) → float`

## What it does

Gamma-Poisson conjugate prior: Gamma prior on Poisson rate parameter.

Core idea: prior Gamma(α, β); observe Poisson counts; posterior is Gamma(α + Σcount, β + n).
Sequential updates ≡ batch update (conjugacy). Posterior matches closed form.

When to use: rate estimation, count data modeling, reliability/failure analysis.

## Guarantee

When it runs, gamma poisson conjugate guarantees alpha_weak_post == alpha_weak + sum(counts); beta_weak_post == beta_weak + len(counts); prior_mean_weak < mean_weak_post < empirical_mean or prior_mean_weak > mean_weak_post > empirical_mean (weak-grade: directional, proven by run).

**Checkable constraints:**

- `alpha_weak_post == alpha_weak + sum(counts)`
- `beta_weak_post == beta_weak + len(counts)`
- `prior_mean_weak < mean_weak_post < empirical_mean or prior_mean_weak > mean_weak_post > empirical_mean`
- `min(prior_mean_strong, empirical_mean) <= mean_strong_post <= max(prior_mean_strong, empirical_mean)`
- `var_weak_post < var_weak_prior`
- `not math.isnan(ll) and (not math.isinf(ll))`
- `seq_alpha == alpha_weak_post and seq_beta == beta_weak_post`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
