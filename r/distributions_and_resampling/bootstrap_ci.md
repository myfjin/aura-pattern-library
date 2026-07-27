# bootstrap ci

**Language:** R · **Sphere:** R · **Category:** Distributions & Resampling

## What it does

Bootstrap Confidence Interval
Implements percentile bootstrap; verifies coverage of true mean over repeated runs
Use when: estimating CI without distributional assumptions

## Guarantee

When it runs, bootstrap ci guarantees all.equal(boot_se, sample_se, tolerance = 0.1); true_mean >= ci_lower && true_mean <= ci_upper (proven by run).

**Checkable constraints:**

- `true_mean >= ci_lower && true_mean <= ci_upper`
- `all.equal(boot_se, sample_se, tolerance = 0.1)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric vector named `y` and a scalar `true_mean`. The script generates its own demo sample if `y` is absent.
**Core:** Draws `B = 1000` bootstrap resamples with replacement, computes the mean of each, and returns the 2.5th and 97.5th percentile intervals.
**Assert:** The planted `true_mean` falls inside the percentile CI; the bootstrap SE approximates the analytical sample SE within 10%.
**⚠️ Defect:** Hardcoded `B = 1000` and `alpha = 0.05`; no parameterization. Uses the percentile method only — no BCa or bias correction. `NA` values in `y` silently contaminate bootstrap means. No input validation. No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
