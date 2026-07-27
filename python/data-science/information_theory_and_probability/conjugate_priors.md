# conjugate priors

**Language:** Python · **Sphere:** data-science · **Category:** Information Theory & Probability

**Signature:** `(alpha_prior: float, beta_prior: float, successes: int, failures: int) → Tuple[float, float]`

## What it does

Conjugate prior Bayesian updates: Beta-Binomial and Normal-Normal (known variance).

Core idea: Conjugate priors have closed-form posterior updates. Beta prior on a Binomial
likelihood updates by adding counts: Beta(α, β) → Beta(α+successes, β+failures).
Normal prior with known observation variance gives Normal posterior with updated mean/variance.
Sequential updates produce the same result as batch updating.

Use when: conjugate Bayesian inference, updating beliefs iteratively, combining prior knowledge
with observations, comparing sequential vs batch learning.

## Guarantee

When it runs, conjugate priors guarantees abs(mean_prior - 0.5) < 1e-09; abs(mu_batch - 1.5) < 1e-09; abs(sigma2_batch - sigma2_post_expected) < 1e-09 (proven by run).

**Checkable constraints:**

- `abs(alpha_batch - alpha_seq) < 1e-09`
- `abs(beta_batch - beta_seq) < 1e-09`
- `abs(mean_prior - 0.5) < 1e-09`
- `abs(mean_post - 81.0 / 102.0) < 1e-09`
- `var_many < var_few`
- `abs(mu_batch - mu_seq) < 1e-09`
- `abs(sigma2_batch - sigma2_seq) < 1e-09`
- `abs(mu_batch - 1.5) < 1e-09`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def beta_binomial_posterior(alpha_prior: float, beta_prior: float, successes: int, failures: int) -> Tuple[float, float]:`, `def beta_mean_variance(alpha: float, beta: float) -> Tuple[float, float]:`, `def normal_normal_posterior_known_variance(mu_prior: float, sigma2_prior: float, sigma2_obs: float, observations: List[float]) -> Tuple[float, float]:`
**Valid input:** `alpha_prior`, `beta_prior`, `alpha`, `beta`, `sigma2_prior`, `sigma2_obs` > 0; `successes`, `failures` ≥ 0; `observations` non-empty for meaningful inference.
**Core:** Closed-form Bayesian updates: Beta-Binomial adds successes/failures to prior parameters; Normal-Normal (known variance) combines prior precision with observed data precision to update the posterior mean and variance. Includes sequential-update equivalence checks.
**Assert:** Batch and sequential updates produce identical posterior parameters within 1e-9; more data reduces posterior variance; a strong prior regularizes the posterior toward the prior mean.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
