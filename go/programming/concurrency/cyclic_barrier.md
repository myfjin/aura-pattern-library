# cyclic barrier

**Language:** Go · **Sphere:** programming · **Category:** Concurrency

**Signature:**
```go
type CyclicBarrier struct { /* parties, count, generation, mu, cond */ }
func NewCyclicBarrier(parties int) *CyclicBarrier
func (cb *CyclicBarrier) Await()
```

**Valid input:** `parties` must be ≥ 1 (no guard against 0 or negative). `Await()` is called by exactly `parties` goroutines per phase; calling it from fewer or more goroutines than `parties` will deadlock or cause incorrect phase advancement.

## What it does

A reusable barrier synchronizing N goroutines across multiple phases. Internally, `Await()` locks a mutex, increments a counter, and checks whether the last party has arrived. If so, it resets the counter to 0, increments the generation, and broadcasts to all waiters. Otherwise it waits on a condition variable until the generation changes (indicating the last party arrived and released everyone). The barrier is reusable because the generation counter distinguishes one phase from the next — a waiter that wakes from a spurious signal checks `cb.generation == currentGen` and re-waits if the generation hasn't advanced. The self-test runs 8 parties × 5 phases in two scenarios: equal-speed parties (verifying per-party phase sequences are `[0,1,2,3,4]` and cumulative arrivals at each phase release are `8*(k+1)`), and unequal-speed parties (party 0 sleeps 50ms per phase, verifying total arrivals still equal `8*5 = 40`).

## Guarantee

All three commands pass cleanly on Go 1.22.12.

Proven self-test line:

```
cyclic_barrier: 8 parties × 5 phases rendezvous == 40 arrivals, unequal speeds proven, all phases 0-4 traversed — PASS
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

The barrier uses a single `sync.Cond` with `Broadcast()` — every phase release wakes all waiters, which is O(N) wakeups per phase. For very large N, a barrier using a semaphore or `sync.WaitGroup` reset would be more efficient. The `Await()` method holds the mutex for the entire duration of the wait (the `sync.Cond.Wait()` releases it internally, but the deferred `cb.mu.Unlock()` only fires after the goroutine re-acquires it on wake). This is correct but means the last party to arrive holds the mutex while calling `Broadcast()`, serializing the wakeup. The self-test uses `sync.WaitGroup`-based gating between phases (lines 71–78, 98–110) to verify per-phase arrival counts — this is a test harness detail, not part of the barrier itself. No guard against `NewCyclicBarrier(0)` or negative parties (would cause division-by-zero or deadlock).
