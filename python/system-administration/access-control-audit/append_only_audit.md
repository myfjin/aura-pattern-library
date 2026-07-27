# append only audit

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 18 · Access control & audit

**Signature:** `(event: str) → ?`

## What it does

append_only_audit: maintain an append-only audit log with hash chaining.
Each entry hash includes the previous entry's hash (forming a chain).
Tampering with an old entry breaks all subsequent hashes.
Flip a byte in a past entry and verify the chain verification catches the break.

## Guarantee

When it runs, append only audit guarantees audit.verify_chain(); 'hash mismatch' in str(e) or 'chain broken' in str(e) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `audit.verify_chain()`
- `'hash mismatch' in str(e) or 'chain broken' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def sha256(data):`, `class AppendOnlyAudit:`, `def __init__(self, log_path):`, `def append(self, event):`, `def _write(self):`, `def verify_chain(self):`
**Valid input:** `event` is any JSON-serializable value; `log_path` is writable.
**Core:** Append-only audit log where each entry stores the SHA-256 hash of `{event, prev_hash}` and links to the previous entry's hash. `verify_chain` recomputes every hash from the genesis `0...0` and raises `ValueError` on any mismatch.
**Assert:** A three-event chain verifies cleanly; after flipping a byte in the first event on disk and reloading, `verify_chain` raises with "hash mismatch" or "chain broken".
**⚠️ Defect:** `append` rewrites the entire log to disk after every event, so write amplification is O(n²) for n entries. Reloading is left to the caller (the demo manually populates `entries` from disk); there is no `load` method, so the class is not self-contained.

---
*△ AURA Pattern Library — © Reality Optimizer*
