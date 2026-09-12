"""Signed metamorphic (transform, comparator) relations per pattern category.

A Relation is a named callable that takes a user module (the implementation under
verification), produces one or more source/follow-up input pairs, runs the
implementation on both, and checks a deterministic property.
"""
from __future__ import annotations

import copy
import random
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Tuple


random.seed(0)  # module-level determinism


@dataclass(frozen=True)
class RelationResult:
    name: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class Relation:
    name: str
    pattern_category: str
    check: Callable[[Any], RelationResult]


def _predict_linear(mod, X, params):
    weights, bias = params
    return [bias + sum(weights[j] * x[j] for j in range(len(weights))) for x in X]


def _approx(a, b, tol=1e-6):
    if isinstance(a, float) and isinstance(b, (int, float)):
        return abs(a - float(b)) <= tol
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(_approx(x, y, tol) for x, y in zip(a, b))
    return a == b


def _linreg_scale_target(mod) -> RelationResult:
    """Scaling all targets by k scales all predictions by k."""
    random.seed(42)
    n = 30
    X = [[random.uniform(-5, 5), random.uniform(-5, 5)] for _ in range(n)]
    y = [2.0 * X[i][0] + 3.0 * X[i][1] + random.gauss(0, 0.5) for i in range(n)]
    k = 2.5

    fit = getattr(mod, "linear_regression_gd")
    source = _predict_linear(mod, X, fit(X, y, 0.05, 500))
    y_scaled = [k * v for v in y]
    follow = _predict_linear(mod, X, fit(X, y_scaled, 0.05, 500))
    expected = [k * v for v in source]
    ok = _approx(follow, expected, tol=1e-3)
    return RelationResult(
        "linreg_scale_target", ok,
        "scaled predictions match" if ok else f"expected {expected[:3]}..., got {follow[:3]}..."
    )


def _linreg_shift_target(mod) -> RelationResult:
    """Adding a constant to all targets shifts predictions by that constant."""
    random.seed(43)
    n = 30
    X = [[random.uniform(-5, 5), random.uniform(-5, 5)] for _ in range(n)]
    y = [2.0 * X[i][0] + 3.0 * X[i][1] + random.gauss(0, 0.5) for i in range(n)]
    c = 7.0

    fit = getattr(mod, "linear_regression_gd")
    source = _predict_linear(mod, X, fit(X, y, 0.05, 500))
    y_shifted = [v + c for v in y]
    follow = _predict_linear(mod, X, fit(X, y_shifted, 0.05, 500))
    expected = [v + c for v in source]
    ok = _approx(follow, expected, tol=1e-3)
    return RelationResult(
        "linreg_shift_target", ok,
        "shifted predictions match" if ok else f"expected {expected[:3]}..., got {follow[:3]}..."
    )


def _linreg_feature_permutation(mod) -> RelationResult:
    """Permuting feature columns preserves predictions up to column reordering."""
    random.seed(44)
    n = 30
    X = [[random.uniform(-5, 5), random.uniform(-5, 5)] for _ in range(n)]
    y = [2.0 * X[i][0] + 3.0 * X[i][1] + random.gauss(0, 0.5) for i in range(n)]

    fit = getattr(mod, "linear_regression_gd")
    weights, bias = fit(X, y, 0.01, 1000)
    perm = [1, 0]
    X_perm = [[row[perm[j]] for j in range(len(row))] for row in X]
    weights_perm, bias_perm = fit(X_perm, y, 0.01, 1000)

    source_pred = [bias + weights[0] * X[i][0] + weights[1] * X[i][1] for i in range(n)]
    follow_pred = [bias_perm + weights_perm[0] * X_perm[i][0] + weights_perm[1] * X_perm[i][1] for i in range(n)]
    ok = _approx(source_pred, follow_pred, tol=1e-3)
    return RelationResult(
        "linreg_feature_permutation", ok,
        "permuted-feature predictions match" if ok else f"expected {source_pred[:3]}..., got {follow_pred[:3]}..."
    )


def _poly_scale_target(mod) -> RelationResult:
    """Scaling targets by k scales polynomial evaluations by k."""
    random.seed(45)
    true_coeffs = [2.0, 3.0, 0.5]
    x_vals = [float(i) * 0.5 for i in range(20)]
    eval_poly = getattr(mod, "eval_poly")
    y_vals = [eval_poly(true_coeffs, x) + random.gauss(0, 0.1) for x in x_vals]
    k = 2.0

    fit = getattr(mod, "fit_polynomial")
    source = [eval_poly(fit(x_vals, y_vals, 2), x) for x in x_vals]
    y_scaled = [k * v for v in y_vals]
    follow = [eval_poly(fit(x_vals, y_scaled, 2), x) for x in x_vals]
    expected = [k * v for v in source]
    ok = _approx(follow, expected, tol=1e-3)
    return RelationResult(
        "poly_scale_target", ok,
        "scaled polynomial predictions match" if ok else f"expected {expected[:3]}..., got {follow[:3]}..."
    )


