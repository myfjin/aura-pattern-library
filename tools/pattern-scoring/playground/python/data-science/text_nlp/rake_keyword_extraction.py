"""
RAKE-Style Keyword Extraction

Core idea: split text into phrases delimited by stopwords, score phrases by
degree (unique words in phrase) and frequency (how often phrase appears).
Higher-scoring phrases are likely meaningful keywords.

Use when: extracting keywords from documents, summarizing text topics, building
terminology indices, or understanding key concepts in unstructured text.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple, Set, Dict
import re
from collections import defaultdict


class RAKEExtractor:
    """Extract keywords using RAKE (Rapid Automatic Keyword Extraction)."""

    def __init__(self, stopwords: Set[str] = None):
        if stopwords is None:
            # Common English stopwords
            self.stopwords = {
                "the", "a", "an", "and", "or", "but", "is", "are", "was", "were",
                "be", "been", "being", "have", "has", "had", "do", "does", "did",
                "will", "would", "should", "could", "may", "might", "can", "must",
                "in", "on", "at", "by", "for", "with", "to", "of", "from", "up",
                "as", "if", "about", "into", "through", "during", "this", "that",
                "these", "those", "i", "you", "he", "she", "it", "we", "they",
            }
        else:
            self.stopwords = stopwords

    def _tokenize(self, text: str) -> List[str]:
        """Simple tokenization."""
        text = text.lower()
        words = re.findall(r'\b[a-z]+\b', text)
        return words

    def extract_phrases(self, text: str) -> List[List[str]]:
        """Split text into phrases delimited by stopwords.

        Returns list of phrases, where each phrase is a list of words.
        """
        words = self._tokenize(text)

        phrases = []
        current_phrase = []

        for word in words:
            if word in self.stopwords:
                if current_phrase:
                    phrases.append(current_phrase)
                    current_phrase = []
            else:
                current_phrase.append(word)

        if current_phrase:
            phrases.append(current_phrase)

        return phrases

    def compute_word_scores(self, phrases: List[List[str]]) -> Dict[str, float]:
        """Compute degree and frequency scores for each word.

        degree(w) = number of times w appears with other words
        frequency(w) = how often w appears
        score(w) = degree(w) / frequency(w)
        """
        co_occurrence = defaultdict(set)
        frequency = defaultdict(int)

        for phrase in phrases:
            for word in phrase:
                frequency[word] += 1
                # Co-occurrence: all other words in this phrase
                for other in phrase:
                    if other != word:
                        co_occurrence[word].add(other)

        # Degree = number of unique co-occurrence partners
        word_scores = {}
        for word in frequency:
            degree = len(co_occurrence[word])
            freq = frequency[word]
            # Avoid division by zero; use freq as tie-breaker
            word_scores[word] = (degree + 1) / (freq + 1)

        return word_scores

    def score_phrases(self, phrases: List[List[str]], word_scores: Dict[str, float]) -> List[Tuple[str, float]]:
        """Score each phrase as sum of word scores."""
        phrase_scores = []

        for phrase in phrases:
            phrase_text = " ".join(phrase)
            score = sum(word_scores.get(word, 0.0) for word in phrase)
            phrase_scores.append((phrase_text, score))

        return phrase_scores

    def extract_keywords(self, text: str, top_k: int = 5) -> List[Tuple[str, float]]:
        """Extract top-k keywords from text.

        Returns list of (keyword, score) tuples sorted by score descending.
        """
        phrases = self.extract_phrases(text)
        word_scores = self.compute_word_scores(phrases)
        phrase_scores = self.score_phrases(phrases, word_scores)

        # Sort by score descending
        phrase_scores.sort(key=lambda x: x[1], reverse=True)
        return phrase_scores[:top_k]


if __name__ == "__main__":
    import random
    random.seed(42)

    # Deterministic corpus
    text = """
    Machine learning is a subset of artificial intelligence that focuses on
    learning from data. Deep learning uses neural networks with multiple layers.
    Natural language processing is used for text analysis. Machine learning models
    are trained on large datasets. Deep learning is powerful for image recognition
    and language understanding.
    """

    extractor = RAKEExtractor()

    # Test 1: Extract phrases correctly
    phrases = extractor.extract_phrases(text)
    assert len(phrases) > 0, "Should extract phrases"
    assert all(isinstance(p, list) for p in phrases), "Phrases should be lists"
    assert all(all(isinstance(w, str) for w in p) for p in phrases), "Words should be strings"

    # Test 2: No phrase should contain stopwords
    for phrase in phrases:
        assert not any(w in extractor.stopwords for w in phrase), \
            f"Phrase {phrase} contains stopwords"

    # Test 3: Word scores are computed
    word_scores = extractor.compute_word_scores(phrases)
    assert len(word_scores) > 0, "Should compute word scores"
    assert all(v >= 0 for v in word_scores.values()), "Scores should be non-negative"

    # Test 4: Keywords are extracted
    keywords = extractor.extract_keywords(text, top_k=5)
    assert len(keywords) <= 5, "Should return at most top_k"
    assert all(isinstance(k, str) and isinstance(s, float) for k, s in keywords), \
        "Keywords should be (str, float) tuples"

    # Test 5: Keywords are sorted by score descending
    assert keywords == sorted(keywords, key=lambda x: x[1], reverse=True), \
        "Keywords should be sorted by score descending"

    # Test 6: High-frequency technical terms should rank high
    # "machine learning" and "deep learning" appear multiple times
    keyword_texts = [k for k, _ in keywords]
    has_ml_or_dl = any("learning" in k for k in keyword_texts)
    assert has_ml_or_dl, "Learning-related keywords should rank high"

    # Test 7: Empty text returns no keywords
    keywords_empty = extractor.extract_keywords("", top_k=5)
    assert len(keywords_empty) == 0, "Empty text should return no keywords"

    print("PASS: RAKE extracts phrases, scores by degree/frequency, ranks technical terms higher")
