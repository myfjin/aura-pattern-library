# cow backup

**Language:** Go · **Oracle sphere:** system-administration (this file is the Go twin) · **Category:** Wave 2 · Filesystem Integrity & Atomic Ops

## What it does

cow_backup: an independent point-in-time backup that survives later source corruption.
Honest disclosure: this is an EAGER FULL COPY (read all bytes → temp → atomic rename),
not block-level copy-on-write. It delivers the same user-facing guarantee a CoW backup
gives — the backup is fully independent of the source — without a CoW filesystem.

## Guarantee

When it runs, cow backup guarantees result == expected_original and len(result) == len(expected_original); result == expected_original; result != expected_corrupted (proven by run on the SYS original).

**Checkable constraints:**

- `result == expected_original and len(result) == len(expected_original)`
- `result == expected_original`
- `result != expected_corrupted`
- `source_data == expected_corrupted`
- `result != source_data`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the SYS original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
