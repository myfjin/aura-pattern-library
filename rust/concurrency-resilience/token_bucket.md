# token bucket

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `(now: i64) → ?`

## What it does

token_bucket — real token bucket with virtual clock; burst shaped to rate.

Core idea: token bucket rate limiter using a virtual clock. Tokens accumulate over time
at a fixed rate; consumers take tokens to perform work. Bursts are bounded by bucket
capacity. THE ONE LAW: advance the virtual clock, request tokens, and assert the burst
pattern matches the expected shape — an unguarded bucket would allow unlimited bursts,
failing the capacity assert. When to use: API rate limiting, traffic shaping.

## Guarantee

When it runs, token bucket guarantees assert_eq!(burst_count, 0, "burst should be fully depleted") (proven by rustc-run).

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
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
