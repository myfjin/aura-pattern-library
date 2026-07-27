# suffix array

**Language:** Python · **Sphere:** programming · **Category:** Data Structures

**Signature:** `(text1: str, text2: str) → Tuple[str, List[Tuple[int, int]]]`

## What it does

Suffix array (naive sort build) with pattern search, a Kasai LCP array, a sparse-
table RMQ over the LCP, and a longest-common-substring routine.

Use to index a string for substring search (binary search over sorted suffixes)
and to answer longest-common-prefix / longest-common-substring questions.

Guarantees (self-test): 'banana' suffix array and LCP match the textbook values,
pattern search matches brute force, a 120-char oracle agrees on SA/LCP/search, and
longest_common_substring recovers a planted overlap.

## Guarantee

When it runs, suffix array guarantees flcp[i] == true_lcp; sa.suffixes == [5, 3, 1, 0, 4, 2]; sa.to_suffix(0) == 'a' and sa.to_suffix(3) == 'banana' (proven by run).

**Checkable constraints:**

- `sa.suffixes == [5, 3, 1, 0, 4, 2]`
- `sa.to_suffix(0) == 'a' and sa.to_suffix(3) == 'banana'`
- `lcp.lcp == [1, 3, 0, 0, 2, 0]`
- `sorted(sa.search('ana')) == [1, 3]`
- `sorted(sa.search('na')) == [2, 4]`
- `sa.search('ban') == [0]`
- `sa.search('xyz') == []`
- `sorted(sa.search('a')) == [1, 3, 5]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
