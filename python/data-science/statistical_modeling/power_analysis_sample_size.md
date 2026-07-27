# power analysis sample size

**Language:** Python · **Sphere:** data-science · **Category:** Statistical Modeling

**Signature:** `(p: float) → float`

## What it does

Power Analysis: Sample Size for Two-Proportion Z-Test.

Computes required sample size per group for a given effect size, alpha, and power
using normal approximation. Verifies the computed n reproduces the target power.
Use for study design when comparing two proportions.

## Guarantee

When it runs, power analysis sample size guarantees achieved_power >= target_power - 0.05; power_lower < achieved_power (weak-grade: directional, proven by run).

**Checkable constraints:**

- `achieved_power >= target_power - 0.05`
- `power_lower < achieved_power`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `sample_size_two_proportion(p1, p2, alpha=0.05, target_power=0.80) → int`
**Valid input:** `p1, p2: float` in (0, 1). `alpha` in (0, 1). `target_power` in (0, 1).
**Core:** Compute required sample size per group for two-proportion z-test. Uses normal approximation: n = (z_α/2 + z_β)² · se² / δ². Verifies by computing achieved power at the estimated n. Uses rational approximation for normal quantile.
**Assert:** For p1=0.3, p2=0.5, α=0.05, power=0.80, computed n achieves power ≥ 0.75, and n-1 gives lower power.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
