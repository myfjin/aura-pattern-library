# placebo test causal

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference & Experimentation

**Signature:** `(T: List[int], Y: List[float]) → float`

## What it does

Placebo Test for Causal Inference.

Under the null (no treatment effect), permuting treatment labels should destroy
the measured effect. Under the alternative (true treatment effect), the effect
persists under the true assignment but disappears under permuted assignments.
We verify that true assignment recovers effect, permuted assignments do not.

## Guarantee

When it runs, placebo test causal guarantees true_effect_estimate > avg_permuted; p_value_approx < 0.1 (proven by run).

**Checkable constraints:**

- `true_effect_estimate > avg_permuted`
- `p_value_approx < 0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
