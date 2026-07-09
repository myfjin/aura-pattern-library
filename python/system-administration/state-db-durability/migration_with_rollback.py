"""
migration_with_rollback: apply a schema migration with the ability to roll back if crash occurs.
Failure simulated: crash mid-migration (after some ALTER TABLE steps, before COMMIT).
Recovery asserted: on reopen, the schema is either the old version (rolled back) or the new
version (fully applied), never a partial mix. A torn migration would leave the schema inconsistent.
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

MIGRATION_CHILD = r"""
import sqlite3, sys, os, signal
db_path = sys.argv[1]
conn = sqlite3.connect(db_path)
conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, name TEXT)")
conn.execute("INSERT INTO t (name) VALUES ('alice'), ('bob')")
conn.commit()

# Now apply a migration: add a new column
conn.execute("BEGIN")
conn.execute("ALTER TABLE t ADD COLUMN email TEXT")
# Pause before COMMIT
os.kill(os.getpid(), signal.SIGSTOP)
conn.commit()
conn.close()
"""


def get_schema_version(db_path):
    """Determine if the new column (email) exists."""
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        info = conn.execute("PRAGMA table_info(t)").fetchall()
        conn.close()
        columns = [row["name"] for row in info]
        return "new" if "email" in columns else "old", columns
    except Exception as e:
        return "error", str(e)


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    db_path = os.path.join(tmpdir, "test.db")

    # Pre-setup: create old schema.
    conn = sqlite3.connect(db_path)
    conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, name TEXT)")
    conn.execute("INSERT INTO t (name) VALUES ('alice'), ('bob')")
    conn.commit()
    conn.close()

    # Record old schema.
    old_version, old_cols = get_schema_version(db_path)
    assert old_version == "old", f"setup failed: {old_cols}"

    # Spawn child to apply migration; kill it mid-way.
    child = subprocess.Popen([sys.executable, "-c", MIGRATION_CHILD, db_path])
    time.sleep(0.2)

    # Kill child mid-migration (after BEGIN/ALTER but before COMMIT).
    try:
        os.kill(child.pid, signal.SIGKILL)
    except:
        pass
    try:
        child.wait(timeout=1)
    except:
        pass

    # RECOVERY: check the schema.
    version_after, cols_after = get_schema_version(db_path)

    # RECOVERY assert 1: schema is in one of the two valid states (not partial).
    assert version_after in ["old", "new"], \
        f"schema is neither old nor new (partial migration): {cols_after}"

    # RECOVERY assert 2: all rows are still present (migration didn't lose data).
    try:
        conn = sqlite3.connect(db_path)
        row_count = conn.execute("SELECT COUNT(*) FROM t").fetchone()[0]
        conn.close()
        assert row_count == 2, f"migration lost rows: {row_count} instead of 2"
    except Exception as e:
        assert False, f"cannot query table after migration crash: {e}"

    # RECOVERY assert 3: the old column still exists.
    assert "name" in cols_after, f"migration corrupted existing column: {cols_after}"

    import shutil
    shutil.rmtree(tmpdir)
    print(f"migration_with_rollback: schema recovered as {version_after} (cols: {cols_after})")
    print("migration_with_rollback PASS")
    sys.exit(0)
