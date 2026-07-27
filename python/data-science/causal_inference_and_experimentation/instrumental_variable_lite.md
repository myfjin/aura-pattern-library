# instrumental variable lite

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference & Experimentation

**Signature:** `(x: List[float], y: List[float]) → float`

## What it does

Instrumental Variable (IV) Estimation.

Treatment T is endogenous: unobserved U affects both T and Y, creating bias.
An instrument Z affects Y only through T (exogeneity), and Z is independent of U.
IV estimate = Cov(Y, Z) / Cov(T, Z) (Wald estimator for binary Z, one endogenous T).
We plant endogeneity and an valid instrument; IV recovers the true effect.

## Guarantee

When it runs, instrumental variable lite guarantees bias_iv < bias_naive; bias_iv < 2.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `bias_iv < bias_naive`
- `bias_iv < 2.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
