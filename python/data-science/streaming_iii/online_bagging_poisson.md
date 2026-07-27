# online bagging poisson

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(Xtr: ?, ytr: ?, thresholds: ?, n_models: int) → ?`

## What it does

Online bagging via Poisson(1) weighting (Oza & Russell, 2001).
Core idea: batch bagging resamples each point ~Binomial(n,1/n) times, which -> Poisson(1)
as n grows. So online bagging draws k ~ Poisson(1) per arriving point PER model and updates
that model with weight k -- no stored dataset, one pass, bounded memory. Oza's result: the
online ensemble converges to the batch-bagging ensemble. That convergence is the DEFINING,
universal property demonstrated here (identical predictions). On this noisy-label setup the
bagged ensemble is also a genuine aggregate that denoises a single stump -- so the
convergence is shown on a NON-degenerate ensemble, not two ways of writing one stump.
When: bag an ensemble over a stream in one pass with bounded memory.

## Guarantee

When it runs, online bagging poisson guarantees ob_agree >= 0.99; abs(online_acc - batch_acc) < 0.01; distinct >= 3 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `ob_agree >= 0.99`
- `abs(online_acc - batch_acc) < 0.01`
- `distinct >= 3`
- `bs_agree < 0.9`
- `online_acc > single_acc + 0.03`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
