# Batch 23 — DS Pattern Detail Docs (18 patterns)

Categories: `text_nlp` (10) + `text_nlp_ii` (8). Final batch of the Python DS sphere.

---

## Category: text_nlp

### 1. bag_of_words.py
**Entry fn:** `class BagOfWordsVectorizer:`, `def __init__(self):`, `def _tokenize(self, text: str) -> List[str]:`, `def build_vocabulary(self, documents: List[str]) -> None:`, `def vectorize(self, text: str) -> Dict[int, int]:`, `def get_vector_dense(self, text: str) -> List[int]:`, `def cosine_similarity(vec1: List[int], vec2: List[int]) -> float:`
**Valid input:** `documents` is a list/iterable of strings containing alphanumeric words; `text` is a string after vocabulary is built.
**Core:** Learns a sorted vocabulary from the corpus and encodes each document as either a sparse `{word_id: count}` dict or a dense count vector. Also exposes a dense-vector cosine similarity helper for baseline document similarity.
**Assert:** Vocabulary contains expected words such as "cat" and "dog"; "cat cat dog" vectorizes to counts 2 and 1; a mat-related doc is more similar to another mat-related doc than to a dog-park doc.
**⚠️ Defect:** No handling of out-of-vocabulary words during `vectorize` (they are silently dropped). `cosine_similarity` does not validate equal length or non-empty vectors, so mismatched lengths raise an opaque index error and zero vectors divide by zero (returns 0.0 only because of the guard, which is fine, but no warning).

### 2. bpe_tokenizer_lite.py
**Entry fn:** `class BPETokenizer:`, `def __init__(self, vocab_size: int = 100):`, `def _get_word_frequencies(self, text: str) -> Dict[Tuple[str, ...], int]:`, `def learn_merges(self, text: str, num_merges: int = None) -> None:`, `def encode(self, text: str) -> List[int]:`, `def decode(self, token_ids: List[int]) -> str:`
**Valid input:** `text` is a lowercase-able ASCII string containing words matching `\b[a-z]+\b`; `vocab_size` is a positive integer; `num_merges` defaults to `vocab_size - 256`.
**Core:** Simplified byte-pair encoding: learns the most frequent character/bigram merges from a corpus, builds a vocabulary, encodes new text to token IDs, and decodes IDs back to a space-separated approximation of the original.
**Assert:** `learn_merges` produces a non-empty vocab and merge list; `encode` returns a list of ints; `decode` returns a non-empty string; the same word encodes identically across two calls.
**⚠️ Defect:** Tokenization drops all non-alphabetic tokens, numbers, punctuation, and mixed-case words. If `num_merges` exceeds available pairs the loop simply breaks, but the default formula `vocab_size - 256` can be negative for small `vocab_size`. Decode strips `</w>` into spaces, which can mis-recover word order and spacing.

### 3. cosine_similarity_search.py
**Entry fn:** `class SimpleSearchEngine:`, `def __init__(self):`, `def _tokenize(self, text: str) -> List[str]:`, `def index(self, documents: List[str]) -> None:`, `def _get_tfidf_vector(self, text: str) -> Dict[int, float]:`, `def _cosine_similarity(self, vec1: Dict[int, float], vec2: Dict[int, float]) -> float:`, `def search(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:`
**Valid input:** `documents` is a list of strings; `query` is a string; `top_k` is a non-negative integer.
**Core:** Builds a TF-IDF index over a corpus and ranks documents by cosine similarity to a free-text query. Returns the top-k `(document, score)` tuples.
**Assert:** Query "machine learning" ranks the two ML-related documents highest; query "python" returns the Python doc first; exact-query search returns the same document with score > 0.9.
**⚠️ Defect:** The private `_cosine_similarity` is not normalized by document length in any length-biased way; it uses raw term-frequency times IDF, so longer documents can dominate unless the query is also long. No validation that `documents` is non-empty before `index` is called; an empty corpus leaves IDF dictionaries empty and search silently returns `[]`.

