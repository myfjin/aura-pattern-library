"""
point_in_time_restore: restore a DB to an exact point in time = a base backup + replay of the
write-ahead log up to a target timestamp (no entry newer than the target is applied).
Failure simulated: crash mid-restore (killed after the base copy, before the log is fully
replayed). Recovery asserted: (1) restoring to a target yields EXACTLY the state committed by
that time (older targets exclude newer rows — a no-op "copy the latest DB" fails this), and
(2) restore is crash-resumable — a killed restore, re-run, converges to the same exact state.
Uses logical timestamps (1,2,3) so the point-in-time is deterministic.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
import sqlite3
import subprocess
import signal
import time
import json
import shutil

# child: perform a restore but block AFTER copying the base, BEFORE replaying the log.
CHILD = r"""
import sys, os, shutil, time
base, db, ready = sys.argv[1], sys.argv[2], sys.argv[3]
shutil.copy(base, db)         # base copied; log NOT yet replayed
open(ready, "w").close()
time.sleep(3600)              # parent SIGKILLs us here — restore is incomplete
"""


def restore_to(base_path, log_path, target_ts, db_path):
    """Idempotent restore: copy the base, then replay every log entry with ts <= target_ts."""
    shutil.copy(base_path, db_path)                       # always start from the base (resumable)
    conn = sqlite3.connect(db_path)
    with open(log_path) as f:
        for line in f:
            e = json.loads(line)
            if e["ts"] <= target_ts:
                conn.execute("INSERT INTO t (val) VALUES (?)", (e["val"],))
    conn.commit()
    conn.close()


def vals(db_path):
    c = sqlite3.connect(db_path)
    v = sorted(r[0] for r in c.execute("SELECT val FROM t").fetchall())
    c.close()
    return v


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    base = os.path.join(tmpdir, "base.db")
    log = os.path.join(tmpdir, "wal.jsonl")
    db = os.path.join(tmpdir, "restored.db")

    # Base backup at logical time 0: row_1 committed.
    c = sqlite3.connect(base)
    c.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, val TEXT)")
    c.execute("INSERT INTO t (val) VALUES ('row_1')")
    c.commit(); c.close()
    # Write-ahead log: row_2 @ t=2, row_3 @ t=3.
    with open(log, "w") as f:
        f.write(json.dumps({"ts": 2, "val": "row_2"}) + "\n")
        f.write(json.dumps({"ts": 3, "val": "row_3"}) + "\n")

    # RECOVERY assert 1 (point-in-time EXACTNESS): each target gives exactly its committed state.
    restore_to(base, log, 1, db); assert vals(db) == ["row_1"], vals(db)
    restore_to(base, log, 2, db); assert vals(db) == ["row_1", "row_2"], vals(db)
    restore_to(base, log, 3, db); assert vals(db) == ["row_1", "row_2", "row_3"], vals(db)
    # A no-op "restore = copy the newest DB" would give row_1,row_2,row_3 for target=1 → fails above.

    # THE CRASH: a restore killed after the base copy, before replay, leaves an INCOMPLETE db.
    ready = os.path.join(tmpdir, "ready")
    child = subprocess.Popen([sys.executable, "-c", CHILD, base, db, ready])
    while not os.path.exists(ready):
        time.sleep(0.005)
    os.kill(child.pid, signal.SIGKILL)
    try:
        child.wait(timeout=1)
    except Exception:
        pass
    assert vals(db) == ["row_1"], f"pre-condition: crashed restore left {vals(db)}"  # base only

    # RECOVERY assert 2 (crash-resumable): re-run the same restore → converges to the exact state.
    restore_to(base, log, 2, db)
    assert vals(db) == ["row_1", "row_2"], f"resumed restore did not converge: {vals(db)}"

    shutil.rmtree(tmpdir)
    print("point_in_time_restore: exact PITR at t=1/2/3; crash mid-restore re-ran to the exact state")
    print("point_in_time_restore PASS")
    sys.exit(0)
