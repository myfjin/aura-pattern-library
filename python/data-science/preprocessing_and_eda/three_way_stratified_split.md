# three way stratified split

**Language:** Python · **Sphere:** data-science · **Category:** Preprocessing & EDA

**Signature:** `(data: List[tuple], labels: List[int], splits: Tuple[float, float, float]) → Tuple[List[tuple], List[tuple], List[tuple], List[int], List[int], List[int]]`

## What it does

Three-Way Stratified Split Pattern.

Partitions a dataset into train/validation/test sets while preserving class
proportions in all three splits. Core idea: stratification ensures each split
is representative of the full distribution (important for imbalanced data).

When to use: classification datasets, ensuring all class proportions preserved,
train-val-test evaluation protocols, handling imbalanced classes.

## Guarantee

When it runs, three way stratified split guarantees len(train_labels) + len(val_labels) + len(test_labels) == len(labels); abs(split_pct - full_pct) < tolerance; 0 in train_labels and 1 in train_labels (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(train_labels) + len(val_labels) + len(test_labels) == len(labels)`
- `abs(split_pct - full_pct) < tolerance`
- `0 in train_labels and 1 in train_labels`
- `0 in val_labels and 1 in val_labels`
- `0 in test_labels and 1 in test_labels`
- `len(train_set & val_set) == 0`
- `len(train_set & test_set) == 0`
- `len(val_set & test_set) == 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
