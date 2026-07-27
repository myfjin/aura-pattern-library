# integrity check

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 4 · State/DB durability

**Signature:** `(path: str) → ?`

## What it does

integrity_check: detect DB corruption via PRAGMA integrity_check (and catch open/query failures).
Failure simulated: overwrite a b-tree data page in the middle of the file with garbage (reliable
corruption, past the header). Recovery asserted: a CLEAN DB checks "ok", and the CORRUPTED DB is
DETECTED as non-ok (or fails to open/query) — never silently passed. The old version hedged with
a tautology because its 2-byte flip might not be detected; this corrupts a whole page region so
detection is deterministic, and the assert is unconditional: clean == ok, corrupted != ok.

## Guarantee

When it runs, integrity check guarantees size > 8192; clean == 'ok'; corrupted != 'ok' (weak-grade: directional, proven by run).

**Checkable constraints:**

- `size > 8192`
- `clean == 'ok'`
- `corrupted != 'ok'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
