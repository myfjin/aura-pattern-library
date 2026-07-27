# transaction rollback

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 4 · State/DB durability

## What it does

Transaction rollback: crash inside an active transaction before COMMIT.

A child process inserts a committed row, begins a transaction with two more
uncommitted rows, then is killed. On reopen, SQLite must roll back the
uncommitted rows automatically. The test asserts only the pre-transaction row
remains.

## Guarantee

When it runs, transaction rollback guarantees count == expected_count; False; 'pre_commit' in vals (proven by run).

**Checkable constraints:**

- `count == expected_count`
- `'pre_commit' in vals`
- `'txn_row_1' not in vals and 'txn_row_2' not in vals`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — chaos (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
