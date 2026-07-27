# chi square independence

**Language:** R · **Sphere:** data-science · **Category:** Statistics & Testing

**Signature:** `(contingency_table: List[List[int]]) → Tuple[float, float, bool]`

## What it does

Chi-Square Test of Independence
Implements chi-square statistic from expected counts; verifies against chisq.test()
Use when: testing association between two categorical variables

## Guarantee

When it runs, chi square independence guarantees not sig_indep (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `not sig_indep`
- `sig_assoc`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this R twin (twin agreement is the evidence: hard, reseed_ref, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def chi_square_independence(contingency_table: List[List[int]]) -> Tuple[float, float, bool]:`
**Valid input:** `contingency_table` is a non-empty rectangular matrix of non-negative integers with non-zero grand total.
**Core:** Pearson chi-square test of independence. Computes expected cell counts from row and column marginals, sums `(observed - expected)^2 / expected`, and compares to a hardcoded critical-value table for alpha=0.05.
**Assert:** A balanced, independent 2×3 table is not significant; a diagonal-dominant 2×3 table is significant.
**⚠️ Defect:** The p-value is only a rough approximation (0.05 if significant, 0.95 otherwise) rather than a real chi-square CDF computation. The critical-value table covers df 1–10; tables outside that range use a default df=1 critical value, which is wrong for larger tables.

---
*△ AURA Pattern Library — © Reality Optimizer*
