# watchdog restart

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 1 · Process Supervision & Immortality

**Signature:** `(pred: Callable, timeout: float) → ?`

## What it does

watchdog_restart: a real watchdog supervises a child, restarts it on death up to a cap,
then STOPS restarting and flags a crash-loop once the cap is exceeded.
Failure simulated: the watchdog's OWN child is SIGKILL'd repeatedly (real deaths).
Recovery asserted: the WATCHDOG (not the test) detects each death and restarts — assert the
watchdog's restart counter reached the cap and a live child exists; then one death past the
cap → assert it did NOT restart and raised the crash-loop flag. The assert fails on a no-op
watchdog (one that never restarts leaves the counter at 0 and the flag unset).

## Guarantee

When it runs, watchdog restart guarantees _wait_until(lambda: wd.child is not None); _wait_until(lambda: wd.restarts >= n); wd.restarts == cap (weak-grade: directional, proven by run).

**Checkable constraints:**

- `_wait_until(lambda: wd.child is not None)`
- `_wait_until(lambda: wd.restarts >= n)`
- `wd.restarts == cap`
- `live`
- `wd.capped is False`
- `_wait_until(lambda: wd.capped)`
- `wd.restarts == cap`
- `wd.child is None`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
