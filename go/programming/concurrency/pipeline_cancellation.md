# pipeline cancellation

**Language:** Go · **Sphere:** programming · **Category:** Concurrency

**Signature:**
```go
// No exported types or functions — the pattern is the channel pipeline structure in main():
// stage 1 (generator) → stage1out → stage 2 (transformer) → stage2out → stage 3 (consumer)
// with a shared cancel channel that stops all stages and prevents goroutine leaks.
```

**Valid input:** The pipeline processes integers. Stage 1 generates `i` from 0 to N-1. Stage 2 doubles each value (`val * 2`). Stage 3 consumes the doubled values. The cancel channel is closed externally after a condition is met (e.g., consumed count reaches a threshold). All channels are buffered (capacity 10) to allow some decoupling between stages.

## What it does

A 3-stage channel pipeline with cancellation that guarantees no goroutine leaks. Each stage checks the shared `cancel` channel in its `select` statement before sending. Stage 1 generates items and sends them to `stage1out` (buffered, 10). Stage 2 reads from `stage1out`, doubles the value, and sends to `stage2out` (buffered, 10). Stage 3 reads from `stage2out` and counts consumption. Each stage has a `defer stagesFinished.Add(1)` to signal its exit. When `cancel` is closed, all stages that are blocked on a send or waiting to receive see the cancellation via `select` and return immediately. The self-test has two parts: (1) Success case — 100 items, pipeline runs to completion, verifies `generated == 100`, `consumed == 100`, `stagesFinished == 3`, and goroutine count returns to baseline. (2) Disaster case — 10,000 items, stage 3 consumes slowly (1ms per item) to create backpressure, cancellation is triggered after 50 items consumed, verifies goroutine count returns to baseline (no leak), `consumed < 10000` (cancellation really cut it short), `consumed >= 50` (cancellation didn't fire too early), and `stagesFinished == 3`.

## Guarantee

All three commands pass cleanly on Go 1.22.12.  

(Note: the exact cancellation point varies between runs — 61 and 64 in the two runs above — because it depends on scheduler timing. The assert only requires `consumed >= 50` and `consumed < 10000`.)

Proven self-test line:

```
pipeline_cancellation: success case 100 items complete, disaster case cancelled at 61 items, 3 stages exited cleanly, baseline goroutines restored — PASS
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

The pipeline uses busy-polling to detect completion: `time.Sleep(500ms)` for the success case and a polling loop (`time.Sleep(100ms)` × 20 iterations = up to 2s) for goroutine count settling. This makes the test slow (~2.5s total) and schedule-dependent. A more responsive design would use a `sync.WaitGroup` or a done channel per stage. The goroutine-count baseline check uses `runtime.NumGoroutine()` which includes GC workers and runtime threads — the 50ms sleep + GC call before measuring baseline is a heuristic. The pipeline has no backpressure mechanism beyond the channel buffer size (10); if stage 3 is slow, stage 2 blocks on send, which in turn blocks stage 1 — this is correct but means a single slow consumer stalls the entire pipeline.
