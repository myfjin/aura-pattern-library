# Richardson Extrapolation

**File:** `python/data-science/numerical_methods/richardson_extrapolation.py`
**Sphere:** Data Science — Numerical Methods

---

## What it solves

**Boost convergence order via linear combination.** If F(h) ≈ L + C·h^p + O(h^(2p)), then (2^p·F(h/2) − F(h))/(2^p − 1) ≈ L + O(h^(2p)). The C·h^p term cancels. Raises O(h^p) error to O(h^(2p)) without changing the method.

**When to use:** Improving accuracy of numerical methods without changing the underlying algorithm.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `F` | Callable, method returning estimate at step h | |
| `h` | float, step size | |
| `p` | int, error order of the method | |

---

## How inputs shape the output

- **Error after extrapolation < error before** — improvement guaranteed.
- **Error after extrapolation < 1e-10** — O(h²) midpoint rule raised to O(h⁴).
- **The factor is 2^p, not p** — using p leaves residual O(h^p) error.

---

## Worked example (real run)

```
$ python3 python/data-science/numerical_methods/richardson_extrapolation.py
PASS
```

**Reading the output:** midpoint rule (O(h²)) on ∫₀¹ x³ dx = 0.25 is extrapolated to O(h⁴) accuracy (< 1e-10).

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| wrong p value | error not cancelled | needs correct error order |
| h too large | extrapolation may not help | asymptotic regime not reached |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20