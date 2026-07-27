# backfill range

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 19 · Data pipeline ops

**Signature:** `(records: List[dict], range_start: int, range_end: int, backfill_path: str) → ?`

## What it does

Backfill Range Pattern
Fill gaps in time series or sequence.
Assert: no gaps remain, existing records not duplicated.

## Guarantee

When it runs, backfill range guarantees gaps_filled == 2; gaps1 == 2; len(filled) == 5 (proven by run).

**Checkable constraints:**

- `gaps_filled == 2`
- `len(filled) == 5`
- `seqs == [1, 2, 3, 4, 5]`
- `len(backfilled) == 2`
- `gaps1 == 2`
- `len(filled1) == 5`
- `gaps2 == 0`
- `len(filled2) == 5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def backfill_range(records, range_start, range_end, backfill_path):`
**Valid input:** `records` is a list of dicts each containing `'seq'`; `range_start` and `range_end` are ints defining the inclusive sequence range to fill; `backfill_path` is a writable JSON path that persists processed ranges.
**Core:** Computes gaps in the sequence range, skips the whole range if it was already backfilled (recorded in `backfill_path`), otherwise appends synthetic backfill records and persists the new range.
**Assert:** Sparse records `seq 1,3,5` backfilled to `[1,5]` produce 5 records with gaps 2 and 4 marked `source='backfill'`; re-running the same range yields zero new fills and no duplicates.
**⚠️ Defect:** The gap-filling logic mutates the input `records` list in place. The per-record processing order is not transactional: if the process crashes after writing some backfilled records but before persisting the range, a retry could duplicate those records. The synthetic backfill value is just `f'backfilled_{seq}'`, with no schema integration.

---
*△ AURA Pattern Library — © Reality Optimizer*
