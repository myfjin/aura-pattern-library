# corruption repair

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 4 · State/DB durability

## What it does

corruption_repair: detect and repair SQLite DB corruption (or mark unrecoverable).

The disaster test creates a valid database, backs it up, truncates the live DB
mid-write to corrupt it, then attempts detection + repair. If direct repair
fails it falls back to the backup. The test asserts that corruption was detected,
that the final DB is consistent, and that no data was lost.

## Guarantee

When it runs, corruption repair guarantees rows == 3; corruption_detected; result == 'ok' (proven by run).

**Checkable constraints:**

- `corruption_detected`
- `result == 'ok'`
- `rows == 3`
- `corruption_detected`
- `corruption_detected and (repair_ok or not final_ok)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
