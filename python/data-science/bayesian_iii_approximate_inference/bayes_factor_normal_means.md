# bayes factor normal means

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Approximate Inference

**Signature:** `(data: ?, prior_var_h1: ?) → float`

## What it does

Bayes factor for comparing two normal means: H1 (θ ≠ 0) vs H0 (θ = 0).

BF = p(data|H1) / p(data|H0). Core claim: BF>1 when H1 is true AND BF<1 when H0 is true
(BOTH directions asserted; the two-sided test).

## Guarantee

When it runs, bayes factor normal means guarantees bf_h1 > 1.0; bf_h0 < 1.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `bf_h1 > 1.0`
- `bf_h0 < 1.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — positive, xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
