# softmax regression

**Language:** Python · **Sphere:** data-science · **Category:** Neural Networks From Scratch

**Signature:** `(logits: List[float]) → List[float]`

## What it does

Multi-class softmax regression with cross-entropy loss.

Core idea: Learn to classify 3 synthetic clusters in 2D using a linear classifier
with softmax output and cross-entropy loss. Gradient descent updates weights to
maximize log-probability of true class.

When to use: Multiclass classification, understanding softmax and cross-entropy,
baseline for any categorical prediction task.

## Guarantee

When it runs, softmax regression guarantees accuracy >= 0.9 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `accuracy >= 0.9`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `SoftmaxRegression(input_dim=2, num_classes=3, lr=0.01)` → `train(data, epochs)` → `predict(x) → int`
**Valid input:** `data: List[Tuple[List[float], int]]` — feature vectors and class labels (0..num_classes-1).
**Core:** Multi-class softmax regression with cross-entropy loss. Forward: logits = Wx + b, softmax normalization (subtract max for numerical stability). Backward: gradient of cross-entropy w.r.t. logits is (probs - one_hot). Update W and b via SGD.
**Assert:** On 3 synthetic Gaussian clusters (10 pts each, centered at (0,0), (3,0), (1.5,3) with σ=0.3), 100 epochs at lr=0.1, accuracy ≥ 90%.
**⚠️ Defect:** The `train` method computes final loss by re-running the forward pass after training, but the loss printed during training is accumulated per-epoch and then overwritten. The final loss returned is computed on a separate pass, which is correct but the per-epoch loss tracking is misleading (it's the cumulative sum, not the average).

---
*△ AURA Pattern Library — © Reality Optimizer*
