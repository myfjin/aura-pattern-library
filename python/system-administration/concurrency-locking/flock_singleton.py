"""
flock_singleton: two processes contend for the same fcntl.flock(LOCK_EX) on a file.
Failure simulated: launch a holder and a blocker AT THE SAME TIME; the blocker attempts the
exclusive lock while the holder holds it. Recovery asserted: the blocker's acquire happens
strictly AFTER the holder's release (event ordering via shared-clock epoch timestamps), and its
wait was ~the hold time — proving it genuinely blocked. A no-op lock lets the blocker acquire
immediately (before the holder released) → the ordering assert fails.
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


def holder_then_releaser(filename, results_dict):
    with open(filename, "a") as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        results_dict["holder_acquired_at"] = time.time()
        time.sleep(0.5)
        results_dict["holder_released_at"] = time.time()   # record the release moment
        fcntl.flock(f.fileno(), fcntl.LOCK_UN)


def blocker(filename, results_dict):
    time.sleep(0.1)                                         # let the holder acquire first
    with open(filename, "a") as f:
        start = time.time()
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)             # blocks until holder releases
        acquired_at = time.time()
        fcntl.flock(f.fileno(), fcntl.LOCK_UN)
    results_dict["blocker_acquired_at"] = acquired_at
    results_dict["blocker_wait"] = acquired_at - start     # RELATIVE wait, not epoch


if __name__ == "__main__":
    random.seed(42)
    tmpdir = tempfile.mkdtemp()
    lockfile = os.path.join(tmpdir, "test.lock")
    open(lockfile, "w").close()

    with multiprocessing.Manager() as manager:
        results = manager.dict()
        p_holder = multiprocessing.Process(target=holder_then_releaser, args=(lockfile, results))
        p_blocker = multiprocessing.Process(target=blocker, args=(lockfile, results))
        p_holder.start()
        time.sleep(0.05)                                   # holder reaches the lock first
        p_blocker.start()
        p_holder.join(timeout=5)
        p_blocker.join(timeout=5)

        assert results.get("holder_released_at"), "holder never held/released the lock"
        assert results.get("blocker_acquired_at"), "blocker never acquired the lock"

        held_release = results["holder_released_at"]
        blk_acquire = results["blocker_acquired_at"]
        blk_wait = results["blocker_wait"]

        # RECOVERY assert 1 (event ordering): the blocker acquired only AFTER the holder
        # released — the two share the same clock, so this compares real moments, not an epoch
        # to a constant. A no-op lock lets the blocker in DURING the hold → blk_acquire < release.
        assert blk_acquire >= held_release - 0.005, \
            f"blocker acquired before holder released (no blocking): {blk_acquire:.3f} < {held_release:.3f}"

        # RECOVERY assert 2 (real wait): the blocker waited ~the remaining hold (started 0.1s in,
        # holder holds 0.5s → ~0.4s of blocking). A non-blocking no-op returns in ~0s.
        assert blk_wait > 0.25, f"blocker wait {blk_wait:.3f}s too short — it did not block"

    import shutil
    shutil.rmtree(tmpdir)
    # don't print the measured wait (varies by load) — keep stdout deterministic
    print("flock_singleton: blocker blocked and acquired only after holder released (ordering proven)")
    print("flock_singleton PASS")
    sys.exit(0)
