# Linear Regression via Normal Equations (R)

**File:** `r/regression_and_glm/linear_regression_normal_eq.R`
**Sphere:** R — Regression and GLM
**Status:** PASS-WITH-FLAG (Illia's audit 2026-07-20)

---

## What it solves

The most fundamental question in statistics: "given data points, what's the best-fit line (or plane)?" Ordinary least squares. This does it the textbook way — the **NORMAL EQUATIONS** β = (XᵀX)⁻¹Xᵀy — instead of calling a black box, then PROVES its answer matches R's trusted `lm()` to 1e-8.

**When to use:** You want to understand what `lm()` does under the hood, or you need the coefficients in a setting where you can't depend on `lm()`. The self-check against R's built-in `lm()` is the trust anchor — if the manual path ever diverges, the assert catches it.

---

## Valid inputs / contract

| Input | Domain | Today |
|---|---|---|
| X (design matrix) | full column rank (no collinear columns) | collinear → `solve()` LAPACK "exactly singular" error ✅ (caught) |
| y (response) | numeric, NO missing values | **NA → manual path yields all-NA coefficients SILENTLY** (⚠, caught only by the lm cross-check) |

---

## How inputs shape the output

- **Collinearity kills the normal equations:** if two columns are perfectly correlated, XᵀX is singular and `solve()` errors. This is honest — the math can't proceed, and it says so loudly.
- **NA in y propagates silently through matrix operations:** R's weak typing means `NA` flows through `t(X) %*% y` and `solve()` without error, producing all-NA coefficients. The `lm()` cross-check catches this, but standalone use would return NA with no warning.
- **Sampling noise is visible in the coefficients:** the demo's true coefficients [2, 0.5, -0.3] are recovered as [2.0009, 0.428, -0.257] — within expected error for n=100 with σ=1.

---

## Worked example (real run)

```r
> source("r/regression_and_glm/linear_regression_normal_eq.R")
> beta_manual
[1]  2.0009  0.4280 -0.2570
> coef(lm_fit)
(Intercept)         x1         x2
  2.0009     0.4280    -0.2570
> all.equal(as.numeric(beta_manual), as.numeric(coef(lm_fit)), tolerance = 1e-8)
[1] TRUE
```

**Reading the output:** the manual normal-equations solution matches R's `lm()` to 1e-8. The coefficients are within sampling error of the true values [2, 0.5, -0.3] — the math is honest.

---

## Failure modes (audited by hand)

| Trigger | What happens | Meaning |
|---|---|---|
| `y[5] <- NA` | `beta_manual` = all NA; `lm()` drops the row (na.omit) → they disagree → stopifnot errors | R weak-typing: NA propagates silently through matrix ops; standalone use would return NA with no warning |
| collinear columns | `solve()` errors "system is exactly singular" | honest loud failure ✅ |
| oracle (recover truth) | [2.0009, 0.428, -0.257] vs true [2, 0.5, -0.3] | within sampling error — math honest ✅ |

**Meta-law data point:** R (weakly typed) shows the NA/value finding that Rust (strongly typed) could not — confirming the language-aware prior: fire type/NaN recipes on Python & R, skip them on Rust.

---

## Provenance

Machine-VERIFIED · Illia's audit 2026-07-20: PASS-WITH-FLAG (NA-propagation flag; math + singular handling genuine) · evidence: `output/manual_audit_2026-07-19.csv`
