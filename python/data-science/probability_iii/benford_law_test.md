# benford law test

**Language:** Python · **Sphere:** data-science · **Category:** Probability III

**Signature:** `(n: int) → List[float]`

## What it does

Benford's law: leading digit distribution in many real datasets.

P(digit d) = log₁₀(1 + 1/d) for d ∈ {1,...,9}. Multiplicative data follows;
uniform data violates it. Chi-square test.

## Guarantee

When it runs, benford law test guarantees chi_mult < chi_unif (weak-grade: directional, proven by run).

**Checkable constraints:**

- `chi_mult < chi_unif`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
