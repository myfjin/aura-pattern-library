# sequential probability ratio

**Language:** C++ · **Sphere:** data-science · **Category:** Causal Inference & Experimentation

**Signature:** `(data: list, p0: float, p1: float, alpha: float, beta: float) → Tuple[str, int]`

## What it does

Sequential Probability Ratio Test (SPRT).
C++17 self-contained implementation.

## Guarantee

When it runs, sequential probability ratio guarantees avg_sprt > 0; avg_sprt < fixed_n_typical; h1_rate_fixed > 0.7 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `avg_sprt > 0`
- `avg_sprt < fixed_n_typical`
- `h1_rate_fixed > 0.7`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
