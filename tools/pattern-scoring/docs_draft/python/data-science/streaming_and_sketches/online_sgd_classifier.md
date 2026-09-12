# Online SGD Classifier

**File:** `python/data-science/streaming_and_sketches/online_sgd_classifier.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Train a model on data that doesn't fit in memory.** Instead of loading the entire dataset and iterating, process one sample at a time, updating weights incrementally. This pattern implements logistic regression trained via online SGD (single pass over the data) and compares it to batch SGD (multiple epochs). On separable data, the online version achieves >70% accuracy in a single pass.

**When to use:** Data is too large to fit in memory, or you need to update models continuously as new data arrives (online learning). Common in ad targeting, recommendation systems, and real-time fraud detection.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `stream` | list of `(features, label)` tuples | — |
| `learning_rate` | > 0 | 0 → no learning |
| `epochs` | int ≥ 1 | — |

---

## How inputs shape the output

- **Online SGD converges in one pass:** on separable data, a single pass achieves >70% accuracy. More passes would improve it further.
- **Batch SGD with multiple epochs does better:** 5 epochs of batch training achieves lower loss and higher accuracy.
- **The online loss is within 3× of batch loss:** a reasonable gap for the 5× difference in training epochs.

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_and_sketches/online_sgd_classifier.py
Online SGD loss (1 epoch): 0.1523
Batch SGD loss (5 epochs): 0.0987
Online accuracy: 94.00%
Batch accuracy: 96.00%
✓ Online SGD Classifier: PASS
```

**Reading the output:** online SGD achieves 94% accuracy in a single pass — close to the batch version's 96% with 5× more training. The loss is within 2× of batch.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| `learning_rate = 0` | no learning, loss stays high | correct but useless |
| empty stream | IndexError | needs guard |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18
