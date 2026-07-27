# space saving heavy hitters

**Language:** Python · **Sphere:** data-science · **Category:** Streaming & Sketches

## What it does

Space-Saving Algorithm for Top-K Heavy Hitters

Core idea: Maintain exactly k counters for the top-k most frequent items seen so far.
When a new item arrives, either increment an existing counter or replace the smallest one.

When to use: You need the top-k most frequent items from a stream with minimal memory
(only k counters, not a full frequency table).

## Guarantee

When it runs, space saving heavy hitters guarantees est_id == tru_id; tru_cnt <= est_cnt <= tru_cnt + err_bound (weak-grade: directional, proven by run).

**Checkable constraints:**

- `est_id == tru_id`
- `tru_cnt <= est_cnt <= tru_cnt + err_bound`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class SpaceSavingTopK:`, `def __init__(self, k: int = 5):`, `def process(self, item: str) -> None:`, `def get_top_k(self) -> List[Tuple[str, int]:`
**Valid input:** `k` is a positive integer; `item` is hashable.
**Core:** Space-Saving top-k heavy-hitter algorithm. Maintains at most `k` counters; on a new unseen item when full, it evicts the item with the smallest count and assigns the new item `min_count + 1`, preserving the error bound `exact <= estimate <= exact + N/k`.
**Assert:** On a Zipfian 8-item stream with `k=6`, the top-3 identities and order match the exact top-3, and every estimate lies within the Space-Saving error bound.
**⚠️ Defect:** The guarantee only holds when the number of counters is strictly larger than the number of items of interest; with `k` equal to the desired top-k size, tail churn can erode accuracy. The stream generation in the demo uses `max(1, 100 // (i+1))`, which is not a true Zipf distribution.

---
*△ AURA Pattern Library — © Reality Optimizer*
