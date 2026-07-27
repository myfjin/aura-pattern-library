# token bucket limiter

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 6 · Resource guards & quotas

**Signature:** `(tokens_per_sec: int) → ?`

## What it does

Token bucket limiter: caps operation rate to tokens/sec.
Failure simulated: issue 1000 ops over 2 sec with 10 tokens/sec cap;
assert only ~20 ops granted, rest delayed/denied.

## Guarantee

When it runs, token bucket limiter guarantees granted <= 25; denied > 900; granted > 15 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `granted <= 25`
- `denied > 900`
- `granted > 15`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — positive (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
