"""
Claim: trains a logistic regression classifier.

Valid input: X, y — numeric features and binary labels.
Returns a trained scikit-learn LogisticRegression model.
"""
from sklearn.linear_model import LogisticRegression


def train_logreg(X, y):
    return LogisticRegression().fit(X, y)
