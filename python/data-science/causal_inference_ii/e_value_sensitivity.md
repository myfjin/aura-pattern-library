# e value sensitivity

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference II

**Signature:** `(t1_y1: int, t1_y0: int, t0_y1: int, t0_y0: int) → float`

## What it does

E-value sensitivity analysis: how strong must an unmeasured confounder be to explain away an effect?

E-value = (RR + sqrt(RR*(RR-1))) / 1 for RR > 1. A strong effect (RR=3) needs implausibly
large confounder to explain away; weak effect (RR=1.1) can be explained by modest confounder.
Core claim: strong vs weak effects quantified; numbers demonstrate implausibility thresholds.

## Guarantee

When it runs, e value sensitivity guarantees rr_strong > 2.0; rr_weak < 1.5; e_strong > e_weak * 1.5 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `rr_strong > 2.0`
- `rr_weak < 1.5`
- `e_strong > e_weak * 1.5`
- `e_strong > 1.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
