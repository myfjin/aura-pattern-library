# perceptron

**Language:** Python · **Sphere:** data-science · **Category:** Core ML

**Signature:** `(X: List[List[float]], y: List[int], learning_rate: float, max_iterations: int) → Tuple[List[float], float]`

## What it does

Perceptron Learning Algorithm (from scratch).

Core idea: A linear classifier for linearly separable data. The perceptron
iteratively updates weights on misclassified samples using the rule:
w ← w + y_i * x_i for each error. Converges in finite steps on separable data.

When to use: Binary classification on linearly separable data; fast training.

## Guarantee

When it runs, perceptron guarantees accuracy >= 0.9 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `accuracy >= 0.9`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — metamorphic, xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `perceptron_fit(X, y, learning_rate=1.0, max_iterations=100) → (weights, bias)`
**Valid input:** `X: List[List[float]]` non-empty. `y: List[int]` with values 0 or 1 (converted internally to {-1, +1}).
**Core:** Perceptron learning rule. Convert labels to {-1, +1}. Initialize w=0, b=0. For each misclassified sample: w ← w + lr·(yᵢ - ŷ)·xᵢ/2, b ← b + lr·(yᵢ - ŷ)/2. Converges in finite steps on separable data.
**Assert:** On linearly separable 2D data (2 classes, 20 pts each, separated by a margin of 0.5-2.5), accuracy ≥ 90%.
**⚠️ Defect:** The update rule uses `error = y_labels[i] - pred` divided by 2.0, which is non-standard. Classic perceptron: w ← w + yᵢ·xᵢ. This implementation uses w ← w + lr·(yᵢ - ŷ)·xᵢ/2, which is closer to a gradient descent update on squared error than the classic perceptron rule. It still converges on separable data but the convergence proof doesn't directly apply.

---
*△ AURA Pattern Library — © Reality Optimizer*
