# errgroup first error

**Language:** Go · **Sphere:** programming · **Category:** Concurrency

**Signature:**
```go
type ErrGroup struct { /* mu, cancelled, cancelledChan, wg, firstErr, errOnce, goroutinesExited, cancelledObserved */ }
func NewErrGroup() *ErrGroup
func (g *ErrGroup) Go(f func(cancel <-chan struct{}) error)
func (g *ErrGroup) Wait() error
```

**Valid input:** `f` is a function that receives a read-only `<-chan struct{}` cancellation signal and returns an `error`. The function should periodically check the cancellation channel (via `select`) and return early when it fires. The `Go` method can be called multiple times before `Wait()`.

## What it does

A custom errgroup that captures the first error returned by any goroutine, cancels all remaining goroutines via a shared channel, and blocks `Wait()` until every goroutine has exited. When a goroutine returns a non-nil error, `errOnce.Do` ensures only the first error is recorded. The error-setter also acquires `mu`, sets `cancelled = true`, and closes `cancelledChan` (under the mutex to prevent double-close). Other goroutines observe the closed channel via `select` and return early. `Wait()` simply calls `sync.WaitGroup.Wait()` and returns the stored `firstErr` (nil if all succeeded). The self-test has two parts: (1) 5 tasks all returning nil — verifies `err == nil` and `goroutinesExited == 5`; (2) 10 tasks where task 3 (index 2) fails after 20ms — verifies returned error string is `"task 3 failed"`, wall clock < 1s, `goroutinesExited == 10`, and `cancelledObserved == 9` (the failing task itself does not observe cancellation).

## Guarantee

All three commands pass cleanly on Go 1.22.12.

Proven self-test line:

```
errgroup_first_error: success nil, disaster 'task 3 failed' at <1s, 10 goroutines exited, 9 observed cancellation — PASS
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

The `Go` method does not handle panics from `f` — if a task panics, the `wg.Done()` and `goroutinesExited.Add(1)` in the deferred function still fire, but the panic propagates and crashes the program. The standard `errgroup.Group` from `golang.org/x/sync/errgroup` recovers panics. The cancellation signal is a closed channel (not a context), so there is no deadline or timeout propagation — only broadcast cancellation. The `cancelledObserved` counter is incremented inside the task function (line 103), which relies on the task author remembering to check the cancel channel; a task that ignores cancellation and runs to completion would not increment this counter, making the assert `cancelledObserved == 9` a test-harness guarantee rather than a structural one.
