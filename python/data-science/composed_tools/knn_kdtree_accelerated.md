# knn kdtree accelerated

**Language:** Python · **Sphere:** data-science · **Category:** Composed Tools

**Signature:** `(items: List[Tuple[Point, int]], depth: int) → Optional[KDNode]`

## What it does

KD-Tree Accelerated k-NN — the search engine meets the classifier.

CROSS-SPHERE COMPOSED PATTERN: kd_tree (programming sphere, awesome-python-
patterns) x knn_classifier (data-science sphere) — embedding bridge 0.484,
found 2026-07-06. The DS sphere's kNN is brute-force: every query touches
every training point. The programming sphere's kd-tree is a spatial search
engine with no purpose of its own. Composed: identical predictions,
a fraction of the distance computations — both PROVEN, not assumed.

Use when: kNN on low-dimensional data where query volume makes brute force
expensive.

## Guarantee

When it runs, knn kdtree accelerated guarantees all((abs(a[0] - b[0]) < 1e-09 for a, b in zip(nt, nb))); agree == len(queries); ratio < 0.4 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `all((abs(a[0] - b[0]) < 1e-09 for a, b in zip(nt, nb)))`
- `agree == len(queries)`
- `ratio < 0.4`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
