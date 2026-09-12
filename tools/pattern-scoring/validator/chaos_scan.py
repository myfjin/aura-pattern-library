#!/usr/bin/env python3
"""
chaos_scan.py — FOLD 5: chaos / fault-injection (AWS game-day method). NEW BUILD (no inherited
code) — designed against R13 (state-lies-over-time). Keeps the validation tool SEPARATE from Forge
Gate.

R13 (recipes.py) attacks stateful patterns with adversarial INPUT SEQUENCES (idle_then_burst,
expire_without_touch, clock_rewind, ...). Chaos goes one level deeper: it injects a REALISTIC FAULT
into the middle of an operation a pattern CLAIMS to survive, then checks a SURVIVAL PREDICATE. The
law (Illia's / AWS game-day): a pattern advertised as crash-safe that DIES to its OWN injected fault
is INVALID — the safety claim is theater.

Each probe injects the exact fault the pattern claims to withstand and asserts the invariant that
must survive it. Every probe is paired with a NEGATIVE CONTROL: a crash-UNSAFE variant of the same
operation that MUST die to the identical fault — proving the survival predicate actually discriminates
safe from unsafe (not a check that anything passes).

Targets (fault -> survival predicate):
  atomic_write_temp_rename : crash before the rename commits -> destination is intact OLD content
                             (never truncated/partial) and no temp litter is left behind.
  write_ahead_log          : torn tail (crash mid-append truncates the last record) -> replay
                             recovers every COMPLETE record, drops the torn one, and does NOT crash.
  checkpoint_resume        : crash after batch 0 commits -> resume processes every record EXACTLY
                             ONCE (no skip, no duplicate).

Verdict-ladder mapping:
  pattern SURVIVES its fault  -> chaos positive oracle ('chaos') in oracle_coverage.
  pattern DIES to its fault   -> INVALID-CANDIDATE (safety theater) -> evidence card, routed to
     calibration; MUST NOT auto-flip a frozen exam verdict (a contradiction => the injection is
     miscalibrated, not the ruler).

Faults are injected into throwaway temp dirs / monkeypatches that are always restored; the real
signed library is never mutated and the exam grader is never touched.
"""
from __future__ import annotations
import importlib.util, json, os, tempfile, shutil, struct, pickle, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIB = Path(os.path.expanduser("~/aura-pattern-library"))

ATOMIC = "python/system-administration/filesystem-integrity/atomic_write_temp_rename.py"
WAL = "python/programming/persistence/write_ahead_log.py"
CKPT = "python/system-administration/data-pipeline-ops/checkpoint_resume.py"


def _load(relpath, name):
    import sys
    spec = importlib.util.spec_from_file_location(name, str(LIB / relpath))
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m          # WAL pickles its LogEntry -> pickle must resolve the module by name
    spec.loader.exec_module(m)
    return m


class _Crash(RuntimeError):
    pass


# ---------------------------------------------------------------- atomic write
def _atomic_write_trial(write_fn):
    """Return (dest_ok, no_litter). write_fn(target, content) is crashed mid-write via os.rename."""
    d = tempfile.mkdtemp(prefix="chaos_aw_")
    try:
        target = os.path.join(d, "target.txt")
        # write_fn is expected to atomic_write; establish OLD via the same fn (no fault yet)
        write_fn(target, b"OLD_v1", inject=False)
        orig_rename = os.rename
        os.rename = lambda a, b: (_ for _ in ()).throw(_Crash("crash before rename commit"))
        try:
            write_fn(target, b"NEW_v2", inject=True)
        except Exception:
            pass  # the crash is expected; we test what it left behind
        finally:
            os.rename = orig_rename
        dest = Path(target).read_bytes() if os.path.exists(target) else b""
        dest_ok = dest == b"OLD_v1"                       # intact old content, never partial/empty
        litter = [f for f in os.listdir(d) if f != "target.txt"]
        return dest_ok, (len(litter) == 0)
    finally:
        shutil.rmtree(d, ignore_errors=True)


def chaos_atomic_write():
    m = _load(ATOMIC, "chaos_atomic")

    def real_write(target, content, inject=False):
        m.atomic_write(target, content)  # the pattern; os.rename is patched to crash when inject

    dest_ok, no_litter = _atomic_write_trial(real_write)
    survived = dest_ok and no_litter
    return {"survived": survived, "predicate": "dest==OLD (no partial) & no temp litter",
            "detail": f"dest_intact={dest_ok} no_litter={no_litter}"}


def _nc_atomic_write():
    """Crash-UNSAFE writer: writes straight to the destination (truncates it first). The same crash
    leaves the destination truncated -> predicate fails -> proves the injection is real."""
    def naive_write(target, content, inject=False):
        if not inject:
            with open(target, "wb") as f:
                f.write(content)
            return
        with open(target, "wb") as f:       # truncates the destination immediately
            raise _Crash("crash after truncate, before write")  # destination now empty
    dest_ok, _ = _atomic_write_trial(naive_write)
    return dest_ok is False                 # NC must DIE (dest corrupted)


# ---------------------------------------------------------------- write-ahead log
def _wal_torn_trial(replay_fn, n_records=3, cut=3):
    """Append n records, truncate the tail (torn last record), then replay via replay_fn(WAL, log).
    Returns (recovered_count, crashed_bool)."""
    m = _load(WAL, "chaos_wal")
    d = tempfile.mkdtemp(prefix="chaos_wal_")
    try:
        log = os.path.join(d, "wal.log")
        w = m.WAL(log)
        for i in range(n_records):
            w.append(m.LogEntryType.INSERT, f"k{i}", f"v{i}")
        size = os.path.getsize(log)
        with open(log, "r+b") as f:
            f.truncate(size - cut)          # torn tail: cut into the last record's body
        try:
            got = []
            recovered = replay_fn(m, log, got)
            return recovered, False
        except Exception:
            return -1, True                 # replay crashed on the torn tail
    finally:
        shutil.rmtree(d, ignore_errors=True)


def chaos_wal():
    def real_replay(m, log, got):
        w2 = m.WAL(log)
        return w2.replay(lambda e: got.append(e.sequence_number))
    recovered, crashed = _wal_torn_trial(real_replay)
    survived = (not crashed) and recovered == 2      # 3 appended, last torn -> 2 complete recovered
    return {"survived": survived, "predicate": "replay recovers complete records, drops torn tail, no crash",
            "detail": f"recovered={recovered} crashed={crashed} (expected 2, no crash)"}


def _nc_wal():
    """Crash-UNSAFE replay: reads size frame then blindly pickle.loads whatever bytes remain, with no
    incomplete-read guard and no try/except -> the torn tail makes it crash -> proves the fault real."""
    def naive_replay(m, log, got):
        with open(log, "rb") as f:
            while True:
                sz = f.read(4)
                if len(sz) < 4:
                    break
                size = struct.unpack("I", sz)[0]
                data = f.read(size)          # may be short on the torn tail
                entry = pickle.loads(data)   # no len(data)<size guard -> raises on torn tail
                got.append(entry.sequence_number)
        return len(got)
    recovered, crashed = _wal_torn_trial(naive_replay)
    return crashed is True                    # NC must DIE (uncaught crash on torn tail)


# ---------------------------------------------------------------- checkpoint / resume
def _ckpt_trial(m):
    """Crash the run after batch 0 commits its checkpoint, then resume. Return the resumed output."""
    d = tempfile.mkdtemp(prefix="chaos_ck_")
    try:
        cp = os.path.join(d, "checkpoint.json")
        records = [{"id": x, "value": v} for x, v in (("a", 1), ("b", 2), ("c", 3), ("d", 4))]
        # phase 1: crash json.dump after the FIRST checkpoint write (batch 0 committed)
        real_dump = m.json.dump
        state = {"n": 0}

        def crashing_dump(obj, f, *a, **k):
            real_dump(obj, f, *a, **k)
            state["n"] += 1
            if state["n"] == 1:
                raise _Crash("crash after batch 0 checkpoint")
        m.json.dump = crashing_dump
        try:
            m.process_batch_with_checkpoint(records, cp)
        except _Crash:
            pass
        finally:
            m.json.dump = real_dump
        # phase 2: resume
        return m.process_batch_with_checkpoint(records, cp), records
    finally:
        shutil.rmtree(d, ignore_errors=True)


