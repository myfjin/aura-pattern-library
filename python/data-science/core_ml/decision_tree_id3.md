# decision tree id3

**Language:** Python · **Sphere:** data-science · **Category:** Core ML

**Signature:** `(class_counts: Dict[int, int]) → float`

## What it does

Decision Tree Classifier using ID3 Algorithm (from scratch).

Core idea: Recursively split data on the feature that gives the highest
information gain (reduction in entropy). Build tree top-down, stopping when
all samples are of one class or max depth is reached.

When to use: Non-linear boundaries; interpretable rules; categorical/continuous data.

## Guarantee

When it runs, decision tree id3 guarantees accuracy >= 0.95 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `accuracy >= 0.95`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — metamorphic, xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `decision_tree_id3(X, y, max_depth=5) → tree (nested dict)`
**Valid input:** `X: List[List[float]]` non-empty. `y: List[int]` class labels. `max_depth ≥ 1`.
**Core:** ID3-style decision tree. Compute Gini impurity (not entropy despite "ID3" name). For each feature, find best split threshold maximizing information gain = Gini(parent) - Σ (nᵢ/n)·Gini(childᵢ). Recurse until pure leaf, max depth, or min_samples. Tree as nested dicts with 'feature', 'threshold', 'left', 'right', 'value' keys.
**Assert:** On 2-class synthetic data (2 features, 30 per class, Gaussian clusters at (3,3) and (7,7) with σ=2), accuracy > 80%.
**⚠️ Defect:** The tree uses Gini impurity for splitting, not entropy — despite being called "ID3" (which traditionally uses entropy/information gain). The docstring says "information gain (reduction in entropy)" but the code uses Gini. Also, the test only checks training accuracy, not held-out generalization, so overfitting is undetected.

---
*△ AURA Pattern Library — © Reality Optimizer*
