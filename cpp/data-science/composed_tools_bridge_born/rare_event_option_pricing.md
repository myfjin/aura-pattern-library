# rare event option pricing

**Language:** C++ · **Sphere:** data-science · **Category:** Composed Tools

**Signature:** `(x: float) → float`

## What it does

rare_event_option_pricing.cpp — Deep OTM option: naive MC vs importance sampling.

## Guarantee

When it runs, rare event option pricing guarantees err_is < 0.1; err_naive > 3 * err_is; se / truth < 0.1 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `err_is < 0.1`
- `err_naive > 3 * err_is`
- `se / truth < 0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
