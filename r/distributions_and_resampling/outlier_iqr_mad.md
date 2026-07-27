# outlier iqr mad

**Language:** R · **Sphere:** R · **Category:** Distributions & Resampling

## What it does

Outlier Detection (IQR & MAD)
Implements IQR fences + MAD z-scores; planted outliers caught, clean data passes
Use when: identifying extreme values

## Guarantee

When it runs, outlier iqr mad guarantees x[51] > upper_fence || x[51] < lower_fence; x[52] > upper_fence || x[52] < lower_fence; clean_flags <= 3 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `length(outliers_iqr) >= 2`
- `52 %in% outliers_iqr || 51 %in% outliers_iqr`
- `x[51] > upper_fence || x[51] < lower_fence`
- `x[52] > upper_fence || x[52] < lower_fence`
- `clean_flags <= 3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric vector named `x`. The script plants two extreme outliers in a standard-normal sample if `x` is absent.
**Core:** Computes IQR fences (`Q1 - 1.5*IQR`, `Q3 + 1.5*IQR`) and MAD z-scores (`|x - median| / MAD > 2.5`), then flags outliers.
**Assert:** The planted outliers are flagged by IQR; at most 3 of 200 clean N(0,1) observations are flagged by chance.
**⚠️ Defect:** Hardcoded thresholds (1.5*IQR, 2.5*MAD) with no parameterization. `NA` values are silently dropped by `quantile()` and `median()`, changing the computed fences without warning. The MAD method uses the constant 2.5, which is not the standard 3.5×MAD convention and is not justified in the script. No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
