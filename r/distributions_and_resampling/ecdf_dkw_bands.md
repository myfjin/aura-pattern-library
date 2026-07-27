# ecdf dkw bands

**Language:** R · **Sphere:** R · **Category:** Distributions & Resampling

## What it does

ECDF and DKW Confidence Bands: empirical CDF with probability coverage
Implements Dvoretzky-Kiefer-Wolfowitz bands: Fn(x) ± ε with ε = sqrt(log(2/α)/(2n))
Core: compute ECDF at order statistics, construct bands, verify true CDF inside bands at 1-α nominal
Planted: normal sample n=100, true CDF N(0,1); over 100 replications, track coverage

## Guarantee

When it runs, ecdf dkw bands guarantees coverage_one > 0.9; avg_coverage > 1 - alpha - 0.05 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `coverage_one > 0.9`
- `avg_coverage > 1 - alpha - 0.05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric sample named `x` and a significance level `alpha` in `(0, 1)`. Default demo uses `n = 100`, `alpha = 0.05`, and `N(0,1)`.
**Core:** Computes the empirical CDF at order statistics and adds/subtracts the DKW epsilon `sqrt(log(2/alpha)/(2*n))`, clipping to `[0, 1]`.
**Assert:** Single-sample coverage of the true CDF is > 0.9; average coverage over 100 repeated samples exceeds `1 - alpha - 0.05`.
**⚠️ Defect:** No input validation: `alpha <= 0` or `alpha >= 1` produces `NaN`/`Inf` epsilon silently. The script evaluates coverage only at sample order statistics, not over a dense grid, so bands between order statistics are not verified. No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
