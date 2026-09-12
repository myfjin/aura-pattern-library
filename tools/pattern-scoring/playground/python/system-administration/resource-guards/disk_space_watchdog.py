"""Disk space watchdog: refuses writes when available space < threshold.
Failure simulated: "fill" disk by tracking usage, attempt 1000 writes with cap=100MB;
assert guard refuses writes when available < cap, peak usage ≤ cap.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import tempfile
import os

def disk_space_watchdog(threshold_mb=100):
    """Guard that refuses writes when available disk space < threshold.
    Returns: context with can_write(), write_file(), peak_usage_bytes.
    """
    class DiskGuard:
        def __init__(self, threshold):
            self.threshold_bytes = threshold * 1024 * 1024
            self.used_bytes = 0
            self.peak_used = 0
            self.refused = 0
            self.tmpdir = tempfile.mkdtemp()
            self.written_files = []

        def available_space(self):
            """Bytes left under the guard's budget (the writes below consume real disk)."""
            return self.threshold_bytes - self.used_bytes

        def can_write(self, size_bytes):
            """Check if write would exceed threshold."""
            if self.available_space() < size_bytes:
                self.refused += 1
                return False
            return True

        def write_file(self, size_bytes):
            """Write a file if space allows; return True/False."""
            if not self.can_write(size_bytes):
                return False
            self.used_bytes += size_bytes
            self.peak_used = max(self.peak_used, self.used_bytes)
            # Create actual temp file to hold the space
            try:
                f = tempfile.NamedTemporaryFile(dir=self.tmpdir, delete=False)
                f.write(b'x' * size_bytes)  # FULL size — real disk bytes, not a 1 KB token
                f.close()
                self.written_files.append(f.name)
                return True
            except:
                return False

        def cleanup(self):
            """Remove temp files."""
            for fname in self.written_files:
                try:
                    os.unlink(fname)
                except:
                    pass
            try:
                os.rmdir(self.tmpdir)
            except:
                pass

    return DiskGuard(threshold_mb)

if __name__ == '__main__':
    import random
    random.seed(42)

    guard = disk_space_watchdog(threshold_mb=100)
    write_size = 1024 * 1024  # 1MB per write

    num_wrote = 0
    num_refused = 0

    try:
        # Try 1000 writes with 100MB cap
        for i in range(1000):
            if guard.write_file(write_size):
                num_wrote += 1
            else:
                num_refused += 1

        peak_mb = guard.peak_used / (1024 * 1024)

        # Assert: peak usage ≤ 100MB, guard refused 900+ of 1000 attempts
        assert peak_mb <= 100, f"Peak disk usage {peak_mb:.1f}MB exceeded cap 100MB"
        assert num_refused >= 900, f"Guard refused {num_refused}, expected ≥ 900 (out of 1000)"
        assert num_wrote <= 100, f"Wrote {num_wrote} files, should be ≤ 100"
        assert num_refused > num_wrote * 5, f"Refused {num_refused} << wrote {num_wrote}"

    finally:
        guard.cleanup()

    print(f"disk_space_watchdog: peak={peak_mb:.0f}MB wrote={num_wrote} refused={num_refused} PASS")
