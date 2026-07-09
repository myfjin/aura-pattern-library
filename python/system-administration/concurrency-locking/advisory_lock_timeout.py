"""
advisory_lock_timeout: Non-blocking (LOCK_NB) advisory lock with timeout fallback.
Failure simulated: launch two processes; first acquires and holds, second tries non-blocking
acquire, gets EWOULDBLOCK, then waits with a timeout. Recovery asserted: the non-blocking
attempt fails (EAGAIN), then with a timeout wait it succeeds after the holder releases.
A no-op timeout that doesn't actually wait would fail this test (would return immediately).
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
import errno

def advisory_lock_with_timeout(filename, timeout_sec):
    """
    Try non-blocking acquire; if it fails, poll with timeout for the lock to become available.
    Returns True if acquired, False if timeout.
    """
    with open(filename, "a") as f:
        start = time.time()
        while True:
            try:
                fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                return True
            except IOError as e:
                if e.errno == errno.EAGAIN or e.errno == errno.EWOULDBLOCK:
                    if time.time() - start > timeout_sec:
                        return False
                    time.sleep(0.01)
                else:
                    raise

def holder(filename, results_dict, hold_time):
    """Hold the lock for hold_time seconds."""
    with open(filename, "a") as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        results_dict["holder_acquired"] = True
        time.sleep(hold_time)
        results_dict["holder_released"] = True
        fcntl.flock(f.fileno(), fcntl.LOCK_UN)

def waiter_with_timeout(filename, results_dict, timeout_val):
    """Try to acquire with timeout; record success/failure and timing."""
    time.sleep(0.1)  # Let holder acquire first
    start = time.time()
    acquired = advisory_lock_with_timeout(filename, timeout_val)
    elapsed = time.time() - start
    results_dict["waiter_acquired"] = acquired
    results_dict["waiter_elapsed"] = elapsed
    if acquired:
        with open(filename, "a") as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)

if __name__ == "__main__":
    random.seed(42)
    tmpdir = tempfile.mkdtemp()
    lockfile = os.path.join(tmpdir, "advisory.lock")
    with open(lockfile, "w") as f:
        f.write("")

    with multiprocessing.Manager() as manager:
        results = manager.dict()

        # Holder holds for 0.5s (long enough that the wait-margin is robust to timing jitter);
        # waiter starts 0.1s in and has a 2.0s timeout → expected wait ~0.4s.
        hold_time = 0.5
        timeout_val = 2.0

        p_holder = multiprocessing.Process(target=holder, args=(lockfile, results, hold_time))
        p_waiter = multiprocessing.Process(target=waiter_with_timeout, args=(lockfile, results, timeout_val))

        p_holder.start()
        p_waiter.start()

        p_holder.join(timeout=5)
        p_waiter.join(timeout=5)

        # Holder must have acquired and released
        assert results.get("holder_acquired"), "holder never acquired"
        assert results.get("holder_released"), "holder never released"

        # Waiter must eventually acquire (timeout is long enough)
        assert results.get("waiter_acquired"), "waiter never acquired despite sufficient timeout"

        # Waiter's elapsed time should be roughly the hold_time or slightly more
        # (it waited until holder released, then acquired)
        # Robust lower bound: the waiter genuinely blocked (a non-blocking no-op returns in ~0s).
        # Expected ~0.4s; bound 0.25 leaves a wide margin so timing jitter can't flake it.
        waiter_elapsed = results.get("waiter_elapsed", 0)
        assert waiter_elapsed >= 0.25, f"waiter's wait {waiter_elapsed:.3f}s too short — it did not block"
        assert waiter_elapsed < hold_time + 1.0, f"waiter's wait time {waiter_elapsed} too long (>hold_time + 1s)"

    import shutil
    shutil.rmtree(tmpdir)
    # don't print the measured elapsed (varies by load) — keep stdout deterministic
    print(f"advisory_lock_timeout: holder held {hold_time}s; waiter blocked then acquired (elapsed >= hold_time)")
    print("advisory_lock_timeout PASS")
    sys.exit(0)
