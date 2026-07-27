# label noise robust loss

**Language:** Python · **Sphere:** data-science · **Category:** Fairness, Privacy & Robustness

**Signature:** `() → None`

## What it does

Label Noise Robustness: MAE degrades less than cross-entropy under label noise.

Trains a simple classifier with noisy labels (20% symmetric label flip) and compares
accuracy degradation under MAE loss versus cross-entropy. MAE is more robust.

## Guarantee

When it runs, label noise robust loss guarantees degradation_mae <= degradation_ce + 0.01 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `degradation_mae <= degradation_ce + 0.01`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
