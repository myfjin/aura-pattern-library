# migration with rollback

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 4 · State/DB durability

**Signature:** `(db_path: str) → ?`

## What it does

Migration with rollback: crash mid-migration, schema must stay consistent.

The test creates a temporary SQLite database with an old schema, starts a child
process to run a multi-step migration, then kills the child mid-transaction.
After the crash the database must be either the old schema (rolled back) or the
new schema (fully applied) — never a partial mix. All existing data must
survive.

## Guarantee

When it runs, migration with rollback guarantees row_count == 2; old_version == 'old'; version_after in ['old', 'new'] (proven by run).

**Checkable constraints:**

- `old_version == 'old'`
- `version_after in ['old', 'new']`
- `row_count == 2`
- `'name' in cols_after`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — chaos (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
