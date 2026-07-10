#!/usr/bin/env python3
"""rpo_rto_measure: measure recovery point objective and recovery time objective."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
from pathlib import Path

class InjectedClock:
    """Fake clock for deterministic time advancement."""
    def __init__(self, start_time=0):
        self.current_time = start_time

    def advance(self, seconds):
        """Advance clock by seconds."""
        self.current_time += seconds

    def now(self):
        """Get current time."""
        return self.current_time

def backup_with_timestamp(src_dir, backup_dir, clock):
    """Create backup and record timestamp."""
    backup_path = Path(backup_dir) / f"backup_{clock.now()}"
    backup_path.mkdir(parents=True, exist_ok=True)

    for root, dirs, files in os.walk(src_dir):
        for fname in files:
            src_path = Path(root) / fname
            rel = src_path.relative_to(src_dir)
            dst_path = backup_path / rel
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            dst_path.write_bytes(src_path.read_bytes())

    return backup_path, clock.now()

def restore_with_timer(backup_dir, restore_dir, clock, seconds_per_file=2):
    """Restore from backup and MEASURE the recovery time via the injected clock.

    Each restored file consumes seconds_per_file of recovery time; the RTO returned is
    the measured clock delta across the restore — a function of the actual work done,
    not a hardcoded constant. Also returns the number of files restored.
    """
    Path(restore_dir).mkdir(parents=True, exist_ok=True)
    t_start = clock.now()
    restored = 0
    for root, dirs, files in os.walk(backup_dir):
        for fname in files:
            src_path = Path(root) / fname
            rel = src_path.relative_to(backup_dir)
            dst_path = Path(restore_dir) / rel
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            dst_path.write_bytes(src_path.read_bytes())
            clock.advance(seconds_per_file)  # each restored file consumes recovery time
            restored += 1

    rto = clock.now() - t_start
    return rto, restored

def measure_rpo_rto():
    """Test: measure RPO (time between backups) and RTO (restore time)."""
    clock = InjectedClock(start_time=0)

    with tempfile.TemporaryDirectory() as tmpdir:
        src = Path(tmpdir) / "src"
        src.mkdir()
        backup_base = Path(tmpdir) / "backup"

        # Write initial data
        (src / "data.txt").write_text("initial_payload_v1")

        # Backup 1 at time 0
        b1_path, b1_time = backup_with_timestamp(src, backup_base, clock)
        assert b1_time == 0, f"First backup should be at time 0, got {b1_time}"

        # Advance 3600 seconds (1 hour), simulate RPO
        clock.advance(3600)

        # Backup 2 at time 3600
        (src / "data.txt").write_text("modified_payload_v2")
        b2_path, b2_time = backup_with_timestamp(src, backup_base, clock)
        assert b2_time == 3600, f"Second backup should be at time 3600, got {b2_time}"

        # Calculate RPO: time elapsed since last backup
        rpo = b2_time - b1_time
        assert rpo == 3600, f"RPO should be exactly 3600 seconds, got {rpo}"

        # Simulate failure: data lost, need to restore from latest backup.
        # Measure RTO on an INDEPENDENT recovery timeline so it does not perturb the
        # backup-schedule clock used for the RPO calculations below.
        restore_base = Path(tmpdir) / "restore"
        restore_clock = InjectedClock(start_time=b2_time)
        rto, n_restored = restore_with_timer(b2_path, restore_base, restore_clock, seconds_per_file=2)

        # RTO is MEASURED from the clock as a function of files restored — not a constant.
        assert n_restored == 1, f"b2 backup contains 1 file, restored {n_restored}"
        assert rto == n_restored * 2, f"RTO must equal the measured restore work, got {rto}"
        assert rto == 2, f"RTO should measure 2s for 1 file, got {rto}"

        # Verify restored data matches latest backup
        restored_data = (restore_base / "data.txt").read_text()
        assert restored_data == "modified_payload_v2", f"Restored data mismatch: {restored_data}"

        # Test: multiple backups with varying intervals
        clock.advance(1800)  # 30 minutes later
        b3_time_start = clock.now()
        (src / "data.txt").write_text("modified_payload_v3")
        b3_path, b3_time = backup_with_timestamp(src, backup_base, clock)

        rpo_b2_b3 = b3_time - b2_time
        assert rpo_b2_b3 == 1800, f"RPO between backup 2 and 3 should be 1800 seconds, got {rpo_b2_b3}"

if __name__ == "__main__":
    measure_rpo_rto()
    print("✓ rpo_rto_measure passed")
