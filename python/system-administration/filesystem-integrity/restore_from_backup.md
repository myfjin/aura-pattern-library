# restore from backup

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 2 · Filesystem Integrity & Atomic Ops

**Signature:** `(backup_path: str, target_path: str) → ?`

## What it does

restore_from_backup: restore a file from backup after corruption/deletion.
Failure simulated: backup a file; delete/corrupt the original; restore from backup;
assert the original is recovered to exact byte-for-byte match.
Recovery asserted: restored file == backed-up file; no data loss; corruption is undone.
Pattern's own restore function is called, not the test scaffold.

## Guarantee

When it runs, restore from backup guarantees Path(backup).read_bytes() == expected_original; Path(source).read_bytes() != expected_original; Path(source).read_bytes() == expected_corrupted (proven by run).

**Checkable constraints:**

- `Path(backup).read_bytes() == expected_original`
- `Path(source).read_bytes() != expected_original`
- `Path(source).read_bytes() == expected_corrupted`
- `result == expected_original`
- `len(result) == len(expected_original)`
- `result[:17] == b'restore_original_'`
- `result[-1:] == expected_original[-1:]`
- `result != expected_corrupted`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
