# circuit breaker

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 6 · Resource guards & quotas

**Signature:** `(failure_threshold: int, recovery_timeout: float) → ?`

## What it does

Circuit breaker: opens after N failures, short-circuits further calls.
Failure simulated: call function 100 times, it fails first 10 times;
assert breaker opens after 10 failures, short-circuits remaining 90 calls,
short-circuit count = 90.

## Guarantee

When it runs, circuit breaker guarantees breaker.state == 'open'; short_circuits >= 80; breaker.failure_count >= 10 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `breaker.state == 'open'`
- `short_circuits >= 80`
- `breaker.failure_count >= 10`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — positive, xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
