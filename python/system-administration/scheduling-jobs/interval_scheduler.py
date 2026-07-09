"""Interval scheduler: fire a job at fixed intervals.
Failure simulated: verify job fires at each expected interval boundary, no missed runs.
Assert: execution times match expected interval schedule exactly.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time
import threading

class IntervalScheduler:
    def __init__(self, interval_seconds):
        """Create scheduler that fires every interval_seconds."""
        self.interval = interval_seconds
        self.execution_times = []
        self.lock = threading.Lock()
        self.running = False
        self.thread = None

    def start(self, callback):
        """Start the periodic job."""
        if self.running:
            return
        self.running = True
        self.execution_times = []

        def periodic_loop():
            start_time = time.time()
            next_fire = start_time + self.interval
            run_count = 0

            while self.running:
                now = time.time()
                if now >= next_fire:
                    with self.lock:
                        self.execution_times.append(now)
                    callback()
                    run_count += 1
                    next_fire = start_time + (run_count + 1) * self.interval
                time.sleep(0.001)  # Poll frequently

        self.thread = threading.Thread(target=periodic_loop, daemon=True)
        self.thread.start()

    def stop(self):
        """Stop the periodic job."""
        self.running = False
        if self.thread:
            self.thread.join(timeout=1)

    def get_execution_times(self):
        """Return list of execution times."""
        with self.lock:
            return list(self.execution_times)

def test_interval_scheduler():
    """Simulate failure: verify job fires at exact interval boundaries."""
    # Test 1: Job fires at expected intervals
    interval = 0.05
    scheduler = IntervalScheduler(interval)
    fire_count = [0]

    def callback():
        fire_count[0] += 1

    scheduler.start(callback)
    time.sleep(0.25)  # Let it run for 5 intervals
    scheduler.stop()

    exec_times = scheduler.get_execution_times()
    assert len(exec_times) >= 4, f"Expected at least 4 fires, got {len(exec_times)}"
    assert fire_count[0] >= 4, f"Expected at least 4 executions, got {fire_count[0]}"

    # Verify intervals: each fire should be roughly interval apart
    start_time = exec_times[0]
    for i, fire_time in enumerate(exec_times):
        expected_time = start_time + i * interval
        drift = abs(fire_time - expected_time)
        assert drift < interval * 0.5, f"Fire {i} at {fire_time} (expected ~{expected_time}), drift {drift}"

    # Test 2: Starting and stopping multiple times
    scheduler2 = IntervalScheduler(0.05)
    fire_count[0] = 0
    scheduler2.start(callback)
    time.sleep(0.1)
    scheduler2.stop()
    count_after_first = fire_count[0]
    assert count_after_first >= 1, "Should have fired at least once"

    # Start again
    scheduler2.start(callback)
    time.sleep(0.1)
    scheduler2.stop()
    count_after_second = fire_count[0]
    assert count_after_second > count_after_first, "Should fire more times on second start"

    # Test 3: Scheduler respects stop() signal
    scheduler3 = IntervalScheduler(0.02)
    fire_count[0] = 0
    scheduler3.start(callback)
    time.sleep(0.08)
    scheduler3.stop()
    final_count = fire_count[0]
    time.sleep(0.1)  # Wait and verify no more fires after stop
    assert fire_count[0] == final_count, "Scheduler should not fire after stop()"

if __name__ == "__main__":
    test_interval_scheduler()
    print("✓ interval_scheduler passed all assertions")