### 4. edit_distance.py
**Entry fn:** `class EditDistanceDP:`, `def distance(s1: str, s2: str) -> int:`, `def backtrace(s1: str, s2: str) -> List[Tuple[str, str, str]]:`
**Valid input:** `s1` and `s2` are strings.
**Core:** Computes Levenshtein edit distance via dynamic programming and optionally back-traces the DP table to recover the sequence of match/replace/insert/delete operations.
**Assert:** `distance("kitten", "sitting") == 3`; `distance("", "abc") == 3`; `distance("abc", "abc") == 0`; backtrace on "cat" → "car" produces a valid edit sequence that transforms `s1` into `s2`.
**⚠️ Defect:** `distance` and `backtrace` duplicate the DP computation; `backtrace` could reuse a cached table. The backtrace tie-breaking is implicit (the `elif` order), so when multiple optimal paths exist it returns one arbitrary path without documenting the tie-breaking rule.

### 5. markov_chain_text.py
**Entry fn:** `class MarkovChainText:`, `def __init__(self, order: int = 1):`, `def _tokenize(self, text: str) -> List[str]:`, `def fit(self, documents: List[str]) -> None:`, `def generate(self, max_length: int = 20, seed_context: Tuple[str, ...] = None) -> str:`, `def get_transition_counts(self) -> Dict[Tuple[str, ...], Dict[str, int]]:`, `def sanity_check(self) -> Tuple[bool, str]:`
**Valid input:** `documents` is a list of strings; `order` is a positive integer; `seed_context` is a tuple of length `order`.
**Core:** Word-level Markov chain: learns conditional transition counts for n-grams of the requested order and generates text by sampling from observed next-word lists.
**Assert:** After fitting a small corpus, transitions are non-empty, sanity check passes, START transitions exist, every transition count is positive, and generated text is a non-empty string without the internal `<START>` marker.
**⚠️ Defect:** Generation uses `random.choice` on the observed next-word list, which samples with replacement relative to raw occurrence counts but is not the same as normalized probability sampling with smoothing. Unseen contexts cause generation to stop early. `sanity_check` only validates structure, not that probabilities sum to one.

### 6. minhash_dedup.py
**Entry fn:** `class MinHashDedup:`, `def __init__(self, num_hashes: int = 256):`, `def _tokenize(self, text: str) -> Set[str]:`, `def _hash_shingle(self, shingle: str, seed: int) -> int:`, `def compute_signature(self, text: str) -> Tuple[int, ...]:`, `def fit_signatures(self, documents: List[str]) -> None:`, `def estimated_jaccard(self, sig1: Tuple[int, ...], sig2: Tuple[int, ...]) -> float:`, `def exact_jaccard(set1: Set[str], set2: Set[str]) -> float:`, `def find_similar_pairs(self, threshold: float = 0.5) -> List[Tuple[int, int, float]]:`
**Valid input:** `documents` is a list of strings; `num_hashes` is a positive integer; `threshold` ∈ [0, 1].
**Core:** Computes MinHash signatures using MD5-based permutations, estimates Jaccard similarity from signature collision rate, and finds near-duplicate document pairs above a threshold. Also exposes exact Jaccard for validation.
**Assert:** A document compared to itself has estimated Jaccard 1.0; exact Jaccard is symmetric; the three planted near-duplicate pairs are detected with 128 hashes; the MinHash estimate is within 0.15 of exact Jaccard for word-shingle sets.
**⚠️ Defect:** `_hash_shingle` uses MD5, which is unnecessary for a non-cryptographic MinHash and slower than integer hashing. `_tokenize` treats whitespace-split words as shingles, so punctuation and case variations produce different shingles. The `estimated_jaccard` returns 0.0 for mismatched signature lengths instead of raising.

### 7. ngram_language_model.py
**Entry fn:** `class NGramLanguageModel:`, `def __init__(self, n: int = 2):`, `def _tokenize(self, text: str) -> List[str]:`, `def fit(self, documents: List[str]) -> None:`, `def get_probability(self, context: Tuple[str, ...], token: str) -> float:`, `def perplexity(self, text: str) -> float:`, `def sample(self, num_tokens: int = 10, seed_context: Tuple[str, ...] = None) -> str:`
**Valid input:** `documents` is a list of strings; `n` ≥ 1; `text` is a string using the learned vocabulary.
**Core:** Count-based n-gram language model with add-one (Laplace) smoothing. Computes conditional probabilities, perplexity on held-out text, and can sample a continuation from a seed context.
**Assert:** Vocabulary includes `<s>`, `cat`, `dog`; probabilities over the vocabulary sum to ~1.0 for a given context; common tokens have higher probability than rare unknown tokens; training-text perplexity is lower than random-text perplexity; sampling returns a non-empty string.
**⚠️ Defect:** Add-one smoothing is aggressive for large vocabularies and can drastically flatten probabilities. `sample` silently falls back to the alphabetically first token if cumulative-sum rounding causes `chosen_token` to remain `None`, which biases sampling. No handling of unseen contexts outside the initial `<s>` padding.

