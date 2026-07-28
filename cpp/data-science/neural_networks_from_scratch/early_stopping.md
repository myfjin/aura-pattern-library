# early stopping

**Language:** C++ · **Sphere:** data-science · **Category:** Neural Networks From Scratch

**Signature:** `(x: float) → float`

## What it does

Early stopping with patience-based validation monitoring.
C++17 self-contained port with full parity to Python oracle.

## Guarantee

When it runs, early stopping guarantees epochs_trained < 100; val_loss_with_stop <= val_loss_no_stop * 1.1 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `epochs_trained < 100`
- `val_loss_with_stop <= val_loss_no_stop * 1.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `NetworkWithEarlyStopping()` → `train_with_early_stopping(train_data, val_data, max_epochs=100, patience=10, lr=0.1) → (epochs_trained, best_val_loss)`
**Valid input:** `train_data, val_data: List[Tuple[List[float], float]]` — 3D inputs, binary targets with 10% noise.
**Core:** 3→6→1 network with sigmoid activations. Train monitors validation loss each epoch. If no improvement for `patience` consecutive epochs, stops and restores best weights. Prevents overfitting.
**Assert:** On 40 train + 40 validation samples (x₀+x₁ > 0 rule, 10% label noise), patience=10, early stopping stops before 100 epochs and val_loss ≤ no-stop val_loss × 1.1.
**⚠ Retrofit NOT in this twin:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E input-contract retrofit on the PY original (7497d40, 2026-07-21). That pass deliberately excluded the compiled lanes, so this C++ twin does NOT carry the contract its source now enforces. Declared in MANIFEST.json `twin_contract_divergence`; unblocking it needs the cpp attack lane. Corrected 2026-07-28 — the card previously claimed the fix was in this file.

---
*△ AURA Pattern Library — © Reality Optimizer*
