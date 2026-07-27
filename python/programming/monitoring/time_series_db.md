# time series db

**Language:** Python · **Sphere:** programming · **Category:** Monitoring

**Signature:** `(values: List[float]) → float`

## What it does

In-memory time-series database module with support for insertion, querying,
aggregation, and downsampling.

## Guarantee

When it runs, time series db guarantees db.aggregate('temperature', base, base + 99, sum_func) == 2450; db.aggregate('temperature', base, base + 99, avg_func) == 24.5; db.aggregate('temperature', base, base + 99, max_func) == 29 (proven by run).

**Checkable constraints:**

- `[p.value for p in pts] == [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]`
- `[p.timestamp for p in pts] == [base + 90 + k for k in range(10)]`
- `db.aggregate('temperature', base, base + 99, sum_func) == 2450`
- `db.aggregate('temperature', base, base + 99, avg_func) == 24.5`
- `db.aggregate('temperature', base, base + 99, max_func) == 29`
- `db.aggregate('temperature', base, base + 99, min_func) == 20`
- `len(buckets) == 10`
- `all((b.value == 24.5 for b in buckets))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
