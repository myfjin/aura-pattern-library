# failover switch

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 8 · Network reachability & health

**Signature:** `(host: str, port: int, timeout_sec: float) → ?`

## What it does

failover_switch: when primary endpoint fails, switch to secondary; assert the switch happens.
Failure simulated: primary server fails; failover_switch should detect and return secondary endpoint.
Recovery asserted: primary is marked failed; secondary is chosen; switch is verifiable.

## Guarantee

When it runs, failover switch guarantees endpoint == (primary_host, primary_port); failover_happened is False; endpoint == (secondary_host, secondary_port) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `endpoint == (primary_host, primary_port)`
- `failover_happened is False`
- `endpoint == (secondary_host, secondary_port)`
- `failover_happened is True`
- `endpoint2 == (secondary_host, secondary_port)`
- `failover_happened2 is False`
- `switcher.failed_primary is True`
- `switcher.current_endpoint == (secondary_host, secondary_port)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
