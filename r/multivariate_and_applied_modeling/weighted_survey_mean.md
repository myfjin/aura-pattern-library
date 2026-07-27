# weighted survey mean

**Language:** R · **Sphere:** R · **Category:** Multivariate & Applied Modeling

## What it does

weighted_survey_mean.R
Weighted mean with design effect-adjusted standard error for survey data.
Oracle: weighted.mean() for means; manual SE with design effect correction.
Claim: weighted mean corrects for planted oversampling bias; SE accounts for design.
Tolerance: weighted mean exact match; SE agreement <5%.

## Guarantee

When it runs, weighted survey mean guarantees abs(weighted_mean_result - true_mean) < abs(naive_mean - true_mean); abs(weighted_mean_result - true_mean) < 5; abs(sum(weights) - (n1_pop + n2_pop)) < 1e-06 (proven by run).

**Checkable constraints:**

- `abs(weighted_mean_result - true_mean) < abs(naive_mean - true_mean)`
- `abs(weighted_mean_result - true_mean) < 5`
- `se_design_adj > 0`
- `se_naive > 0`
- `se_design_adj >= se_naive * 0.8`
- `!is.na(weighted_mean_result)`
- `all(weights > 0 & is.finite(weights))`
- `abs(sum(weights) - (n1_pop + n2_pop)) < 1e-06`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; 2 strata (pop 1000 @μ50 / 4000 @μ100), survey oversamples stratum 1 (200) vs stratum 2 (100).
**Core:** Design-weighted (Horvitz-Thompson-style) survey mean: inverse-inclusion weights `w = N_stratum/n_stratum`, `weighted.mean`, plus a design-adjusted variance/SE using normalized weights and Kish effective sample size `n_eff = (Σw)²/Σw²`.
**Assert:** weighted mean closer to the true population mean than the naïve mean; `|weighted − true| < 5`; design-adjusted and naïve SE both > 0.
**⚠️ Defect:** Sampling is without replacement but the variance uses no **finite-population correction**, so the design SE is slightly conservative. Only two strata, weights hard-coded to the planted design; no guard for a stratum with zero surveyed units (division by zero in the weight).

---
*△ AURA Pattern Library — © Reality Optimizer*
