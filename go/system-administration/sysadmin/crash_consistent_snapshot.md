# crash consistent snapshot

**Language:** Go · **Sphere:** system-administration · **Category:** Wave 4 · State/DB durability

**Signature:** `(db_path: str, snap_path: str) → ?`

## What it does

crash_consistent_snapshot: snapshot a live DB atomically so the snapshot is never torn.

## Guarantee

When it runs, crash consistent snapshot guarantees not os.path.exists(snap) or _valid_db(snap); _valid_db(snap); snap_rows == committed (weak-grade: directional, proven by run on the SYS original).

**Checkable constraints:**

- `not os.path.exists(snap) or _valid_db(snap)`
- `_valid_db(snap)`
- `snap_rows == committed`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the SYS original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
