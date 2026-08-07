# simpsons paradox demo

**Language:** Python · **Sphere:** data-science · **Category:** Applied DS Practice

**Signature:** `(numerator: int, denominator: int) → float`

## What it does

Simpson's Paradox: aggregate trend reverses within strata.

An association between two variables at the aggregate level reverses direction
when data is split by a confounding variable (stratum). Classic example:
treatment A beats B overall, but B beats A within every subgroup.

Use: causal inference, detecting confounding, interpreting correlations.

## Guarantee

When it runs, simpsons paradox demo guarantees not b_wins_aggregate (weak-grade: directional, proven by run).

**Checkable constraints:**

- `b_wins_s1`
- `b_wins_s2`
- `not b_wins_aggregate`
- `paradox_detected`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def compute_rate(numerator: int, denominator: int) -> float:`
**Valid input:** `denominator > 0`; `0 <= numerator <= denominator`.
**Core:** Demonstrates Simpson's paradox: treatment B can beat treatment A within every stratum yet lose in the aggregate because the strata have different base rates and unequal treatment allocation.
**Assert:** On the planted two-strata example, B wins stratum 1 (90% vs 80%), B wins stratum 2 (12% vs 10%), but A wins aggregate (73% vs 19%). The paradox is detected and asserted.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