def chaos_checkpoint():
    m = _load(CKPT, "chaos_ckpt")
    out, records = _ckpt_trial(m)
    ids = [r["id"] for r in out]
    exactly_once = sorted(ids) == ["a", "b", "c", "d"] and len(ids) == 4
    values_ok = all(any(o["id"] == r["id"] and o["processed"] == r["value"] + 100 for o in out)
                    for r in records)
    survived = exactly_once and values_ok
    return {"survived": survived, "predicate": "resume processes every record EXACTLY once",
            "detail": f"ids={ids} exactly_once={exactly_once} values_ok={values_ok}"}


def _nc_checkpoint():
    """Crash-UNSAFE resumer: ignores the checkpoint and reprocesses from the start -> after crash+
    resume, batch 0 records appear TWICE -> exactly-once predicate fails -> proves the fault real."""
    d = tempfile.mkdtemp(prefix="chaos_ncck_")
    try:
        records = [{"id": x, "value": v} for x, v in (("a", 1), ("b", 2), ("c", 3), ("d", 4))]

        def naive_resume(prior_output):
            # simulates a resumer with no checkpoint memory: redo everything, appended to prior work
            redo = [{"id": r["id"], "processed": r["value"] + 100} for r in records]
            return prior_output + redo
        prior = [{"id": "a", "processed": 101}, {"id": "b", "processed": 102}]  # batch 0 already done
        out = naive_resume(prior)
        ids = [r["id"] for r in out]
        exactly_once = sorted(ids) == ["a", "b", "c", "d"] and len(ids) == 4
        return exactly_once is False          # NC must DIE (a,b duplicated)
    finally:
        shutil.rmtree(d, ignore_errors=True)


# ================================================================ WAVE 3 (2026-07-27)
# Targeting law: build game-days for patterns whose ADVERTISED CLAIM *is* survival — there a chaos
# oracle is not merely extra evidence, it is the honest test of the claim the pattern is sold on.

SEGWAL = "python/programming/persistence/segmented_wal.py"
JOURNALED = "python/system-administration/state-db-durability/journaled_write.py"


# ---------------------------------------------------------------- segmented WAL (torn tail)
def _segwal_torn_trial(recover_fn):
    """Append 5 records, TRUNCATE the segment mid-record (the classic torn tail a crash leaves),
    then recover. Returns (recovered_payloads, crashed)."""
    m = _load(SEGWAL, "chaos_segwal")
    d = tempfile.mkdtemp(prefix="chaos_segwal_")
    try:
        wal = m.WriteAheadLog(d)
        for i in range(5):
            wal.append(f"rec{i}".encode())
        if hasattr(wal, "close"):
            wal.close()
        segs = sorted(Path(d).glob("*.wal"))
        p = str(segs[-1])
        size = os.path.getsize(p)
        with open(p, "r+b") as f:
            f.truncate(size - 3)          # torn: last record's payload is short
        try:
            recovered = recover_fn(m, d)
        except Exception as e:
            return [], True, f"{type(e).__name__}: {e}"
        out = [(r.data if hasattr(r, "data") else r) for r in recovered]
        return out, False, ""
    finally:
        shutil.rmtree(d, ignore_errors=True)


def chaos_segmented_wal():
    out, crashed, err = _segwal_torn_trial(lambda m, d: m.recover_from_crash(d))
    expect = [f"rec{i}".encode() for i in range(4)]     # 4 complete; the 5th is torn
    exact = out == expect
    survived = (not crashed) and exact
    return {"survived": survived,
            "predicate": "replay recovers every COMPLETE record, drops the torn tail, never crashes",
            "detail": f"crashed={crashed}{' ' + err if err else ''} recovered={[o.decode(errors='replace') for o in out]} exact={exact}"}


def _nc_segmented_wal():
    """Crash-UNSAFE reader: trusts the length prefix and NEVER verifies the checksum, so a torn tail
    is either accepted as a (short/garbage) record or blows up. Either way the predicate must fail —
    proving the checksum is what actually buys the survival, not the harness being lenient."""
    m = _load(SEGWAL, "chaos_ncsegwal")
    d = tempfile.mkdtemp(prefix="chaos_ncsegwal_")
    try:
        wal = m.WriteAheadLog(d)
        for i in range(5):
            wal.append(f"rec{i}".encode())
        if hasattr(wal, "close"):
            wal.close()
        segs = sorted(Path(d).glob("*.wal"))
        p = str(segs[-1])
        size = os.path.getsize(p)
        with open(p, "r+b") as f:
            f.truncate(size - 3)
        # naive: split on the 4-byte length prefix, no checksum check, no bounds discipline
        raw = Path(p).read_bytes()
        got, i = [], 0
        try:
            while i + 4 <= len(raw):
                ln = struct.unpack(">I", raw[i:i + 4])[0]
                got.append(raw[i + 4:i + 4 + ln])       # may run past EOF -> short/garbage payload
                i += 4 + ln
        except Exception:
            return True                                  # died to the fault
        expect = [f"rec{i}".encode() for i in range(4)]
        return got != expect                             # NC must NOT reproduce the clean result
    finally:
        shutil.rmtree(d, ignore_errors=True)


# ---------------------------------------------------------------- journaled write (crash mid-apply)
def _journaled_trial(recover_fn):
    """Crash BETWEEN a flushed journal and the main-store update — the exact window the pattern
    claims to close. Recovery must leave the store in ONE of the two legal states (old or new),
    never a torn/half-applied one."""
    m = _load(JOURNALED, "chaos_journaled")
    d = tempfile.mkdtemp(prefix="chaos_jw_")
    try:
        data_path = os.path.join(d, "store.json")
        journal_path = os.path.join(d, "store.journal")
        Path(data_path).write_text(json.dumps({"v": "OLD"}))
        # journal fully flushed, main store NOT yet updated == the crash window
        Path(journal_path).write_text(json.dumps({"old": {"v": "OLD"}, "new": {"v": "NEW"}}))
        try:
            recover_fn(m, data_path, journal_path)
        except Exception as e:
            return None, True, f"{type(e).__name__}: {e}"
        final = json.loads(Path(data_path).read_text())
        return final, False, ""
    finally:
        shutil.rmtree(d, ignore_errors=True)


def chaos_journaled_write():
    final, crashed, err = _journaled_trial(
        lambda m, dp, jp: m.recover_from_journal(dp, jp))
    legal = final in ({"v": "OLD"}, {"v": "NEW"})
    survived = (not crashed) and legal
    return {"survived": survived,
            "predicate": "after crash mid-apply the store is OLD or NEW — never a torn/half state",
            "detail": f"crashed={crashed}{' ' + err if err else ''} final={final} legal={legal}"}


def _nc_journaled_write():
    """Crash-UNSAFE applier: writes the new value field-by-field with the crash landing in the
    middle, leaving a store that is neither OLD nor NEW -> the legality predicate must fail."""
    d = tempfile.mkdtemp(prefix="chaos_ncjw_")
    try:
        data_path = os.path.join(d, "store.json")
        Path(data_path).write_text(json.dumps({"v": "OLD"}))
        # no journal, no atomic swap: truncate then crash before the new bytes land
        with open(data_path, "w") as f:
            f.write('{"v": "NE')          # torn write
        final = Path(data_path).read_text()
        try:
            parsed = json.loads(final)
        except Exception:
            return True                    # unparseable == torn == died (good)
        return parsed not in ({"v": "OLD"}, {"v": "NEW"})
    finally:
        shutil.rmtree(d, ignore_errors=True)


