# char ngram language id

**Language:** Python · **Sphere:** data-science · **Category:** Text / NLP II

**Signature:** `(text: str) → Dict[str, int]`

## What it does

Character n-gram language identification: distinguish languages via bigram profiles.

Builds character bigram frequencies; compares via distance. Core claim:
true language matched; false language rejected. Planted English vs pseudo-lang.

## Guarantee

When it runs, char ngram language id guarantees dist_english < dist_pseudo (weak-grade: directional, proven by run).

**Checkable constraints:**

- `dist_english < dist_pseudo`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def char_bigrams(text: str) -> Dict[str, int]:`, `def ngram_distance(bigrams1: Dict[str, int], bigrams2: Dict[str, int]) -> float:`
**Valid input:** `text` is a string of length ≥ 2; `bigrams1`/`bigrams2` are dictionaries mapping bigram strings to positive counts.
**Core:** Extracts character bigram frequency profiles and compares them with normalized L1 distance. Enables simple language/dialect discrimination by profile similarity.
**Assert:** English-like text is closer to an English bigram profile than to a pseudo-random character profile; distance is symmetric.
**⚠️ Defect:** `ngram_distance` does not handle empty profiles except by returning `inf` when one total is zero; two empty texts would also return `inf`. It uses L1 distance on normalized counts, which is valid but does not account for bigram rank or top-N out-of-vocabulary robustness.

---
*△ AURA Pattern Library — © Reality Optimizer*