### 8. rake_keyword_extraction.py
**Entry fn:** `class RAKEExtractor:`, `def __init__(self, stopwords: Set[str] = None):`, `def _tokenize(self, text: str) -> List[str]:`, `def extract_phrases(self, text: str) -> List[List[str]]:`, `def compute_word_scores(self, phrases: List[List[str]]) -> Dict[str, float]:`, `def score_phrases(self, phrases: List[List[str]], word_scores: Dict[str, float]) -> List[Tuple[str, float]]:`, `def extract_keywords(self, text: str, top_k: int = 5) -> List[Tuple[str, float]]:`
**Valid input:** `text` is a string; `stopwords` is a set of lowercase strings; `top_k` is a non-negative integer.
**Core:** RAKE-style keyword extraction: splits text into stopword-delimited phrases, scores each word by `(degree + 1) / (frequency + 1)`, and ranks candidate phrases by summed word scores.
**Assert:** Phrases are lists of non-stopword strings; word scores are non-negative; `extract_keywords` returns at most `top_k` `(phrase, score)` tuples sorted descending; high-frequency technical terms such as "learning" rank in the top-k for the demo text; empty text returns no keywords.
**⚠️ Defect:** The word-score formula is not the original RAKE degree/frequency ratio (degree should be co-occurrence count, not unique neighbors). Stopwords list is hardcoded and small, so domain terms that happen to match it are discarded. Multi-word phrase quality depends entirely on the arbitrary stopword set.

### 9. tfidf_vectorizer.py
**Entry fn:** `class TFIDFVectorizer:`, `def __init__(self, smooth_idf: bool = True):`, `def _tokenize(self, text: str) -> List[str]:`, `def fit(self, documents: List[str]) -> None:`, `def transform(self, text: str) -> Dict[int, float]:`, `def get_dense_vector(self, text: str) -> List[float]:`, `def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:`
**Valid input:** `documents` is a non-empty list of strings; `text` is a string after fitting.
**Core:** Learns IDF weights from a corpus (with optional smoothing), converts text to sparse or dense TF-IDF vectors, and provides a cosine-similarity helper for ranking and retrieval.
**Assert:** A term appearing in many documents (e.g., "apple") has lower IDF than a term appearing in few documents (e.g., "date"); documents sharing exclusive terms have higher cosine similarity than dissimilar documents; a query containing a rare term ranks documents containing that term above documents that do not.
**⚠️ Defect:** `fit` requires `documents` to be non-empty to compute IDF; calling `transform` before `fit` produces an empty vector because `vocab` and `idf` are uninitialized. The standalone `cosine_similarity` function does not validate equal-length vectors, so mismatched dense vectors raise a runtime index error.

### 10. viterbi_hmm.py
**Entry fn:** `class SimpleHMM:`, `def __init__(self):`, `def viterbi(self, observations: List[str]) -> Tuple[float, List[str]]:`, `def brute_force_best_path(self, observations: List[str]) -> Tuple[float, List[str]]:`, `def enumerate_paths(obs_idx: int, current_seq: List[str], current_log_prob: float):`
**Valid input:** `observations` is a list of observation strings that are keys in the toy emission table.
**Core:** Viterbi decoding for a toy two-state HMM (NOUN/VERB) with hand-specified start, transition, and emission probabilities. Returns the log probability of the most likely state sequence and the sequence itself. Includes a brute-force enumerator for verification on short sequences.
**Assert:** Viterbi log probability and path match brute-force enumeration for all planted test cases; path length equals observation length; every state in the path is valid; single-observation inputs match brute force.
**⚠️ Defect:** The model probabilities and observation vocabulary are hardcoded in `__init__`, so the class cannot be reused for other HMMs. `enumerate_paths` is a nested helper that accumulates paths exponentially and is only practical for very short observation sequences. Missing observations use a tiny `1e-10` emission probability without raising.

