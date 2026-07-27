# backup rotation

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 4 · State/DB durability

**Signature:** `(d: str) → ?`

## What it does

backup_rotation: keep N versioned backups; rotate with ATOMIC renames so a crash during rotation
never tears a file and never loses the newest backup.
Failure simulated: SIGKILL the process DURING the rotation rename sequence (not before it).
Recovery asserted (unconditional): after the crash, (1) EVERY surviving backup file is COMPLETE
(never a torn/half-written file — guaranteed by rename atomicity), and (2) the NEWEST backup's
content still exists somewhere (renames move it, never delete it). A naive copy-based rotation
(read+write) killed mid-copy leaves a torn file and FAILS (1).

## Guarantee

When it runs, backup rotation guarantees content.startswith('backup_data_version_') and content.endswith('\n'); 'backup_data_version_3' in all_content (weak-grade: directional, proven by run).

**Checkable constraints:**

- `survivors`
- `content.startswith('backup_data_version_') and content.endswith('\n')`
- `'backup_data_version_3' in all_content`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
