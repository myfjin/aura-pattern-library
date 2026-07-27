# circuit breaker

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 6 · Resource guards & quotas

**Signature:** `(failure_threshold: int, recovery_timeout: float) → ?`

## What it does

Circuit breaker that stops calling a failing dependency.

Wraps a callable (as decorator or via call()) and tracks failures: after the
threshold trips it opens and fails fast without invoking the callable, then
after a recovery timeout enters half-open to probe once — a success closes and
resets, a failure re-opens. Use it to prevent cascading failures against a
flaky downstream service. Guarantees (self-test oracle): the threshold count
opens the circuit, an open breaker does not call the wrapped function, a
half-open failure re-opens while a success closes and zeroes the count, and
exceptions outside the expected type pass through without tripping it.

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
