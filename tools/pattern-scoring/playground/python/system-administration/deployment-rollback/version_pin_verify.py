"""Verify version pins match deployed artifacts."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import hashlib


class VersionPinVerify:
    """Verify that deployed version matches the pinned hash."""

    def __init__(self):
        self.version_pins = {}  # version -> expected_hash

    def pin_version(self, version, expected_hash):
        """Register expected hash for a version."""
        self.version_pins[version] = expected_hash

    def compute_hash(self, content):
        """Compute SHA256 hash of content."""
        return hashlib.sha256(content.encode("utf-8")).hexdigest()

    def verify_deployment(self, version, actual_content):
        """
        Verify deployed content matches pinned hash.
        Raise ValueError if mismatch.
        Return True if matches.
        """
        if version not in self.version_pins:
            raise ValueError(f"No pin found for version {version}")

        expected_hash = self.version_pins[version]
        actual_hash = self.compute_hash(actual_content)

        if actual_hash != expected_hash:
            raise ValueError(
                f"Version {version} hash mismatch: "
                f"expected {expected_hash}, got {actual_hash}"
            )

        return True


def test_verify_matching_hash():
    """Test: accept deployment with matching hash."""
    verifier = VersionPinVerify()

    content = "app code v1.0"
    hash_value = verifier.compute_hash(content)

    verifier.pin_version("v1.0", hash_value)

    # Deploy should succeed
    assert verifier.verify_deployment("v1.0", content) is True


def test_reject_mismatched_hash():
    """Test: reject deployment with mismatched hash."""
    verifier = VersionPinVerify()

    content = "app code v1.0"
    expected_hash = "abc123"

    verifier.pin_version("v1.0", expected_hash)

    # SIMULATE FAILURE: deploy with wrong content
    try:
        verifier.verify_deployment("v1.0", content)
        assert False, "Should reject mismatched hash"
    except ValueError as e:
        assert "hash mismatch" in str(e)
        assert expected_hash in str(e)


def test_reject_unpinned_version():
    """Test: reject version without a pin."""
    verifier = VersionPinVerify()

    try:
        verifier.verify_deployment("unknown", "some content")
        assert False, "Should reject unpinned version"
    except ValueError as e:
        assert "No pin found" in str(e)


def test_hash_deterministic():
    """Test: same content produces same hash."""
    verifier = VersionPinVerify()

    content = "same content"

    hash1 = verifier.compute_hash(content)
    hash2 = verifier.compute_hash(content)

    assert hash1 == hash2, "Hash should be deterministic"


def test_different_content_different_hash():
    """Test: different content produces different hash."""
    verifier = VersionPinVerify()

    content1 = "version 1.0"
    content2 = "version 2.0"

    hash1 = verifier.compute_hash(content1)
    hash2 = verifier.compute_hash(content2)

    assert hash1 != hash2, "Different content should have different hash"


def test_single_byte_change_detected():
    """Test: single byte change is detected."""
    verifier = VersionPinVerify()

    content = "application binary"
    hash_original = verifier.compute_hash(content)

    verifier.pin_version("v1.0", hash_original)

    # SIMULATE FAILURE: single byte changed
    corrupted = "application binars"  # y -> s

    try:
        verifier.verify_deployment("v1.0", corrupted)
        assert False, "Should detect single byte change"
    except ValueError as e:
        assert "hash mismatch" in str(e)


def test_pin_multiple_versions():
    """Test: pin and verify multiple versions."""
    verifier = VersionPinVerify()

    versions = {
        "v1.0": "code v1",
        "v1.1": "code v1.1",
        "v2.0": "code v2",
    }

    # Pin all versions
    for ver, content in versions.items():
        hash_val = verifier.compute_hash(content)
        verifier.pin_version(ver, hash_val)

    # Verify each version
    for ver, content in versions.items():
        assert verifier.verify_deployment(ver, content) is True


if __name__ == "__main__":
    test_verify_matching_hash()
    test_reject_mismatched_hash()
    test_reject_unpinned_version()
    test_hash_deterministic()
    test_different_content_different_hash()
    test_single_byte_change_detected()
    test_pin_multiple_versions()
    print("✓ version_pin_verify passed")
