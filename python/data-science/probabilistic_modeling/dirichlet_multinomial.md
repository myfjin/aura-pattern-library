# dirichlet multinomial

**Language:** Python · **Sphere:** data-science · **Category:** Probabilistic Modeling

**Signature:** `(x: float) → float`

## What it does

Dirichlet-multinomial: conjugate posterior over category probabilities.

Core idea: Dirichlet prior Dir(α) on probability simplex; observe multinomial counts;
posterior is Dir(α + counts). Sequential updates ≡ batch update (exchangeability).

When to use: topic modeling, urn problems, belief updating on discrete distributions.

## Guarantee

When it runs, dirichlet multinomial guarantees abs(sum(weak_post) - 1.0) < 0.01; abs(sum(strong_post) - 1.0) < 0.01; abs(weak_post[i] - empirical_freqs[i]) < 0.15 (proven by run).

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
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
