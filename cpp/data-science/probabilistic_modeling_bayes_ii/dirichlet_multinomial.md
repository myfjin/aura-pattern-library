# dirichlet multinomial

**Language:** C++ · **Sphere:** data-science · **Category:** Probabilistic Modeling

**Signature:** `(x: float) → float`

## What it does

Dirichlet-multinomial posterior and log-likelihood — C++17 port.
Includes Stirling log-gamma approximation matching the Python oracle.

## Guarantee

When it runs, dirichlet multinomial guarantees abs(sum(weak_post) - 1.0) < 0.01; abs(sum(strong_post) - 1.0) < 0.01; abs(weak_post[i] - empirical_freqs[i]) < 0.15 (proven by run on the PY original).

**Checkable constraints:**

- `abs(sum(weak_post) - 1.0) < 0.01`
- `abs(sum(strong_post) - 1.0) < 0.01`
- `abs(weak_post[i] - empirical_freqs[i]) < 0.15`
- `strong_post[0] > weak_post[0] - 0.05`
- `weak_post == weak_post2`
- `not math.isnan(ll) and (not math.isinf(ll))`
- `not math.isnan(ll_informed)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
