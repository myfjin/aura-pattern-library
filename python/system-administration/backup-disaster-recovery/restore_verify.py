#!/usr/bin/env python3
"""restore_verify: verify backup integrity, fail on tampering."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
import hashlib
import json
from pathlib import Path

def create_backup_with_manifest(src_dir, backup_dir):
    """Create backup and manifest with per-file checksums."""
    backup_path = Path(backup_dir) / "data"
    backup_path.mkdir(parents=True, exist_ok=True)
    manifest = {}

    for root, dirs, files in os.walk(src_dir):
        for fname in files:
            src_path = Path(root) / fname
            rel = src_path.relative_to(src_dir)
            dst_path = backup_path / rel
            dst_path.parent.mkdir(parents=True, exist_ok=True)

            content = src_path.read_bytes()
            dst_path.write_bytes(content)

            manifest[str(rel)] = hashlib.sha256(content).hexdigest()

    with open(Path(backup_dir) / "manifest.json", 'w') as f:
        json.dump(manifest, f)
    return manifest

def verify_backup(backup_dir):
    """Verify backup against manifest. Raise ValueError if any file is tampered."""
    with open(Path(backup_dir) / "manifest.json", 'r') as f:
        manifest = json.load(f)

    backup_path = Path(backup_dir) / "data"
    for rel_path, expected_hash in manifest.items():
        file_path = backup_path / rel_path
        if not file_path.exists():
            raise ValueError(f"Missing file in backup: {rel_path}")

        actual_hash = hashlib.sha256(file_path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            raise ValueError(f"Backup corrupted: {rel_path} hash mismatch (expected {expected_hash}, got {actual_hash})")

    return True

def restore_verified(backup_dir, restore_dir):
    """Restore backup only if verification passes."""
    verify_backup(backup_dir)  # Will raise if verification fails

    Path(restore_dir).mkdir(parents=True, exist_ok=True)
    backup_path = Path(backup_dir) / "data"

    for root, dirs, files in os.walk(backup_path):
        for fname in files:
            src_path = Path(root) / fname
            rel = src_path.relative_to(backup_path)
            dst_path = Path(restore_dir) / rel
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            dst_path.write_bytes(src_path.read_bytes())

    return True

def test_restore_verify():
    """Test: create backup, verify integrity, corrupt backup, verify fails."""
    with tempfile.TemporaryDirectory() as tmpdir:
        src = Path(tmpdir) / "src"
        src.mkdir()
        backup_base = Path(tmpdir) / "backup"
        restore_base = Path(tmpdir) / "restore"

        # Create source files
        (src / "file1.txt").write_text("content1_payload")
        (src / "file2.txt").write_text("content2_payload")

        # Create backup with manifest
        manifest = create_backup_with_manifest(src, backup_base)
        assert len(manifest) == 2, f"Expected exactly 2 files in manifest, got {len(manifest)}"
        assert "file1.txt" in manifest and "file2.txt" in manifest, "Should have both files"

        # Verify backup passes
        assert verify_backup(backup_base), "Fresh backup should verify"

        # Restore from verified backup
        restore_verified(backup_base, restore_base)
        assert (restore_base / "file1.txt").read_text() == "content1_payload"
        assert (restore_base / "file2.txt").read_text() == "content2_payload"

        # Corrupt one file in the backup
        backup_data = Path(backup_base) / "data"
        corrupted_file = backup_data / "file1.txt"
        corrupted_file.write_text("CORRUPTED_CONTENT_X")

        # Verify should now FAIL
        try:
            verify_backup(backup_base)
            assert False, "Verification should have failed on corrupted backup"
        except ValueError as e:
            assert "hash mismatch" in str(e).lower(), f"Expected hash mismatch error, got: {e}"

        # Restore from corrupted backup should also FAIL
        restore_base2 = Path(tmpdir) / "restore2"
        try:
            restore_verified(backup_base, restore_base2)
            assert False, "Restore from corrupted backup should have failed"
        except ValueError as e:
            assert "corrupted" in str(e).lower() or "mismatch" in str(e).lower(), f"Expected corruption error, got: {e}"

if __name__ == "__main__":
    test_restore_verify()
    print("✓ restore_verify passed")
