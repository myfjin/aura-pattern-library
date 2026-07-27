# dropout regularization sim

**Language:** Python · **Sphere:** data-science · **Category:** Neural Networks From Scratch

**Signature:** `(x: float) → float`

## What it does

Dropout regularization: network with vs without dropout on a noisy dataset.

Core idea: Generate a small noisy dataset prone to overfitting. Train two networks:
one with dropout (randomly zero hidden activations during training only) and
one without. The dropout version regularizes the network and generalizes better
to held-out validation data, especially on small datasets.

When to use: Overfitting prevention, regularization, robust model training.

## Guarantee

When it runs, dropout regularization sim guarantees dropout_gap <= no_dropout_gap (weak-grade: directional, proven by run).

**Checkable constraints:**

- `dropout_gap <= no_dropout_gap`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `SimpleNetwork(hidden_dim=8, use_dropout=False, dropout_rate=0.3)` → `train(data, epochs, lr)` → `evaluate(data) → (loss, correct)`
**Valid input:** `train_data: List[Tuple[List[float], float]]` — 4D inputs, binary targets with 30% label noise. `val_data: List[Tuple[List[float], float]]` — clean validation set.
**Core:** Compare two 4→8→1 networks (sigmoid), one with dropout (randomly zero 15% of hidden activations during training) and one without. Dropout should show smaller generalization gap (val_loss - train_loss) on a small noisy dataset.
**Assert:** On 25 noisy training samples (30% label noise) and 100 clean validation samples, 60-80 epochs at lr=0.5, dropout generalization gap ≤ no-dropout gap.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
