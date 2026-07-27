# treiber lock free stack

**Language:** Go · **Sphere:** programming · **Category:** Concurrency

**Signature:**
```go
type node struct { value int; next *node }
type Stack struct { head atomic.Pointer[node] }
func (s *Stack) Push(value int)
func (s *Stack) Pop() (int, bool)
```

**Valid input:** Any `int` value. `Push` is safe to call concurrently from any number of goroutines. `Pop` returns `(value, true)` if the stack is non-empty, or `(0, false)` if empty. The stack is not bounded — it grows with each push.

## What it does

A Treiber stack — a lock-free concurrent stack using CAS on the head pointer. `Push` creates a new node, then loops: loads the current head, sets the new node's `next` to it, and attempts `CompareAndSwap` to make the new node the head. If CAS fails (another goroutine changed the head), it retries. `Pop` loops: loads the head, returns `(0, false)` if empty, otherwise attempts CAS to swing the head to `head.next`. If CAS fails, it retries. Both Push and Pop are lock-free, not wait-free: the CAS retry loops are unbounded, so individual goroutines may lose the race arbitrarily many times while the system as a whole makes progress. The self-test has two parts: (1) Sequential push of 16,000 values, then sequential pop — verifies `len(popped) == 16000`, `maxTally == 1` (no value popped twice), `len(tally) == 16000` (all values distinct), and stack is empty after drain. (2) 16 concurrent pushers (1,000 values each = 16,000 total) and 16 concurrent poppers — verifies the same invariants under contention, with poppers spinning when the stack is temporarily empty until all pushes complete.

## Guarantee

All three commands pass cleanly on Go 1.22.12.

Proven self-test line:

```
16000 distinct values pushed/popped exactly once (max_tally=1), stack drained to empty; 16 concurrent pushers and 16 concurrent poppers with head-pointer contention — PASS
```

## Verification evidence

- `go vet` · `go build` · `go run` · `go run -race` — all exit 0, no data race.
- Verified on **two toolchains**: macOS go1.26.4 (.5) and Linux go1.22.12 (.8).
- Harvest gate: **P1** (`~/ai-lab/tools/go_harvest_gate.py`, evidence card in the staging dir).
- Library validator: `polyglot.py` **BASELINE-OK**. Note the validator caps concurrency
  patterns at FLAG by design (memory-ordering is routed to a model-checker), so its ladder
  cannot issue a PASS for this sphere — the race detector and the counted invariants are the
  discriminating oracles here.
- Doc claims verified against the code by an independent reviewer (Ver): **MATCHES**
  (`VER_review_2026-07-27.md`).

## Known limitation

The Treiber stack suffers from the classic ABA problem: if a node is popped, freed, and a new node with the same address is pushed, a CAS that only compares pointer values cannot distinguish this. In Go with garbage collection, the ABA problem is mitigated (nodes are not freed and reused while references exist), but the `head.next` pointer could theoretically be stale if the head node is popped and its `next` field is modified by a concurrent push of a recycled node. In practice, Go's GC prevents this because a node reachable from a goroutine's local `head` variable cannot be collected. The stack is LIFO (not FIFO) — elements are popped in reverse push order. The concurrent poppers in the self-test spin-wait when the stack is temporarily empty (lines 142–151), which burns CPU. A notification mechanism (channel or condition variable) would be more efficient. The `maxTally == 1` assert (lines 91, 179) is entailed by `len(popped) == 16000` and `len(tally) == 16000` (16,000 pops over 16,000 distinct values = one apiece by arithmetic) — it is redundant but documents the exactly-once guarantee.
