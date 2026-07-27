# linear regression normal eq

**Language:** R · **Sphere:** R · **Category:** Regression & GLM

## What it does

Linear Regression via Normal Equations
Implements y = Xβ using (X^T X)^-1 X^T y; verifies against lm() to 1e-8
Use when: need coefficients and understand matrix form

## Guarantee

When it runs, linear regression normal eq guarantees all.equal(as.numeric(beta_manual), as.numeric(beta_lm), tolerance = 1e-08) (proven by run).

**Checkable constraints:**

- `all.equal(as.numeric(beta_manual), as.numeric(beta_lm), tolerance = 1e-08)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Numeric design matrix `X` with an intercept column and one or more predictors, and numeric response vector `y` of length `nrow(X)`. The demo uses `n = 100`, two predictors, and planted coefficients `c(2, 0.5, -0.3)`.
**Core:** Solves the normal equations `β = (XᵀX)⁻¹ Xᵀy` and compares coefficients against `lm()`.
**Assert:** Manual coefficients match `lm()` within `1e-8`.
**⚠️ Defect:** No input validation: singular or rank-deficient `XᵀX` raises an uncontrolled `solve()` error; non-numeric or length-mismatched `X`/`y` produce confusing errors; collinear predictors silently produce numerically unstable coefficients. No function wrapper, so the demo cannot be reused as a function.

---
*△ AURA Pattern Library — © Reality Optimizer*
