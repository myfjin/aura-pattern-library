"""
N-gram Language Model with Add-One Smoothing

Core idea: model text as a Markov chain over n-grams (sequences of n tokens).
Estimate P(token | preceding n-1 tokens) from data; use add-one smoothing
to handle unseen contexts. Measure quality via perplexity on held-out text.

Use when: generating text, evaluating text likelihood, building simple
language models without neural networks, or studying Markov assumptions in NLP.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Dict, List, Tuple
from collections import defaultdict
import math
import re


class NGramLanguageModel:
    """Learn n-gram counts and probabilities with add-one smoothing."""

    def __init__(self, n: int = 2):
        """n=2 means bigram model (P(w2 | w1))."""
        self.n = n
        self.context_counts: Dict[Tuple[str, ...], int] = defaultdict(int)
        self.transition_counts: Dict[Tuple[str, ...], int] = defaultdict(int)
        self.vocab: set = set()
        self.vocab_size: int = 0

    def _tokenize(self, text: str) -> List[str]:
        """Simple tokenization with start/stop markers."""
        text = text.lower()
        words = re.findall(r'\b[a-z]+\b', text)
        # Prepend start marker for n-1 tokens
        return ["<s>"] * (self.n - 1) + words + ["</s>"]

    def fit(self, documents: List[str]) -> None:
        """Learn n-gram counts from documents."""
        for doc in documents:
            tokens = self._tokenize(doc)
            # Build vocabulary
            self.vocab.update(tokens)
            # Count n-grams
            for i in range(len(tokens) - self.n + 1):
                ngram = tuple(tokens[i : i + self.n])
                context = ngram[:-1]
                token = ngram[-1]
                self.context_counts[context] += 1
                self.transition_counts[ngram] += 1

        self.vocab_size = len(self.vocab)

    def get_probability(self, context: Tuple[str, ...], token: str) -> float:
        """Compute P(token | context) with add-one smoothing."""
        ngram = context + (token,)
        # Add-one smoothing: (count + 1) / (context_count + vocab_size)
        numerator = self.transition_counts[ngram] + 1
        denominator = self.context_counts[context] + self.vocab_size
        return numerator / denominator

    def perplexity(self, text: str) -> float:
        """Compute perplexity: exp(-avg(log P(w|context)))."""
        tokens = self._tokenize(text)
        log_probs = []
        for i in range(len(tokens) - self.n + 1):
            ngram = tuple(tokens[i : i + self.n])
            context = ngram[:-1]
            token = ngram[-1]
            prob = self.get_probability(context, token)
            log_probs.append(math.log(prob))

        if not log_probs:
            return float('inf')

        avg_log_prob = sum(log_probs) / len(log_probs)
        return math.exp(-avg_log_prob)

    def sample(self, num_tokens: int = 10, seed_context: Tuple[str, ...] = None) -> str:
        """Generate text by sampling from the model."""
        import random
        if seed_context is None:
            seed_context = tuple(["<s>"] * (self.n - 1))

        context = seed_context
        tokens = []
        for _ in range(num_tokens):
            # Collect all possible next tokens for this context
            possible_next = {}
            for ngram, count in self.transition_counts.items():
                if ngram[:-1] == context:
                    possible_next[ngram[-1]] = count

            if not possible_next:
                break

            # Sample proportionally to counts
            total = sum(possible_next.values())
            r = random.uniform(0, total)
            cumsum = 0
            chosen_token = None
            for token, count in sorted(possible_next.items()):
                cumsum += count
                if r <= cumsum:
                    chosen_token = token
                    break

            if chosen_token is None:
                chosen_token = list(possible_next.keys())[0]

            if chosen_token == "</s>":
                break

            tokens.append(chosen_token)
            context = (context[1:] + (chosen_token,)) if self.n > 1 else (chosen_token,)

        return " ".join(tokens)


if __name__ == "__main__":
    import random
    random.seed(42)

    # Deterministic corpus
    corpus = [
        "the cat sat on the mat",
        "the dog ran in the park",
        "the cat and the dog played",
        "on the mat sat the cat",
        "in the park ran the dog",
    ]

    # Fit bigram model
    model = NGramLanguageModel(n=2)
    model.fit(corpus)

    # Test 1: Check vocabulary is learned
    assert "<s>" in model.vocab
    assert "cat" in model.vocab
    assert "dog" in model.vocab

    # Test 2: Probabilities are normalized over vocab
    context = ("<s>",)
    total_prob = sum(model.get_probability(context, token) for token in model.vocab)
    assert 0.99 < total_prob < 1.01, f"Probabilities should sum to ~1.0, got {total_prob}"

    # Test 3: Common contexts should have higher probability for frequent tokens
    # After "the", "cat" should be common
    context = ("the",)
    prob_cat = model.get_probability(context, "cat")
    prob_unknown = model.get_probability(context, "zzz_rare_word_zzz")
    assert prob_cat > prob_unknown, "Common token should have higher prob than unknown"

    # Test 4: Perplexity on training data should be lower than on random text
    train_text = corpus[0]
    random_text = "zzz qqq xxx ppp rrr mmm"
    perp_train = model.perplexity(train_text)
    perp_random = model.perplexity(random_text)
    assert perp_train < perp_random, f"Training perplexity {perp_train} should be < random {perp_random}"

    # Test 5: Generate sample (just verify it doesn't crash and returns text)
    sample = model.sample(num_tokens=10)
    assert isinstance(sample, str)
    assert len(sample) > 0

    print("PASS: N-gram LM learns contexts, smooths unseen ngrams, perplexity ranks in-domain text lower")
