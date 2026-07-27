# crash consistent snapshot

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 4 · State/DB durability

**Signature:** `(db_path: str, snap_path: str) → ?`

## What it does

crash_consistent_snapshot: snapshot a live DB atomically (backup -> temp -> fsync -> rename)
so the snapshot is NEVER visible in a torn state.
Failure simulated: SIGKILL the snapshotting process INSIDE the (slow, page-by-page) copy,
before the atomic rename. Recovery asserted: the target snapshot is either ABSENT (rename never
happened) or a fully-valid DB — NEVER a torn/half-written file. A naive backup written directly
to the target, killed mid-copy, leaves a torn target and FAILS this. A clean run then proves the
snapshot equals the exact committed row count.

## Guarantee

When it runs, crash consistent snapshot guarantees not os.path.exists(snap) or _valid_db(snap); _valid_db(snap); snap_rows == committed (weak-grade: directional, proven by run).

**Checkable constraints:**

- `not os.path.exists(snap) or _valid_db(snap)`
- `_valid_db(snap)`
- `snap_rows == committed`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
