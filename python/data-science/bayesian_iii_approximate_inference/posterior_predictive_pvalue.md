# posterior predictive pvalue

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Approximate Inference

**Signature:** `(observed_stat: float, posterior_samples: List[float]) → float`

## What it does

Posterior predictive p-value: compare observed data to posterior predictive distribution.

ppp ≈ 0.5 for the correct model; extreme (<0.05 or >0.95) for misspecified model.
Core claim: ppp ≈ 0.5 for correct model; extreme for misspecified one.

## Guarantee

When it runs, posterior predictive pvalue guarantees 0.2 < ppp_correct < 0.8; ppp_wrong < 0.1 or ppp_wrong > 0.9 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `0.2 < ppp_correct < 0.8`
- `ppp_wrong < 0.1 or ppp_wrong > 0.9`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
