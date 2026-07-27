# dedupe records fuzzy

**Language:** Python · **Sphere:** data-science · **Category:** Data Wrangling From Scratch

**Signature:** `(s: str) → str`

## What it does

Fuzzy Record Deduplication.

Normalize records and link near-duplicates via edit-distance threshold.
We plant duplicates (with typos/variations) and verify they are identified.

## Guarantee

When it runs, dedupe records fuzzy guarantees [0, 1] in two_clusters; kept_ids == [1, 3, 5] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(clusters) == 3`
- `len(two_clusters) == 2`
- `[0, 1] in two_clusters`
- `len(deduped) == 3`
- `kept_ids == [1, 3, 5]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def normalize(s: str) -> str:`, `def edit_distance(s1: str, s2: str) -> int:`, `def find_duplicates(records: List[Dict[str, Any]], match_key: str, threshold: int = 2) -> List[List[int]]:`, `def dedupe(records: List[Dict[str, Any]], match_key: str, threshold: int = 2) -> List[Dict[str, Any]]:`
**Valid input:** `records` non-empty list of dicts; `match_key` present in every record; `threshold >= 0`.
**Core:** Fuzzy deduplication via Levenshtein edit distance on a single string field. Normalizes strings, greedily clusters records whose key distance is within the threshold, then keeps the first record of each cluster.
**Assert:** On planted records with two 1-character typos (Alice Johnson/Alice Jonson, Bob Smith/Bob Smyth) and one distinct record, `find_duplicates` returns three clusters with two two-record clusters, and `dedupe` keeps ids [1, 3, 5].
**⚠️ Defect:** The greedy clustering performs transitive chaining: if A is within threshold of B and B is within threshold of C, A and C are forced into the same cluster even when their direct distance exceeds the threshold. This can merge genuinely distinct records through a middle typo. The algorithm also only compares a single `match_key`; typos in other fields or swapped name order are ignored.

---
*△ AURA Pattern Library — © Reality Optimizer*