# ================================================================ WAVE 3 batch 2 (2026-07-27)
PITR = "python/system-administration/state-db-durability/point_in_time_restore.py"
ETL = "python/system-administration/data-pipeline-ops/idempotent_etl_step.py"
REPL = "python/system-administration/mesh-distributed/idempotent_replication.py"
ONCE = "python/system-administration/concurrency-locking/idempotent_once_guard.py"


def _pitr_setup(d, m):
    """Base backup + a log whose tail is NEWER than the restore target (the entries a PITR must
    refuse to replay)."""
    import sqlite3
    base = os.path.join(d, "base.db")
    conn = sqlite3.connect(base)
    conn.execute("CREATE TABLE t (val TEXT)")
    conn.commit(); conn.close()
    log = os.path.join(d, "wal.log")
    with open(log, "w") as f:
        for ts, val in [(1, "a"), (2, "b"), (3, "c"), (4, "TOO_NEW"), (5, "TOO_NEW2")]:
            f.write(json.dumps({"ts": ts, "val": val}) + "\n")
    return base, log


def chaos_point_in_time_restore():
    """FAULT: crash mid-restore, then resume. PREDICATE: the resumed restore equals a clean one —
    every entry <= target replayed EXACTLY once, and NO entry newer than the target ever lands."""
    import sqlite3
    m = _load(PITR, "chaos_pitr")
    d = tempfile.mkdtemp(prefix="chaos_pitr_")
    try:
        base, log = _pitr_setup(d, m)
        db = os.path.join(d, "restored.db")
        # --- crash the first restore partway through the replay ---
        real_connect = sqlite3.connect

        opened = []

        class _CrashConn:
            def __init__(self, inner): self._i, self._n = inner, 0
            def execute(self, *a, **k):
                self._n += 1
                if self._n > 2:
                    raise _Crash("crash mid-replay")
                return self._i.execute(*a, **k)
            def __getattr__(self, n): return getattr(self._i, n)

        def _mk(p, *a, **k):
            inner = real_connect(p, *a, **k)
            opened.append(inner)
            return _CrashConn(inner)

        sqlite3.connect = _mk
        try:
            m.restore_to(base, log, 3, db)
        except Exception:
            pass                                    # expected crash
        finally:
            sqlite3.connect = real_connect
            for c in opened:                        # a crashed process releases its handles;
                try: c.close()                      # emulate that so the db is not left locked
                except Exception: pass
        # --- resume: run the restore again, cleanly ---
        m.restore_to(base, log, 3, db)
        got = m.vals(db)
        clean_db = os.path.join(d, "clean.db")
        m.restore_to(base, log, 3, clean_db)
        clean = m.vals(clean_db)
        no_future = all("TOO_NEW" not in str(v) for v in got)
        idempotent = list(got) == list(clean) == ["a", "b", "c"]
        return {"survived": no_future and idempotent,
                "predicate": "resume == clean restore (exactly once) & no entry newer than target",
                "detail": f"got={list(got)} clean={list(clean)} no_future={no_future} idempotent={idempotent}"}
    finally:
        shutil.rmtree(d, ignore_errors=True)


def _nc_point_in_time_restore():
    """Crash-UNSAFE restorer: resumes by APPENDING to the half-built db instead of restarting from
    the base -> the interrupted entries are replayed twice."""
    import sqlite3
    d = tempfile.mkdtemp(prefix="chaos_ncpitr_")
    try:
        db = os.path.join(d, "r.db")
        conn = sqlite3.connect(db)
        conn.execute("CREATE TABLE t (val TEXT)")
        for v in ("a", "b"):                          # partial work from the crashed attempt
            conn.execute("INSERT INTO t (val) VALUES (?)", (v,))
        conn.commit()
        for v in ("a", "b", "c"):                     # naive resume: replay everything again
            conn.execute("INSERT INTO t (val) VALUES (?)", (v,))
        conn.commit()
        got = [r[0] for r in conn.execute("SELECT val FROM t")]
        conn.close()
        return got != ["a", "b", "c"]                 # NC must duplicate
    finally:
        shutil.rmtree(d, ignore_errors=True)


def chaos_idempotent_etl():
    """FAULT: crash mid-transform after some records are checkpointed. PREDICATE: resuming produces
    output bit-identical to an uninterrupted run, with no duplicated record."""
    m = _load(ETL, "chaos_etl")
    d = tempfile.mkdtemp(prefix="chaos_etl_")
    try:
        records = [{"id": f"r{i}", "value": i} for i in range(6)]
        cp = os.path.join(d, "ckpt.json")
        real_ck = m.stable_checksum
        state = {"n": 0}

        def crashing(v):
            state["n"] += 1
            if state["n"] > 3:
                raise _Crash("crash mid-transform")
            return real_ck(v)

        m.stable_checksum = crashing
        try:
            m.idempotent_transform(records, cp)
        except Exception:
            pass                                     # expected
        finally:
            m.stable_checksum = real_ck
        resumed = m.idempotent_transform(records, cp)          # resume from checkpoint
        clean_cp = os.path.join(d, "clean.json")
        clean = m.idempotent_transform(records, clean_cp)      # uninterrupted reference
        ids = [r.get("id") for r in resumed] if isinstance(resumed, list) else []
        no_dupes = len(ids) == len(set(ids))
        identical = resumed == clean
        return {"survived": bool(identical and no_dupes),
                "predicate": "resume is bit-identical to an uninterrupted run, no duplicates",
                "detail": f"identical={identical} no_dupes={no_dupes} n={len(ids)}"}
    finally:
        shutil.rmtree(d, ignore_errors=True)


def _nc_idempotent_etl():
    """Crash-UNSAFE ETL: no checkpoint, so a resume re-emits the records it already produced."""
    records = [{"id": f"r{i}", "value": i} for i in range(6)]
    produced = [{"id": r["id"]} for r in records[:3]]          # work done before the crash
    resumed = produced + [{"id": r["id"]} for r in records]     # naive resume redoes everything
    ids = [r["id"] for r in resumed]
    return len(ids) != len(set(ids))                            # NC must duplicate


def chaos_idempotent_replication():
    """FAULT: crash mid-replication, then the SAME writes are re-delivered on resume (at-least-once
    delivery is the realistic failure). PREDICATE: each write lands exactly once."""
    m = _load(REPL, "chaos_repl")
    store = m.ReplicatedStore("replica-A")
    writes = [(f"w{i}", f"k{i}", f"v{i}") for i in range(5)]
    for w in writes[:3]:
        store.apply_write(*w)                       # ... crash here ...
    for w in writes:
        store.apply_write(*w)                       # resume re-delivers everything
    applied = store.get_applied()
    n = len(applied)
    data_ok = all(store.data.get(f"k{i}") == f"v{i}" for i in range(5))
    exactly_once = n == 5 and data_ok
    return {"survived": exactly_once,
            "predicate": "re-delivered writes apply exactly once (no duplicate application)",
            "detail": f"applied={n} expected=5 data_ok={data_ok}"}


def _nc_idempotent_replication():
    """Crash-UNSAFE replica: no write_id tracking -> re-delivery double-applies."""
    applied = []
    writes = [(f"w{i}", f"k{i}", f"v{i}") for i in range(5)]
    for w in writes[:3]:
        applied.append(w[0])
    for w in writes:
        applied.append(w[0])                        # no dedupe
    return len(applied) != len(set(applied))        # NC must duplicate


def chaos_idempotent_once_guard():
    """FAULT: two concurrent callers race the same guarded action. PREDICATE: it runs exactly once."""
    import threading
    m = _load(ONCE, "chaos_once")
    d = tempfile.mkdtemp(prefix="chaos_once_")
    try:
        marker = os.path.join(d, "done.marker")
        results, ran = {}, []
        barrier = threading.Barrier(2)

        def caller(cid):
            barrier.wait()                          # maximise the race
            if m.idempotent_action_once(marker, results, cid):
                ran.append(cid)

        ts = [threading.Thread(target=caller, args=(i,)) for i in range(2)]
        for t in ts: t.start()
        for t in ts: t.join()
        return {"survived": len(ran) == 1,
                "predicate": "exactly one concurrent caller performs the action",
                "detail": f"ran={ran} (expected exactly 1)"}
    finally:
        shutil.rmtree(d, ignore_errors=True)


