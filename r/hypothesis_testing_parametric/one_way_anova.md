# one way anova

**Language:** R · **Sphere:** R · **Category:** Hypothesis Testing — Parametric

## What it does

One-Way ANOVA
Implements F statistic from sum of squares; verifies against aov()
Use when: comparing means across 3+ groups

## Guarantee

When it runs, one way anova guarantees all.equal(f_stat, as.numeric(aov_summary[1, "F value"]), tolerance = 1e-08); all.equal(p_val, aov_summary[1, "Pr(>F)"], tolerance = 1e-08) (proven by run).

**Checkable constraints:**

- `all.equal(f_stat, as.numeric(aov_summary[1, "F value"]), tolerance = 1e-08)`
- `all.equal(p_val, aov_summary[1, "Pr(>F)"], tolerance = 1e-08)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric response vector `y` and an integer grouping vector `groups` of equal length with at least two groups.
**Core:** Computes total, between-group, and within-group sum of squares, derives the F statistic and p-value, and verifies against `aov()`/`anova()`.
**Assert:** Manual F statistic and p-value match the `aov()` summary within `1e-8`.
**⚠️ Defect:** Assumes groups are coded as consecutive integers starting at 1; missing groups or non-integer labels are not handled. No post-hoc tests. No input validation (empty groups, non-numeric response). No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