def _poly_shift_target(mod) -> RelationResult:
    """Adding a constant to targets shifts polynomial intercept by that constant."""
    random.seed(46)
    true_coeffs = [2.0, 3.0, 0.5]
    x_vals = [float(i) * 0.5 for i in range(20)]
    eval_poly = getattr(mod, "eval_poly")
    y_vals = [eval_poly(true_coeffs, x) + random.gauss(0, 0.1) for x in x_vals]
    c = 5.0

    fit = getattr(mod, "fit_polynomial")
    source = [eval_poly(fit(x_vals, y_vals, 2), x) for x in x_vals]
    y_shifted = [v + c for v in y_vals]
    follow = [eval_poly(fit(x_vals, y_shifted, 2), x) for x in x_vals]
    expected = [v + c for v in source]
    ok = _approx(follow, expected, tol=1e-3)
    return RelationResult(
        "poly_shift_target", ok,
        "shifted polynomial predictions match" if ok else f"expected {expected[:3]}..., got {follow[:3]}..."
    )


def _ridge_scale_target(mod) -> RelationResult:
    """Scaling targets by k scales ridge predictions by k."""
    random.seed(47)
    n = 30
    X = [[random.uniform(-5, 5), random.uniform(-5, 5)] for _ in range(n)]
    y = [2.0 * X[i][0] + 3.0 * X[i][1] + random.gauss(0, 0.5) for i in range(n)]
    k = 2.0

    fit = getattr(mod, "ridge_regression_normal_eq")
    weights = fit(X, y, 0.01)
    source = [sum(weights[j] * X[i][j] for j in range(len(weights))) for i in range(n)]
    y_scaled = [k * v for v in y]
    weights2 = fit(X, y_scaled, 0.01)
    follow = [sum(weights2[j] * X[i][j] for j in range(len(weights2))) for i in range(n)]
    expected = [k * v for v in source]
    ok = _approx(follow, expected, tol=1e-3)
    return RelationResult(
        "ridge_scale_target", ok,
        "scaled ridge predictions match" if ok else f"expected {expected[:3]}..., got {follow[:3]}..."
    )


def _ridge_ols_approx(mod) -> RelationResult:
    """With lambda near zero, ridge predictions should match ordinary least squares."""
    random.seed(48)
    n = 30
    X = [[random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)] for _ in range(n)]
    true_w = [2.0, 3.0, -1.0]
    y = [sum(true_w[j] * X[i][j] for j in range(3)) + random.gauss(0, 0.5) for i in range(n)]

    fit = getattr(mod, "ridge_regression_normal_eq")
    w_ols = fit(X, y, 1e-12)
    w_ridge = fit(X, y, 1e-6)

    pred_ols = [sum(w_ols[j] * X[i][j] for j in range(3)) for i in range(n)]
    pred_ridge = [sum(w_ridge[j] * X[i][j] for j in range(3)) for i in range(n)]

    ok = _approx(pred_ridge, pred_ols, tol=1e-2)
    return RelationResult(
        "ridge_ols_approx", ok,
        "ridge ≈ OLS for tiny lambda" if ok else f"expected {pred_ols[:3]}..., got {pred_ridge[:3]}..."
    )


# ---------------------------------------------------------------------------
# Classification relations
# ---------------------------------------------------------------------------

def _swap_labels(y: List[int]) -> List[int]:
    return [1 - v for v in y]


def _make_binary_classification_data(seed: int, n: int = 80, sep: float = 1.5):
    random.seed(seed)
    X, y = [], []
    for _ in range(n):
        label = random.choice([0, 1])
        x1 = random.uniform(-3, 3)
        noise = random.gauss(0, 0.8)
        x2 = (x1 + sep + noise) if label == 1 else (x1 - sep + noise)
        X.append([x1, x2])
        y.append(label)
    return X, y


def _logreg_label_permutation(mod) -> RelationResult:
    """Swapping class labels should swap predicted labels."""
    X, y = _make_binary_classification_data(50)
    fit = getattr(mod, "logistic_regression_fit")
    predict = getattr(mod, "logistic_regression_predict")

    w, b = fit(X, y, 0.1, 200)
    source_preds = predict(X, w, b)
    y_swapped = _swap_labels(y)
    w2, b2 = fit(X, y_swapped, 0.1, 200)
    follow_preds = predict(X, w2, b2)
    expected = _swap_labels(source_preds)
    ok = follow_preds == expected
    return RelationResult(
        "logreg_label_permutation", ok,
        "label swap reflected in predictions" if ok else f"expected {_swap_labels(source_preds[:5])}, got {follow_preds[:5]}"
    )


