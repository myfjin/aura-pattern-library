# randomized response

**Language:** C++ · **Sphere:** data-science · **Category:** Fairness, Privacy & Robustness

**Signature:** `() → None`

## What it does

randomized_response.cpp — Privacy-preserving survey bias correction.

## Guarantee

When it runs, randomized response guarantees abs(unbiased_estimate - true_rate) < 0.2; naive_error > unbiased_error (proven by run on the PY original).

**Checkable constraints:**

- `naive_error > unbiased_error`
- `abs(unbiased_estimate - true_rate) < 0.2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
