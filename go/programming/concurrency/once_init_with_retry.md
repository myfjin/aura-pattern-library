# once init with retry

**Language:** Go · **Sphere:** programming · **Category:** Concurrency

**Signature:**
```go
type OnceInitWithRetry struct { /* mu, cond, result, err, success, inFlight, attempts, concurrent, maxObservedConcurrent */ }
func NewOnceInitWithRetry() *OnceInitWithRetry
func (o *OnceInitWithRetry) Do(fn func() (interface{}, error)) (interface{}, error)
func (o *OnceInitWithRetry) Stats() (totalAttempts, maxConc int32)
```

**Valid input:** `fn` is a function that returns `(result, nil)` on success or `(nil, error)` on failure. Multiple goroutines may call `Do` concurrently with the same `fn`. The function should be idempotent or safe to retry — it may be called more than once if earlier attempts fail.

## What it does

A lazy initializer that caches only successful results and allows retry after failures — the gap `sync.Once` leaves, which caches failure permanently. `Do` enters a loop under a mutex: if a successful result already exists, it returns it immediately. If no attempt is in flight, it claims the attempt slot (`inFlight = true`) and exits the loop to run `fn`. If an attempt is in flight, it waits on a condition variable and re-checks on wake. The actual function call runs *outside* the mutex (unlocked at line 65, re-locked at line 84) so concurrent callers waiting on the condition variable can be notified. Concurrent depth is tracked atomically and capped at 1 (the pattern guarantees at most one concurrent init attempt). On success, `result` and `success` are set; on failure, `err` is set. Either way, `inFlight` is cleared and `cond.Broadcast()` wakes all waiters. The self-test has two parts: (1) 100 concurrent callers with a function that succeeds on first call — verifies `successfulInits == 1`, `maxConc == 1`, all 100 results are the identical pointer, and no torn results (every caller gets exactly `(result, nil)` or `(nil, error)`, never both or neither). (2) A function that fails on attempts 1 and 2 and succeeds on attempt 3, with three waves of 100 concurrent callers — verifies `successes == 1`, `attempts == failures + successes`, `maxConc == 1`, all non-nil results are the identical pointer, no torn results, and a fourth cached wave of 100 callers adds zero new attempts.

## Guarantee

All three commands pass cleanly on Go 1.22.12.

Proven self-test line:

```
part 1 success: successful_inits=1, max_concurrent_attempts=1, distinct_pointers=1, torn_results=0 — PASS
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

The `Do` method releases the mutex while running `fn` (line 65) and re-acquires it afterward (line 84). If `fn` panics, the mutex is never re-acquired, leaving the `OnceInitWithRetry` permanently locked and all future callers deadlocked. A `defer o.mu.Lock()` after the unlock would not work (it would block); the correct fix is a `defer` that re-acquires the mutex on panic recovery. The `Stats()` method returns `int32` values that are atomically loaded but the two fields are loaded separately — a caller reading both may see them from different points in time (not a consistency issue for monitoring, but worth noting). The `maxObservedConcurrent` tracking uses a CAS loop (lines 69–77) that is correct but could be simplified with `max` + atomic swap.
