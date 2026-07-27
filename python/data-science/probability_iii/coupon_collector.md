# coupon collector

**Language:** Python · **Sphere:** data-science · **Category:** Probability III

**Signature:** `(n: int) → float`

## What it does

Coupon collector: expected trials to collect all n distinct items.

E[T] = n·H_n where H_n = 1 + 1/2 + ... + 1/n is harmonic series. Core claim:
simulated mean matches n·H_n; planted n values.

## Guarantee

When it runs, coupon collector guarantees abs(expected_sim - expected_exact) < expected_exact * 0.1 (proven by run).

**Checkable constraints:**

- `abs(expected_sim - expected_exact) < expected_exact * 0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
