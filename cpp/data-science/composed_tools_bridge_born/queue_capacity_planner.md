# queue capacity planner

**Language:** C++ · **Oracle sphere:** data-science (this file is the C++ twin) · **Category:** Composed Tools

## What it does

queue_capacity_planner.cpp — Discrete-event queue simulation + capacity planning.
Matches the Python oracle: Poisson arrivals, exponential service, FIFO workers.

## Guarantee

When it runs, queue capacity planner guarantees served == len(arrivals); rel_err < 0.05; at['mean_wait'] <= sla (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `served == len(arrivals)`
- `rel_err < 0.05`
- `at['mean_wait'] <= sla`
- `below['mean_wait'] > sla`
- `all((curve[a] >= curve[b] - 1e-09 for a, b in zip(ks, ks[1:])))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