---

## Category: text_nlp_ii

### 11. char_ngram_language_id.py
**Entry fn:** `def char_bigrams(text: str) -> Dict[str, int]:`, `def ngram_distance(bigrams1: Dict[str, int], bigrams2: Dict[str, int]) -> float:`
**Valid input:** `text` is a string of length ≥ 2; `bigrams1`/`bigrams2` are dictionaries mapping bigram strings to positive counts.
**Core:** Extracts character bigram frequency profiles and compares them with normalized L1 distance. Enables simple language/dialect discrimination by profile similarity.
**Assert:** English-like text is closer to an English bigram profile than to a pseudo-random character profile; distance is symmetric.
**⚠️ Defect:** `ngram_distance` does not handle empty profiles except by returning `inf` when one total is zero; two empty texts would also return `inf`. It uses L1 distance on normalized counts, which is valid but does not account for bigram rank or top-N out-of-vocabulary robustness.

### 12. naive_bayes_complement.py
**Entry fn:** `def naive_bayes_fit(docs: List[List[str]], labels: List[int]):`, `def naive_bayes_predict(doc, loglik, logprior, vocab) -> int:`, `def complement_nb_fit(docs: List[List[str]], labels: List[int]):`, `def complement_nb_predict(doc, comp_weights, vocab) -> int:`, `def minority_recall(predict) -> float:`
**Valid input:** `docs` is a list of tokenized documents (list of string lists); `labels` is a list of integer class IDs aligned with `docs`; `doc` is a tokenized document; `loglik`/`logprior`/`comp_weights` are the fitted NB/CNB model outputs; `vocab` is the set/vocabulary returned by fit.
**Core:** Compares vanilla multinomial Naive Bayes against Complement Naive Bayes. Vanilla NB uses `log P(c) + Σ log P(w|c)`, which can be biased toward the majority class on imbalanced data. CNB scores each class by how poorly the document fits the complement of that class (all other classes) and omits the class prior, reducing majority bias.
**Assert:** On an imbalanced 90/10 training set, the ambiguous document `["good", "bad"]` is classified as the majority class by vanilla NB and as the minority class by CNB; CNB minority recall exceeds vanilla NB minority recall; both classifiers correctly label clear minority-class documents.
**⚠️ Defect:** `minority_recall` is defined inside `if __name__ == "__main__"`, so it is not a reusable top-level entry point despite appearing in the signature list. `naive_bayes_predict` and `complement_nb_predict` take `doc` without a type annotation and silently ignore out-of-vocabulary tokens. The demonstration test set and imbalance ratio are hardcoded in the main block.

### 13. porter_stemmer_lite.py
**Entry fn:** `def porter_stem_lite(word: str) -> str:`
**Valid input:** `word` is a string.
**Core:** Simplified rule-based Porter stemmer that strips common English suffixes (-s, -es, -ies, -ing, -ed, -ational, -tional, -ly, -ness) and performs minor orthographic fixes.
**Assert:** Planted pairs stem as expected: "running" → "runn", "runs" → "run", "ponies" → "poni", "caresses" → "caress", "organizational" → "organize", "happiness" → "happi", "slowly" → "slow".
**⚠️ Defect:** The implementation covers only a tiny subset of Porter's steps and conditions; many valid English words will be under-stemmed or over-stemmed. It does not handle the consonant/vowel measure (`m`) that the full Porter algorithm uses to decide when suffix removal is safe, so words like "ational" in other contexts may be over-truncated.

