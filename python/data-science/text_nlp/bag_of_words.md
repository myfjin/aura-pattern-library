# bag of words

**Language:** Python · **Sphere:** data-science · **Category:** Text / NLP

**Signature:** `(vec1: List[int], vec2: List[int]) → float`

## What it does

Bag-of-Words Vectorizer

Core idea: represent each document as a sparse count vector of word frequencies.
Build a shared vocabulary from all documents, then encode each document as counts
over that vocabulary. Useful for baseline text representation before more complex methods.

Use when: you need a simple baseline text representation, want to measure document
similarity by raw term overlap, or need feature vectors for ML classifiers.

## Guarantee

When it runs, bag of words guarantees test_vec[vec.vocab['cat']] == 2; sim_0_3 > sim_0_4; 'cat' in vec.vocab (proven by run).

**Checkable constraints:**

- `sim_0_3 > sim_0_4`
- `'cat' in vec.vocab`
- `'dog' in vec.vocab`
- `len(vec.vocab) > 0`
- `test_vec[vec.vocab['cat']] == 2`
- `test_vec[vec.vocab['dog']] == 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class BagOfWordsVectorizer:`, `def __init__(self):`, `def _tokenize(self, text: str) -> List[str]:`, `def build_vocabulary(self, documents: List[str]) -> None:`, `def vectorize(self, text: str) -> Dict[int, int]:`, `def get_vector_dense(self, text: str) -> List[int]:`, `def cosine_similarity(vec1: List[int], vec2: List[int]) -> float:`
**Valid input:** `documents` is a list/iterable of strings containing alphanumeric words; `text` is a string after vocabulary is built.
**Core:** Learns a sorted vocabulary from the corpus and encodes each document as either a sparse `{word_id: count}` dict or a dense count vector. Also exposes a dense-vector cosine similarity helper for baseline document similarity.
**Assert:** Vocabulary contains expected words such as "cat" and "dog"; "cat cat dog" vectorizes to counts 2 and 1; a mat-related doc is more similar to another mat-related doc than to a dog-park doc.
**⚠️ Defect:** No handling of out-of-vocabulary words during `vectorize` (they are silently dropped). `cosine_similarity` does not validate equal length or non-empty vectors, so mismatched lengths raise an opaque index error and zero vectors divide by zero (returns 0.0 only because of the guard, which is fine, but no warning).

---
*△ AURA Pattern Library — © Reality Optimizer*
