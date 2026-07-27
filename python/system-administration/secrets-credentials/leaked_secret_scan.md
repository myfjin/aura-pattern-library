# leaked secret scan

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 10 · Secrets & credentials

**Signature:** `(blob: str, patterns: None) → ?`

## What it does

Leaked secret scan: detect secrets in code blobs via regex patterns.
Failure simulated: blob contains "password = 'hunter2'" and API key patterns;
scan detects and reports exact matches and line numbers.

## Guarantee

When it runs, leaked secret scan guarantees any(('hunter2' in m['secret'] for m in password_matches)); any(('sk_live' in m['secret'] for m in api_matches)); 'line' in match (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(matches) >= 4`
- `len(password_matches) > 0`
- `any(('hunter2' in m['secret'] for m in password_matches))`
- `len(api_matches) > 0`
- `any(('sk_live' in m['secret'] for m in api_matches))`
- `'line' in match`
- `match['line'] > 0`
- `match['secret']`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
