# version pin verify

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 12 · Deployment & rollback

**Signature:** `(version: str, expected_hash: str) → ?`

## What it does

Verify version pins match deployed artifacts.

## Guarantee

When it runs, version pin verify guarantees expected_hash in str(e); verifier.verify_deployment('v1.0', content) is True; False (proven by run).

**Checkable constraints:**

- `verifier.verify_deployment('v1.0', content) is True`
- `'hash mismatch' in str(e)`
- `expected_hash in str(e)`
- `'No pin found' in str(e)`
- `hash1 == hash2`
- `hash1 != hash2`
- `'hash mismatch' in str(e)`
- `verifier.verify_deployment(ver, content) is True`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class VersionPinVerify:`, `def __init__(self):`, `def pin_version(self, version, expected_hash):`, `def compute_hash(self, content):`, `def verify_deployment(self, version, actual_content):`
**Valid input:** `version` is a string; `expected_hash` is a 64-char hex SHA-256 string; `actual_content` is the deployed string.
**Core:** Registers a SHA-256 hash pin per version and verifies that the actual deployed content hashes to the pinned value.
**Assert:** Matching content passes; mismatched content raises `ValueError`; unpinned version raises `ValueError`; same content yields same hash, different content yields different hash, and a single-byte change is detected.
**⚠️ Defect:** There is no mechanism to discover or fetch the actual deployed content; the caller must supply it. The hash is computed over UTF-8 string content, so binary artifacts must be decoded first. Pin registry is in-memory only and is lost on process restart.

---
*△ AURA Pattern Library — © Reality Optimizer*
