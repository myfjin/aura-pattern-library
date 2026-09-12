# Hybrid Bisection-Newton Root-Finding

**File:** `python/data-science/numerical_methods/bisection_newton_hybrid.py`
**Sphere:** Data Science — Numerical Methods

---

## What it solves

**Combine bisection's guaranteed convergence with Newton's speed.** Uses Newton when safe; reverts to bisection if Newton drifts outside the bracket. Planted root recovered accurately even when Newton would diverge.

**When to use:** Root-finding where you want Newton's speed but need bisection's robustness.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `f` | Callable, function to find root of | |
| `df` | Callable, derivative of f | |
| `a`, `b` | float, bracket with f(a)·f(b) < 0 | |
| `tol` | float > 0, convergence tolerance | |

---

## How inputs shape the output

- **Root recovered to within 1e-6** of true value (3.0).
- **f(root) < 1e-8** — residual near zero.
- **Newton used when within bracket and step is small**; bisection otherwise.

---

## Worked example (real run)

```
$ python3 python/data-science/numerical_methods/bisection_newton_hybrid.py
PASS
```

**Reading the output:** root of x² − x − 6 = 0 in [1, 5] found at x ≈ 3.0.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| f(a)·f(b) > 0 | ValueError | no sign change in bracket |
| df(x) ≈ 0 | falls back to bisection | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20