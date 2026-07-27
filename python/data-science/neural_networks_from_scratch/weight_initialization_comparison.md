# weight initialization comparison

**Language:** Python · **Sphere:** data-science · **Category:** Neural Networks From Scratch

**Signature:** `(x: float) → float`

## What it does

Weight initialization comparison: naive vs Xavier/He initialization.

Core idea: Build a deeper network (5 layers) and train it with three different
initialization schemes: (1) small random [-0.1, 0.1], (2) large random [-1, 1],
(3) Xavier initialization (std proportional to 1/sqrt(fan_in)). Measure activation
variance layer-to-layer. Xavier should preserve signal variance; naive init should
either explode or vanish.

When to use: Deep network training, preventing vanishing/exploding gradients,
understanding initialization pitfalls.

## Guarantee

When it runs, weight initialization comparison guarantees small_first < xavier_first < large_first or small_first < xavier_first (weak-grade: directional, proven by run).

**Checkable constraints:**

- `small_first < xavier_first < large_first or small_first < xavier_first`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `DeepNetwork(init_scheme="xavier")` — 5-layer network (10→32→32→32→16→1).
**Valid input:** Random 10D input. No training — just forward pass to measure activation variance.
**Core:** Compare three initialization schemes on a 5-layer network: small uniform [-0.1, 0.1], large uniform [-1, 1], Xavier uniform [±√(1/fan_in)]. Measure activation variance at each layer. Xavier preserves variance; small init causes vanishing; large init causes exploding.
**Assert:** On random 10D input, Xavier init maintains activation variance within [0.01, 10] at all layers. Small init produces variance < 0.01 at layer 5. Large init produces variance > 10 or NaN at some layer.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
