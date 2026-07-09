"""Idempotency key: same key submitted twice → operation runs exactly once.
Failure simulated: submit same key twice concurrently; assert callback fires once.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import threading
import hashlib
from collections import defaultdict

class IdempotencyStore:
    def __init__(self):
        self.executed_keys = {}  # key -> (result, timestamp)
        self.key_locks = {}  # key -> threading.Lock
        self.global_lock = threading.Lock()
        self.execution_log = []

    def execute_idempotent(self, idempotency_key, callback):
        """Execute callback exactly once per idempotency_key.

        If the key has been seen before, return the cached result or re-raise cached exception.
        Returns: (was_executed, result).
        """
        # Get or create lock for this key
        with self.global_lock:
            if idempotency_key not in self.key_locks:
                self.key_locks[idempotency_key] = threading.Lock()
            key_lock = self.key_locks[idempotency_key]

        # Check if already executed (fast path, no lock)
        if idempotency_key in self.executed_keys:
            result, _ = self.executed_keys[idempotency_key]
            self.execution_log.append(('cached', idempotency_key))
            if isinstance(result, Exception):
                raise result  # Re-raise cached exception
            return (False, result)

        # Try to execute (slow path, with lock)
        acquired = key_lock.acquire(blocking=True, timeout=5)
        if not acquired:
            # Could not acquire lock, return error
            return (False, None)

        try:
            # Double-check after acquiring lock
            if idempotency_key in self.executed_keys:
                result, _ = self.executed_keys[idempotency_key]
                self.execution_log.append(('dup_cached', idempotency_key))
                if isinstance(result, Exception):
                    raise result  # Re-raise cached exception
                return (False, result)

            # Execute the callback
            try:
                result = callback()
                self.executed_keys[idempotency_key] = (result, threading.current_thread().ident)
                self.execution_log.append(('executed', idempotency_key))
                return (True, result)
            except Exception as e:
                # Store the error as the result
                self.executed_keys[idempotency_key] = (e, threading.current_thread().ident)
                self.execution_log.append(('executed_with_error', idempotency_key))
                raise

        finally:
            key_lock.release()

    def get_log(self):
        """Return execution log."""
        return list(self.execution_log)

    def get_result(self, key):
        """Get cached result for a key."""
        if key in self.executed_keys:
            result, _ = self.executed_keys[key]
            return result
        return None

def test_idempotency_key():
    """Simulate failure: submit same key twice concurrently; assert callback fires once."""
    # Test 1: Same key submitted twice concurrently → executes once
    store = IdempotencyStore()
    exec_count = [0]
    barrier = threading.Barrier(2)

    def increment_callback():
        exec_count[0] += 1
        return exec_count[0]

    def submit_job(key):
        barrier.wait()  # Sync both threads
        was_executed, result = store.execute_idempotent(key, increment_callback)
        return (was_executed, result)

    results = []

    def thread_work(key):
        results.append(submit_job(key))

    t1 = threading.Thread(target=thread_work, args=("key1",))
    t2 = threading.Thread(target=thread_work, args=("key1",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # Exactly one should have executed, one should have gotten cached result
    assert exec_count[0] == 1, f"Expected 1 execution, got {exec_count[0]}"
    assert len(results) == 2, f"Expected 2 results, got {len(results)}"

    # One should be (True, 1), one should be (False, 1)
    executed_flags = [r[0] for r in results]
    result_values = [r[1] for r in results]

    assert sum(executed_flags) == 1, f"Expected 1 execution flag, got {sum(executed_flags)}"
    assert result_values[0] == result_values[1], "Both should return same result"

    # Test 2: Different keys execute independently
    store2 = IdempotencyStore()
    exec_count[0] = 0

    results = []

    def sync_submit(key):
        barrier.wait()
        was_executed, result = store2.execute_idempotent(key, increment_callback)
        results.append((was_executed, result))

    barrier = threading.Barrier(2)
    t1 = threading.Thread(target=sync_submit, args=("key_a",))
    t2 = threading.Thread(target=sync_submit, args=("key_b",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    assert exec_count[0] == 2, f"Expected 2 executions (different keys), got {exec_count[0]}"
    assert all(r[0] for r in results), "Both should have executed"

    # Test 3: Sequential submissions with same key
    store3 = IdempotencyStore()
    exec_count[0] = 0

    was_exec1, result1 = store3.execute_idempotent("key_seq", increment_callback)
    assert was_exec1 is True, "First submission should execute"
    assert result1 == 1, f"Expected result 1, got {result1}"

    was_exec2, result2 = store3.execute_idempotent("key_seq", increment_callback)
    assert was_exec2 is False, "Second submission should be cached"
    assert result2 == 1, f"Expected cached result 1, got {result2}"

    was_exec3, result3 = store3.execute_idempotent("key_seq", increment_callback)
    assert was_exec3 is False, "Third submission should be cached"
    assert result3 == 1, f"Expected cached result 1, got {result3}"

    assert exec_count[0] == 1, f"Expected 1 total execution, got {exec_count[0]}"

    # Test 4: Exception is also idempotent
    store4 = IdempotencyStore()
    call_count = [0]

    def failing_callback():
        call_count[0] += 1
        raise ValueError("Test error")

    try:
        was_exec1, _ = store4.execute_idempotent("error_key", failing_callback)
        assert False, "First call should raise"
    except ValueError as e:
        assert "Test error" in str(e), "Should raise test error"

    # Second call should raise the cached exception
    try:
        was_exec2, _ = store4.execute_idempotent("error_key", failing_callback)
        assert False, "Should have raised cached exception"
    except ValueError as e:
        assert "Test error" in str(e), "Should raise same error"

    assert call_count[0] == 1, f"Callback should only be called once, got {call_count[0]}"

    # Test 5: Execution log tracks idempotent behavior (sequential calls take fast path)
    store5 = IdempotencyStore()
    exec_count[0] = 0

    for i in range(3):
        store5.execute_idempotent("key_log", lambda: exec_count[0] + 1)

    log = store5.get_log()
    # First should be 'executed', subsequent are 'cached' (fast path, no lock needed)
    assert log[0][0] == 'executed', f"First should be executed, got {log[0]}"
    assert log[1][0] == 'cached', f"Second should be cached (fast path), got {log[1]}"
    assert log[2][0] == 'cached', f"Third should be cached (fast path), got {log[2]}"

if __name__ == "__main__":
    test_idempotency_key()
    print("✓ idempotency_key passed all assertions")
