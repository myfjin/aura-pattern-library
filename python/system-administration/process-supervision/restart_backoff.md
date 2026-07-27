# restart backoff

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 1 · Process Supervision & Immortality

**Signature:** `(max_backoff: float, backoff_factor: float) → ?`

## What it does

restart_backoff: on repeated crashes, increase delay between restarts: 1, 2, 4, 8, ... (capped).
Failure simulated: child crashes repeatedly.
Recovery asserted: measure delays; assert they grow exponentially (1s, 2s, 4s, 8s) up to cap.

## Guarantee

When it runs, restart backoff guarantees abs(delays[0] - target_first_delay) < tolerance; len(delays) == 3; delays[0] < delays[1] < delays[2] (proven by run).

**Checkable constraints:**

- `len(delays) == 3`
- `delays[0] < delays[1] < delays[2]`
- `abs(delays[0] - target_first_delay) < tolerance`
- `ratio_1_to_2 >= 1.5`
- `ratio_2_to_3 >= 1.5`
- `min(delays) > 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
