# Hoeffding Tree (VFDT) Lite — Streaming Decision Stump

**File:** `python/data-science/streaming_iii/hoeffding_tree_lite.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Grow a decision tree online with a statistical guarantee on each split decision.** The Hoeffding bound says: after n samples, the true information gain of a split is within ε = √(R²·ln(1/δ) / 2n) of its observed gain. As soon as the best candidate's observed gain beats the runner-up by more than ε, that split is provably the true best with probability ≥ 1−δ.

**When to use:** You need to train a decision tree on a stream where data arrives one sample at a time and you can't store it all — the Very Fast Decision Tree (VFDT) family.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `X` | list of feature vectors | numeric features only |
| `y` | list of labels (0/1) | binary classification |
| `thresholds` | list of split candidates | should cover the feature range |
| `delta` | float > 0, confidence | smaller = more samples needed |

---

## How inputs shape the output

- **Hoeffding bound drives the split decision:** the algorithm waits until the gap between the best and second-best split exceeds the bound — then it's statistically safe to split.
- **The split matters:** the demo proves the streaming stump beats the majority baseline by >25% and matches a batch-trained stump within 3%.
- **Confidence δ controls patience:** smaller δ = tighter bound = more samples needed before splitting. The demo's δ=1e-6 is conservative.

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/hoeffding_tree_lite.py
streaming split: feature=0 thr=0.6 after n=2000
test acc: streaming=0.998 batch=0.999 majority=0.500
Hoeffding tree PASS
```

**Reading the output:** the streaming stump correctly identifies feature 0 with threshold 0.6 as the best split (the true concept is x[0] > 0.6 → class 1). It achieves 99.8% test accuracy, matching the batch stump.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| no informative feature | split never fires | correct — no split is justified |
| delta too small for stream length | never splits | needs more data |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20