# Romberg Integration

**File:** `python/data-science/numerical_methods/romberg_integration.py`
**Sphere:** Data Science — Numerical Methods

---

## What it solves

**Richardson extrapolation on the trapezoid rule.** Generates a table of progressively refined trapezoid estimates, then extrapolates to higher-order accuracy. O(h⁴) error for smooth integrands vs O(h²) from bare trapezoid.

**When to use:** High-accuracy numerical integration with automatic order improvement.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `f` | Callable, integrand function | |
| `a`, `b` | float, integration bounds | |
| `n` | int, number of Romberg table rows | |

---

## How inputs shape the output

- **∫₀^π sin(x) dx = 2** computed to within 1e-6 with n=5.
- **Richardson extrapolation uses 4^j factor** (trapezoid is O(h²), so p=2 → 2^p = 4).

---

## Worked example (real run)

```
$ python3 python/data-science/numerical_methods/romberg_integration.py
PASS
```

**Reading the output:** ∫₀^π sin(x) dx = 2.0 computed to within 1e-6 with 5 Romberg rows.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| n = 1 | bare trapezoid | no extrapolation |
| non-smooth integrand | accuracy degrades | Romberg assumes smoothness |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20