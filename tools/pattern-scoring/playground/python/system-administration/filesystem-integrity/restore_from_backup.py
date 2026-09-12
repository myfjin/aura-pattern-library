"""
restore_from_backup: restore a file from backup after corruption/deletion.
Failure simulated: backup a file; delete/corrupt the original; restore from backup;
assert the original is recovered to exact byte-for-byte match.
Recovery asserted: restored file == backed-up file; no data loss; corruption is undone.
Pattern's own restore function is called, not the test scaffold.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import tempfile
import sys
import shutil
from pathlib import Path


def create_backup(source_path, backup_path):
    """Create a backup by copying source to backup."""
    source_data = Path(source_path).read_bytes()
    fd, temp_path = tempfile.mkstemp(dir=os.path.dirname(backup_path) or ".")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(source_data)
        os.rename(temp_path, backup_path)
    except:
        try:
            os.unlink(temp_path)
        except:
            pass
        raise


def restore_from_backup(backup_path, target_path):
    """Restore target_path from backup_path (overwrites target)."""
    backup_data = Path(backup_path).read_bytes()
    fd, temp_path = tempfile.mkstemp(dir=os.path.dirname(target_path) or ".")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(backup_data)
        os.rename(temp_path, target_path)
    except:
        try:
            os.unlink(temp_path)
        except:
            pass
        raise


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    source = os.path.join(tmpdir, "source.dat")
    backup = os.path.join(tmpdir, "backup.dat")

    # Seed: deterministic test data
    expected_original = b"restore_original_" + (b"z" * 4096)
    expected_corrupted = b"corrupted_" + (b"X" * 2048)

    # Write original and back it up
    Path(source).write_bytes(expected_original)
    create_backup(source, backup)

    # Verify backup is correct
    assert Path(backup).read_bytes() == expected_original, "backup is corrupted"

    # FAILURE SIM: corrupt the original file
    Path(source).write_bytes(expected_corrupted)

    # Verify corruption
    assert Path(source).read_bytes() != expected_original, "source not corrupted (test setup)"
    assert Path(source).read_bytes() == expected_corrupted, "source is wrong corrupted data"

    # FAILURE SIM: restore from backup
    restore_from_backup(backup, source)

    # RECOVERY assert 1: source is now restored to original bytes
    result = Path(source).read_bytes()
    assert result == expected_original, f"restored data != original: {result[:50]!r}"

    # RECOVERY assert 2: restored size matches original exactly
    assert len(result) == len(expected_original), \
        f"restored size {len(result)} != original {len(expected_original)}"

    # RECOVERY assert 3: no partial or truncated restore
    assert result[:17] == b"restore_original_", f"restored header wrong: {result[:17]!r}"
    assert result[-1:] == expected_original[-1:], f"restored tail wrong"

    # RECOVERY assert 4: restored != corrupted (data is truly recovered, not still corrupt)
    assert result != expected_corrupted, f"restore failed: still holds corrupted data"

    # RECOVERY assert 5: byte-by-byte match (use a random sample to avoid exact comparison overhead)
    import random
    random.seed(42)
    sample_indices = random.sample(range(len(expected_original)), min(20, len(expected_original)))
    for idx in sample_indices:
        assert result[idx] == expected_original[idx], \
            f"byte mismatch at {idx}: {result[idx]:02x} != {expected_original[idx]:02x}"

    # Clean up
    shutil.rmtree(tmpdir)

    print(f"restore_from_backup: original={len(expected_original)}, restored={len(result)}, corrupted={len(expected_corrupted)}")
    print("restore_from_backup PASS")
    sys.exit(0)
