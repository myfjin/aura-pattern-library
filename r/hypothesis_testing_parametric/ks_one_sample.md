# ks one sample

**Language:** R · **Sphere:** R · **Category:** Hypothesis Testing — Parametric

## What it does

Kolmogorov-Smirnov One-Sample Test: D statistic vs known CDF
Implements empirical CDF and maximum deviation from theoretical CDF
Core: sort data, compute Fn(x) = (# ≤ x)/n, compare to F(x) at each order stat,
D = max(|Fn - F|), compare to ks.test()
Planted: normal sample (accepted under H0), exponential sample (rejected, clearly non-normal)

## Guarantee

When it runs, ks one sample guarantees all.equal(D_normal, unname(oracle_normal$statistic), tolerance = 1e-06); all.equal(D_exp, unname(oracle_exp$statistic), tolerance = 1e-06); oracle_normal$p.value > 0.05 (proven by run).

**Checkable constraints:**

- `all.equal(D_normal, unname(oracle_normal$statistic), tolerance = 1e-06)`
- `oracle_normal$p.value > 0.05`
- `all.equal(D_exp, unname(oracle_exp$statistic), tolerance = 1e-06)`
- `oracle_exp$p.value < 0.05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric sample `x` to be tested against the standard normal CDF `pnorm(0,1)`. The demo creates `x_normal <- rnorm(50,0,1)` and `x_exp <- rexp(50,1)`.
**Core:** Computes the ECDF at order statistics (`i/n` and `(i-1)/n`), forms `D+` and `D-`, and compares the D statistic to `ks.test()`. Also checks that the normal sample is accepted and the exponential sample is rejected at `alpha = 0.05`.
**Assert:** `D_normal` and `D_exp` match the `ks.test()` statistic within `1e-6`; normal sample p-value `> 0.05`; exponential sample p-value `< 0.05`.
**⚠️ Defect:** Tests only against fixed `pnorm(0,1)` parameters. If the true distribution has different mean/variance or is not normal, the test is not the Lilliefors-corrected version and may be invalid. No input validation. No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
