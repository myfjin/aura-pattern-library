# image stats

**Language:** Python · **Sphere:** programming · **Category:** Vision

**Signature:** `() → None`

## What it does

Histogram-based image contrast stretcher module.

This module provides functionality to enhance image contrast by stretching
the histogram of an image using percentile-based clipping and lookup table
(LUT) generation.

## Guarantee

When it runs, image stats guarantees stats.total_pixels == 400; stats.histogram[50] == 100 and stats.histogram[100] == 200 and (stats.histogram[150] == 100); sum(stats.histogram) == 400 (proven by run).

**Checkable constraints:**

- `stats.total_pixels == 400`
- `stats.histogram[50] == 100 and stats.histogram[100] == 200 and (stats.histogram[150] == 100)`
- `sum(stats.histogram) == 400`
- `stats.histogram[0] == 0 and stats.histogram[255] == 0`
- `stretcher.min_val == 50 and stretcher.max_val == 150`
- `mapped[0] == 0`
- `mapped[-1] == 255`
- `120 <= mapped[1] <= 135`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
