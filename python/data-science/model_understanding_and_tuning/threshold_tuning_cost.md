# threshold tuning cost

**Language:** Python · **Sphere:** data-science · **Category:** Model Understanding & Tuning

**Signature:** `(y_true: List[float], y_scores: List[float], threshold: float, cost_fp: float, cost_fn: float) → float`

## Guarantee

When it runs, threshold tuning cost guarantees opt_cost < default_cost; opt_threshold < 0.5; opt_cost < default_cost * 0.8 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `opt_cost < default_cost`
- `opt_threshold < 0.5`
- `opt_cost < default_cost * 0.8`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
