# placebo test causal

**Language:** C++ · **Sphere:** data-science · **Category:** Causal Inference & Experimentation

**Signature:** `(T: List[int], Y: List[float]) → float`

## What it does

placebo_test_causal.cpp
Placebo test for causal inference using permuted treatment labels.

## Guarantee

When it runs, placebo test causal guarantees true_effect_estimate > avg_permuted; p_value_approx < 0.1 (proven by run on the PY original).

**Checkable constraints:**

- `true_effect_estimate > avg_permuted`
- `p_value_approx < 0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
