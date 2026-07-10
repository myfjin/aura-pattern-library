"""Immutable release artifacts (prevent re-deployment or modification)."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import tempfile


class ImmutableRelease:
    """Manage immutable release artifacts."""

    def __init__(self, releases_dir):
        """Init with releases directory."""
        self.releases_dir = releases_dir
        os.makedirs(releases_dir, exist_ok=True)
        self.released = {}  # version -> metadata

    def create_release(self, version, content):
        """
        Create a release (immutable after creation).
        Raise error if version already exists.
        """
        if version in self.released:
            raise ValueError(f"Release {version} already exists (immutable)")

        # Create version directory
        ver_dir = os.path.join(self.releases_dir, version)
        if os.path.exists(ver_dir):
            raise ValueError(f"Release directory already exists: {ver_dir}")

        os.makedirs(ver_dir)

        # Write artifact
        artifact_file = os.path.join(ver_dir, "artifact.txt")
        with open(artifact_file, "w") as f:
            f.write(content)

        # Store metadata
        self.released[version] = {
            "path": ver_dir,
            "content": content,
        }

    def get_release(self, version):
        """Get release content."""
        if version not in self.released:
            raise ValueError(f"Release {version} not found")

        return self.released[version]["content"]

    def release_exists(self, version):
        """Check if release exists."""
        return version in self.released

    def prevent_modification(self, version):
        """Mark release as immutable (in practice, use file permissions)."""
        if version not in self.released:
            raise ValueError(f"Release {version} not found")

        ver_dir = self.released[version]["path"]
        artifact_file = os.path.join(ver_dir, "artifact.txt")

        # Make file read-only
        os.chmod(artifact_file, 0o444)


def test_create_release():
    """Test: create a release."""
    with tempfile.TemporaryDirectory() as tmpdir:
        immutable = ImmutableRelease(tmpdir)

        immutable.create_release("v1.0", "app code v1")

        assert immutable.release_exists("v1.0")
        assert immutable.get_release("v1.0") == "app code v1"


def test_reject_duplicate_release():
    """Test: reject re-creation of same version."""
    with tempfile.TemporaryDirectory() as tmpdir:
        immutable = ImmutableRelease(tmpdir)

        immutable.create_release("v1.0", "code")

        # SIMULATE FAILURE: try to create same version again
        try:
            immutable.create_release("v1.0", "different code")
            assert False, "Should reject duplicate release"
        except ValueError as e:
            assert "already exists" in str(e)
            assert "immutable" in str(e)


def test_release_immutable():
    """Test: release cannot be modified after creation."""
    with tempfile.TemporaryDirectory() as tmpdir:
        immutable = ImmutableRelease(tmpdir)

        immutable.create_release("v1.0", "original")
        immutable.prevent_modification("v1.0")

        # Get the file path
        ver_dir = os.path.join(tmpdir, "v1.0")
        artifact_file = os.path.join(ver_dir, "artifact.txt")

        # Try to modify (should fail due to permissions)
        try:
            with open(artifact_file, "w") as f:
                f.write("modified")
            assert False, "Should not be able to write to immutable file"
        except PermissionError:
            pass  # Expected


def test_multiple_releases():
    """Test: multiple versions can coexist."""
    with tempfile.TemporaryDirectory() as tmpdir:
        immutable = ImmutableRelease(tmpdir)

        versions = [
            ("v1.0", "code v1"),
            ("v2.0", "code v2"),
            ("v3.0", "code v3"),
        ]

        for ver, content in versions:
            immutable.create_release(ver, content)

        for ver, content in versions:
            assert immutable.get_release(ver) == content


def test_reject_nonexistent_release():
    """Test: reject access to nonexistent release."""
    with tempfile.TemporaryDirectory() as tmpdir:
        immutable = ImmutableRelease(tmpdir)

        try:
            immutable.get_release("v999.0")
            assert False, "Should reject nonexistent release"
        except ValueError as e:
            assert "not found" in str(e)


def test_release_directory_isolation():
    """Test: releases are isolated in separate directories."""
    with tempfile.TemporaryDirectory() as tmpdir:
        immutable = ImmutableRelease(tmpdir)

        immutable.create_release("v1.0", "content1")
        immutable.create_release("v2.0", "content2")

        v1_dir = os.path.join(tmpdir, "v1.0")
        v2_dir = os.path.join(tmpdir, "v2.0")

        assert os.path.exists(v1_dir)
        assert os.path.exists(v2_dir)
        assert v1_dir != v2_dir


def test_release_archival():
    """Test: releases serve as historical archive."""
    with tempfile.TemporaryDirectory() as tmpdir:
        immutable = ImmutableRelease(tmpdir)

        # Release several versions
        for i in range(1, 6):
            immutable.create_release(f"v{i}.0", f"code v{i}")

        # Can retrieve any historical version
        for i in range(1, 6):
            ver = f"v{i}.0"
            assert immutable.get_release(ver) == f"code v{i}"


if __name__ == "__main__":
    test_create_release()
    test_reject_duplicate_release()
    test_release_immutable()
    test_multiple_releases()
    test_reject_nonexistent_release()
    test_release_directory_isolation()
    test_release_archival()
    print("✓ immutable_release passed")
