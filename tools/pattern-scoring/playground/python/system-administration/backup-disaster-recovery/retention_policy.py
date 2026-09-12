#!/usr/bin/env python3
"""retention_policy: implement backup retention rules (age-based, count-based)."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
from pathlib import Path

class InjectedClock:
    """Fake clock for deterministic time."""
    def __init__(self, start_time=0):
        self.current_time = start_time

    def advance(self, seconds):
        self.current_time += seconds

    def now(self):
        return self.current_time

def create_backup(backup_dir, backup_id, clock):
    """Create backup with timestamp."""
    backup_path = Path(backup_dir) / f"backup_{backup_id}"
    backup_path.mkdir(parents=True, exist_ok=True)

    # Store timestamp (fake clock time)
    (backup_path / "timestamp.txt").write_text(str(clock.now()))
    (backup_path / "data.txt").write_text(f"backup_{backup_id}_content")

    return backup_path

def apply_retention_policy(backup_dir, policy_config, clock):
    """Apply retention policy: keep backups based on age and count rules."""
    # policy_config: {"max_age_seconds": int, "min_count": int}
    max_age = policy_config.get("max_age_seconds", float('inf'))
    min_count = policy_config.get("min_count", 1)

    backup_entries = []
    for backup_path in sorted(Path(backup_dir).glob("backup_*")):
        if not backup_path.is_dir():
            continue

        timestamp_file = backup_path / "timestamp.txt"
        if timestamp_file.exists():
            timestamp = int(timestamp_file.read_text().strip())
            age = clock.now() - timestamp
            backup_entries.append((backup_path, timestamp, age))

    # Sort by timestamp (newest first)
    backup_entries.sort(key=lambda x: x[1], reverse=True)

    deleted = []
    kept = []

    for i, (backup_path, timestamp, age) in enumerate(backup_entries):
        # Keep if:
        # 1. This is one of the newest min_count backups, OR
        # 2. Age is within max_age (unless max_age is infinite, then only respect min_count)

        is_in_min_count = i < min_count

        # Only check age if it's finite
        if max_age == float('inf'):
            should_keep = is_in_min_count
        else:
            is_within_age = age <= max_age
            should_keep = is_in_min_count or is_within_age

        if should_keep:
            kept.append(backup_path.name)
        else:
            # Old backup beyond min_count: delete
            import shutil
            shutil.rmtree(backup_path)
            deleted.append(backup_path.name)

    return kept, deleted

def test_retention_policy():
    """Test: create backups over time, apply retention policy, verify correct ones deleted."""
    with tempfile.TemporaryDirectory() as tmpdir:
        backup_base = Path(tmpdir) / "backups"
        backup_base.mkdir()

        clock = InjectedClock(start_time=0)

        # Create 5 backups at different times
        create_backup(backup_base, "1", clock)
        clock.advance(3600)  # 1 hour

        create_backup(backup_base, "2", clock)
        clock.advance(3600)

        create_backup(backup_base, "3", clock)
        clock.advance(3600)

        create_backup(backup_base, "4", clock)
        clock.advance(3600)

        create_backup(backup_base, "5", clock)
        # Current time: 14400 seconds (4 hours)

        # Policy: keep backups less than 2 hours old, minimum 2 backups
        policy = {"max_age_seconds": 7200, "min_count": 2}

        kept, deleted = apply_retention_policy(backup_base, policy, clock)

        # Backups 4 and 5 are within 2 hours (created 0-3600 seconds ago)
        # Backup 3 is 3600 seconds old (within 2 hours)
        # Backup 2 is 7200 seconds old (exactly at boundary)
        # Backup 1 is 10800 seconds old (outside retention)

        # Expected: keep 5, 4, 3 (all within 2 hours)
        # But also ensure min_count=2 is satisfied
        assert "backup_5" in kept, "Backup 5 (newest) should be kept"
        assert "backup_4" in kept, "Backup 4 should be kept (within 2 hours)"
        assert "backup_3" in kept, "Backup 3 should be kept (within 2 hours)"
        assert len(kept) >= 2, f"Should keep at least {policy['min_count']} backups, kept {len(kept)}"
        assert len(kept) == 3, f"Should keep exactly 3 recent backups (5,4,3), kept {len(kept)}"

        assert "backup_1" in deleted, "Backup 1 (oldest) should be deleted"

        # Verify remaining backups exist
        for backup_id in kept:
            backup_path = backup_base / backup_id
            assert backup_path.exists(), f"{backup_id} should exist"

        # Test: strict age policy with higher min_count
        clock.advance(7200)  # Current time: 21600 seconds
        # All backups are now very old

        # Recreate backups for fresh test
        backup_base2 = Path(tmpdir) / "backups2"
        backup_base2.mkdir()

        clock2 = InjectedClock(start_time=0)
        for i in range(1, 6):
            create_backup(backup_base2, str(i), clock2)
            clock2.advance(1800)  # 30 min intervals

        # After all 5 backups: time = 9000 seconds

        # Policy: keep only last 3 (count-based)
        policy2 = {"max_age_seconds": float('inf'), "min_count": 3}
        kept2, deleted2 = apply_retention_policy(backup_base2, policy2, clock2)

        assert len(kept2) == 3, f"Should keep exactly 3 backups, kept {len(kept2)}"
        assert len(deleted2) == 2, f"Should delete 2 backups, deleted {len(deleted2)}"
        assert "backup_5" in kept2, "Newest backup should be kept"
        assert "backup_4" in kept2, "Second newest should be kept"
        assert "backup_3" in kept2, "Third newest should be kept"
        assert "backup_1" in deleted2, "Oldest should be deleted"

if __name__ == "__main__":
    test_retention_policy()
    print("✓ retention_policy passed")
