# laplace approximation posterior

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Approximate Inference

**Signature:** `(theta: float, data: ?, prior_mu: ?, prior_sigma: ?) → float`

## What it does

Laplace approximation: approximate posterior p(θ|data) with Gaussian at MAP.

Curvature of the log-posterior at the mode provides variance. Core claim: Gaussian-at-MAP
mode ≈ true MAP; curvature ≈ observed Fisher info.

## Guarantee

When it runs, laplace approximation posterior guarantees abs(theta_map - mu_true) < 0.5; posterior_var > 0; posterior_var < 1.0 (proven by run).

**Checkable constraints:**

- `abs(theta_map - mu_true) < 0.5`
- `posterior_var > 0`
- `posterior_var < 1.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
