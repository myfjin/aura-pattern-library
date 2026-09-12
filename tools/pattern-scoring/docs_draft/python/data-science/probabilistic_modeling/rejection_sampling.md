# Rejection Sampling

**File:** `python/data-science/probabilistic_modeling/rejection_sampling.py`
**Sphere:** Data Science — Probabilistic Modeling

---

## What it solves

**Sample from a complex density under an envelope.** Sample from a proposal distribution, accept with probability p(x) / (M · q(x)). Empirical moments match numeric-integration moments. Acceptance rate ≈ theoretical 1/M.

**When to use:** Non-standard distributions, Bayesian posterior sampling, missing primitives.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `target_density` | function, unnormalized density | |
| `proposal_sample` | function, samples from proposal | |
| `proposal_density` | function, proposal PDF | |
| `M` | float, envelope constant | p(x) ≤ M·q(x) |

---

## How inputs shape the output

- **Empirical mean matches integrated mean** within 0.5.
- **Empirical variance matches integrated variance** within 0.5.
- **All samples are in proposal support** — valid range.

---

## Worked example (real run)

```
$ python3 python/data-science/probabilistic_modeling/rejection_sampling.py
PASS
```

**Reading the output:** from a bimodal target density with uniform proposal on [-5,5], 1000 samples have mean and variance matching numeric integration.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| M too small | acceptance ratio > 1 | invalid envelope |
| M too large | very low acceptance rate | inefficient |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20