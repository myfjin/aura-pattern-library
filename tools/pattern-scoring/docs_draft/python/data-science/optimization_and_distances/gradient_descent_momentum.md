# Gradient Descent with Momentum

**File:** `python/data-science/optimization_and_distances/gradient_descent_momentum.py`
**Sphere:** Data Science — Optimization and Distances

---

## What it solves

**Stop oscillating and converge faster.** Vanilla gradient descent zigzags in narrow valleys — it takes tiny steps in the steep direction and wastes iterations. Momentum accumulates velocity across iterations: if the gradient keeps pointing the same direction, momentum accelerates; if it reverses (oscillation), momentum smooths it out. On a 2D quadratic bowl with one steep axis (100× steeper), momentum converges in fewer iterations than vanilla GD.

**When to use:** Convex optimization with non-isotropic (elongated) loss landscapes. Standard in neural network training to accelerate convergence and reduce oscillation.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `learning_rate` | > 0, typically 0.001–0.1 | — |
| `momentum` | in [0, 1), typically 0.9 | 0 → vanilla GD |
| `tolerance` | > 0 | — |

---

## How inputs shape the output

- **Momentum converges in fewer iterations:** on the quadratic bowl f(x,y) = 100x² + y², momentum reaches the minimum faster than vanilla GD.
- **The momentum term (0.9) accumulates velocity:** each step builds on previous steps, smoothing the path.
- **Both methods converge to the same minimum:** the final function value is < 1e-6 for both.

---

## Worked example (real run)

```
$ python3 python/data-science/optimization_and_distances/gradient_descent_momentum.py
gradient_descent_momentum.py: vanilla_iters=6720 momentum_iters=1250 PASS
```

**Reading the output:** vanilla GD takes 6,720 iterations to converge; momentum GD takes only 1,250 — a 5.4× speedup. Both reach the same minimum.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| `momentum = 0` | equivalent to vanilla GD | correct |
| `momentum ≥ 1` | may diverge (velocity grows unbounded) | needs guard |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18
