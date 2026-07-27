# weighted reservoir sampling

**Language:** Python · **Sphere:** data-science · **Category:** Streaming & Sketches

## What it does

Weighted Reservoir Sampling (A-Res Algorithm)

Core idea: Sample k items from a weighted stream such that inclusion probability is
proportional to item weight. A-Res: use u^(1/w) as sort key.

When to use: You have a stream of weighted items and need a representative sample
where rare (high-weight) items are more likely to appear.

## Guarantee

When it runs, weighted reservoir sampling guarantees rare_freq > common_freq; rare_freq > 0.3 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `rare_freq > common_freq`
- `rare_freq > 0.3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class WeightedReservoirSampler:`, `def __init__(self, k: int = 5):`, `def process(self, item: str, weight: float) -> None:`, `def get_sample(self) -> List[Tuple[str, float]]:`, `def get_inclusion_freq(self, item: str, total_samples: int) -> float:`
**Valid input:** `k` is a positive integer; `weight` is a positive float; `item` is a string.
**Core:** A-Res weighted reservoir sampling. Assigns each item a key `u^(1/weight)` where `u` is uniform; keeps the top `k` keys in a sorted list, giving higher-weight items larger inclusion probability.
**Assert:** Over many runs, high-weight "rare" items have a higher empirical inclusion frequency than low-weight "common" items, and rare-item frequency exceeds 30%.
**⚠️ Defect:** The implementation uses a plain sorted list instead of a heap, so insertion is `O(k)` rather than `O(log k)`. `get_inclusion_freq` is semantically odd: it returns `count_in_current_reservoir / total_samples`, which is not the standard definition of inclusion probability over runs. Items with weight ≤ 0 are silently skipped rather than raising. The demo inflates the stream by adding each item `int(weight)` times, conflating weight with multiplicity.

---
*△ AURA Pattern Library — © Reality Optimizer*