def _logreg_duplicate_invariance(mod) -> RelationResult:
    """Duplicating a training point should not flip its prediction."""
    X, y = _make_binary_classification_data(51)
    fit = getattr(mod, "logistic_regression_fit")
    predict = getattr(mod, "logistic_regression_predict")

    probe = X[0]
    w, b = fit(X, y, 0.1, 200)
    pred_source = predict([probe], w, b)[0]

    X_dup = X + [probe]
    y_dup = y + [y[0]]
    w2, b2 = fit(X_dup, y_dup, 0.1, 200)
    pred_follow = predict([probe], w2, b2)[0]
    ok = pred_source == pred_follow
    return RelationResult(
        "logreg_duplicate_invariance", ok,
        "duplicate point prediction unchanged" if ok else f"source={pred_source}, follow={pred_follow}"
    )


def _logreg_feature_permutation(mod) -> RelationResult:
    """Permuting feature columns consistently preserves predictions."""
    X, y = _make_binary_classification_data(52)
    fit = getattr(mod, "logistic_regression_fit")
    predict = getattr(mod, "logistic_regression_predict")

    w, b = fit(X, y, 0.1, 200)
    source_preds = predict(X, w, b)

    perm = [1, 0]
    X_perm = [[row[perm[j]] for j in range(len(row))] for row in X]
    w2, b2 = fit(X_perm, y, 0.1, 200)
    follow_preds = predict(X_perm, w2, b2)
    ok = follow_preds == source_preds
    return RelationResult(
        "logreg_feature_permutation", ok,
        "feature permutation preserves predictions" if ok else f"source[:5]={source_preds[:5]}, follow[:5]={follow_preds[:5]}"
    )


def _knn_label_permutation(mod) -> RelationResult:
    """Swapping class labels should swap predicted labels."""
    random.seed(53)
    X_train, y_train = _make_binary_classification_data(53, n=60)
    X_test, y_test = _make_binary_classification_data(54, n=30)
    predict = getattr(mod, "knn_predict_batch")

    source_preds = predict(X_test, X_train, y_train, k=5)
    y_train_swapped = _swap_labels(y_train)
    follow_preds = predict(X_test, X_train, y_train_swapped, k=5)
    expected = _swap_labels(source_preds)
    ok = follow_preds == expected
    return RelationResult(
        "knn_label_permutation", ok,
        "label swap reflected in predictions" if ok else f"expected {_swap_labels(source_preds[:5])}, got {follow_preds[:5]}"
    )


def _knn_duplicate_invariance(mod) -> RelationResult:
    """Duplicating a training point should not flip its own prediction."""
    random.seed(55)
    X_train, y_train = _make_binary_classification_data(55, n=60)
    X_test, y_test = _make_binary_classification_data(56, n=30)
    predict = getattr(mod, "knn_predict_batch")

    probe = X_train[0]
    pred_source = predict([probe], X_train, y_train, k=5)[0]

    X_train_dup = X_train + [probe]
    y_train_dup = y_train + [y_train[0]]
    pred_follow = predict([probe], X_train_dup, y_train_dup, k=5)[0]
    ok = pred_source == pred_follow
    return RelationResult(
        "knn_duplicate_invariance", ok,
        "duplicate point prediction unchanged" if ok else f"source={pred_source}, follow={pred_follow}"
    )


def _knn_feature_permutation(mod) -> RelationResult:
    """Permuting feature columns consistently preserves predictions."""
    random.seed(57)
    X_train, y_train = _make_binary_classification_data(57, n=60)
    X_test, y_test = _make_binary_classification_data(58, n=30)
    predict = getattr(mod, "knn_predict_batch")

    perm = [1, 0]
    X_train_perm = [[row[perm[j]] for j in range(len(row))] for row in X_train]
    X_test_perm = [[row[perm[j]] for j in range(len(row))] for row in X_test]
    source_preds = predict(X_test, X_train, y_train, k=5)
    follow_preds = predict(X_test_perm, X_train_perm, y_train, k=5)
    ok = follow_preds == source_preds
    return RelationResult(
        "knn_feature_permutation", ok,
        "feature permutation preserves predictions" if ok else f"source[:5]={source_preds[:5]}, follow[:5]={follow_preds[:5]}"
    )


def _tree_label_permutation(mod) -> RelationResult:
    """Swapping class labels should swap predicted labels."""
    random.seed(59)
    X_train, y_train = _make_binary_classification_data(59, n=70)
    X_test, y_test = _make_binary_classification_data(60, n=30)
    build = getattr(mod, "build_tree")
    predict = getattr(mod, "predict_tree")

    tree = build(X_train, y_train, max_depth=5)
    source_preds = [predict(X_test[i], tree) for i in range(len(X_test))]
    tree2 = build(X_train, _swap_labels(y_train), max_depth=5)
    follow_preds = [predict(X_test[i], tree2) for i in range(len(X_test))]
    expected = _swap_labels(source_preds)
    ok = follow_preds == expected
    return RelationResult(
        "tree_label_permutation", ok,
        "label swap reflected in predictions" if ok else f"expected {_swap_labels(source_preds[:5])}, got {follow_preds[:5]}"
    )


