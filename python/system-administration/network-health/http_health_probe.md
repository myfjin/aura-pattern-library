# http health probe

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 8 · Network reachability & health

**Signature:** `(url: str, timeout_sec: float) → ?`

## What it does

http_health_probe: probe HTTP /health endpoint; return status_ok if 200, down if connection refused.
Failure simulated: start an http.server on 127.0.0.1:ephemeral, probe /health, stop server, probe again.
Recovery asserted: probe returns 200 when server up, ConnectionRefused when server down.

## Guarantee

When it runs, http health probe guarantees status_up == 200; status_up == 200 and status_down == -1; status_down == -1 (proven by run).

**Checkable constraints:**

- `status_up == 200`
- `status_down == -1`
- `status_up == 200 and status_down == -1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
