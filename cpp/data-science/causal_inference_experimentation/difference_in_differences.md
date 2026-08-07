# difference in differences

**Language:** C++ · **Oracle sphere:** data-science (this file is the C++ twin) · **Category:** Causal Inference & Experimentation

## What it does

Difference-in-Differences — C++17 port.
Two groups, before/after, parallel trends, recovers planted treatment effect.

## Guarantee

When it runs, difference in differences guarantees bias < 3.0; estimate_did(pre_c, pre_c, pre_t, pre_t) < 1.0; abs(control_only_effect) < 2.0 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `bias < 3.0`
- `estimate_did(pre_c, pre_c, pre_t, pre_t) < 1.0`
- `abs(control_only_effect) < 2.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
