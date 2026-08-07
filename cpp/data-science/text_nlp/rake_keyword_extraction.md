# rake keyword extraction

**Language:** C++ · **Oracle sphere:** data-science (this file is the C++ twin) · **Category:** Text / NLP

## What it does

rake_keyword_extraction.cpp — RAKE-style keyword extraction.

## Guarantee

When it runs, rake keyword extraction guarantees not any((w in extractor.stopwords for w in phrase)); all((v >= 0 for v in word_scores.values())); keywords == sorted(keywords, key=lambda x: x[1], reverse=True) (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `len(phrases) > 0`
- `all((isinstance(p, list) for p in phrases))`
- `all((all((isinstance(w, str) for w in p)) for p in phrases))`
- `not any((w in extractor.stopwords for w in phrase))`
- `len(word_scores) > 0`
- `all((v >= 0 for v in word_scores.values()))`
- `len(keywords) <= 5`
- `all((isinstance(k, str) and isinstance(s, float) for k, s in keywords))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class RAKEExtractor:`, `def __init__(self, stopwords: Set[str] = None):`, `def _tokenize(self, text: str) -> List[str]:`, `def extract_phrases(self, text: str) -> List[List[str]]:`, `def compute_word_scores(self, phrases: List[List[str]]) -> Dict[str, float]:`, `def score_phrases(self, phrases: List[List[str]], word_scores: Dict[str, float]) -> List[Tuple[str, float]]:`, `def extract_keywords(self, text: str, top_k: int = 5) -> List[Tuple[str, float]]:`
**Valid input:** `text` is a string; `stopwords` is a set of lowercase strings; `top_k` is a non-negative integer.
**Core:** RAKE-style keyword extraction: splits text into stopword-delimited phrases, scores each word by `(degree + 1) / (frequency + 1)`, and ranks candidate phrases by summed word scores.
**Assert:** Phrases are lists of non-stopword strings; word scores are non-negative; `extract_keywords` returns at most `top_k` `(phrase, score)` tuples sorted descending; high-frequency technical terms such as "learning" rank in the top-k for the demo text; empty text returns no keywords.
**⚠️ Defect:** The word-score formula is not the original RAKE degree/frequency ratio (degree should be co-occurrence count, not unique neighbors). Stopwords list is hardcoded and small, so domain terms that happen to match it are discarded. Multi-word phrase quality depends entirely on the arbitrary stopword set.

---
*△ AURA Pattern Library — © Reality Optimizer*
