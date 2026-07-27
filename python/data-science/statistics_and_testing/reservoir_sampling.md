# reservoir sampling

**Language:** Python · **Sphere:** data-science · **Category:** Statistics & Testing

**Signature:** `(stream: ?, k: int) → List`

## What it does

Reservoir Sampling (Algorithm R)

Core idea: Sample k items uniformly from a stream of unknown length without storing the
entire stream. Maintain a "reservoir" of k items; for each new item i (i >= k), include
it with probability k/i, replacing a random reservoir item if accepted.

When to use: Sample from data streams, huge files, or situations where you can't load all
data into memory at once.

## Guarantee

When it runs, reservoir sampling guarantees all((0 <= x < 20 for x in sample_1)); sample_tiny == [0, 1, 2] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(sample_1) == 5`
- `all((0 <= x < 20 for x in sample_1))`
- `len(set(sample_1)) == 5`
- `is_uniform`
- `len(sample_tiny) == 3`
- `sample_tiny == [0, 1, 2]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def reservoir_sample(stream, k: int) -> List:`, `def verify_uniformity(samples_per_run: List[List], item_count: int) -> bool:`, `def simple_stream():`, `def stream():`, `def tiny_stream():`
**Valid input:** `stream` is any iterable; `k` is a positive integer.
**Core:** Algorithm R reservoir sampling: keeps a reservoir of size `k`; the i-th item (0-indexed) replaces a random reservoir element with probability `k/(i+1)`.
**Assert:** Sampling 5 from 20 yields 5 unique in-range items; 50 runs of 10 from 100 pass a uniformity check; sampling more than the stream length returns all available items.
**⚠️ Defect:** The `verify_uniformity` helper expects `item_count` distinct IDs and declares success if at least 70% of observed counts fall within a factor of 2 of expected — this is a weak statistical test. The helper stream generators are defined in the main block and are not generally reusable.

---
*△ AURA Pattern Library — © Reality Optimizer*
