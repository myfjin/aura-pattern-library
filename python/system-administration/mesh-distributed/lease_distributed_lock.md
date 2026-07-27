# lease distributed lock

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 20 · Mesh / distributed coordination

**Signature:** `(holder_id: str) → ?`

## What it does

Distributed Lock with Lease Pattern
Lock expires after lease_ttl (logical time, not wall-clock).
Assert: lock is reacquirable after expiry, holder can renew.

## Guarantee

When it runs, lease distributed lock guarantees lock.acquire('A'); lock.holder() == 'A'; not lock.acquire('B') (weak-grade: directional, proven by run).

**Checkable constraints:**

- `lock.acquire('A')`
- `lock.holder() == 'A'`
- `not lock.acquire('B')`
- `lock.holder() == 'A'`
- `lock.acquire('A')`
- `lock.holder() == 'A'`
- `lock.holder() == 'A'`
- `lock.holder() is None`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
