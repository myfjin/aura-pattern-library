"""
2D grid density binning: partition points into cells, count per-cell density.

Core idea: divide (minx,miny)-(maxx,maxy) into regular grid; assign points to cells;
count occupancy. Planted hotspot lands in correct cell; total count = input count.

When to use: heatmaps, spatial statistics, clustering pre-processing.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple, Dict

def grid_density_binning(points: List[Tuple[float, float]],
                         grid_size: float) -> Tuple[Dict[Tuple[int, int], int], float, float]:
    """
    Bin points into grid cells of size grid_size.
    Return: (cell_counts dict, min_point, max_point), and verify total count.
    """
    if not points:
        return {}, float('inf'), float('-inf')

    minx = min(p[0] for p in points)
    miny = min(p[1] for p in points)
    maxx = max(p[0] for p in points)
    maxy = max(p[1] for p in points)

    cell_counts: Dict[Tuple[int, int], int] = {}
    for x, y in points:
        cell_x = int((x - minx) / grid_size)
        cell_y = int((y - miny) / grid_size)
        key = (cell_x, cell_y)
        cell_counts[key] = cell_counts.get(key, 0) + 1

    return cell_counts, minx, miny

if __name__ == '__main__':
    import random
    random.seed(42)

    # Scattered points
    points = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(100)]
    grid_size = 2.0

    cell_counts, minx, miny = grid_density_binning(points, grid_size)

    # Total count should match input
    total = sum(cell_counts.values())
    assert total == len(points), f"Total count {total} != input {len(points)}"

    # All cells should have positive count
    for count in cell_counts.values():
        assert count > 0, "All cells should have at least 1 point"

    # Number of cells should be reasonable (not all in 1 cell, not empty cells)
    assert len(cell_counts) >= 2, "Should occupy multiple cells"
    assert len(cell_counts) <= 100, "Should not create too many cells"

    # Plant a hotspot: cluster points in a region
    cluster_points = [(5.0 + random.uniform(-0.3, 0.3), 5.0 + random.uniform(-0.3, 0.3))
                      for _ in range(30)]
    cluster_points.extend([(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(20)])

    cell_counts_cluster, _, _ = grid_density_binning(cluster_points, 1.0)
    total_cluster = sum(cell_counts_cluster.values())
    assert total_cluster == 50, f"Total should be 50, got {total_cluster}"

    # Hotspot cells should exist and have high counts (may split across cells due to grid)
    # Verify that there's a clear dense region (cluster should dominate)
    max_count = max(cell_counts_cluster.values())
    assert max_count >= 5, f"Densest cell should have >= 5 points, got {max_count}"

    # Count cells with significant population; cluster's 30 points should occupy a small region
    high_count_cells = sum(1 for c in cell_counts_cluster.values() if c >= 3)
    assert high_count_cells <= 8, "Cluster should occupy few cells (with ±0.3 noise and grid_size=1.0)"

    # Fine grid: should have more cells but same total
    cell_counts_fine, _, _ = grid_density_binning(points, 1.0)
    total_fine = sum(cell_counts_fine.values())
    assert total_fine == len(points), "Fine grid should preserve total count"
    assert len(cell_counts_fine) > len(cell_counts), "Fine grid should have more cells"

    print("PASS")
