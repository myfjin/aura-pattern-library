# elbo monotone vi

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Approximate Inference

**Signature:** `(data: ?, mu0: ?, s0: ?) → float`

## What it does

ELBO monotonicity in coordinate-ascent variational inference.

Coordinate-ascent VI (CAVI) maximizes the Evidence Lower Bound one factor at a time; each
update is a conditional maximizer, so the ELBO is NON-DECREASING every step, and it is
bounded above by the true log-evidence (ELBO = log p(data) − KL(q‖posterior) ≤ log p(data)).
For a conjugate Gaussian the bound is tight — CAVI converges to exactly the log-evidence.
Core claim: from a bad initialization the ELBO rises MONOTONICALLY, stays ≤ log-evidence,
and converges to it.

## Guarantee

When it runs, elbo monotone vi guarantees all((seq[i + 1] >= seq[i] - 1e-09 for i in range(len(seq) - 1))); all((e <= log_ev + 1e-06 for e in seq)); seq[-1] - seq[0] > 50.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `all((seq[i + 1] >= seq[i] - 1e-09 for i in range(len(seq) - 1)))`
- `all((e <= log_ev + 1e-06 for e in seq))`
- `seq[-1] - seq[0] > 50.0`
- `abs(seq[-1] - log_ev) < 0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
