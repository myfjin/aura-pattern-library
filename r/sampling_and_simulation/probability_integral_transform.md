# probability integral transform

**Language:** R · **Sphere:** R · **Category:** Sampling & Simulation

## What it does

Probability Integral Transform: U = F(X) ~ Uniform(0,1) under correct F
Implements: if X ~ F, then F(X) ~ Uniform(0,1); verifies via ks.test
Core: if F is correct, PIT uniform and ks.test not rejected; if F wrong, ks.test rejects
Planted: normal X, test against pnorm(true) [accept], pexp [reject]

## Guarantee

When it runs, probability integral transform guarantees ks_correct$p.value > 0.05; ks_wrong$p.value < 0.05; mean_wrong < 0.3 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `ks_correct$p.value > 0.05`
- `ks_wrong$p.value < 0.05`
- `mean_wrong < 0.3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; n=150 draws from N(0,1) fixed.
**Core:** Probability Integral Transform: applying the *correct* CDF F(X) to X yields Uniform(0,1); applying a *wrong* CDF does not. Tests both the true pnorm and a deliberately-wrong pexp.
**Assert:** correct-CDF KS p>0.05 (not rejected); wrong-CDF KS p<0.05 (rejected); `mean(u_wrong)<0.3`.
**⚠️ Defect:** Thin coverage — a single correct vs single wrong CDF; the `mean(u_wrong)<0.3` bound is a planted-specific expectation, not a general property. No input validation; not reusable as a function.

---
*△ AURA Pattern Library — © Reality Optimizer*
