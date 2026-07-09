"""
cas_file_update: optimistic compare-and-swap on a versioned file (read → compute → swap-if-
version-unchanged → retry on conflict). This is REAL CAS, not pessimistic whole-cycle locking:
the read and the (expensive) compute happen OUTSIDE any lock; only the atomic compare-and-swap
(re-read version, write iff it still matches) is guarded, and a losing writer RETRIES.
Failure simulated: two processes read the same version concurrently, both compute, then race to
swap. Recovery asserted: (1) final value == N (no lost update — the loser's stale swap is
REJECTED and it retries on the fresh value), (2) at least one real CONFLICT+RETRY occurred
(retries >= 1) — which a pessimistic full-lock could never produce, proving this is genuine CAS.
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
import json


def _read(path):
    with open(path, "r") as f:
        d = json.load(f)
    return d["value"], d["version"]


def cas_increment(path, lockfile, results_dict, updater_id, barrier):
    retries = 0
    barrier.wait()                                  # both start together → both read same version
    while True:
        value, version = _read(path)               # READ (no lock)
        time.sleep(0.03)                            # compute window — widens the real race
        new_value = value + 1                       # COMPUTE (no lock)
        # COMPARE-AND-SWAP: under a brief lock, write ONLY if the version is still what we read.
        with open(lockfile, "a") as lf:
            fcntl.flock(lf.fileno(), fcntl.LOCK_EX)
            try:
                _, cur_version = _read(path)
                if cur_version == version:          # no one changed it → our swap is valid
                    with open(path, "w") as f:
                        json.dump({"value": new_value, "version": version + 1}, f)
                    break                            # success
                # else: version moved under us → CONFLICT, retry with fresh value
                retries += 1
            finally:
                fcntl.flock(lf.fileno(), fcntl.LOCK_UN)
    results_dict[f"updater_{updater_id}_retries"] = retries
    results_dict[f"updater_{updater_id}_ok"] = True


if __name__ == "__main__":
    random.seed(42)
    tmpdir = tempfile.mkdtemp()
    counter = os.path.join(tmpdir, "counter.json")
    lockfile = os.path.join(tmpdir, "counter.lock")
    with open(counter, "w") as f:
        json.dump({"value": 0, "version": 0}, f)
    open(lockfile, "w").close()

    num = 2
    with multiprocessing.Manager() as manager:
        results = manager.dict()
        barrier = manager.Barrier(num)
        procs = [multiprocessing.Process(target=cas_increment,
                                         args=(counter, lockfile, results, i, barrier))
                 for i in range(num)]
        for p in procs:
            p.start()
        for p in procs:
            p.join(timeout=10)

        for i in range(num):
            assert results.get(f"updater_{i}_ok"), f"updater {i} never completed"

        final_value, final_version = _read(counter)
        total_retries = sum(results.get(f"updater_{i}_retries", 0) for i in range(num))

        # RECOVERY assert 1: no lost update — every increment landed (the stale swap was rejected
        # and retried on the fresh value). A no-op CAS that ignored the version → final 1.
        assert final_value == num, f"lost update: final value {final_value}, expected {num}"
        assert final_version == num, f"version count wrong: {final_version}"

        # RECOVERY assert 2: a real CONFLICT was detected and retried — this is what makes it CAS
        # rather than pessimistic locking (which would serialize with ZERO retries).
        assert total_retries >= 1, f"no CAS conflict occurred ({total_retries}) — not optimistic CAS"

    import shutil
    shutil.rmtree(tmpdir)
    print(f"cas_file_update: optimistic CAS, final value={final_value} (no lost update), {total_retries} conflict-retry")
    print("cas_file_update PASS")
    sys.exit(0)