def _tree_duplicate_invariance(mod) -> RelationResult:
    """Duplicating a training point should not flip its prediction."""
    random.seed(61)
    X_train, y_train = _make_binary_classification_data(61, n=70)
    build = getattr(mod, "build_tree")
    predict = getattr(mod, "predict_tree")

    probe = X_train[0]
    tree = build(X_train, y_train, max_depth=5)
    pred_source = predict(probe, tree)

    X_train_dup = X_train + [probe]
    y_train_dup = y_train + [y_train[0]]
    tree2 = build(X_train_dup, y_train_dup, max_depth=5)
    pred_follow = predict(probe, tree2)
    ok = pred_source == pred_follow
    return RelationResult(
        "tree_duplicate_invariance", ok,
        "duplicate point prediction unchanged" if ok else f"source={pred_source}, follow={pred_follow}"
    )


def _tree_noise_feature_invariance(mod) -> RelationResult:
    """Adding a pure-noise feature should not change predictions."""
    random.seed(63)
    X_train, y_train = _make_binary_classification_data(63, n=70)
    X_test, y_test = _make_binary_classification_data(64, n=30)
    build = getattr(mod, "build_tree")
    predict = getattr(mod, "predict_tree")

    tree = build(X_train, y_train, max_depth=5)
    source_preds = [predict(X_test[i], tree) for i in range(len(X_test))]

    X_train_noise = [row + [random.gauss(0, 10.0)] for row in X_train]
    X_test_noise = [row + [random.gauss(0, 10.0)] for row in X_test]
    tree2 = build(X_train_noise, y_train, max_depth=5)
    follow_preds = [predict(X_test_noise[i], tree2) for i in range(len(X_test_noise))]
    ok = follow_preds == source_preds
    return RelationResult(
        "tree_noise_feature_invariance", ok,
        "noise feature ignored" if ok else f"source[:5]={source_preds[:5]}, follow[:5]={follow_preds[:5]}"
    )


