# sharded counter

**Language:** Go · **Sphere:** programming · **Category:** Concurrency

**Signature:**
```go
const numShards = 8
type shard struct { mu sync.Mutex; data map[string]int }
type ShardedCounter struct { shards []*shard }
func NewShardedCounter() *ShardedCounter
func (sc *ShardedCounter) Increment(key string, value int)
func (sc *ShardedCounter) Get(key string) int
func (sc *ShardedCounter) Sum() int
```

**Valid input:** Any string key. `value` is typically 1 (increment by one) but any positive int works. Keys are distributed across 8 shards via a simple hash (sum of byte values modulo 8). The counter is not safe for concurrent reads during concurrent writes on the same shard (Get and Increment both lock per-shard).

## What it does

A striped-lock counter that shards a `map[string]int` across 8 independent mutexes to reduce contention. `Increment` hashes the key to select a shard, locks it, and increments the value. `Get` hashes the key, locks the shard, and reads the value. `Sum` iterates all shards, locks each one, and sums all values. The self-test runs 64 goroutines × 10,000 increments across 8 keys (total 640,000 increments), then verifies `Sum() == 640000` and each key's count == 80000. A counterexample function (gated behind `SKIP_COUNTEREXAMPLE` env var) demonstrates lost updates on an unsynchronized `int` under the same load — it verifies the unsynchronized total is NOT 640000, proving the sharded counter's correctness is not trivial.

## Guarantee

All commands pass cleanly on Go 1.22.12. The `-race` run requires `SKIP_COUNTEREXAMPLE=1` because the counterexample deliberately contains a data race.

Proven self-test line:

```
sharded_counter: 64 goroutines × 10000 increments = 640000 total, Sum() == 640000, each of 8 keys == 80000 — PASS
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

The hash function (sum of byte values modulo 8) is a poor distribution — for real workloads, use a proper hash (e.g., FNV-1a) to avoid collisions. The number of shards is hardcoded at 8; a configurable shard count would allow tuning for different contention levels. `Sum()` locks each shard sequentially — this is correct but means `Sum()` blocks concurrent `Increment`/`Get` calls on every shard while it runs. For a large number of shards or frequent `Sum()` calls, a snapshot-based approach (atomic per-shard totals) would reduce blocking. The counterexample uses `unsyncCounter++` which is a read-modify-write without synchronization — the race detector catches this, which is why `SKIP_COUNTEREXAMPLE=1` is needed for `-race` runs.
