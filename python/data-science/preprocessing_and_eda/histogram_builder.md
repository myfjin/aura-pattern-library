# histogram builder

**Language:** Python · **Sphere:** data-science · **Category:** Preprocessing & EDA

**Signature:** `(n: int) → int`

## What it does

Histogram Builder Pattern.

Constructs a histogram using equal-width bins with automatic bin-count selection
(Sturges' rule). Core idea: Sturges rule k = ceil(log2(n) + 1) works well for
normal data; easy rule without parameter tuning.

When to use: exploratory data analysis, visualizing distributions, detecting
multimodality, choosing reasonable bin counts automatically.

## Guarantee

When it runs, histogram builder guarantees len(counts) == expected_bins; sum(counts) == len(bimodal_data); edges[i] <= edges[i + 1] (proven by run).

**Checkable constraints:**

- `sum(counts) == len(bimodal_data)`
- `edges[i] <= edges[i + 1]`
- `len(counts) == expected_bins`
- `peak1_val > 8`
- `peak2_val > 8`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
