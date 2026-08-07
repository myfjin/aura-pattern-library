# euler vs rk4 error order

**Language:** C++ · **Oracle sphere:** data-science (this file is the C++ twin) · **Category:** Numerical Methods

## What it does

Forward Euler vs RK4: measure convergence order difference.
C++17 self-contained port with full parity to Python oracle.

## Guarantee

When it runs, euler vs rk4 error order guarantees 1.5 < euler_ratio < 2.5; 10 < rk4_ratio < 20 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `1.5 < euler_ratio < 2.5`
- `10 < rk4_ratio < 20`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
