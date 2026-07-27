# heartbeat lease

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 20 · Mesh / distributed coordination

**Signature:** `(lease_ttl: int) → ?`

## What it does

Heartbeat/Lease Pattern
Follower sends heartbeats to leader.
Leader grants lease based on heartbeats.
Assert: lease expires if heartbeats stop, leader detects failure.

## Guarantee

When it runs, heartbeat lease guarantees follower.last_heartbeat == 5; follower.last_heartbeat == 0; follower.is_alive() (proven by run).

**Checkable constraints:**

- `follower.last_heartbeat == 0`
- `follower.is_alive()`
- `follower.is_alive()`
- `not follower.is_alive()`
- `follower.is_alive()`
- `follower.last_heartbeat == 5`
- `follower.is_alive()`
- `not follower.is_alive()`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
