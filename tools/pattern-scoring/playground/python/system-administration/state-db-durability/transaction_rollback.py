"""Transaction rollback: crash inside an active transaction before COMMIT.

A child process inserts a committed row, begins a transaction with two more
uncommitted rows, then is killed. On reopen, SQLite must roll back the
uncommitted rows automatically. The test asserts only the pre-transaction row
remains.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import os
import shutil
import signal
import sqlite3
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import List


def start_transaction_child(db_path: str, marker_file: str) -> subprocess.Popen:
    """Spawn a child that commits one row, then opens a transaction with uncommitted rows."""
    code = r"""
import sqlite3, sys, os, time
db_path = sys.argv[1]
marker_file = sys.argv[2]
conn = sqlite3.connect(db_path)
conn.isolation_level = None
conn.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY, val TEXT)")
conn.execute("INSERT INTO t (val) VALUES ('pre_commit')")
conn.commit()
open(marker_file, 'w').write('post_commit')
time.sleep(0.05)
conn.execute("BEGIN")
conn.execute("INSERT INTO t (val) VALUES ('txn_row_1')")
conn.execute("INSERT INTO t (val) VALUES ('txn_row_2')")
while True:
    time.sleep(1)
"""
    return subprocess.Popen([sys.executable, "-c", code, db_path, marker_file])


def wait_for_marker(marker_file: str, timeout: float = 2.0) -> None:
    """Wait until the child has finished its committed insert."""
    start = time.time()
    while time.time() - start < timeout:
        if os.path.exists(marker_file):
            break
        time.sleep(0.01)


def kill_child(child: subprocess.Popen) -> None:
    """Kill the child process while its transaction is still open."""
    try:
        os.kill(child.pid, signal.SIGKILL)
    except Exception:
        pass
    try:
        child.wait(timeout=1)
    except Exception:
        pass


def read_rows(db_path: str) -> List[str]:
    """Return the ``val`` column from table ``t``."""
    conn = sqlite3.connect(db_path)
    try:
        conn.isolation_level = None
        return [r[0] for r in conn.execute("SELECT val FROM t").fetchall()]
    finally:
        conn.close()


def assert_rolled_back(db_path: str, expected_count: int = 1) -> None:
    """Assert the DB is openable, the committed row remains, and txn rows are gone.

    Args:
        db_path:        Path to the reopened database after crash.
        expected_count: Number of rows expected (only the committed row).

    Returns:
        None

    Raises:
        AssertionError: if the DB is corrupt, if txn rows persisted, or if the
                        committed row disappeared.

    Failure scenario:
        An uncommitted write that survived the crash would leave txn_row_1/2 in
        the table, violating ACID rollback semantics.
    """
    try:
        conn = sqlite3.connect(db_path)
        try:
            conn.isolation_level = None
            count = conn.execute("SELECT COUNT(*) FROM t").fetchone()[0]
        finally:
            conn.close()
    except Exception as e:
        raise AssertionError(f"DB corrupted after crash: {e}")

    assert count == expected_count, \
        f"uncommitted changes persisted: {count} rows, expected {expected_count}"

    rows = read_rows(db_path)
    assert "pre_commit" in rows, f"committed row lost: {rows}"
    assert "txn_row_1" not in rows and "txn_row_2" not in rows, \
        f"uncommitted txn rows were not rolled back: {rows}"


def main() -> None:
    """Self-test with hand-computable planted truths."""
    tmpdir = tempfile.mkdtemp()
    db_path = os.path.join(tmpdir, "test.db")
    marker = os.path.join(tmpdir, "marker")

    try:
        child = start_transaction_child(db_path, marker)
        wait_for_marker(marker)
        time.sleep(0.1)  # margin for child to BEGIN and insert txn rows
        kill_child(child)

        assert_rolled_back(db_path, expected_count=1)
        print("PASS")
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == "__main__":
    main()
