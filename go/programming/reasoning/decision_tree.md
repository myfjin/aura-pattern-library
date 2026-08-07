# decision tree

**Language:** Go · **Oracle sphere:** programming (this file is the Go twin) · **Category:** Reasoning

## What it does

decision_tree: simple decision tree classifier with information gain and pruning.

## Guarantee

When it runs, decision tree guarantees preds == truth; sum(preds) == 6; train_acc == 1.0 (proven by run on the PY-PROG original).

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
- **Independent oracle:** — established on the PY-PROG original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
