# ridge regression

**Language:** R · **Sphere:** R · **Category:** Regression & GLM

## What it does

Ridge Regression: closed-form (X'X + λI)^-1 X'y
Implements Tikhonov regularization for multiple regression; verifies λ=0 equals lm() and monotonic shrinkage
Core: solve (X'X + λI) = X'y for β, shrinkage increases with λ
Planted: multivariate data with strong correlations, λ sequence shows coefficient decay

## Guarantee

When it runs, ridge regression guarantees all.equal(ridge_coefs[1, ], unname(c(lm_coefs[1], lm_coefs[2:4])), tolerance = 1e-06); coef_norms[i] >= coef_norms[i + 1] (proven by run).

**Checkable constraints:**

- `all.equal(ridge_coefs[1, ], unname(c(lm_coefs[1], lm_coefs[2:4])), tolerance = 1e-06)`
- `coef_norms[i] >= coef_norms[i + 1]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Numeric design matrix `X` with an intercept column and one or more predictors, and numeric response vector `y` of length `nrow(X)`. The demo uses three predictors and a lambda sequence `c(0, 0.1, 1, 10, 100)`.
**Core:** Computes ridge coefficients `β = (XᵀX + λI)⁻¹ Xᵀy` for a sequence of lambdas, verifies `λ = 0` matches `lm()`, and checks that the L2 norm of non-intercept coefficients is non-increasing in `λ`.
**Assert:** `λ = 0` coefficients match `lm()` within `1e-6`; `L2` norm of slopes is non-increasing across the lambda sequence.
**⚠️ Defect:** No input validation: singular `XᵀX` even for small `λ` can fail; non-numeric or mismatched `X`/`y` raise uncontrolled errors. The intercept is included in the regularization (`λI` for all columns), which is usually not desired — standard practice either centers/scales data or excludes the intercept from shrinkage. Lambda sequence is hardcoded. No function wrapper.

---

**R-sphere batch 4: 8/8 patterns documented.** Verifier should check source at `/home/au/aura-pattern-library/r/regression_and_glm/` (canonical) or `/tmp/aura-review/aura-pattern-library/r/regression_and_glm/` (review copy). No Rscript on `.8`, so verification is doc-accuracy only: signatures, top-level script vs function, and defect claims vs source.

---
*△ AURA Pattern Library — © Reality Optimizer*
