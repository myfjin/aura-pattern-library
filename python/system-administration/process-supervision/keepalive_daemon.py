"""
keepalive_daemon: a background thread pokes a keepalive file every interval; a watcher treats
the process as alive only while pokes keep arriving within a timeout.
Failure simulated (the real one): the daemon STOPS poking — the file goes stale.
Recovery asserted: while poking, check_keepalive() is True; after the daemon stops and the
timeout elapses, check_keepalive() flips to False — the stall is DETECTED (not because the
file was deleted, but because its timestamp went stale). A no-op watcher that always returns
True would fail the post-stop assert.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import threading
import time
import os
import tempfile
import sys


class KeepAliveDaemon:
    def __init__(self, poke_interval=0.05, timeout_threshold=0.3):
        self.poke_interval = poke_interval
        self.timeout = timeout_threshold
        self.poke_file = tempfile.mktemp(prefix="keepalive_", suffix=".txt")
        self.poke_count = 0
        self.running = True
        self.lock = threading.Lock()

    def poke(self):
        with self.lock:
            with open(self.poke_file, "w") as f:
                f.write(str(time.time()))
            self.poke_count += 1

    def keepalive_loop(self):
        while self.running:
            self.poke()
            time.sleep(self.poke_interval)

    def check_keepalive(self):
        """Alive iff the most recent poke is within the timeout window."""
        if not os.path.exists(self.poke_file):
            return False
        with open(self.poke_file, "r") as f:
            last = float(f.read().strip())
        return (time.time() - last) < self.timeout

    def stop(self):
        self.running = False            # stop poking, but LEAVE the file so staleness is detectable

    def cleanup(self):
        if os.path.exists(self.poke_file):
            os.remove(self.poke_file)


if __name__ == "__main__":
    daemon = KeepAliveDaemon(poke_interval=0.05, timeout_threshold=0.3)
    assert daemon.poke_count == 0, "poke_count should start at 0"

    t = threading.Thread(target=daemon.keepalive_loop, daemon=True)
    t.start()

    # Healthy path: pokes arrive → watcher reports alive.
    time.sleep(0.2)
    mid = daemon.poke_count
    assert mid >= 3, f"poke_count={mid}, expected >= 3 while poking"
    assert daemon.check_keepalive() is True, "keepalive should read healthy while poking"

    # THE FAILURE: stop poking (do NOT delete the file), let the timeout elapse.
    daemon.stop()
    t.join(timeout=1.0)
    after_stop = daemon.poke_count
    assert after_stop == mid, f"poke_count changed after stop: {mid} -> {after_stop}"

    # RECOVERY assert: the stall is DETECTED once the last poke ages past the timeout.
    assert daemon.check_keepalive() is True, "just after stop, the last poke is still fresh"
    time.sleep(daemon.timeout + 0.15)
    assert daemon.check_keepalive() is False, \
        "stalled daemon NOT detected — check_keepalive still True after timeout elapsed"

    daemon.cleanup()
    print(f"pokes={daemon.poke_count}; stall detected after {daemon.timeout}s timeout")
    print("keepalive_daemon PASS")
    sys.exit(0)
