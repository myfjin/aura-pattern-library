# PATTERN SHEET — linear_regression_normal_eq (R)
`r/regression_and_glm/linear_regression_normal_eq.R`
**Status: PASS-WITH-FLAG (Illia's audit, 2026-07-20) — honest math, self-checking against lm();
one weak-typing flag (silent NA propagation in the manual path). Description too terse for R.**

## What it solves (human version — the standard R needs)
The most fundamental question in statistics: "given data points, what's the best-fit line (or
plane)?" Ordinary least squares. This does it the textbook way — the NORMAL EQUATIONS
β = (XᵀX)⁻¹Xᵀy — instead of calling a black box, then PROVES its answer matches R's trusted
`lm()` to 1e-8. Use it to understand what `lm()` does under the hood, or when you need the
coefficients in a setting where you can't depend on lm.

## Valid inputs / contract
| Input | Domain | Today |
|---|---|---|
| X (design matrix) | full column rank (no collinear columns) | collinear → `solve()` LAPACK "exactly singular" error ✅ (caught) |
| y (response) | numeric, NO missing values | **NA → manual path yields all-NA coefficients SILENTLY** (⚠, caught only by the lm cross-check) |

## Failure modes (audited by hand)
| Trigger | What happens | Meaning |
|---|---|---|
| `y[5] <- NA` | `beta_manual` = all NA; `lm()` drops the row (na.omit) → they disagree → stopifnot errors | R weak-typing: NA propagates silently through matrix ops; standalone use would return NA with no warning |
| collinear columns | `solve()` errors "system is exactly singular" | honest loud failure ✅ |
| oracle (recover truth) | [2.0009, 0.428, -0.257] vs true [2, 0.5, -0.3] | within sampling error — math honest ✅ |

## Meta-law data point
R (weakly typed) shows the NA/value finding that rust (strongly typed) could not — confirming the
language-aware prior: fire type/NaN recipes on R & python, skip them on rust.

## Provenance
Machine-VERIFIED · **Illia's audit 07-20: PASS-WITH-FLAG (NA-propagation flag; math + singular
handling genuine)** · evidence: output/manual_audit_2026-07-19.csv
