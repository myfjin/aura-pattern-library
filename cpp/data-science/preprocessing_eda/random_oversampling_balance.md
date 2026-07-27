# random oversampling balance

**Language:** C++ · **Sphere:** data-science · **Category:** Preprocessing & EDA

**Signature:** `(X: List[List[float]], y: List[int]) → Tuple[List[List[float]], List[int]]`

## What it does

random_oversampling_balance.cpp — Random oversampling and SMOTE-lite for class balance.

## Guarantee

When it runs, random oversampling balance guarantees count0_after == count1_after; count0_after == count0_before; count1_after > count1_before (weak-grade: directional, proven by run on the PY original).

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
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
