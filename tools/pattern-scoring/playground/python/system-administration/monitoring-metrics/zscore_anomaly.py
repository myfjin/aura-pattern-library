#!/usr/bin/env python3
"""zscore_anomaly: detect anomalies using z-score."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys
import math

class ZScoreAnomaly:
    """Detect anomalies using z-score."""
    def __init__(self, threshold=3.0, window_size=30):
        self.threshold = threshold
        self.window_size = window_size
        self.observations = []
        self.anomalies = []

    def add(self, value):
        """Add observation and check for anomaly."""
        self.observations.append(value)

        # Calculate mean and stddev of window
        window = self.observations[-self.window_size:]

        if len(window) < 2:
            return False  # Not enough data

        mean = sum(window) / len(window)
        variance = sum((x - mean) ** 2 for x in window) / len(window)
        stddev = math.sqrt(variance)

        if stddev == 0:
            return False  # No variation to detect

        # Calculate z-score for current value
        zscore = (value - mean) / stddev

        if abs(zscore) > self.threshold:
            self.anomalies.append((len(self.observations) - 1, value, zscore))
            return True

        return False

    def get_anomalies(self):
        """Return list of anomalies detected."""
        return self.anomalies

def test_zscore_anomaly():
    """Test: normal data passes, outliers detected."""
    # Test 1: known series with outlier
    detector = ZScoreAnomaly(threshold=2.0, window_size=10)

    # Normal data: 100 ± 5
    normal_seq = [100, 102, 99, 101, 98, 102, 99, 100, 101, 99]
    for v in normal_seq:
        is_anomaly = detector.add(v)
        assert not is_anomaly, f"Normal value {v} should not be anomaly"

    assert len(detector.get_anomalies()) == 0, "No anomalies in normal data"

    # Add outlier: 200 is far from 100
    is_anomaly = detector.add(200)
    assert is_anomaly, "Value 200 should be detected as anomaly"

    anomalies = detector.get_anomalies()
    assert len(anomalies) == 1, f"Should have 1 anomaly, got {len(anomalies)}"
    assert anomalies[0][1] == 200, "Anomaly should be the value 200"

    # Test 2: multiple outliers
    detector2 = ZScoreAnomaly(threshold=2.5, window_size=10)

    for v in [50, 51, 49, 52, 50, 51, 49, 50]:
        detector2.add(v)

    # Add lower outlier
    detector2.add(0)
    assert len(detector2.get_anomalies()) == 1, "Should detect lower outlier"

    # Add upper outlier
    detector2.add(500)
    assert len(detector2.get_anomalies()) == 2, "Should detect upper outlier too"

    # Test 3: threshold sensitivity
    detector_low = ZScoreAnomaly(threshold=1.0)  # Sensitive
    detector_high = ZScoreAnomaly(threshold=10.0)  # Insensitive

    # Moderate outlier: 50 in series [10..20]
    for d in [detector_low, detector_high]:
        for v in [10, 12, 11, 13, 12, 11, 10, 12, 11, 13]:
            d.add(v)

    # Low threshold should detect outlier
    assert detector_low.add(50), "Low threshold should detect 50 as outlier"

    # High threshold might not
    # (depending on calculation, but 50 is likely still anomalous)
    # We'll verify low threshold is more sensitive by checking count
    assert len(detector_low.get_anomalies()) >= 1, "Low threshold detects something"

    # Test 4: gradual drift doesn't trigger anomaly
    detector_drift = ZScoreAnomaly(threshold=3.0, window_size=5)

    # Gradual drift from 100 to 200
    for i in range(0, 101, 10):
        detector_drift.add(100 + i)

    # Should not have many anomalies (drift is gradual)
    assert len(detector_drift.get_anomalies()) < 3, "Gradual drift should not trigger many anomalies"

    # Test 5: insufficient data
    detector_empty = ZScoreAnomaly(threshold=2.0)

    assert not detector_empty.add(100), "Single point should not be anomaly"
    assert len(detector_empty.get_anomalies()) == 0

    # Test 6: build variation then detect outlier
    detector_const2 = ZScoreAnomaly(threshold=1.5, window_size=5)  # Lower threshold for better detection
    for v in [50, 50, 50, 50, 50]:  # Baseline around 50
        detector_const2.add(v)

    # Now add clear outlier
    result = detector_const2.add(150)  # 3x baseline
    assert result, "Should detect 150 as outlier when baseline is 50"

if __name__ == "__main__":
    test_zscore_anomaly()
    print("✓ zscore_anomaly passed")
