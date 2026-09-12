"""
Shoelace formula: polygon area and centroid from vertex coordinates.

Core idea: area via sum of cross products; centroid via weighted average.
Works for both convex and concave polygons (signed area can be negative).

When to use: geometry calculations, shape analysis, mass properties.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple

def polygon_area_centroid(vertices: List[Tuple[float, float]]) -> Tuple[float, Tuple[float, float]]:
    """Return absolute area and centroid (cx, cy) of polygon."""
    n = len(vertices)
    if n < 3:
        return 0.0, (0.0, 0.0)

    signed_area = 0.0
    cx_sum = 0.0
    cy_sum = 0.0

    for i in range(n):
        x0, y0 = vertices[i]
        x1, y1 = vertices[(i + 1) % n]
        cross = x0 * y1 - x1 * y0
        signed_area += cross
        cx_sum += (x0 + x1) * cross
        cy_sum += (y0 + y1) * cross

    area = abs(signed_area) / 2.0
    if signed_area == 0:
        return 0.0, (0.0, 0.0)

    cx = cx_sum / (3.0 * signed_area)
    cy = cy_sum / (3.0 * signed_area)

    return area, (cx, cy)

if __name__ == '__main__':
    # Unit square: area=1, centroid=(0.5, 0.5)
    square = [(0, 0), (1, 0), (1, 1), (0, 1)]
    area_sq, (cx_sq, cy_sq) = polygon_area_centroid(square)
    assert abs(area_sq - 1.0) < 0.001, f"Square area should be 1.0, got {area_sq}"
    assert abs(cx_sq - 0.5) < 0.01 and abs(cy_sq - 0.5) < 0.01, f"Square centroid should be (0.5, 0.5), got ({cx_sq}, {cy_sq})"

    # Triangle: (0,0), (1,0), (0,1) => area=0.5, centroid=(1/3, 1/3)
    tri = [(0, 0), (1, 0), (0, 1)]
    area_tri, (cx_tri, cy_tri) = polygon_area_centroid(tri)
    assert abs(area_tri - 0.5) < 0.001, f"Triangle area should be 0.5, got {area_tri}"
    assert abs(cx_tri - 1/3) < 0.01 and abs(cy_tri - 1/3) < 0.01, f"Triangle centroid should be ~(0.333, 0.333), got ({cx_tri}, {cy_tri})"

    # Concave L-shape: (0,0)-(2,0)-(2,1)-(1,1)-(1,2)-(0,2)
    # Area = 2*2 - 1*1 = 3
    l_shape = [(0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2)]
    area_l, (cx_l, cy_l) = polygon_area_centroid(l_shape)
    assert abs(area_l - 3.0) < 0.01, f"L-shape area should be 3.0, got {area_l}"
    # Centroid should be somewhere central (rough check)
    assert 0.3 < cx_l < 1.3 and 0.3 < cy_l < 1.3, f"L-shape centroid should be roughly central, got ({cx_l}, {cy_l})"

    # Degenerate: three collinear points should have area 0
    line = [(0, 0), (1, 1), (2, 2)]
    area_line, _ = polygon_area_centroid(line)
    assert area_line < 0.001, f"Collinear points should have near-zero area, got {area_line}"

    # Reverse orientation should give same area (absolute value)
    area_sq_rev, (cx_sq_rev, cy_sq_rev) = polygon_area_centroid(list(reversed(square)))
    assert abs(area_sq_rev - area_sq) < 0.001, "Reversed orientation should have same area"
    assert abs(cx_sq_rev - cx_sq) < 0.01 and abs(cy_sq_rev - cy_sq) < 0.01, "Reversed centroid should match"

    print("PASS")
