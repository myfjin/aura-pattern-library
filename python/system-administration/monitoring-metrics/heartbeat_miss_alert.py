#!/usr/bin/env python3
"""heartbeat_miss_alert: detect heartbeat/watchdog timeouts."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys

class HeartbeatMissAlert:
    """Detect missed heartbeats and fire alerts."""
    def __init__(self, timeout_seconds=60):
        self.timeout_seconds = timeout_seconds
        self.last_heartbeat = None
        self.alerting = False
        self.alert_count = 0

    def heartbeat(self, timestamp):
        """Record heartbeat at timestamp."""
        self.last_heartbeat = timestamp

        # Clear alert if we get heartbeat
        if self.alerting:
            self.alerting = False

    def check(self, current_timestamp):
        """Check if timeout exceeded, fire alert if missed."""
        alert_fired = False

        if self.last_heartbeat is None:
            # No heartbeat yet
            if current_timestamp > self.timeout_seconds:
                if not self.alerting:
                    self.alerting = True
                    alert_fired = True
                    self.alert_count += 1
        else:
            elapsed = current_timestamp - self.last_heartbeat
            if elapsed > self.timeout_seconds:
                if not self.alerting:
                    self.alerting = True
                    alert_fired = True
                    self.alert_count += 1
            else:
                # Within timeout, clear alert
                self.alerting = False

        return alert_fired

    def is_alerting(self):
        """Check if currently alerting."""
        return self.alerting

def test_heartbeat_miss_alert():
    """Test: fire on timeout, clear on heartbeat, no false alarms."""
    # Test 1: normal heartbeats, no alert
    alert = HeartbeatMissAlert(timeout_seconds=30)

    # Heartbeats every 10 seconds
    alert.heartbeat(0)
    assert not alert.check(10), "Should not alert with fresh heartbeat"
    assert not alert.is_alerting()

    alert.heartbeat(10)
    assert not alert.check(20), "Should not alert within timeout"
    assert not alert.is_alerting()

    # Test 2: missed heartbeat fires alert
    alert2 = HeartbeatMissAlert(timeout_seconds=60)

    alert2.heartbeat(0)
    assert not alert2.check(30), "Should not alert at 30s (within 60s)"
    assert not alert2.check(59), "Should not alert at 59s (within 60s)"

    # Timeout exceeded
    assert alert2.check(61), "Should fire alert at 61s (> 60s timeout)"
    assert alert2.is_alerting(), "Should be in alert state"

    # Stay alerting until heartbeat
    assert not alert2.check(70), "Should not re-fire while already alerting"
    assert alert2.is_alerting(), "Should still be alerting"

    assert not alert2.check(100), "Should stay alerting even at 100s"
    assert alert2.is_alerting()

    # Heartbeat clears alert
    alert2.heartbeat(100)
    assert not alert2.check(101), "Heartbeat should clear alert"
    assert not alert2.is_alerting(), "Should clear alert state"

    # Test 3: no initial heartbeat
    alert3 = HeartbeatMissAlert(timeout_seconds=30)

    # Time advances without heartbeat
    assert not alert3.check(10), "Should not alert before timeout"
    assert not alert3.check(29), "Should not alert at 29s"

    # Timeout exceeded with no heartbeat
    assert alert3.check(31), "Should fire alert with no heartbeat"
    assert alert3.is_alerting()

    # Test 4: multiple miss/recover cycles
    alert4 = HeartbeatMissAlert(timeout_seconds=20)

    # Cycle 1: normal
    alert4.heartbeat(0)
    assert not alert4.check(15)

    # Cycle 2: miss
    assert alert4.check(25), "Should fire on miss"
    assert alert4.alert_count == 1

    # Recover
    alert4.heartbeat(30)
    assert not alert4.check(35)
    assert not alert4.is_alerting()

    # Cycle 3: miss again
    assert alert4.check(60), "Should fire again on second miss"
    assert alert4.alert_count == 2

    # Recover again
    alert4.heartbeat(61)
    assert not alert4.is_alerting()

    # Test 5: boundary conditions
    alert5 = HeartbeatMissAlert(timeout_seconds=100)

    alert5.heartbeat(50)
    assert not alert5.check(150), "Should not alert at exactly 100s since heartbeat"
    # Actually: 150 - 50 = 100, which is NOT > 100, so no alert yet

    assert alert5.check(151), "Should alert at 101s since heartbeat"
    assert alert5.alert_count == 1

    # Test 6: verify no false positives on constant heartbeats
    alert6 = HeartbeatMissAlert(timeout_seconds=10)

    for t in range(0, 100, 5):
        alert6.heartbeat(t)
        result = alert6.check(t + 1)
        assert not result, f"Should not alert with regular heartbeats at t={t}"

    assert alert6.alert_count == 0, "Should have 0 alerts with good heartbeats"

    # Test 7: alert on missed single heartbeat
    alert7 = HeartbeatMissAlert(timeout_seconds=30)

    alert7.heartbeat(0)
    assert not alert7.check(15)
    # Miss next heartbeat, just check at 40s
    assert alert7.check(40), "Should detect single missed heartbeat"

if __name__ == "__main__":
    test_heartbeat_miss_alert()
    print("✓ heartbeat_miss_alert passed")
