# rhat convergence diagnostic

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Approximate Inference

**Signature:** `(chains: List[List[float]]) → float`

## What it does

R-hat convergence diagnostic: measures MCMC chain mixing. R̂ ≈ 1 for well-mixed chains,
>1.1 for stuck chains. Core claim: R̂ ≈ 1 for well-mixed AND >1.1 for stuck (BOTH directions).

## Guarantee

When it runs, rhat convergence diagnostic guarantees rhat_good < rhat_bad; rhat_bad > 1.1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `rhat_good < rhat_bad`
- `rhat_bad > 1.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
