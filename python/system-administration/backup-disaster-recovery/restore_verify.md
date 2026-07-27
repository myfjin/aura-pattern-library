# restore verify

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 13 · Backup & disaster recovery

**Signature:** `(src_dir: Path, backup_dir: Path) → ?`

## What it does

restore_verify: verify backup integrity, fail on tampering.

## Guarantee

When it runs, restore verify guarantees 'file1.txt' in manifest and 'file2.txt' in manifest; verify_backup(backup_base); (restore_base / 'file1.txt').read_text() == 'content1_payload' (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(manifest) == 2`
- `'file1.txt' in manifest and 'file2.txt' in manifest`
- `verify_backup(backup_base)`
- `(restore_base / 'file1.txt').read_text() == 'content1_payload'`
- `(restore_base / 'file2.txt').read_text() == 'content2_payload'`
- `'hash mismatch' in str(e).lower()`
- `'corrupted' in str(e).lower() or 'mismatch' in str(e).lower()`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def create_backup_with_manifest(src_dir, backup_dir):`, `def verify_backup(backup_dir):`, `def restore_verified(backup_dir, restore_dir):`, `def test_restore_verify():`
**Valid input:** Source directory exists; backup directory is writable.
**Core:** Creates a backup with a per-file SHA-256 manifest. `verify_backup` checks every file's presence and hash; `restore_verified` only restores after verification succeeds.
**Assert:** Fresh backup verifies and restores correctly; corrupting `file1.txt` in the backup makes `verify_backup` raise with "hash mismatch", and `restore_verified` fails rather than restore corrupted data.
**⚠️ Defect:** `verify_backup` and `restore_verified` both walk `backup_dir/data` independently; a race between verification and restore could allow a file to be corrupted after verification but before copy. There is no checksum verification of the restored copy itself.

---
*△ AURA Pattern Library — © Reality Optimizer*
