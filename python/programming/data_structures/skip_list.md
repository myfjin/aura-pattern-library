# skip list

**Language:** Python · **Oracle sphere:** rust (this file is the Python twin) · **Category:** data structures

## What it does

Probabilistic skip list mapping int keys to values with randomized level
promotion, giving expected O(log n) search, insert, and delete.

Use as an ordered map with sorted iteration and range queries, without the
rotation machinery of a balanced tree.

Guarantees (self-test): iteration stays sorted after shuffled inserts, range
queries return exact contiguous slices, insert on an existing key updates in
place, delete reports honestly, and a 600-op fuzz agrees with a dict oracle.

## Guarantee

When it runs, skip list guarantees `len(sl) == 100`; `[k for k, _ in sl] == list(range(100))`; `sl.search(50) == 'value_50'` — read from this file's own self-test. The oracle behind this pattern was established on the rust original and is not claimed to have been run against this file.

**Checkable constraints:**

- `len(sl) == 100`
- `[k for k, _ in sl] == list(range(100))`
- `sl.search(50) == 'value_50'`
- `sl.search(150) is None`
- `sl.range_query(10, 13) == [(10, 'value_10'), (11, 'value_11'), (12, 'value_12'), (13, 'value_13')]`
- `sum((k for k, _ in sl.range_query(10, 13))) == 46`
- `sl.range_query(200, 300) == []`
- `len(sl) == 100 and sl.search(50) == 'replaced'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the RUST original and shared by this Python twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
