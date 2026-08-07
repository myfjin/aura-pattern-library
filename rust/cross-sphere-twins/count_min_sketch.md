# count min sketch

**Language:** Rust · **Oracle sphere:** data-science (this file is the Rust twin) · **Category:** Streaming & Sketches

## What it does

count_min_sketch — frequency sketch; OVERESTIMATE-ONLY guarantee.

Core idea: k hash functions, m counters per hash. For a key, increment all k
counters. Query returns the minimum. Guarantee: est ≥ true for every key.
THE LAW: plant a known frequency set, query each, and assert est ≥ true always.
When to use: heavy-hitter detection, space-efficient frequency estimation.

## Guarantee

When it runs, count min sketch guarantees cat_est >= 50; dog_est >= 40; cat_est - 50 <= max_allowed_error (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `cat_est >= 50`
- `dog_est >= 40`
- `cat_est - 50 <= max_allowed_error`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this Rust twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class CountMinSketch:`, `def __init__(self, width: int = 100, depth: int = 5, epsilon: float = 0.01):`, `def _hash(self, item: str, seed: int) -> int:`, `def increment(self, item: str, count: int = 1) -> None:`, `def query(self, item: str) -> int:`, `def find_heavy_hitters(self, threshold: int) -> List[str]:`
**Valid input:** `item` is a string; `count` is a positive integer; `width`, `depth` are positive integers; `epsilon` is a small positive float.
**Core:** Streaming Count-Min Sketch with `depth` independent MD5 hash functions over a `width × depth` counter table. Provides frequency upper bounds and a heavy-hitter scan.
**Assert:** Estimated counts for planted heavy hitters are at least their true counts and within the claimed epsilon error bound; total stream length is tracked implicitly.
**⚠️ Defect:** `find_heavy_hitters` scans raw cell counts rather than querying known keys, so it returns integer counts instead of item identifiers. The class stores `epsilon` but does not use it to size the table automatically. MD5 hashing is overkill for a non-cryptographic frequency sketch.

---
*△ AURA Pattern Library — © Reality Optimizer*
