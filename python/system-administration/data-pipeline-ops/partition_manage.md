# partition manage

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 19 · Data pipeline ops

**Signature:** `(records: List[dict], partition_meta_path: str) → ?`

## What it does

Partition Management Pattern
Manage partitions (e.g., date-based, range-based).
Track which partitions are closed (immutable), which are open (mutable).
Assert: no reprocessing closed partitions, exactly-once per partition.

## Guarantee

When it runs, partition manage guarantees 'p1' in meta1['closed']; 'p2' not in meta1['closed']; set(p2_ids) == {'d', 'e'} (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(output1) == 3`
- `'p1' in meta1['closed']`
- `'p2' not in meta1['closed']`
- `len(output2) == 2`
- `len(p1_ids_in_output2) == 0`
- `set(p2_ids) == {'d', 'e'}`
- `len(output1) == 2`
- `len(output2) == 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def process_partitioned(records, partition_meta_path):`
**Valid input:** `records` is a list of dicts with `'id'`, `'partition'`, and `'value'`; `partition_meta_path` is a writable JSON path.
**Core:** Tracks per-partition processed counts and a closed-partition list; records belonging to a closed partition are skipped; a partition is closed once it reaches `max_per_partition=2` records.
**Assert:** Processing 2 records for partition `p1` plus 1 for `p2` closes `p1`; a second batch with more `p1` records skips them while accepting additional `p2` records.
**⚠️ Defect:** The closure threshold is hardcoded to 2, which is arbitrary and unsuitable for real partitions. Partition closure is irreversible in the current run, so late-arriving records for a closed partition are silently dropped rather than quarantined or logged.

---
*△ AURA Pattern Library — © Reality Optimizer*
