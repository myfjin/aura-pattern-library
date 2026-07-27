# anova tukey

**Language:** R · **Sphere:** R · **Category:** Hypothesis Testing — Parametric

## What it does

anova_tukey.R
Tukey's HSD test via studentized range distribution (qtukey).
Oracle: TukeyHSD() in stats.
Claim: manual pairwise intervals match oracle.
Tolerance: interval bounds agreement <1e-10 (relative).

## Guarantee

When it runs, anova tukey guarantees abs(row_manual$diff[1] - (-row_oracle["diff"])) < 1e-08; abs(row_manual$lwr[1] - (-row_oracle["upr"])) < 1e-06; abs(row_manual$upr[1] - (-row_oracle["lwr"])) < 1e-06 (proven by run).

**Checkable constraints:**

- `oracle_name %in% rownames(oracle_ci)`
- `abs(row_manual$diff[1] - (-row_oracle["diff"])) < 1e-08`
- `abs(row_manual$lwr[1] - (-row_oracle["upr"])) < 1e-06`
- `abs(row_manual$upr[1] - (-row_oracle["lwr"])) < 1e-06`
- `abs(row_manual$p.adj[1] - row_oracle["p adj"]) < 1e-06`
- `nrow(tukey_ci_manual) == choose(groups, 2)`
- `all(tukey_ci_manual$p.adj >= 0 & tukey_ci_manual$p.adj <= 1)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Hardcoded four-group normal demo with `groups = 4`, `n_per_group = 20`, and `group_means = c(10, 12, 11.5, 14)`. For reuse, a numeric response vector `y` and an integer grouping factor `group_factor` of equal length must exist.
**Core:** Fits one-way ANOVA with `aov()`, extracts MSE and residual df, then computes all pairwise Tukey HSD confidence intervals and adjusted p-values using `qtukey`/`ptukey`. Verifies against `TukeyHSD()`.
**Assert:** Manual pairwise CIs are the mirror of the oracle intervals within `1e-6`; adjusted p-values match `TukeyHSD` within `1e-6`; number of pairs equals `choose(groups, 2)`; all adjusted p-values are in `[0,1]`.
**⚠️ Defect:** Assumes equal sample sizes per group (`n_each` is used for every pair). Assumes homoscedasticity because it uses the common MSE. No input validation (empty groups, unequal n, non-numeric values). No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