def _make_tree_data(seed: int, n: int = 100, leak: float = 0.15):
    """Generate ID3-style data with a clean x0 boundary and optional leak."""
    random.seed(seed)
    X, y = [], []
    for _ in range(n // 2):
        x0 = random.uniform(0, 2.5) if random.random() < (1 - leak) else random.uniform(2.5, 5)
        x1 = random.uniform(0, 5)
        X.append([x0, x1])
        y.append(0)
    for _ in range(n // 2):
        x0 = random.uniform(2.5, 5) if random.random() < (1 - leak) else random.uniform(0, 2.5)
        x1 = random.uniform(0, 5)
        X.append([x0, x1])
        y.append(1)
    indices = list(range(n))
    random.shuffle(indices)
    train_idx, test_idx = indices[: 70 * n // 100], indices[70 * n // 100 :]
    X_train = [X[i] for i in train_idx]
    y_train = [y[i] for i in train_idx]
    X_test = [X[i] for i in test_idx]
    y_test = [y[i] for i in test_idx]
    return X_train, y_train, X_test, y_test


def _tree_clean_separable(mod) -> RelationResult:
    """Removing class overlap should let a correct tree separate classes perfectly."""
    random.seed(72)
    X_train_src, y_train_src, X_test_src, y_test_src = _make_tree_data(72, n=100, leak=0.15)
    X_train_fol, y_train_fol, X_test_fol, y_test_fol = _make_tree_data(73, n=100, leak=0.0)
    build = getattr(mod, "build_tree")
    predict = getattr(mod, "predict_tree")

    tree_src = build(X_train_src, y_train_src, max_depth=5)
    src_acc = sum(
        predict(X_test_src[i], tree_src) == y_test_src[i] for i in range(len(X_test_src))
    ) / len(X_test_src)

    tree_fol = build(X_train_fol, y_train_fol, max_depth=5)
    fol_acc = sum(
        predict(X_test_fol[i], tree_fol) == y_test_fol[i] for i in range(len(X_test_fol))
    ) / len(X_test_fol)

    ok = fol_acc >= 0.95 and fol_acc >= src_acc - 0.05
    return RelationResult(
        "tree_clean_separable", ok,
        f"clean accuracy {fol_acc:.2f} (source {src_acc:.2f})" if ok
        else f"expected >=0.95 after removing overlap, got {fol_acc:.2f} (source {src_acc:.2f})"
    )


def _nb_label_permutation(mod) -> RelationResult:
    """Swapping class labels should swap predicted labels."""
    random.seed(65)
    spam = ["cheap", "free", "buy", "offer", "click"]
    ham = ["meeting", "report", "data", "project", "deadline"]
    texts, labels = [], []
    for _ in range(20):
        words = [random.choice(spam) for _ in range(random.randint(3, 5))]
        texts.append(words)
        labels.append(1)
    for _ in range(20):
        words = [random.choice(ham) for _ in range(random.randint(3, 5))]
        texts.append(words)
        labels.append(0)

    train = getattr(mod, "naive_bayes_train")
    predict = getattr(mod, "naive_bayes_predict")

    priors, probs = train(texts, labels)
    source_preds = [predict(texts[i], priors, probs) for i in range(len(texts))]
    priors2, probs2 = train(texts, _swap_labels(labels))
    follow_preds = [predict(texts[i], priors2, probs2) for i in range(len(texts))]
    expected = _swap_labels(source_preds)
    ok = follow_preds == expected
    return RelationResult(
        "nb_label_permutation", ok,
        "label swap reflected in predictions" if ok else f"expected {_swap_labels(source_preds[:5])}, got {follow_preds[:5]}"
    )


def _nb_duplicate_invariance(mod) -> RelationResult:
    """Duplicating a training document should not flip its prediction."""
    random.seed(66)
    spam = ["cheap", "free", "buy", "offer", "click"]
    ham = ["meeting", "report", "data", "project", "deadline"]
    texts, labels = [], []
    for _ in range(20):
        words = [random.choice(spam) for _ in range(random.randint(3, 5))]
        texts.append(words)
        labels.append(1)
    for _ in range(20):
        words = [random.choice(ham) for _ in range(random.randint(3, 5))]
        texts.append(words)
        labels.append(0)

    train = getattr(mod, "naive_bayes_train")
    predict = getattr(mod, "naive_bayes_predict")

    probe = texts[0]
    priors, probs = train(texts, labels)
    pred_source = predict(probe, priors, probs)

    texts_dup = texts + [probe]
    labels_dup = labels + [labels[0]]
    priors2, probs2 = train(texts_dup, labels_dup)
    pred_follow = predict(probe, priors2, probs2)
    ok = pred_source == pred_follow
    return RelationResult(
        "nb_duplicate_invariance", ok,
        "duplicate document prediction unchanged" if ok else f"source={pred_source}, follow={pred_follow}"
    )


def _nb_word_order_invariance(mod) -> RelationResult:
    """Shuffling word order in a document should not change Naive Bayes prediction."""
    random.seed(67)
    spam = ["cheap", "free", "buy", "offer", "click"]
    ham = ["meeting", "report", "data", "project", "deadline"]
    texts, labels = [], []
    for _ in range(20):
        words = [random.choice(spam) for _ in range(random.randint(3, 5))]
        texts.append(words)
        labels.append(1)
    for _ in range(20):
        words = [random.choice(ham) for _ in range(random.randint(3, 5))]
        texts.append(words)
        labels.append(0)

    train = getattr(mod, "naive_bayes_train")
    predict = getattr(mod, "naive_bayes_predict")

    priors, probs = train(texts, labels)
    probe = list(texts[0])
    random.shuffle(probe)
    pred_source = predict(texts[0], priors, probs)
    pred_follow = predict(probe, priors, probs)
    ok = pred_source == pred_follow
    return RelationResult(
        "nb_word_order_invariance", ok,
        "word order does not change prediction" if ok else f"source={pred_source}, follow={pred_follow}"
    )


def _perceptron_label_permutation(mod) -> RelationResult:
    """Swapping class labels should swap predicted labels."""
    X, y = _make_binary_classification_data(68)
    fit = getattr(mod, "perceptron_fit")
    predict = getattr(mod, "perceptron_predict")

    w, b = fit(X, y, 1.0, 100)
    source_preds = predict(X, w, b)
    w2, b2 = fit(X, _swap_labels(y), 1.0, 100)
    follow_preds = predict(X, w2, b2)
    expected = _swap_labels(source_preds)
    ok = follow_preds == expected
    return RelationResult(
        "perceptron_label_permutation", ok,
        "label swap reflected in predictions" if ok else f"expected {_swap_labels(source_preds[:5])}, got {follow_preds[:5]}"
    )


def _perceptron_duplicate_invariance(mod) -> RelationResult:
    """Duplicating a correctly-classified training point should not flip its prediction."""
    random.seed(69)
    X, y = _make_binary_classification_data(69, n=80, sep=1.2)
    fit = getattr(mod, "perceptron_fit")
    predict = getattr(mod, "perceptron_predict")

    w, b = fit(X, y, 1.0, 100)
    preds = predict(X, w, b)
    # Pick a correctly-classified point to duplicate.
    correct_idx = next((i for i in range(len(X)) if preds[i] == y[i]), 0)
    probe = X[correct_idx]
    probe_label = y[correct_idx]
    pred_source = predict([probe], w, b)[0]

    X_dup = X + [probe]
    y_dup = y + [probe_label]
    w2, b2 = fit(X_dup, y_dup, 1.0, 100)
    pred_follow = predict([probe], w2, b2)[0]
    ok = pred_source == pred_follow
    return RelationResult(
        "perceptron_duplicate_invariance", ok,
        "duplicate point prediction unchanged" if ok else f"source={pred_source}, follow={pred_follow}"
    )


def _perceptron_feature_permutation(mod) -> RelationResult:
    """Permuting feature columns consistently preserves predictions."""
    X, y = _make_binary_classification_data(70)
    fit = getattr(mod, "perceptron_fit")
    predict = getattr(mod, "perceptron_predict")

    w, b = fit(X, y, 1.0, 100)
    source_preds = predict(X, w, b)

    perm = [1, 0]
    X_perm = [[row[perm[j]] for j in range(len(row))] for row in X]
    w2, b2 = fit(X_perm, y, 1.0, 100)
    follow_preds = predict(X_perm, w2, b2)
    ok = follow_preds == source_preds
    return RelationResult(
        "perceptron_feature_permutation", ok,
        "feature permutation preserves predictions" if ok else f"source[:5]={source_preds[:5]}, follow[:5]={follow_preds[:5]}"
    )


# ---------------------------------------------------------------------------
# Discriminating classification relations: catch sign-flip / directional bugs
# Structural relations (label swap, duplicate invariance, feature permutation)
# pass global sign flips; these deep-region relations force correct orientation.
# ---------------------------------------------------------------------------


def _logreg_deep_class_region(mod) -> RelationResult:
    """A correct logistic-regression classifier puts deep points in the right class."""
    random.seed(80)
    X, y = [], []
    for _ in range(40):
        X.append([random.gauss(-3.0, 0.6), random.gauss(0.0, 0.6)])
        y.append(0)
        X.append([random.gauss(3.0, 0.6), random.gauss(0.0, 0.6)])
        y.append(1)

    fit = getattr(mod, "logistic_regression_fit")
    predict = getattr(mod, "logistic_regression_predict")
    w, b = fit(X, y, 0.1, 200)
    deep = [[-5.0, 0.0], [5.0, 0.0]]
    preds = predict(deep, w, b)
    ok = preds == [0, 1]
    return RelationResult(
        "logreg_deep_class_region", ok,
        f"deep points predicted {preds}" if ok else f"expected [0, 1], got {preds}"
    )


def _knn_deep_class_region(mod) -> RelationResult:
    """A correct kNN puts deep points in the class of their nearest cluster."""
    random.seed(82)
    X_train, y_train = [], []
    for _ in range(40):
        X_train.append([random.gauss(-3.0, 0.6), random.gauss(0.0, 0.6)])
        y_train.append(0)
        X_train.append([random.gauss(3.0, 0.6), random.gauss(0.0, 0.6)])
        y_train.append(1)

    predict = getattr(mod, "knn_predict_batch")
    deep = [[-5.0, 0.0], [5.0, 0.0]]
    preds = predict(deep, X_train, y_train, k=5)
    ok = preds == [0, 1]
    return RelationResult(
        "knn_deep_class_region", ok,
        f"deep points predicted {preds}" if ok else f"expected [0, 1], got {preds}"
    )


def _tree_deep_class_region(mod) -> RelationResult:
    """A correct decision tree puts deep points on the correct side of its split."""
    random.seed(83)
    X_train, y_train = [], []
    for _ in range(40):
        X_train.append([random.uniform(0.0, 2.5), random.uniform(0.0, 5.0)])
        y_train.append(0)
        X_train.append([random.uniform(2.5, 5.0), random.uniform(0.0, 5.0)])
        y_train.append(1)

    build = getattr(mod, "build_tree")
    predict = getattr(mod, "predict_tree")
    tree = build(X_train, y_train, max_depth=5)
    deep = [[-1.0, 2.5], [6.0, 2.5]]
    preds = [predict(p, tree) for p in deep]
    ok = preds == [0, 1]
    return RelationResult(
        "tree_deep_class_region", ok,
        f"deep points predicted {preds}" if ok else f"expected [0, 1], got {preds}"
    )


def _nb_deep_class_region(mod) -> RelationResult:
    """A correct Naive Bayes classifier labels class-typical documents correctly."""
    random.seed(84)
    spam = ["cheap", "free", "buy", "offer", "click"]
    ham = ["meeting", "report", "data", "project", "deadline"]
    texts, labels = [], []
    for _ in range(20):
        texts.append([random.choice(spam) for _ in range(random.randint(3, 5))])
        labels.append(1)
    for _ in range(20):
        texts.append([random.choice(ham) for _ in range(random.randint(3, 5))])
        labels.append(0)

    train = getattr(mod, "naive_bayes_train")
    predict = getattr(mod, "naive_bayes_predict")
    priors, probs = train(texts, labels)
    pred_spam = predict(["cheap", "free", "buy", "offer", "click"], priors, probs)
    pred_ham = predict(["meeting", "report", "data", "project", "deadline"], priors, probs)
    ok = pred_spam == 1 and pred_ham == 0
    return RelationResult(
        "nb_deep_class_region", ok,
        f"deep docs predicted spam={pred_spam}, ham={pred_ham}" if ok
        else f"expected spam=1, ham=0; got spam={pred_spam}, ham={pred_ham}"
    )


def _perceptron_deep_class_region(mod) -> RelationResult:
    """A correct perceptron puts deep points on the correct side of the boundary."""
    random.seed(85)
    X, y = [], []
    for _ in range(40):
        x1 = random.uniform(-3.0, 3.0)
        x2 = x1 - random.uniform(1.2, 2.5)
        X.append([x1, x2])
        y.append(0)
        x1 = random.uniform(-3.0, 3.0)
        x2 = x1 + random.uniform(1.2, 2.5)
        X.append([x1, x2])
        y.append(1)

    fit = getattr(mod, "perceptron_fit")
    predict = getattr(mod, "perceptron_predict")
    w, b = fit(X, y, 1.0, 200)
    deep = [[0.0, -4.0], [0.0, 4.0]]
    preds = predict(deep, w, b)
    ok = preds == [0, 1]
    return RelationResult(
        "perceptron_deep_class_region", ok,
        f"deep points predicted {preds}" if ok else f"expected [0, 1], got {preds}"
    )


# ---------------------------------------------------------------------------
# Clustering relations
# ---------------------------------------------------------------------------

def _make_kmeans_data(seed: int, n_per_cluster: int = 20):
    random.seed(seed)
    X = []
    for _ in range(n_per_cluster):
        X.append([random.gauss(0, 0.5), random.gauss(0, 0.5)])
    for _ in range(n_per_cluster):
        X.append([random.gauss(5, 0.5), random.gauss(0, 0.5)])
    for _ in range(n_per_cluster):
        X.append([random.gauss(2.5, 0.5), random.gauss(4, 0.5)])
    return X


def _best_label_mapping(source_labels: List[int], follow_labels: List[int]) -> Dict[int, int]:
    """Find a source-label -> follow-label permutation that maximizes agreement."""
    counts: Dict[Tuple[int, int], int] = {}
    for s, f in zip(source_labels, follow_labels):
        counts[(s, f)] = counts.get((s, f), 0) + 1
    source_set = sorted(set(source_labels))
    follow_set = sorted(set(follow_labels))
    mapping: Dict[int, int] = {}
    used: set = set()
    for s in source_set:
        best_f, best_count = None, -1
        for f in follow_set:
            if f in used:
                continue
            c = counts.get((s, f), 0)
            if c > best_count:
                best_f, best_count = f, c
        if best_f is None:
            best_f = follow_set[0]
        mapping[s] = best_f
        used.add(best_f)
    return mapping


def _kmeans_shift_invariance(mod) -> RelationResult:
    """Translating all points by a constant vector preserves cluster assignments."""
    X = _make_kmeans_data(80)
    fit = getattr(mod, "kmeans")

    random.seed(80)
    _, source_assignments = fit(X, k=3, max_iterations=100, tolerance=1e-4)

    shift = [10.0, -7.0]
    X_shifted = [[x[0] + shift[0], x[1] + shift[1]] for x in X]
    random.seed(80)
    _, follow_assignments = fit(X_shifted, k=3, max_iterations=100, tolerance=1e-4)

    mapping = _best_label_mapping(source_assignments, follow_assignments)
    remapped = [mapping[s] for s in source_assignments]
    ok = remapped == follow_assignments
    return RelationResult(
        "kmeans_shift_invariance", ok,
        "shifted assignments match" if ok else f"source[:10]={source_assignments[:10]}, follow[:10]={follow_assignments[:10]}"
    )


def _kmeans_scale_invariance(mod) -> RelationResult:
    """Uniformly scaling all features preserves cluster assignments."""
    X = _make_kmeans_data(82)
    fit = getattr(mod, "kmeans")

    random.seed(82)
    _, source_assignments = fit(X, k=3, max_iterations=100, tolerance=1e-4)

    scale = 3.0
    X_scaled = [[x[0] * scale, x[1] * scale] for x in X]
    random.seed(82)
    _, follow_assignments = fit(X_scaled, k=3, max_iterations=100, tolerance=1e-4)

    mapping = _best_label_mapping(source_assignments, follow_assignments)
    remapped = [mapping[s] for s in source_assignments]
    ok = remapped == follow_assignments
    return RelationResult(
        "kmeans_scale_invariance", ok,
        "scaled assignments match" if ok else f"source[:10]={source_assignments[:10]}, follow[:10]={follow_assignments[:10]}"
    )


def _kmeans_duplicate_invariance(mod) -> RelationResult:
    """Duplicating the full dataset should not change original-point assignments."""
    X = _make_kmeans_data(81)
    fit = getattr(mod, "kmeans")

    random.seed(81)
    _, source_assignments = fit(X, k=3, max_iterations=100, tolerance=1e-4)

    X_dup = X + [[x[0], x[1]] for x in X]
    random.seed(81)
    _, follow_assignments_all = fit(X_dup, k=3, max_iterations=100, tolerance=1e-4)
    follow_assignments = follow_assignments_all[: len(X)]

    mapping = _best_label_mapping(source_assignments, follow_assignments)
    remapped = [mapping.get(s, s) for s in source_assignments]
    agreement = sum(r == f for r, f in zip(remapped, follow_assignments)) / len(X)
    ok = agreement >= 0.95
    return RelationResult(
        "kmeans_duplicate_invariance", ok,
        f"duplicate agreement {agreement:.2f}" if ok else f"expected >=0.95, got {agreement:.2f}"
    )


# ---------------------------------------------------------------------------
# Optimization relations
# ---------------------------------------------------------------------------

def _gd_momentum_faster(mod) -> RelationResult:
    """Momentum GD should converge at least as fast as vanilla GD on the bowl."""
    x0, y0 = 10.0, 10.0
    vanilla = getattr(mod, "vanilla_gd")
    momentum = getattr(mod, "momentum_gd")

    iters_vanilla, fx_vanilla = vanilla(x0, y0)
    iters_momentum, fx_momentum = momentum(x0, y0)

    ok = fx_momentum < 1e-6 and fx_vanilla < 1e-6 and iters_momentum < iters_vanilla
    return RelationResult(
        "gd_momentum_faster", ok,
        f"momentum {iters_momentum} iters vs vanilla {iters_vanilla}" if ok
        else f"momentum iters={iters_momentum}, fx={fx_momentum}; vanilla iters={iters_vanilla}, fx={fx_vanilla}"
    )


REGISTRY: Dict[str, List[Relation]] = {
    "regression": [
        Relation("linreg_scale_target", "regression", _linreg_scale_target),
        Relation("linreg_shift_target", "regression", _linreg_shift_target),
        Relation("linreg_feature_permutation", "regression", _linreg_feature_permutation),
        Relation("poly_scale_target", "regression", _poly_scale_target),
        Relation("poly_shift_target", "regression", _poly_shift_target),
        Relation("ridge_scale_target", "regression", _ridge_scale_target),
        Relation("ridge_ols_approx", "regression", _ridge_ols_approx),
    ],
    "classification": [
        Relation("logreg_label_permutation", "classification", _logreg_label_permutation),
        Relation("logreg_duplicate_invariance", "classification", _logreg_duplicate_invariance),
        Relation("logreg_feature_permutation", "classification", _logreg_feature_permutation),
        Relation("logreg_deep_class_region", "classification", _logreg_deep_class_region),
        Relation("knn_label_permutation", "classification", _knn_label_permutation),
        Relation("knn_duplicate_invariance", "classification", _knn_duplicate_invariance),
        Relation("knn_feature_permutation", "classification", _knn_feature_permutation),
        Relation("knn_deep_class_region", "classification", _knn_deep_class_region),
        Relation("tree_label_permutation", "classification", _tree_label_permutation),
        Relation("tree_duplicate_invariance", "classification", _tree_duplicate_invariance),
        Relation("tree_noise_feature_invariance", "classification", _tree_noise_feature_invariance),
        Relation("tree_clean_separable", "classification", _tree_clean_separable),
        Relation("tree_deep_class_region", "classification", _tree_deep_class_region),
        Relation("nb_label_permutation", "classification", _nb_label_permutation),
        Relation("nb_duplicate_invariance", "classification", _nb_duplicate_invariance),
        Relation("nb_word_order_invariance", "classification", _nb_word_order_invariance),
        Relation("nb_deep_class_region", "classification", _nb_deep_class_region),
        Relation("perceptron_label_permutation", "classification", _perceptron_label_permutation),
        Relation("perceptron_duplicate_invariance", "classification", _perceptron_duplicate_invariance),
        Relation("perceptron_feature_permutation", "classification", _perceptron_feature_permutation),
        Relation("perceptron_deep_class_region", "classification", _perceptron_deep_class_region),
    ],
    "clustering": [
        Relation("kmeans_shift_invariance", "clustering", _kmeans_shift_invariance),
        Relation("kmeans_scale_invariance", "clustering", _kmeans_scale_invariance),
        Relation("kmeans_duplicate_invariance", "clustering", _kmeans_duplicate_invariance),
    ],
    "optimization": [
        Relation("gd_momentum_faster", "optimization", _gd_momentum_faster),
    ],
}


def _prefix_for_pattern(pattern: str) -> str:
    mapping = {
        "linear_regression_gd": "linreg_",
        "polynomial_regression": "poly_",
        "ridge_regression_normal_eq": "ridge_",
        "logistic_regression": "logreg_",
        "knn_classifier": "knn_",
        "decision_tree_id3": "tree_",
        "naive_bayes_text": "nb_",
        "perceptron": "perceptron_",
        "kmeans_clustering": "kmeans_",
        "gradient_descent_momentum": "gd_",
    }
    return mapping.get(pattern, "")


def evaluate_relations(category: str, mod: Any, pattern: str = "") -> List[RelationResult]:
    """Run all relations for a category against a loaded user module.

    If pattern is provided, skip relations whose name doesn't start with the
    pattern prefix (e.g. 'linreg_' for linear_regression_gd). This avoids
    requiring unrelated functions from alternative implementations.
    """
    prefix = _prefix_for_pattern(pattern)
    return [
        rel.check(mod)
        for rel in REGISTRY.get(category, [])
        if not prefix or rel.name.startswith(prefix)
    ]


def registry() -> Dict[str, List[Relation]]:
    return dict(REGISTRY)
