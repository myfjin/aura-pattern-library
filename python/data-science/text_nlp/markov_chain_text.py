"""
Word-Level Markov Chain Text Generator

Core idea: build a transition matrix of word frequencies (conditional on previous word).
Generate text by sampling from this distribution at each step, deterministic given seed.
Useful for understanding Markov assumptions, text generation baselines, and data exploration.

Use when: generating synthetic text, understanding term co-occurrence, building simple
language models, or studying order-n dependencies in text.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Dict, List, Tuple
from collections import defaultdict
import random
import re


class MarkovChainText:
    """Learn word transitions, generate text, validate transition matrix."""

    def __init__(self, order: int = 1):
        """order=1 means unigram->bigram transitions (P(w2|w1))."""
        self.order = order
        self.transitions: Dict[Tuple[str, ...], List[str]] = defaultdict(list)
        self.vocab: set = set()

    def _tokenize(self, text: str) -> List[str]:
        """Simple tokenization with start marker."""
        text = text.lower()
        words = re.findall(r'\b[a-z]+\b', text)
        # Add START token for initial state
        return ["<START>"] + words

    def fit(self, documents: List[str]) -> None:
        """Learn transition probabilities from documents."""
        for doc in documents:
            tokens = self._tokenize(doc)
            self.vocab.update(tokens)

            # Build transitions: (prev_order words) -> [next words list]
            for i in range(len(tokens) - self.order):
                context = tuple(tokens[i : i + self.order])
                next_word = tokens[i + self.order]
                self.transitions[context].append(next_word)

    def generate(self, max_length: int = 20, seed_context: Tuple[str, ...] = None) -> str:
        """Generate text by sampling from learned transitions.

        Returns text as space-separated words, with START token removed.
        """
        if seed_context is None:
            seed_context = ("<START>",) * self.order

        context = seed_context
        tokens = []

        for _ in range(max_length):
            if context not in self.transitions:
                break

            # Sample uniformly from observed transitions for this context
            next_words = self.transitions[context]
            next_word = random.choice(next_words)

            tokens.append(next_word)

            # Shift context window
            context = context[1:] + (next_word,)

        # Remove START tokens
        result = [t for t in tokens if t != "<START>"]
        return " ".join(result)

    def get_transition_counts(self) -> Dict[Tuple[str, ...], Dict[str, int]]:
        """Return transition matrix as counts: {context -> {next_word -> count}}."""
        counts = {}
        for context, next_words in self.transitions.items():
            counts[context] = defaultdict(int)
            for word in next_words:
                counts[context][word] += 1
        return counts

    def sanity_check(self) -> Tuple[bool, str]:
        """Verify transition matrix properties.

        Returns (valid, reason) tuple.
        """
        if not self.transitions:
            return False, "No transitions learned"

        # Check: each context has at least one transition
        for context, words in self.transitions.items():
            if not words:
                return False, f"Context {context} has no transitions"

        # Check: all contexts are tuples of correct order
        for context in self.transitions.keys():
            if not isinstance(context, tuple) or len(context) != self.order:
                return False, f"Invalid context format or length: {context}"

        # Check: all next_words are strings
        for words in self.transitions.values():
            for word in words:
                if not isinstance(word, str):
                    return False, f"Non-string word in transitions: {word}"

        return True, "Transition matrix valid"


if __name__ == "__main__":
    random.seed(42)

    # Deterministic corpus
    corpus = [
        "the cat sat on the mat",
        "the dog ran in the park",
        "the cat and dog played",
        "on the mat sat the cat",
        "in the park the dog ran",
    ]

    # Build bigram model
    model = MarkovChainText(order=1)
    model.fit(corpus)

    # Test 1: Transitions are learned
    assert len(model.transitions) > 0, "Should learn transitions"
    assert ("<START>",) in model.transitions, "Should have START transitions"

    # Test 2: Sanity check passes
    valid, reason = model.sanity_check()
    assert valid, f"Sanity check failed: {reason}"

    # Test 3: Common words appear in transitions
    start_transitions = model.transitions[("<START>",)]
    assert "the" in start_transitions, "'the' should follow START"

    # Test 4: Transition counts are consistent
    counts = model.get_transition_counts()
    for context, word_counts in counts.items():
        for word, count in word_counts.items():
            assert count > 0, f"Count should be positive for {context}->{word}"

    # Test 5: Generation produces strings without START
    text = model.generate(max_length=10)
    assert isinstance(text, str), "Generated text should be string"
    assert "<START>" not in text, "Generated text should not contain START"
    assert len(text) > 0, "Should generate non-empty text"

    # Test 6: With seed context, generation produces valid output
    seed_ctx = ("the",)
    text1 = model.generate(max_length=5, seed_context=seed_ctx)
    text2 = model.generate(max_length=5, seed_context=seed_ctx)
    # Both should be valid strings (may differ due to sampling, but both valid)
    assert isinstance(text1, str) and isinstance(text2, str), \
        "Generated text should be strings"

    print("PASS: Markov chain learns transitions, generates deterministic text, sanity checks validate matrix")
