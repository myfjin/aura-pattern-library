# p2 percentile

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 14 · Monitoring & metrics

**Signature:** `(i: int, d: int) → ?`

## What it does

p2_percentile: P2 algorithm (Jain & Chlamtac 1985) for online percentile estimation.

The P2 estimator keeps only FIVE markers (O(1) memory) and never stores the stream.
The middle marker q[2] tracks the desired p-quantile; the estimate is read from the
markers, NOT from a retained copy of the data.

## Guarantee

When it runs, p2 percentile guarantees single.get_percentile() == 42; not hasattr(probe, 'observations'); len(probe.q) == 5 (proven by run).

**Checkable constraints:**

- `not hasattr(probe, 'observations')`
- `len(probe.q) == 5`
- `abs(est - true) / true < 0.01`
- `abs(est - true) / true < 0.05`
- `p2_of(ten, 50) != brute_force_percentile(ten, 50)`
- `p2_of(ten, 25) < p2_of(ten, 50) < p2_of(ten, 90)`
- `P2Percentile(percentile=50).get_percentile() == 0`
- `single.get_percentile() == 42`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
