# seqlock snapshot

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `(new_x: u64, new_y: u64) → ?`

## What it does

seqlock_snapshot — a seqlock ensuring readers never observe torn (partial) updates.

Core idea: a sequence number guards reads — there is NO lock on the data itself, so a
reader genuinely can catch the writer mid-update. The writer bumps seq to odd, writes
the two fields (as independent atomics, so field-by-field visibility is real), then
bumps seq to even. A reader samples seq (must be even), reads both fields lock-free,
then re-samples seq; if it changed, the writer intervened and the reader retries.
THE ONE LAW: a writer updates a 2-field value (y == 2·x) concurrently with lock-free
readers. Because the fields are separate atomics, a reader with a broken/absent seq
protocol WOULD see x from the new value and y from the old (y != 2·x). The seq protocol
must catch every such torn read. When to use: multi-field snapshots under high
concurrent read pressure with a single writer.

## Guarantee

When it runs, seqlock snapshot guarantees assert_eq!(total_torn, 0, "seqlock failed: {total_torn} torn reads observed") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(total_torn, 0, "seqlock failed: {total_torn} torn reads observed")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — chaos (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
