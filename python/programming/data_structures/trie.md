# trie

**Language:** Python · **Sphere:** programming · **Category:** Data Structures

**Signature:** `() → None`

## What it does

Trie (Prefix Tree) implementation with autocomplete functionality.

## Guarantee

When it runs, trie guarantees survivors == 17; trie.search(w) is True; trie.search(w) is False (proven by run).

**Checkable constraints:**

- `trie.search(w) is True`
- `trie.search(w) is False`
- `trie.starts_with(p) is True`
- `trie.starts_with('xyz') is False`
- `trie.starts_with('') is True`
- `sorted(trie.autocomplete('app', 10)) == ['app', 'apple', 'application', 'apply']`
- `sorted(trie.autocomplete('band', 10)) == ['band', 'bandana', 'bandit']`
- `trie.autocomplete('xyz', 10) == []`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
