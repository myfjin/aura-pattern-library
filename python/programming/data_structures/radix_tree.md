# radix tree

**Language:** Python · **Sphere:** programming · **Category:** Data Structures

## What it does

Radix tree (compressed trie) mapping string keys to values, splitting and
merging edges so each node carries the longest shared prefix.

Use for prefix-dense string keys where a plain trie wastes single-child chains;
supports insert (with in-place overwrite), search, delete, and keys().

Guarantees (self-test): all keys resolve through edge-splits, deleting a key that
prefixes others leaves the longer keys intact, internal edge fragments are not
reported as keys, and a 400-op fuzz on collision-heavy keys agrees with a dict
oracle.

## Guarantee

When it runs, radix tree guarantees sum((tree.search(k) for k, _ in test_data)) == 55; tree.search('app') == 20 and len(tree.keys()) == 10; tree.search('apple') == 1 and tree.search('application') == 3 (proven by run).

**Checkable constraints:**

- `tree.search(key) == value`
- `tree.search('missing') is None`
- `tree.search('appl') is None`
- `tree.search('ap') is None`
- `sorted(tree.keys()) == sorted((k for k, _ in test_data))`
- `sum((tree.search(k) for k, _ in test_data)) == 55`
- `tree.search('app') == 20 and len(tree.keys()) == 10`
- `tree.delete('app') is True`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
