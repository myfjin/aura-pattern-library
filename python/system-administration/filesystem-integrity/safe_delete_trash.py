"""
safe_delete_trash: delete files to trash (not permanent deletion).
Failure simulated: delete a file via trash move; assert file is gone from original location
but recoverable from trash. Prevent permanent data loss via trash buffer.
Recovery asserted: file removed from source; file exists in trash; can be restored from trash.
Pattern's own delete-to-trash function is called.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import tempfile
import sys
import time
from pathlib import Path


def safe_delete_to_trash(file_path, trash_dir):
    """
    Delete file_path by moving it to trash_dir (safe delete, not permanent).
    """
    if not Path(file_path).exists():
        raise FileNotFoundError(f"{file_path} does not exist")
    if not Path(trash_dir).exists():
        os.makedirs(trash_dir, exist_ok=True)

    # Use a timestamped trash name to avoid collisions
    basename = os.path.basename(file_path)
    timestamp = str(int(time.time() * 1000000))  # microseconds
    trash_name = f"{timestamp}_{basename}"
    trash_path = os.path.join(trash_dir, trash_name)

    os.rename(file_path, trash_path)
    return trash_path


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    source_file = os.path.join(tmpdir, "important.dat")
    trash_dir = os.path.join(tmpdir, "trash")

    # Seed: deterministic test data
    expected_content = b"safe_delete_test_content_" + (b"d" * 2048)

    # Write file
    Path(source_file).write_bytes(expected_content)
    assert Path(source_file).exists(), "source file not created"

    # FAILURE SIM: delete to trash
    trash_path = safe_delete_to_trash(source_file, trash_dir)

    # RECOVERY assert 1: file is gone from original location
    assert not Path(source_file).exists(), f"file still in original location: {source_file}"

    # RECOVERY assert 2: file exists in trash
    assert Path(trash_path).exists(), f"file not in trash: {trash_path}"

    # RECOVERY assert 3: trash file contains original data
    result = Path(trash_path).read_bytes()
    assert result == expected_content, f"trash file corrupted: {result[:50]!r}"

    # RECOVERY assert 4: trash directory has exactly one file (the deleted one)
    trash_files = os.listdir(trash_dir)
    assert len(trash_files) == 1, f"trash has wrong file count: {trash_files}"
    assert trash_files[0] == os.path.basename(trash_path), f"trash filename mismatch"

    # RECOVERY assert 5: can recover from trash (restore)
    recovered_path = os.path.join(tmpdir, "recovered.dat")
    os.rename(trash_path, recovered_path)
    recovered_result = Path(recovered_path).read_bytes()
    assert recovered_result == expected_content, "recovery from trash failed"

    # RECOVERY assert 6: trash is now empty
    assert len(os.listdir(trash_dir)) == 0, "trash not empty after recovery"

    # Clean up
    import shutil
    shutil.rmtree(tmpdir)

    # NOTE: the trash filename carries a microsecond timestamp (collision-avoidance) — do NOT
    # print it, so stdout stays deterministic across runs (the logic already is).
    print(f"safe_delete_trash: original_size={len(expected_content)}, recovered_size={len(recovered_result)}, trash_now_empty=True")
    print("safe_delete_trash PASS")
    sys.exit(0)
