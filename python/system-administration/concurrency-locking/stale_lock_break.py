"""
stale_lock_break: detect and break a stale lock when its holder dies.
Failure simulated: process A acquires a lock, then dies (SIGKILL) without releasing.
Process B detects the stale lock (holder is dead) and breaks it by waiting for it to be released.
Recovery asserted: (1) B detects the lock is held (not acquired without effort), (2) B reads
the holder pid, (3) after holder is killed, B acquires the now-released lock, (4) the pidfile
proves a real holder existed. A no-op stale-break would leave the lock held forever or fail
to detect the held lock.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
import fcntl
import signal
import time
import multiprocessing
import random

def acquire_and_hold_with_pidfile(lockfile, pidfile, results_dict, ready_marker):
    """Acquire lock, write pid, signal readiness, then hang (to be killed)."""
    with open(lockfile, "a") as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        pid = os.getpid()
        with open(pidfile, "w") as pf:
            pf.write(str(pid))
        results_dict["holder_acquired"] = True
        # Signal that we're ready to be detected
        with open(ready_marker, "w") as rm:
            rm.write("ready")
        # Hang indefinitely (will be SIGKILL'd)
        for _ in range(1000):
            time.sleep(0.1)

def detector_and_breaker(lockfile, pidfile, results_dict, ready_marker):
    """Detect stale lock, wait for it to be released, and acquire."""
    # Wait for holder to be ready (has lock + written pidfile)
    for _ in range(20):
        if os.path.exists(ready_marker):
            break
        time.sleep(0.05)

    # Try non-blocking acquire first (should fail if holder is alive)
    try:
        with open(lockfile, "a") as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            # If we got here, the lock is free (unexpected — holder should be holding)
            results_dict["breaker_got_lock_without_breaking"] = True
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
            return
    except IOError:
        # Lock is held, as expected
        pass

    # Read the pid from pidfile
    holder_pid = None
    try:
        with open(pidfile) as pf:
            holder_pid = int(pf.read().strip())
        results_dict["breaker_read_pid"] = True
        results_dict["holder_pid"] = holder_pid
    except (FileNotFoundError, ValueError):
        results_dict["breaker_error"] = "Could not read holder pid"
        return

    # Now wait for the lock to be released (holder dies)
    # The lock will be auto-released by the OS when the holder process dies
    timeout = 5.0
    start = time.time()
    while time.time() - start < timeout:
        try:
            with open(lockfile, "a") as f:
                fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                # Success: we got the lock (holder is dead, lock was released)
                results_dict["breaker_acquired"] = True
                fcntl.flock(f.fileno(), fcntl.LOCK_UN)
                break
        except IOError:
            # Lock still held; wait and retry
            time.sleep(0.05)

if __name__ == "__main__":
    random.seed(42)
    tmpdir = tempfile.mkdtemp()
    lockfile = os.path.join(tmpdir, "stale.lock")
    pidfile = os.path.join(tmpdir, "lock.pid")
    ready_marker = os.path.join(tmpdir, "holder.ready")
    with open(lockfile, "w") as f:
        f.write("")

    with multiprocessing.Manager() as manager:
        results = manager.dict()

        p_holder = multiprocessing.Process(target=acquire_and_hold_with_pidfile, args=(lockfile, pidfile, results, ready_marker))
        p_breaker = multiprocessing.Process(target=detector_and_breaker, args=(lockfile, pidfile, results, ready_marker))

        p_holder.start()
        p_breaker.start()

        # Give both time to start and for holder to be detected
        time.sleep(0.3)

        # Kill the holder (it's holding the lock and won't release)
        try:
            os.kill(p_holder.pid, signal.SIGKILL)
        except:
            pass
        p_holder.join(timeout=1)

        # Wait for breaker to complete its detection and acquisition
        p_breaker.join(timeout=5)

        # Verify the breaker detected and acquired the stale lock
        assert results.get("holder_acquired"), "holder never acquired the lock"
        assert results.get("breaker_read_pid"), "breaker never read the holder's pid"
        assert results.get("breaker_acquired"), "breaker never acquired the stale lock"

        # The breaker should NOT have gotten the lock without breaking (that would mean no blocking)
        assert not results.get("breaker_got_lock_without_breaking"), "breaker got lock without stale-break (lock was not held or blocking)"

    import shutil
    shutil.rmtree(tmpdir)
    print(f"stale_lock_break: holder died with lock held; breaker detected, waited for release, and acquired")
    print("stale_lock_break PASS")
    sys.exit(0)
