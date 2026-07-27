# heterogeneous effects subgroups

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference II

**Signature:** `(t: List[int], y: List[float], subgroup: List[int], sg_val: int) → float`

## Guarantee

When it runs, heterogeneous effects subgroups guarantees abs(ate_group_0 - 1.0) < 0.5; abs(ate_group_1 - 3.0) < 0.5; abs(ate_group_1 - ate_group_0) > 1.0 (proven by run).

**Checkable constraints:**

- `abs(ate_group_0 - 1.0) < 0.5`
- `abs(ate_group_1 - 3.0) < 0.5`
- `abs(ate_group_1 - ate_group_0) > 1.0`
- `min(ate_group_0, ate_group_1) < ate_pooled < max(ate_group_0, ate_group_1) + 0.3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
