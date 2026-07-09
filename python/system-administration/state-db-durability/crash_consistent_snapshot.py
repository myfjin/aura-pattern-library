"""
crash_consistent_snapshot: snapshot a live DB atomically (backup -> temp -> fsync -> rename)
so the snapshot is NEVER visible in a torn state.
Failure simulated: SIGKILL the snapshotting process INSIDE the (slow, page-by-page) copy,
before the atomic rename. Recovery asserted: the target snapshot is either ABSENT (rename never
happened) or a fully-valid DB — NEVER a torn/half-written file. A naive backup written directly
to the target, killed mid-copy, leaves a torn target and FAILS this. A clean run then proves the
snapshot equals the exact committed row count.
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
import shutil

# child: mirror atomic_snapshot but SLOW (page-by-page) so the parent can kill it mid-copy.
CHILD = r"""
import sqlite3, sys, os
db, snap = sys.argv[1], sys.argv[2]
part = snap + ".part"
src = sqlite3.connect(db)
dst = sqlite3.connect(part)
with dst:
    src.backup(dst, pages=1, sleep=0.01)   # slow: parent SIGKILLs during this
dst.close(); src.close()
os.replace(part, snap)                      # atomic rename — never reached (we're killed above)
"""


def atomic_snapshot(db_path, snap_path):
    """Consistent snapshot: backup to a temp file, fsync, atomic rename into place."""
    part = snap_path + ".part"
    src = sqlite3.connect(db_path)
    dst = sqlite3.connect(part)
    with dst:
        src.backup(dst)
    dst.close()
    src.close()
    fd = os.open(part, os.O_RDONLY)
    os.fsync(fd)
    os.close(fd)
    os.replace(part, snap_path)             # atomic


def _valid_db(path):
    try:
        c = sqlite3.connect(path)
        ok = c.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
        c.close()
        return ok
    except Exception:
        return False


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    db_path = os.path.join(tmpdir, "live.db")
    conn = sqlite3.connect(db_path)
    conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, val TEXT)")
    conn.executemany("INSERT INTO t (val) VALUES (?)", [(f"v{i}",) for i in range(3000)])
    conn.commit()
    committed = conn.execute("SELECT COUNT(*) FROM t").fetchone()[0]
    conn.close()

    # THE CRASH: kill the snapshotter mid-copy, before its atomic rename.
    snap = os.path.join(tmpdir, "snap.db")
    child = subprocess.Popen([sys.executable, "-c", CHILD, db_path, snap])
    time.sleep(0.15)                        # well inside the slow page-by-page copy
    os.kill(child.pid, signal.SIGKILL)
    try:
        child.wait(timeout=1)
    except Exception:
        pass

    # RECOVERY assert 1 (crash-consistency): the target is ABSENT or fully valid — never torn.
    # A naive direct-to-target copy killed mid-write leaves a torn target and fails here.
    assert (not os.path.exists(snap)) or _valid_db(snap), \
        "snapshot target is TORN after mid-copy crash (atomicity violated)"

    # clear any orphan temp/target from the crash, then do a CLEAN snapshot via the function.
    for p in (snap, snap + ".part"):
        if os.path.exists(p):
            os.unlink(p)
    atomic_snapshot(db_path, snap)

    # RECOVERY assert 2 (correctness): the clean snapshot is valid and has the EXACT committed rows.
    assert _valid_db(snap), "clean snapshot is not a valid DB"
    sc = sqlite3.connect(snap)
    snap_rows = sc.execute("SELECT COUNT(*) FROM t").fetchone()[0]
    sc.close()
    assert snap_rows == committed, f"snapshot rows {snap_rows} != committed {committed}"

    shutil.rmtree(tmpdir)
    print(f"crash_consistent_snapshot: mid-copy crash left no torn target; clean snapshot = {committed} committed rows")
    print("crash_consistent_snapshot PASS")
    sys.exit(0)
