# copy on write config

**Language:** Go · **Sphere:** programming · **Category:** Concurrency

**Signature:**
```go
type Config struct {
    Host       string
    Port       int
    Generation int
}
// No exported functions — the pattern is the atomic.Pointer[Config] usage pattern
// in main(): configPtr.Store(newCfg) for writes, configPtr.Load() for reads.
```

**Valid input:** A `Config` struct where `Host` is formatted as `"host-N"` (N integer), `Port` is `8080 + N`, and `Generation` is `N`. The initial config is `&Config{Host: "host-0", Port: 8080, Generation: 0}`. The writer increments N from 1 to 500 across two rounds.

## What it does

A copy-on-write config pattern using `atomic.Pointer[Config]`. One writer creates a fresh `Config` struct for each generation swap and atomically stores the pointer via `configPtr.Store(newCfg)`. 32 concurrent readers load the pointer via `configPtr.Load()` and read all fields from the same snapshot. Each reader checks for torn reads by verifying that `Host`'s generation suffix, `Port`, and `Generation` are mutually consistent (port must equal `8080 + hostGen`, generation must equal `hostGen`). Two rounds of 32 readers × 20,000 reads + 1 writer × 500 swaps each (total 640,000 reads per round). The pattern guarantees that no reader ever observes a mix of fields from different generations.

## Guarantee

All three commands pass cleanly on Go 1.22.12.

Proven self-test line:

```
copy_on_write_config: 0 torn reads (both rounds), 500 generations, 640000 reads × 2, race-clean — PASS
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

The pattern relies on `atomic.Pointer[Config]` (Go 1.19+). On Go 1.18 and earlier, the equivalent is `atomic.LoadPointer`/`atomic.StorePointer` with `unsafe.Pointer` casts, which loses type safety. The torn-read detection logic (lines 49–57) parses the `Host` string to extract the generation — this is a string-format coupling that would break if the `Host` format changes. The two rounds are identical in structure (same reader/writer counts, same assertions) and test the same mechanism twice; the second round adds no new failure mode beyond the first.
