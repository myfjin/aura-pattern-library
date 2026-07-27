# supervisor restart

**Language:** Rust · **Sphere:** rust · **Category:** filesystem-process

**Signature:** `(time: u32) → ?`

## What it does

supervisor_restart — restart backoff state machine; crash loop backs off, stable resets.

Core idea: track restart attempts; increase backoff on consecutive crashes, reset on stability.
THE ONE LAW: plant a crash sequence and a stability window, simulate restarts, assert
backoff increases and resets correctly.
When to use: process supervision, daemon restarts, circuit breakers.

## Guarantee

When it runs, supervisor restart guarantees assert_eq!(backoff.backoff_ms, 200, "first crash backoff should be 200ms"); assert_eq!(backoff.attempt, 1); assert_eq!(backoff.backoff_ms, 400, "second crash backoff should be 400ms") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(backoff.backoff_ms, 200, "first crash backoff should be 200ms")`
- `assert_eq!(backoff.attempt, 1)`
- `assert_eq!(backoff.backoff_ms, 400, "second crash backoff should be 400ms")`
- `assert_eq!(backoff.attempt, 2)`
- `assert_eq!(backoff.backoff_ms, 800, "third crash backoff should be 800ms")`
- `assert_eq!(backoff.backoff_ms, 1600, "fourth crash backoff should be 1600ms")`
- `assert_eq!(backoff.backoff_ms, 3200, "fifth crash backoff should be 3200ms")`
- `assert_eq!(backoff2.attempt, 3)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
