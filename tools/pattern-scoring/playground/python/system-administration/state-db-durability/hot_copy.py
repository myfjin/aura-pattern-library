"""Hot-copy a live SQLite database into a consistent point-in-time snapshot.

Uses SQLite's backup API while a writer is actively committing inserts. The
resulting copy must be a valid database whose rows form a contiguous committed
prefix (no gaps), proving it captures a single transaction point rather than a
torn mix.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import os
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import List


def hot_copy_sqlite(source_path: str, dest_path: str, pages: int = 1, sleep: float = 0.005) -> None:
    """Copy ``source_path`` to ``dest_path`` using SQLite's online backup API.

    Args:
        source_path: Path to the live SQLite database.
        dest_path:   Path where the consistent snapshot will be written.
        pages:       Pages copied per backup step (default 1, fine-grained lock).
        sleep:       Seconds to sleep between backup steps.

    Returns:
        None

    Guarantees:
        - The destination file is a valid SQLite database after the call.
        - The snapshot represents a single committed point in time; rows in the
          copy are a contiguous prefix of the source's committed history.
        - No torn or interleaved state is produced.

    Failure scenario:
        A naive byte-for-byte copy of a live database can capture a torn page or
        a mix of commits, yielding either a corrupt file or rows with gaps in
        sequence.
    """
    src = sqlite3.connect(source_path)
    dst = sqlite3.connect(dest_path)
    try:
        with dst:
            src.backup(dst, pages=pages, sleep=sleep)
    finally:
        dst.close()
        src.close()


def seed_database(db_path: str) -> None:
    """Create an empty schema in ``db_path`` so a hot copy always sees a real table.

    Args:
        db_path: Path to the live database file.

    Guarantees:
        - Table ``t`` exists (id INTEGER PRIMARY KEY, idx INTEGER) after the call.
    """
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, idx INTEGER)")
        conn.commit()
    finally:
        conn.close()


def start_writer(db_path: str) -> subprocess.Popen:
    """Start a subprocess that inserts 12 rows into ``db_path`` while copying."""
    code = r"""
import sqlite3, sys, time
db = sys.argv[1]
c = sqlite3.connect(db)
c.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY, idx INTEGER)")
c.commit()
for i in range(12):
    c.execute("INSERT INTO t (idx) VALUES (?)", (i,))
    c.commit()
    time.sleep(0.03)
c.close()
"""
    return subprocess.Popen([sys.executable, "-c", code, db_path])


def read_copy_indexes(copy_path: str) -> List[int]:
    """Return sorted ``idx`` values from the copied database."""
    conn = sqlite3.connect(copy_path)
    try:
        return sorted(r[0] for r in conn.execute("SELECT idx FROM t").fetchall())
    finally:
        conn.close()


def count_live_rows(live_path: str) -> int:
    """Return row count in the live database."""
    conn = sqlite3.connect(live_path)
    try:
        return conn.execute("SELECT COUNT(*) FROM t").fetchone()[0]
    finally:
        conn.close()


def assert_copy_consistency(copy_path: str, live_path: str) -> None:
    """Assert the hot copy is valid and a contiguous prefix of the live DB.

    Args:
        copy_path: Path to the copied database.
        live_path: Path to the live database.

    Raises:
        AssertionError: if integrity fails, rows have gaps, or copy is not a prefix.

    Failure scenario:
        A naive byte-copy taken mid-write yields a torn DB that either fails
        integrity_check or contains gaps in the ``idx`` sequence.
    """
    assert os.path.exists(copy_path), "hot copy was not produced"
    conn = sqlite3.connect(copy_path)
    try:
        assert conn.execute("PRAGMA integrity_check").fetchone()[0] == "ok", \
            "hot copy is corrupt (torn)"
    finally:
        conn.close()

    idxs = read_copy_indexes(copy_path)
    assert idxs == list(range(len(idxs))), f"hot copy is a torn interleave (gaps): {idxs}"

    live = count_live_rows(live_path)
    assert live == 12 and len(idxs) <= live, \
        f"live={live}, copy={len(idxs)} (copy not a prefix)"


def main() -> None:
    """Self-test with hand-computable planted truths."""
    tmpdir = tempfile.mkdtemp()
    db = os.path.join(tmpdir, "live.db")
    cp = os.path.join(tmpdir, "copy.db")

    try:
        seed_database(db)

        writer = start_writer(db)
        time.sleep(0.10)  # let several writes land first
        hot_copy_sqlite(db, cp)
        writer.wait(timeout=5)

        assert_copy_consistency(cp, db)
        print("PASS")
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == "__main__":
    main()
