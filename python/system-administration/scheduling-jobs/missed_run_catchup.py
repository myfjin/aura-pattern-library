"""Missed run catchup: detect and execute missed scheduled runs.
Failure simulated: job is paused for N intervals; assert all missed runs are caught up.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time
import threading

class MissedRunCatchup:
    def __init__(self, interval=1.0):
        self.interval = interval
        self.last_run_time = None
        self.execution_log = []
        self.lock = threading.Lock()
        self.running = False

    def run_with_catchup(self, callback, current_time=None):
        """Execute callback, catching up missed runs.

        If current_time - last_run_time > interval, calculate missed runs and execute.
        """
        if current_time is None:
            current_time = time.time()

        with self.lock:
            if self.last_run_time is None:
                # First run
                self.last_run_time = current_time
                callback()
                self.execution_log.append(('run', current_time))
                return 1  # 1 execution

            time_since_last = current_time - self.last_run_time
            if time_since_last < self.interval:
                # Not time yet
                return 0

            # Calculate missed runs
            missed_count = int(time_since_last / self.interval)
            executions = 0

            # Catch up all missed runs
            for i in range(missed_count):
                run_time = self.last_run_time + (i + 1) * self.interval
                callback()
                self.execution_log.append(('catchup', run_time))
                executions += 1

            self.last_run_time = current_time
            return executions

    def get_log(self):
        """Return execution log."""
        with self.lock:
            return list(self.execution_log)

    def reset(self):
        """Reset the scheduler."""
        with self.lock:
            self.last_run_time = None
            self.execution_log = []

def test_missed_run_catchup():
    """Simulate failure: pause scheduler for N intervals; assert missed runs are caught up."""
    # Test 1: Single missed interval is caught up
    catchup = MissedRunCatchup(interval=1.0)
    call_count = [0]

    def callback():
        call_count[0] += 1

    # First run at time 0
    catchup.run_with_catchup(callback, current_time=0)
    assert call_count[0] == 1, f"Expected 1 call, got {call_count[0]}"

    # Next run at time 1 (normal interval)
    catchup.run_with_catchup(callback, current_time=1.0)
    assert call_count[0] == 2, f"Expected 2 calls, got {call_count[0]}"

    # Skip ahead 3 intervals (should catch up 3 missed runs)
    catchup.run_with_catchup(callback, current_time=4.0)
    assert call_count[0] == 5, f"Expected 5 calls (2 + 3 missed), got {call_count[0]}"

    log = catchup.get_log()
    assert len(log) == 5, f"Expected 5 log entries, got {len(log)}"
    catchup_entries = [e for e in log if e[0] == 'catchup']
    # 1 catchup at time 1 (interval) + 3 catchups at times 2,3,4 (missed)
    assert len(catchup_entries) == 4, f"Expected 4 catchup entries, got {len(catchup_entries)}"

    # Test 2: No catchup if not enough time has passed
    catchup2 = MissedRunCatchup(interval=1.0)
    call_count[0] = 0

    catchup2.run_with_catchup(callback, current_time=0)
    assert call_count[0] == 1

    # Run at time 0.5 (less than interval, no catchup)
    catchup2.run_with_catchup(callback, current_time=0.5)
    assert call_count[0] == 1, f"Should not run before interval, got {call_count[0]}"

    # Test 3: Large catch-up (10 missed intervals)
    catchup3 = MissedRunCatchup(interval=0.5)
    call_count[0] = 0

    catchup3.run_with_catchup(callback, current_time=0)
    assert call_count[0] == 1

    # Skip 5 seconds (10 intervals missed)
    catchup3.run_with_catchup(callback, current_time=5.0)
    assert call_count[0] == 11, f"Expected 11 calls (1 + 10 missed), got {call_count[0]}"

    log = catchup3.get_log()
    catchup_entries = [e for e in log if e[0] == 'catchup']
    assert len(catchup_entries) == 10, f"Expected 10 catchup entries, got {len(catchup_entries)}"

    # Test 4: Exact interval boundary (no extra runs)
    catchup4 = MissedRunCatchup(interval=1.0)
    call_count[0] = 0

    catchup4.run_with_catchup(callback, current_time=0)
    assert call_count[0] == 1

    # Exactly 3 intervals later
    catchup4.run_with_catchup(callback, current_time=3.0)
    assert call_count[0] == 4, f"Expected 4 calls, got {call_count[0]}"

    # Verify log times
    log = catchup4.get_log()
    run_times = [e[1] for e in log if e[0] != 'run']
    for i, run_time in enumerate(run_times):
        expected = (i + 1) * 1.0
        assert abs(run_time - expected) < 0.01, f"Run time {run_time} doesn't match expected {expected}"

if __name__ == "__main__":
    test_missed_run_catchup()
    print("✓ missed_run_catchup passed all assertions")
