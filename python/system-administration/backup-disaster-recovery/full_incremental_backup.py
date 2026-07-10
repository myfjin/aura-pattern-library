#!/usr/bin/env python3
"""full_incremental_backup: multi-level backup with change detection."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
import hashlib
import json
from pathlib import Path

def compute_checksum(path):
    """SHA256 of file contents."""
    sha = hashlib.sha256()
    with open(path, 'rb') as f:
        sha.update(f.read())
    return sha.hexdigest()

def backup_full(src_dir, backup_dir):
    """Create full backup of all files in src_dir to backup_dir/level0/."""
    level0 = Path(backup_dir) / "level0"
    level0.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for root, dirs, files in os.walk(src_dir):
        for fname in files:
            src_path = Path(root) / fname
            rel = src_path.relative_to(src_dir)
            dst_path = level0 / rel
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            with open(src_path, 'rb') as s, open(dst_path, 'wb') as d:
                d.write(s.read())
            manifest[str(rel)] = compute_checksum(dst_path)
    with open(level0 / ".manifest.json", 'w') as f:
        json.dump(manifest, f)
    return manifest

def backup_incremental(src_dir, backup_dir, level_num, last_manifest):
    """Create incremental backup: only files changed since last_manifest."""
    inc_dir = Path(backup_dir) / f"level{level_num}"
    inc_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}
    current = {}
    for root, dirs, files in os.walk(src_dir):
        for fname in files:
            src_path = Path(root) / fname
            rel = src_path.relative_to(src_dir)
            current[str(rel)] = compute_checksum(src_path)

    for rel, cur_hash in current.items():
        prev_hash = last_manifest.get(rel)
        if prev_hash != cur_hash:
            src_path = Path(src_dir) / rel
            dst_path = inc_dir / rel
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            with open(src_path, 'rb') as s, open(dst_path, 'wb') as d:
                d.write(s.read())
            manifest[str(rel)] = cur_hash

    with open(inc_dir / ".manifest.json", 'w') as f:
        json.dump(manifest, f)
    return current, manifest

def restore_from_backup(backup_dir, restore_dir):
    """Restore from level0 + all incremental levels in order."""
    Path(restore_dir).mkdir(parents=True, exist_ok=True)

    for level_dir in sorted(Path(backup_dir).glob("level*")):
        manifest_file = level_dir / ".manifest.json"
        if not manifest_file.exists():
            continue
        for root, dirs, files in os.walk(level_dir):
            for fname in files:
                if fname.startswith("."):
                    continue
                src_path = Path(root) / fname
                rel = src_path.relative_to(level_dir)
                dst_path = Path(restore_dir) / rel
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                with open(src_path, 'rb') as s, open(dst_path, 'wb') as d:
                    d.write(s.read())

def test_full_incremental_backup():
    """Test: create files, full backup, modify, incremental backup, corrupt, restore, verify."""
    with tempfile.TemporaryDirectory() as tmpdir:
        src = Path(tmpdir) / "src"
        src.mkdir()
        backup_base = Path(tmpdir) / "backup"
        restore_base = Path(tmpdir) / "restore"

        # Write initial files
        (src / "file1.txt").write_text("content1")
        (src / "file2.txt").write_text("content2")
        original_hashes = {
            "file1.txt": compute_checksum(src / "file1.txt"),
            "file2.txt": compute_checksum(src / "file2.txt"),
        }

        # Full backup
        manifest0 = backup_full(src, backup_base)
        assert len(manifest0) == 2, f"Expected 2 files in full backup, got {len(manifest0)}"

        # Modify one file, delete source
        (src / "file1.txt").write_text("content1_modified")
        (src / "file3.txt").write_text("content3")
        current, manifest1 = backup_incremental(src, backup_base, 1, manifest0)
        assert "file1.txt" in manifest1, "Modified file1.txt not in incremental"
        assert "file3.txt" in manifest1, "New file3.txt not in incremental"

        # Corrupt/delete source completely
        import shutil
        shutil.rmtree(src)

        # Restore from backup
        restore_from_backup(backup_base, restore_base)

        # Verify restored files match original (first backup's state)
        restored_file1 = (restore_base / "file1.txt").read_text()
        restored_file2 = (restore_base / "file2.txt").read_text()
        restored_file3 = (restore_base / "file3.txt").read_text()

        assert restored_file2 == "content2", f"file2 mismatch: {restored_file2}"
        assert restored_file3 == "content3", "file3 should be latest from incremental"
        assert restored_file1 == "content1_modified", "file1 should be latest from incremental"

        # Verify checksums exactly
        restored_hash1 = compute_checksum(restore_base / "file1.txt")
        expected_hash1 = current["file1.txt"]
        assert len(restored_hash1) == 64, f"SHA256 hash must be 64 chars, got {len(restored_hash1)}"
        assert restored_hash1 == expected_hash1, f"file1 hash mismatch: {restored_hash1} vs {expected_hash1}"

if __name__ == "__main__":
    test_full_incremental_backup()
    print("✓ full_incremental_backup passed")
