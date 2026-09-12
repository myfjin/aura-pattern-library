"""
Three-Way Stratified Split Pattern.

Partitions a dataset into train/validation/test sets while preserving class
proportions in all three splits. Core idea: stratification ensures each split
is representative of the full distribution (important for imbalanced data).

When to use: classification datasets, ensuring all class proportions preserved,
train-val-test evaluation protocols, handling imbalanced classes.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple
import random


def stratified_split(
    data: List[tuple], labels: List[int], splits: Tuple[float, float, float] = (0.6, 0.2, 0.2)
) -> Tuple[List[tuple], List[tuple], List[tuple], List[int], List[int], List[int]]:
    """
    Split data into train/val/test preserving class proportions.
    Args:
        data: List of samples
        labels: List of class labels
        splits: (train_frac, val_frac, test_frac), must sum to 1.0
    Returns:
        (train_data, val_data, test_data, train_labels, val_labels, test_labels)
    """
    if not (0.99 <= sum(splits) <= 1.01):
        raise ValueError(f"Splits must sum to ~1.0, got {sum(splits)}")

    train_frac, val_frac, test_frac = splits

    # Group by class
    class_groups = {}
    for i, label in enumerate(labels):
        if label not in class_groups:
            class_groups[label] = []
        class_groups[label].append(i)

    train_indices = []
    val_indices = []
    test_indices = []

    # Stratified split within each class
    for label, indices in class_groups.items():
        # Shuffle within class
        random.shuffle(indices)
        n_class = len(indices)

        n_train = max(1, int(n_class * train_frac))
        n_val = max(1, int(n_class * val_frac))
        n_test = n_class - n_train - n_val

        train_indices.extend(indices[:n_train])
        val_indices.extend(indices[n_train : n_train + n_val])
        test_indices.extend(indices[n_train + n_val :])

    # Shuffle combined splits
    random.shuffle(train_indices)
    random.shuffle(val_indices)
    random.shuffle(test_indices)

    train_data = [data[i] for i in train_indices]
    val_data = [data[i] for i in val_indices]
    test_data = [data[i] for i in test_indices]

    train_labels = [labels[i] for i in train_indices]
    val_labels = [labels[i] for i in val_indices]
    test_labels = [labels[i] for i in test_indices]

    return train_data, val_data, test_data, train_labels, val_labels, test_labels


def class_proportion(labels: List[int]) -> dict:
    """Compute class proportions."""
    total = len(labels)
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    return {label: count / total for label, count in counts.items()}


if __name__ == "__main__":
    random.seed(42)

    # Synthetic imbalanced dataset
    # Class 0: 70 samples, Class 1: 30 samples
    n0 = 70
    n1 = 30
    data = list(range(n0 + n1))
    labels = [0] * n0 + [1] * n1

    train_data, val_data, test_data, train_labels, val_labels, test_labels = stratified_split(
        data, labels, splits=(0.6, 0.2, 0.2)
    )

    # Compute proportions
    full_prop = class_proportion(labels)
    train_prop = class_proportion(train_labels)
    val_prop = class_proportion(val_labels)
    test_prop = class_proportion(test_labels)

    # Verify counts sum
    assert len(train_labels) + len(val_labels) + len(test_labels) == len(labels), "Count mismatch"

    # Verify proportions preserved within tolerance (5%)
    tolerance = 0.05
    for split_name, split_prop in [("train", train_prop), ("val", val_prop), ("test", test_prop)]:
        for class_label, full_pct in full_prop.items():
            split_pct = split_prop.get(class_label, 0)
            assert (
                abs(split_pct - full_pct) < tolerance
            ), f"{split_name} class {class_label}: {split_pct:.3f} vs {full_pct:.3f}"

    # Verify all classes present in all splits
    assert 0 in train_labels and 1 in train_labels, "Train missing class"
    assert 0 in val_labels and 1 in val_labels, "Val missing class"
    assert 0 in test_labels and 1 in test_labels, "Test missing class"

    # Verify no overlap
    train_set = set(train_data)
    val_set = set(val_data)
    test_set = set(test_data)
    assert len(train_set & val_set) == 0, "Train-val overlap"
    assert len(train_set & test_set) == 0, "Train-test overlap"
    assert len(val_set & test_set) == 0, "Val-test overlap"

    print("three_way_stratified_split.py: PASS")
