# bayesian linear regression

**Language:** Python · **Sphere:** data-science · **Category:** Probabilistic Modeling

**Signature:** `(X: List[float], y: List[float], mu0: float, sigma0_sq: float, sigma_sq: float) → Tuple[float, float]`

## What it does

Bayesian linear regression: conjugate normal prior, known noise, closed-form posterior.

Core idea: prior N(μ₀, Σ₀); likelihood N(y | Xβ, σ²I); posterior is N(μ_post, Σ_post)
with closed-form updates. Posterior mean is between prior and OLS; variance shrinks with data.

When to use: interpretable regression with uncertainty, small data, informative priors.

## Guarantee

When it runs, bayesian linear regression guarantees abs(mu_weak - true_beta) < 1.0; abs(mu_weak - ols_beta) < 0.5; mu_strong > 1.5 and mu_strong < ols_beta (proven by run).

**Checkable constraints:**

- `abs(mu_weak - ols_beta) < 0.5`
- `mu_strong > 1.5 and mu_strong < ols_beta`
- `sigma_sq_weak < 100.0`
- `sigma_sq_strong < 0.1`
- `abs(mu_weak - true_beta) < 1.0`
- `1.5 < mu_strong < ols_beta`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