### 14. sentence_boundary_detection.py
**Entry fn:** `def split_sentences(text: str) -> List[str]:`
**Valid input:** `text` is a string containing sentence-ending punctuation and optional abbreviations.
**Core:** Splits text into sentences at `.`, `!`, or `?` when the punctuation is followed by a space or end of text, while protecting a small hardcoded set of abbreviations (`Dr`, `Mr`, `Mrs`, `Ms`, `Prof`, `St`, `Ave`, `Inc`, `Ltd`, `vs`, `etc`).
**Assert:** "Hello world. This is a test. How are you?" splits into 3 sentences; "Dr. Smith went home. He was tired." splits into 2 sentences with the abbreviation kept intact; two abbreviations in one sentence do not cause spurious splits.
**⚠️ Defect:** The abbreviation set is tiny and English-centric; any abbreviation not in the set triggers a false split. It only checks whether the word stripped of punctuation is in the set, so "Dr" at a real sentence end is also protected. Punctuation followed by a newline rather than a space is not treated as a boundary.

### 15. soundex_phonetic.py
**Entry fn:** `def soundex(name: str) -> str:`
**Valid input:** `name` is a string; empty string is allowed.
**Core:** Computes the classic Soundex phonetic code: first letter + up to three digits derived from consonant classes, removing adjacent duplicate codes and padding to four characters with zeros.
**Assert:** `soundex("Robert") == soundex("Rupert")`; `soundex("Ashcraft") == soundex("Ashcroft")`; `soundex("Alice") != soundex("Bob")`.
**⚠️ Defect:** The simplified implementation does not follow the full Soundex rule that a code assigned to the first letter should be dropped, nor does it always handle adjacent duplicate codes correctly when the first letter maps to a digit. Non-ASCII names and mixed-case input may produce unexpected results.

### 16. textrank_lite.py
**Entry fn:** `def jaccard_similarity(sent1: List[str], sent2: List[str]) -> float:`, `def textrank_sentences(sentences: List[List[str]], damping: float = 0.85, iterations: int = 50) -> List[float]:`
**Valid input:** `sentences` is a list of tokenized sentences (list of string lists); `damping` ∈ [0, 1]; `iterations` > 0.
**Core:** Builds a sentence-similarity graph using Jaccard word overlap and runs the damped PageRank/TextRank power iteration to rank sentences by centrality.
**Assert:** On a three-sentence corpus where the middle sentence shares words with both neighbors (the hub), the hub sentence has the strict highest rank.
**⚠️ Defect:** The graph is fully connected even for very dissimilar sentences, so low-overlap edges still contribute small amounts of weight to every node. The implementation does not provide a convergence threshold; it always runs the fixed number of iterations regardless of whether ranks have stabilized.

### 17. tf_idf_bm25_comparison.py
**Entry fn:** `def tf_idf(docs: List[List[str]], query: List[str]) -> List[float]:`, `def bm25(docs: List[List[str]], query: List[str], k1: float = 1.5, b: float = 0.75) -> List[float]:`
**Valid input:** `docs` is a list of tokenized documents; `query` is a list of query tokens; `k1` > 0; `b` ∈ [0, 1].
**Core:** Compares TF-IDF (linear term-frequency scoring) with Okapi BM25 (dampened, length-normalized term-frequency scoring). BM25 penalizes long documents relative to TF-IDF, reducing length bias in retrieval.
**Assert:** For a short document with high query-term frequency versus a long document with a single query-term occurrence, BM25 ranks the short document higher; TF-IDF may or may not, depending on IDF, but the demo asserts the BM25 ordering.
**⚠️ Defect:** Both functions build IDF on every call instead of caching it across repeated queries over the same corpus. The TF-IDF IDF uses `log(num_docs / (1 + doc_count))`, which is a non-standard smoothing choice and can produce negative scores. BM25 uses the standard Robertson/Sparck-Jones IDF form, which can be negative when a term appears in more than half the documents.

### 18. zipf_law_fit.py
**Entry fn:** `def fit_zipf(word_frequencies: List[int]) -> float:`
**Valid input:** `word_frequencies` is a list of non-negative integers; length ≥ 2.
**Core:** Fits Zipf's law by sorting frequencies in descending order and regressing log(frequency) against log(rank); returns the negative slope.
**Assert:** A Zipf-like distribution yields a slope between 0.5 and 2.0; a uniform distribution yields a slope near 0 (below 0.5).
**⚠️ Defect:** Zero frequencies are replaced with `log(0) = 0`, which distorts the regression for low-frequency or padded rank bins. The regression uses population covariance/variance rather than sample formulas, and it does not return any goodness-of-fit or intercept, only the slope.
