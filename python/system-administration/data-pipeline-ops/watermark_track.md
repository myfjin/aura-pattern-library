# watermark track

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 19 · Data pipeline ops

**Signature:** `(records: List[dict], watermark_path: str) → ?`

## What it does

Watermark Tracking Pattern
Track the highest record timestamp processed.
On resume, only process records with timestamp > watermark.
Asserts: no reprocessing of old records, watermark monotonically increases.

## Guarantee

When it runs, watermark track guarantees wm1 == 30; skipped2 == 3; wm2 == 50 (proven by run).

**Checkable constraints:**

- `len(processed1) == 3`
- `wm1 == 30`
- `skipped1 == 0`
- `len(processed2) == 2`
- `skipped2 == 3`
- `wm2 == 50`
- `ids2 == ['d', 'e']`
- `wm1 == 200`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def process_with_watermark(records, watermark_path):`
**Valid input:** `records` is a list of dicts with `'id'`, `'timestamp'`, and `'value'`; `watermark_path` is a writable JSON path.
**Core:** Tracks the highest timestamp processed in `watermark_path`; on each run, skips records with `timestamp <=` current watermark and updates the watermark after each processed record.
**Assert:** First batch `10,20,30` yields watermark 30 and 3 processed; second batch containing the same old records plus `40,50` skips 3 old records and processes 2 new ones with watermark 50.
**⚠️ Defect:** Out-of-order records with timestamps below the watermark are silently skipped, so late-arriving data is lost. The watermark is rewritten after every record, which is fine for small streams but inefficient for high-throughput pipelines. The initial watermark defaults to 0, which would skip any records with non-positive timestamps.

---

## Category: deployment-rollback

---
*△ AURA Pattern Library — © Reality Optimizer*
