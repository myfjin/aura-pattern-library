# Secant Method

**File:** `python/data-science/numerical_methods/secant_method.py`
**Sphere:** Data Science — Numerical Methods

---

## What it solves

**Newton's speed without derivatives.** Uses finite-difference slope from two prior points to approximate f'(x). Converges superlinearly (order ≈ 1.618) without explicit derivative.

**When to use:** Root-finding when the derivative is expensive or unavailable.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `f` | Callable, function to find root of | |
| `x0`, `x1` | float, two initial guesses | |
| `tol` | float > 0, convergence tolerance | |

---

## How inputs shape the output

- **Root of x³ − 2 = 0 found at ∛2 ≈ 1.2599** — within 1e-4.
- **f(root) < 1e-8** — residual near zero.
- **Superlinear convergence** (order ≈ 1.618).

---

## Worked example (real run)

```
$ python3 python/data-science/numerical_methods/secant_method.py
PASS
```

**Reading the output:** root of x³ − 2 = 0 found at x ≈ 1.2599 from initial guesses 1.0 and 1.5.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| f(x0) = f(x1) | division by near-zero | returns last value |
| max_iter reached | returns last value | may not have converged |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20