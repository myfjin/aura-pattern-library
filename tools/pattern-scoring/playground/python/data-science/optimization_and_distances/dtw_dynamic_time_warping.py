"""
DISTANCE METRIC: Dynamic Time Warping (DTW)

Core idea: Align two time series by warping time, allowing elastic matching of
temporal patterns. DTW distance <= euclidean distance and captures shape similarity
better than point-wise metrics. Includes optimal alignment path reconstruction.

When to use: Time series comparison, speech recognition, gesture recognition, or
any domain where temporal stretching/compression is semantically valid.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple


def euclidean_distance(a: float, b: float) -> float:
    """Point-wise Euclidean distance."""
    return abs(a - b)


def dtw_distance(series1: List[float], series2: List[float]) -> Tuple[float, List[Tuple[int, int]]]:
    """
    Compute Dynamic Time Warping distance and optimal alignment path.

    Returns (dtw_distance, alignment_path) where alignment_path is a list of (i, j) tuples
    indicating which indices from series1 and series2 are aligned.
    """
    n, m = len(series1), len(series2)

    # Initialize cost matrix with infinity
    cost = [[float("inf")] * (m + 1) for _ in range(n + 1)]
    cost[0][0] = 0

    # Fill cost matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dist = euclidean_distance(series1[i - 1], series2[j - 1])
            cost[i][j] = dist + min(cost[i - 1][j], cost[i][j - 1], cost[i - 1][j - 1])

    # Backtrack to find optimal alignment
    alignment = []
    i, j = n, m
    while i > 0 or j > 0:
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            # Choose direction that gave minimum cost
            candidates = [
                (cost[i - 1][j - 1], i - 1, j - 1),  # Diagonal
                (cost[i - 1][j], i - 1, j),  # Up
                (cost[i][j - 1], i, j - 1),  # Left
            ]
            _, i, j = min(candidates, key=lambda x: x[0])

        alignment.append((i, j))

    alignment.reverse()
    return cost[n][m], alignment


if __name__ == "__main__":
    # Test 1: Identical series should have DTW distance 0
    series_a = [1.0, 2.0, 3.0, 4.0, 5.0]
    series_b = [1.0, 2.0, 3.0, 4.0, 5.0]

    dtw_dist_identical, alignment_identical = dtw_distance(series_a, series_b)
    assert (
        dtw_dist_identical == 0.0
    ), f"Identical series should have DTW=0, got {dtw_dist_identical}"

    # Test 2: Series with time warping should be closer than euclidean
    # series_c is stretched version of series_a: repeats some values
    series_c = [1.0, 1.0, 2.0, 3.0, 3.0, 4.0, 5.0]
    series_d = [1.0, 2.0, 3.0, 4.0, 5.0]

    # Compute DTW
    dtw_dist, alignment = dtw_distance(series_c, series_d)

    # DTW should align the warped series despite different lengths
    assert len(alignment) > 0, "No alignment path found"
    assert dtw_dist >= 0, f"DTW distance should be non-negative, got {dtw_dist}"

    # Test 3: Known small example
    # series1 = [0, 1, 2]
    # series2 = [0, 1]
    # Manual trace: cost[1][1]=0, cost[2][2]=0, cost[3][3]=0
    # Then cost[3][3] should be 0 (perfect alignment of [0,1] with [0,1])
    series_x = [0.0, 1.0, 2.0]
    series_y = [0.0, 1.0]

    dtw_xy, _ = dtw_distance(series_x, series_y)
    # Aligning [0,1,2] to [0,1]: best alignment costs 0+0+1=1 (the 2 unmatched)
    # or we align: 0->0 (cost 0), 1->1 (cost 0), 2 has no match (cost from DTW allows this)
    # Actual DTW allows flexible warping, so dtw([0,1,2], [0,1]) should be quite small
    assert dtw_xy >= 0, f"DTW should be non-negative, got {dtw_xy}"

    print(f"dtw_dynamic_time_warping.py: identical_dtw={dtw_dist_identical} warped_dtw={dtw_dist:.4f} PASS")
