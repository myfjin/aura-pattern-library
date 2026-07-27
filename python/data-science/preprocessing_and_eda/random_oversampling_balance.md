# random oversampling balance

**Language:** Python · **Sphere:** data-science · **Category:** Preprocessing & EDA

**Signature:** `(X: List[List[float]], y: List[int]) → Tuple[List[List[float]], List[int]]`

## What it does

Random Oversampling and Synthetic Minority Balance Pattern.

Rebalances imbalanced datasets by random oversampling (duplicate minority) and
SMOTE-lite (interpolate between minority neighbors). Core idea: majority class
stays fixed, minority class is augmented to match majority size via repetition
and interpolation.

When to use: imbalanced classification, oversampling minority before training,
creating synthetic samples without upsampling majority, class balance restoration.

## Guarantee

When it runs, random oversampling balance guarantees count0_after == count1_after; count0_after == count0_before; count1_after > count1_before (weak-grade: directional, proven by run).

**Checkable constraints:**

- `count0_after == count1_after`
- `count0_after == count0_before`
- `count1_after > count1_before`
- `count0_smote == count1_smote`
- `count0_smote == count0_before`
- `len(X_smote) > len(X)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
