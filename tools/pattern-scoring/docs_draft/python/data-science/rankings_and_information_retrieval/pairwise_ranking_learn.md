# Pairwise Ranking via Logistic Regression

**File:** `python/data-science/rankings_and_information_retrieval/pairwise_ranking_learn.py`
**Sphere:** Data Science — Rankings and Information Retrieval

---

## What it solves

**Learn item ordering from pairwise comparisons.** For each pair (i,j), fit logistic regression on feature difference (f_i − f_j) to predict which ranks higher. The learned model recovers the planted order with high Kendall tau correlation.

**When to use:** Learning to rank when you have pairwise preference data — "item A should rank above item B."

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `items` | List[str], item IDs | |
| `features` | List[float], feature values per item | should correlate with rank |
| `true_order` | List[str], ground-truth ranking | |

---

## How inputs shape the output

- **Learned model recovers the planted order** with Kendall tau > 0.7.
- **Logistic regression on pairwise differences** learns a linear scoring function.
- **Weight and bias reflect the feature-to-rank mapping.**

---

## Worked example (real run)

```
$ python3 python/data-science/rankings_and_information_retrieval/pairwise_ranking_learn.py
True order: ['A', 'B', 'C', 'D', 'E'] | Predicted: ['A', 'B', 'C', 'D', 'E'] | Weight=0.52 | Bias=0.01 | Kendall tau=1.00 | PASS
```

**Reading the output:** the logistic model recovers the exact true order (Kendall tau = 1.0) from pairwise comparisons.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| features uncorrelated with rank | low Kendall tau | not learnable from features |
| very few items | unreliable gradient estimates | needs more data |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20