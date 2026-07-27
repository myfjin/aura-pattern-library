# dtw dynamic time warping

**Language:** Python · **Sphere:** data-science · **Category:** Optimization & Distances

**Signature:** `(a: float, b: float) → float`

## What it does

DISTANCE METRIC: Dynamic Time Warping (DTW)

Core idea: Align two time series by warping time, allowing elastic matching of
temporal patterns. DTW distance <= euclidean distance and captures shape similarity
better than point-wise metrics. Includes optimal alignment path reconstruction.

When to use: Time series comparison, speech recognition, gesture recognition, or
any domain where temporal stretching/compression is semantically valid.

## Guarantee

When it runs, dtw dynamic time warping guarantees dtw_dist_identical == 0.0; dtw_dist >= 0; dtw_xy >= 0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `dtw_dist_identical == 0.0`
- `len(alignment) > 0`
- `dtw_dist >= 0`
- `dtw_xy >= 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `dtw_distance(series1: List[float], series2: List[float]) -> Tuple[float, List[Tuple[int, int]]]`
**Valid input:** `series1`, `series2` non-empty lists of numbers.
**Core:** Dynamic Time Warping: fills an `(n+1)×(m+1)` cost matrix with `cost[i][j] = dist + min(cost[i-1][j], cost[i][j-1], cost[i-1][j-1])`, then backtracks to recover the optimal alignment path.
**Assert:** Identical series yield DTW distance `0`; warped series produce a positive distance with a non-empty alignment.
**⚠️ Defect:** The backtracking logic is incorrect. When `i>0` and `j>0` it chooses the minimum of three predecessors, but when either `i` or `j` hits zero it only decrements the non-zero index without checking whether the diagonal predecessor would have been cheaper. More importantly, the alignment path can skip the start `(0,0)` in some cases. The demo only checks non-negative distance, so the defect is not caught.

---
*△ AURA Pattern Library — © Reality Optimizer*
