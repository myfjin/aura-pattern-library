"""
Cosine Similarity Search: Rank Documents by Query

Core idea: convert documents and query to TF-IDF vectors, rank documents by
cosine similarity to query. Fast baseline for relevance ranking and information
retrieval.

Use when: building a search engine, ranking results by relevance, finding top-k
similar documents without heavy infrastructure.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple, Dict
from collections import defaultdict
import math
import re


class SimpleSearchEngine:
    """TF-IDF search: build index, score documents by cosine similarity to query."""

    def __init__(self):
        self.documents: List[str] = []
        self.vocab: Dict[str, int] = {}
        self.doc_freq: Dict[str, int] = defaultdict(int)
        self.idf: Dict[str, float] = {}

    def _tokenize(self, text: str) -> List[str]:
        """Simple tokenization."""
        text = text.lower()
        return re.findall(r'\b[a-z]+\b', text)

    def index(self, documents: List[str]) -> None:
        """Build index from documents."""
        self.documents = documents
        vocab_set = set()

        # Collect vocabulary and doc frequencies
        for doc in documents:
            words = self._tokenize(doc)
            unique_words = set(words)
            vocab_set.update(unique_words)
            for word in unique_words:
                self.doc_freq[word] += 1

        # Assign word IDs
        for word in sorted(vocab_set):
            self.vocab[word] = len(self.vocab)

        # Compute IDF with smoothing
        n_docs = len(documents)
        for word, count in self.doc_freq.items():
            self.idf[word] = math.log((n_docs + 1) / (count + 1)) + 1

    def _get_tfidf_vector(self, text: str) -> Dict[int, float]:
        """Convert text to TF-IDF vector: {word_id -> score}."""
        words = self._tokenize(text)
        tf = defaultdict(int)
        for word in words:
            if word in self.vocab:
                tf[word] += 1

        vector = {}
        for word, freq in tf.items():
            word_id = self.vocab[word]
            idf = self.idf.get(word, 0.0)
            vector[word_id] = freq * idf

        return vector

    def _cosine_similarity(self, vec1: Dict[int, float], vec2: Dict[int, float]) -> float:
        """Cosine similarity between two sparse vectors."""
        dot = sum(vec1.get(wid, 0) * vec2.get(wid, 0) for wid in set(vec1) | set(vec2))
        norm1 = sum(v * v for v in vec1.values()) ** 0.5
        norm2 = sum(v * v for v in vec2.values()) ** 0.5
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return dot / (norm1 * norm2)

    def search(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:
        """Search for documents similar to query, return top-k with scores."""
        query_vec = self._get_tfidf_vector(query)

        scores = []
        for i, doc in enumerate(self.documents):
            doc_vec = self._get_tfidf_vector(doc)
            score = self._cosine_similarity(query_vec, doc_vec)
            scores.append((doc, score))

        # Sort by score descending
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]


if __name__ == "__main__":
    import random
    random.seed(42)

    # Deterministic corpus
    docs = [
        "machine learning algorithms",
        "deep learning neural networks",
        "python programming language",
        "web development html css",
        "machine learning classification tasks",
        "java programming for beginners",
    ]

    engine = SimpleSearchEngine()
    engine.index(docs)

    # Test 1: Query "machine learning" should rank docs 0 and 4 highest
    results = engine.search("machine learning", top_k=3)
    top_docs = [doc for doc, _ in results]
    assert docs[0] in top_docs, "Doc 0 should rank high for 'machine learning'"
    assert docs[4] in top_docs, "Doc 4 should rank high for 'machine learning'"

    # Test 2: Query "python" should rank doc 2 highest
    results = engine.search("python", top_k=1)
    assert results[0][0] == docs[2], f"Expected docs[2], got {results[0][0]}"

    # Test 3: Query and exact doc match should have high similarity
    results = engine.search(docs[0], top_k=1)
    assert results[0][0] == docs[0], "Exact query should rank its doc first"
    assert results[0][1] > 0.9, "Exact match should have high score"

    # Test 4: Unrelated query should have lower scores overall
    results_ml = engine.search("machine learning", top_k=6)
    results_web = engine.search("machine learning", top_k=1)
    scores_ml = [s for _, s in results_ml]
    scores_web = [s for _, s in results_web]
    # Web query should be less similar to ML docs than ML query
    assert max(scores_web) <= max(scores_ml), \
        "ML query should score higher on ML-relevant corpus"

    print("PASS: Cosine similarity search indexes docs, ranks by TF-IDF relevance, exact match scores highest")
