"""Rate limiting using sliding time window."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class SlidingRateWindow:
    """Track event count in a sliding time window."""

    def __init__(self, clock_fn, window_seconds, max_events):
        """Init with clock, window size, and max events allowed."""
        self.clock_fn = clock_fn
        self.window_seconds = window_seconds
        self.max_events = max_events
        self.events = []  # List of (timestamp, count) tuples

    def is_allowed(self):
        """Check if next event is allowed. Return True if allowed."""
        current = self.clock_fn()
        window_start = current - self.window_seconds

        # Remove expired events outside the window
        self.events = [
            (ts, count) for ts, count in self.events
            if ts >= window_start
        ]

        # Count total events in window
        total_in_window = sum(count for _, count in self.events)

        if total_in_window >= self.max_events:
            return False

        # Record this event
        self.events.append((current, 1))
        return True

    def get_event_count(self):
        """Return current event count in window."""
        current = self.clock_fn()
        window_start = current - self.window_seconds

        self.events = [
            (ts, count) for ts, count in self.events
            if ts >= window_start
        ]

        return sum(count for _, count in self.events)


def test_allow_within_limit():
    """Test: allow events within rate limit."""
    clock_value = [1000.0]

    def mock_clock():
        return clock_value[0]

    window = SlidingRateWindow(mock_clock, window_seconds=10.0, max_events=3)

    # Add 3 events (at limit)
    assert window.is_allowed() is True
    assert window.is_allowed() is True
    assert window.is_allowed() is True
    assert window.get_event_count() == 3


def test_reject_over_limit():
    """Test: reject events exceeding rate limit."""
    clock_value = [1000.0]

    def mock_clock():
        return clock_value[0]

    window = SlidingRateWindow(mock_clock, window_seconds=10.0, max_events=2)

    # Add 2 events
    assert window.is_allowed() is True
    assert window.is_allowed() is True

    # SIMULATE FAILURE: 3rd event should be rejected
    allowed = window.is_allowed()
    assert allowed is False, "3rd event should be rejected (over limit of 2)"


def test_sliding_window_expires_old_events():
    """Test: old events drop out of window."""
    clock_value = [1000.0]

    def mock_clock():
        return clock_value[0]

    window = SlidingRateWindow(mock_clock, window_seconds=10.0, max_events=2)

    # Add 2 events at time 1000
    assert window.is_allowed() is True
    assert window.is_allowed() is True

    # 3rd event at 1000 should be rejected
    assert window.is_allowed() is False

    # SIMULATE FAILURE -> SUCCESS: advance time past window
    clock_value[0] = 1011.0  # Old events are now > 10 seconds old

    # Now 3rd event should be allowed (old events expired)
    assert window.is_allowed() is True, "Old events should expire, allowing new event"
    assert window.get_event_count() == 1


def test_multiple_event_bursts():
    """Test: rate limit across multiple bursts."""
    clock_value = [1000.0]

    def mock_clock():
        return clock_value[0]

    window = SlidingRateWindow(mock_clock, window_seconds=10.0, max_events=3)

    # Burst 1: add 3 events
    window.is_allowed()
    window.is_allowed()
    window.is_allowed()

    # 4th would be rejected
    assert window.is_allowed() is False

    # Advance to 1006 (inside window, but some events start expiring at 1011)
    clock_value[0] = 1006.0

    # Still at limit
    assert window.is_allowed() is False

    # Advance to 1012 (all old events expired)
    clock_value[0] = 1012.0

    # Now can add more
    assert window.is_allowed() is True
    assert window.get_event_count() == 1


if __name__ == "__main__":
    test_allow_within_limit()
    test_reject_over_limit()
    test_sliding_window_expires_old_events()
    test_multiple_event_bursts()
    print("✓ sliding_rate_window passed")
