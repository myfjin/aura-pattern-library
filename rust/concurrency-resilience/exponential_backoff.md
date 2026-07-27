# exponential backoff

**Language:** Rust · **Sphere:** system-administration · **Category:** Wave 8 · Network reachability & health

**Signature:** `(operation: Callable, max_attempts: int, base_delay_ms: int) → ?`

## What it does

exponential_backoff — backoff + seeded jitter; bounded, monotone-in-expectation.

Core idea: implement exponential backoff with deterministic seeded jitter. Each retry
waits longer than the previous. THE ONE LAW: seed a deterministic RNG, compute backoff
times, then assert they increase monotonically (in expectation, with jitter) and stay
within a bounded max — an uncapped backoff or missing jitter would fail the bound or
expectation asserts. When to use: retry logic, distributed system resilience.

## Guarantee

When it runs, exponential backoff guarantees attempts == 4; success is True; len(delays) == 3 (proven by run on the SYS original).

**Checkable constraints:**

- `success is True`
- `attempts == 4`
- `len(delays) == 3`
- `delays[1] > delays[0] * 0.8`
- `delays[2] > delays[1] * 0.8`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the SYS original and shared by this Rust twin (twin agreement is the evidence: hard, positive, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
