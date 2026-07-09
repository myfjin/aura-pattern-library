"""
Graham scan: compute convex hull of a point set.

Core idea: sort points by polar angle from lowest point, use stack to
maintain left-turn invariant. Hull vertices are exactly the extremes.

When to use: bounding envelopes, distance metrics, collision bounds.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple

def cross_product(o: Tuple[float, float], a: Tuple[float, float],
                  b: Tuple[float, float]) -> float:
    """Cross product of vectors OA and OB."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull_graham(points: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    """Return convex hull vertices in CCW order."""
    if len(points) < 3:
        return sorted(points)

    # Find lowest point (lexicographic if tied)
    start = min(points, key=lambda p: (p[1], p[0]))

    # Sort by polar angle from start
    def polar_angle_key(p: Tuple[float, float]) -> float:
        if p == start:
            return -math.pi
        return math.atan2(p[1] - start[1], p[0] - start[0])

    sorted_points = sorted(points, key=polar_angle_key)

    # Graham scan with stack
    hull = []
    for p in sorted_points:
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    return hull

if __name__ == '__main__':
    # Square
    square_pts = [(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 0.5)]
    hull = convex_hull_graham(square_pts)
    # Hull should have exactly 4 vertices (corners, in CCW order)
    assert len(hull) == 4, f"Square with center should have hull of 4, got {len(hull)}"
    # All hull vertices should be corners
    corners = {(0, 0), (1, 0), (1, 1), (0, 1)}
    hull_set = set(hull)
    assert hull_set == corners, f"Hull vertices should be corners, got {hull_set}"

    # Triangle
    tri_pts = [(0, 0), (1, 0), (0.5, 1), (0.5, 0.3)]
    hull_tri = convex_hull_graham(tri_pts)
    assert len(hull_tri) == 3, f"Triangle with interior point should have hull of 3, got {len(hull_tri)}"

    # Collinear points: should still work
    line_pts = [(0, 0), (1, 1), (2, 2), (0.5, 0.5)]
    hull_line = convex_hull_graham(line_pts)
    assert len(hull_line) >= 2, "Collinear points should have at least endpoints"

    # Dense cloud with clear extremes
    import random
    random.seed(42)
    cloud = [(random.random(), random.random()) for _ in range(50)]
    cloud.extend([(0, 0), (2, 0), (2, 2), (0, 2)])  # Add known extremes
    hull_cloud = convex_hull_graham(cloud)
    # Hull should contain the planted extremes
    assert (0, 0) in hull_cloud or any(abs(p[0]) < 0.01 and abs(p[1]) < 0.01 for p in hull_cloud), "Should have lower-left extreme"
    assert len(hull_cloud) >= 4, f"Cloud with 4 planted extremes should have hull >= 4, got {len(hull_cloud)}"

    print("PASS")
