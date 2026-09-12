"""
KD-Tree Accelerated k-NN — the search engine meets the classifier.

CROSS-SPHERE COMPOSED PATTERN: kd_tree (programming sphere, awesome-python-
patterns) x knn_classifier (data-science sphere) — embedding bridge 0.484,
found 2026-07-06. The DS sphere's kNN is brute-force: every query touches
every training point. The programming sphere's kd-tree is a spatial search
engine with no purpose of its own. Composed: identical predictions,
a fraction of the distance computations — both PROVEN, not assumed.

Use when: kNN on low-dimensional data where query volume makes brute force
expensive.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Optional, Tuple

Point = Tuple[float, float]
COUNTER = {"tree": 0, "brute": 0}


class KDNode:
    __slots__ = ("point", "label", "axis", "left", "right")

    def __init__(self, point: Point, label: int, axis: int):
        self.point = point
        self.label = label
        self.axis = axis
        self.left: Optional["KDNode"] = None
        self.right: Optional["KDNode"] = None


def build_kdtree(items: List[Tuple[Point, int]], depth: int = 0) -> Optional[KDNode]:
    if not items:
        return None
    axis = depth % 2
    items = sorted(items, key=lambda it: it[0][axis])
    mid = len(items) // 2
    node = KDNode(items[mid][0], items[mid][1], axis)
    node.left = build_kdtree(items[:mid], depth + 1)
    node.right = build_kdtree(items[mid + 1:], depth + 1)
    return node


def sqdist(a: Point, b: Point, counter_key: str) -> float:
    COUNTER[counter_key] += 1
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def knn_tree(root: KDNode, q: Point, k: int) -> List[Tuple[float, int]]:
    """Best-first descent with pruning: a subtree is skipped only when the
    splitting plane is farther than the current k-th best distance — the
    defining move that saves distance computations without changing results."""
    best: List[Tuple[float, int]] = []   # (sqdist, label), kept sorted, len<=k

    def visit(node: Optional[KDNode]):
        if node is None:
            return
        d = sqdist(q, node.point, "tree")
        if len(best) < k or d < best[-1][0]:
            best.append((d, node.label))
            best.sort()
            del best[k:]
        axis_gap = q[node.axis] - node.point[node.axis]
        near, far = (node.left, node.right) if axis_gap <= 0 else (node.right, node.left)
        visit(near)
        if len(best) < k or axis_gap ** 2 < best[-1][0]:
            visit(far)

    visit(root)
    return best


def knn_brute(items: List[Tuple[Point, int]], q: Point, k: int) -> List[Tuple[float, int]]:
    ds = sorted((sqdist(q, p, "brute"), lbl) for p, lbl in items)
    return ds[:k]


def majority(neigh: List[Tuple[float, int]]) -> int:
    votes = {}
    for _, lbl in neigh:
        votes[lbl] = votes.get(lbl, 0) + 1
    return max(votes, key=lambda l: (votes[l], -l))


if __name__ == "__main__":
    random.seed(42)

    # Two gaussian classes, 2000 training points, 300 queries.
    train: List[Tuple[Point, int]] = []
    for _ in range(1000):
        train.append(((random.gauss(0, 1), random.gauss(0, 1)), 0))
        train.append(((random.gauss(3, 1), random.gauss(3, 1)), 1))
    queries = [(random.gauss(1.5, 2.0), random.gauss(1.5, 2.0)) for _ in range(300)]

    root = build_kdtree(train)
    k = 5
    agree = 0
    for q in queries:
        nt = knn_tree(root, q, k)
        nb = knn_brute(train, q, k)
        # identical neighbor DISTANCES (labels can differ only on exact ties)
        assert all(abs(a[0] - b[0]) < 1e-9 for a, b in zip(nt, nb)), \
            f"neighbor distances differ at {q}"
        agree += majority(nt) == majority(nb)

    ratio = COUNTER["tree"] / COUNTER["brute"]
    print(f"queries: {len(queries)} · prediction agreement {agree}/{len(queries)} · "
          f"distance computations: tree {COUNTER['tree']} vs brute {COUNTER['brute']} "
          f"({ratio:.1%})")

    # The composed claim, measured on both sides:
    assert agree == len(queries), "kd-tree kNN must predict identically to brute force"
    assert ratio < 0.40, \
        f"kd-tree should cut distance computations by >60%: got {ratio:.1%}"
    print("knn_kdtree_accelerated.py PASS")
