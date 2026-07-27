# atomic max tracker

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `(val: u64) → ?`

## What it does

atomic_max_tracker — a lock-free running maximum via CAS without locking.

Core idea: an AtomicU64 holds the current maximum. To update, spin-CAS: if the
new value exceeds the current max, replace it; otherwise, skip. THE ONE LAW:
N threads each observe random values and call update(); the final max must equal
the true maximum observed value. A non-atomic max or a broken CAS loop reports wrong results.
When to use: high-concurrency metrics where only the max matters, no lock desired.

## Guarantee

When it runs, atomic max tracker guarantees assert_eq!(got, expected_max, "max tracker reported wrong maximum") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(got, expected_max, "max tracker reported wrong maximum")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
