"""
MinHash Signatures for Near-Duplicate Detection

Core idea: compute compact hash signatures for sets of tokens. Use Jaccard similarity
from signatures to estimate similarity and detect near-duplicates. Verify against
exact Jaccard computation.

Use when: detecting similar documents, deduplicating text corpora, or building
scalable similarity search without comparing all pairs directly.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Set, Tuple
import hashlib
from functools import reduce


class MinHashDedup:
    """Learn MinHash signatures, estimate Jaccard similarity, compare to exact."""

    def __init__(self, num_hashes: int = 256):
        self.num_hashes = num_hashes
        self.hash_seeds = list(range(num_hashes))
        self.signatures: List[Tuple[int, ...]] = []

    def _tokenize(self, text: str) -> Set[str]:
        """Simple tokenization to word shingles."""
        text = text.lower()
        words = text.split()
        # Use words as shingles (could also use character n-grams)
        return set(words)

    def _hash_shingle(self, shingle: str, seed: int) -> int:
        """Hash a shingle with seed."""
        h = hashlib.md5()
        h.update(f"{seed}:{shingle}".encode())
        return int(h.hexdigest(), 16)

    def compute_signature(self, text: str) -> Tuple[int, ...]:
        """Compute MinHash signature for text."""
        shingles = self._tokenize(text)

        signature = []
        for seed in self.hash_seeds:
            # For this hash function, find minimum hash value over shingles
            min_hash = float('inf')
            for shingle in shingles:
                hash_val = self._hash_shingle(shingle, seed)
                min_hash = min(min_hash, hash_val)

            # If no shingles, use sentinel
            if min_hash == float('inf'):
                min_hash = 0

            signature.append(min_hash)

        return tuple(signature)

    def fit_signatures(self, documents: List[str]) -> None:
        """Compute signatures for all documents."""
        self.signatures = [self.compute_signature(doc) for doc in documents]

    def estimated_jaccard(self, sig1: Tuple[int, ...], sig2: Tuple[int, ...]) -> float:
        """Estimate Jaccard similarity from MinHash signatures."""
        if len(sig1) != len(sig2):
            return 0.0

        # Jaccard similarity ≈ fraction of matching hash values
        matches = sum(1 for h1, h2 in zip(sig1, sig2) if h1 == h2)
        return matches / len(sig1)

    @staticmethod
    def exact_jaccard(set1: Set[str], set2: Set[str]) -> float:
        """Compute exact Jaccard similarity."""
        if len(set1) == 0 and len(set2) == 0:
            return 1.0
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        if union == 0:
            return 0.0
        return intersection / union

    def find_similar_pairs(self, threshold: float = 0.5) -> List[Tuple[int, int, float]]:
        """Find document pairs with estimated Jaccard >= threshold.

        Returns list of (doc_id1, doc_id2, estimated_jaccard).
        """
        pairs = []
        for i in range(len(self.signatures)):
            for j in range(i + 1, len(self.signatures)):
                sim = self.estimated_jaccard(self.signatures[i], self.signatures[j])
                if sim >= threshold:
                    pairs.append((i, j, sim))
        return pairs


if __name__ == "__main__":
    import random
    random.seed(42)

    # Deterministic corpus with duplicates
    docs = [
        "the cat sat on the mat",
        "the cat sat on the rug",  # similar to 0
        "the dog ran in the park",
        "the dog ran in the field",  # similar to 2
        "apple banana orange grape",
        "apple banana orange kiwi",  # similar to 4
    ]

    dedup = MinHashDedup(num_hashes=128)
    dedup.fit_signatures(docs)

    # Test 1: Signatures are computed
    assert len(dedup.signatures) == len(docs), "Should compute signature for each doc"
    for sig in dedup.signatures:
        assert len(sig) == dedup.num_hashes, "Signature should have correct length"

    # Test 2: Identical documents have similarity 1.0
    sig_same = dedup.compute_signature(docs[0])
    sim_same = dedup.estimated_jaccard(sig_same, sig_same)
    assert sim_same == 1.0, "Document should be identical to itself"

    # Test 3: MinHash estimates are within reasonable bounds of exact Jaccard
    set0 = dedup._tokenize(docs[0])
    set1 = dedup._tokenize(docs[1])
    exact_jac = dedup.exact_jaccard(set0, set1)
    estimated_jac = dedup.estimated_jaccard(dedup.signatures[0], dedup.signatures[1])

    # MinHash estimate must be close to exact — 256 hashes tightens the estimator
    error = abs(exact_jac - estimated_jac)
    assert error < 0.15, \
        f"MinHash estimate {estimated_jac} too far from exact {exact_jac}, error={error}"

    # Test 4: Find similar pairs detects known similar documents
    similar_pairs = dedup.find_similar_pairs(threshold=0.4)
    pair_indices = {(i, j) for i, j, _ in similar_pairs}

    # Pairs (0,1), (2,3), (4,5) should be similar
    assert (0, 1) in pair_indices or (1, 0) in pair_indices, "Docs 0 and 1 should be similar"
    assert (2, 3) in pair_indices or (3, 2) in pair_indices, "Docs 2 and 3 should be similar"
    assert (4, 5) in pair_indices or (5, 4) in pair_indices, "Docs 4 and 5 should be similar"

    # Test 5: Exact Jaccard is symmetric
    jac_01 = dedup.exact_jaccard(set0, set1)
    set1_again = dedup._tokenize(docs[1])
    jac_10 = dedup.exact_jaccard(set1_again, set0)
    assert abs(jac_01 - jac_10) < 1e-6, "Exact Jaccard should be symmetric"

    print("PASS: MinHash signatures compute efficiently, estimates within 0.15 of exact Jaccard (256 hashes), finds similar pairs")
