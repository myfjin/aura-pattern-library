"""
reader_writer_lock: many concurrent readers, but a writer needs exclusive access.
Failure simulated: (1) 3 readers run at once — they must NOT serialize behind each other;
(2) readers hold while a writer starts — the writer must WAIT, and must never overlap a reader.
Recovery asserted (both catch a no-op lock):
 - PARALLELISM: the 3-reader phase finishes in ~one hold, not three (wall-clock < 2*hold, and no
   single reader waited for another). A lock that serialized readers → phase ~3*hold → fails.
 - EXCLUSIVITY: reader/writer race-detection flags any overlap; the writer genuinely BLOCKS behind
   the readers (its wait > 0). A no-op lock lets writer+reader overlap → race_detected → fails.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys
import time
import threading
import random

HOLD = 0.2


class ReaderWriterLock:
    def __init__(self):
        self.readers = 0
        self.writers = 0
        self.writer_waiting = False
        self.cond = threading.Condition(threading.RLock())

    def acquire_read(self):
        with self.cond:
            while self.writers > 0 or self.writer_waiting:
                self.cond.wait()
            self.readers += 1

    def release_read(self):
        with self.cond:
            self.readers -= 1
            if self.readers == 0:
                self.cond.notify_all()

    def acquire_write(self):
        with self.cond:
            self.writer_waiting = True
            while self.readers > 0 or self.writers > 0:
                self.cond.wait()
            self.writer_waiting = False
            self.writers += 1

    def release_write(self):
        with self.cond:
            self.writers -= 1
            self.cond.notify_all()


def reader(lock, res, rid, state):
    start = time.time()
    lock.acquire_read()
    wait = time.time() - start
    with state["mx"]:
        state["active_readers"] += 1
        if state["writer_active"]:
            res[f"reader_{rid}_race"] = True
    time.sleep(HOLD)
    with state["mx"]:
        state["active_readers"] -= 1
    lock.release_read()
    res[f"reader_{rid}_ok"] = True
    res[f"reader_{rid}_wait"] = wait


def writer(lock, res, wid, state):
    start = time.time()
    lock.acquire_write()
    wait = time.time() - start
    with state["mx"]:
        state["writer_active"] = True
        if state["active_readers"] > 0:
            res[f"writer_{wid}_race"] = True
    time.sleep(HOLD)
    with state["mx"]:
        state["writer_active"] = False
    lock.release_write()
    res[f"writer_{wid}_ok"] = True
    res[f"writer_{wid}_wait"] = wait


if __name__ == "__main__":
    random.seed(42)
    lock = ReaderWriterLock()
    state = {"active_readers": 0, "writer_active": False, "mx": threading.Lock()}
    res = {}

    # --- Test 1: 3 readers concurrently ---
    phase_start = time.time()
    ts = [threading.Thread(target=reader, args=(lock, res, i, state)) for i in range(3)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    phase_wall = time.time() - phase_start

    for i in range(3):
        assert res.get(f"reader_{i}_ok"), f"reader {i} never ran"
        assert not res.get(f"reader_{i}_race"), f"reader {i} overlapped a writer"

    # PARALLELISM assert: concurrent readers finish in ~one hold. Serial readers would take
    # ~3*HOLD and each later reader's wait would be ~HOLD. Both bounds fail on a serializing lock.
    assert phase_wall < 2 * HOLD, f"readers serialized: phase {phase_wall:.3f}s ≈ 3*HOLD, not concurrent"
    assert max(res[f"reader_{i}_wait"] for i in range(3)) < 0.5 * HOLD, \
        "a reader waited for another reader (not concurrent)"

    # --- Test 2: readers hold, writer must WAIT and stay exclusive ---
    rt = [threading.Thread(target=reader, args=(lock, res, 10 + i, state)) for i in range(2)]
    for t in rt:
        t.start()
    time.sleep(0.05)                                  # let the readers acquire
    wt = threading.Thread(target=writer, args=(lock, res, 0, state))
    wt.start()
    for t in rt:
        t.join()
    wt.join()

    for i in range(2):
        assert res.get(f"reader_{10+i}_ok"), f"reader {10+i} never ran"
    assert res.get("writer_0_ok"), "writer never acquired"
    assert not res.get("writer_0_race"), "writer overlapped a reader (exclusivity broken)"
    # the writer genuinely blocked behind the readers (a no-op lock → wait ~0)
    assert res["writer_0_wait"] > 0.05, f"writer did not wait for readers: {res['writer_0_wait']:.3f}s"

    print(f"reader_writer_lock: 3 readers in {phase_wall:.2f}s (~1 hold, concurrent); "
          f"writer waited {res['writer_0_wait']:.2f}s, exclusive, no races")
    print("reader_writer_lock PASS")
    sys.exit(0)
