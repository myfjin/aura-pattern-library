# reader writer lock

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 3 · Concurrency & Locking

**Signature:** `(lock: ReaderWriterLock, res: dict, rid: int, state: dict) → ?`

## What it does

reader_writer_lock: many concurrent readers, but a writer needs exclusive access.
Failure simulated: (1) 3 readers run at once — they must NOT serialize behind each other;
(2) readers hold while a writer starts — the writer must WAIT, and must never overlap a reader.
Recovery asserted (both catch a no-op lock):
 - PARALLELISM: the 3-reader phase finishes in ~one hold, not three (wall-clock < 2*hold, and no
   single reader waited for another). A lock that serialized readers → phase ~3*hold → fails.
 - EXCLUSIVITY: reader/writer race-detection flags any overlap; the writer genuinely BLOCKS behind
   the readers (its wait > 0). A no-op lock lets writer+reader overlap → race_detected → fails.

## Guarantee

When it runs, reader writer lock guarantees res.get(f'reader_{i}_ok'); not res.get(f'reader_{i}_race'); phase_wall < 2 * HOLD (weak-grade: directional, proven by run).

**Checkable constraints:**

- `res.get(f'reader_{i}_ok')`
- `not res.get(f'reader_{i}_race')`
- `phase_wall < 2 * HOLD`
- `max((res[f'reader_{i}_wait'] for i in range(3))) < 0.5 * HOLD`
- `res.get(f'reader_{10 + i}_ok')`
- `res.get('writer_0_ok')`
- `not res.get('writer_0_race')`
- `res['writer_0_wait'] > 0.05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class ReaderWriterLock:`, `def __init__(self):`, `def acquire_read(self):`, `def release_read(self):`, `def acquire_write(self):`, `def release_write(self):`, `def reader(lock, res, rid, state):`, `def writer(lock, res, wid, state):`
**Valid input:** The lock is shared among threads; readers and writers use the corresponding acquire/release pairs.
**Core:** Condition-variable-based reader-writer lock. Multiple readers can hold simultaneously; writers wait for all readers to exit and then hold exclusively.
**Assert:** Three concurrent readers finish in roughly one hold time (not three); a writer blocked behind two readers waits > 0.05 s and never overlaps an active reader.
**⚠️ Defect:** The lock is writer-preferring only via `writer_waiting`, but new readers can still slip in before a waiting writer in some wakeups. There is no ownership tracking, so `release_read`/`release_write` can be called by the wrong thread and silently corrupt the counters.

---
*△ AURA Pattern Library — © Reality Optimizer*
