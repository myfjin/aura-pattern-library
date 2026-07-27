# missing pattern matrix

**Language:** R · **Sphere:** R · **Category:** Data Wrangling & Feature Engineering

## What it does

missing_pattern_matrix.R
Missing data pattern analysis: missingness patterns and correlation handling.
Oracle: cor(use="pairwise.complete.obs") for pairwise correlation.
Claim: pattern matrix reveals planted MAR mechanism; pairwise cor matches oracle.
Tolerance: pattern counts exact; correlation rel error <1e-10.

## Guarantee

When it runs, missing pattern matrix guarantees pattern_df$count[pattern_000] == max(pattern_df$count); abs(corr_13_manual - corr_13_oracle) < 1e-10; abs(corr_23_manual - corr_23_oracle) < 1e-10 (proven by run).

**Checkable constraints:**

- `length(pattern_000) > 0`
- `pattern_df$count[pattern_000] == max(pattern_df$count)`
- `pattern_01_exists`
- `abs(corr_13_manual - corr_13_oracle) < 1e-10`
- `abs(corr_23_manual - corr_23_oracle) < 1e-10`
- `nrow(pattern_df) <= 2^3`
- `all(corr_matrix_oracle >= -1 & corr_matrix_oracle <= 1)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Three numeric vectors named `x1`, `x2`, `x3` must exist in the global environment. The script plants its own MAR missingness mechanism as a demo if they are absent.
**Core:** Builds a binary missingness pattern matrix, counts unique patterns, and computes pairwise-complete correlations using `cor(use="pairwise.complete.obs")` as an oracle.
**Assert:** Pattern `(0,0,0)` is the most common; pattern `(0,1,x)` exists; pairwise correlations agree with the oracle within `1e-10`.
**⚠️ Defect:** Two sanity checks are commented out: `sum(pattern_df$count) == n` and one of the correlation agreement checks. This means the script does not actually enforce that all rows are accounted for or that all pairwise correlations match. Hardcoded to three variables. No input validation. No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
