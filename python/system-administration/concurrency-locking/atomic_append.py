"""
atomic_append: serialize a read-modify-write "append" so concurrent writers never lose data.
Failure simulated: MANY processes each do read-the-whole-file → add their line → write it back
(a read-modify-write, the classic lost-update race). WITHOUT the lock, two writers that read the
same content each overwrite the other → lines are lost. WITH fcntl.flock serializing the whole
RMW, every writer's line survives.
Recovery asserted: all N distinct writer lines are present and the count == N. This assert FAILS
on a no-op lock — the RMW race drops lines (which is why we use N=20, not 2: pure O_APPEND would
hide the race, so the demo makes the lock genuinely necessary).
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


def atomic_append(filename, lockfile, line, results_dict, writer_id):
    """Locked read-modify-write append: lock → read all → add line → write all → unlock."""
    with open(lockfile, "a") as lf:
        fcntl.flock(lf.fileno(), fcntl.LOCK_EX)
        try:
            with open(filename, "r") as f:
                content = f.read()
            # brief pause widens the race window a no-op lock would lose on
            time.sleep(0.001)
            content += line
            with open(filename, "w") as f:
                f.write(content)
                f.flush()
        finally:
            fcntl.flock(lf.fileno(), fcntl.LOCK_UN)
    results_dict[f"writer_{writer_id}_done"] = True


if __name__ == "__main__":
    random.seed(42)
    tmpdir = tempfile.mkdtemp()
    appfile = os.path.join(tmpdir, "appends.txt")
    lockfile = os.path.join(tmpdir, "appends.lock")
    with open(appfile, "w") as f:
        f.write("APPENDS:\n")
    open(lockfile, "w").close()

    num_writers = 20
    with multiprocessing.Manager() as manager:
        results = manager.dict()
        procs = [
            multiprocessing.Process(target=atomic_append,
                                    args=(appfile, lockfile, f"writer_{i}_line\n", results, i))
            for i in range(num_writers)
        ]
        for p in procs:
            p.start()
        for p in procs:
            p.join(timeout=10)

        for i in range(num_writers):
            assert results.get(f"writer_{i}_done"), f"writer {i} never completed"

        with open(appfile, "r") as f:
            content = f.read()
        data_lines = [l for l in content.splitlines() if l.startswith("writer_")]

        # RECOVERY assert: EVERY writer's line survived the concurrent read-modify-write. A no-op
        # lock loses lines (two writers read the same content, one overwrites the other).
        assert len(data_lines) == num_writers, \
            f"lost updates: {len(data_lines)} of {num_writers} lines survived"
        assert len(set(data_lines)) == num_writers, "duplicate/torn lines (RMW not serialized)"
        for i in range(num_writers):
            assert f"writer_{i}_line" in content, f"writer {i}'s line was lost"

    import shutil
    shutil.rmtree(tmpdir)
    print(f"atomic_append: {num_writers} concurrent read-modify-write appends, all {len(data_lines)} lines survived (no lost updates)")
    print("atomic_append PASS")
    sys.exit(0)
