"""
Bag-of-Words Vectorizer

Core idea: represent each document as a sparse count vector of word frequencies.
Build a shared vocabulary from all documents, then encode each document as counts
over that vocabulary. Useful for baseline text representation before more complex methods.

Use when: you need a simple baseline text representation, want to measure document
similarity by raw term overlap, or need feature vectors for ML classifiers.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Dict, List, Tuple
from collections import defaultdict
import re


class BagOfWordsVectorizer:
    """Learns vocabulary and converts documents to count vectors."""

    def __init__(self):
        self.vocab: Dict[str, int] = {}  # word -> word_id
        self.vocab_size: int = 0

    def _tokenize(self, text: str) -> List[str]:
        """Simple word tokenization: lowercase, alphanumeric words."""
        text = text.lower()
        words = re.findall(r'\b[a-z]+\b', text)
        return words

    def build_vocabulary(self, documents: List[str]) -> None:
        """Learn vocabulary from documents."""
        vocab_set = set()
        for doc in documents:
            words = self._tokenize(doc)
            vocab_set.update(words)
        # Sort for determinism
        for word in sorted(vocab_set):
            self.vocab[word] = len(self.vocab)
        self.vocab_size = len(self.vocab)

    def vectorize(self, text: str) -> Dict[int, int]:
        """Convert document text to sparse word-count vector: {word_id -> count}."""
        vector = defaultdict(int)
        words = self._tokenize(text)
        for word in words:
            if word in self.vocab:
                word_id = self.vocab[word]
                vector[word_id] += 1
        return dict(vector)

    def get_vector_dense(self, text: str) -> List[int]:
        """Return dense vector (vocab_size,) with word counts."""
        vec = self.vectorize(text)
        dense = [0] * self.vocab_size
        for word_id, count in vec.items():
            dense[word_id] = count
        return dense


def cosine_similarity(vec1: List[int], vec2: List[int]) -> float:
    """Cosine similarity between two dense count vectors."""
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
        "The cat sat on the mat",
        "The dog played in the park",
        "Cats and dogs are pets",
        "The mat was comfortable",
        "Parks are good for dogs",
    ]

    # Build vectorizer
    vec = BagOfWordsVectorizer()
    vec.build_vocabulary(corpus)

    # Vectorize all documents
    vectors = [vec.get_vector_dense(doc) for doc in corpus]

    # Test 1: similar documents should have higher cosine similarity
    sim_0_1 = cosine_similarity(vectors[0], vectors[1])
    sim_0_3 = cosine_similarity(vectors[0], vectors[3])
    sim_0_4 = cosine_similarity(vectors[0], vectors[4])

    # Document 0 ("The cat sat on the mat") and 3 ("The mat was comfortable")
    # share "the" and "mat", so should be more similar than 0 and 4
    assert sim_0_3 > sim_0_4, f"Expected sim(0,3)={sim_0_3} > sim(0,4)={sim_0_4}"

    # Test 2: vocabulary built correctly
    assert "cat" in vec.vocab
    assert "dog" in vec.vocab
    assert len(vec.vocab) > 0

    # Test 3: vectorize returns valid counts
    test_vec = vec.vectorize("cat cat dog")
    assert test_vec[vec.vocab["cat"]] == 2, "Cat count should be 2"
    assert test_vec[vec.vocab["dog"]] == 1, "Dog count should be 1"

    print("PASS: Bag-of-Words vectorizer learns vocabulary, encodes documents as count vectors, similar docs rank higher")
