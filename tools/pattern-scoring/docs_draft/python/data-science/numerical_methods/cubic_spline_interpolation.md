# Natural Cubic Spline Interpolation

**File:** `python/data-science/numerical_methods/cubic_spline_interpolation.py`
**Sphere:** Data Science — Numerical Methods

---

## What it solves

**Piecewise cubic interpolation with C² continuity.** Solves tridiagonal system for interior knot second derivatives; uses them to define cubic polynomials on each segment. Natural boundary condition: second derivative = 0 at endpoints.

**When to use:** Smooth interpolation of data points where you need continuous first and second derivatives.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `x_data`, `y_data` | list, known points | |
| `x_eval` | list, points to interpolate at | |

---

## How inputs shape the output

- **Interpolation error < 0.05** on sin(x) with 5 knots.
- **C² continuity** at interior knots.
- **Natural boundary** (zero second derivative at endpoints).

---

## Worked example (real run)

```
$ python3 python/data-science/numerical_methods/cubic_spline_interpolation.py
PASS
```

**Reading the output:** sin(x) sampled at 5 points on [0, π] is interpolated at 3 interior points with error < 0.05.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| singular tridiagonal matrix | ValueError | duplicate x values |
| x_eval outside data range | extrapolation | no natural boundary outside |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20