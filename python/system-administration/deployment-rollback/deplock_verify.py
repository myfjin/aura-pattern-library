"""Verify dependency lock file consistency."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import json
import hashlib


class DeplockVerify:
    """Verify lock file integrity and dependencies."""

    def __init__(self):
        self.lock_file = {}  # pkg_name -> (version, hash)
        self.lock_hash = None

    def load_lock(self, lock_dict):
        """Load lock file content."""
        self.lock_file = dict(lock_dict)
        self.lock_hash = self._compute_lock_hash()

    def _compute_lock_hash(self):
        """Compute hash of current lock file."""
        content = json.dumps(self.lock_file, sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()

    def verify_lock_integrity(self):
        """
        Verify lock file has not been tampered with.
        Return True if unchanged since load.
        """
        current_hash = self._compute_lock_hash()
        return current_hash == self.lock_hash

    def add_dependency(self, pkg_name, version, dep_hash):
        """Add or update a dependency."""
        self.lock_file[pkg_name] = (version, dep_hash)
        self.lock_hash = self._compute_lock_hash()

    def verify_package(self, pkg_name, expected_version, expected_hash):
        """
        Verify a package matches lock file expectations.
        Raise error if mismatch.
        """
        if pkg_name not in self.lock_file:
            raise ValueError(f"Package {pkg_name} not in lock file")

        stored_version, stored_hash = self.lock_file[pkg_name]

        if stored_version != expected_version:
            raise ValueError(
                f"Package {pkg_name} version mismatch: "
                f"expected {expected_version}, got {stored_version}"
            )

        if stored_hash != expected_hash:
            raise ValueError(
                f"Package {pkg_name} hash mismatch: "
                f"expected {expected_hash}, got {stored_hash}"
            )

        return True


def test_load_lock_file():
    """Test: load lock file."""
    verifier = DeplockVerify()

    lock = {
        "django": ("3.2.0", "abc123"),
        "numpy": ("1.21.0", "def456"),
    }

    verifier.load_lock(lock)

    assert verifier.verify_lock_integrity() is True


def test_detect_lock_tampering():
    """Test: detect modification to lock file."""
    verifier = DeplockVerify()

    lock = {"django": ("3.2.0", "abc123")}
    verifier.load_lock(lock)

    assert verifier.verify_lock_integrity() is True

    # SIMULATE FAILURE: tamper with lock file
    verifier.lock_file["django"] = ("3.3.0", "modified")

    assert verifier.verify_lock_integrity() is False


def test_verify_package_success():
    """Test: verify package matches lock expectations."""
    verifier = DeplockVerify()

    lock = {"requests": ("2.28.0", "hash789")}
    verifier.load_lock(lock)

    # Verify with matching version and hash
    assert verifier.verify_package("requests", "2.28.0", "hash789") is True


def test_verify_package_version_mismatch():
    """Test: reject package with wrong version."""
    verifier = DeplockVerify()

    lock = {"django": ("3.2.0", "abc123")}
    verifier.load_lock(lock)

    # SIMULATE FAILURE: wrong version deployed
    try:
        verifier.verify_package("django", "3.1.0", "abc123")
        assert False, "Should reject version mismatch"
    except ValueError as e:
        assert "version mismatch" in str(e)
        assert "3.1.0" in str(e)


def test_verify_package_hash_mismatch():
    """Test: reject package with wrong hash."""
    verifier = DeplockVerify()

    lock = {"numpy": ("1.21.0", "correcthash")}
    verifier.load_lock(lock)

    # SIMULATE FAILURE: wrong hash (e.g., corrupted download)
    try:
        verifier.verify_package("numpy", "1.21.0", "wronghash")
        assert False, "Should reject hash mismatch"
    except ValueError as e:
        assert "hash mismatch" in str(e)


def test_reject_missing_package():
    """Test: reject if package not in lock file."""
    verifier = DeplockVerify()

    lock = {"django": ("3.2.0", "abc123")}
    verifier.load_lock(lock)

    try:
        verifier.verify_package("unknown", "1.0.0", "hash")
        assert False, "Should reject unknown package"
    except ValueError as e:
        assert "not in lock file" in str(e)


def test_add_dependency_updates_hash():
    """Test: adding dependency updates lock hash."""
    verifier = DeplockVerify()

    verifier.load_lock({})
    hash_before = verifier.lock_hash

    verifier.add_dependency("new_pkg", "1.0.0", "newhash")

    hash_after = verifier.lock_hash

    assert hash_before != hash_after, "Lock hash should change"
    assert verifier.verify_lock_integrity() is True


def test_multiple_package_verification():
    """Test: verify multiple packages."""
    verifier = DeplockVerify()

    lock = {
        "pkg1": ("1.0.0", "hash1"),
        "pkg2": ("2.0.0", "hash2"),
        "pkg3": ("3.0.0", "hash3"),
    }

    verifier.load_lock(lock)

    # All should pass
    for pkg in ["pkg1", "pkg2", "pkg3"]:
        version = f"{lock[pkg][0]}"
        hash_val = f"{lock[pkg][1]}"
        assert verifier.verify_package(pkg, version, hash_val) is True


if __name__ == "__main__":
    test_load_lock_file()
    test_detect_lock_tampering()
    test_verify_package_success()
    test_verify_package_version_mismatch()
    test_verify_package_hash_mismatch()
    test_reject_missing_package()
    test_add_dependency_updates_hash()
    test_multiple_package_verification()
    print("✓ deplock_verify passed")
