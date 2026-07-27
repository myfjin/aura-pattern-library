# k anonymity generalization

**Language:** Python · **Sphere:** data-science · **Category:** Fairness, Privacy & Robustness

**Signature:** `() → None`

## What it does

k-Anonymity: generalize quasi-identifiers until each combination appears >= k times.

Creates a dataset with age/gender quasi-identifiers, generalizes age ranges to achieve
k-anonymity (k=3), and verifies that each generalized combination appears >= k times.
Utility loss is measured as the difference in granularity.

## Guarantee

When it runs, k anonymity generalization guarantees count >= k; utility_loss > 0.1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `count >= k`
- `utility_loss > 0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
