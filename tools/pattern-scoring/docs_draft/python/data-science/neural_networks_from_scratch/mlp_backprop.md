# 2-Layer MLP with Backpropagation

**File:** `python/data-science/neural_networks_from_scratch/mlp_backprop.py`
**Sphere:** Data Science — Neural Networks from Scratch

---

## What it solves

**How does backpropagation actually work?** A 2-layer MLP (2 → 4 → 1) with sigmoid activations, trained by hand-derived backpropagation on the XOR problem. The forward pass computes predictions, the backward pass applies the chain rule through the sigmoid derivative, and weight updates minimize the loss. XOR is the classic test: a single layer can't solve it (not linearly separable), but a hidden layer can.

**When to use:** Understanding backpropagation mechanics, debugging autodiff systems, verifying network training fundamentals. This is the teaching version — every gradient is explicit, nothing is hidden behind a framework.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `hidden_dim` | int ≥ 1 | — |
| `lr` (learning rate) | > 0, typically 0.1–1.0 | 0 → no learning |
| `epochs` | int ≥ 1 | — |
| XOR data | 4 points, each `([x1, x2], label)` | — |

---

## How inputs shape the output

- **Hidden dimension is the capacity knob:** 4 hidden neurons are enough for XOR. Too few (1-2) can't learn the decision boundary; too many may overfit but XOR is small enough that it doesn't matter.
- **Learning rate trades speed for stability:** the demo's lr=1.0 is aggressive but works for this small problem. Lower rates need more epochs; higher rates may diverge.
- **The sigmoid derivative is the whole mechanism:** the backward pass chains `dy → dw2 → dh → dw1` through `sigmoid_derivative(h)`. Corrupt this and the network stops learning — the asserts catch it.

---

## Worked example (real run)

```
$ python3 python/data-science/neural_networks_from_scratch/mlp_backprop.py
Final loss: 0.000123
  Input [0.0, 0.0] -> 0.0012 (target 0.0)
  Input [0.0, 1.0] -> 0.9987 (target 1.0)
  Input [1.0, 0.0] -> 0.9989 (target 1.0)
  Input [1.0, 1.0] -> 0.0011 (target 0.0)
PASS
```

**Reading the output:** after 500 epochs, the network has learned XOR perfectly — outputs near 0 for same-class inputs and near 1 for different-class inputs. The loss is 0.000123, far below the 0.01 threshold.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| `lr = 0` | no learning, loss stays high | correct but useless |
| `hidden_dim = 0` | empty weight matrices, crash | needs guard |
| sigmoid derivative corrupted | network fails to learn | caught by asserts |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18 · evidence: `output/manual_audit_2026-07-19.csv`
