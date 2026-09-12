# RK4 ODE Solver

**File:** `python/data-science/numerical_methods/rk4_ode_solver.py`
**Sphere:** Data Science — Numerical Methods

---

## What it solves

**Fourth-order Runge-Kutta: standard explicit ODE integrator.** Solves dy/dt = f(t, y) using 4-stage RK scheme with O(h⁵) local error. High accuracy on smooth systems.

**When to use:** Solving ordinary differential equations where high accuracy is needed.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `f` | Callable, ODE right-hand side | |
| `t0`, `y0` | float, initial condition | |
| `t_final` | float, integration endpoint | |
| `num_steps` | int, number of steps | |

---

## How inputs shape the output

- **Planted ODE dy/dt = −2y, y(0) = 1** solved to within 1e-5 of exact e⁻².
- **O(h⁴) global error** — verified in euler_vs_rk4_error_order.

---

## Worked example (real run)

```
$ python3 python/data-science/numerical_methods/rk4_ode_solver.py
PASS
```

**Reading the output:** y(1) = e⁻² ≈ 0.1353 computed to within 1e-5 with 100 steps.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| stiff ODE | may need very small steps | use implicit method |
| num_steps = 0 | no integration | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20