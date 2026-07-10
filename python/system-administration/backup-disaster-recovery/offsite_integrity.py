#!/usr/bin/env python3
"""offsite_integrity: verify offsite backup integrity via remote checksums."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
import hashlib
import json
from pathlib import Path

def create_offsite_backup(src_dir, offsite_dir):
    """Create offsite backup and generate checksums for verification."""
    offsite_path = Path(offsite_dir) / "offsite"
    offsite_path.mkdir(parents=True, exist_ok=True)

    checksums = {}
    for root, dirs, files in os.walk(src_dir):
        for fname in files:
            src_path = Path(root) / fname
            rel = src_path.relative_to(src_dir)
            dst_path = offsite_path / rel
            dst_path.parent.mkdir(parents=True, exist_ok=True)

            content = src_path.read_bytes()
            dst_path.write_bytes(content)
            checksums[str(rel)] = hashlib.sha256(content).hexdigest()

    # Store checksums in a separate "remote" file (simulating remote transmission)
    with open(Path(offsite_dir) / "checksums.json", 'w') as f:
        json.dump(checksums, f)

    return checksums

def verify_offsite_integrity(offsite_dir):
    """Verify local offsite copy against stored checksums (simulating remote check)."""
    with open(Path(offsite_dir) / "checksums.json", 'r') as f:
        stored_checksums = json.load(f)

    offsite_path = Path(offsite_dir) / "offsite"
    mismatches = []

    for rel_path, expected_hash in stored_checksums.items():
        file_path = offsite_path / rel_path
        if not file_path.exists():
            mismatches.append((rel_path, "missing"))
            continue

        actual_hash = hashlib.sha256(file_path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            mismatches.append((rel_path, f"hash mismatch: {actual_hash} vs {expected_hash}"))

    if mismatches:
        raise ValueError(f"Offsite integrity check failed: {mismatches}")

    return True

def test_offsite_integrity():
    """Test: create offsite backup, verify integrity, corrupt, detect tampering."""
    with tempfile.TemporaryDirectory() as tmpdir:
        src = Path(tmpdir) / "src"
        src.mkdir()
        offsite_base = Path(tmpdir) / "offsite"

        # Create source files
        (src / "important1.dat").write_bytes(b"critical_data_001")
        (src / "important2.dat").write_bytes(b"critical_data_002")
        (src / "config.json").write_text('{"version": 1}')

        # Create offsite backup
        checksums = create_offsite_backup(src, offsite_base)
        assert len(checksums) == 3, f"Expected exactly 3 files, got {len(checksums)}"
        for fkey in ["important1.dat", "important2.dat", "config.json"]:
            assert fkey in checksums, f"Missing {fkey} in checksum manifest"

        # Verify integrity passes
        assert verify_offsite_integrity(offsite_base), "Fresh offsite backup should verify"

        # Simulate network tampering: corrupt a file in offsite
        offsite_path = Path(offsite_base) / "offsite"
        (offsite_path / "important1.dat").write_bytes(b"CORRUPTED_BY_ATTACKER")

        # Verify should FAIL
        try:
            verify_offsite_integrity(offsite_base)
            assert False, "Verification should have failed on corrupted offsite backup"
        except ValueError as e:
            assert "hash mismatch" in str(e), f"Expected hash mismatch error, got: {e}"

        # Restore checksums for next test
        create_offsite_backup(src, offsite_base)

        # Simulate bit-flip: flip one byte in important2.dat
        offsite_path = Path(offsite_base) / "offsite"
        data = bytearray((offsite_path / "important2.dat").read_bytes())
        data[0] ^= 0xFF  # Flip bits in first byte
        (offsite_path / "important2.dat").write_bytes(bytes(data))

        # Verify should FAIL
        try:
            verify_offsite_integrity(offsite_base)
            assert False, "Verification should have detected bit-flip"
        except ValueError as e:
            assert "hash mismatch" in str(e) or "mismatch" in str(e).lower(), f"Expected mismatch error, got: {e}"

        # Test: missing file in offsite
        create_offsite_backup(src, offsite_base)
        (offsite_path / "important1.dat").unlink()

        try:
            verify_offsite_integrity(offsite_base)
            assert False, "Verification should have detected missing file"
        except ValueError as e:
            assert "missing" in str(e).lower(), f"Expected missing file error, got: {e}"

if __name__ == "__main__":
    test_offsite_integrity()
    print("✓ offsite_integrity passed")
