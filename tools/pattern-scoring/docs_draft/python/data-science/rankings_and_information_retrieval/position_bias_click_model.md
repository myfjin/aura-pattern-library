# Position Bias in Click Models and Inverse Propensity Weighting

**File:** `python/data-science/rankings_and_information_retrieval/position_bias_click_model.py`
**Sphere:** Data Science — Rankings and Information Retrieval

---

## What it solves

**Users click documents based on both relevance and position (position bias).** Naive click-count ranking is confounded by position — a relevant doc at position 3 gets fewer clicks than an irrelevant doc at position 1. Inverse propensity weighting (IPW) corrects for position bias and recovers the true relevance order.

**When to use:** Analyzing click data from search logs where position bias distorts raw click counts.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `ranking` | List[str], document ranking | |
| `true_relevances` | Dict[str, float], ground-truth relevance | 0–1 scale |
| `position_bias` | float, bias strength | higher = stronger position effect |

---

## How inputs shape the output

- **Naive ranking is distorted by position bias** — the most relevant doc (at position 3) is not ranked first.
- **IPW recovers the true relevance order** — A (most relevant) ranks first after correction.
- **IPW ranking matches true ranking** better than naive.

---

## Worked example (real run)

```
$ python3 python/data-science/rankings_and_information_retrieval/position_bias_click_model.py
True ranking: ['A', 'B', 'C', 'D'] | Naive (biased): ['D', 'C', 'B', 'A'] | IPW (corrected): ['A', 'B', 'C', 'D'] | PASS
```

**Reading the output:** naive click-count ranks D first (it's at position 1, gets clicks from position bias). IPW corrects for position and recovers the true order A > B > C > D.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| no position bias | naive = IPW | correction has no effect |
| wrong position_bias parameter | IPW may over/under-correct | needs accurate bias estimate |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20