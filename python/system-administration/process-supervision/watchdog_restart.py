"""
watchdog_restart: a real watchdog supervises a child, restarts it on death up to a cap,
then STOPS restarting and flags a crash-loop once the cap is exceeded.
Failure simulated: the watchdog's OWN child is SIGKILL'd repeatedly (real deaths).
Recovery asserted: the WATCHDOG (not the test) detects each death and restarts — assert the
watchdog's restart counter reached the cap and a live child exists; then one death past the
cap → assert it did NOT restart and raised the crash-loop flag. The assert fails on a no-op
watchdog (one that never restarts leaves the counter at 0 and the flag unset).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import subprocess
import os
import signal
import threading
import time
import sys


class Watchdog:
    def __init__(self, cap):
        self.cap = cap
        self.restarts = 0
        self.capped = False
        self.child = None
        self.running = True
        self.lock = threading.Lock()

    def _spawn(self):
        self.child = subprocess.Popen([sys.executable, "-c", "import signal; signal.pause()"])

    def run(self):
        with self.lock:
            self._spawn()                      # initial child (not counted as a restart)
        while self.running:
            with self.lock:
                dead = self.child is not None and self.child.poll() is not None
                if dead:
                    if self.restarts < self.cap:
                        self._spawn()
                        self.restarts += 1     # the WATCHDOG restarts, on a real death
                    else:
                        self.capped = True     # cap exceeded → stop restarting, flag it
                        self.child = None
                        self.running = False
                        break
            time.sleep(0.01)

    def kill_current(self):
        """Test hook: kill the watchdog's current child (a real death for it to detect)."""
        with self.lock:
            if self.child is not None and self.child.poll() is None:
                os.kill(self.child.pid, signal.SIGKILL)
                self.child.wait()

    def stop(self):
        self.running = False
        with self.lock:
            if self.child is not None and self.child.poll() is None:
                os.kill(self.child.pid, signal.SIGKILL)


def _wait_until(pred, timeout=3.0):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if pred():
            return True
        time.sleep(0.005)
    return False


if __name__ == "__main__":
    cap = 3
    wd = Watchdog(cap=cap)
    t = threading.Thread(target=wd.run, daemon=True)
    t.start()
    assert _wait_until(lambda: wd.child is not None), "watchdog never spawned its initial child"

    # Force `cap` real deaths; each time, wait for the WATCHDOG to observe it and restart.
    for n in range(1, cap + 1):
        wd.kill_current()
        assert _wait_until(lambda: wd.restarts >= n), f"watchdog did not restart after death {n}"

    # RECOVERY assert 1: the watchdog restarted exactly up to the cap and keeps a live child.
    with wd.lock:
        live = wd.child is not None and wd.child.poll() is None
    assert wd.restarts == cap, f"watchdog restarts={wd.restarts}, expected {cap}"
    assert live, "watchdog has no live child after restarting up to the cap"
    assert wd.capped is False, "cap flag set too early"

    # Now one death PAST the cap: the watchdog must refuse to restart and flag the crash-loop.
    wd.kill_current()
    assert _wait_until(lambda: wd.capped), "watchdog did not flag crash-loop after exceeding the cap"

    # RECOVERY assert 2: past the cap it did NOT restart (counter unchanged) and no live child.
    assert wd.restarts == cap, f"watchdog restarted past the cap: {wd.restarts} > {cap}"
    with wd.lock:
        assert wd.child is None, "watchdog kept a child alive past the crash-loop cap"

    wd.stop()
    t.join(timeout=1.0)
    print(f"watchdog: restarts={wd.restarts} (cap {cap}), crash_loop_capped={wd.capped}")
    print("watchdog_restart PASS")
    sys.exit(0)
