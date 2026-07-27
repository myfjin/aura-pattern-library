# simulated annealing

**Language:** C++ · **Sphere:** data-science · **Category:** Optimization & Distances

**Signature:** `(x_init: float, y_init: float, func: ?, bounds: Tuple[float, float], initial_temp: float, cooling_rate: float, max_iters: int) → Tuple[float, float, float]`

## What it does

Simulated Annealing.
C++17 self-contained implementation.

## Guarantee

When it runs, simulated annealing guarantees best_value < tolerance; distance_from_optimum < 2.0 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `best_value < tolerance`
- `distance_from_optimum < 2.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `simulated_annealing(x_init: float, y_init: float, func, bounds: Tuple[float, float], initial_temp: float = 10.0, cooling_rate: float = 0.95, max_iters: int = 5000) -> Tuple[float, float, float]`
**Valid input:** `func(x,y) -> float`; `bounds[0] < bounds[1]`; `initial_temp > 0`; `cooling_rate` in `(0,1)`.
**Core:** 2D simulated annealing. Proposes Gaussian neighbors with scale proportional to temperature, accepts worse moves via the Metropolis criterion, and cools geometrically. Bounds are clamped.
**Assert:** On 2D Rastrigin centered at `(3,3)` with `random.seed(42)`, finds `best_value < 2.0` and final point within distance `2.0` of `(3,3)`.
**⚠️ Defect:** No lower bound on proposed move scale: as temperature drops, `scale = 0.5 * temperature` can become extremely small (`< 1e-8`), so the final iterations make no meaningful progress. Combined with the geometric cooling, the algorithm can freeze before truly converging, and the tolerance is loose enough to accept a wide neighborhood around the optimum.

---

*5S · Batch 1 detail docs · 2026-07-20*

---
*△ AURA Pattern Library — © Reality Optimizer*
