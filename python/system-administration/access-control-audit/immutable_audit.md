# immutable audit

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 18 · Access control & audit

**Signature:** `(event: dict) → ?`

## What it does

immutable_audit: create an immutable audit log by sealing it with a cryptographic signature
once written. After sealing, any tampering is detectable. Tamper with a sealed log and
verify the signature breaks.

## Guarantee

When it runs, immutable audit guarantees audit.verify_seal(); 'tampering' in str(e).lower() and 'seal' in str(e).lower(); 'tampering' in str(e).lower() (weak-grade: directional, proven by run).

**Checkable constraints:**

- `audit.verify_seal()`
- `'tampering' in str(e).lower() and 'seal' in str(e).lower()`
- `'tampering' in str(e).lower()`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def sha256(data):`, `class ImmutableAudit:`, `def __init__(self, log_path, secret_key):`, `def append(self, event):`, `def seal(self):`, `def _write(self):`, `def verify_seal(self):`
**Valid input:** `event` is any JSON-serializable object; `secret_key` is a string or bytes; sealing happens before verification.
**Core:** HMAC-SHA-256 sealed audit log. `seal` signs the sorted JSON serialization of all entries; `verify_seal` reloads the file and recomputes the HMAC, raising `ValueError` if tampering is detected.
**Assert:** Sealed log verifies; after changing an entry on disk, `verify_seal` raises with "tampering detected".
**⚠️ Defect:** Appending after sealing is correctly rejected, but the class never records that an append-was-attempted. There is no `load` method, so callers must manually assign `entries`, `sealed`, and `seal_signature` from the JSON record before verifying.

---
*△ AURA Pattern Library — © Reality Optimizer*
