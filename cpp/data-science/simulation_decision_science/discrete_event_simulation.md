# discrete event simulation

**Language:** C++ · **Sphere:** data-science · **Category:** Simulation & Decision Science

**Signature:** `() → None`

## What it does

Discrete Event Simulation (M/M/1 service desk) — C++17 port.
Event-driven simulation with conservation: arrivals == served + still-in-system.

## Guarantee

When it runs, discrete event simulation guarantees abs(unaccounted) <= 1; total_arrivals > 50; total_served > 50 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `abs(unaccounted) <= 1`
- `total_arrivals > 50`
- `total_served > 50`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def discrete_event_simulation() -> None:`
**Valid input:** None (function is self-contained with hardcoded parameters).
**Core:** Event-driven simulation of a single-server queue using a priority queue (heapq). Models Poisson arrivals and exponential service times, tracking arrivals, departures, queue length, server busy state, and total waiting time. Verifies conservation: total arrivals ≈ served + still in system.
**Assert:** Over `sim_time = 100` with arrival rate `0.9` and service rate `1.0`, more than 50 customers arrive and are served, and conservation holds within one customer.
**⚠️ Defect:** The simulation logic is hardcoded inside the function with no tunable parameters, so it cannot be reused for other arrival/service rates or queue disciplines. The `server_busy` flag can become inconsistent because service-end events set it to `False` before starting the next customer, which could briefly leave the flag wrong if multiple events share the same timestamp.

---
*△ AURA Pattern Library — © Reality Optimizer*
