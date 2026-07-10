"""Promote deployment only after health checks pass."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class HealthGatedPromote:
    """Gate deployment promotion on health check results."""

    def __init__(self):
        self.deployed_version = None
        self.active_version = None
        self.health_checks = {}  # name -> (passed, error_msg)

    def deploy(self, version):
        """Deploy a new version (not yet active)."""
        self.deployed_version = version
        self.health_checks = {}

    def run_health_check(self, check_name, should_pass):
        """
        Run a health check. should_pass=True if check succeeds.
        Store result.
        """
        if should_pass:
            self.health_checks[check_name] = (True, None)
        else:
            self.health_checks[check_name] = (False, f"{check_name} failed")

    def promote(self):
        """
        Promote deployed version to active.
        Raise error if health checks have failures.
        """
        # Check all health checks passed
        for check_name, (passed, error_msg) in self.health_checks.items():
            if not passed:
                raise RuntimeError(
                    f"Cannot promote: health check '{check_name}' failed"
                )

        # Ensure at least one check was run
        if not self.health_checks:
            raise RuntimeError("Cannot promote: no health checks run")

        self.active_version = self.deployed_version

    def get_active_version(self):
        """Return currently active version."""
        return self.active_version

    def get_deployed_version(self):
        """Return currently deployed (but maybe not active) version."""
        return self.deployed_version


def test_promote_after_passing_checks():
    """Test: promote version after health checks pass."""
    gate = HealthGatedPromote()

    gate.deploy("v2.0")

    # Run health checks
    gate.run_health_check("http_ping", True)
    gate.run_health_check("db_connect", True)
    gate.run_health_check("metrics", True)

    # Should promote successfully
    gate.promote()

    assert gate.get_active_version() == "v2.0"


def test_reject_promote_if_check_fails():
    """Test: reject promotion if any health check fails."""
    gate = HealthGatedPromote()

    gate.deploy("v2.0")

    # SIMULATE FAILURE: one check fails
    gate.run_health_check("http_ping", True)
    gate.run_health_check("db_connect", False)  # FAIL
    gate.run_health_check("metrics", True)

    try:
        gate.promote()
        assert False, "Should reject promotion"
    except RuntimeError as e:
        assert "db_connect" in str(e)
        assert "failed" in str(e)

    # Active version should remain unchanged
    assert gate.get_active_version() is None


def test_require_health_checks_before_promote():
    """Test: require at least one health check before promote."""
    gate = HealthGatedPromote()

    gate.deploy("v2.0")

    # Try to promote without running checks
    try:
        gate.promote()
        assert False, "Should require health checks"
    except RuntimeError as e:
        assert "no health checks" in str(e)


def test_deployed_vs_active():
    """Test: deployed and active versions can differ."""
    gate = HealthGatedPromote()

    # Deploy v2
    gate.deploy("v2.0")
    gate.run_health_check("ping", True)

    # v2 not active yet
    assert gate.get_deployed_version() == "v2.0"
    assert gate.get_active_version() is None

    # Promote v2
    gate.promote()
    assert gate.get_deployed_version() == "v2.0"
    assert gate.get_active_version() == "v2.0"

    # Deploy v3 (but don't promote yet)
    gate.deploy("v3.0")
    assert gate.get_deployed_version() == "v3.0"
    assert gate.get_active_version() == "v2.0"  # v2 still active


def test_all_checks_must_pass():
    """Test: all checks must pass for promotion."""
    gate = HealthGatedPromote()

    gate.deploy("v2.0")

    checks_passed = [True, True, False, True]

    for i, passed in enumerate(checks_passed):
        gate.run_health_check(f"check_{i}", passed)

    try:
        gate.promote()
        assert False, "Should fail on one failing check"
    except RuntimeError as e:
        assert "check_2" in str(e)


def test_promotion_chain():
    """Test: promoting through multiple versions."""
    gate = HealthGatedPromote()

    versions = ["v1.0", "v2.0", "v3.0"]

    for ver in versions:
        gate.deploy(ver)
        gate.run_health_check("ping", True)
        gate.promote()

        assert gate.get_active_version() == ver


if __name__ == "__main__":
    test_promote_after_passing_checks()
    test_reject_promote_if_check_fails()
    test_require_health_checks_before_promote()
    test_deployed_vs_active()
    test_all_checks_must_pass()
    test_promotion_chain()
    print("✓ health_gated_promote passed")
