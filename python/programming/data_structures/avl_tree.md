# avl tree

**Language:** Python · **Sphere:** programming · **Category:** Data Structures

**Signature:** `() → None`

## What it does

AVL Tree Implementation

A self-balancing binary search tree where the heights of the two child subtrees 
of any node differ by at most one.

## Guarantee

When it runs, avl tree guarantees sum(avl.inorder_traversal()) == 1275; avl.is_balanced(); avl.root.height <= 8 (proven by run).

**Checkable constraints:**

- `avl.is_balanced()`
- `avl.root.height <= 8`
- `avl.inorder_traversal() == list(range(1, 51))`
- `sum(avl.inorder_traversal()) == 1275`
- `avl.search(25) is True and avl.search(1) is True and (avl.search(50) is True)`
- `avl.search(100) is False and avl.search(0) is False`
- `avl.inorder_traversal() == list(range(1, 51))`
- `avl.is_balanced()`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
