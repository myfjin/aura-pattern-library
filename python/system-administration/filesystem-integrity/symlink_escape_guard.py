"""
symlink_escape_guard: refuse to create symlinks that escape the root directory.
Failure simulated: attempt to create symlinks that point outside root (escape attack);
assert the guard refuses it. Allow symlinks within root.
Recovery asserted: escape attempts are blocked; safe symlinks are created; path resolution
proves the target is within root or denied. Pattern's own guard function is called.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import tempfile
import sys
from pathlib import Path


def safe_symlink(link_path, target_path, root_dir):
    """
    Create a symlink from link_path to target_path, but only if target_path
    resolves to within root_dir. Raises if escape is detected.
    """
    # Resolve the target to an absolute path
    resolved_target = os.path.abspath(os.path.join(os.path.dirname(link_path), target_path))
    abs_root = os.path.abspath(root_dir)

    # Check if resolved target is within root_dir
    if not resolved_target.startswith(abs_root + os.sep) and resolved_target != abs_root:
        raise ValueError(f"symlink escape detected: {resolved_target} outside {abs_root}")

    # Create the symlink
    os.symlink(target_path, link_path)


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    root = tmpdir
    target_file = os.path.join(root, "target.txt")
    parent_dir = os.path.dirname(root)
    outside_file = os.path.join(parent_dir, "outside.txt")

    # Create a safe target file inside root
    Path(target_file).write_bytes(b"safe_target_content")

    # Create an unsafe file outside root
    Path(outside_file).write_bytes(b"outside_content")

    # FAILURE SIM 1: attempt to create symlink to outside file (should fail)
    link_path = os.path.join(root, "link_to_outside")
    relative_outside = os.path.relpath(outside_file, os.path.dirname(link_path))

    try:
        safe_symlink(link_path, relative_outside, root)
        assert False, "escape guard did not block symlink to outside"
    except ValueError as e:
        assert "escape detected" in str(e), f"wrong error: {e}"

    # RECOVERY assert 1: link_path does not exist (symlink was not created)
    assert not Path(link_path).exists(), f"escape symlink was created: {link_path}"
    assert not os.path.islink(link_path), f"escape symlink exists: {link_path}"

    # FAILURE SIM 2: create symlink to relative ../../../outside (should fail)
    link_path2 = os.path.join(root, "link_traversal")
    try:
        safe_symlink(link_path2, "../" * 3 + "outside.txt", root)
        assert False, "escape guard did not block traversal symlink"
    except ValueError as e:
        assert "escape detected" in str(e), f"wrong error: {e}"

    # RECOVERY assert 2: traversal symlink was not created
    assert not Path(link_path2).exists(), f"traversal symlink was created: {link_path2}"

    # FAILURE SIM 3: create safe symlink to file within root (should succeed)
    link_safe = os.path.join(root, "link_safe")
    relative_target = os.path.relpath(target_file, os.path.dirname(link_safe))
    safe_symlink(link_safe, relative_target, root)

    # RECOVERY assert 3: safe symlink is created
    assert os.path.islink(link_safe), f"safe symlink not created: {link_safe}"

    # RECOVERY assert 4: safe symlink points to correct target
    assert os.readlink(link_safe) == relative_target, f"symlink points wrong: {os.readlink(link_safe)}"

    # RECOVERY assert 5: reading through safe symlink works
    content_via_link = Path(link_safe).read_bytes()
    assert content_via_link == b"safe_target_content", f"symlink resolution failed"

    # RECOVERY assert 6: can't resolve escaped symlinks even if they were created
    # (this proves the guard works at creation time)
    try:
        # Try to create an absolute symlink to outside
        link_abs = os.path.join(root, "link_abs")
        safe_symlink(link_abs, outside_file, root)  # absolute path
        assert False, "escape guard did not block absolute symlink"
    except ValueError:
        pass

    # Clean up
    import shutil
    shutil.rmtree(tmpdir)

    print(f"symlink_escape_guard: blocked_escape=2, allowed_safe=1")
    print("symlink_escape_guard PASS")
    sys.exit(0)
