"""Atomic symlink swap for deployment (never dangling link)."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import tempfile
import shutil


class AtomicSymlinkSwap:
    """Perform atomic symlink swap using rename (all-or-nothing)."""

    def __init__(self, live_link_path):
        """Init with path to the live symlink."""
        self.live_link = live_link_path

    def deploy(self, new_target_path):
        """
        Atomically point live symlink to new_target.

        Strategy: write to temp link, then rename (atomic on most filesystems).
        If crash occurs between temp write and rename, old link still points to old target.
        """
        # Create parent directory if needed
        parent = os.path.dirname(self.live_link)
        os.makedirs(parent, exist_ok=True)

        # Ensure new target exists
        if not os.path.exists(new_target_path):
            raise ValueError(f"New target does not exist: {new_target_path}")

        # Create temp symlink in same directory (ensures same filesystem)
        temp_link = self.live_link + ".tmp"

        # Remove any stale temp link
        if os.path.lexists(temp_link):
            os.unlink(temp_link)

        # Write new symlink to temp location
        os.symlink(new_target_path, temp_link)

        # ATOMIC SWAP: rename is atomic (all-or-nothing)
        # If crash here, temp_link exists but old live_link is unchanged
        os.rename(temp_link, self.live_link)

    def get_target(self):
        """Return current symlink target."""
        if os.path.islink(self.live_link):
            return os.readlink(self.live_link)
        return None

    def link_exists(self):
        """Check if symlink exists (not dangling)."""
        return os.path.lexists(self.live_link)


def test_atomic_swap_points_to_new_target():
    """Test: symlink points to new target after swap."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create two version directories
        v1_dir = os.path.join(tmpdir, "app-v1")
        v2_dir = os.path.join(tmpdir, "app-v2")
        live_link = os.path.join(tmpdir, "app-live")

        os.makedirs(v1_dir)
        os.makedirs(v2_dir)

        # Create initial link to v1
        swapper = AtomicSymlinkSwap(live_link)
        swapper.deploy(v1_dir)

        assert swapper.get_target() == v1_dir
        assert swapper.link_exists() is True

        # SIMULATE DEPLOYMENT: swap to v2
        swapper.deploy(v2_dir)

        assert swapper.get_target() == v2_dir, "Should point to v2"


def test_swap_maintains_link_validity():
    """Test: link is never dangling (always points to valid target)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        v1_dir = os.path.join(tmpdir, "app-v1")
        v2_dir = os.path.join(tmpdir, "app-v2")
        live_link = os.path.join(tmpdir, "app-live")

        os.makedirs(v1_dir)
        os.makedirs(v2_dir)

        swapper = AtomicSymlinkSwap(live_link)
        swapper.deploy(v1_dir)

        # After swap, link must exist and point to valid target
        swapper.deploy(v2_dir)

        assert swapper.link_exists() is True, "Link should exist"
        assert os.path.exists(swapper.get_target()), "Target should be accessible"


def test_crash_between_temp_and_rename_leaves_live_intact():
    """SIMULATE CRASH at the dangerous moment: temp symlink written but the atomic
    rename never runs. The live link must STILL resolve to the OLD target (never
    dangling) — that is the entire justification for the temp+rename strategy."""
    with tempfile.TemporaryDirectory() as tmpdir:
        v1_dir = os.path.join(tmpdir, "app-v1")
        v2_dir = os.path.join(tmpdir, "app-v2")
        live_link = os.path.join(tmpdir, "app-live")

        os.makedirs(v1_dir)
        os.makedirs(v2_dir)

        swapper = AtomicSymlinkSwap(live_link)
        swapper.deploy(v1_dir)  # live -> v1
        assert swapper.get_target() == v1_dir

        # Reproduce deploy() up to — but NOT including — the rename, i.e. the process
        # crashes with the new link staged but not yet swapped in.
        temp_link = live_link + ".tmp"
        if os.path.lexists(temp_link):
            os.unlink(temp_link)
        os.symlink(v2_dir, temp_link)
        # <<< CRASH HERE: os.rename(temp_link, live_link) never executes >>>

        # Defended outcome: live pointer is UNCHANGED and still valid (points to v1).
        assert swapper.link_exists() is True, "Live link must survive the crash"
        assert swapper.get_target() == v1_dir, "Live link must still point to OLD target after crash"
        assert os.path.exists(swapper.get_target()), "Live target must be accessible (never dangling)"

        # Recovery: completing the rename finishes the swap cleanly.
        os.rename(temp_link, live_link)
        assert swapper.get_target() == v2_dir, "After the rename completes, live points to v2"


def test_reject_nonexistent_target():
    """Test: refuse to deploy to non-existent target."""
    with tempfile.TemporaryDirectory() as tmpdir:
        v1_dir = os.path.join(tmpdir, "app-v1")
        bad_dir = os.path.join(tmpdir, "nonexistent")
        live_link = os.path.join(tmpdir, "app-live")

        os.makedirs(v1_dir)

        swapper = AtomicSymlinkSwap(live_link)

        # SIMULATE FAILURE: try to deploy to nonexistent directory
        try:
            swapper.deploy(bad_dir)
            assert False, "Should reject nonexistent target"
        except ValueError as e:
            assert "does not exist" in str(e)


def test_rollback_to_previous():
    """Test: swap back to previous version (rollback)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        v1_dir = os.path.join(tmpdir, "app-v1")
        v2_dir = os.path.join(tmpdir, "app-v2")
        live_link = os.path.join(tmpdir, "app-live")

        os.makedirs(v1_dir)
        os.makedirs(v2_dir)

        swapper = AtomicSymlinkSwap(live_link)

        # Deploy v1
        swapper.deploy(v1_dir)
        assert swapper.get_target() == v1_dir

        # Deploy v2
        swapper.deploy(v2_dir)
        assert swapper.get_target() == v2_dir

        # SIMULATE FAILURE RECOVERY: rollback to v1
        swapper.deploy(v1_dir)
        assert swapper.get_target() == v1_dir, "Rollback should restore v1"


def test_multiple_deployments():
    """Test: sequence of deployments maintains link integrity."""
    with tempfile.TemporaryDirectory() as tmpdir:
        live_link = os.path.join(tmpdir, "app-live")
        swapper = AtomicSymlinkSwap(live_link)

        # Create and deploy through 5 versions
        for i in range(1, 6):
            ver_dir = os.path.join(tmpdir, f"app-v{i}")
            os.makedirs(ver_dir)

            swapper.deploy(ver_dir)

            assert swapper.link_exists() is True
            assert swapper.get_target() == ver_dir
            assert os.path.exists(swapper.get_target())


if __name__ == "__main__":
    test_atomic_swap_points_to_new_target()
    test_swap_maintains_link_validity()
    test_crash_between_temp_and_rename_leaves_live_intact()
    test_reject_nonexistent_target()
    test_rollback_to_previous()
    test_multiple_deployments()
    print("✓ atomic_symlink_swap passed")
