# rejection sampling beta

**Language:** R · **Sphere:** R · **Category:** Sampling & Simulation

**Signature:** `(x: ?) → ?`

## What it does

Rejection Sampling for Beta(2,5): use uniform envelope, accept/reject via density ratio
Implements Beta density f(x)∝x(1-x)^4 via uniform proposal over [0,1] with envelope constant M
Core: draw from Uniform(0,1), accept if U < f(X)/(M*g(X)); M = max density / g density
Planted: β(α=2,β=5); ks.test not rejected; acceptance rate ≈ 1/M (true rate:integral of β)

## Guarantee

When it runs, rejection sampling beta guarantees ks_result$p.value > 0.05 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `ks_result$p.value > 0.05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper). (Local helper `beta_density(x)` defined but the pattern runs as a script.)
**Valid input:** No params; target Beta(α=2, β=5), uniform proposal, n_target=200 fixed.
**Core:** Rejection sampling from Beta(2,5) with a Uniform(0,1) proposal: envelope constant `M=max` of a 1000-point density grid; accept X if `U < f(X)/M`. Vectorized in blocks of 1000.
**Assert:** `ks.test` vs pbeta not rejected; reports acceptance rate.
**⚠️ Defect:** The envelope `M` is estimated from a **discrete 1000-point grid**, so it can *under*-estimate the true density maximum → acceptance ratio >1 for some x → the accepted sample is no longer exactly Beta (silent bias). For Beta(2,5) the mode is interior so it's fine here, but the method is unsafe for peakier targets. `c()`-growth in the while loop.

---
*△ AURA Pattern Library — © Reality Optimizer*
