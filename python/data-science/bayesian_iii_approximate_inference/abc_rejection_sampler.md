# abc rejection sampler

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Approximate Inference

## What it does

Approximate Bayesian Computation (ABC): rejection sampling for intractable likelihoods.

Sample from prior, simulate data, accept if simulated ≈ observed (within ε).
Core claim: posterior mean recovers the planted parameter; acceptance rate shrinks as ε tightens.

## Guarantee

When it runs, abc rejection sampler guarantees abs(mean_loose - theta_true) < 1.0; abs(mean_tight - theta_true) < 1.0; accept_loose > accept_tight (proven by run).

**Checkable constraints:**

- `abs(mean_loose - theta_true) < 1.0`
- `abs(mean_tight - theta_true) < 1.0`
- `accept_loose > accept_tight`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
