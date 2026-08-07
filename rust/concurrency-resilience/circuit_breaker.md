# circuit breaker

**Language:** Rust · **Oracle sphere:** system-administration (this file is the Rust twin) · **Category:** Wave 6 · Resource guards & quotas

## What it does

circuit_breaker — typestate closed/open/half-open enum; transitions asserted.

Core idea: implement the circuit breaker pattern using Rust's typestate pattern to
ensure state transitions are valid at compile time and runtime. States: Closed (ok),
Open (failing), HalfOpen (probing). THE ONE LAW: simulate a series of successes and
failures, verify state transitions are correct, and assert invalid transitions are
caught — an unguarded state machine would allow invalid paths.
When to use: fault tolerance, preventing cascading failures, dependency health checks.

## Guarantee

When it runs, circuit breaker guarantees breaker.state == 'open'; short_circuits >= 80; breaker.failure_count >= 10 (weak-grade: directional, proven by run on the SYS original).

**Checkable constraints:**

- `breaker.state == 'open'`
- `short_circuits >= 80`
- `breaker.failure_count >= 10`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the SYS original and shared by this Rust twin (twin agreement is the evidence: hard, positive, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
