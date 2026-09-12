# Forward Euler vs RK4: Convergence Order

**File:** `python/data-science/numerical_methods/euler_vs_rk4_error_order.py`
**Sphere:** Data Science — Numerical Methods

---

## What it solves

**Measure convergence order difference between Forward Euler and RK4.** Solves the same ODE with both methods at successive step sizes. Euler is O(h), RK4 is O(h⁴). Measured convergence rates match theory.

**When to use:** Understanding numerical ODE solver accuracy and choosing step size.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `f` | Callable, ODE right-hand side | |
| `t0`, `y0` | float, initial condition | |
| `t_final` | float, integration endpoint | |
| `h` | float, step size | |

---

## How inputs shape the output

- **Euler error ratio ≈ 2** when halving step (O(h) convergence).
- **RK4 error ratio ≈ 16** when halving step (O(h⁴) convergence).
- **Planted ODE dy/dt = −y, y(0) = 1** with exact solution e⁻¹.

---

## Worked example (real run)

```
$ python3 python/data-science/numerical_methods/euler_vs_rk4_error_order.py
PASS
```

**Reading the output:** Euler error ratio ~2, RK4 error ratio ~16 — matching O(h) and O(h⁴) theory.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| very large step | both methods inaccurate | correct |
| stiff ODE | both may diverge | needs implicit method |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20