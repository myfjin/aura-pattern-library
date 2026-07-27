# gaussian naive bayes

**Language:** Python · **Sphere:** data-science · **Category:** Model Diagnostics

**Signature:** `(n_per_class: int, seed: int) → Tuple[List[Tuple[float, float]], List[int]]`

## What it does

Gaussian Naive Bayes Classifier

Implements a Gaussian Naive Bayes classifier for continuous features.
Assumes each feature is independently distributed as Gaussian given the class label.

Use this for fast, interpretable classification on continuous data,
especially when feature independence is a reasonable assumption.

## Guarantee

When it runs, gaussian naive bayes guarantees accuracy >= 0.9 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `accuracy >= 0.9`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `fit_gaussian_naive_bayes(X, y) → (class_priors, means_per_class, stds_per_class, classes)`, `predict_gaussian_naive_bayes(x, ...) → int`
**Valid input:** `X: List[Tuple[float, float]]` — 2D features. `y: List[int]` — class labels.
**Core:** Gaussian Naive Bayes classifier. For each class, compute per-feature mean and std (using sample variance, denominator n-1). Predict: posterior ∝ prior × Π P(feature|class) using Gaussian PDF. Assumes feature independence given class.
**Assert:** On 2-class 2D Gaussian data (100 train, 100 test, means at (0,0) and (3,3), σ=1), accuracy ≥ 90%.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
