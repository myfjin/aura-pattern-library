# decision tree

**Language:** Python · **Sphere:** programming · **Category:** Reasoning

## What it does

Simple Decision Tree Classifier

A complete implementation of a decision tree classifier with information gain,
prediction, and pruning capabilities.

## Guarantee

When it runs, decision tree guarantees preds == truth; sum(preds) == 6; train_acc == 1.0 (proven by run).

**Checkable constraints:**

- `train_acc == 1.0`
- `preds == truth`
- `sum(preds) == 6`
- `acc_after >= acc_before`
- `acc_after == 1.0`
- `flat.predict([[9, 9], [0, 0]]) == [7, 7]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
