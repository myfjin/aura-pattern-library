"""
path_sanity: verify that required binaries exist in PATH and are at expected locations.
Failure simulated: a binary is moved/deleted, or a malicious binary is injected earlier
in PATH. The checker must detect the absence or unexpected location.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import tempfile
import shutil
import sys
from pathlib import Path


def find_binary(name, path_str):
    """
    Find binary 'name' in PATH-like string. Returns full path or None.
    path_str is colon-separated like "/usr/bin:/bin:/usr/local/bin"
    """
    for directory in path_str.split(":"):
        if not directory:
            continue
        candidate = os.path.join(directory, name)
        if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return candidate
    return None


def verify_binary_locations(path_str, required):
    """
    Verify that all binaries in required dict are found at expected locations.
    required = {name: expected_dir, ...}
    Raises ValueError if binary not found or in wrong directory.
    """
    for name, expected_dir in required.items():
        actual_path = find_binary(name, path_str)
        if actual_path is None:
            raise ValueError(f"binary not found in PATH: {name}")
        actual_dir = os.path.dirname(actual_path)
        if actual_dir != expected_dir:
            raise ValueError(
                f"binary {name} in wrong directory: expected {expected_dir}, got {actual_dir}"
            )
    return True


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    bin_dir1 = os.path.join(tmpdir, "bin1")
    bin_dir2 = os.path.join(tmpdir, "bin2")
    os.makedirs(bin_dir1)
    os.makedirs(bin_dir2)

    # Create real binaries (just executable files).
    python_bin = os.path.join(bin_dir1, "python")
    gcc_bin = os.path.join(bin_dir2, "gcc")
    Path(python_bin).touch()
    Path(gcc_bin).touch()
    os.chmod(python_bin, 0o755)
    os.chmod(gcc_bin, 0o755)

    path_str = f"{bin_dir1}:{bin_dir2}"

    # Clean case: all binaries found at expected locations.
    required = {"python": bin_dir1, "gcc": bin_dir2}
    assert verify_binary_locations(path_str, required)

    # THE FAILURE: delete one binary.
    os.unlink(python_bin)

    # ASSERT: verifier catches the missing binary.
    try:
        verify_binary_locations(path_str, required)
        assert False, "should have raised ValueError on missing binary"
    except ValueError as e:
        assert "binary not found" in str(e) and "python" in str(e)

    # Recreate python for next test.
    Path(python_bin).touch()
    os.chmod(python_bin, 0o755)

    # THE FAILURE 2: move binary to wrong directory.
    # Move python to bin_dir2 (wrong directory).
    shutil.move(python_bin, os.path.join(bin_dir2, "python"))

    # ASSERT: verifier catches the wrong directory.
    try:
        verify_binary_locations(path_str, required)
        assert False, "should have raised ValueError on wrong directory"
    except ValueError as e:
        assert "wrong directory" in str(e) and "python" in str(e)

    shutil.rmtree(tmpdir)
    print("✓ path_sanity passed")
    sys.exit(0)
