# learning rate schedules

**Language:** Python · **Sphere:** data-science · **Category:** Neural Networks From Scratch

**Signature:** `(x: float) → float`

## What it does

Learning rate schedules: constant vs step-decay vs cosine annealing.

Core idea: Train the same network three times with different LR schedules on the
same problem. Show that step-decay and cosine schedules reach comparable or better
final loss with more stable late-phase updates compared to constant high LR.

When to use: Hyperparameter tuning, convergence acceleration, avoiding divergence
in late training stages.

## Guarantee

When it runs, learning rate schedules guarantees const_loss < 0.1; step_loss < 0.1; cosine_loss < 0.1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `const_loss < 0.1`
- `step_loss < 0.1`
- `cosine_loss < 0.1`
- `step_late_var < 1e-06`
- `cosine_late_var < 1e-06`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `SimpleNet()` → `train(data, epochs, lr_schedule) → (final_loss, loss_history)`
**Valid input:** `data: List[Tuple[List[float], float]]` — 2D inputs, binary targets (x₀+x₁ > 0). `lr_schedule: Callable[[int, int], float]`.
**Core:** Compare three LR schedules on a 2→4→1 network: constant (0.05), step-decay (0.05→0.025→0.0125 at epochs 40/80), and cosine annealing (0.05→0.001). All converge to loss < 0.1. Schedules show lower late-phase variance.
**Assert:** On 40 synthetic samples, 120 epochs, all schedules reach final loss < 0.1. Step-decay and cosine late-phase variance < 1e-6.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
