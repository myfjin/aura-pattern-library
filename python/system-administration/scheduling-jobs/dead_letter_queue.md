# dead letter queue

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 7 · Scheduling & jobs

**Signature:** `(job_id: str, callback: Callable) → ?`

## What it does

Dead letter queue: move jobs to DLQ after N consecutive failures.
Failure simulated: job fails N times; assert it moves to DLQ exactly once.

## Guarantee

When it runs, dead letter queue guarantees dlq_items[0]['failure_count'] == 3; dlq3.get_dlq_count() == 2; result1 == 'retry' (proven by run).

**Checkable constraints:**

- `result1 == 'retry'`
- `result2 == 'retry'`
- `result3 == 'dlq'`
- `len(dlq_items) == 1`
- `dlq_items[0]['job_id'] == 'job_1'`
- `dlq_items[0]['failure_count'] == 3`
- `result4 == 'dlq'`
- `len(dlq_items) == 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
