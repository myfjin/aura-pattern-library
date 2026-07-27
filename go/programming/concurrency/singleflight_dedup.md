# singleflight dedup

**Language:** Go · **Sphere:** programming · **Category:** Concurrency

**Signature:**
```go
type flightResult struct { result interface{}; err error; done chan struct{} }
type Singleflight struct { mu sync.Mutex; inflight map[string]*flightResult }
func NewSingleflight() *Singleflight
func (sf *Singleflight) Do(key string, fn func() (interface{}, error)) (interface{}, error)
```

**Valid input:** `key` is a string identifying the operation to deduplicate. `fn` is a function that returns `(result, error)`. Multiple goroutines may call `Do` concurrently with the same key. The function should be idempotent or safe to run once per in-flight window.

## What it does

A call deduplication pattern that collapses concurrent calls for the same key into a single function execution. When `Do` is called, it acquires the mutex and checks if a flight for that key already exists in the `inflight` map. If so, it releases the mutex and blocks on `flight.done` — when the first caller's function completes, the done channel is closed and all waiters receive the identical result. If no flight exists, the caller creates a new `flightResult`, stores it in the map, releases the mutex, runs `fn`, stores the result, deletes the key from the map (under mutex), and closes the done channel to unblock all waiters. Deduplication is scoped to the in-flight window only — after the flight completes, a new call for the same key runs `fn` again. The self-test spawns 200 goroutines on key `"a"` and 50 on key `"b"`, with a function that increments an atomic counter and sleeps 10ms. It verifies: call counter == 2 (one per distinct key), all 200 results for `"a"` are identical, all 50 results for `"b"` are identical. A post-flight call for `"a"` verifies the counter advances to 3 (proving in-flight-only dedup) and the result matches the original.

## Guarantee

All three commands pass cleanly on Go 1.22.12.

Proven self-test line:

```
singleflight_dedup: 200 concurrent calls + 50 concurrent calls collapsed to 2 total function executions, identical results per key, in-flight dedup proven by post-flight re-execution (counter: 2→3) — PASS
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

The `Do` method holds the mutex while creating the flight entry (lines 43–56) but releases it before running `fn`. If `fn` panics, the flight entry remains in the `inflight` map forever — the done channel is never closed, and all waiters for that key block permanently. A `defer` that cleans up the flight entry on panic would prevent this leak. The `inflight` map is never cleaned up for keys whose function never returns (e.g., blocks forever) — this is a memory leak. The pattern does not support context-based cancellation: if a caller is waiting on `<-flight.done` and the caller's context is cancelled, there is no way to abort the wait. The standard `golang.org/x/sync/singleflight` package supports forgetting keys and shared results.
