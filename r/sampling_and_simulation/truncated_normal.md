# truncated normal

**Language:** R · **Sphere:** R · **Category:** Sampling & Simulation

## What it does

Truncated Normal: N(μ,σ²) on [a,b] via acceptance-rejection
Implements: proposal from untruncated N(μ,σ²), accept if X in [a,b]
Core: compute analytic truncated mean E[X|a<X<b] and var using pnorm/dnorm, verify sample stats
Planted: N(0,1) truncated to [0,2]; analytic moments from formula

## Guarantee

When it runs, truncated normal guarantees abs(mean_sample - mean_trunc_analytic) < 0.15; abs(var_sample - var_trunc_analytic) < 0.2 (proven by run).

**Checkable constraints:**

- `abs(mean_sample - mean_trunc_analytic) < 0.15`
- `abs(var_sample - var_trunc_analytic) < 0.2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; N(0,1) truncated to [a=0, b=2], n_target=500 fixed.
**Core:** Truncated-normal sampling by rejection (draw N(μ,σ), keep those in [a,b]); compares sample mean/var to the closed-form truncated moments (via φ, Φ at standardized α,β).
**Assert:** `|mean_sample − mean_analytic|<0.15`; `|var_sample − var_analytic|<0.2`.
**⚠️ Defect:** Pure **rejection** truncation is inefficient when the truncation interval carries little probability mass (here [0,2] under N(0,1) keeps ~48%, so acceptable, but the method degrades badly for tail truncations — no fallback to inverse-CDF truncation). Draws in fixed blocks of 5000; variance tolerance (0.2) is loose.

---
*△ AURA Pattern Library — © Reality Optimizer*
