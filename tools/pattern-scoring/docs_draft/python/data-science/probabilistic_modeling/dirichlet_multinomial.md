# Dirichlet-Multinomial Conjugate

**File:** `python/data-science/probabilistic_modeling/dirichlet_multinomial.py`
**Sphere:** Data Science — Probabilistic Modeling

---

## What it solves

**Conjugate posterior over category probabilities.** Dirichlet prior Dir(α) on the probability simplex; observe multinomial counts; posterior is Dir(α + counts). Sequential updates ≡ batch update (exchangeability). MAP estimate: (α_i + count_i − 1) / (sum(α) + sum(counts) − K).

**When to use:** Topic modeling, urn problems, belief updating on discrete distributions.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `counts` | List[int], observed counts per category | |
| `alpha_prior` | List[float], Dirichlet prior parameters | |

---

## How inputs shape the output

- **Posterior probabilities sum to 1** — the simplex constraint.
- **Weak prior posterior matches empirical frequencies** — barely influential.
- **Strong prior skews posterior toward its mode** — the defining property.

---

## Worked example (real run)

```
$ python3 python/data-science/probabilistic_modeling/dirichlet_multinomial.py
PASS
```

**Reading the output:** with true probs [0.5, 0.3, 0.2] and 100 samples, weak prior (α=[1,1,1]) gives posterior near empirical. Strong prior (α=[20,5,1]) skews toward category 0.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| all counts zero | posterior = prior | correct |
| alpha_i < 1 for all i | MAP may be 0 | mode at boundary |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20