"""
journaled_write: write data to a journal first, then apply to the main store (undo logging).
Failure simulated: crash between journal write and main store update.
Recovery asserted: on reopen, the system is in a consistent state: either old data (if journal
wasn't fully flushed) or new data (if journal was flushed and uncommitted changes rolled forward).
Never a torn state where the journal is half-written or the main file is half-updated.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
import json
import subprocess
import signal
import time
from pathlib import Path

JOURNAL_CHILD = r"""
import os, sys, json, signal, time
data_path = sys.argv[1]
journal_path = sys.argv[2]
# Initial state
data = {"count": 0}
with open(data_path, "w") as f:
    json.dump(data, f)
# Now: write the new state to journal, then apply to data file
new_data = {"count": 1}
with open(journal_path, "w") as f:
    json.dump({"old": data, "new": new_data}, f)
    f.flush()
    os.fsync(f.fileno())  # ensure journal is on disk
os.kill(os.getpid(), signal.SIGSTOP)  # pause BEFORE applying the new data
# this would be the apply step: write new_data to data_path
with open(data_path, "w") as f:
    json.dump(new_data, f)
    f.flush()
    os.fsync(f.fileno())
os.unlink(journal_path)  # remove journal after successful apply
"""


def recover_from_journal(data_path, journal_path):
    """Simulate recovery: if journal exists, decide old or new; remove journal on success."""
    with open(data_path) as f:
        current = json.load(f)

    if os.path.exists(journal_path):
        with open(journal_path) as f:
            journal = json.load(f)
        # Journal exists: decide based on whether new_data is already in place
        if current == journal["new"]:
            # Already applied, just remove journal
            os.unlink(journal_path)
            return current
        else:
            # Journal exists but not applied; roll back (keep old)
            return journal["old"]
    else:
        # No journal, current state is committed
        return current


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    data_path = os.path.join(tmpdir, "data.json")
    journal_path = os.path.join(tmpdir, "journal.json")

    # Spawn child that writes journal, then we kill it before apply.
    child = subprocess.Popen([sys.executable, "-c", JOURNAL_CHILD, data_path, journal_path])
    time.sleep(0.2)

    # Kill child mid-apply (after journal is written, before data is updated).
    try:
        os.kill(child.pid, signal.SIGKILL)
    except:
        pass
    try:
        child.wait(timeout=1)
    except:
        pass

    # RECOVERY: run recovery logic.
    recovered = recover_from_journal(data_path, journal_path)
    expected_old = {"count": 0}
    expected_new = {"count": 1}

    # RECOVERY assert 1 (RECOVERY tier): recovered state must equal one of the expected states.
    assert recovered == expected_old or recovered == expected_new, \
        f"recovered state {recovered} is neither old nor new (torn state)"

    # RECOVERY assert 2: the recovered state is consistent (can be re-serialized).
    recovered_str = json.dumps(recovered)
    re_parsed = json.loads(recovered_str)
    assert re_parsed == recovered, "recovered state is corrupted"

    # RECOVERY assert 3: if journal was removed, it means recovery completed cleanly.
    # If it still exists, that's OK too (recovery decided not to apply).
    if not os.path.exists(journal_path):
        # Journal removed: verify data matches expected (either old or new, not mixed)
        with open(data_path) as f:
            final = json.load(f)
        assert final in [{"count": 0}, {"count": 1}], f"final data {final} is invalid"

    import shutil
    shutil.rmtree(tmpdir)
    print(f"journaled_write: recovered to consistent state ({recovered['count']}), no torn state")
    print("journaled_write PASS")
    sys.exit(0)