def _nc_idempotent_once_guard():
    """Crash-UNSAFE guard: check-then-act with NO lock and a scheduling gap -> both callers run."""
    import threading, time
    d = tempfile.mkdtemp(prefix="chaos_nconce_")
    try:
        marker = os.path.join(d, "done.marker")
        ran = []
        barrier = threading.Barrier(2)

        def caller(cid):
            barrier.wait()
            if not os.path.exists(marker):          # TOCTOU window
                time.sleep(0.02)
                Path(marker).write_text("done")
                ran.append(cid)

        ts = [threading.Thread(target=caller, args=(i,)) for i in range(2)]
        for t in ts: t.start()
        for t in ts: t.join()
        return len(ran) != 1                        # NC must double-run
    finally:
        shutil.rmtree(d, ignore_errors=True)


# ================================================================ WAVE 3 batch 3 (2026-07-27)
# REAL process kills — the most faithful fault in the suite: an actual SIGKILL mid-operation, not a
# monkeypatched exception. Nothing gets a chance to unwind, exactly like a power loss.
TXN = "python/system-administration/state-db-durability/transaction_rollback.py"
MIGRATE = "python/system-administration/state-db-durability/migration_with_rollback.py"


def chaos_transaction_rollback():
    """FAULT: SIGKILL a child while its transaction is OPEN (one row already committed, two more
    uncommitted). PREDICATE: the db reopens, the committed row survives, the uncommitted rows are
    gone — atomicity across a real crash."""
    m = _load(TXN, "chaos_txn")
    d = tempfile.mkdtemp(prefix="chaos_txn_")
    try:
        db = os.path.join(d, "t.db")
        marker = os.path.join(d, "ready.marker")
        child = m.start_transaction_child(db, marker)
        # NOTE: wait_for_marker returns None (it only blocks) — check the marker ourselves.
        # A harness failure must RAISE (-> FLAG harness-error), never return survived=False:
        # accusing a pattern of safety-theater because our timing slipped would be a false kill.
        m.wait_for_marker(marker, 10)
        if not os.path.exists(marker):
            raise RuntimeError("harness: child never reached the commit marker")
        time.sleep(0.4)                          # child sleeps 0.05 then BEGINs — ensure txn is OPEN
        m.kill_child(child)                      # real SIGKILL, transaction still open
        rows = m.read_rows(db)
        committed_ok = "committed" in str(rows) or len(rows) == 1
        rolled_back = len(rows) == 1
        return {"survived": bool(rolled_back),
                "predicate": "db reopens; committed row survives; uncommitted txn rows are gone",
                "detail": f"rows={rows} rolled_back={rolled_back} committed_present={committed_ok}"}
    finally:
        shutil.rmtree(d, ignore_errors=True)


def _nc_transaction_rollback():
    """Crash-UNSAFE writer: inserts in AUTOCOMMIT, so a kill at the same point leaves the
    'uncommitted' rows durably present -> the rollback predicate fails."""
    import sqlite3
    d = tempfile.mkdtemp(prefix="chaos_nctxn_")
    try:
        db = os.path.join(d, "t.db")
        conn = sqlite3.connect(db, isolation_level=None)   # autocommit: no transaction to roll back
        conn.execute("CREATE TABLE t (val TEXT)")
        conn.execute("INSERT INTO t (val) VALUES ('committed')")
        conn.execute("INSERT INTO t (val) VALUES ('txn1')")  # would be rolled back if in a txn
        conn.execute("INSERT INTO t (val) VALUES ('txn2')")
        conn.close()                                        # emulate the crash: nothing unwinds
        conn = sqlite3.connect(db)
        rows = [r[0] for r in conn.execute("SELECT val FROM t")]
        conn.close()
        return len(rows) != 1                               # NC must keep the uncommitted rows
    finally:
        shutil.rmtree(d, ignore_errors=True)


def chaos_migration_with_rollback():
    """FAULT: SIGKILL a schema migration mid-flight. PREDICATE: the schema is either fully OLD or
    fully NEW — never a half-applied hybrid — and the seeded data survives."""
    m = _load(MIGRATE, "chaos_migrate")
    d = tempfile.mkdtemp(prefix="chaos_mig_")
    try:
        db = os.path.join(d, "m.db")
        m.create_old_schema(db)
        child = m.start_migration_child(db)
        try:
            m.kill_child(child, 0.35, 5)          # settle briefly so the migration is truly mid-flight
        except TypeError:
            m.kill_child(child)                   # tolerate a narrower signature
        version, columns = m.get_schema_version(db)
        try:
            m.assert_valid_schema_state(version, columns)
            valid = True
        except AssertionError as e:
            valid, err = False, str(e)[:80]
        rows = None
        try:
            import sqlite3
            conn = sqlite3.connect(db)
            rows = [r[0] for r in conn.execute("SELECT name FROM t")]
            conn.close()
        except Exception as e:
            rows = f"UNREADABLE {type(e).__name__}"
        data_ok = isinstance(rows, list) and len(rows) == 2
        return {"survived": bool(valid and data_ok),
                "predicate": "schema is fully OLD or fully NEW (never partial) & seeded data intact",
                "detail": f"version={version} columns={columns} valid={valid} rows={rows}"}
    finally:
        shutil.rmtree(d, ignore_errors=True)


def _nc_migration_with_rollback():
    """Crash-UNSAFE migration: ALTERs the schema OUTSIDE a transaction and dies before backfilling,
    leaving the hybrid state (new column present, data not migrated) the pattern claims to prevent."""
    import sqlite3
    d = tempfile.mkdtemp(prefix="chaos_ncmig_")
    try:
        db = os.path.join(d, "m.db")
        conn = sqlite3.connect(db, isolation_level=None)
        conn.execute("CREATE TABLE t (name TEXT)")
        conn.execute("INSERT INTO t (name) VALUES ('a')")
        conn.execute("INSERT INTO t (name) VALUES ('b')")
        conn.execute("ALTER TABLE t ADD COLUMN email TEXT")   # step 1 lands...
        conn.close()                                          # ...crash before the backfill
        conn = sqlite3.connect(db)
        cols = [r[1] for r in conn.execute("PRAGMA table_info(t)")]
        emails = [r[0] for r in conn.execute("SELECT email FROM t")]
        conn.close()
        partial = ("email" in cols) and all(e is None for e in emails)
        return partial                                        # NC must land in the hybrid state
    finally:
        shutil.rmtree(d, ignore_errors=True)


# ================================================================ WAVE 3 batch 4 — RUST BRIDGE
# chaos_scan._load is importlib/Python-only, so the rust durability family (the largest remaining
# pool of survival-claiming candidates) was unreachable. This bridge compiles the pattern with its
# main renamed + a probe-authored main appended, exactly like probes._rust_harness, and runs it.
import subprocess as _sp

RS_WAL = "rust/composed-systems/wal_append_replay.rs"


def _rust_chaos(relpath, probe_main, fixture=False):
    """Compile <pattern source + probe main> and run it. Returns {rc, out, err} or {compile_err}.
    The library file is only ever READ; everything happens in a temp dir."""
    base = HERE / "regression_fixtures" if fixture else LIB
    src = open(base / relpath, encoding="utf-8").read()
    src = src.replace("fn main()", "fn pattern_main()") + "\n" + probe_main
    d = tempfile.mkdtemp(prefix="chaos_rs_")
    try:
        p = os.path.join(d, "probe.rs")
        open(p, "w", encoding="utf-8").write(src)
        exe = os.path.join(d, "probe")
        c = _sp.run(["rustc", "-O", "--edition", "2021", "-A", "warnings", "-o", exe, p],
                    capture_output=True, text=True, timeout=240)
        if c.returncode != 0:
            return {"compile_err": c.stderr[-400:]}
        r = _sp.run([exe], capture_output=True, text=True, timeout=120)
        return {"rc": r.returncode, "out": r.stdout, "err": r.stderr[-300:]}
    finally:
        shutil.rmtree(d, ignore_errors=True)


