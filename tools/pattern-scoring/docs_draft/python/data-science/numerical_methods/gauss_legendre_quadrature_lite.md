# Gauss-Legendre Quadrature (Lite)

**File:** `python/data-science/numerical_methods/gauss_legendre_quadrature_lite.py`
**Sphere:** Data Science — Numerical Methods

---

## What it solves

**Optimal node placement for polynomial integration.** Hardcoded nodes and weights for n=4 (integrates degree ≤7 polynomials exactly). Fewer function evals than trapezoid for smooth functions.

**When to use:** Numerical integration where the integrand is smooth and you want high accuracy with few evaluations.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `f` | Callable, integrand function | |
| `a`, `b` | float, integration bounds | |

---

## How inputs shape the output

- **∫₀¹ x² dx = 1/3** computed to within 1e-10 (exact for degree ≤7).
- **∫₀^π sin(x) dx = 2** computed to within 1e-4.
- **4 function evaluations** for high accuracy.

---

## Worked example (real run)

```
$ python3 python/data-science/numerical_methods/gauss_legendre_quadrature_lite.py
PASS
```

**Reading the output:** ∫₀¹ x² dx = 1/3 exactly (machine epsilon). ∫₀^π sin(x) dx = 2.0 within 1e-4.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| non-smooth integrand | accuracy degrades | Gauss-Legendre assumes smoothness |
| a = b | returns 0 | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20