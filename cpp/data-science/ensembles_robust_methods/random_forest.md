# random forest

**Language:** C++ · **Sphere:** data-science · **Category:** Ensembles & Robust Methods

**Signature:** `(X: List[Tuple[float, float]], y: List[int], n_trees: int) → List[dict]`

## What it does

random_forest.cpp — Random forest classification with bootstrap samples.

## Guarantee

When it runs, random forest guarantees forest_acc >= single_tree_acc (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `forest_acc >= single_tree_acc`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `random_forest(X, y, n_trees=10) → list of trees (dicts)`
**Valid input:** `X: List[Tuple[float, float]]` — 2D features. `y: List[int]` class labels. `n_trees ≥ 1`.
**Core:** Random forest: train n_trees decision trees (max_depth=5, min_samples=2), each on a bootstrap sample of the data. At each split, consider a random subset of features (size ≈ √p). Each tree grown to max_depth. Prediction = majority vote across trees.
**Assert:** On 2-class 2D synthetic data (40 per class, Gaussians at (3,3) and (7,7) with σ=2), 10 trees, forest accuracy ≥ single tree accuracy.
**⚠️ Defect:** The test only checks training accuracy, not generalization. Forest ≥ single tree on training data is almost guaranteed because the forest has more capacity (10 trees × bootstrap diversity). A proper test would check held-out accuracy or OOB error. Also, the forest doesn't track OOB samples for unbiased evaluation, and the random feature subset is always `sqrt(n_features)` with no configurability.

---
*△ AURA Pattern Library — © Reality Optimizer*