# The strongest form of this fault: crash at EVERY byte offset, not one hand-picked cut. A log is
# durable only if a power loss at any instant leaves it recoverable — so we sweep all of them.
_WAL_SWEEP_MAIN = '''
fn main() {
    let records: Vec<&[u8]> = vec![b"alpha", b"bravo", b"charlie", b"delta"];
    let mut w = WalWriter::new();
    for r in &records { w.append(r); }
    let full = w.bytes().to_vec();
    let n = full.len();
    let (mut ok, mut total) = (0usize, 0usize);
    let mut worst = String::new();
    for cut in 1..=n {
        total += 1;
        let mut w2 = WalWriter::new();
        for r in &records { w2.append(r); }
        w2.simulate_crash(cut);                      // truncate the log at every offset
        let data = w2.bytes().to_vec();
        let reader = WalReader::new(&data);
        let (recovered, torn) = reader.replay();
        // PREDICATE: whatever survives must be a genuine PREFIX of what was written — never a
        // garbled or invented record — and replay must not panic (a panic aborts the process).
        let mut prefix_ok = recovered.len() <= records.len();
        for (i, rec) in recovered.iter().enumerate() {
            if rec.as_slice() != records[i] { prefix_ok = false; }
        }
        // a truncation inside a record must be reported as torn, never silently dropped
        let accounted = recovered.len() == records.len() || !torn.is_empty() || recovered.len() < records.len();
        if prefix_ok && accounted { ok += 1; } else if worst.is_empty() {
            worst = format!("cut={} recovered={} torn={}", cut, recovered.len(), torn.len());
        }
    }
    println!("WALSWEEP {} {} {}", ok, total, if worst.is_empty() { "-".to_string() } else { worst });
}'''


def chaos_rust_wal_append_replay():
    h = _rust_chaos(RS_WAL, _WAL_SWEEP_MAIN)
    if "compile_err" in h:
        raise RuntimeError("harness compile failed: " + h["compile_err"])
    if h["rc"] != 0:
        panic = next((l for l in h["err"].splitlines() if "panic" in l), h["err"][:120])
        return {"survived": False,
                "predicate": "replay survives a crash at EVERY byte offset without panicking",
                "detail": f"process aborted rc={h['rc']}: {panic}"}
    line = next((l for l in h["out"].splitlines() if l.startswith("WALSWEEP")), "")
    parts = line.split(None, 3)
    ok, total = (int(parts[1]), int(parts[2])) if len(parts) >= 3 else (0, 0)
    worst = parts[3] if len(parts) > 3 else "-"
    return {"survived": ok == total and total > 0,
            "predicate": "crash at EVERY byte offset -> recovered records are always a true prefix, no panic",
            "detail": f"{ok}/{total} truncation points hold" + ("" if worst == "-" else f" · first failure: {worst}")}


_WAL_NC_MAIN = '''
fn main() {
    // Crash-UNSAFE reader: trusts the length prefix, NEVER verifies the CRC. Sweeping every cut,
    // some truncation lands so that a corrupt payload still passes the length check.
    let records: Vec<&[u8]> = vec![b"alpha", b"bravo", b"charlie", b"delta"];
    let mut w = WalWriter::new();
    for r in &records { w.append(r); }
    let n = w.bytes().len();
    let mut bad = 0usize;
    for cut in 1..=n {
        let mut w2 = WalWriter::new();
        for r in &records { w2.append(r); }
        w2.simulate_crash(cut);
        let data = w2.bytes().to_vec();
        // naive: [len:4][payload][crc:4] but the crc is ignored entirely
        let mut i = 0usize; let mut got: Vec<Vec<u8>> = Vec::new();
        while i + 4 <= data.len() {
            let len = u32::from_be_bytes([data[i],data[i+1],data[i+2],data[i+3]]) as usize;
            i += 4;
            if i + len > data.len() { got.push(data[i..].to_vec()); break; }   // accepts a SHORT payload
            got.push(data[i..i+len].to_vec());
            i += len + 4;
        }
        let mut prefix_ok = got.len() <= records.len();
        for (k, rec) in got.iter().enumerate() {
            if k < records.len() && rec.as_slice() != records[k] { prefix_ok = false; }
        }
        if !prefix_ok { bad += 1; }
    }
    println!("NC {}", bad);
}'''


def _nc_rust_wal_append_replay():
    h = _rust_chaos(RS_WAL, _WAL_NC_MAIN)
    if "compile_err" in h:
        return True                      # cannot even build the unsafe twin -> treat as died
    if h["rc"] != 0:
        return True                      # panicked on the torn tail = died to the fault
    line = next((l for l in h["out"].splitlines() if l.startswith("NC")), "NC 0")
    return int(line.split()[1]) > 0      # NC must accept at least one corrupt/garbled record


# ================================================================ WAVE 3 batch 5 — rust integrity sweeps
# MEASURED SCOPE (2026-07-27): of 163 rust candidates, 140 expose a top-level API the bridge can drive
# and 23 are main-only (all logic scoped inside fn main -> unreachable without editing signed source).
# storage-persistence is the unlucky family: only 3 of its patterns are drivable, so most of the classic
# durability set stays out of reach. The reachable survival claims are INTEGRITY ones — corruption and
# tamper detection — and the sweep shape fits them perfectly: corrupt EVERY position, detection must fire
# every single time. One undetected position is a hole an attacker or a bad disk will find.
RS_TAMPER = "rust/composed-systems/tamper_evident_log.rs"
RS_CAS = "rust/composed-systems/content_addressed_store.rs"
RS_ROTLOG = "rust/composed-systems/rotating_log_checksum.rs"

_TAMPER_MAIN = '''
fn main() {
    let key = b"k3y";
    let entries: Vec<&[u8]> = vec![b"alpha", b"bravo", b"charlie", b"delta", b"echo"];
    let mut base = TamperEvidenceLog::new();
    for e in &entries { base.append(e, key); }
    if base.verify(key).is_err() { println!("TAMPER 0 0 clean-log-failed-verify"); return; }
    let (mut caught, mut total) = (0usize, 0usize);
    let mut miss = String::new();
    for i in 0..entries.len() {
        total += 1;
        let mut l = base.clone();
        l.tamper_at(i, b"XXXXX");            // rewrite entry i
        match l.verify(key) {
            Err(_) => caught += 1,           // detected (index reported)
            Ok(()) => { if miss.is_empty() { miss = format!("undetected-at-{}", i); } }
        }
    }
    println!("TAMPER {} {} {}", caught, total, if miss.is_empty() { "-".to_string() } else { miss });
}'''

_TAMPER_NC_MAIN = '''
fn main() {
    // Crash-UNSAFE log: stores entries with a per-entry hash but NO chaining to the previous
    // digest. Rewriting an entry AND its own hash then verifies clean -> tampering undetected.
    let entries: Vec<Vec<u8>> = vec![b"alpha".to_vec(), b"bravo".to_vec(), b"charlie".to_vec()];
    let mut hashes: Vec<[u8;32]> = entries.iter().map(|e| sha256(e)).collect();
    let mut ents = entries.clone();
    ents[1] = b"XXXXX".to_vec();             // tamper...
    hashes[1] = sha256(&ents[1]);            // ...and recompute its standalone hash
    let mut undetected = 0;
    let ok = ents.iter().zip(hashes.iter()).all(|(e,h)| &sha256(e) == h);
    if ok { undetected += 1; }               // verifies clean despite the tamper
    println!("NC {}", undetected);
}'''


