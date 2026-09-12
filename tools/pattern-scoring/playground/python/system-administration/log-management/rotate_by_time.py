#!/usr/bin/env python3
"""Rotate logs by time: age past the retention window, assert old files are pruned.
Failure simulated: a fake logical clock ages rotated files well past the window.
Defended outcome: every file older than keep_duration is deleted; a no-op keeps them → fails.
NOTE: rotated files are stamped with the FAKE time via os.utime, so the prune comparison and
the age assert live on ONE clock (mixing fake time with real ~1.7e9 mtimes made this vacuous).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os, tempfile, pathlib, glob


def rotate_by_time(log_path, rotation_interval_sec=5, keep_duration_sec=10):
    """Rotate at intervals; prune files whose (logical) mtime is older than keep_duration."""
    log_file = pathlib.Path(log_path)
    last_rotation = [0.0]

    def append_line(text, now):
        if now - last_rotation[0] > rotation_interval_sec:
            rotated = pathlib.Path(f"{log_path}.{int(last_rotation[0])}")
            log_file.rename(rotated)
            os.utime(rotated, (last_rotation[0], last_rotation[0]))   # stamp on the fake clock
            log_file.touch()
            last_rotation[0] = now
            # prune rotated files older than the window (all on the fake clock)
            for fpath in glob.glob(f"{log_path}.*"):
                if os.path.getmtime(fpath) < now - keep_duration_sec:
                    os.unlink(fpath)
        log_file.write_text(log_file.read_text() + text + "\n")
        os.utime(log_file, (now, now))                               # current log = now (fake)

    return append_line


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        log_path = os.path.join(tmpdir, "test.log")
        pathlib.Path(log_path).touch()

        interval, keep_window = 5, 30
        append_line = rotate_by_time(log_path, rotation_interval_sec=interval, keep_duration_sec=keep_window)

        # Age entries across the fake timeline t=0,5,...,25 → rotations accumulate (all within the
        # 30s window, so none pruned yet).
        for t in range(0, 30, interval):
            append_line("line", now=float(t))

        rotated_before = [f for f in glob.glob(f"{log_path}.*")]
        assert len(rotated_before) >= 2, f"setup: expected rotations to accumulate, got {rotated_before}"

        # Jump far past the window and write once → this prune must delete everything aged out.
        now = 100.0
        append_line("line", now=now)

        # RECOVERY assert 1 (real prune): NO surviving file is older than the window. Every mtime
        # is on the fake clock, so age is meaningful. A no-op prune leaves mtimes 0..25 → age ~75-100
        # → FAILS here.
        survivors = [f for f in glob.glob(f"{log_path}*") if os.path.isfile(f)]
        for fpath in survivors:
            age = now - os.path.getmtime(fpath)
            assert age <= keep_window, f"{os.path.basename(fpath)} aged {age} > window {keep_window} (not pruned)"

        # RECOVERY assert 2: the current log survived, and the aged rotated files are gone.
        assert os.path.exists(log_path), "current log was pruned"
        assert not glob.glob(f"{log_path}.[0-9]*"), "aged rotated files were not pruned"

        print("PASS")
