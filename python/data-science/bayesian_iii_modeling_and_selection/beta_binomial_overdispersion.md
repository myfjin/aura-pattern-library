# beta binomial overdispersion

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Modeling & Selection

**Signature:** `(counts: List[int], n_trials: int, alpha: float, beta: float) → float`

## What it does

Beta-binomial: recover the planted overdispersion and beat the plain binomial.

Counts with a random per-trial success probability p ~ Beta(α, β) are OVERDISPERSED
relative to a binomial. Method-of-moments recovers (α, β) from the sample mean and variance
(via the intra-class correlation ρ), and the beta-binomial log-likelihood at the recovered
parameters beats the binomial at its MLE. Core claim: (α, β) recovered AND beta-binomial
fits the overdispersed data strictly better than the binomial.

## Guarantee

When it runs, beta binomial overdispersion guarantees abs(a_est - alpha_true) < 0.8; abs(b_est - beta_true) < 1.0; obs_var > binom_var (proven by run).

**Checkable constraints:**

- `abs(a_est - alpha_true) < 0.8`
- `abs(b_est - beta_true) < 1.0`
- `obs_var > binom_var`
- `ll_bb > ll_binom`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
