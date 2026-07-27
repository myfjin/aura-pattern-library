# order statistics

**Language:** R · **Sphere:** R · **Category:** Sampling & Simulation

## What it does

Order Statistics: distribution of min/max/median of n uniforms
Implements CDF and PDF of order statistics via Beta distributions
Core: X_{(k)} ~ Beta(k, n-k+1) for uniform order statistics; verify via ks.test on min/max
Planted: n=10 uniforms, track min (Beta(1,10)), max (Beta(10,1)), ks.test not rejected

## Guarantee

When it runs, order statistics guarantees ks_min$p.value > 0.05; ks_max$p.value > 0.05; mean_min < 0.1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `ks_min$p.value > 0.05`
- `ks_max$p.value > 0.05`
- `mean_min < 0.1`
- `mean_max > 0.9`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; n=10 uniforms, 200 replications fixed.
**Core:** Order statistics of n uniforms: min ~ Beta(1,n), max ~ Beta(n,1). Loops 200× computing min/max, verifies distribution via `ks.test` vs pbeta.
**Assert:** min KS p>0.05, max KS p>0.05; `mean(min)<0.1`, `mean(max)>0.9`.
**⚠️ Defect:** Only min and max are distribution-tested — the **median** order statistic is discussed in comments (`Beta(5,6)/Beta(6,1)`) but never actually verified. Grows result vectors in an explicit R loop (slow, though preallocated here). 200 reps is a modest sample for KS.

---
*△ AURA Pattern Library — © Reality Optimizer*
