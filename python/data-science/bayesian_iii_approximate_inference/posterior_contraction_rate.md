# posterior contraction rate

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Approximate Inference

**Signature:** `(data: ?, prior_mu: ?, prior_sigma_sq: ?) → float`

## What it does

Posterior contraction rate: posterior sd shrinks ~1/√n as sample size increases.

Bayesian consistency: posterior concentrates on true parameter. Core claim: posterior sd
shrinks ~1/√n as n grows (assert the ratio across two sample sizes).

## Guarantee

When it runs, posterior contraction rate guarantees abs(contraction_ratio - expected_ratio) < 0.1; posterior_sd2 < posterior_sd1 (proven by run).

**Checkable constraints:**

- `abs(contraction_ratio - expected_ratio) < 0.1`
- `posterior_sd2 < posterior_sd1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
