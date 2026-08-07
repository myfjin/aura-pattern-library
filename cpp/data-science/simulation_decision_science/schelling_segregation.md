# schelling segregation

**Language:** C++ · **Oracle sphere:** data-science (this file is the C++ twin) · **Category:** Simulation & Decision Science

## What it does

Schelling Segregation: mild preference produces high global segregation.
C++17 self-contained implementation.

## Guarantee

When it runs, schelling segregation guarantees final_seg > 0.5; final_seg >= initial_seg (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `final_seg > 0.5`
- `final_seg >= initial_seg`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def schelling_segregation() -> None:`, `def get_neighbors(r: int, c: int) -> list[int]:`, `def is_satisfied(r: int, c: int) -> bool:`, `def measure_segregation() -> float:`
**Valid input:** `r`, `c` are valid indices in the 10×10 grid.
**Core:** Schelling model of segregation on a 10×10 grid with two agent types. Agents are satisfied if at least 30% of their neighbors are the same type. Unsatisfied agents swap with random agents of the opposite type; global segregation is measured as the fraction of neighbor pairs that are same-type.
**Assert:** Initial segregation is recorded; final segregation > 0.5 and ≥ initial segregation after up to 100 iterations, showing mild individual preference produces high global segregation.
**⚠️ Defect:** The swap logic looks for "a random cell with a different type" and only attempts 20 random cells before giving up, so an unsatisfied agent may remain in place. The simulation moves only one random unsatisfied agent per iteration, which is slow and not the standard Schelling update. No guarantee that the final state has no unsatisfied agents.

---
*△ AURA Pattern Library — © Reality Optimizer*
