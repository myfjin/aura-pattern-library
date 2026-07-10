"""
capability_probe: probe system capabilities (hardlinks, symlinks, sparse files, etc.)
and record which are available. Mutate the system state (remove capability) and re-probe;
verify the capability is no longer reported.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import tempfile
import sys
from pathlib import Path


def probe_capabilities(test_dir):
    """
    Probe what capabilities the filesystem supports.
    Returns dict {capability: True/False, ...}
    """
    capabilities = {}

    # Test hardlinks.
    try:
        f1 = os.path.join(test_dir, "file1")
        f2 = os.path.join(test_dir, "hardlink")
        Path(f1).touch()
        os.link(f1, f2)
        os.unlink(f2)
        os.unlink(f1)
        capabilities["hardlinks"] = True
    except Exception:
        capabilities["hardlinks"] = False

    # Test symlinks.
    try:
        f3 = os.path.join(test_dir, "file3")
        sym = os.path.join(test_dir, "symlink")
        Path(f3).touch()
        os.symlink(f3, sym)
        os.unlink(sym)
        os.unlink(f3)
        capabilities["symlinks"] = True
    except Exception:
        capabilities["symlinks"] = False

    # Test chmod (execute bit).
    try:
        f4 = os.path.join(test_dir, "file4")
        Path(f4).touch()
        os.chmod(f4, 0o755)
        mode = os.stat(f4).st_mode & 0o111
        os.unlink(f4)
        capabilities["execute_bit"] = mode != 0
    except Exception:
        capabilities["execute_bit"] = False

    return capabilities


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    test_dir = os.path.join(tmpdir, "probe")
    os.makedirs(test_dir)

    # Initial probe.
    caps1 = probe_capabilities(test_dir)

    # Most systems support symlinks, so symlinks should be True.
    # (hardlinks might fail on some filesystems, but symlinks generally work)
    assert caps1.get("symlinks") or caps1.get("hardlinks"), "expected at least symlinks or hardlinks"
    assert "execute_bit" in caps1

    # THE FAILURE: simulate losing a capability by retesting in a degraded state.
    # We can't actually disable the filesystem capability, but we can verify that
    # if a test fails, the capability is reported as False.
    # Let's make a read-only directory and verify we can't create files.
    test_dir_readonly = os.path.join(tmpdir, "readonly")
    os.makedirs(test_dir_readonly)

    # Save initial capabilities.
    caps_before = probe_capabilities(test_dir_readonly)
    # Should support basic file creation at this point.
    assert caps_before.get("symlinks"), "should support symlinks"

    # Now make directory read-only.
    os.chmod(test_dir_readonly, 0o555)

    # Re-probe in read-only directory.
    caps_after = probe_capabilities(test_dir_readonly)

    # ASSERT: read-only directory prevents symlink creation, so symlinks capability is lost.
    assert not caps_after.get("symlinks"), "should not support symlinks in read-only dir"
    assert caps_before.get("symlinks"), "should have supported symlinks before read-only"

    # Restore permissions for cleanup.
    os.chmod(test_dir_readonly, 0o755)

    import shutil
    shutil.rmtree(tmpdir)
    print("✓ capability_probe passed")
    sys.exit(0)
