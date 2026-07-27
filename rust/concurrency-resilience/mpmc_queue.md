# mpmc queue

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

## What it does

mpmc_queue — a multi-producer/multi-consumer queue using std::sync::mpsc.

Core idea: multiple producers send items via an mpsc channel; multiple consumers
share a receiver (behind Arc<Mutex>) and pull until the queue drains and closes.
THE ONE LAW: P producers each send M items; C consumers drain the queue. Every
item is consumed EXACTLY once (summed total equals P × M × item_value). If items
are lost or duplicated, the sum will mismatch.
When to use: work distribution among multiple workers with guaranteed delivery.

## Guarantee

When it runs, mpmc queue guarantees assert_eq!(got, expected, "mpmc sum mismatch: items lost or duplicated") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(got, expected, "mpmc sum mismatch: items lost or duplicated")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
