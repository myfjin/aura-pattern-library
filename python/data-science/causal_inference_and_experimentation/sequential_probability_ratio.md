# sequential probability ratio

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference & Experimentation

**Signature:** `(data: list, p0: float, p1: float, alpha: float, beta: float) → Tuple[str, int]`

## What it does

Sequential Probability Ratio Test (SPRT).

A sequential test that stops early: accumulate log-likelihood ratio for H0 vs H1.
Stop when LR > threshold (accept H1) or LR < -threshold (accept H0).
Compared to fixed-n testing at the same error rates, SPRT uses fewer observations on average.
We verify that SPRT stops earlier than fixed-n while maintaining error rates.

## Guarantee

When it runs, sequential probability ratio guarantees avg_sprt > 0; avg_sprt < fixed_n_typical; h1_rate_fixed > 0.7 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `avg_sprt > 0`
- `avg_sprt < fixed_n_typical`
- `h1_rate_fixed > 0.7`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
