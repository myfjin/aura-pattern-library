"""
Claim: walk-forward cross-validation for time-series models.

Valid input: X, y, model — time-ordered features, target, and a scikit-learn
compatible estimator. Returns a list of out-of-sample scores.
"""


def walk_forward_score(X, y, model):
    scores = []
    n = len(X)
    for i in range(2, n):
        train_X, train_y = X[:i], y[:i]
        test_X, test_y = X[i:i + 1], y[i:i + 1]
        model.fit(train_X, train_y)
        pred = model.predict(test_X)
        scores.append(float(pred[0] == test_y[0]) if pred else 0.0)
    return scores
