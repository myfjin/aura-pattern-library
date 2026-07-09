"""Oneshot scheduler: fire a job exactly once at a specified time.
Failure simulated: oneshot is submitted multiple times; assert it fires exactly once.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time
import threading
from collections import defaultdict

class OneShotScheduler:
    def __init__(self):
        self.scheduled_jobs = {}  # key -> (target_time, executed, lock)
        self.execution_count = defaultdict(int)

    def schedule(self, job_key, target_time, callback):
        """Schedule a job to fire at target_time (Unix timestamp).
        If the same job_key is scheduled again before firing, the old schedule is replaced.
        """
        if job_key in self.scheduled_jobs:
            old_entry = self.scheduled_jobs[job_key]
            old_entry['lock'].acquire()
            try:
                if not old_entry['executed']:
                    # Cancel the old job
                    if 'thread' in old_entry:
                        old_entry['cancel'] = True
                    del self.scheduled_jobs[job_key]
            finally:
                old_entry['lock'].release()

        lock = threading.Lock()
        job_entry = {'target_time': target_time, 'executed': False, 'cancel': False, 'lock': lock}

        def wait_and_execute():
            while True:
                now = time.time()
                if now >= target_time:
                    with lock:
                        if job_entry['cancel']:
                            return
                        if not job_entry['executed']:
                            job_entry['executed'] = True
                            self.execution_count[job_key] += 1
                            callback()
                    return
                time.sleep(0.01)

        thread = threading.Thread(target=wait_and_execute, daemon=True)
        job_entry['thread'] = thread
        self.scheduled_jobs[job_key] = job_entry
        thread.start()

    def wait_all(self, timeout=10):
        """Wait for all jobs to complete or timeout."""
        end_time = time.time() + timeout
        while time.time() < end_time:
            if all(job['executed'] for job in self.scheduled_jobs.values()):
                return
            time.sleep(0.01)

    def get_count(self, job_key):
        """Return execution count for a job_key."""
        return self.execution_count[job_key]

def test_oneshot_at_time():
    """Simulate failure: schedule same oneshot multiple times; assert it fires exactly once."""
    scheduler = OneShotScheduler()
    fire_count = [0]

    def callback():
        fire_count[0] += 1

    # Test 1: Single oneshot fires exactly once at the target time
    target = time.time() + 0.1
    scheduler.schedule("job1", target, callback)
    scheduler.wait_all(timeout=2)
    assert fire_count[0] == 1, f"Expected 1 execution, got {fire_count[0]}"
    assert scheduler.get_count("job1") == 1, f"Execution count mismatch"

    # Test 2: Rescheduling same job_key before fire cancels old schedule
    fire_count[0] = 0
    target1 = time.time() + 10  # Far in future, will be replaced
    target2 = time.time() + 0.1  # Near future
    scheduler.schedule("job2", target1, callback)
    scheduler.schedule("job2", target2, callback)  # Replace with new target
    scheduler.wait_all(timeout=2)
    assert fire_count[0] == 1, f"Expected 1 execution after reschedule, got {fire_count[0]}"
    assert scheduler.get_count("job2") == 1, f"Execution count should be 1, got {scheduler.get_count('job2')}"

    # Test 3: Multiple different jobs each fire exactly once
    fire_count[0] = 0
    target = time.time() + 0.1
    scheduler.schedule("job3a", target, callback)
    scheduler.schedule("job3b", target, callback)
    scheduler.schedule("job3c", target, callback)
    scheduler.wait_all(timeout=2)
    assert fire_count[0] == 3, f"Expected 3 executions, got {fire_count[0]}"
    assert scheduler.get_count("job3a") == 1
    assert scheduler.get_count("job3b") == 1
    assert scheduler.get_count("job3c") == 1

    # Test 4: Job that fires in the past fires immediately, exactly once
    fire_count[0] = 0
    target = time.time() - 1  # Already in the past
    scheduler.schedule("job4", target, callback)
    scheduler.wait_all(timeout=1)
    assert fire_count[0] == 1, f"Expected 1 execution for past target, got {fire_count[0]}"

if __name__ == "__main__":
    test_oneshot_at_time()
    print("✓ oneshot_at_time passed all assertions")
