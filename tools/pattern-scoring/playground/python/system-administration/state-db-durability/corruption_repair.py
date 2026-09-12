"""
corruption_repair: detect and repair SQLite DB corruption (or mark unrecoverable).

The disaster test creates a valid database, backs it up, truncates the live DB
mid-write to corrupt it, then attempts detection + repair. If direct repair
fails it falls back to the backup. The test asserts that corruption was detected,
that the final DB is consistent, and that no data was lost.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import os
import shutil
import sqlite3
import sys
import tempfile
from pathlib import Path


def create_good_database(db_path: str) -> None:
    """Create a valid SQLite database with a table, an index, and sample rows.

    Args:
        db_path: Path for the new database file.

    Guarantees:
        - The database opens and accepts writes.
        - Table `t` contains exactly 3 rows after this call.
    """
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, val TEXT)")
        conn.execute("CREATE INDEX idx_val ON t(val)")
        conn.execute("INSERT INTO t (val) VALUES ('a'), ('b'), ('c')")
        conn.commit()
    finally:
        conn.close()


def backup_database(source: str, backup: str) -> None:
    """Copy `source` to `backup` for later restore."""
    shutil.copy(source, backup)


def corrupt_by_truncation(db_path: str, factor: float = 0.5) -> None:
    """Truncate a database file to corrupt it.

    Args:
        db_path: Path to the database file.
        factor:  Fraction of the file to keep (default 0.5).

    Failure scenario:
        Truncating mid-data guarantees that SQLite integrity checks will fail.
    """
    original_size = os.path.getsize(db_path)
    with open(db_path, 'r+b') as f:
        f.truncate(max(100, int(original_size * factor)))


def detect_corruption(db_path: str) -> bool:
    """Return True if the DB fails PRAGMA integrity_check or cannot open.

    Args:
        db_path: Path to the database file.

    Returns:
        True if corruption is detected, False if integrity_check returns "ok".
    """
    try:
        conn = sqlite3.connect(db_path)
        try:
            result = conn.execute("PRAGMA integrity_check").fetchone()[0]
        finally:
            conn.close()
        return result != "ok"
    except Exception:
        return True


def attempt_repair(db_path: str) -> bool:
    """Try to repair a corrupt DB with REINDEX + VACUUM.

    Args:
        db_path: Path to the database file.

    Returns:
        True if repair commands succeeded, False otherwise.

    Note:
        This does not guarantee the repaired DB is valid; call
        assert_repair_consistency to verify.
    """
    try:
        conn = sqlite3.connect(db_path)
        try:
            conn.execute("PRAGMA writable_schema=ON")
            conn.execute("REINDEX")
            conn.execute("PRAGMA writable_schema=OFF")
            conn.execute("VACUUM")
            conn.commit()
        finally:
            conn.close()
        return True
    except Exception:
        return False


def restore_from_backup(backup: str, target: str) -> bool:
    """Copy backup over target. Return True on success."""
    try:
        shutil.copy(backup, target)
        return True
    except Exception:
        return False


def assert_repair_consistency(db_path: str, expected_rows: int = 3) -> None:
    """Assert the DB passes integrity_check and contains the expected row count.

    Args:
        db_path:       Path to the repaired/restored database.
        expected_rows: The number of rows table `t` should contain.

    Raises:
        AssertionError: if integrity check fails or row count is wrong.

    Failure scenario:
        A repair that silently loses rows or leaves torn pages is caught here.
    """
    conn = sqlite3.connect(db_path)
    try:
        result = conn.execute("PRAGMA integrity_check").fetchone()[0]
        rows = conn.execute("SELECT COUNT(*) FROM t").fetchone()[0]
        assert result == "ok", f"repair did not fix corruption: {result}"
        assert rows == expected_rows, f"repair lost data: {rows} rows instead of {expected_rows}"
    finally:
        conn.close()


def main() -> None:
    """Self-test: corrupt DB by truncation, detect it, repair or restore."""
    tmpdir = tempfile.mkdtemp()
    db_path = os.path.join(tmpdir, "test.db")
    backup_path = os.path.join(tmpdir, "test.db.backup")

    try:
        create_good_database(db_path)
        backup_database(db_path, backup_path)
        corrupt_by_truncation(db_path)

        corruption_detected = detect_corruption(db_path)
        assert corruption_detected, "truncation-induced corruption was not detected"

        repair_ok = attempt_repair(db_path)
        if not repair_ok:
            repair_ok = restore_from_backup(backup_path, db_path)

        assert repair_ok, "repair and restore both failed"
        assert_repair_consistency(db_path, expected_rows=3)

        print(f"corruption_repair: detected truncation-induced corruption, final DB consistent")
        print("corruption_repair PASS")
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == "__main__":
    main()
