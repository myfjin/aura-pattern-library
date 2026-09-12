# Threshold Tuning with Asymmetric Costs

**File:** `python/data-science/model_understanding_and_tuning/threshold_tuning_cost.py`
**Sphere:** Data Science — Model Understanding and Tuning

---

## What it solves

**Binary classifiers typically use 0.5 threshold, but with asymmetric costs (e.g., false negatives cost more than false positives), the optimal threshold shifts.** Grid search over thresholds finds the minimum-cost decision boundary.

**When to use:** Fraud detection (missing fraud = high cost) or spam filtering (blocking users = high cost).

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `y_true` | List[float], true labels | |
| `y_scores` | List[float], predicted scores | |
| `cost_fp` | float, cost of false positive | |
| `cost_fn` | float, cost of false negative | |

---

## How inputs shape the output

- **Optimal threshold < 0.5** when FN cost > FP cost — the defining shift.
- **Optimal cost < default cost** — meaningful improvement.
- **Cost reduction > 20%** — significant savings.

---

## Worked example (real run)

```
$ python3 python/data-science/model_understanding_and_tuning/threshold_tuning_cost.py
Default threshold 0.5 cost: 45.0
Optimal threshold: 0.32, cost: 25.0
Improvement: 44.4%
✓ Threshold Tuning with Asymmetric Costs: PASS
```

**Reading the output:** with FN cost 10× FP cost, the optimal threshold shifts from 0.5 to 0.32, reducing total cost by 44%.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| symmetric costs | optimal threshold ≈ 0.5 | correct |
| perfect classifier | any threshold works | cost = 0 |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20