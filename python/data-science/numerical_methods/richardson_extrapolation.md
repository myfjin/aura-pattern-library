# richardson extrapolation

**Language:** Python · **Sphere:** data-science · **Category:** Numerical Methods

**Signature:** `(F: Callable[[float], float], h: float, p: int) → float`

## Guarantee

When it runs, richardson extrapolation guarantees error_after < error_before; error_after < 1e-10 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `error_after < error_before`
- `error_after < 1e-10`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
