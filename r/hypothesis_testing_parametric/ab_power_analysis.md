# ab power analysis

**Language:** R · **Sphere:** R · **Category:** Hypothesis Testing — Parametric

## What it does

ab_power_analysis.R
Two-proportion power analysis from normal approximation.
Oracle: power.prop.test() in stats.
Claim: manual n and power calculations match oracle.
Tolerance: n agreement within 1 sample, power rel error <1e-4.

## Guarantee

When it runs, ab power analysis guarantees abs(n_manual - n_oracle) <= 3; abs(power_manual - power_oracle) < 0.05; power_oracle >= power_target * 0.95 (proven by run).

**Checkable constraints:**

- `abs(n_manual - n_oracle) <= 3`
- `power_oracle >= power_target * 0.95`
- `n_manual > 0`
- `power_oracle >= 0`
- `power_oracle <= 1`
- `power_oracle > power_target * 0.95`
- `abs(power_manual - power_oracle) < 0.05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Numeric scalars `p1`, `p2` (proportions in `(0,1)`), `alpha` (significance level in `(0,1)`), and `beta_risk` (type-II risk in `(0,1)`). The demo sets `p1 = 0.40`, `p2 = 0.50`, `alpha = 0.05`, `beta_risk = 0.20`.
**Core:** Computes a two-proportion sample size via the Fleiss normal approximation and then computes achieved power at that sample size. Compares both to `power.prop.test()`.
**Assert:** `n_manual` is within 3 samples of the oracle `n`; the oracle's achieved power is at least `0.95 * power_target`; `abs(power_manual - power_oracle) < 0.05`.
**⚠️ Defect:** No input validation: invalid proportions or negative/≥1 alpha/beta produce uncontrolled or nonsensical results. Uses a normal approximation without continuity correction. Hardcoded two-sided alternative. No function wrapper, so parameters cannot be passed in.

---
*△ AURA Pattern Library — © Reality Optimizer*