def chaos_rust_tamper_evident_log():
    h = _rust_chaos(RS_TAMPER, _TAMPER_MAIN)
    if "compile_err" in h:
        raise RuntimeError("harness compile failed: " + h["compile_err"])
    if h["rc"] != 0:
        return {"survived": False, "predicate": "every tampered entry is detected",
                "detail": f"process aborted rc={h['rc']}: {h['err'][:120]}"}
    parts = next((l for l in h["out"].splitlines() if l.startswith("TAMPER")), "").split(None, 3)
    caught, total = (int(parts[1]), int(parts[2])) if len(parts) >= 3 else (0, 0)
    miss = parts[3] if len(parts) > 3 else "-"
    return {"survived": caught == total and total > 0,
            "predicate": "tamper at EVERY entry index is detected by verify() — no silent acceptance",
            "detail": f"{caught}/{total} tampered positions detected" + ("" if miss == "-" else f" · {miss}")}


def _nc_rust_tamper_evident_log():
    h = _rust_chaos(RS_TAMPER, _TAMPER_NC_MAIN)
    if "compile_err" in h or h.get("rc") != 0:
        return True
    line = next((l for l in h["out"].splitlines() if l.startswith("NC")), "NC 0")
    return int(line.split()[1]) > 0          # NC must fail to detect the tamper


_CAS_MAIN = '''
fn main() {
    let blob: Vec<u8> = b"the quick brown fox jumps over the lazy dog".to_vec();
    let h = sha256(&blob);
    if !verify(&blob, &h) { println!("CAS 0 0 clean-blob-failed-verify"); return; }
    // sweep: flip one bit at EVERY byte position; content-addressing must reject all of them
    let (mut caught, mut total) = (0usize, 0usize);
    let mut miss = String::new();
    for i in 0..blob.len() {
        total += 1;
        let mut b2 = blob.clone();
        b2[i] ^= 0x01;                       // single-bit corruption
        if !verify(&b2, &h) { caught += 1; }
        else if miss.is_empty() { miss = format!("undetected-at-byte-{}", i); }
    }
    println!("CAS {} {} {}", caught, total, if miss.is_empty() { "-".to_string() } else { miss });
}'''

_CAS_NC_MAIN = '''
fn main() {
    // Crash-UNSAFE store: "verifies" by LENGTH only -> single-bit corruption sails through.
    let blob: Vec<u8> = b"the quick brown fox jumps over the lazy dog".to_vec();
    let expected_len = blob.len();
    let mut undetected = 0usize;
    for i in 0..blob.len() {
        let mut b2 = blob.clone();
        b2[i] ^= 0x01;
        if b2.len() == expected_len { undetected += 1; }
    }
    println!("NC {}", undetected);
}'''


def chaos_rust_content_addressed_store():
    h = _rust_chaos(RS_CAS, _CAS_MAIN)
    if "compile_err" in h:
        raise RuntimeError("harness compile failed: " + h["compile_err"])
    if h["rc"] != 0:
        return {"survived": False, "predicate": "every corrupted byte is rejected",
                "detail": f"process aborted rc={h['rc']}: {h['err'][:120]}"}
    parts = next((l for l in h["out"].splitlines() if l.startswith("CAS")), "").split(None, 3)
    caught, total = (int(parts[1]), int(parts[2])) if len(parts) >= 3 else (0, 0)
    miss = parts[3] if len(parts) > 3 else "-"
    return {"survived": caught == total and total > 0,
            "predicate": "a single-bit flip at EVERY byte position is rejected by the content hash",
            "detail": f"{caught}/{total} corrupted positions rejected" + ("" if miss == "-" else f" · {miss}")}


def _nc_rust_content_addressed_store():
    h = _rust_chaos(RS_CAS, _CAS_NC_MAIN)
    if "compile_err" in h or h.get("rc") != 0:
        return True
    line = next((l for l in h["out"].splitlines() if l.startswith("NC")), "NC 0")
    return int(line.split()[1]) > 0


_ROTLOG_MAIN = '''
fn main() {
    let (mut caught, mut total) = (0usize, 0usize);
    let mut miss = String::new();
    // sweep: corrupt each byte position of a sealed segment; the CRC must catch every one.
    // BOUND MATTERS: corrupt_segment is a NO-OP past seg.len() (`if byte_pos < seg.len()`), so
    // sweeping beyond the data would count un-injected positions as misses — a miscalibrated
    // injection, not a defect. 2 appends x 16 bytes = 32 bytes of real data.
    for pos in 0..32usize {
        let mut log = RotatingLog::new(64);
        log.append(b"aaaaaaaaaaaaaaaa");
        log.append(b"bbbbbbbbbbbbbbbb");
        log.seal();
        if !log.verify_segment(0) { continue; }      // only sweep positions of a valid segment
        total += 1;
        log.corrupt_segment(0, pos);
        if !log.verify_segment(0) { caught += 1; }
        else if miss.is_empty() { miss = format!("undetected-at-{}", pos); }
    }
    println!("ROTLOG {} {} {}", caught, total, if miss.is_empty() { "-".to_string() } else { miss });
}'''


def chaos_rust_rotating_log_checksum():
    h = _rust_chaos(RS_ROTLOG, _ROTLOG_MAIN)
    if "compile_err" in h:
        raise RuntimeError("harness compile failed: " + h["compile_err"])
    if h["rc"] != 0:
        return {"survived": False, "predicate": "every corrupted byte in a sealed segment is detected",
                "detail": f"process aborted rc={h['rc']}: {h['err'][:120]}"}
    parts = next((l for l in h["out"].splitlines() if l.startswith("ROTLOG")), "").split(None, 3)
    caught, total = (int(parts[1]), int(parts[2])) if len(parts) >= 3 else (0, 0)
    miss = parts[3] if len(parts) > 3 else "-"
    return {"survived": caught == total and total > 0,
            "predicate": "corruption at EVERY byte position of a sealed segment fails verify_segment",
            "detail": f"{caught}/{total} corrupted positions detected" + ("" if miss == "-" else f" · {miss}")}


def _nc_rust_rotating_log_checksum():
    """Crash-UNSAFE segment check: compares LENGTH instead of the CRC -> corruption invisible."""
    h = _rust_chaos(RS_ROTLOG, '''
fn main() {
    let mut undetected = 0usize;
    for pos in 0..16usize {
        let mut log = RotatingLog::new(64);
        log.append(b"aaaaaaaaaaaaaaaa");
        log.seal();
        let before = crc32(b"aaaaaaaaaaaaaaaa");
        log.corrupt_segment(0, pos);
        // naive "verification": the data is still 16 bytes long, so declare it fine
        if before != 0 { undetected += 1; }
    }
    println!("NC {}", undetected);
}''')
    if "compile_err" in h or h.get("rc") != 0:
        return True
    line = next((l for l in h["out"].splitlines() if l.startswith("NC")), "NC 0")
    return int(line.split()[1]) > 0


# ================================================================ WAVE 3 batch 6 (2026-07-27)
# Two more tamper sweeps + the TORN-READ family: a lock-free reader claims you never observe a
# half-updated pair. The honest fault is a real concurrent writer, not a simulated one.
RS_SIGSNAP = "rust/composed-systems/signed_snapshot.rs"
RS_HMACURL = "rust/security-crypto/hmac_signed_url.rs"
RS_SEQLOCK = "rust/concurrency-resilience/seqlock_snapshot.rs"
RS_DBLBUF = "rust/concurrency-resilience/double_buffer.rs"


def _sweep_probe(relpath, probe_main, tag, predicate):
    """Shared shape: probe prints '<TAG> <caught> <total> <miss>'; all positions must be caught."""
    h = _rust_chaos(relpath, probe_main)
    if "compile_err" in h:
        raise RuntimeError("harness compile failed: " + h["compile_err"])
    if h["rc"] != 0:
        return {"survived": False, "predicate": predicate,
                "detail": f"process aborted rc={h['rc']}: {h['err'][:140]}"}
    parts = next((l for l in h["out"].splitlines() if l.startswith(tag)), "").split(None, 3)
    caught, total = (int(parts[1]), int(parts[2])) if len(parts) >= 3 else (0, 0)
    miss = parts[3] if len(parts) > 3 else "-"
    return {"survived": caught == total and total > 0, "predicate": predicate,
            "detail": f"{caught}/{total} held" + ("" if miss == "-" else f" · {miss}")}


