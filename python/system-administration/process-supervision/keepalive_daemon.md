# keepalive daemon

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 1 · Process Supervision & Immortality

**Signature:** `(poke_interval: float, timeout_threshold: float) → ?`

## What it does

keepalive_daemon: a background thread pokes a keepalive file every interval; a watcher treats
the process as alive only while pokes keep arriving within a timeout.
Failure simulated (the real one): the daemon STOPS poking — the file goes stale.
Recovery asserted: while poking, check_keepalive() is True; after the daemon stops and the
timeout elapses, check_keepalive() flips to False — the stall is DETECTED (not because the
file was deleted, but because its timestamp went stale). A no-op watcher that always returns
True would fail the post-stop assert.

## Guarantee

When it runs, keepalive daemon guarantees daemon.poke_count == 0; mid >= 3; daemon.check_keepalive() is True (weak-grade: directional, proven by run).

**Checkable constraints:**

- `daemon.poke_count == 0`
- `mid >= 3`
- `daemon.check_keepalive() is True`
- `after_stop == mid`
- `daemon.check_keepalive() is True`
- `daemon.check_keepalive() is False`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
