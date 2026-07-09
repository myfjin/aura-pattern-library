"""
transaction_rollback: begin a transaction, write data, then crash before commit.
Failure simulated: crash inside an active transaction (process killed while transaction is open).
Recovery asserted: on reopen, the uncommitted changes are NOT visible (rolled back automatically),
and the DB shows only the pre-transaction state. An uncommitted write that persisted would
violate ACID; this assert catches that.
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
from pathlib import Path

TXN_CHILD = r"""
import sqlite3, sys, os, time
db_path = sys.argv[1]
marker_file = sys.argv[2]
conn = sqlite3.connect(db_path)
conn.isolation_level = None
conn.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY, val TEXT)")
# Committed insert (will be visible after crash)
conn.execute("INSERT INTO t (val) VALUES ('pre_commit')")
open(marker_file, 'w').write('post_commit')
time.sleep(0.05)  # ensure pre_commit is written
# Now start a transaction and insert more (uncommitted)
conn.execute("BEGIN")
conn.execute("INSERT INTO t (val) VALUES ('txn_row_1')")
conn.execute("INSERT INTO t (val) VALUES ('txn_row_2')")
# Stay in transaction; parent will kill us
while True:
    time.sleep(1)
# Never reach commit
conn.commit()
conn.close()
"""


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    db_path = os.path.join(tmpdir, "test.db")
    marker = os.path.join(tmpdir, "marker")

    # Spawn child that creates table, inserts pre_commit, then starts transaction with uncommitted rows.
    child = subprocess.Popen([sys.executable, "-c", TXN_CHILD, db_path, marker])

    # Wait for child to complete pre_commit insert
    start = time.time()
    while time.time() - start < 2:
        if os.path.exists(marker):
            break
        time.sleep(0.01)

    time.sleep(0.1)  # extra margin for child to BEGIN and insert txn rows

    # Kill the child while transaction is open.
    try:
        os.kill(child.pid, signal.SIGKILL)
    except:
        pass
    try:
        child.wait(timeout=1)
    except:
        pass

    # Reopen DB and check: uncommitted changes should be rolled back.
    conn = sqlite3.connect(db_path)
    conn.isolation_level = None

    # RECOVERY assert 1: the DB can be opened without error.
    try:
        count = conn.execute("SELECT COUNT(*) FROM t").fetchone()[0]
    except Exception as e:
        assert False, f"DB corrupted after crash: {e}"

    # RECOVERY assert 2 (RECOVERY tier): only pre_commit row exists (txn rows rolled back).
    expected_count = 1
    assert count == expected_count, \
        f"uncommitted changes persisted: {count} rows, expected {expected_count} (only pre_commit should exist)"

    # RECOVERY assert 3: verify the pre_commit row is still there and txn rows are gone.
    rows = conn.execute("SELECT val FROM t").fetchall()
    vals = [r[0] for r in rows]
    assert "pre_commit" in vals, f"committed row lost: {vals}"
    assert "txn_row_1" not in vals and "txn_row_2" not in vals, \
        f"uncommitted txn rows were not rolled back: {vals}"

    conn.close()

    import shutil
    shutil.rmtree(tmpdir)
    print(f"transaction_rollback: crash mid-txn rolled back uncommitted rows (final count: {count})")
    print("transaction_rollback PASS")
    sys.exit(0)
