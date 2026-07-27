# evidence ranks true model

**Language:** C++ · **Sphere:** data-science · **Category:** Bayesian III — Modeling & Selection

**Signature:** `(data: List[float]) → float`

## What it does

Model evidence (via BIC) ranks the true generative model above the alternative.
C++17 self-contained port with full parity to Python oracle.

## Guarantee

When it runs, evidence ranks true model guarantees bic_true < bic_alt; bic_alt - bic_true > 10.0 (proven by run on the PY original).

**Checkable constraints:**

- `bic_true < bic_alt`
- `bic_alt - bic_true > 10.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
