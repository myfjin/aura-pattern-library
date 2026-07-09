"""Dead letter queue: move jobs to DLQ after N consecutive failures.
Failure simulated: job fails N times; assert it moves to DLQ exactly once.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import threading
from collections import deque

class DeadLetterQueue:
    def __init__(self, max_retries=3):
        self.max_retries = max_retries
        self.dlq = deque()  # Dead letter queue
        self.dlq_lock = threading.Lock()
        self.job_state = {}  # job_id -> {'failures': int, 'in_dlq': bool}
        self.state_lock = threading.Lock()

    def execute_with_dlq(self, job_id, callback):
        """Execute job, move to DLQ on repeated failures.

        Returns: ('success', None) or ('dlq', error_msg) or ('retry', error_msg).
        """
        with self.state_lock:
            if job_id not in self.job_state:
                self.job_state[job_id] = {'failures': 0, 'in_dlq': False}
            state = self.job_state[job_id]

        try:
            callback()
            # Success: reset failure count
            with self.state_lock:
                state['failures'] = 0
            return ('success', None)

        except Exception as e:
            error_msg = str(e)
            with self.state_lock:
                state['failures'] += 1
                if state['failures'] >= self.max_retries:
                    if not state['in_dlq']:
                        state['in_dlq'] = True
                        # Move to DLQ
                        with self.dlq_lock:
                            self.dlq.append({
                                'job_id': job_id,
                                'error': error_msg,
                                'failure_count': state['failures']
                            })
                        return ('dlq', error_msg)
                    else:
                        # Already in DLQ, don't re-add
                        return ('dlq', error_msg)

            return ('retry', error_msg)

    def get_dlq(self):
        """Get list of jobs in DLQ."""
        with self.dlq_lock:
            return list(self.dlq)

    def get_dlq_count(self):
        """Get number of jobs in DLQ."""
        with self.dlq_lock:
            return len(self.dlq)

    def get_job_state(self, job_id):
        """Get state of a job."""
        with self.state_lock:
            return dict(self.job_state.get(job_id, {}))

def test_dead_letter_queue():
    """Simulate failure: job fails N times; assert it moves to DLQ exactly once."""
    # Test 1: Job fails N times, then moves to DLQ on (N+1)th attempt
    dlq = DeadLetterQueue(max_retries=3)

    def failing_job():
        raise RuntimeError("Persistent failure")

    # First 3 failures should return 'retry'
    result1, msg1 = dlq.execute_with_dlq("job_1", failing_job)
    assert result1 == 'retry', f"Expected 'retry' on 1st failure, got {result1}"

    result2, msg2 = dlq.execute_with_dlq("job_1", failing_job)
    assert result2 == 'retry', f"Expected 'retry' on 2nd failure, got {result2}"

    result3, msg3 = dlq.execute_with_dlq("job_1", failing_job)
    assert result3 == 'dlq', f"Expected 'dlq' on 3rd failure (max_retries reached), got {result3}"

    # Check DLQ
    dlq_items = dlq.get_dlq()
    assert len(dlq_items) == 1, f"Expected 1 item in DLQ, got {len(dlq_items)}"
    assert dlq_items[0]['job_id'] == 'job_1', "DLQ should contain job_1"
    assert dlq_items[0]['failure_count'] == 3, "Failure count should be 3"

    # Subsequent failures should not re-add to DLQ
    result4, msg4 = dlq.execute_with_dlq("job_1", failing_job)
    assert result4 == 'dlq', f"Expected 'dlq' on 4th failure, got {result4}"
    dlq_items = dlq.get_dlq()
    assert len(dlq_items) == 1, f"DLQ should still have 1 item (not re-added), got {len(dlq_items)}"

    # Test 2: Job succeeds, failure count resets
    dlq2 = DeadLetterQueue(max_retries=2)
    fail_count = [0]

    def fail_then_succeed():
        fail_count[0] += 1
        if fail_count[0] <= 1:
            raise RuntimeError("First call fails")

    result1, _ = dlq2.execute_with_dlq("job_2", fail_then_succeed)
    assert result1 == 'retry', "First failure should retry"

    result2, _ = dlq2.execute_with_dlq("job_2", fail_then_succeed)
    assert result2 == 'success', "Second call should succeed"

    # Verify failure count reset
    state = dlq2.get_job_state("job_2")
    assert state['failures'] == 0, f"Failures should reset to 0, got {state['failures']}"

    # Test 3: Multiple jobs to DLQ
    dlq3 = DeadLetterQueue(max_retries=1)
    dlq_count = [0]

    def always_fail(msg):
        raise RuntimeError(msg)

    # Job A fails
    dlq3.execute_with_dlq("job_a", lambda: always_fail("A fails"))
    assert dlq3.get_dlq_count() == 1, "DLQ should have 1 job"

    # Job B fails (different job_id)
    dlq3.execute_with_dlq("job_b", lambda: always_fail("B fails"))
    assert dlq3.get_dlq_count() == 2, "DLQ should have 2 jobs"

    dlq_items = dlq3.get_dlq()
    job_ids = {item['job_id'] for item in dlq_items}
    assert job_ids == {'job_a', 'job_b'}, f"DLQ should contain both jobs, got {job_ids}"

    # Test 4: Job with max_retries=1 (fails immediately on second attempt)
    dlq4 = DeadLetterQueue(max_retries=1)
    fail_count[0] = 0

    def fail_first():
        fail_count[0] += 1
        raise RuntimeError("Always fails")

    result1, _ = dlq4.execute_with_dlq("job_4", fail_first)
    assert result1 == 'dlq', "Should go to DLQ on first failure when max_retries=1"
    assert dlq4.get_dlq_count() == 1, "Should have 1 item in DLQ"

    # Test 5: Multiple failures then success - once in DLQ, stays in DLQ
    dlq5 = DeadLetterQueue(max_retries=2)

    def persistent_failure():
        raise RuntimeError("Persistent failure")

    result1, _ = dlq5.execute_with_dlq("job_5", persistent_failure)
    assert result1 == 'retry', "Call 1: should retry"

    result2, _ = dlq5.execute_with_dlq("job_5", persistent_failure)
    assert result2 == 'dlq', "Call 2: should go to DLQ (max_retries=2)"
    assert dlq5.get_dlq_count() == 1, "Should have 1 item in DLQ"

    # After it's in DLQ, subsequent attempts shouldn't add duplicates
    result3, _ = dlq5.execute_with_dlq("job_5", persistent_failure)
    assert result3 == 'dlq', "Call 3: should remain in DLQ"
    assert dlq5.get_dlq_count() == 1, "Should still have 1 item (no duplicates)"

if __name__ == "__main__":
    test_dead_letter_queue()
    print("✓ dead_letter_queue passed all assertions")
