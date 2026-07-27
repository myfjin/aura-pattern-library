# session record

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 18 · Access control & audit

**Signature:** `(event_type: str, details: dict) → ?`

## What it does

session_record: record a user session (login, commands, logout). Verify the record
is accurate and tamper-proof. Modify a logged command and verify tampering is detected.

## Guarantee

When it runs, session record guarantees recorder.verify_integrity(); events[0]['type'] == 'login'; events[-1]['type'] == 'logout' (weak-grade: directional, proven by run).

**Checkable constraints:**

- `recorder.verify_integrity()`
- `len(events) == 4`
- `events[0]['type'] == 'login'`
- `events[-1]['type'] == 'logout'`
- `'tampering' in str(e) and 'hash mismatch' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def sha256(data):`, `class SessionRecorder:`, `def __init__(self, session_file):`, `def record_event(self, event_type, details):`, `def seal(self):`, `def _write(self):`, `def verify_integrity(self):`, `def list_events(self):`
**Valid input:** `event_type` and `details` are JSON-serializable; `session_file` is writable.
**Core:** Session recorder with hash integrity. Records login/command/logout events, seals by hashing the sorted JSON of all events, and detects on-disk tampering by recomputing the hash.
**Assert:** Four recorded events list correctly and verify after sealing; modifying a command to `rm -rf /` on disk triggers "tampering" / "hash mismatch" on reload.
**⚠️ Defect:** Timestamps are simulated by event index (`len(self.events)`), not real time, so event ordering is just insertion order. Like the other audit classes, there is no `load` method; callers must manually populate fields from the JSON record before calling `verify_integrity`.

---
*△ AURA Pattern Library — © Reality Optimizer*
