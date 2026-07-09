"""
named_mutex: a named mutex using filesystem locking (tempfile-based).
Failure simulated: two processes try to acquire the same named mutex at the same time.
Recovery asserted: (1) both acquire and release successfully in sequence (one blocks until
the other releases), (2) the execution times show clear serialization (each holds for ~0.3s,
total time ~0.6s, not concurrent). A no-op mutex would allow both to enter "critical section"
at once, violating the mutex invariant.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
import fcntl
import time
import multiprocessing
import random

class NamedMutex:
    """A named mutex backed by a lockfile."""
    def __init__(self, name):
        self.name = name
        self.lockdir = tempfile.gettempdir()
        self.lockfile = os.path.join(self.lockdir, f"mutex_{name}.lock")
        self.fd = None

    def acquire(self, timeout=None):
        """Acquire the mutex; block until available or timeout."""
        start = time.time()
        while True:
            try:
                # Open with O_CREAT | O_EXCL to get exclusive creation (atomic)
                self.fd = os.open(self.lockfile, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
                return True
            except FileExistsError:
                # Lock is held by another process
                if timeout is not None and time.time() - start > timeout:
                    return False
                time.sleep(0.01)

    def release(self):
        """Release the mutex."""
        if self.fd is not None:
            try:
                os.close(self.fd)
            except:
                pass
            try:
                os.remove(self.lockfile)
            except:
                pass
            self.fd = None

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, *args):
        self.release()

def critical_section(mutex_name, results_dict, worker_id, hold_time):
    """Enter critical section, hold it, and record timings."""
    start = time.time()
    mutex = NamedMutex(mutex_name)
    acquired = mutex.acquire()
    acquire_time = time.time()

    if not acquired:
        results_dict[f"worker_{worker_id}_acquired"] = False
        return

    results_dict[f"worker_{worker_id}_acquired"] = True
    results_dict[f"worker_{worker_id}_acquire_latency"] = acquire_time - start

    # Hold the critical section
    time.sleep(hold_time)
    release_time = time.time()

    mutex.release()
    results_dict[f"worker_{worker_id}_held_duration"] = release_time - acquire_time

if __name__ == "__main__":
    random.seed(42)

    with multiprocessing.Manager() as manager:
        results = manager.dict()

        mutex_name = "test_mutex"
        hold_time = 0.3
        num_workers = 2

        processes = []
        start_all = time.time()
        for i in range(num_workers):
            p = multiprocessing.Process(target=critical_section, args=(mutex_name, results, i, hold_time))
            processes.append(p)

        # Start workers at roughly the same time
        for p in processes:
            p.start()
        for p in processes:
            p.join(timeout=5)
        end_all = time.time()

        # All workers must have acquired the mutex
        for i in range(num_workers):
            assert results.get(f"worker_{i}_acquired"), f"worker {i} never acquired the mutex"

        # All workers must have held the section for approximately hold_time
        for i in range(num_workers):
            held = results.get(f"worker_{i}_held_duration", 0)
            assert held >= hold_time - 0.05, f"worker {i} held for {held}s, less than {hold_time}s"

        # Total time should be roughly 2 * hold_time (sequential, not parallel)
        total_time = end_all - start_all
        assert total_time >= (2 * hold_time - 0.1), f"total_time {total_time}s suggests parallel execution (expected ~{2*hold_time}s)"
        assert total_time < (2 * hold_time + 1.0), f"total_time {total_time}s too long"

    # don't print the measured total (varies by load) — keep stdout deterministic
    print(f"named_mutex: {num_workers} workers each held {hold_time}s; total >= 2*hold (serial, mutual exclusion proven)")
    print("named_mutex PASS")
    sys.exit(0)
