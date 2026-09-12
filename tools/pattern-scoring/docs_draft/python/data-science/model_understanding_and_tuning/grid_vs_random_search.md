# Grid Search vs Random Search

**File:** `python/data-science/model_understanding_and_tuning/grid_vs_random_search.py`
**Sphere:** Data Science — Model Understanding and Tuning

---

## What it solves

**When hyperparameter space is high-dimensional but only a few params matter, random search explores more efficiently than grid search.** Random search finds comparable quality with fewer evaluations.

**When to use:** You have many hyperparams but limited evaluation budget.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `param_ranges` | Dict[str, Tuple[float, float]], param bounds | |
| `num_values` | int, values per param for grid | |
| `num_samples` | int, samples for random search | |

---

## How inputs shape the output

- **Random search finds near-optimal quality** with fewer evaluations than grid.
- **Grid search: 3 values × 3 params = 27 evaluations.**
- **Random search: 20 samples** — fewer evals, comparable quality.

---

## Worked example (real run)

```
$ python3 python/data-science/model_understanding_and_tuning/grid_vs_random_search.py
Grid Search (3 values per param, 27 total):
  Best score: -0.0012, Evals: 27
Random Search (20 samples):
  Best score: -0.0008, Evals: 20
✓ Grid vs Random Search: PASS
```

**Reading the output:** random search (20 evals) finds comparable quality to grid search (27 evals) when only 1 of 3 params matters.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| all params matter | grid may be better | random still competitive |
| very small budget | both may miss optimum | needs more evaluations |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20