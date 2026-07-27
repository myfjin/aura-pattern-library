# inverse cdf sampling

**Language:** R · **Sphere:** R · **Category:** Sampling & Simulation

## What it does

Inverse-Transform Sampling: generate samples via F^{-1}(U)
Implements inverse CDF for exponential and logistic; verifies via ks.test against true CDFs
Core: U ~ Uniform(0,1), X = F^{-1}(U) has distribution F; planted params, ks.test not rejected
Planted: exponential(λ=1.5), logistic(μ=2, s=0.8); sample n=100 each

## Guarantee

When it runs, inverse cdf sampling guarantees ks_exp$p.value > 0.05; ks_logistic$p.value > 0.05 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `ks_exp$p.value > 0.05`
- `ks_logistic$p.value > 0.05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; `n=100`, exponential λ=1.5, logistic μ=2 s=0.8 hard-coded.
**Core:** Inverse-transform sampling: exponential `F⁻¹(u)=-log(1-u)/λ`, logistic `F⁻¹(u)=μ+s·log(u/(1-u))`. Verifies each via `ks.test` vs pexp / plogis.
**Assert:** Both KS p>0.05 (not rejected).
**⚠️ Defect:** No domain guard on `u`: `u→1` makes `-log(1-u)→+Inf` (exp) and `log(u/(1-u))→+Inf` (logistic); `u=0` breaks the logistic. n=100 is small for KS power. Params fixed, not caller-supplied.

---
*△ AURA Pattern Library — © Reality Optimizer*
