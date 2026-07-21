"""Migration with rollback: crash mid-migration, schema must stay consistent.

The test creates a temporary SQLite database with an old schema, starts a child
process to run a multi-step migration, then kills the child mid-transaction.
After the crash the database must be either the old schema (rolled back) or the
new schema (fully applied) — never a partial mix. All existing data must
survive.
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
from typing import List, Tuple


def create_old_schema(db_path: str) -> None:
    """Create table ``t`` with only the ``name`` column and seed two rows.

    Args:
        db_path: Path to the SQLite database (will be created if needed).

    Guarantees:
        - Table ``t`` exists with columns ``id`` and ``name``.
        - Table contains exactly two rows: ``alice`` and ``bob``.
    """
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, name TEXT)")
        conn.execute("INSERT INTO t (name) VALUES ('alice'), ('bob')")
        conn.commit()
    finally:
        conn.close()


def get_schema_version(db_path: str) -> Tuple[str, List[str]]:
    """Return the schema version and column list for table ``t``.

    Args:
        db_path: Path to the SQLite database.

    Returns:
        A tuple ``(version, columns)``. ``version`` is ``'new'`` if the ``email``
        column exists, ``'old'`` if it does not, or ``'error'`` on read failure.

    Guarantees:
        - Never raises; errors are reported as ``('error', [str(exc)])``.
    """
    try:
        conn = sqlite3.connect(db_path)
        try:
            conn.row_factory = sqlite3.Row
            info = conn.execute("PRAGMA table_info(t)").fetchall()
            columns = [row["name"] for row in info]
            return ("new" if "email" in columns else "old"), columns
        finally:
            conn.close()
    except Exception as exc:
        return "error", [str(exc)]


def start_migration_child(db_path: str) -> subprocess.Popen:
    """Spawn a child that begins adding an ``email`` column inside a transaction."""
    code = r"""
import sqlite3, sys, os, signal
db_path = sys.argv[1]
conn = sqlite3.connect(db_path)
conn.execute("BEGIN")
conn.execute("ALTER TABLE t ADD COLUMN email TEXT")
os.kill(os.getpid(), signal.SIGSTOP)
conn.commit()
conn.close()
"""
    return subprocess.Popen([sys.executable, "-c", code, db_path])


def kill_child(child: subprocess.Popen, settle: float = 0.2, wait_timeout: float = 1.0) -> None:
    """Kill the child process mid-migration.

    Args:
        child: The running migration child.
        settle: Seconds to let the child reach BEGIN/ALTER before killing.
        wait_timeout: Seconds to wait for child death after SIGKILL.
    """
    time.sleep(settle)
    try:
        os.kill(child.pid, signal.SIGKILL)
    except Exception:
        pass
    try:
        child.wait(timeout=wait_timeout)
    except Exception:
        pass


def assert_valid_schema_state(version: str, columns: List[str]) -> None:
    """Assert the schema is either old or new, never partial.

    Args:
        version: Schema version label.
        columns: Current column names of table ``t``.

    Returns:
        None

    Raises:
        AssertionError: if the schema is in an inconsistent state.

    Failure scenario:
        A torn migration could leave the table missing expected columns or with
        broken metadata, neither old nor new.
    """
    assert version in ["old", "new"], \
        f"schema is neither old nor new (partial migration): {columns}"
    assert "name" in columns, f"migration corrupted existing column: {columns}"


def assert_data_preserved(db_path: str, expected_rows: int = 2) -> None:
    """Assert all original rows are still present after the crash.

    Args:
        db_path: Path to the SQLite database.
        expected_rows: Expected row count (default 2).

    Raises:
        AssertionError: if the table is unreadable or rows are missing.
    """
    try:
        conn = sqlite3.connect(db_path)
        try:
            row_count = conn.execute("SELECT COUNT(*) FROM t").fetchone()[0]
        finally:
            conn.close()
        assert row_count == expected_rows, \
            f"migration lost rows: {row_count} instead of {expected_rows}"
    except Exception as exc:
        raise AssertionError(f"cannot query table after migration crash: {exc}")


def main() -> None:
    """Self-test with hand-computable planted truths.

    Creates its own temporary SQLite database via ``tempfile``, migrates it in a
    child process, crash-tests the rollback, and cleans up. No external DB
    required.
    """
    tmpdir = tempfile.mkdtemp()
    db_path = os.path.join(tmpdir, "test.db")

    try:
        create_old_schema(db_path)

        old_version, old_cols = get_schema_version(db_path)
        assert old_version == "old", f"setup failed: {old_cols}"

        child = start_migration_child(db_path)
        kill_child(child)

        version_after, cols_after = get_schema_version(db_path)
        assert_valid_schema_state(version_after, cols_after)
        assert_data_preserved(db_path, expected_rows=2)

        print("PASS")
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == "__main__":
    main()
