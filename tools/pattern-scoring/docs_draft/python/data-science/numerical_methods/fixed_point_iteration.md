# Fixed-Point Iteration

**File:** `python/data-science/numerical_methods/fixed_point_iteration.py`
**Sphere:** Data Science — Numerical Methods

---

## What it solves

**Find x where g(x) = x.** Equivalently solves f(x) = 0 by reformulating as g(x) = x where g(x) = x − f(x). Convergence speed depends on |g'(x*)|; contraction mapping guarantees.

**When to use:** Solving equations where the function can be rearranged into fixed-point form.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `g` | Callable, fixed-point function | |
| `x0` | float, initial guess | |
| `tol` | float > 0, convergence tolerance | |

---

## How inputs shape the output

- **Fixed point of g(x) = cos(x) is x ≈ 0.7391** — recovered to within 0.001.
- **|g(x) − x| < 1e-7** — converged.
- **Linear convergence** rate depends on |g'(x*)|.

---

## Worked example (real run)

```
$ python3 python/data-science/numerical_methods/fixed_point_iteration.py
PASS
```

**Reading the output:** fixed point of cos(x) found at x ≈ 0.7391 from initial guess 0.5.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| |g'(x*)| ≥ 1 | may diverge | not a contraction mapping |
| max_iter reached | returns last value | may not have converged |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20