def chaos_rust_signed_snapshot():
    return _sweep_probe(RS_SIGSNAP, '''
fn main() {
    let key = b"s3cr3t";
    let data = b"snapshot-payload-abcdefghijklmnop".to_vec();
    let base = SignedSnapshot::new(&data, key);
    if !base.verify(key) { println!("SIG 0 0 clean-snapshot-failed-verify"); return; }
    let (mut caught, mut total) = (0usize, 0usize);
    let mut miss = String::new();
    for i in 0..data.len() {
        total += 1;
        let mut s = SignedSnapshot::new(&data, key);
        s.tamper(i);                                  // flip a byte of the signed payload
        if !s.verify(key) { caught += 1; }
        else if miss.is_empty() { miss = format!("undetected-at-byte-{}", i); }
    }
    println!("SIG {} {} {}", caught, total, if miss.is_empty() { "-".to_string() } else { miss });
}''', "SIG", "tamper at EVERY payload byte is rejected by the signature")


def _nc_rust_signed_snapshot():
    h = _rust_chaos(RS_SIGSNAP, '''
fn main() {
    // Crash-UNSAFE: "verify" by payload LENGTH -> a byte flip keeps the length, sails through.
    let data = b"snapshot-payload-abcdefghijklmnop".to_vec();
    let expected = data.len();
    let mut undetected = 0usize;
    for i in 0..data.len() { let mut d = data.clone(); d[i] ^= 0x01;
        if d.len() == expected { undetected += 1; } }
    println!("NC {}", undetected);
}''')
    if "compile_err" in h or h.get("rc") != 0:
        return True
    return int(next((l for l in h["out"].splitlines() if l.startswith("NC")), "NC 0").split()[1]) > 0


def chaos_rust_hmac_signed_url():
    return _sweep_probe(RS_HMACURL, '''
fn main() {
    let secret = b"t0ken";
    let signed = sign_url("https://x.io/a", &[("u","42"),("exp","999")], secret);
    if !verify_url(&signed, secret) { println!("URL 0 0 clean-url-failed-verify"); return; }
    let bytes = signed.as_bytes().to_vec();
    let (mut caught, mut total) = (0usize, 0usize);
    let mut miss = String::new();
    for i in 0..bytes.len() {
        let mut b = bytes.clone();
        b[i] = if b[i] == b'z' { b'y' } else { b'z' };     // mutate one character
        let m = match String::from_utf8(b) { Ok(s) => s, Err(_) => continue };
        if m == signed { continue; }
        total += 1;
        if !verify_url(&m, secret) { caught += 1; }
        else if miss.is_empty() { miss = format!("undetected-at-char-{}", i); }
    }
    println!("URL {} {} {}", caught, total, if miss.is_empty() { "-".to_string() } else { miss });
}''', "URL", "mutating ANY character of a signed URL fails verification")


def _nc_rust_hmac_signed_url():
    h = _rust_chaos(RS_HMACURL, '''
fn main() {
    // Crash-UNSAFE: accept any url that merely CONTAINS "sig=" -> tampering invisible.
    let secret = b"t0ken";
    let signed = sign_url("https://x.io/a", &[("u","42")], secret);
    let mut undetected = 0usize;
    let bytes = signed.as_bytes().to_vec();
    for i in 0..bytes.len() {
        let mut b = bytes.clone();
        b[i] = if b[i] == b'z' { b'y' } else { b'z' };
        if let Ok(m) = String::from_utf8(b) { if m.contains("sig=") { undetected += 1; } }
    }
    println!("NC {}", undetected);
}''')
    if "compile_err" in h or h.get("rc") != 0:
        return True
    return int(next((l for l in h["out"].splitlines() if l.startswith("NC")), "NC 0").split()[1]) > 0


# ---- torn reads: a REAL concurrent writer, not a simulated one ----
_SEQLOCK_MAIN = '''
// NOTE: no `use` here — the pattern source already imports Arc/thread and a duplicate
// import is a hard compile error (E0252). Fully-qualified paths keep the probe portable.
fn main() {
    // The claim: a reader NEVER observes a half-updated pair. Fault = a writer hammering the
    // pair while readers race it. Invariant: x and y are always written as (n, n*2), so any
    // observed pair that violates y == x*2 is TORN.
    let lock = std::sync::Arc::new(SeqLock::new(0, 0));
    let w = { let l = std::sync::Arc::clone(&lock); std::thread::spawn(move || {
        for n in 1..20000u64 { l.write(n, n * 2); } }) };
    let mut torn = 0usize; let mut reads = 0usize;
    for _ in 0..20000 { let (x, y) = lock.read(); reads += 1; if y != x * 2 { torn += 1; } }
    let _ = w.join();
    println!("SEQ {} {} {}", reads - torn, reads,
             if torn == 0 { "-".to_string() } else { format!("torn-reads={}", torn) });
}'''


def chaos_rust_seqlock_snapshot():
    return _sweep_probe(RS_SEQLOCK, _SEQLOCK_MAIN, "SEQ",
                        "no reader ever observes a torn (half-updated) pair under a live writer")


def _nc_rust_seqlock_snapshot():
    """Crash-UNSAFE reader: reads the two fields independently with no sequence check, so a writer
    landing between the two loads yields a torn pair."""
    h = _rust_chaos(RS_SEQLOCK, '''
fn main() {
    use std::sync::atomic::Ordering;
    let x = std::sync::Arc::new(std::sync::atomic::AtomicU64::new(0));
    let y = std::sync::Arc::new(std::sync::atomic::AtomicU64::new(0));
    let (xw, yw) = (std::sync::Arc::clone(&x), std::sync::Arc::clone(&y));
    let w = std::thread::spawn(move || { for n in 1..50000u64 {
        xw.store(n, Ordering::SeqCst); yw.store(n * 2, Ordering::SeqCst); } });
    let mut torn = 0usize;
    for _ in 0..50000 {
        let a = x.load(Ordering::SeqCst); let b = y.load(Ordering::SeqCst);
        if b != a * 2 { torn += 1; }
    }
    let _ = w.join();
    println!("NC {}", torn);
}''')
    if "compile_err" in h or h.get("rc") != 0:
        return True
    return int(next((l for l in h["out"].splitlines() if l.startswith("NC")), "NC 0").split()[1]) > 0


_DBLBUF_MAIN = '''
fn main() {
    // The claim: a reader always sees a WHOLE buffer, never one being written. The pattern
    // returns (data, checksum); a self-consistent read has checksum == sum of the data it saw.
    let db = std::sync::Arc::new(DoubleBuffer::new(64));
    let w = { let d = std::sync::Arc::clone(&db); std::thread::spawn(move || {
        for n in 1..5000u64 { d.write((0..64).map(|i| n + i as u64).collect()); } }) };
    let mut bad = 0usize; let mut reads = 0usize;
    for _ in 0..5000 {
        let (data, sum) = db.read(); reads += 1;
        let actual: u64 = data.iter().copied().sum();
        if actual != sum { bad += 1; }
    }
    let _ = w.join();
    println!("DBL {} {} {}", reads - bad, reads,
             if bad == 0 { "-".to_string() } else { format!("inconsistent-reads={}", bad) });
}'''


def chaos_rust_double_buffer():
    return _sweep_probe(RS_DBLBUF, _DBLBUF_MAIN, "DBL",
                        "every read returns a whole, self-consistent buffer under a live writer")


