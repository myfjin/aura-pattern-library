# demographic parity metrics

**Language:** C++ · **Oracle sphere:** data-science (this file is the C++ twin) · **Category:** Fairness, Privacy & Robustness

## What it does

Demographic Parity Metrics — C++17 port.
Measures equalized positive rates across groups.

## Guarantee

When it runs, demographic parity metrics guarantees dp_b > 0.2; di_b < 0.7; dp_u < 0.3 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `dp_b > 0.2`
- `di_b < 0.7`
- `dp_u < 0.3`
- `0.7 < di_u < 1.3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
