# walk forward early stopping

**Language:** Python · **Sphere:** data-science · **Category:** Composed Tools

**Signature:** `(X: List[List[float]], r: List[float]) → Stump`

## What it does

Walk-Forward Early Stopping — training halted by the future, not by a random split.

COMPOSED PATTERN: early_stopping (Neural Networks) x walk_forward_validation
(Time Series) — embedding bridge 0.502, found 2026-07-06. Both parents encode
the same ethic — judge yourself only on data from AFTER your training window —
and their child is a tool neither field names: iterative training (here,
gradient-boosted stumps on lag features) monitored per-round on a FORWARD
time window, stopped with patience when forward error degrades. A random
validation split would leak future regime into training; the forward window
cannot.

Use when: tuning training duration/rounds for any iterative model on
time-ordered data.

## Guarantee

When it runs, walk forward early stopping guarantees train_final < best_fw; final_fw > best_fw * 1.05; stopped_at < max_rounds (weak-grade: directional, proven by run).

**Checkable constraints:**

- `train_final < best_fw`
- `final_fw > best_fw * 1.05`
- `stopped_at < max_rounds`
- `stopped_at - best_round == patience`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — positive, xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
