# fan in multiplexer

**Language:** Go · **Sphere:** programming · **Category:** Concurrency

**Signature:**
```go
func fanIn(inputs ...<-chan int) <-chan int
```

**Valid input:** Any number of `<-chan int` (read-only int channels). Input channels should eventually be closed by their senders. Passing a nil channel will cause the goroutine reading from it to block forever (no nil-guard).

## What it does

A standard fan-in multiplexer. For each input channel, a goroutine is spawned that reads values via `range` and forwards them to a shared output channel. A separate goroutine waits on a `sync.WaitGroup` (one `Done` per input goroutine) and closes the output channel when all inputs are exhausted. The output channel is unbuffered, so sends block until the consumer reads — this provides backpressure. The self-test uses 4 input channels sending 250, 100, 1, and 0 values (total 351). It verifies: total received == 351, per-source counts == 250/100/1/0, and every value seen exactly once (no duplicates). A second "disaster" case uses 2 channels with 10 and 5 values (total 15) and verifies the same invariants.

## Guarantee

All three commands pass cleanly.

Proven self-test line:

```
fan_in_multiplexer: 351 values multiplexed exactly (250+100+1+0), per-source counts verified 250/100/1/0, output closed exactly once, every value seen exactly once — PASS
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

The output channel is unbuffered — a slow consumer blocks every producer goroutine. For bursty inputs, a buffered output channel (or a separate goroutine that batches) would reduce producer blocking. The per-source count verification (lines 81–103) uses value ranges (`0-249`, `250-349`, `==350`) rather than tracking source identity — this works for the test but would not generalize to arbitrary value sets. The `fanIn` function does not accept a cancellation signal; if the consumer stops reading, all producer goroutines leak (they block forever on `out <- val`). A context-aware variant would allow early termination.
