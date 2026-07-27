# demographic parity metrics

**Language:** Python · **Sphere:** data-science · **Category:** Fairness, Privacy & Robustness

**Signature:** `() → None`

## What it does

Demographic Parity: measure fairness as equalized positive rates across groups.

Tests that disparate impact ratio (minority positive rate / majority positive rate)
and demographic parity difference (DP_diff) differ between biased and unbiased classifiers.
A biased classifier favoring one group shows DP_diff >> 0 and disparate impact << 1;
an unbiased classifier shows both near 0 and 1.

## Guarantee

When it runs, demographic parity metrics guarantees dp_b > 0.2; di_b < 0.7; dp_u < 0.3 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `dp_b > 0.2`
- `di_b < 0.7`
- `dp_u < 0.3`
- `0.7 < di_u < 1.3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
