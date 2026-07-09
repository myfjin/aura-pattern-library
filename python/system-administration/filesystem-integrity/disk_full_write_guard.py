"""
disk_full_write_guard: refuse writes when disk space is exhausted or quota exceeded.
Failure simulated: attempt to write past disk quota; guard should refuse; existing
data remains intact. Guard trips BEFORE exhaustion, not after.
Recovery asserted: write is blocked when it would exceed quota; existing data untouched;
no partial/torn writes. Pattern's own guard function is called.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import tempfile
import sys
from pathlib import Path


class QuotaGuard:
    """
    A simple quota guard: tracks bytes written and refuses writes that exceed quota.
    """
    def __init__(self, quota_bytes):
        self.quota = quota_bytes
        self.used = 0

    def write_file(self, path, content):
        """
        Write content to path, but refuse if it would exceed quota.
        Returns True on success, raises ValueError on quota exceeded.
        """
        content_size = len(content)
        if self.used + content_size > self.quota:
            raise ValueError(f"quota exceeded: {self.used} + {content_size} > {self.quota}")

        # Write to temp, then rename (atomic)
        import tempfile
        fd, temp_path = tempfile.mkstemp(dir=os.path.dirname(path) or ".")
        try:
            with os.fdopen(fd, "wb") as f:
                f.write(content)
            os.rename(temp_path, path)
            self.used += content_size
            return True
        except:
            try:
                os.unlink(temp_path)
            except:
                pass
            raise

    def get_used(self):
        """Return bytes used."""
        return self.used

    def remaining(self):
        """Return bytes remaining."""
        return self.quota - self.used


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()

    # Seed: deterministic quota and data sizes
    expected_quota = 2048
    expected_file1_size = 512
    expected_file2_size = 768
    expected_file3_size = 768   # Total so far: 2048 (exactly full)
    expected_file4_size = 512   # Would exceed: 2048 + 512 > 2048

    guard = QuotaGuard(expected_quota)

    # FAILURE SIM 1: write file1 (within quota)
    file1_path = os.path.join(tmpdir, "file1.bin")
    file1_content = b"file1_" + (b"a" * (expected_file1_size - 6))
    guard.write_file(file1_path, file1_content)

    # RECOVERY assert 1: file1 written, quota updated
    assert Path(file1_path).exists(), "file1 not written"
    assert guard.get_used() == expected_file1_size, f"used count wrong: {guard.get_used()} != {expected_file1_size}"
    assert guard.remaining() == expected_quota - expected_file1_size, "remaining wrong"

    # FAILURE SIM 2: write file2 (within quota)
    file2_path = os.path.join(tmpdir, "file2.bin")
    file2_content = b"file2_" + (b"b" * (expected_file2_size - 6))
    guard.write_file(file2_path, file2_content)

    # RECOVERY assert 2: file2 written, quota updated
    assert Path(file2_path).exists(), "file2 not written"
    assert guard.get_used() == expected_file1_size + expected_file2_size, "used count wrong after file2"

    # FAILURE SIM 3: write file3 (exactly at quota boundary)
    file3_path = os.path.join(tmpdir, "file3.bin")
    file3_content = b"file3_" + (b"c" * (expected_file3_size - 6))
    guard.write_file(file3_path, file3_content)

    # RECOVERY assert 3: file3 written, quota exactly full
    assert Path(file3_path).exists(), "file3 not written"
    assert guard.get_used() == expected_quota, f"quota not full: {guard.get_used()} != {expected_quota}"
    assert guard.remaining() == 0, "remaining should be 0"

    # FAILURE SIM 4: attempt to write file4 (would exceed quota)
    file4_path = os.path.join(tmpdir, "file4.bin")
    file4_content = b"file4_" + (b"d" * (expected_file4_size - 6))

    try:
        guard.write_file(file4_path, file4_content)
        assert False, "guard did not refuse write past quota"
    except ValueError as e:
        assert "quota exceeded" in str(e), f"wrong error: {e}"

    # RECOVERY assert 4: file4 was not written (guard blocked it)
    assert not Path(file4_path).exists(), f"file4 exists but should have been blocked"

    # RECOVERY assert 5: used bytes unchanged (no partial write counted)
    assert guard.get_used() == expected_quota, f"used changed after blocked write: {guard.get_used()}"

    # RECOVERY assert 6: existing files are still intact
    assert Path(file1_path).read_bytes() == file1_content, "file1 corrupted"
    assert Path(file2_path).read_bytes() == file2_content, "file2 corrupted"
    assert Path(file3_path).read_bytes() == file3_content, "file3 corrupted"

    # RECOVERY assert 7: no temp files left behind from failed write
    all_files = os.listdir(tmpdir)
    expected_file_count = 3
    assert len(all_files) == expected_file_count, f"unexpected files in tmpdir: {all_files}"
    assert not any(f.startswith("tmp") for f in all_files), f"temp files leaked: {all_files}"

    # RECOVERY assert 8: guard state is consistent (no leaking counts)
    assert guard.remaining() == 0, "remaining should stay 0 after refused write"

    # Clean up
    import shutil
    shutil.rmtree(tmpdir)

    print(f"disk_full_write_guard: quota={expected_quota}, used={guard.get_used()}, refused_count=1")
    print("disk_full_write_guard PASS")
    sys.exit(0)
