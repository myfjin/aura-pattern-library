# na imputation

**Language:** R · **Sphere:** R · **Category:** Data Wrangling & Feature Engineering

## What it does

NA Imputation (Mean/Median/Mode)
Implements imputation strategies; verifies imputed stats match strategy
Use when: handling missing data

## Guarantee

When it runs, na imputation guarantees n_missing == 2; all.equal(mean(x_mean_imp), mean_val, tolerance = 0.1); all.equal(median_calc, median_val, tolerance = 1e-08) (proven by run).

**Checkable constraints:**

- `n_missing == 2`
- `all(!is.na(x_mean_imp))`
- `all.equal(mean(x_mean_imp), mean_val, tolerance = 0.1)`
- `all(!is.na(x_median_imp))`
- `all.equal(median_calc, median_val, tolerance = 1e-08)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric vector named `x` containing some `NA` values.
**Core:** Creates two imputed copies: mean-imputed and median-imputed, plus a missingness indicator vector.
**Assert:** The number of missing values matches the planted count (2 in the demo); all imputed vectors are `NA`-free; imputed mean/median statistics stay close to the imputation strategy values.
**⚠️ Defect:** Despite the file name and header mentioning "Mean/Median/Mode", no mode imputation is implemented. No input validation: `mean(x, na.rm=TRUE)` on a non-numeric or all-`NA` vector raises uncontrolled errors. Mean imputation deflates variance and distorts correlations; the script does not document this statistical bias. No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
