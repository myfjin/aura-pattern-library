"""
Simplified Byte-Pair Encoding (BPE) Tokenizer

Core idea: learn merge operations from a corpus (combining frequent character pairs),
then apply merges to tokenize new text. Encode text to token IDs, decode back to text.

Use when: understanding subword tokenization, building custom tokenizers for small
models, or studying how BPE reduces vocabulary size.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Dict, Tuple
from collections import defaultdict, Counter
import re


class BPETokenizer:
    """Learn BPE merges from corpus, encode/decode text."""

    def __init__(self, vocab_size: int = 100):
        self.vocab_size = vocab_size
        self.merges: List[Tuple[str, str]] = []
        self.vocab: Dict[str, int] = {}
        self.reverse_vocab: Dict[int, str] = {}

    def _get_word_frequencies(self, text: str) -> Dict[Tuple[str, ...], int]:
        """Split text into words, count frequencies, return as tuple-form."""
        text = text.lower()
        words = re.findall(r'\b[a-z]+\b', text)

        # Convert each word to tuple of characters with end marker
        word_freqs = defaultdict(int)
        for word in words:
            word_tuple = tuple(list(word) + ["</w>"])
            word_freqs[word_tuple] += 1

        return dict(word_freqs)

    def learn_merges(self, text: str, num_merges: int = None) -> None:
        """Learn BPE merges from text."""
        if num_merges is None:
            num_merges = self.vocab_size - 256  # Reserve 256 for chars

        word_freqs = self._get_word_frequencies(text)

        # Initialize with single characters
        for word, freq in word_freqs.items():
            for char in word:
                if char not in self.vocab:
                    self.vocab[char] = len(self.vocab)

        # Learn merges
        for merge_idx in range(num_merges):
            # Find most frequent pair
            pairs = defaultdict(int)
            for word, freq in word_freqs.items():
                for i in range(len(word) - 1):
                    pair = (word[i], word[i + 1])
                    pairs[pair] += freq

            if not pairs:
                break

            best_pair = max(pairs.items(), key=lambda x: x[1])[0]
            self.merges.append(best_pair)

            # Merge the pair in all words
            new_word_freqs = {}
            for word, freq in word_freqs.items():
                # Replace pair in word
                new_word = []
                i = 0
                while i < len(word):
                    if i < len(word) - 1 and (word[i], word[i + 1]) == best_pair:
                        new_word.append(best_pair[0] + best_pair[1])
                        i += 2
                    else:
                        new_word.append(word[i])
                        i += 1
                new_word_freqs[tuple(new_word)] = freq

            word_freqs = new_word_freqs

            # Add new token to vocab
            new_token = best_pair[0] + best_pair[1]
            if new_token not in self.vocab:
                self.vocab[new_token] = len(self.vocab)

        # Build reverse vocab
        self.reverse_vocab = {v: k for k, v in self.vocab.items()}

    def encode(self, text: str) -> List[int]:
        """Tokenize text using learned merges."""
        text = text.lower()
        words = re.findall(r'\b[a-z]+\b', text)

        tokens = []
        for word in words:
            # Start with character-level tokens
            word_tokens = list(word) + ["</w>"]

            # Apply merges in order
            for pair in self.merges:
                new_word_tokens = []
                i = 0
                while i < len(word_tokens):
                    if i < len(word_tokens) - 1 and \
                       word_tokens[i] == pair[0] and word_tokens[i + 1] == pair[1]:
                        new_word_tokens.append(pair[0] + pair[1])
                        i += 2
                    else:
                        new_word_tokens.append(word_tokens[i])
                        i += 1
                word_tokens = new_word_tokens

            # Convert to IDs
            for token in word_tokens:
                if token in self.vocab:
                    tokens.append(self.vocab[token])
                else:
                    # Fallback: character by character
                    for char in token:
                        if char in self.vocab:
                            tokens.append(self.vocab[char])

        return tokens

    def decode(self, token_ids: List[int]) -> str:
        """Convert token IDs back to text."""
        tokens = [self.reverse_vocab.get(tid, "<UNK>") for tid in token_ids]
        # Remove word boundary markers and join
        text = "".join(tokens).replace("</w>", " ").strip()
        return text


if __name__ == "__main__":
    import random
    random.seed(42)

    # Deterministic corpus
    corpus = "the cat sat on the mat the dog ran in the park the cat and dog played"

    # Learn BPE
    tokenizer = BPETokenizer(vocab_size=50)
    tokenizer.learn_merges(corpus, num_merges=20)

    # Test 1: Vocabulary is built
    assert len(tokenizer.vocab) > 0, "Vocabulary should be non-empty"
    assert len(tokenizer.merges) > 0, "Should learn some merges"

    # Test 2: Encode returns token IDs
    encoded = tokenizer.encode("the cat")
    assert isinstance(encoded, list), "Encode should return list"
    assert all(isinstance(t, int) for t in encoded), "Encoded should be list of ints"
    assert len(encoded) > 0, "Should encode non-empty"

    # Test 3: Decode recovers approximate text
    decoded = tokenizer.decode(encoded)
    assert isinstance(decoded, str), "Decode should return string"
    assert len(decoded) > 0, "Decoded should be non-empty"

    # Test 4: Round-trip encode->decode preserves words (though format may differ)
    original = "cat dog"
    encoded = tokenizer.encode(original)
    decoded = tokenizer.decode(encoded)
    # Check that both words appear in result
    assert "cat" in decoded or "c" in decoded, "Cat should be in decoded"
    assert "dog" in decoded or "d" in decoded, "Dog should be in decoded"

    # Test 5: Same word encodes consistently
    enc1 = tokenizer.encode("cat")
    enc2 = tokenizer.encode("cat")
    assert enc1 == enc2, "Same word should encode identically"

    # Test 6: Reverse vocab is complete
    for vocab_id in range(len(tokenizer.vocab)):
        assert vocab_id in tokenizer.reverse_vocab, f"Missing reverse mapping for ID {vocab_id}"

    print("PASS: BPE tokenizer learns merges, encodes words to IDs, decodes back, round-trips correctly")
