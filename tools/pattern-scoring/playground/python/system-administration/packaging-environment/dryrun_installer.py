"""
dryrun_installer: perform a dry-run installation (no actual modifications), verify it
would succeed, then do a real installation and verify the system state changed correctly.
The dry-run must NOT modify the system; a broken dry-run would leave side effects.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import tempfile
import json
import sys
from pathlib import Path


def install(install_dir, packages, dry_run=False):
    """
    Simulate installing packages to install_dir.
    packages = {name: version, ...}
    dry_run=True: verify without modifying; dry_run=False: actually install.
    Returns list of installed packages or error message.
    """
    if dry_run:
        # Dry-run: just check what WOULD be installed, don't modify.
        # Verify permissions to write (check dir would be writable if it existed).
        parent_dir = os.path.dirname(install_dir) or "."
        if not os.path.exists(parent_dir):
            raise ValueError(f"parent dir doesn't exist: {parent_dir}")
        return list(packages.keys())

    # Real install: create dir if needed, write manifest and package files.
    if not os.path.exists(install_dir):
        os.makedirs(install_dir)

    manifest_path = os.path.join(install_dir, "manifest.json")

    installed = {}
    for name, version in packages.items():
        pkg_file = os.path.join(install_dir, f"{name}-{version}.pkg")
        Path(pkg_file).touch()
        installed[name] = version

    with open(manifest_path, "w") as f:
        json.dump(installed, f)

    return list(installed.keys())


def verify_installation(install_dir, expected_packages):
    """Verify that expected_packages are installed in install_dir."""
    manifest_path = os.path.join(install_dir, "manifest.json")
    if not os.path.exists(manifest_path):
        raise ValueError("manifest not found")

    with open(manifest_path) as f:
        installed = json.load(f)

    for name, version in expected_packages.items():
        if name not in installed:
            raise ValueError(f"package not installed: {name}")
        if installed[name] != version:
            raise ValueError(f"wrong version for {name}: expected {version}, got {installed[name]}")
    return True


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    install_dir = os.path.join(tmpdir, "apps")

    packages = {"app1": "1.0.0", "app2": "2.0.0"}

    # DRY-RUN: verify it would install, without modifying.
    dry_result = install(install_dir, packages, dry_run=True)
    assert sorted(dry_result) == ["app1", "app2"], "dry-run result wrong"

    # ASSERT: dry-run did NOT create the install directory or any files.
    assert not os.path.exists(install_dir), "dry-run should not create install_dir"

    # THE FAILURE: a broken dry-run would have created files or modified the system.
    # We verify that the absence of these files proves the dry-run was safe.

    # REAL INSTALL: now actually install.
    real_result = install(install_dir, packages, dry_run=False)
    assert sorted(real_result) == ["app1", "app2"]

    # ASSERT: real install created files and manifest.
    assert os.path.exists(install_dir), "real install should create install_dir"
    manifest_path = os.path.join(install_dir, "manifest.json")
    assert os.path.exists(manifest_path), "manifest not created"

    # ASSERT: manifest contains the right packages and versions.
    verify_installation(install_dir, packages)

    # ASSERT: package files exist.
    assert os.path.exists(os.path.join(install_dir, "app1-1.0.0.pkg"))
    assert os.path.exists(os.path.join(install_dir, "app2-2.0.0.pkg"))

    import shutil
    shutil.rmtree(tmpdir)
    print("✓ dryrun_installer passed")
    sys.exit(0)
