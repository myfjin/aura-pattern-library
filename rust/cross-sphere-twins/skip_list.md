# skip list

**Language:** Rust · **Sphere:** rust · **Category:** cross-sphere-twins

**Signature:** `() → usize`

## What it does

skip_list — a real probabilistic skip list (index-arena, safe); levels drive search.

Core idea: each node has a random height; higher levels are "express lanes" that skip ahead,
giving O(log n) expected search. Nodes live in a Vec (index links, no unsafe). Search starts
at the top level and drops down — the levels are LOAD-BEARING, not decoration. THE LAW: insert
a set, and assert (1) sorted iteration and (2) search results match a BTreeSet reference, AND
(3) the structure actually built multiple levels (a sorted-Vec impostor never would). When to
use: ordered sets, Redis sorted-sets, probabilistic ordered indices.

## Guarantee

When it runs, skip list guarantees assert_eq!(SkipList::new(1).iter_sorted().len(), 0, "empty skip list") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(sl.iter_sorted(), sorted, "skip-list iteration must match BTreeSet order")`
- `assert_eq!(sl.search(v), reference.contains(&v), "search({v}) must match reference")`
- `assert!(sl.max_level_used() > 1, "a real skip list builds >1 level, got {}", sl.max_level_used())`
- `assert!(has_express, "at least one node must have an express-lane link above level 0")`
- `assert_eq!(sl.iter_sorted().len(), vals.len(), "duplicate insert does not grow the set")`
- `assert_eq!(SkipList::new(1).iter_sorted().len(), 0, "empty skip list")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
