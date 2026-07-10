"""Detect configuration drift between expected and actual state."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import hashlib


class ConfigDriftDetect:
    """Track configuration state and detect drift."""

    def __init__(self):
        self.expected_config = {}  # key -> value
        self.expected_hash = None
        self.actual_config = {}
        self.actual_hash = None

    def set_expected(self, config_dict):
        """Set expected configuration."""
        self.expected_config = dict(config_dict)
        self.expected_hash = self._compute_hash(self.expected_config)

    def scan_actual(self, config_dict):
        """Scan actual system configuration."""
        self.actual_config = dict(config_dict)
        self.actual_hash = self._compute_hash(self.actual_config)

    def _compute_hash(self, config_dict):
        """Compute hash of configuration."""
        import json

        content = json.dumps(config_dict, sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()

    def has_drift(self):
        """Return True if actual differs from expected."""
        return self.expected_hash != self.actual_hash

    def get_drift_details(self):
        """Return dict of differences between expected and actual."""
        drift = {}

        # Keys in expected but not in actual
        for key in self.expected_config:
            if key not in self.actual_config:
                drift[key] = ("missing", self.expected_config[key], None)

        # Keys in actual but not in expected
        for key in self.actual_config:
            if key not in self.expected_config:
                drift[key] = ("extra", None, self.actual_config[key])

        # Keys in both but different values
        for key in self.expected_config:
            if key in self.actual_config:
                if self.expected_config[key] != self.actual_config[key]:
                    drift[key] = (
                        "changed",
                        self.expected_config[key],
                        self.actual_config[key],
                    )

        return drift


def test_no_drift():
    """Test: no drift when configs match."""
    detector = ConfigDriftDetect()

    config = {"db_host": "localhost", "db_port": 5432, "timeout": 30}

    detector.set_expected(config)
    detector.scan_actual(config)

    assert detector.has_drift() is False


def test_detect_value_change():
    """Test: detect when value changes."""
    detector = ConfigDriftDetect()

    expected = {"db_host": "localhost", "timeout": 30}
    actual = {"db_host": "localhost", "timeout": 60}

    detector.set_expected(expected)
    detector.scan_actual(actual)

    assert detector.has_drift() is True

    drift = detector.get_drift_details()
    assert "timeout" in drift
    assert drift["timeout"] == ("changed", 30, 60)


def test_detect_missing_config():
    """Test: detect missing configuration."""
    detector = ConfigDriftDetect()

    expected = {"db_host": "localhost", "db_port": 5432, "timeout": 30}
    actual = {"db_host": "localhost", "timeout": 30}  # Missing db_port

    detector.set_expected(expected)
    detector.scan_actual(actual)

    assert detector.has_drift() is True

    drift = detector.get_drift_details()
    assert "db_port" in drift
    assert drift["db_port"][0] == "missing"


def test_detect_extra_config():
    """Test: detect unexpected extra configuration."""
    detector = ConfigDriftDetect()

    expected = {"db_host": "localhost"}
    actual = {"db_host": "localhost", "debug": True}  # Extra key

    detector.set_expected(expected)
    detector.scan_actual(actual)

    assert detector.has_drift() is True

    drift = detector.get_drift_details()
    assert "debug" in drift
    assert drift["debug"][0] == "extra"


def test_multiple_drift_issues():
    """Test: detect multiple configuration issues."""
    detector = ConfigDriftDetect()

    expected = {
        "db_host": "localhost",
        "db_port": 5432,
        "timeout": 30,
        "workers": 4,
    }

    actual = {
        "db_host": "127.0.0.1",  # Changed
        "db_port": 5432,
        "timeout": 60,  # Changed
        # workers missing
        "debug": True,  # Extra
    }

    detector.set_expected(expected)
    detector.scan_actual(actual)

    assert detector.has_drift() is True

    drift = detector.get_drift_details()

    # Should have 4 issues
    assert len(drift) == 4
    assert "db_host" in drift
    assert "timeout" in drift
    assert "workers" in drift
    assert "debug" in drift


def test_drift_allows_remediation():
    """Test: after detecting drift, fix and rescan."""
    detector = ConfigDriftDetect()

    expected = {"server_port": 8080, "workers": 4}
    detector.set_expected(expected)

    # Scan with drift
    actual_bad = {"server_port": 9000, "workers": 4}
    detector.scan_actual(actual_bad)

    assert detector.has_drift() is True

    # Fix the drift and rescan
    actual_good = {"server_port": 8080, "workers": 4}
    detector.scan_actual(actual_good)

    assert detector.has_drift() is False


def test_empty_configs():
    """Test: empty configurations have no drift."""
    detector = ConfigDriftDetect()

    detector.set_expected({})
    detector.scan_actual({})

    assert detector.has_drift() is False


def test_large_config_drift():
    """Test: large configuration with multiple drifts."""
    detector = ConfigDriftDetect()

    expected = {f"key_{i}": f"value_{i}" for i in range(100)}

    actual = dict(expected)
    # Introduce several drifts
    actual["key_10"] = "wrong_value"
    del actual["key_50"]
    actual["key_999"] = "extra_value"

    detector.set_expected(expected)
    detector.scan_actual(actual)

    assert detector.has_drift() is True

    drift = detector.get_drift_details()
    assert "key_10" in drift
    assert "key_50" in drift
    assert "key_999" in drift


if __name__ == "__main__":
    test_no_drift()
    test_detect_value_change()
    test_detect_missing_config()
    test_detect_extra_config()
    test_multiple_drift_issues()
    test_drift_allows_remediation()
    test_empty_configs()
    test_large_config_drift()
    print("✓ config_drift_detect passed")
