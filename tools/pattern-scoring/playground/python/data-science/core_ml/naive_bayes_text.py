"""
Multinomial Naive Bayes for Text Classification (from scratch).

Core idea: Represent documents as word-frequency vectors. Assume features
(word counts) are conditionally independent given class. Compute P(class|doc)
using Bayes' rule and word probabilities per class (with Laplace smoothing).

When to use: Text classification (spam/ham, sentiment); fast training; baseline.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from collections import defaultdict
from typing import List, Tuple, Dict


def naive_bayes_train(
    texts: List[List[str]],
    labels: List[int]
) -> Tuple[Dict[int, float], Dict[int, Dict[str, float]]]:
    """
    Train a Multinomial Naive Bayes classifier on tokenized text.

    Args:
        texts: list of documents, each a list of word tokens
        labels: list of class labels (0 or 1)

    Returns:
        (class_priors, word_probs): priors and conditional word probabilities
    """
    n_docs = len(texts)
    classes = set(labels)

    # Count class occurrences
    class_counts = {c: 0 for c in classes}
    for label in labels:
        class_counts[label] += 1

    # Compute class priors
    class_priors = {c: class_counts[c] / n_docs for c in classes}

    # Build word frequency tables per class (with Laplace smoothing)
    word_counts = {c: defaultdict(int) for c in classes}
    total_words = {c: 0 for c in classes}

    for i in range(n_docs):
        label = labels[i]
        for word in texts[i]:
            word_counts[label][word] += 1
            total_words[label] += 1

    # Compute word probabilities per class (Laplace smoothing: add 1)
    vocab_size = len(set(w for text in texts for w in text))
    word_probs = {}

    for c in classes:
        word_probs[c] = {}
        for word in set(w for text in texts for w in text):
            word_probs[c][word] = (word_counts[c][word] + 1) / (total_words[c] + vocab_size)

    return class_priors, word_probs


def naive_bayes_predict(
    text: List[str],
    class_priors: Dict[int, float],
    word_probs: Dict[int, Dict[str, float]]
) -> int:
    """
    Predict the class of a document using Naive Bayes.

    Args:
        text: document as a list of word tokens
        class_priors: class prior probabilities
        word_probs: word probability tables per class

    Returns:
        predicted class label
    """
    best_class = None
    best_score = -float('inf')

    for c in class_priors:
        # Start with log(prior)
        score = math.log(class_priors[c])

        # Add log of word probabilities
        for word in text:
            if word in word_probs[c]:
                score += math.log(word_probs[c][word])
            else:
                # Unseen word: use Laplace smoothing
                vocab_size = len(word_probs[c])
                score += math.log(1.0 / (sum(len(wp) for wp in word_probs.values()) + vocab_size))

        if score > best_score:
            best_score = score
            best_class = c

    return best_class


if __name__ == "__main__":
    random.seed(42)

    # Simple synthetic text classification: spam vs ham
    # Spam: contains "cheap", "free", "buy"; Ham: contains "meeting", "report", "data"
    spam_words = ["cheap", "free", "buy", "offer", "click"]
    ham_words = ["meeting", "report", "data", "project", "deadline"]

    texts = []
    labels = []

    # Generate spam documents
    for _ in range(10):
        doc = [random.choice(spam_words) for _ in range(random.randint(3, 5))]
        texts.append(doc)
        labels.append(1)  # spam

    # Generate ham documents
    for _ in range(10):
        doc = [random.choice(ham_words) for _ in range(random.randint(3, 5))]
        texts.append(doc)
        labels.append(0)  # ham

    # Train
    class_priors, word_probs = naive_bayes_train(texts, labels)

    # Test on training data (sanity check)
    correct = 0
    for i in range(len(texts)):
        pred = naive_bayes_predict(texts[i], class_priors, word_probs)
        if pred == labels[i]:
            correct += 1

    accuracy = correct / len(texts)
    assert accuracy >= 0.9, f"Accuracy = {accuracy} is too low"

    # Test on new example
    test_spam = ["cheap", "free", "buy"]
    test_ham = ["meeting", "data", "report"]

    pred_spam = naive_bayes_predict(test_spam, class_priors, word_probs)
    pred_ham = naive_bayes_predict(test_ham, class_priors, word_probs)

    assert pred_spam == 1, "Failed to classify spam"
    assert pred_ham == 0, "Failed to classify ham"

    print(f"NAIVE_BAYES_TEXT PASS: accuracy = {accuracy:.3f}, test_spam → {pred_spam}, test_ham → {pred_ham}")
