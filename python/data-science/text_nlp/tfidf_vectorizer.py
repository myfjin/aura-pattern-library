"""
TF-IDF Vectorizer

Core idea: weight term frequencies by inverse document frequency to emphasize
distinctive terms. TF-IDF(t,d) = freq(t in d) * log(N / doc_count(t)). Common
baseline for document ranking and similarity.

Use when: ranking documents by relevance to a query, finding similar documents,
or preparing text for ML classifiers where term importance matters.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Dict, List
from collections import defaultdict
import math
import re


class TFIDFVectorizer:
    """Learn IDF weights from corpus, compute TF-IDF vectors."""

    def __init__(self, smooth_idf: bool = True):
        self.idf: Dict[str, float] = {}
        self.smooth_idf = smooth_idf
        self.vocab: Dict[str, int] = {}
        self.vocab_size: int = 0
        self.doc_count: int = 0

    def _tokenize(self, text: str) -> List[str]:
        """Simple tokenization."""
        text = text.lower()
        return re.findall(r'\b[a-z]+\b', text)

    def fit(self, documents: List[str]) -> None:
        """Learn IDF weights and build vocabulary."""
        self.doc_count = len(documents)
        doc_word_set = []

        # Build vocabulary and track doc frequency
        doc_freq = defaultdict(int)
        for doc in documents:
            words = self._tokenize(doc)
            unique_words = set(words)
            doc_word_set.append(unique_words)
            for word in unique_words:
                doc_freq[word] += 1

        # Assign word IDs
        for word in sorted(doc_freq.keys()):
            self.vocab[word] = len(self.vocab)

        self.vocab_size = len(self.vocab)

        # Compute IDF
        for word, count in doc_freq.items():
            # Smooth IDF: add 1 to numerator and denominator
            if self.smooth_idf:
                self.idf[word] = math.log((self.doc_count + 1) / (count + 1)) + 1
            else:
                self.idf[word] = math.log(self.doc_count / count)

    def transform(self, text: str) -> Dict[int, float]:
        """Convert text to sparse TF-IDF vector: {word_id -> tfidf_value}."""
        words = self._tokenize(text)
        tf = defaultdict(int)
        for word in words:
            if word in self.vocab:
                tf[word] += 1

        # Compute TF-IDF
        tfidf = {}
        for word, freq in tf.items():
            word_id = self.vocab[word]
            idf = self.idf.get(word, 0.0)
            tfidf[word_id] = freq * idf

        return tfidf

    def get_dense_vector(self, text: str) -> List[float]:
        """Return dense TF-IDF vector."""
        sparse = self.transform(text)
        dense = [0.0] * self.vocab_size
        for word_id, value in sparse.items():
            dense[word_id] = value
        return dense


def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """Cosine similarity between two TF-IDF vectors."""
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = sum(x * x for x in vec1) ** 0.5
    norm2 = sum(x * x for x in vec2) ** 0.5
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)


if __name__ == "__main__":
    import random
    random.seed(42)

    # Deterministic corpus
    corpus = [
        "apple banana cherry",
        "apple apple orange",
        "banana cherry date",
        "date fig grape",
        "grape apple fruit",
    ]

    # Fit TF-IDF
    tfidf = TFIDFVectorizer(smooth_idf=True)
    tfidf.fit(corpus)

    # Vectorize documents
    vectors = [tfidf.get_dense_vector(doc) for doc in corpus]

    # Test 1: "apple" should have lower IDF (appears in many docs)
    # "date" should have higher IDF (appears in fewer docs)
    assert tfidf.idf.get("apple", 0) < tfidf.idf.get("date", 0), \
        f"apple IDF {tfidf.idf.get('apple')} should be < date IDF {tfidf.idf.get('date')}"

    # Test 2: Documents with more exclusive terms should rank closer
    # Document 0 ("apple banana cherry") vs 3 ("date fig grape") are dissimilar
    # Document 0 vs 1 ("apple apple orange") should be more similar (both have apple)
    sim_0_1 = cosine_similarity(vectors[0], vectors[1])
    sim_0_3 = cosine_similarity(vectors[0], vectors[3])
    assert sim_0_1 > sim_0_3, f"Expected sim(0,1)={sim_0_1} > sim(0,3)={sim_0_3}"

    # Test 3: Query "apple" should rank docs with apple highest
    query_vec = tfidf.get_dense_vector("apple")
    sims = [cosine_similarity(query_vec, v) for v in vectors]
    # Docs 0, 1, 4 contain apple; doc 2, 3 do not
    assert sims[0] > sims[2], "Doc with apple should rank above doc without"
    assert sims[1] > sims[3], "Doc with apple should rank above doc without"

    print("PASS: TF-IDF vectorizer learns IDF, ranks distinctive terms higher, queries match relevant documents")
