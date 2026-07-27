# load shedding

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 6 · Resource guards & quotas

**Signature:** `(capacity: int) → ?`

## What it does

Load shedding: drops excess requests to keep served load ≤ capacity.
Failure simulated: submit 1000 requests with capacity=64;
assert served ≤ 64, dropped > 900, peak served ≤ capacity.

## Guarantee

When it runs, load shedding guarantees peak_queue <= 64; num_dropped > 900; total_served <= 100 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `peak_queue <= 64`
- `num_dropped > 900`
- `total_served <= 100`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
