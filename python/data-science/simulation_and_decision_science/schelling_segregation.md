# schelling segregation

**Language:** Python · **Sphere:** data-science · **Category:** Simulation & Decision Science

**Signature:** `() → None`

## What it does

Schelling Segregation: mild preference produces high global segregation.

Agents prefer neighbors of same type with threshold >= 30%.
Simulation shows high global segregation emerges from mild individual preference.
Segregation measured before/after as ratio of same-type neighbors.

## Guarantee

When it runs, schelling segregation guarantees final_seg > 0.5; final_seg >= initial_seg (weak-grade: directional, proven by run).

**Checkable constraints:**

- `final_seg > 0.5`
- `final_seg >= initial_seg`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
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
