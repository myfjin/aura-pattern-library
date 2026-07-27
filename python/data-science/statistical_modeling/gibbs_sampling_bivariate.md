# gibbs sampling bivariate

**Language:** Python · **Sphere:** data-science · **Category:** Statistical Modeling

**Signature:** `(rho: float, n_iter: int, initial_x: float, initial_y: float) → Tuple[List[float], List[float]]`

## What it does

Gibbs Sampling for Bivariate Normal Distribution.

Alternately samples each variable from its conditional distribution.
Recovers correlation structure from a correlated bivariate normal.
Use when joint sampling is hard but conditionals are tractable.

## Guarantee

When it runs, gibbs sampling bivariate guarantees abs(recovered_rho - true_rho) < 0.1; abs(var_x - 1.0) < 0.1; abs(var_y - 1.0) < 0.1 (proven by run).

**Checkable constraints:**

- `abs(recovered_rho - true_rho) < 0.1`
- `abs(var_x - 1.0) < 0.1`
- `abs(var_y - 1.0) < 0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `gibbs_bivariate_normal(rho, n_iter, initial_x=0.0, initial_y=0.0) → (x_samples, y_samples)`
**Valid input:** `rho: float` in (-1, 1). `n_iter ≥ 1`.
**Core:** Gibbs sampler for bivariate normal N([0,0], [[1, ρ], [ρ, 1]]). Conditionals: X|Y ~ N(ρ·Y, 1-ρ²), Y|X ~ N(ρ·X, 1-ρ²). Alternately sample each variable. Discard 500 burn-in samples.
**Assert:** On ρ=0.7, 3000 post-burn-in samples, recovered correlation within 0.1 of true, marginal variances within 0.1 of 1.0.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
