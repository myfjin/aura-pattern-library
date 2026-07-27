# class weight imbalance

**Language:** Python · **Sphere:** data-science · **Category:** Model Understanding & Tuning

**Signature:** `(z: float) → float`

## What it does

Class Weights for Imbalanced Classification

Core idea: When classes are imbalanced (e.g., 95% negative, 5% positive), training loss
can favor predicting the majority class. Assigning higher weight to the minority class
penalizes misclassification more, recovering minority recall.

When to use: Binary or multiclass classification with severe class imbalance, where you
care about minority class performance.

## Guarantee

When it runs, class weight imbalance guarantees recall_w >= recall_unw * 0.8; recall_w > 0.1 or recall_unw == 0.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `recall_w >= recall_unw * 0.8`
- `recall_w > 0.1 or recall_unw == 0.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
