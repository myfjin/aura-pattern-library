# spsc ring buffer

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `(val: u64) → bool`

## What it does

spsc_ring_buffer — a single-producer/single-consumer bounded ring using atomic indices.

Core idea: a fixed-size ring with atomic head (producer) and atomic tail (consumer).
No locks — just atomics for indices and a Vec<AtomicU64> for data. THE ONE LAW:
producer writes N items concurrently while consumer reads concurrently; every item
arrives exactly once in FIFO order. A non-atomic head/tail would lose or duplicate items.
When to use: high-performance bounded queues with exactly one producer and consumer.

## Guarantee

When it runs, spsc ring buffer guarantees assert_eq!(written, n_items, "producer wrote wrong count"); assert_eq!(received.len(), n_items, "consumer received wrong count"); assert_eq!(received, (0..n_items as u64).collect::<Vec<_>>(), "FIFO order violated") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(written, n_items, "producer wrote wrong count")`
- `assert_eq!(received.len(), n_items, "consumer received wrong count")`
- `assert_eq!(received, (0..n_items as u64).collect::<Vec<_>>(), "FIFO order violated")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
