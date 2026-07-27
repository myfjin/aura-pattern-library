# hot copy

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 4 · State/DB durability

**Signature:** `(.0: list_iterator) → ?`

## What it does

Hot-copy a live SQLite database into a consistent point-in-time snapshot.

Uses SQLite's backup API while a writer is actively committing inserts. The
resulting copy must be a valid database whose rows form a contiguous committed
prefix (no gaps), proving it captures a single transaction point rather than a
torn mix.

## Guarantee

When it runs, hot copy guarantees live == 12 and len(idxs) <= live; os.path.exists(cp); cc.execute('PRAGMA integrity_check').fetchone()[0] == 'ok' (proven by run).

**Checkable constraints:**

- `os.path.exists(cp)`
- `cc.execute('PRAGMA integrity_check').fetchone()[0] == 'ok'`
- `idxs == list(range(len(idxs)))`
- `live == 12 and len(idxs) <= live`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
