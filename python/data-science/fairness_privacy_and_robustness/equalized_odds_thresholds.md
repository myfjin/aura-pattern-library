# equalized odds thresholds

**Language:** Python · **Sphere:** data-science · **Category:** Fairness, Privacy & Robustness

**Signature:** `() → None`

## What it does

Equalized Odds: per-group thresholds equalize TPR across groups.

Shows that a single global threshold cannot close a planted TPR gap between groups,
but per-group thresholds can. TPR gap before and after is measured and asserted.

## Guarantee

When it runs, equalized odds thresholds guarantees gap_global > 0.1; gap_per < gap_global (weak-grade: directional, proven by run).

**Checkable constraints:**

- `gap_global > 0.1`
- `gap_per < gap_global`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
