# http retry client

**Language:** Python · **Sphere:** programming · **Category:** Networking

## What it does

HTTP Client with Retry, Backoff, and Circuit Breaker Support

This module provides a robust HTTP client that supports configurable retry policies,
exponential backoff, and circuit breaker pattern to handle transient failures gracefully.

## Guarantee

When it runs, http retry client guarantees failures == 3 and cb.state == CircuitState.OPEN; resp.status_code == 200; attempts[0] == 3 (proven by run).

**Checkable constraints:**

- `trace == [0.5, 1.0, 2.0, 4.0, 5.0]`
- `all((0 < jbo.calculate_delay(a) <= 5.0 for a in range(1, 8)))`
- `failures == 3 and cb.state == CircuitState.OPEN`
- `called[0] == 0`
- `cb.call(probe) == 'ok'`
- `cb.state == CircuitState.CLOSED`
- `called[0] == 1`
- `resp.status_code == 200`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
