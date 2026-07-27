# readiness vs liveness

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 1 · Process Supervision & Immortality

**Signature:** `(n: int) → ?`

## What it does

readiness_vs_liveness: liveness = the process is running; readiness = it can serve requests.
They are INDEPENDENT, and the point of the distinction is operational: a router must withhold
traffic from an instance that is alive-but-unready, and drop one that is dead — while a
liveness-only view would wrongly keep routing to a degraded instance.
Failure simulated: a live instance degrades (unready), then a ready instance dies.
Recovery asserted: the readiness-aware router sends ZERO requests to the unready-but-alive
instance (traffic withheld) and none to the dead one — proven by per-instance request counts.
A liveness-only router (ignoring readiness) would keep feeding the degraded instance → the
assert on its 0-count would fail.

## Guarantee

When it runs, readiness vs liveness guarantees a.handled > 0 and b.handled > 0; a.check_liveness() is True and a.check_readiness() is False; a.handled == p1_a (weak-grade: directional, proven by run).

**Checkable constraints:**

- `a.handled > 0 and b.handled > 0`
- `a.check_liveness() is True and a.check_readiness() is False`
- `a.handled == p1_a`
- `b.handled == p1_b + 100`
- `a.handled > p1_a`
- `b.check_liveness() is False and b.check_readiness() is False`
- `b.handled == handled_b_before`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
