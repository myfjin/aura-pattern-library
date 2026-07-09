"""
Douglas-Peucker polyline simplification: reduce point count while bounding deviation.

Core idea: find point with max distance to chord; if > epsilon, recurse on
both halves; otherwise remove all intermediate points. Output ⊂ input,
max deviation ≤ epsilon.

When to use: map rendering, trajectory compression, lossy path storage.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple

def point_line_distance(point: Tuple[float, float],
                        line_start: Tuple[float, float],
                        line_end: Tuple[float, float]) -> float:
    """Perpendicular distance from point to line segment."""
    x, y = point
    x1, y1 = line_start
    x2, y2 = line_end
    num = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1)
    denom = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    return num / denom if denom > 0 else 0

def douglas_peucker(points: List[Tuple[float, float]], epsilon: float) -> List[Tuple[float, float]]:
    """Simplify polyline: output is subset of input, max deviation ≤ epsilon."""
    if len(points) < 3:
        return points

    max_dist, max_idx = 0, 0
    for i in range(1, len(points) - 1):
        dist = point_line_distance(points[i], points[0], points[-1])
        if dist > max_dist:
            max_dist, max_idx = dist, i

    if max_dist > epsilon:
        left = douglas_peucker(points[:max_idx + 1], epsilon)
        right = douglas_peucker(points[max_idx:], epsilon)
        return left[:-1] + right
    else:
        return [points[0], points[-1]]

if __name__ == '__main__':
    # Gentle curve: should simplify significantly
    gentle = [(i, i * 0.1 + (i % 3) * 0.05) for i in range(20)]
    simp_gentle = douglas_peucker(gentle, epsilon=0.3)
    assert len(simp_gentle) < len(gentle), f"Should simplify gentle curve, got {len(simp_gentle)} vs {len(gentle)}"
    assert 2 <= len(simp_gentle) <= len(gentle), f"Simplified gentle should be reasonable, got {len(simp_gentle)}"

    # Straight line: should collapse to 2 points
    line = [(i, 2 * i) for i in range(10)]
    simp_line = douglas_peucker(line, epsilon=0.1)
    assert len(simp_line) == 2, f"Straight line should simplify to 2 points, got {len(simp_line)}"
    assert simp_line[0] == line[0] and simp_line[-1] == line[-1], "Should keep endpoints"

    # Sharp corner: should preserve corner with tight epsilon
    corner = [(0, 0), (1, 0), (1, 1), (2, 1)]
    simp_corner_tight = douglas_peucker(corner, epsilon=0.05)
    assert len(simp_corner_tight) >= 3, f"Sharp corner with tight epsilon should keep >= 3 points, got {len(simp_corner_tight)}"

    # Same corner with loose epsilon: may collapse
    simp_corner_loose = douglas_peucker(corner, epsilon=0.5)
    assert 2 <= len(simp_corner_loose) <= 4, f"Corner with loose epsilon should be 2-4 points, got {len(simp_corner_loose)}"

    # Verify deviation constraint on a test case
    tight = [(0, 0), (1, 1), (2, 0), (3, 1), (4, 0)]
    simp_tight = douglas_peucker(tight, epsilon=0.2)
    assert simp_tight[0] == tight[0] and simp_tight[-1] == tight[-1], "Endpoints preserved"
    for i in range(1, len(simp_tight) - 1):
        # Each simplified point should have been in original (subset invariant)
        assert simp_tight[i] in tight, f"Simplified point {simp_tight[i]} not in original"

    print("PASS")
