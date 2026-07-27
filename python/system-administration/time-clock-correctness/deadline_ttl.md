# deadline ttl

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 11 · Time, clock & correctness

**Signature:** `(ttl_seconds: float) → ?`

## What it does

Deadline/TTL checker over an injectable clock.

DeadlineChecker turns a TTL into an absolute deadline via a supplied clock
function, then reports whether that deadline has passed and how much time
remains (negative once expired). Injecting the clock keeps expiry logic
deterministic and testable. Use it for cache TTLs, request deadlines, or
lease timers. Guarantees (self-test oracle): not-expired before the deadline,
expired exactly at and after it (>= boundary), remaining time is exact
including negative values, and independent deadlines are tracked separately.

## Guarantee

When it runs, deadline ttl guarantees checker.remaining(deadline) == 10.0; checker.remaining(deadline2) == 4.0; checker.is_expired(deadline) is False (proven by run).

**Checkable constraints:**

- `checker.is_expired(deadline) is False`
- `checker.remaining(deadline) == 10.0`
- `checker.is_expired(deadline) is True`
- `checker.remaining(deadline) == -1.0`
- `checker.is_expired(deadline) is True`
- `checker.remaining(deadline) == 0.0`
- `checker.is_expired(deadline1) is True`
- `checker.is_expired(deadline2) is False`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
