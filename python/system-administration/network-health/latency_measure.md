# latency measure

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 8 · Network reachability & health

**Signature:** `(host: str, port: int, timeout_sec: float) → ?`

## What it does

latency_measure: measure round-trip latency between two endpoints on localhost.
Failure simulated: measure latency from client to server socket; verify latency ≥ 0 and ≤ reasonable bound.
Recovery asserted: latency can be measured; close server and latency becomes unmeasurable (returns None).

## Guarantee

When it runs, latency measure guarantees latency_up is not None; latency_up >= 0; latency_up < 100 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `latency_up is not None`
- `latency_up >= 0`
- `latency_up < 100`
- `latency_down is None`
- `latency_up is not None and latency_down is None`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
