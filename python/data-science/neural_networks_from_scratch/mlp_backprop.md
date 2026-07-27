# mlp backprop

**Language:** Python · **Sphere:** data-science · **Category:** Neural Networks From Scratch

**Signature:** `(x: float) → float`

## What it does

2-Layer MLP trained by hand-derived backpropagation on XOR.

Core idea: Manually implement the forward pass (linear -> sigmoid), backward pass
(chain rule through sigmoid), and weight updates. Learn to solve XOR by driving
loss to near zero.

When to use: Understanding backpropagation mechanics, debugging autodiff systems,
verifying network training fundamentals.

## Guarantee

When it runs, mlp backprop guarantees final_loss < 0.01; error < 0.2 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `final_loss < 0.01`
- `error < 0.2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `SimpleMLPBackprop.__init__(hidden_dim=4, lr=1.0)` → `train(data, epochs)` → `forward(x) → (y_pred, h)`
**Valid input:** `data: List[Tuple[List[float], float]]` — 2D inputs, scalar targets. `epochs ≥ 1`.
**Core:** 2-layer MLP (2→hidden→1) with sigmoid activations, trained by hand-derived backpropagation on XOR. Forward: linear → sigmoid per layer. Backward: chain rule through sigmoid derivative s(1-s). Update: w ← w - lr·dw. MSE loss.
**Assert:** On XOR dataset (4 points), 500 epochs at lr=1.0, hidden_dim=4, final loss < 0.01 and all prediction errors < 0.2.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
