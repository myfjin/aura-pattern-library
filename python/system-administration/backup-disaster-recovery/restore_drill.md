# restore drill

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 13 · Backup & disaster recovery

**Signature:** `(backup_dir: Path, backup_label: str, drill_restore_dir: Path) → ?`

## What it does

restore_drill: regular restore tests to verify backup recoverability.

## Guarantee

When it runs, restore drill guarantees backup1.exists(); backup1.is_dir(); backup2.exists() (weak-grade: directional, proven by run).

**Checkable constraints:**

- `backup1.exists()`
- `backup1.is_dir()`
- `backup2.exists()`
- `backup3.exists()`
- `run_restore_drill(backup_base, 'backup_2026_01_01', drill1_dir)`
- `(drill1_dir / 'data1.txt').read_text() == 'data_payload_v1'`
- `(drill1_dir / 'subdir' / 'nested.txt').read_text() == 'nested_payload_v1'`
- `not (drill1_dir / 'data2.txt').exists()`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def create_test_backup(src_dir, backup_dir, label):`, `def run_restore_drill(backup_dir, backup_label, drill_restore_dir):`, `def test_restore_drill():`
**Valid input:** Source directory exists; backup label is unique; backup contains a `manifest.json` with per-file checksums.
**Core:** Creates labeled backups with checksum manifests and runs a restore drill: restores the backup to a fresh directory and verifies every restored file matches its original checksum.
**Assert:** Drills for three backups restore the correct point-in-time content; corrupting a file in a backup before the drill causes checksum mismatch and a failed drill.
**⚠️ Defect:** `run_restore_drill` copies dotfiles by skipping only `fname.startswith(".")`, but the manifest itself (`manifest.json`) is also a regular file and gets restored into the drill directory, polluting the restore. Restored file paths are reconstructed by `relative_to(backup_path)`, which fails if the backup contains absolute-symlink-like structures.

---
*△ AURA Pattern Library — © Reality Optimizer*
