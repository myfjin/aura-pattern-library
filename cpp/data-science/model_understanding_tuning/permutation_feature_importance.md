# permutation feature importance

**Language:** C++ · **Oracle sphere:** data-science (this file is the C++ twin) · **Category:** Model Understanding & Tuning

## What it does

permutation_feature_importance.cpp
Permutation feature importance with simple linear model.

## Guarantee

When it runs, permutation feature importance guarantees imp_f1 > imp_f2; imp_f1 > 0.5 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `imp_f1 > imp_f2`
- `imp_f1 > 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
