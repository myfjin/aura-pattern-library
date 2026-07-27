# backpressure queue

**Language:** Go · **Sphere:** system-administration · **Category:** Wave 6 · Resource guards & quotas

**Signature:** `(max_size: int, timeout_sec: float) → ?`

## What it does

Backpressure queue: refuses (non-blocking put_nowait) items when the bounded queue is full.
Failure simulated: flood queue with 1000 items, cap=64; assert items are refused
after the cap, peak depth ≤ cap, refused > 900.

## Guarantee

When it runs, backpressure queue guarantees peak_depth <= 64; num_refused > 900; num_accepted <= 64 (weak-grade: directional, proven by run on the SYS original).

**Checkable constraints:**

- `peak_depth <= 64`
- `num_refused > 900`
- `num_accepted <= 64`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the SYS original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
