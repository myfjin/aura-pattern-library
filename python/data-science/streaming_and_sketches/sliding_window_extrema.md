# sliding window extrema

**Language:** Python · **Sphere:** data-science · **Category:** Streaming & Sketches

**Signature:** `(data: List[float], window_size: int) → List[Tuple[float, float]]`

## Guarantee

When it runs, sliding window extrema guarantees abs(brute_min - deque_min) < 1e-09; abs(brute_max - deque_max) < 1e-09; deque_ops < brute_ops (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(brute_min - deque_min) < 1e-09`
- `abs(brute_max - deque_max) < 1e-09`
- `deque_ops < brute_ops`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class MonotonicDequeMinMax:`, `def __init__(self, window_size: int):`, `def process(self, value: float) -> Tuple[float, float]:`, `def sliding_window_min_max_bruteforce(data: List[float], window_size: int) -> List[Tuple[float, float]]:`, `def sliding_window_min_max_deque(data: List[float], window_size: int) -> List[Tuple[float, float]:`
**Valid input:** `window_size` is a positive integer; `data` is a list of numbers with `len(data) >= window_size`.
**Core:** Provides both a brute-force O(n·w) sliding-window min/max and an efficient deque-based O(n) implementation using two monotonic deques.
**Assert:** The deque solution matches brute-force exactly for a 200-point random stream with window size 10; operation counts show the deque approach is more efficient.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
