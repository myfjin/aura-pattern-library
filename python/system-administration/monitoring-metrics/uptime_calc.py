#!/usr/bin/env python3
"""uptime_calc: calculate uptime percentage from events."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys

class UptimeCalculator:
    """Calculate uptime from state change events."""
    def __init__(self):
        self.events = []  # List of (timestamp, state) where state is True (up) or False (down)

    def add_event(self, timestamp, state):
        """Record state change at timestamp."""
        self.events.append((timestamp, state))

    def calculate_uptime(self, start_time, end_time):
        """Calculate uptime percentage for time range."""
        if start_time >= end_time:
            return 100.0  # Edge case

        # Get all events in range, sorted
        relevant_events = [(t, s) for t, s in self.events if start_time <= t <= end_time]
        relevant_events.sort()

        if not relevant_events:
            # No events in range, assume up
            return 100.0

        # Determine initial state (assume up if no earlier event)
        initial_state = True
        if self.events and self.events[0][0] > start_time:
            initial_state = True
        elif self.events:
            # Find state just before start_time
            for t, s in self.events:
                if t < start_time:
                    initial_state = s
                else:
                    break

        current_state = initial_state
        up_time = 0
        last_timestamp = start_time

        for timestamp, new_state in relevant_events:
            # Add time up to this event
            if current_state:
                up_time += timestamp - last_timestamp
            last_timestamp = timestamp
            current_state = new_state

        # Add remaining time
        if current_state:
            up_time += end_time - last_timestamp

        total_time = end_time - start_time
        if total_time <= 0:
            return 100.0

        uptime_percent = (up_time / total_time) * 100.0
        return min(100.0, max(0.0, uptime_percent))

def test_uptime_calc():
    """Test: calculate uptime from known outage events."""
    # Test 1: all up
    calc = UptimeCalculator()
    # No events means always up
    uptime_all_up = calc.calculate_uptime(0, 1000)
    assert uptime_all_up == 100.0, f"No outages should be 100% uptime, got {uptime_all_up}%"

    # Test 2: one outage
    calc2 = UptimeCalculator()
    calc2.add_event(100, False)  # Goes down at t=100
    calc2.add_event(200, True)   # Comes back up at t=200

    # 0-500: 100 seconds down (100-200), 400 up = 80%
    uptime_2 = calc2.calculate_uptime(0, 500)
    assert uptime_2 == 80.0, f"With 100s outage in 500s should be 80%, got {uptime_2}%"

    # Test 3: multiple outages
    calc3 = UptimeCalculator()
    # 0-50: up, 50-100: down, 100-200: up, 200-250: down, 250-500: up
    calc3.add_event(50, False)
    calc3.add_event(100, True)
    calc3.add_event(200, False)
    calc3.add_event(250, True)

    # Total downtime: (100-50) + (250-200) = 50 + 50 = 100 seconds
    # Total time: 500 seconds
    # Uptime: 400/500 = 80%
    uptime_3 = calc3.calculate_uptime(0, 500)
    assert uptime_3 == 80.0, f"With two 50s outages should be 80%, got {uptime_3}%"

    # Test 4: window filtering
    calc4 = UptimeCalculator()
    calc4.add_event(100, False)
    calc4.add_event(200, True)
    calc4.add_event(400, False)
    calc4.add_event(500, True)

    # Window 0-250: up(0-100) + down(100-200) + up(200-250) = 100s + 100s + 50s = 150s up
    # Uptime: 150/250 = 60%
    uptime_partial = calc4.calculate_uptime(0, 250)
    assert uptime_partial == 60.0, f"Partial window should show 60%, got {uptime_partial}%"

    # Window 250-550: second outage (400-500) in 300s window = 200/300 = 66.67%
    uptime_partial2 = calc4.calculate_uptime(250, 550)
    expected = (200.0 / 300.0) * 100.0
    assert abs(uptime_partial2 - expected) < 0.1, f"Expected ~66.67%, got {uptime_partial2}%"

    # Test 5: nine nines (99.9% uptime)
    # To get 99.9% in 1M seconds: 0.1% downtime = 1000 seconds down
    calc5 = UptimeCalculator()
    calc5.add_event(500000, False)
    calc5.add_event(501000, True)

    uptime_nines = calc5.calculate_uptime(0, 1000000)
    expected_nines = (999000 / 1000000) * 100.0
    assert abs(uptime_nines - expected_nines) < 0.01, f"Expected 99.9%, got {uptime_nines}%"

    # Test 6: starts down
    calc6 = UptimeCalculator()
    calc6.add_event(0, False)
    calc6.add_event(100, True)

    # 0-200: down 0-100, up 100-200 = 100 up / 200 total = 50%
    uptime_starts_down = calc6.calculate_uptime(0, 200)
    assert uptime_starts_down == 50.0, f"Starts down should be 50%, got {uptime_starts_down}%"

    # Test 7: fractional percent
    calc7 = UptimeCalculator()
    calc7.add_event(333, False)
    calc7.add_event(667, True)

    # 0-1000: 333 down / 1000 total = 66.7% up
    uptime_frac = calc7.calculate_uptime(0, 1000)
    expected_frac = (667 / 1000) * 100.0
    assert abs(uptime_frac - expected_frac) < 0.1, f"Expected 66.7%, got {uptime_frac}%"

if __name__ == "__main__":
    test_uptime_calc()
    print("✓ uptime_calc passed")
