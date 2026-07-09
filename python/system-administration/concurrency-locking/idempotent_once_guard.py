"""
idempotent_once_guard: ensure an idempotent action runs exactly once, even if called
from multiple processes concurrently. Failure simulated: two processes call the action
at the same time; only one should succeed and modify the shared state, the other should
skip (already done). Recovery asserted: (1) the action ran exactly once (counter=1), (2)
both processes completed, (3) the second process detected "already done" and returned False.
A no-op guard would allow the action to run twice (or more), violating "exactly once".
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
import fcntl
import time
import multiprocessing
import random
import json

def idempotent_action_once(marker_file, results_dict, caller_id):
    """
    Run an idempotent action exactly once using a marker file + lock.
    The marker file indicates "action already done"; use a lock to serialize the check-and-run.
    Returns True if the action ran, False if already done.
    """
    lockfile = marker_file + ".lock"

    # Acquire lock to serialize access
    with open(lockfile, "a") as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        try:
            # Check if marker already exists
            if os.path.exists(marker_file):
                # Already done
                results_dict[f"caller_{caller_id}_ran_action"] = False
                results_dict[f"caller_{caller_id}_already_done"] = True
                return False

            # Not done yet; run the action
            # Simulate action: write a counter file
            counter_file = marker_file + ".counter"
            try:
                with open(counter_file, "r") as cf:
                    data = json.load(cf)
                counter = data.get("count", 0)
            except (FileNotFoundError, json.JSONDecodeError):
                counter = 0

            # Increment and write
            counter += 1
            with open(counter_file, "w") as cf:
                json.dump({"count": counter}, cf)

            # Write marker to indicate action is done
            with open(marker_file, "w") as mf:
                mf.write(str(os.getpid()))

            results_dict[f"caller_{caller_id}_ran_action"] = True
            results_dict[f"caller_{caller_id}_already_done"] = False
            return True
        finally:
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)

if __name__ == "__main__":
    random.seed(42)
    tmpdir = tempfile.mkdtemp()
    marker_file = os.path.join(tmpdir, "action.done")
    lockfile = marker_file + ".lock"
    counter_file = marker_file + ".counter"

    # Pre-create lock file
    with open(lockfile, "w") as f:
        f.write("")

    with multiprocessing.Manager() as manager:
        results = manager.dict()

        # Launch two callers at roughly the same time
        processes = []
        for i in range(2):
            p = multiprocessing.Process(target=idempotent_action_once, args=(marker_file, results, i))
            processes.append(p)

        for p in processes:
            p.start()
        for p in processes:
            p.join(timeout=5)

        # Exactly one caller should have run the action
        ran_count = sum(1 for i in range(2) if results.get(f"caller_{i}_ran_action"))
        assert ran_count == 1, f"Expected 1 caller to run action, got {ran_count}"

        # The other caller should have detected "already done"
        already_done_count = sum(1 for i in range(2) if results.get(f"caller_{i}_already_done"))
        assert already_done_count == 1, f"Expected 1 caller to see 'already done', got {already_done_count}"

        # The counter must be exactly 1 (action ran once)
        try:
            with open(counter_file, "r") as cf:
                data = json.load(cf)
            counter_value = data.get("count", 0)
        except (FileNotFoundError, json.JSONDecodeError):
            counter_value = 0

        assert counter_value == 1, f"Expected counter=1, got {counter_value}"

        # The marker file must exist (proof action ran)
        assert os.path.exists(marker_file), "marker file not created"

    import shutil
    shutil.rmtree(tmpdir)
    print(f"idempotent_once_guard: 2 callers; action ran exactly once (counter={counter_value}); 1 caller saw 'already done'")
    print("idempotent_once_guard PASS")
    sys.exit(0)
