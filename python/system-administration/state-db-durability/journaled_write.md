# journaled write

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 4 · State/DB durability

**Signature:** `(data_path: str, journal_path: str) → ?`

## What it does

journaled_write: write data to a journal first, then apply to the main store (undo logging).
Failure simulated: crash between journal write and main store update.
Recovery asserted: on reopen, the system is in a consistent state: either old data (if journal
wasn't fully flushed) or new data (if journal was flushed and uncommitted changes rolled forward).
Never a torn state where the journal is half-written or the main file is half-updated.

## Guarantee

When it runs, journaled write guarantees recovered == expected_old or recovered == expected_new; re_parsed == recovered; final in [{'count': 0}, {'count': 1}] (proven by run).

**Checkable constraints:**

- `recovered == expected_old or recovered == expected_new`
- `re_parsed == recovered`
- `final in [{'count': 0}, {'count': 1}]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — chaos (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
