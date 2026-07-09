"""Job dedup: ensure only one instance of a job runs at a time.
Failure simulated: launch same job twice concurrently; assert only one runs.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import threading
import time
import os
import tempfile

class JobDedup:
    def __init__(self):
        self.locks = {}
        self.global_lock = threading.Lock()
        self.execution_count = {}

    def run_job(self, job_id, callback, timeout=5):
        """Run job with dedup. Only one instance per job_id can run.

        Returns True if this call executed the job, False if blocked by another instance.
        """
        with self.global_lock:
            if job_id not in self.locks:
                self.locks[job_id] = threading.Lock()
            job_lock = self.locks[job_id]

        # Try to acquire lock with timeout
        acquired = job_lock.acquire(blocking=True, timeout=timeout)
        if not acquired:
            return False  # Blocked by another instance

        try:
            # We got the lock, execute the job
            if job_id not in self.execution_count:
                self.execution_count[job_id] = 0
            self.execution_count[job_id] += 1
            callback()
            return True
        finally:
            job_lock.release()

    def get_count(self, job_id):
        """Get execution count for a job."""
        return self.execution_count.get(job_id, 0)

def test_job_dedup():
    """Simulate failure: launch same job twice concurrently; assert only one runs."""
    # Test 1: Concurrent launches of same job — only one executes
    dedup = JobDedup()
    exec_results = []
    exec_count = [0]
    hold_lock = threading.Lock()
    hold_lock.acquire()  # Acquire the hold lock

    def long_running_job():
        hold_lock.acquire()  # Wait for hold lock (will block thread 1)
        hold_lock.release()
        exec_count[0] += 1

    def launch_job(job_name):
        result = dedup.run_job(job_name, long_running_job, timeout=0.3)
        exec_results.append(result)

    thread1 = threading.Thread(target=launch_job, args=("job_a",))
    thread2 = threading.Thread(target=launch_job, args=("job_a",))

    time.sleep(0.1)  # Small delay before starting
    thread1.start()
    time.sleep(0.05)  # Let thread1 acquire job lock and start holding hold_lock
    thread2.start()
    time.sleep(0.4)  # Let thread2 timeout

    hold_lock.release()  # Release hold lock to let thread1 complete

    thread1.join()
    thread2.join()

    # Exactly one should have acquired the lock
    assert sum(exec_results) == 1, f"Expected 1 successful execution, got {sum(exec_results)}"
    assert exec_count[0] == 1, f"Expected 1 actual callback execution, got {exec_count[0]}"
    assert dedup.get_count("job_a") == 1, "Job count should be 1"

    # Test 2: Different jobs run in parallel
    dedup2 = JobDedup()
    exec_count[0] = 0
    results = {'job_b': 0, 'job_c': 0}
    results_lock = threading.Lock()

    def job_b_work():
        time.sleep(0.1)
        with results_lock:
            results['job_b'] += 1

    def job_c_work():
        time.sleep(0.1)
        with results_lock:
            results['job_c'] += 1

    barrier = threading.Barrier(2)

    def run_job_b():
        barrier.wait()
        dedup2.run_job("job_b", job_b_work)

    def run_job_c():
        barrier.wait()
        dedup2.run_job("job_c", job_c_work)

    t1 = threading.Thread(target=run_job_b)
    t2 = threading.Thread(target=run_job_c)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    assert results['job_b'] == 1, f"job_b should run once, got {results['job_b']}"
    assert results['job_c'] == 1, f"job_c should run once, got {results['job_c']}"

    # Test 3: Timeout blocks excess concurrent launches
    dedup3 = JobDedup()
    blocked_count = [0]
    acquired_count = [0]
    barrier = threading.Barrier(3)
    job_start = threading.Event()
    job_continue = threading.Event()

    def slow_job():
        job_start.set()
        job_continue.wait()
        time.sleep(0.05)

    def try_launch():
        barrier.wait()
        result = dedup3.run_job("job_slow", slow_job, timeout=0.1)
        if result:
            acquired_count[0] += 1
        else:
            blocked_count[0] += 1

    threads = [threading.Thread(target=try_launch) for _ in range(3)]
    for t in threads:
        t.start()

    job_start.wait()
    time.sleep(0.15)  # Let timeout expire
    job_continue.set()

    for t in threads:
        t.join()

    # First thread should acquire, others should be blocked or timeout
    assert acquired_count[0] == 1, f"Expected 1 acquisition, got {acquired_count[0]}"
    assert blocked_count[0] >= 1, f"Expected at least 1 blocked, got {blocked_count[0]}"

    # Test 4: Sequential runs of same job (not concurrent) all execute
    dedup4 = JobDedup()
    call_count = [0]

    def simple_callback():
        call_count[0] += 1

    result1 = dedup4.run_job("job_seq", simple_callback)
    result2 = dedup4.run_job("job_seq", simple_callback)
    result3 = dedup4.run_job("job_seq", simple_callback)

    assert result1 and result2 and result3, "Sequential runs should all succeed"
    assert call_count[0] == 3, f"Expected 3 executions, got {call_count[0]}"
    assert dedup4.get_count("job_seq") == 3, "Count should be 3"

if __name__ == "__main__":
    test_job_dedup()
    print("✓ job_dedup passed all assertions")