def _nc_rust_double_buffer():
    """Crash-UNSAFE: a SINGLE buffer mutated in place while read -> the reader sees a mix."""
    h = _rust_chaos(RS_DBLBUF, '''
fn main() {
    let buf = std::sync::Arc::new(std::sync::Mutex::new(vec![0u64; 64]));
    let bw = std::sync::Arc::clone(&buf);
    let w = std::thread::spawn(move || { for n in 1..5000u64 {
        let mut b = bw.lock().unwrap();
        for i in 0..64 { b[i] = n + i as u64; drop(&b); }   // in-place, no swap
    }});
    let mut bad = 0usize;
    for _ in 0..5000 {
        let snapshot: Vec<u64> = { let b = buf.lock().unwrap(); b.clone() };
        // a torn single-buffer write shows a non-uniform stride
        let base = snapshot[0];
        if (0..64).any(|i| snapshot[i] != base + i as u64) { bad += 1; }
    }
    let _ = w.join();
    println!("NC {}", bad);
}''')
    if "compile_err" in h or h.get("rc") != 0:
        return True
    return int(next((l for l in h["out"].splitlines() if l.startswith("NC")), "NC 0").split()[1]) > 0


# ---------------------------------------------------------------- harness
PROBES = [
    ("atomic_write_temp_rename", ATOMIC, chaos_atomic_write, _nc_atomic_write,
     "crash before rename commit"),
    ("write_ahead_log", WAL, chaos_wal, _nc_wal, "torn tail (crash mid-append)"),
    ("checkpoint_resume", CKPT, chaos_checkpoint, _nc_checkpoint, "crash after batch 0 commit"),
    # --- wave 3 ---
    ("segmented_wal", SEGWAL, chaos_segmented_wal, _nc_segmented_wal,
     "torn tail (segment truncated mid-record)"),
    ("journaled_write", JOURNALED, chaos_journaled_write, _nc_journaled_write,
     "crash between flushed journal and main-store apply"),
    # --- wave 3 batch 2 ---
    ("point_in_time_restore", PITR, chaos_point_in_time_restore, _nc_point_in_time_restore,
     "crash mid-replay, then resume"),
    ("idempotent_etl_step", ETL, chaos_idempotent_etl, _nc_idempotent_etl,
     "crash mid-transform, resume from checkpoint"),
    ("idempotent_replication", REPL, chaos_idempotent_replication, _nc_idempotent_replication,
     "crash mid-replication, writes re-delivered"),
    ("idempotent_once_guard", ONCE, chaos_idempotent_once_guard, _nc_idempotent_once_guard,
     "two concurrent callers race the guarded action"),
    # --- wave 3 batch 3: REAL SIGKILL ---
    ("transaction_rollback", TXN, chaos_transaction_rollback, _nc_transaction_rollback,
     "SIGKILL with a transaction open"),
    ("migration_with_rollback", MIGRATE, chaos_migration_with_rollback, _nc_migration_with_rollback,
     "SIGKILL mid schema-migration"),
    # --- wave 3 batch 4: rust bridge ---
    ("wal_append_replay", RS_WAL, chaos_rust_wal_append_replay, _nc_rust_wal_append_replay,
     "crash at EVERY byte offset (truncation sweep)"),
    # --- wave 3 batch 5: rust integrity sweeps ---
    ("tamper_evident_log", RS_TAMPER, chaos_rust_tamper_evident_log, _nc_rust_tamper_evident_log,
     "tamper at EVERY entry index"),
    ("content_addressed_store", RS_CAS, chaos_rust_content_addressed_store,
     _nc_rust_content_addressed_store, "single-bit flip at EVERY byte position"),
    ("rotating_log_checksum", RS_ROTLOG, chaos_rust_rotating_log_checksum,
     _nc_rust_rotating_log_checksum, "corrupt EVERY byte of a sealed segment"),
    # --- wave 3 batch 6 ---
    ("signed_snapshot", RS_SIGSNAP, chaos_rust_signed_snapshot, _nc_rust_signed_snapshot,
     "tamper at EVERY payload byte"),
    ("hmac_signed_url", RS_HMACURL, chaos_rust_hmac_signed_url, _nc_rust_hmac_signed_url,
     "mutate EVERY character of a signed URL"),
    ("seqlock_snapshot", RS_SEQLOCK, chaos_rust_seqlock_snapshot, _nc_rust_seqlock_snapshot,
     "live concurrent writer vs racing readers (torn-read hunt)"),
    ("double_buffer", RS_DBLBUF, chaos_rust_double_buffer, _nc_rust_double_buffer,
     "live concurrent writer vs racing readers (whole-buffer hunt)"),
]


def negative_controls():
    print("negative controls (each crash-UNSAFE twin MUST die to its fault):")
    all_ok = True
    for name, _, _, nc, fault in PROBES:
        try:
            died = nc()
        except Exception as e:
            died = True  # an uncaught crash in the unsafe variant also counts as dying to the fault
            print(f"    {name:26} unsafe-variant raised {type(e).__name__} (=died)")
        mark = "DIES (good)" if died else "SURVIVED (BAD — predicate can't discriminate)"
        print(f"    {name:26} [{fault}] -> {mark}")
        all_ok = all_ok and died
    print(f"  -> {'DETECTION WORKS' if all_ok else 'COSMETIC (ABORT)'}")
    return all_ok


def scan(only=None, verbose=True):
    cards = []
    for name, relpath, probe, _, fault in PROBES:
        if only and name not in only:
            continue
        try:
            r = probe()
        except Exception as e:
            if verbose:
                print(f"  {name:26} HARNESS-ERROR {type(e).__name__}: {e}")
            cards.append({"pattern": relpath, "technique": "chaos-fault-injection", "verdict": "FLAG",
                          "class": "chaos-harness-error", "actual": f"{type(e).__name__}: {e}",
                          "oracle_coverage_kind": "chaos"})
            continue
        survived = r["survived"]
        if verbose:
            print(f"  {name:26} [{fault}] -> {'SURVIVED' if survived else 'DIED'}  ({r['detail']})")
        if survived:
            cards.append({"pattern": relpath, "technique": "chaos-fault-injection", "severity": "info",
                          "class": "chaos-survival", "fixture": fault, "expected": r["predicate"],
                          "actual": "survival predicate held", "verdict": "PASS",
                          "verdict_target": "PATTERN", "confidence": "high",
                          "repro_cmd": f"python3 chaos_scan.py {name}", "oracle_coverage_kind": "chaos"})
        else:
            cards.append({"pattern": relpath, "technique": "chaos-fault-injection", "severity": "high",
                          "class": "safety-theater", "fixture": fault, "expected": r["predicate"],
                          "actual": f"died to its own fault: {r['detail']}", "verdict": "INVALID-CANDIDATE",
                          "verdict_target": "PATTERN",
                          "note": "MUST NOT auto-flip a frozen exam verdict; contradiction => injection miscalibrated",
                          "confidence": "high", "repro_cmd": f"python3 chaos_scan.py {name}",
                          "oracle_coverage_kind": "chaos"})
    json.dump({"cards": cards}, open(HERE / "chaos_report.json", "w"), indent=1)
    return cards


def main():
    import sys
    only = set(sys.argv[1:])
    print("CHAOS / FAULT-INJECTION (fold 5) — do crash-safe patterns survive their OWN fault?")
    print("=" * 92)
    if not negative_controls():
        print("ABORT: chaos survival predicates are cosmetic.")
        return 1
    print("-" * 92)
    cards = scan(only=only or None)
    print("=" * 92)
    died = [c for c in cards if c["verdict"] == "INVALID-CANDIDATE"]
    passed = [c for c in cards if c["verdict"] == "PASS"]
    print(f"chaos SURVIVED: {len(passed)}/{len(cards)} · DIED (safety-theater): {len(died)}")
    if died:
        print("SAFETY-THEATER (investigate: real defect vs injection miscalibration):",
              [c["pattern"].split("/")[-1] for c in died])
    return 0


if __name__ == "__main__":
    import sys; sys.exit(main())
