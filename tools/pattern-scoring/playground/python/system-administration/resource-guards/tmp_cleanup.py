"""Tmp cleanup: auto-cleans temp files when usage exceeds quota.
Failure simulated: create files until 200MB used, auto-cleanup kicks at 150MB;
assert final size stays ≤ 150MB after cleanup + new creates, refused > 0.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import tempfile
import os
import time

def tmp_cleanup_guard(quota_mb=150, cleanup_target_mb=100):
    """Auto-cleanup temp files when quota exceeded.
    Returns: context with create_file(), cleanup(), current_usage_bytes.
    """
    class TmpCleanup:
        def __init__(self, quota, cleanup_target):
            self.quota_bytes = quota * 1024 * 1024
            self.cleanup_target_bytes = cleanup_target * 1024 * 1024
            self.tmpdir = tempfile.mkdtemp()
            self.files = {}  # fname -> (size, ctime)
            self.current_usage = 0
            self.cleanup_runs = 0
            self.refused = 0

        def create_file(self, size_bytes):
            """Create a file; trigger cleanup if quota exceeded."""
            if self.current_usage + size_bytes > self.quota_bytes:
                self.refused += 1
                # Trigger cleanup
                self.cleanup()
                # Retry after cleanup
                if self.current_usage + size_bytes > self.quota_bytes:
                    return False

            try:
                f = tempfile.NamedTemporaryFile(dir=self.tmpdir, delete=False)
                f.write(b'x' * size_bytes)  # FULL size — real disk usage
                f.close()
                self.files[f.name] = (size_bytes, time.time())
                self.current_usage += size_bytes
                return True
            except:
                return False

        def cleanup(self):
            """Remove oldest files until usage < cleanup_target."""
            self.cleanup_runs += 1
            sorted_files = sorted(self.files.items(), key=lambda x: x[1][1])
            for fname, (size, ctime) in sorted_files:
                if self.current_usage <= self.cleanup_target_bytes:
                    break
                try:
                    os.unlink(fname)
                    del self.files[fname]
                    self.current_usage -= size
                except:
                    pass

        def cleanup_all(self):
            """Remove all files."""
            for fname in list(self.files.keys()):
                try:
                    os.unlink(fname)
                except:
                    pass
            self.files.clear()
            self.current_usage = 0

    return TmpCleanup(quota_mb, cleanup_target_mb)

if __name__ == '__main__':
    import random
    random.seed(42)

    quota_mb, file_mb = 30, 3
    guard = tmp_cleanup_guard(quota_mb=quota_mb, cleanup_target_mb=20)
    file_size = file_mb * 1024 * 1024  # real bytes per file

    num_created = 0
    try:
        # Create files until we exceed quota; cleanup should auto-run
        for i in range(50):
            if guard.create_file(file_size):
                num_created += 1
            time.sleep(0.01)  # Small delay to ensure distinct ctimes

        final_usage_mb = guard.current_usage / (1024 * 1024)

        # Assert: final usage ≤ quota, cleanup ran and freed space
        # real disk usage stays under the quota
        assert final_usage_mb <= quota_mb, f"Final usage {final_usage_mb:.1f}MB exceeded quota {quota_mb}MB"
        assert guard.cleanup_runs >= 1 and guard.refused >= 1, \
            f"cleanup never triggered: runs={guard.cleanup_runs} refused={guard.refused}"
        # THE real test: cleanup FREED space, letting MORE files be created than the quota alone
        # allows (quota/file = 10). A no-op cleanup caps num_created at 10 → fails here.
        assert num_created > quota_mb // file_mb, \
            f"cleanup did not free space: created {num_created} <= {quota_mb // file_mb}"

    finally:
        guard.cleanup_all()

    print(f"tmp_cleanup: usage={final_usage_mb:.0f}MB created={num_created} cleanup_runs={guard.cleanup_runs} PASS")
