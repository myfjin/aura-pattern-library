# wal checkpoint

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 4 · State/DB durability

**Signature:** `(db_path: str) → ?`

## What it does

wal_checkpoint: SQLite WAL (Write-Ahead Log) checkpoint that replays changes to the main DB.
Failure simulated: crash DURING checkpoint, after some pages flushed but before journal cleared.
Recovery asserted: upon reopen, the WAL is replayed correctly; the DB contains exactly the rows
that were committed before the crash (recovery via WAL replay), never torn state. A checkpoint
that loses mid-flush would leave the DB inconsistent; this assert catches that.

## Guarantee

When it runs, wal checkpoint guarantees count_after == 2; count_after >= count_before; len(rows) == 2 (proven by run).

**Checkable constraints:**

- `count_after == 2`
- `count_after >= count_before`
- `len(rows) == 2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
