# rate limiter

**Language:** Python · **Sphere:** programming · **Category:** Networking

## What it does

Token-bucket rate limiter with independent per-key buckets.

Use to cap request rates per client/key: each key gets its own bucket of a given
capacity that refills at a fixed tokens-per-second; consume() spends tokens (a
burst up to capacity, then denials) and remaining_time() reports the wait until
enough tokens accrue. Refill is lazy (computed from a monotonic clock) and
thread-safe. Guarantees (proven by self-test on a fake clock): a burst grants
exactly the capacity then denies; refill is exact (0.5s at 10/s = 5 tokens) and
never exceeds capacity; the computed wait is precise; keys are isolated; and
reset() restores a fresh full bucket.

## Guarantee

When it runs, rate limiter guarantees granted == 20; regrants == 5; abs(wait - 0.5) < 1e-09 (proven by run).

**Checkable constraints:**

- `granted == 20`
- `limiter.consume('k') is False`
- `regrants == 5`
- `abs(wait - 0.5) < 1e-09`
- `limiter.consume('k', 5.0) is True`
- `stats['tokens'] == 20.0`
- `stats['capacity'] == 20.0 and stats['refill_rate'] == 10.0`
- `all((limiter.consume('a') for _ in range(20)))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
