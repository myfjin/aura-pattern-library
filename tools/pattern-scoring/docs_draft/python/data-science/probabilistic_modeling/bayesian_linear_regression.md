# Bayesian Linear Regression

**File:** `python/data-science/probabilistic_modeling/bayesian_linear_regression.py`
**Sphere:** Data Science — Probabilistic Modeling

---

## What it solves

**Bayesian linear regression with conjugate normal prior, known noise, closed-form posterior.** Prior N(μ₀, Σ₀); likelihood N(y | Xβ, σ²I); posterior is N(μ_post, Σ_post) with closed-form updates. Posterior mean is between prior and OLS; variance shrinks with data.

**When to use:** Interpretable regression with uncertainty, small data, informative priors.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `X`, `y` | List[float], paired observations | |
| `mu0` | float, prior mean | |
| `sigma0_sq` | float > 0, prior variance | |
| `sigma_sq` | float > 0, noise variance | |

---

## How inputs shape the output

- **Weak prior posterior mean is close to OLS** — barely influential.
- **Strong prior pulls posterior toward prior mean** — the defining property.
- **Posterior variance shrinks from prior** — data reduces uncertainty.

---

## Worked example (real run)

```
$ python3 python/data-science/probabilistic_modeling/bayesian_linear_regression.py
PASS
```

**Reading the output:** with true β=2, weak prior (μ₀=0, σ₀²=100) gives posterior near OLS. Strong prior (μ₀=1.5, σ₀²=0.1) pulls toward 1.5. Both posteriors shrink variance.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| empty data | returns prior | correct |
| zero variance in X | OLS denominator = 0 | clamped to 0 |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20