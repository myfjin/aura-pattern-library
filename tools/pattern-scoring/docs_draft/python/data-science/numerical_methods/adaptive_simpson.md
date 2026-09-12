# Adaptive Simpson's Rule

**File:** `python/data-science/numerical_methods/adaptive_simpson.py`
**Sphere:** Data Science — Numerical Methods

---

## What it solves

**Automatic step refinement via error estimation for numerical integration.** Compares Simpson's estimate on [a, b] with two estimates on [a, c] and [c, b]. If error is acceptable, return result; else recurse. O(h⁴) accuracy with far fewer function evals than fixed-step methods.

**When to use:** Numerical integration where the integrand varies in smoothness across the domain.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `f` | Callable, integrand function | |
| `a`, `b` | float, integration bounds | |
| `tol` | float > 0, error tolerance | |

---

## How inputs shape the output

- **Planted integral ∫₀^π sin(x) dx = 2 recovered** to within 1e-7.
- **Recursive refinement** where error estimate exceeds tolerance.
- **Depth limit of 50** prevents infinite recursion.

---

## Worked example (real run)

```
$ python3 python/data-science/numerical_methods/adaptive_simpson.py
PASS
```

**Reading the output:** ∫₀^π sin(x) dx = 2.0 computed to within 1e-7.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| very flat function | single evaluation suffices | correct |
| highly oscillatory | many recursive splits | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20