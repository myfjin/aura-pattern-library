# lm diagnostics

**Language:** R · **Sphere:** R · **Category:** Regression & GLM

## What it does

lm_diagnostics.R
Regression diagnostics: leverage, standardized residuals, Cook's distance.
Oracle: hatvalues(), rstandard(), cooks.distance() in stats.
Claim: manual diagnostics match oracle; planted influential point flagged.
Tolerance: exact agreement (rel error <1e-10).

## Guarantee

When it runs, lm diagnostics guarantees max(rel_error_lev, na.rm = TRUE) < 1e-10; max(rel_error_std, na.rm = TRUE) < 1e-10; max(rel_error_cook, na.rm = TRUE) < 1e-09 (proven by run).

**Checkable constraints:**

- `max(rel_error_lev, na.rm = TRUE) < 1e-10`
- `max(rel_error_std, na.rm = TRUE) < 1e-10`
- `max(rel_error_cook, na.rm = TRUE) < 1e-09`
- `all(leverage_manual >= 0 & leverage_manual <= 1)`
- `all(cooks_manual >= 0)`
- `length(leverage_manual) == n`
- `length(standardized_manual) == n`
- `length(cooks_manual) == n`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Numeric predictor vector `x` and response vector `y` of equal length.
**Core:** Computes leverage via the hat matrix, standardized residuals (with internal estimate of `σ`), and Cook's distance by hand. Verifies against `hatvalues()`, `rstandard()`, and `cooks.distance()`.
**Assert:** Manual leverage, standardized residuals, and Cook's distance match the oracles within relative error `1e-10`, `1e-10`, and `1e-9` respectively; all leverages are in `[0, 1]`; all Cook's distances are non-negative; diagnostics vectors have length `n`.
**⚠️ Defect:** The planted-influential-point assertion (`outlier_idx %in% influential_points`) is commented out, so the script does not actually enforce detection of the planted outlier. Builds the full `n × n` hat matrix explicitly — quadratic in memory and slow for large `n`. No input validation (length mismatch, non-numeric, `n < p`). No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
