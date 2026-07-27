# rendezvous channel

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `(val: T) → ?`

## What it does

rendezvous_channel — an unbuffered synchronous handoff channel.

Core idea: a sender send() blocks until a receiver recv() takes the value.
Zero buffering — the sender and receiver must rendezvous. THE ONE LAW: a sender
and receiver exchange exactly one item; timing measurements prove the sender blocked
until the receiver arrived. Concurrent senders/receivers work correctly with no lost
or duplicated items. When to use: strict producer-consumer synchronization.

## Guarantee

When it runs, rendezvous channel guarantees assert_eq!(exchanged, n_exchanges, "not all items exchanged"); assert_eq!(items, (0..n_exchanges as u64).collect::<Vec<_>>(), "items out of order or lost") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(exchanged, n_exchanges, "not all items exchanged")`
- `assert_eq!(items, (0..n_exchanges as u64).collect::<Vec<_>>(), "items out of order or lost")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
