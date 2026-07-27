# numerical gradient check

**Language:** Python · **Sphere:** data-science · **Category:** Neural Networks From Scratch

**Signature:** `(x: float) → float`

## What it does

Verify analytic backprop gradients against finite-difference numerical gradients.

Core idea: Compute gradients both ways (backprop and numerical finite-difference)
on the same tiny network. Compare element-wise; if max relative error < 1e-4,
backprop is correct. Essential debugging pattern for any hand-rolled network.

When to use: Verifying custom backprop implementations, debugging gradient bugs,
validating autodiff before scaling up.

## Guarantee

When it runs, numerical gradient check guarantees max_rel_err < 0.0001 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `max_rel_err < 0.0001`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `TinyNetwork()` → `analytic_gradients(x, y_true) → (dw1, db1, dw2, db2)` → `numerical_gradient(x, y_true, param_name, indices, eps=1e-5) → float`
**Valid input:** Fixed tiny network (2→2→1) with hardcoded weights. `x: List[float]` length 2. `y_true: float`.
**Core:** Verify backprop gradients against finite-difference numerical gradients (central difference). Compare all 13 parameters (4 w1, 2 b1, 2 w2, 1 b2). Max relative error < 1e-4 confirms backprop is correct.
**Assert:** On fixed test point x=[0.5, -0.3], y_true=0.7, max relative error between analytic and numerical gradients < 1e-4.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
