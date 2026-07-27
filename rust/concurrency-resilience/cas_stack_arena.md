# cas stack arena

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `(val: u64) → bool`

## What it does

cas_stack_arena — a lock-free stack using atomic head pointer and arena indices.

Core idea: arena stores values; head (AtomicUsize) is the stack top. Each slot
in the arena also tracks the next index. Pushes/pops use CAS on head.
THE ONE LAW: multiple threads push items concurrently; pop all items. Every pushed
item is popped exactly once. A broken CAS loses items or causes duplicates.
When to use: lock-free work-stealing or concurrent stacks where push/pop dominate.

## Guarantee

When it runs, cas stack arena guarantees assert_eq!(items.len(), expected_count, "stack lost items or dropped pops") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(items.len(), expected_count, "stack lost items or dropped pops")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
