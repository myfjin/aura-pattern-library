"""Automatic rollback when deployment fails or becomes unhealthy."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class RollbackOnFailure:
    """Monitor deployed version and auto-rollback on failure."""

    def __init__(self):
        self.previous_version = None
        self.current_version = None
        self.healthy = True
        self.failure_reason = None

    def deploy(self, version):
        """Deploy new version."""
        self.previous_version = self.current_version
        self.current_version = version
        self.healthy = True
        self.failure_reason = None

    def mark_unhealthy(self, reason):
        """Mark current version as unhealthy."""
        self.healthy = False
        self.failure_reason = reason

    def rollback(self):
        """
        Rollback to previous version.
        Raise error if no previous version available.
        """
        if self.previous_version is None:
            raise RuntimeError("Cannot rollback: no previous version")

        self.current_version = self.previous_version
        self.healthy = True
        self.failure_reason = None

    def should_rollback(self):
        """Return True if deployment is unhealthy and needs rollback."""
        return not self.healthy

    def get_current_version(self):
        """Return active version."""
        return self.current_version


def test_successful_deployment():
    """Test: successful deployment with no rollback."""
    rollback = RollbackOnFailure()

    rollback.deploy("v1.0")
    assert rollback.get_current_version() == "v1.0"
    assert rollback.should_rollback() is False


def test_detect_unhealthy_deployment():
    """Test: detect unhealthy deployment."""
    rollback = RollbackOnFailure()

    rollback.deploy("v1.0")
    rollback.deploy("v2.0")

    # SIMULATE FAILURE: new version becomes unhealthy
    rollback.mark_unhealthy("database connection failed")

    assert rollback.should_rollback() is True
    assert rollback.failure_reason == "database connection failed"


def test_rollback_restores_previous():
    """Test: rollback restores previous version."""
    rollback = RollbackOnFailure()

    rollback.deploy("v1.0")
    assert rollback.get_current_version() == "v1.0"

    rollback.deploy("v2.0")
    assert rollback.get_current_version() == "v2.0"

    # Detect failure
    rollback.mark_unhealthy("error rate high")
    assert rollback.should_rollback() is True

    # Perform rollback
    rollback.rollback()
    assert rollback.get_current_version() == "v1.0"
    assert rollback.should_rollback() is False


def test_cannot_rollback_without_previous():
    """Test: reject rollback if no previous version."""
    rollback = RollbackOnFailure()

    rollback.deploy("v1.0")
    rollback.mark_unhealthy("startup failed")

    try:
        rollback.rollback()
        assert False, "Should reject rollback without previous version"
    except RuntimeError as e:
        assert "no previous version" in str(e)


def test_rollback_clears_failure_flag():
    """Test: after rollback, healthy flag is reset."""
    rollback = RollbackOnFailure()

    rollback.deploy("v1.0")
    rollback.deploy("v2.0")
    rollback.mark_unhealthy("error")

    rollback.rollback()

    assert rollback.healthy is True
    assert rollback.failure_reason is None


def test_multi_version_rollback_chain():
    """Test: deploy through multiple versions, rollback one at a time."""
    rollback = RollbackOnFailure()

    versions = ["v1.0", "v2.0", "v3.0", "v4.0"]

    for ver in versions:
        rollback.deploy(ver)
        assert rollback.get_current_version() == ver

    # v4 fails
    rollback.mark_unhealthy("memory leak")
    assert rollback.should_rollback() is True

    # Rollback to v3
    rollback.rollback()
    assert rollback.get_current_version() == "v3.0"

    # Now deploy v4 again (healthier)
    rollback.deploy("v4.0")
    assert rollback.get_current_version() == "v4.0"

    # v4 still unhealthy
    rollback.mark_unhealthy("another issue")
    rollback.rollback()

    # Back to v3
    assert rollback.get_current_version() == "v3.0"


def test_recovery_after_rollback():
    """Test: deploy again after rollback."""
    rollback = RollbackOnFailure()

    rollback.deploy("v1.0")
    rollback.deploy("v2.0")

    rollback.mark_unhealthy("error")
    rollback.rollback()

    # Deploy v2 again (fixed)
    rollback.deploy("v2.0")
    assert rollback.get_current_version() == "v2.0"
    assert rollback.should_rollback() is False


if __name__ == "__main__":
    test_successful_deployment()
    test_detect_unhealthy_deployment()
    test_rollback_restores_previous()
    test_cannot_rollback_without_previous()
    test_rollback_clears_failure_flag()
    test_multi_version_rollback_chain()
    test_recovery_after_rollback()
    print("✓ rollback_on_failure passed")
