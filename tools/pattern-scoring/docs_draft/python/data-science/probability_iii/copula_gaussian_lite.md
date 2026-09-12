# Gaussian Copula

**File:** `python/data-science/probability_iii/copula_gaussian_lite.py`
**Sphere:** Data Science — Probability III

---

## What it solves

**Model dependence structure separately from marginals.** A copula C(u,v) = P(U ≤ u, V ≤ v) where U,V ~ Uniform. Independence is C = uv. The Gaussian copula uses the multivariate normal CDF to model correlation between the uniform marginals. Rank correlation is preserved under the copula transform.

**When to use:** Modeling dependencies between variables when their marginal distributions are not normal — finance, risk modeling, any "correlation without normality."

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `rho` | float in [-1, 1], correlation | |
| `n` | int > 0, sample size | |

---

## How inputs shape the output

- **Samples from Gaussian copula** via bivariate normal with correlation rho, transformed to uniform via CDF.
- **Spearman rank correlation** of the uniform samples is close to the true rho.
- **Dependence structure is preserved** regardless of marginal distributions.

---

## Worked example (real run)

```
$ python3 python/data-science/probability_iii/copula_gaussian_lite.py
PASS
```

**Reading the output:** with true rho=0.7, the estimated rank correlation from 500 copula samples is within 0.2 of the true value.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| rho = 0 | independent uniforms | correct |
| rho = ±1 | perfect dependence | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20