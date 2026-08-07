# dead letter queue

**Language:** Go · **Oracle sphere:** system-administration (this file is the Go twin) · **Category:** Wave 7 · Scheduling & jobs

## What it does

dead_letter_queue: retry handler with exponential backoff and poison-pill detection.

## Guarantee

When it runs, dead letter queue guarantees dlq_items[0]['failure_count'] == 3; dlq3.get_dlq_count() == 2; result1 == 'retry' (proven by run on the SYS original).

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
- **Independent oracle:** — established on the SYS original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
