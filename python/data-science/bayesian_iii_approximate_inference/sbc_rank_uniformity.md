# sbc rank uniformity

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Approximate Inference

**Signature:** `(n_sims: int, seed_offset: ?) → List[int]`

## What it does

Simulation Based Calibration (SBC): ranks should be uniform for a well-calibrated sampler.

Simulate parameter, simulate data, infer posterior, check where the true parameter ranks.
Core claim: ranks ~uniform (χ²) for correct sampler; flagged non-uniform for biased one.

## Guarantee

When it runs, sbc rank uniformity guarantees chi_sq_correct < 30; chi_sq_biased > chi_sq_correct (weak-grade: directional, proven by run).

**Checkable constraints:**

- `chi_sq_correct < 30`
- `chi_sq_biased > chi_sq_correct`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
