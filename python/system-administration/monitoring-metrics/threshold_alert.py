#!/usr/bin/env python3
"""threshold_alert: fire alerts when metrics cross thresholds."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys

class ThresholdAlert:
    """Alert when value crosses threshold."""
    def __init__(self, threshold, comparison="greater_than", hysteresis=0):
        """
        threshold: the alert boundary
        comparison: "greater_than", "less_than", "equal"
        hysteresis: deadband to prevent flapping
        """
        self.threshold = threshold
        self.comparison = comparison
        self.hysteresis = hysteresis
        self.alerting = False
        self.last_value = None
        self.alert_count = 0

    def check(self, value):
        """Check value against threshold, return True if alert fires."""
        alert_fired = False

        if self.comparison == "greater_than":
            # Alert if value > threshold (when not already alerting)
            # Hysteresis: stop alerting if value < (threshold - hysteresis)
            if not self.alerting:
                if value > self.threshold:
                    self.alerting = True
                    alert_fired = True
                    self.alert_count += 1
            else:
                if value < (self.threshold - self.hysteresis):
                    self.alerting = False

        elif self.comparison == "less_than":
            # Alert if value < threshold
            if not self.alerting:
                if value < self.threshold:
                    self.alerting = True
                    alert_fired = True
                    self.alert_count += 1
            else:
                if value > (self.threshold + self.hysteresis):
                    self.alerting = False

        elif self.comparison == "equal":
            # Alert only when value == threshold (momentary)
            if value == self.threshold:
                alert_fired = True
                self.alert_count += 1

        self.last_value = value
        return alert_fired

    def is_alerting(self):
        """Check if currently in alert state."""
        return self.alerting

def test_threshold_alert():
    """Test: fire on breach, stay silent on safe series, test hysteresis."""
    # Test 1: greater_than threshold
    alert_gt = ThresholdAlert(threshold=100, comparison="greater_than")

    # Safe values (below threshold)
    assert not alert_gt.check(50), "Should not alert on 50 < 100"
    assert not alert_gt.check(75), "Should not alert on 75 < 100"
    assert not alert_gt.check(100), "Should not alert on 100 == threshold"

    # Breach threshold
    assert alert_gt.check(101), "Should alert on 101 > 100"
    assert alert_gt.is_alerting(), "Should be in alert state"

    # Stay alerting until hysteresis
    assert not alert_gt.check(101), "Should not re-alert while alerting"
    assert not alert_gt.check(100), "Should not alert on 100"
    assert alert_gt.is_alerting(), "Should still be alerting"

    # Recovery below threshold
    assert not alert_gt.check(99), "Should not re-fire on recovery below 100"
    assert not alert_gt.is_alerting(), "Should clear alert state"

    # Test 2: less_than threshold with hysteresis
    alert_lt = ThresholdAlert(threshold=50, comparison="less_than", hysteresis=10)

    # Safe values
    assert not alert_lt.check(60), "Should not alert on 60 > 50"
    assert not alert_lt.check(75), "Should not alert on 75 > 50"

    # Breach threshold
    assert alert_lt.check(49), "Should alert on 49 < 50"
    assert alert_lt.is_alerting(), "Should be in alert state"

    # Hysteresis prevents immediate recovery: must go > (50 + 10) = 60
    assert not alert_lt.check(55), "Should stay alerting at 55"
    assert alert_lt.is_alerting(), "Should still be alerting"

    assert not alert_lt.check(59), "Should stay alerting at 59"
    assert alert_lt.is_alerting(), "Should still be alerting"

    # Above threshold + hysteresis clears alert
    assert not alert_lt.check(61), "Should clear alert on 61 > 60"
    assert not alert_lt.is_alerting(), "Alert should clear"

    # Test 3: equal threshold
    alert_eq = ThresholdAlert(threshold=42, comparison="equal")

    assert not alert_eq.check(41), "Should not alert on 41"
    assert alert_eq.check(42), "Should alert on exact 42"
    assert alert_eq.check(42), "Should alert again on 42"
    assert not alert_eq.check(43), "Should not alert on 43"

    # Test 4: multiple breaches with hysteresis
    alert_multi = ThresholdAlert(threshold=100, comparison="greater_than", hysteresis=10)

    # First breach
    assert alert_multi.check(110), "First breach"
    assert alert_multi.alert_count == 1

    # Recovery within hysteresis (stays alerting)
    assert not alert_multi.check(95), "Should not re-fire during recovery"
    assert alert_multi.is_alerting(), "Still alerting at 95"

    # Fall below hysteresis threshold
    assert not alert_multi.check(85), "Should clear at 85 (< 90)"
    assert not alert_multi.is_alerting(), "Alert cleared"

    # New breach
    assert alert_multi.check(105), "Second breach"
    assert alert_multi.alert_count == 2, f"Should have 2 alerts, got {alert_multi.alert_count}"

    # Test 5: boundary behavior
    alert_boundary = ThresholdAlert(threshold=0, comparison="greater_than")

    assert not alert_boundary.check(0), "0 should not trigger"
    assert alert_boundary.check(0.1), "0.1 should trigger"

    # Test 6: no false positives on constant safe value
    alert_safe = ThresholdAlert(threshold=200, comparison="greater_than")

    for _ in range(10):
        assert not alert_safe.check(100), "Should consistently not alert on safe value"

    assert alert_safe.alert_count == 0, "Should have 0 alerts on safe data"

if __name__ == "__main__":
    test_threshold_alert()
    print("✓ threshold_alert passed")
