# permutation feature importance

**Language:** Python · **Sphere:** data-science · **Category:** Model Understanding & Tuning

**Signature:** `(X: List[List[float]], y: List[float]) → Tuple[float, float, float]`

## What it does

Permutation Feature Importance

Core idea: Shuffle each feature independently on held-out data and measure the drop in model
performance. Features whose shuffling hurts performance are important; noise features don't affect
predictions when shuffled.

When to use: You've trained a model and want to rank features by their predictive contribution,
agnostic to the model's internal structure.

## Guarantee

When it runs, permutation feature importance guarantees imp_f1 > imp_f2; imp_f1 > 0.5 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `imp_f1 > imp_f2`
- `imp_f1 > 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
