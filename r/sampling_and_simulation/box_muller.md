# box muller

**Language:** R · **Sphere:** R · **Category:** Sampling & Simulation

## What it does

Box-Muller Transform: generate bivariate independent gaussians from uniforms
Implements Z1 = sqrt(-2*log(U1)) * cos(2π*U2), Z2 = sqrt(-2*log(U1)) * sin(2π*U2)
Core: two independent uniforms → two independent N(0,1) via trigonometric transform
Planted: n=200 pairs; verify ks.test not rejected, sample mean≈0, var≈1

## Guarantee

When it runs, box muller guarantees abs(sample_sd - 1) < 0.15; ks_result$p.value > 0.05; abs(sample_mean) < 0.1 (proven by run).

**Checkable constraints:**

- `ks_result$p.value > 0.05`
- `abs(sample_mean) < 0.1`
- `abs(sample_sd - 1) < 0.15`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No parameters — `set.seed(42)`, `n_pairs=100` fixed. Depends only on base R `runif`.
**Core:** Box-Muller transform: from two uniforms U1,U2 produces two independent N(0,1) via `r=sqrt(-2*log(U1))`, `z1=r*cos(2πU2)`, `z2=r*sin(2πU2)`. Combines into 200 normals.
**Assert:** `ks.test` vs pnorm not rejected (p>0.05); `|mean|<0.1`; `|sd-1|<0.15`.
**⚠️ Defect:** No guard against `U1=0` → `log(0)=-Inf` → NaN normal (rare but unhandled). Fixed n=100 pairs is a small sample and the sd tolerance (0.15) is loose, so a mildly non-normal generator could still pass. Not reusable — a script, not a `rnorm2()`-style function.

---
*△ AURA Pattern Library — © Reality Optimizer*
