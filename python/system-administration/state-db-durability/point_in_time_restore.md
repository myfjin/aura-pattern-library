# point in time restore

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 4 · State/DB durability

**Signature:** `(base_path: str, log_path: str, target_ts: int, db_path: str) → ?`

## What it does

point_in_time_restore: restore a DB to an exact point in time = a base backup + replay of the
write-ahead log up to a target timestamp (no entry newer than the target is applied).
Failure simulated: crash mid-restore (killed after the base copy, before the log is fully
replayed). Recovery asserted: (1) restoring to a target yields EXACTLY the state committed by
that time (older targets exclude newer rows — a no-op "copy the latest DB" fails this), and
(2) restore is crash-resumable — a killed restore, re-run, converges to the same exact state.
Uses logical timestamps (1,2,3) so the point-in-time is deterministic.

## Guarantee

When it runs, point in time restore guarantees vals(db) == ['row_1']; vals(db) == ['row_1', 'row_2']; vals(db) == ['row_1', 'row_2', 'row_3'] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `vals(db) == ['row_1']`
- `vals(db) == ['row_1', 'row_2']`
- `vals(db) == ['row_1', 'row_2', 'row_3']`
- `vals(db) == ['row_1']`
- `vals(db) == ['row_1', 'row_2']`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — chaos (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
