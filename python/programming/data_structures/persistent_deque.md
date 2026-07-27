# persistent deque

**Language:** Python · **Sphere:** programming · **Category:** Data Structures

## What it does

Doubly-linked deque that serializes its full contents to a pickle file after
every mutation and reloads that state on construction.

Use when a deque must survive process death: append/appendleft/pop/popleft mirror
collections.deque, an optional maxlen evicts from the opposite end, and each
operation persists to disk.

Guarantees (self-test): a fresh instance recovers exact ordered state after the
owning instance is dropped, a 200-op fuzz with periodic reloads tracks
collections.deque, maxlen evicts the correct end, and empty pops raise IndexError.

## Guarantee

When it runs, persistent deque guarantees dq.pop() == 2 and dq.popleft() == 0 and (list(dq) == [1]); list(dq) == [0, 1, 2]; list(recovered) == [-1, 1, 7] (proven by run).

**Checkable constraints:**

- `list(dq) == [0, 1, 2]`
- `dq.pop() == 2 and dq.popleft() == 0 and (list(dq) == [1])`
- `list(recovered) == [-1, 1, 7]`
- `len(recovered) == 3`
- `d.pop() == oracle.pop()`
- `d.popleft() == oracle.popleft()`
- `list(d) == list(oracle)`
- `list(d) == list(oracle) and len(d) == len(oracle)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
