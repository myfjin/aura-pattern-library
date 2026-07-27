# ab test proportions

**Language:** Python · **Sphere:** data-science · **Category:** Statistics & Testing

**Signature:** `(conversions_a: int, trials_a: int, conversions_b: int, trials_b: int) → Tuple[float, float, float]`

## What it does

A/B Test for Two Proportions

Core idea: Test whether two conversion rates differ using a z-test for proportions.
Compute pooled standard error under the null, then the z-statistic. Also compute effect
size (Cohen's h) to quantify the practical difference.

When to use: Compare two click-through rates, conversion rates, or any binary outcomes
in A/B testing scenarios.

## Guarantee

When it runs, ab test proportions guarantees p_null > 0.05; p_alt < 0.05; abs(h_alt) > 0.1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `p_null > 0.05`
- `p_alt < 0.05`
- `abs(h_alt) > 0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def ab_test_proportions(conversions_a: int, trials_a: int, conversions_b: int, trials_b: int) -> Tuple[float, float, float]:`, `def normal_cdf(z):`
**Valid input:** Non-negative integer counts with `0 <= conversions_a <= trials_a`, same for group B, and at least some successes or failures so the pooled proportion is defined.
**Core:** Two-proportion z-test. Computes a pooled standard error under the null, the z-statistic, an approximate two-tailed p-value via a Hart/Abramowitz & Stegun normal CDF, and Cohen's h effect size.
**Assert:** On two roughly equal conversion rates (10/100 vs 11/100), the p-value is above 0.05; on a planted 15% vs 10% split (30/200 vs 15/200), the p-value is below 0.05 and Cohen's h is non-negligible.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
