# jitter backoff

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 7 · Scheduling & jobs

**Signature:** `(attempt: int, base_delay: float, max_jitter_factor: float, max_delay: int) → ?`

## What it does

Jitter backoff: add randomness to retry delays to prevent thundering herd.
Failure simulated: N jobs all retry at the same time; assert jitter spreads fires across time.

## Guarantee

When it runs, jitter backoff guarantees attempt_count[0] == 2; attempt_count[0] == 3; len(retry_times) == 1 (proven by run).

**Checkable constraints:**

- `attempt_count[0] == 2`
- `len(retry_times) == 1`
- `attempt_num == 1`
- `delay > 0`
- `elapsed >= delay * 0.8`
- `attempt_count[0] == 3`
- `len(retry_times) == 2`
- `delay1 > 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
