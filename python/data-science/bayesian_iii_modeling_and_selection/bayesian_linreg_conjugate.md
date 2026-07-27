# bayesian linreg conjugate

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Modeling & Selection

**Signature:** `(x_vals: List[float], y_vals: List[float]) → Tuple[float, float]`

## What it does

Bayesian linear regression with conjugate prior.

Posterior mean ≈ true βs; 95% credible interval covers them.
Core claim: posterior mean ≈ true βs; 95% credible interval covers truth.

## Guarantee

When it runs, bayesian linreg conjugate guarantees abs(posterior_mean_b - beta_true) < 0.5; ci_lower < beta_true < ci_upper (proven by run).

**Checkable constraints:**

- `abs(posterior_mean_b - beta_true) < 0.5`
- `ci_lower < beta_true < ci_upper`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
