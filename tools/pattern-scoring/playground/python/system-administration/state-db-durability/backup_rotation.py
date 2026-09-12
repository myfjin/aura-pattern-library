"""
backup_rotation: keep N versioned backups; rotate with ATOMIC renames so a crash during rotation
never tears a file and never loses the newest backup.
Failure simulated: SIGKILL the process DURING the rotation rename sequence (not before it).
Recovery asserted (unconditional): after the crash, (1) EVERY surviving backup file is COMPLETE
(never a torn/half-written file — guaranteed by rename atomicity), and (2) the NEWEST backup's
content still exists somewhere (renames move it, never delete it). A naive copy-based rotation
(read+write) killed mid-copy leaves a torn file and FAILS (1).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
import subprocess
import signal
import time
import shutil

# child: create v1..v3 (complete, fsync'd), then rotate via atomic renames with pauses so the
# parent's SIGKILL lands DURING the rename sequence.
CHILD = r"""
import os, sys, time
d = sys.argv[1]
def p(v): return os.path.join(d, "backup.v%d.txt" % v)
for i in (1, 2, 3):
    with open(p(i), "w") as f:
        f.write("backup_data_version_%d\n" % i); f.flush(); os.fsync(f.fileno())
open(os.path.join(d, "ready"), "w").close()
time.sleep(0.15)                 # parent kills somewhere in this window / the renames below
os.unlink(p(1))                  # drop oldest
time.sleep(0.15)
os.rename(p(2), p(1))            # shift (atomic)
time.sleep(0.15)
os.rename(p(3), p(2))            # shift (atomic)
"""


def surviving_backups(d):
    out = []
    for f in sorted(os.listdir(d)):
        if f.startswith("backup.v") and f.endswith(".txt"):
            out.append((f, open(os.path.join(d, f)).read()))
    return out


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    bdir = os.path.join(tmpdir, "backups")
    os.makedirs(bdir)

    child = subprocess.Popen([sys.executable, "-c", CHILD, bdir])
    while not os.path.exists(os.path.join(bdir, "ready")):
        time.sleep(0.005)
    time.sleep(0.20)                     # land the kill inside the rename sequence
    os.kill(child.pid, signal.SIGKILL)
    try:
        child.wait(timeout=1)
    except Exception:
        pass

    survivors = surviving_backups(bdir)

    # RECOVERY assert 1 (no torn file): every surviving backup is a COMPLETE record. Rename
    # atomicity guarantees this; a naive copy-based rotation killed mid-write leaves a partial file.
    assert survivors, "rotation crash lost ALL backups"
    for name, content in survivors:
        assert content.startswith("backup_data_version_") and content.endswith("\n"), \
            f"{name} is TORN/incomplete: {content!r}"

    # RECOVERY assert 2 (newest never lost): version_3's content survives the rotation crash
    # (it is only ever renamed, never unlinked).
    all_content = "".join(c for _, c in survivors)
    assert "backup_data_version_3" in all_content, "the NEWEST backup was lost during rotation"

    shutil.rmtree(tmpdir)
    print(f"backup_rotation: crash mid-rotation left {len(survivors)} complete backup(s), newest preserved")
    print("backup_rotation PASS")
    sys.exit(0)
