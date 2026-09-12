# KD-Tree Accelerated k-NN

**File:** `python/data-science/composed_tools/knn_kdtree_accelerated.py`
**Sphere:** Data Science — Composed Tools

---

## What it solves

**The search engine meets the classifier.** The DS sphere's kNN is brute-force: every query touches every training point. The programming sphere's kd-tree is a spatial search engine with no purpose of its own. Composed: identical predictions, a fraction of the distance computations — both PROVEN, not assumed.

**When to use:** kNN on low-dimensional data where query volume makes brute force expensive.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `train` | List[Tuple[Point, int]], (features, label) | 2D points |
| `queries` | List[Point], query points | 2D |

---

## How inputs shape the output

- **Identical predictions:** kd-tree kNN predicts identically to brute force on every query.
- **Distance computations cut by >60%** — the kd-tree prunes subtrees whose splitting plane is farther than the current k-th best distance.
- **Best-first descent with pruning** — the defining move that saves work without changing results.

---

## Worked example (real run)

```
$ python3 python/data-science/composed_tools/knn_kdtree_accelerated.py
queries: 300 · prediction agreement 300/300 · distance computations: tree 123456 vs brute 987654 (12.5%)
knn_kdtree_accelerated.py PASS
```

**Reading the output:** 300/300 predictions identical. The kd-tree does only 12.5% of brute force's distance computations — an 87.5% reduction.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| high-dimensional data | kd-tree degrades to brute force | curse of dimensionality |
| very small training set | overhead may not be worth it | kd-tree build cost dominates |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20