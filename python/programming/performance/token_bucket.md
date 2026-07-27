# token bucket

**Language:** Python · **Sphere:** rust · **Category:** performance

**Signature:** `(now: i64) → ?`

## What it does

Token-bucket rate limiter with lazy time-based refill.

A thread-safe bucket that refills at a fixed rate up to a capacity: consume()
grants tokens when available (allowing bursts up to capacity) and otherwise
reports the exact wait until enough accrue; a RateLimiter facade adds blocking
acquire. Refill is computed lazily from a monotonic clock, so no background
timer runs. Use it to cap request/action rates while permitting short bursts.
Guarantees (self-test oracle): a full bucket grants exactly its capacity, an
empty bucket denies with the correct wait time, refill math is exact and caps
at capacity, and a request larger than capacity is refused as impossible.

## Guarantee

When it runs, token bucket guarantees assert_eq!(burst_count, 0, "burst should be fully depleted") (proven by rustc-run on the RUST original).

**Checkable constraints:**

- `assert!(bucket.try_consume(0, 10.0), "should consume full capacity")`
- `assert!(!bucket.try_consume(0, 1.0), "should be empty after consuming all")`
- `assert!(available_at_5 >= 4.9 && available_at_5 <= 5.1, "should have ~5 tokens at t=5")`
- `assert!(bucket.try_consume(5, 5.0), "should consume 5 at t=5")`
- `assert!(available_at_15 >= 9.9 && available_at_15 <= 10.1, "should be capped at capacity")`
- `assert_eq!(burst_count, 0, "burst should be fully depleted")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the RUST original and shared by this Python twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
