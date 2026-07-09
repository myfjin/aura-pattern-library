"""
deadlock_timeout: detect and break potential deadlocks with a timeout mechanism.
Failure simulated: two threads try to acquire locks in opposite order (A: lock1→lock2,
B: lock2→lock1), creating a cycle. Without timeouts, this deadlocks forever. With timeouts,
the second-to-acquire times out and backs off.
Recovery asserted: at least one thread times out (detecting the deadlock cycle) and retreats,
allowing both threads to finish. A no-op timeout would hang forever.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import threading
import time
import random

class TimeoutLock:
    """A lock with timeout support."""
    def __init__(self):
        self._condition = threading.Condition()
        self._owner = None

    def acquire(self, timeout=None):
        """Acquire with timeout. Returns True if acquired, False if timeout."""
        start = time.time()
        with self._condition:
            while self._owner is not None:
                if timeout is not None:
                    elapsed = time.time() - start
                    if elapsed >= timeout:
                        return False
                    remaining = timeout - elapsed
                    self._condition.wait(timeout=remaining)
                else:
                    self._condition.wait()

            # We got the lock
            self._owner = threading.current_thread().ident
            return True

    def release(self):
        """Release the lock."""
        with self._condition:
            self._owner = None
            self._condition.notify_all()

def acquirer(lock1, lock2, lock_order, results, thread_id, timeout, barrier):
    """Acquire locks in order. Barrier ensures both threads start at the same time."""
    acquired = []
    try:
        # Wait for both threads to be ready
        barrier.wait()

        # Acquire locks in order
        for lock_id in lock_order:
            lock = lock1 if lock_id == 1 else lock2
            if lock.acquire(timeout=timeout):
                acquired.append(lock_id)
                # Hold lock briefly to increase chance of deadlock
                time.sleep(0.02)
            else:
                results[f"thread_{thread_id}_timed_out"] = True
                results[f"thread_{thread_id}_timeout_on_lock"] = lock_id
                break

    finally:
        # Release all acquired locks in reverse order
        for lock_id in reversed(acquired):
            lock = lock1 if lock_id == 1 else lock2
            lock.release()

    results[f"thread_{thread_id}_acquired"] = acquired

if __name__ == "__main__":
    random.seed(42)

    lock1 = TimeoutLock()
    lock2 = TimeoutLock()

    results = {}
    barrier = threading.Barrier(2)  # Wait for both threads to start

    timeout_val = 0.3

    t_a = threading.Thread(
        target=acquirer,
        args=(lock1, lock2, [1, 2], results, "A", timeout_val, barrier)
    )
    t_b = threading.Thread(
        target=acquirer,
        args=(lock1, lock2, [2, 1], results, "B", timeout_val, barrier)
    )

    t_a.start()
    t_b.start()

    t_a.join(timeout=3)
    t_b.join(timeout=3)

    # At least one thread should have timed out
    timed_out_count = sum(1 for t in ["A", "B"] if results.get(f"thread_{t}_timed_out"))
    assert timed_out_count > 0, f"No timeout detected. Results: {results}"

    # Both threads must have exited (not hung)
    assert not t_a.is_alive(), "Thread A hung"
    assert not t_b.is_alive(), "Thread B hung"

    print(f"deadlock_timeout: circular lock order [1→2] and [2→1]; {timed_out_count} thread(s) timed out, breaking deadlock cycle")
    print("deadlock_timeout PASS")
    sys.exit(0)
