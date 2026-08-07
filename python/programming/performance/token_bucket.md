# token bucket

**Language:** Python · **Oracle sphere:** rust (this file is the Python twin) · **Category:** performance

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

When it runs, token bucket guarantees `ok and wait == 0.0`; `not ok`; `abs(wait - 0.2) < 1e-09` — read from this file's own self-test. The oracle behind this pattern was established on the rust original and is not claimed to have been run against this file.

**Checkable constraints:**

- `ok and wait == 0.0`
- `not ok`
- `abs(wait - 0.2) < 1e-09`
- `abs(tb.peek() - 2.5) < 1e-09`
- `ok`
- `abs(tb.peek() - 0.5) < 1e-09`
- `abs(tb.peek() - 10.0) < 1e-09`
- `not ok and wait == float('inf')`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the RUST original and shared by this Python twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
