"""
Skip-gram word2vec with negative sampling on a tiny built-in corpus.

Core idea: For each target word, predict context words using a learnable embedding
matrix. Use negative sampling: update embeddings to score true context pairs high
and random (context, negative-word) pairs low. Related words (co-occurring in context)
converge to nearby embeddings.

When to use: Word embeddings, unsupervised semantic learning, language modeling,
representation learning fundamentals.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List, Tuple, Set


def sigmoid(x: float) -> float:
    if x < -500:
        return 0.0
    if x > 500:
        return 1.0
    return 1.0 / (1.0 + math.exp(-x))


def cosine_similarity(v1: List[float], v2: List[float]) -> float:
    """Compute cosine similarity between two vectors."""
    dot = sum(v1[i] * v2[i] for i in range(len(v1)))
    norm1 = math.sqrt(sum(x**2 for x in v1)) + 1e-10
    norm2 = math.sqrt(sum(x**2 for x in v2)) + 1e-10
    return dot / (norm1 * norm2)


class SkipgramNegativeSampling:
    def __init__(self, vocab_size: int, embedding_dim: int = 8, lr: float = 0.1):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.lr = lr

        # Embedding matrix: vocab_size x embedding_dim
        self.W = [[random.gauss(0, 0.1) for _ in range(embedding_dim)]
                  for _ in range(vocab_size)]

    def forward(self, target_word: int, context_word: int) -> float:
        """Compute score (probability target predicts context) via dot product."""
        dot = sum(self.W[target_word][i] * self.W[context_word][i]
                  for i in range(self.embedding_dim))
        return sigmoid(dot)

    def update(self, target_word: int, context_word: int, label: float):
        """Update embeddings. label=1 for positive pairs, 0 for negative."""
        score = self.forward(target_word, context_word)
        error = score - label

        # Gradient flows to both embeddings
        for i in range(self.embedding_dim):
            grad = error * self.W[context_word][i]
            self.W[target_word][i] -= self.lr * grad

            grad = error * self.W[target_word][i]
            self.W[context_word][i] -= self.lr * grad

    def train_pair(self, target_word: int, context_word: int, negatives: List[int]):
        """Train on one positive pair and K negative samples."""
        # Positive pair
        self.update(target_word, context_word, label=1.0)

        # Negative pairs
        for neg_word in negatives:
            self.update(target_word, neg_word, label=0.0)


if __name__ == "__main__":
    random.seed(42)

    # Tiny corpus (vocab)
    # Related words: (dog, cat, animal), (king, queen, royal), (good, bad)
    vocab = ["dog", "cat", "animal", "king", "queen", "royal", "good", "bad", "the", "a"]
    word2id = {w: i for i, w in enumerate(vocab)}
    vocab_size = len(vocab)

    # Training pairs (target, context) that co-occur
    pairs = [
        ("dog", "animal"), ("dog", "cat"),
        ("cat", "animal"), ("cat", "dog"),
        ("animal", "dog"), ("animal", "cat"),
        ("king", "queen"), ("king", "royal"),
        ("queen", "king"), ("queen", "royal"),
        ("royal", "king"), ("royal", "queen"),
        ("good", "bad"),
        ("bad", "good"),
    ]

    # Train
    model = SkipgramNegativeSampling(vocab_size=vocab_size, embedding_dim=8, lr=0.1)

    for epoch in range(100):
        for target_word_str, context_word_str in pairs:
            target_id = word2id[target_word_str]
            context_id = word2id[context_word_str]

            # Negative sampling: sample K random negatives
            negatives = []
            for _ in range(3):
                neg_id = random.randint(0, vocab_size - 1)
                if neg_id not in (target_id, context_id):
                    negatives.append(neg_id)

            model.train_pair(target_id, context_id, negatives)

    # Evaluate: related words should have high cosine similarity
    print("Cosine similarities:")
    test_pairs = [
        ("dog", "cat"),
        ("dog", "animal"),
        ("king", "queen"),
        ("king", "royal"),
        ("good", "bad"),
        ("dog", "king"),  # unrelated
        ("cat", "queen"),  # unrelated
    ]

    similarities = []
    for w1_str, w2_str in test_pairs:
        w1_id = word2id[w1_str]
        w2_id = word2id[w2_str]
        sim = cosine_similarity(model.W[w1_id], model.W[w2_id])
        similarities.append(sim)
        print(f"  {w1_str:10} <-> {w2_str:10}: {sim:.4f}")

    # Check: related pairs (first 5) should have higher similarity than unrelated (last 2)
    related_sims = similarities[:5]
    unrelated_sims = similarities[5:]

    avg_related = sum(related_sims) / len(related_sims)
    avg_unrelated = sum(unrelated_sims) / len(unrelated_sims)

    print(f"\nAvg similarity (related): {avg_related:.4f}")
    print(f"Avg similarity (unrelated): {avg_unrelated:.4f}")

    assert avg_related > avg_unrelated, \
        f"Related similarity {avg_related} not > unrelated {avg_unrelated}"

    print("PASS")
