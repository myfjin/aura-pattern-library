# grid density binning

**Language:** Python · **Sphere:** data-science · **Category:** Geospatial & Spatial

**Signature:** `(points: List[Tuple[float, float]], grid_size: float) → Tuple[Dict[Tuple[int, int], int], float, float]`

## What it does

2D grid density binning: partition points into cells, count per-cell density.

Core idea: divide (minx,miny)-(maxx,maxy) into regular grid; assign points to cells;
count occupancy. Planted hotspot lands in correct cell; total count = input count.

When to use: heatmaps, spatial statistics, clustering pre-processing.

## Guarantee

When it runs, grid density binning guarantees total_cluster == 50; total == len(points); count > 0 (proven by run).

**Checkable constraints:**

- `total == len(points)`
- `count > 0`
- `len(cell_counts) >= 2`
- `len(cell_counts) <= 100`
- `total_cluster == 50`
- `max_count >= 5`
- `high_count_cells <= 8`
- `total_fine == len(points)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
