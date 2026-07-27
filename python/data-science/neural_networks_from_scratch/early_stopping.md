# early stopping

**Language:** Python · **Sphere:** data-science · **Category:** Neural Networks From Scratch

**Signature:** `(x: float) → float`

## What it does

Early stopping with patience-based validation monitoring.

Core idea: Train a network and monitor validation loss each epoch. If validation loss
doesn't improve for `patience` consecutive epochs, stop training early and restore the
best weights seen. Prevents overfitting and wasted computation.

When to use: Any supervised training with validation data, preventing overfitting,
efficient hyperparameter search.

## Guarantee

When it runs, early stopping guarantees epochs_trained < 100; val_loss_with_stop <= val_loss_no_stop * 1.1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `epochs_trained < 100`
- `val_loss_with_stop <= val_loss_no_stop * 1.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `NetworkWithEarlyStopping()` → `train_with_early_stopping(train_data, val_data, max_epochs=100, patience=10, lr=0.1) → (epochs_trained, best_val_loss)`
**Valid input:** `train_data, val_data: List[Tuple[List[float], float]]` — 3D inputs, binary targets with 10% noise.
**Core:** 3→6→1 network with sigmoid activations. Train monitors validation loss each epoch. If no improvement for `patience` consecutive epochs, stops and restores best weights. Prevents overfitting.
**Assert:** On 40 train + 40 validation samples (x₀+x₁ > 0 rule, 10% label noise), patience=10, early stopping stops before 100 epochs and val_loss ≤ no-stop val_loss × 1.1.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
