# logistic regression irls

**Language:** R · **Sphere:** R · **Category:** Regression & GLM

## What it does

Logistic Regression via IRLS (Iteratively Reweighted Least Squares)
Implements IRLS loop by hand; verifies coefficients against glm(family=binomial) to 1e-6
Use when: binary classification and need to understand Newton-Raphson iteration

## Guarantee

When it runs, logistic regression irls guarantees all.equal(as.numeric(beta), as.numeric(beta_glm), tolerance = 1e-04) (proven by run).

**Checkable constraints:**

- `all.equal(as.numeric(beta), as.numeric(beta_glm), tolerance = 1e-04)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Numeric design matrix `X` with an intercept column and one or more predictors, and binary response vector `y` in `{0, 1}` of length `nrow(X)`. The demo uses two predictors.
**Core:** IRLS (Newton-Raphson) loop for logistic regression with logit link: computes linear predictor, fitted probabilities, working weights, and adjusted response; solves the weighted least-squares system until convergence.
**Assert:** Manual coefficients match `glm(..., family = binomial)` within `1e-4`.
**⚠️ Defect:** No input validation: perfect separation can make weights `w` numerically zero and send coefficients to `±Inf`; non-binary `y` runs silently; singular `X` raises uncontrolled errors. Convergence tolerance and max iterations are hardcoded. Does not compute standard errors, deviance, or fitted values. No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
