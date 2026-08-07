# secant method

**Language:** C++ · **Oracle sphere:** data-science (this file is the C++ twin) · **Category:** Numerical Methods

## What it does

Secant method: Newton's speed without derivatives.
C++17 self-contained implementation.

## Guarantee

When it runs, secant method guarantees abs(root - 1.2599) < 0.0001; abs(f_planted(root)) < 1e-08 (proven by run on the PY original).

**Checkable constraints:**

- `abs(root - 1.2599) < 0.0001`
- `abs(f_planted(root)) < 1e-08`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
