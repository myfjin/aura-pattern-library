# cramers v effect

**Language:** R · **Sphere:** R · **Category:** Nonparametric & Categorical

**Signature:** `(contingency_table: ?) → ?`

## What it does

cramers_v_effect.R
Cramér's V effect size from chi-square test.
Oracle: chisq.test() for chi-square statistic.
Claim: V computed from chi-square matches oracle; strong association -> high V.
Tolerance: V exact match (rel error <1e-10).

## Guarantee

When it runs, cramers v effect guarantees rel_error_v_strong < 1e-10; rel_error_v_weak < 1e-10; v_strong_manual > v_weak_manual (proven by run).

**Checkable constraints:**

- `rel_error_v_strong < 1e-10`
- `rel_error_v_weak < 1e-10`
- `v_strong_manual > v_weak_manual`
- `v_weak_manual < 0.15`
- `all(c(v_strong_manual, v_weak_manual) >= 0)`
- `all(c(v_strong_manual, v_weak_manual) <= 1)`
- `chi_sq_stat_strong > chi_sq_stat_weak`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `cramers_v <- function(contingency_table)`
**Valid input:** A numeric matrix or table representing a contingency table with at least 2 rows and 2 columns and all non-negative entries.
**Core:** Computes the chi-square statistic from expected counts, then Cramér's V = `sqrt(chi_sq / (n_total * (min_dim - 1)))`. Verifies against V recomputed from `chisq.test(..., correct=FALSE)`.
**Assert:** Strong-association V and weak-association V match the oracle within relative error `1e-10`; strong V exceeds weak V; weak V is `< 0.15`; both V values are in `[0,1]`.
**⚠️ Defect:** No input validation inside the function: empty table, `1x1` table, negative entries, or non-numeric inputs will fail or return garbage. Uses uncorrected Pearson chi-square (explicitly sets `correct=FALSE` in the oracle comparison but the function itself has no correction option). One sanity check (`v_strong_manual > 0.4`) is commented out. The function returns a scalar and does not validate dimensions.

---
*△ AURA Pattern Library — © Reality Optimizer*
