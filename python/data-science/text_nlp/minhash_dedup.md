# minhash dedup

**Language:** Python · **Sphere:** data-science · **Category:** Text / NLP

## What it does

MinHash Signatures for Near-Duplicate Detection

Core idea: compute compact hash signatures for sets of tokens. Use Jaccard similarity
from signatures to estimate similarity and detect near-duplicates. Verify against
exact Jaccard computation.

Use when: detecting similar documents, deduplicating text corpora, or building
scalable similarity search without comparing all pairs directly.

## Guarantee

When it runs, minhash dedup guarantees len(dedup.signatures) == len(docs); len(sig) == dedup.num_hashes; sim_same == 1.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(dedup.signatures) == len(docs)`
- `len(sig) == dedup.num_hashes`
- `sim_same == 1.0`
- `error < 0.15`
- `(0, 1) in pair_indices or (1, 0) in pair_indices`
- `(2, 3) in pair_indices or (3, 2) in pair_indices`
- `(4, 5) in pair_indices or (5, 4) in pair_indices`
- `abs(jac_01 - jac_10) < 1e-06`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class MinHashDedup:`, `def __init__(self, num_hashes: int = 256):`, `def _tokenize(self, text: str) -> Set[str]:`, `def _hash_shingle(self, shingle: str, seed: int) -> int:`, `def compute_signature(self, text: str) -> Tuple[int, ...]:`, `def fit_signatures(self, documents: List[str]) -> None:`, `def estimated_jaccard(self, sig1: Tuple[int, ...], sig2: Tuple[int, ...]) -> float:`, `def exact_jaccard(set1: Set[str], set2: Set[str]) -> float:`, `def find_similar_pairs(self, threshold: float = 0.5) -> List[Tuple[int, int, float]]:`
**Valid input:** `documents` is a list of strings; `num_hashes` is a positive integer; `threshold` ∈ [0, 1].
**Core:** Computes MinHash signatures using MD5-based permutations, estimates Jaccard similarity from signature collision rate, and finds near-duplicate document pairs above a threshold. Also exposes exact Jaccard for validation.
**Assert:** A document compared to itself has estimated Jaccard 1.0; exact Jaccard is symmetric; the three planted near-duplicate pairs are detected with 128 hashes; the MinHash estimate is within 0.15 of exact Jaccard for word-shingle sets.
**⚠️ Defect:** `_hash_shingle` uses MD5, which is unnecessary for a non-cryptographic MinHash and slower than integer hashing. `_tokenize` treats whitespace-split words as shingles, so punctuation and case variations produce different shingles. The `estimated_jaccard` returns 0.0 for mismatched signature lengths instead of raising.

---
*△ AURA Pattern Library — © Reality Optimizer*
