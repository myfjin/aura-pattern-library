"""
Claim: computes class weights for an imbalanced binary classification problem.

Valid input: y — a list of binary labels (0/1).
Returns a dictionary mapping class label to balanced weight.
"""


def class_weights(y):
    if not isinstance(y, list):
        raise TypeError("y must be a list of binary labels")
    if not all(isinstance(v, int) and v in (0, 1) for v in y):
        raise ValueError("labels must be 0 or 1")
    from collections import Counter
    counts = Counter(y)
    total = len(y)
    return {label: total / (2.0 * count) for label, count in counts.items()}
