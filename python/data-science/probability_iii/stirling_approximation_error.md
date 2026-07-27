# stirling approximation error

**Language:** Python · **Sphere:** data-science · **Category:** Probability III

**Signature:** `(n: int) → float`

## What it does

Stirling's approximation: log(n!) ≈ n·log(n) - n + 0.5·log(2πn).

Core claim: relative error shrinks as n grows; error measured vs exact factorial.

## Guarantee

When it runs, stirling approximation error guarantees errors[0][1] > errors[1][1]; errors[1][1] > errors[2][1]; errors[2][1] < 0.01 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `errors[0][1] > errors[1][1]`
- `errors[1][1] > errors[2][1]`
- `errors[2][1] < 0.01`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
