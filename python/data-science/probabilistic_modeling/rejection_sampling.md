# rejection sampling

**Language:** Python · **Sphere:** data-science · **Category:** Probabilistic Modeling

**Signature:** `(target_density: ?, proposal_sample: ?, proposal_density: ?, M: float, n_samples: int) → Tuple[List[float], float]`

## What it does

Rejection sampling: sample from complex density under an envelope.

Core idea: sample from proposal, accept with probability p(x) / (M * q(x)).
Empirical moments match numeric-integration moments; acceptance rate ≈ theoretical 1/M.

When to use: non-standard distributions, Bayesian posterior sampling, missing primitives.

## Guarantee

When it runs, rejection sampling guarantees 0 < acc_rate <= 1; abs(mean - mean_ref) < 0.5; abs(var - var_ref) < 0.5 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(samples) == 1000`
- `0 < acc_rate <= 1`
- `abs(mean - mean_ref) < 0.5`
- `abs(var - var_ref) < 0.5`
- `all((-5 <= x <= 5 for x in samples))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
