# meanfield vi gaussian

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Approximate Inference

**Signature:** `(data: List[float], mu0: ?, lam0: ?, a0: ?, b0: ?, max_iter: ?) → Tuple[float, float, List[float]]`

## What it does

Mean-field variational inference for a Gaussian with unknown mean AND precision.

The true posterior over (μ, τ) is Normal-Gamma — NOT factorizable — so a mean-field
q(μ)q(τ) is a genuine APPROXIMATION, not the analytic posterior in disguise. Coordinate-
ascent VI (CAVI) iterates the two factors to convergence. Core claim: VI recovers the
mean the data support (≈ sample mean ≈ true μ) and a positive precision near the truth;
and it genuinely ITERATES (its estimate moves across iterations, unlike a closed form).

## Guarantee

When it runs, meanfield vi gaussian guarantees abs(vi_mu - mu_true) < 0.4; abs(vi_mu - sample_mean) < 0.05; abs(vi_tau - 1.0 / sample_var) < 0.3 (proven by run).

**Checkable constraints:**

- `abs(vi_mu - mu_true) < 0.4`
- `abs(vi_mu - sample_mean) < 0.05`
- `abs(vi_tau - 1.0 / sample_var) < 0.3`
- `traj[0] != traj[-1] and len(set((round(t, 6) for t in traj))) > 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
