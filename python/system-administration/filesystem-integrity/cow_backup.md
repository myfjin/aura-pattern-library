# cow backup

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 2 · Filesystem Integrity & Atomic Ops

**Signature:** `(source_path: str, backup_path: str) → ?`

## What it does

cow_backup: an independent point-in-time backup that survives later source corruption.
NAME DISCLOSURE (honest): this is an EAGER FULL COPY (read all bytes → temp → atomic rename),
NOT block-level copy-on-write. It delivers the same USER-FACING guarantee a CoW backup gives —
the backup is fully independent of the source, so corrupting the source cannot touch it —
WITHOUT the block-sharing space/time efficiency of real CoW (that needs a CoW filesystem).
Failure simulated: back up a live file, then corrupt the original; the backup must still hold
the original bytes. Recovery asserted: backup == original at backup time AND after the source
is corrupted (independence). The pattern's own function is called.

## Guarantee

When it runs, cow backup guarantees result == expected_original and len(result) == len(expected_original); result == expected_original; result != expected_corrupted (proven by run).

**Checkable constraints:**

- `result == expected_original and len(result) == len(expected_original)`
- `result == expected_original`
- `result != expected_corrupted`
- `source_data == expected_corrupted`
- `result != source_data`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
