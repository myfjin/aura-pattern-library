# nonce replay guard

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

## What it does

Nonce replay guard — detect replayed one-time values.
Core idea: monotonic counter, set membership, sliding window.
When to use: CSRF tokens, API request IDs, sequence deduplication.

## Guarantee

When it runs, nonce replay guard guarantees assert!(seen.insert(counter), "fresh nonce should be accepted") (none-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(seen.insert(counter), "fresh nonce should be accepted")`
- `assert!(!seen.insert(3), "replayed nonce should be rejected")`
- `assert!(!seen.insert(1), "replayed nonce should be rejected")`
- `assert!(!seen.insert(1), "old nonce outside window rejected")`
- `assert!(seen.insert(counter), "fresh within window accepted")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** none (no checkable constraint)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
