# evidence ranks true model

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Modeling & Selection

**Signature:** `(data: List[float]) → float`

## What it does

Model evidence (via BIC) ranks the true generative model above the alternative.

A FAIR comparison scores each model by BIC = −2·log L̂ + k·log n, evaluated at each model's
own MLE with its own parameter count (Gaussian k=2, Exponential k=1). Lower BIC = better.
On Gaussian data the Gaussian model earns the lower BIC. Core claim: BIC_true < BIC_alt.

## Guarantee

When it runs, evidence ranks true model guarantees bic_true < bic_alt; bic_alt - bic_true > 10.0 (proven by run).

**Checkable constraints:**

- `bic_true < bic_alt`
- `bic_alt - bic_true > 10.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
