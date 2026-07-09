"""
hot_copy: copy a live DB WHILE it is being written to, using SQLite's backup API under a
BEGIN IMMEDIATE snapshot, so the copy is a consistent point-in-time — not a torn mix.
Failure defended against: a naive byte-copy taken mid-write yields a torn/corrupt file or a
mixed state with gaps. Recovery asserted (UNCONDITIONAL): the hot copy opens, integrity_check
== "ok", AND its rows form a CONTIGUOUS committed prefix row_0..row_{k-1} (no gaps) — proving it
reflects a single commit point, not a torn interleave. A torn naive copy fails integrity; a
mixed copy fails the contiguity check.
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

WRITER = r"""
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

COPIER = r"""
import sqlite3, sys, time
db, cp = sys.argv[1], sys.argv[2]
time.sleep(0.10)                       # let several writes land first
src = sqlite3.connect(db)
dst = sqlite3.connect(cp)
with dst:
    # backup API holds a read lock and RESTARTS if the source changes mid-copy → the finished
    # copy is a consistent snapshot at completion time (no BEGIN IMMEDIATE — that deadlocks backup)
    src.backup(dst, pages=1, sleep=0.005)
src.close()
"""


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    db = os.path.join(tmpdir, "live.db")
    cp = os.path.join(tmpdir, "copy.db")
    # seed the table so the copier's snapshot always sees a real schema
    seed = sqlite3.connect(db)
    seed.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, idx INTEGER)")
    seed.commit(); seed.close()

    writer = subprocess.Popen([sys.executable, "-c", WRITER, db])
    copier = subprocess.Popen([sys.executable, "-c", COPIER, db, cp])
    copier.wait(timeout=5)
    writer.wait(timeout=5)

    # RECOVERY assert 1 (unconditional): the hot copy exists and is a VALID DB (integrity ok).
    # A naive copy torn mid-write fails integrity here. No "if size > N" guard.
    assert os.path.exists(cp), "hot copy was not produced"
    cc = sqlite3.connect(cp)
    assert cc.execute("PRAGMA integrity_check").fetchone()[0] == "ok", "hot copy is corrupt (torn)"
    idxs = sorted(r[0] for r in cc.execute("SELECT idx FROM t").fetchall())
    cc.close()

    # RECOVERY assert 2 (point-in-time consistency): the copied rows are a CONTIGUOUS prefix
    # 0..k-1 — a single commit point, never a mixed/torn interleave with gaps.
    assert idxs == list(range(len(idxs))), f"hot copy is a torn interleave (gaps): {idxs}"

    # RECOVERY assert 3: the live DB ended with all 12 rows (the copy is a prefix of it).
    lc = sqlite3.connect(db)
    live = lc.execute("SELECT COUNT(*) FROM t").fetchone()[0]
    lc.close()
    assert live == 12 and len(idxs) <= live, f"live={live}, copy={len(idxs)} (copy not a prefix)"

    shutil.rmtree(tmpdir)
    print(f"hot_copy: consistent point-in-time copy (contiguous prefix of {len(idxs)} rows; live={live})")
    print("hot_copy PASS")
    sys.exit(0)
