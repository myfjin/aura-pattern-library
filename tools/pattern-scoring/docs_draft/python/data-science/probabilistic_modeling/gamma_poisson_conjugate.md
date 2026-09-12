# Gamma-Poisson Conjugate Prior

**File:** `python/data-science/probabilistic_modeling/gamma_poisson_conjugate.py`
**Sphere:** Data Science — Probabilistic Modeling

---

## What it solves

**Gamma prior on Poisson rate parameter — closed-form posterior.** Prior Gamma(α, β); observe Poisson counts; posterior is Gamma(α + Σcount, β + n). Sequential updates ≡ batch update (conjugacy). Posterior mean is between prior mean and empirical mean.

**When to use:** Rate estimation, count data modeling, reliability/failure analysis.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `counts` | List[int], Poisson observations | |
| `alpha_prior`, `beta_prior` | float > 0, Gamma prior params | |

---

## How inputs shape the output

- **Posterior parameters match closed form** — α + Σcount, β + n.
- **Posterior mean between prior and empirical** — convex combination property.
- **Posterior variance shrinks from prior** — data reduces uncertainty.
- **Sequential updates match batch** — exchangeability.

---

## Worked example (real run)

```
$ python3 python/data-science/probabilistic_modeling/gamma_poisson_conjugate.py
PASS
```

**Reading the output:** with true λ=3.5 and 50 samples, weak prior Gamma(1,1) gives posterior near empirical. Strong prior Gamma(2,1) pulls toward prior mean 2. Sequential updates match batch.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| empty counts | posterior = prior | correct |
| all counts zero | posterior shifts toward prior | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20