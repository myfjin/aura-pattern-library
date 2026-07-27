# online sgd classifier

**Language:** Python · **Sphere:** data-science · **Category:** Streaming & Sketches

**Signature:** `(stream: List[Tuple[List[float], float]], learning_rate: float, epochs: int) → Tuple[List[float], float]`

## What it does

Online Stochastic Gradient Descent Classifier

Core idea: Train a logistic regressor in a single pass over a stream via SGD, updating
weights with each sample. Should converge close to batch solution on separable data.

When to use: Data is too large to fit in memory, or you need to update models continuously
as new data arrives (online learning).

## Guarantee

When it runs, online sgd classifier guarantees online_acc > 0.7; online_loss < batch_loss * 3 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `online_acc > 0.7`
- `online_loss < batch_loss * 3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def logistic(z: float) -> float:`, `def online_sgd_classifier(stream: List[Tuple[List[float], float]], learning_rate: float = 0.01, epochs: int = 1) -> Tuple[List[float], float]:`, `def batch_sgd_classifier(X: List[List[float]], y: List[float], learning_rate: float = 0.01, epochs: int = 10) -> Tuple[List[float], float]:`
**Valid input:** `stream` is a list of `(feature_vector, binary_label)` tuples; all feature vectors have the same dimension; labels are 0 or 1.
**Core:** Logistic-regression training via online SGD (single pass) and batch SGD (multiple epochs). Uses a clamped sigmoid and binary cross-entropy loss.
**Assert:** Online SGD on seeded separable 2D data achieves >70% accuracy; online loss is within 3× of batch loss.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
