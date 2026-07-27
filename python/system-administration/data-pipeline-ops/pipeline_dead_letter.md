# pipeline dead letter

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 19 · Data pipeline ops

**Signature:** `(records: List[dict], dlq_path: str, retry_limit: int) → ?`

## What it does

Dead Letter Queue Pattern
When processing fails, route to dead letter queue.
Retry logic: retry 3 times, then move to DLQ.
Assert: all records either processed or in DLQ, no lost records.

## Guarantee

When it runs, pipeline dead letter guarantees dlq[0]['retry_count'] == 3; len(processed) == 2; len(dlq) == 2 (proven by run).

**Checkable constraints:**

- `len(processed) == 2`
- `len(dlq) == 2`
- `total_ids == {'a', 'b', 'c', 'd'}`
- `len(success_ids & dlq_ids) == 0`
- `len(dlq) == 1`
- `dlq[0]['retry_count'] == 3`
- `len(result) == 2`
- `'b' not in ids`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def process_with_dlq(records, dlq_path, retry_limit=3):`, `class ProcessingError(Exception):`
**Valid input:** `records` is a list of dicts with `'id'` and `'value'`; failing records are marked with `'bad_record': True`; `dlq_path` is a writable JSON path.
**Core:** Retries each record up to `retry_limit` times; records that still fail are appended to a dead-letter queue (DLQ) JSON file together with the original record, error message, and retry count.
**Assert:** Out of 4 records with 2 bad ones and `retry_limit=1`, exactly 2 are processed and 2 land in the DLQ with no overlap and no lost IDs; a single bad record retried 3 times records `retry_count == 3`.
**⚠️ Defect:** The DLQ is appended to memory but the file is only flushed when a record finally fails; a crash mid-retry could lose DLQ entries. There is no backoff between retries. Successfully processed records are not persisted, so an overall pipeline retry could reprocess them.

---
*△ AURA Pattern Library — © Reality Optimizer*
