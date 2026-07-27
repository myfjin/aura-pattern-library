# offsite integrity

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 13 · Backup & disaster recovery

**Signature:** `(offsite_dir: Path) → ?`

## What it does

offsite_integrity: verify offsite backup integrity via remote checksums.

## Guarantee

When it runs, offsite integrity guarantees fkey in checksums; verify_offsite_integrity(offsite_base); 'hash mismatch' in str(e) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(checksums) == 3`
- `fkey in checksums`
- `verify_offsite_integrity(offsite_base)`
- `'hash mismatch' in str(e)`
- `'hash mismatch' in str(e) or 'mismatch' in str(e).lower()`
- `'missing' in str(e).lower()`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def create_offsite_backup(src_dir, offsite_dir):`, `def verify_offsite_integrity(offsite_dir):`, `def test_offsite_integrity():`
**Valid input:** Source directory contains files; `offsite_dir` is writable; `offsite_dir/checksums.json` exists after backup creation.
**Core:** Creates a local copy simulating an offsite backup and stores per-file SHA-256 checksums. Verification compares the offsite copy against the stored checksums and raises `ValueError` on missing files or hash mismatches.
**Assert:** Fresh offsite copy verifies; replacing a file with `CORRUPTED_BY_ATTACKER`, flipping a byte, or deleting a file are all detected with "hash mismatch" or "missing".
**⚠️ Defect:** Checksums are stored alongside the offsite copy in the same directory tree, so an attacker with access to the offsite store can recompute and replace checksums after tampering. There is no separation of checksums to a truly remote/trusted location.

---
*△ AURA Pattern Library — © Reality Optimizer*
