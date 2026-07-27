# broadcast fanout

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `(msg: u64) → ?`

## What it does

broadcast_fanout — one producer broadcasts a message to N receivers.

Core idea: a producer publishes a value; N receivers each receive it exactly once
via a shared Condvar and Mutex<Vec>. THE ONE LAW: the producer sends M messages;
each of N receivers must receive all M messages in the same order, and each message
is received exactly N times (once per receiver).
When to use: one-to-many publish/subscribe patterns.

## Guarantee

When it runs, broadcast fanout guarantees assert_eq!(items, expected, "receiver saw wrong messages/order: {items:?}") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(items, expected, "receiver saw wrong messages/order: {items:?}")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
