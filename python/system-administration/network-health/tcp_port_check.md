# tcp port check

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 8 · Network reachability & health

**Signature:** `(host: str, port: int, timeout_sec: float) → ?`

## What it does

tcp_port_check: attempt to connect to a port; return True if reachable, False if down/refused.
Failure simulated: bind a real socket on 127.0.0.1:ephemeral, verify it's up, close it, verify it's down.
Recovery asserted: reachability changes from True→False when port closes; false reconnect on closed port.

## Guarantee

When it runs, tcp port check guarantees is_up is True; is_down is False; is_up is True and is_down is False (weak-grade: directional, proven by run).

**Checkable constraints:**

- `is_up is True`
- `is_down is False`
- `is_up is True and is_down is False`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
