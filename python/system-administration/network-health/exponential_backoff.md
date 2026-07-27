# exponential backoff

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 8 · Network reachability & health

**Signature:** `(operation: Callable, max_attempts: int, base_delay_ms: int) → ?`

## What it does

exponential_backoff: retry with exponential backoff (2^attempt * base_delay); assert delays increase.
Failure simulated: operation fails first 3 times, succeeds on 4th; measure inter-attempt delays.
Recovery asserted: delays follow 2^n pattern (base, 2*base, 4*base, ...); operation succeeds after retries.

## Guarantee

When it runs, exponential backoff guarantees attempts == 4; success is True; len(delays) == 3 (proven by run).

**Checkable constraints:**

- `success is True`
- `attempts == 4`
- `len(delays) == 3`
- `delays[1] > delays[0] * 0.8`
- `delays[2] > delays[1] * 0.8`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
