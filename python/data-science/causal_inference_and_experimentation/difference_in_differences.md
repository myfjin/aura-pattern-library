# difference in differences

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference & Experimentation

**Signature:** `(n_per_group: int, treatment_effect: float, time_effect: float) → Tuple[List[float], List[float], List[float], List[float]]`

## Guarantee

When it runs, difference in differences guarantees bias < 3.0; estimate_did(pre_c, pre_c, pre_t, pre_t) < 1.0; abs(control_only_effect) < 2.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `bias < 3.0`
- `estimate_did(pre_c, pre_c, pre_t, pre_t) < 1.0`
- `abs(control_only_effect) < 2.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
