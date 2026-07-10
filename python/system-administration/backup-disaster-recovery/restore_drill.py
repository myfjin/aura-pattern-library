#!/usr/bin/env python3
"""restore_drill: regular restore tests to verify backup recoverability."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
import hashlib
import json
from pathlib import Path

def create_test_backup(src_dir, backup_dir, label):
    """Create labeled backup with checksums."""
    backup_path = Path(backup_dir) / label
    backup_path.mkdir(parents=True, exist_ok=True)

    checksums = {}
    for root, dirs, files in os.walk(src_dir):
        for fname in files:
            src_path = Path(root) / fname
            rel = src_path.relative_to(src_dir)
            dst_path = backup_path / rel
            dst_path.parent.mkdir(parents=True, exist_ok=True)

            content = src_path.read_bytes()
            dst_path.write_bytes(content)
            checksums[str(rel)] = hashlib.sha256(content).hexdigest()

    # Store checksums for verification
    with open(backup_path / "manifest.json", 'w') as f:
        json.dump({"label": label, "checksums": checksums}, f)

    return backup_path

def run_restore_drill(backup_dir, backup_label, drill_restore_dir):
    """Run restore drill: restore backup and verify integrity."""
    backup_path = Path(backup_dir) / backup_label

    with open(backup_path / "manifest.json", 'r') as f:
        metadata = json.load(f)
    checksums = metadata["checksums"]

    Path(drill_restore_dir).mkdir(parents=True, exist_ok=True)

    # Restore all files
    for root, dirs, files in os.walk(backup_path):
        for fname in files:
            if fname.startswith("."):
                continue
            src_path = Path(root) / fname
            rel = src_path.relative_to(backup_path)
            dst_path = Path(drill_restore_dir) / rel
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            dst_path.write_bytes(src_path.read_bytes())

    # Verify restored files
    restored_checksums = {}
    for root, dirs, files in os.walk(drill_restore_dir):
        for fname in files:
            src_path = Path(root) / fname
            rel = src_path.relative_to(drill_restore_dir)
            content_hash = hashlib.sha256(src_path.read_bytes()).hexdigest()
            restored_checksums[str(rel)] = content_hash

    # Compare
    mismatches = []
    for orig_rel, orig_hash in checksums.items():
        restored_hash = restored_checksums.get(orig_rel)
        if restored_hash != orig_hash:
            mismatches.append((orig_rel, orig_hash, restored_hash))

    if mismatches:
        raise AssertionError(f"Restore drill failed: {len(mismatches)} checksum mismatches")

    return True

def test_restore_drill():
    """Test: create multiple backups, run drills, verify all restore correctly."""
    with tempfile.TemporaryDirectory() as tmpdir:
        src = Path(tmpdir) / "src"
        src.mkdir()
        backup_base = Path(tmpdir) / "backups"

        # Create initial backup
        (src / "data1.txt").write_text("data_payload_v1")
        (src / "subdir").mkdir()
        (src / "subdir" / "nested.txt").write_text("nested_payload_v1")

        backup1 = create_test_backup(src, backup_base, "backup_2026_01_01")
        assert backup1.exists(), "Backup 1 should exist"
        assert backup1.is_dir(), "Backup 1 should be directory"

        # Modify data and create second backup
        (src / "data1.txt").write_text("data_payload_v2")
        (src / "subdir" / "nested.txt").write_text("nested_payload_v2")
        (src / "data2.txt").write_text("new_data_payload")

        backup2 = create_test_backup(src, backup_base, "backup_2026_01_02")
        assert backup2.exists(), "Backup 2 should exist"

        # Modify again and create third backup
        (src / "data1.txt").write_text("data_payload_v3")
        (src / "data3.txt").write_text("third_data_payload")

        backup3 = create_test_backup(src, backup_base, "backup_2026_01_03")
        assert backup3.exists(), "Backup 3 should exist"

        # Run restore drills on each backup
        drill1_dir = Path(tmpdir) / "drill1"
        assert run_restore_drill(backup_base, "backup_2026_01_01", drill1_dir), "Drill 1 should pass"
        assert (drill1_dir / "data1.txt").read_text() == "data_payload_v1"
        assert (drill1_dir / "subdir" / "nested.txt").read_text() == "nested_payload_v1"
        assert not (drill1_dir / "data2.txt").exists()
        assert not (drill1_dir / "data3.txt").exists()

        drill2_dir = Path(tmpdir) / "drill2"
        assert run_restore_drill(backup_base, "backup_2026_01_02", drill2_dir), "Drill 2 should pass"
        assert (drill2_dir / "data1.txt").read_text() == "data_payload_v2"
        assert (drill2_dir / "data2.txt").read_text() == "new_data_payload"
        assert not (drill2_dir / "data3.txt").exists()

        drill3_dir = Path(tmpdir) / "drill3"
        assert run_restore_drill(backup_base, "backup_2026_01_03", drill3_dir), "Drill 3 should pass"
        assert (drill3_dir / "data1.txt").read_text() == "data_payload_v3"
        assert (drill3_dir / "data3.txt").read_text() == "third_data_payload"

        # Test drill failure: corrupt backup before drill
        corrupted_file = backup2 / "data2.txt"
        corrupted_file.write_text("CORRUPTED_BY_ATTACKER")

        drill_bad_dir = Path(tmpdir) / "drill_bad"
        try:
            run_restore_drill(backup_base, "backup_2026_01_02", drill_bad_dir)
            assert False, "Drill should have failed on corrupted backup"
        except AssertionError as e:
            assert "mismatch" in str(e).lower(), f"Expected mismatch error, got: {e}"

if __name__ == "__main__":
    test_restore_drill()
    print("✓ restore_drill passed")
