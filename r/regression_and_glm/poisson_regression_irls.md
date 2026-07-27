# poisson regression irls

**Language:** R · **Sphere:** R · **Category:** Regression & GLM

## What it does

Poisson Regression via Iteratively Reweighted Least Squares (IRLS) with log link
Implements Newton-Raphson on deviance via weighted regression; compares to glm(family=poisson)
Core: log link g(μ)=log(μ), variance Var(Y)=μ; reweight by 1/μ at each iter, refit until convergence
Planted: Poisson counts with clear covariate signal, count range matches typical log-linear data

## Guarantee

When it runs, poisson regression irls guarantees all.equal(as.vector(beta), unname(coef(oracle_fit)), tolerance = 1e-06) (proven by run).

**Checkable constraints:**

- `all.equal(as.vector(beta), unname(coef(oracle_fit)), tolerance = 1e-06)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Numeric predictor vector `x` and integer/count response vector `y` of equal length.
**Core:** IRLS for Poisson regression with log link using a diagonal weight matrix `W = diag(μ)` and adjusted response `z = η + (y - μ)/μ`.
**Assert:** Manual coefficients match `glm(..., family = poisson)` within `1e-6`.
**⚠️ Defect:** No input validation: zero or negative `y` values still work in the algorithm but are statistically invalid for Poisson; non-numeric inputs raise uncontrolled errors; `x` is coerced to a single-predictor design matrix. Convergence tolerance and max iterations are hardcoded. Does not compute deviance or standard errors. No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
