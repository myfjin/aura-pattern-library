# Forest Size by Variance

**File:** `python/data-science/composed_tools/forest_size_by_variance.py`
**Sphere:** Data Science — Composed Tools

---

## What it solves

**Stop hiring trees when the crew is steady enough.** Practitioners guess n_trees (default 100) or grid-search it. This composition runs the bias-variance decomposition's bootstrap estimator ACROSS forest sizes: bias stays flat (more trees don't change what the forest is biased toward) while ensemble variance falls as ~1/n. The data-driven size is the DIMINISHING-RETURNS knee: the smallest forest that captures most of the achievable variance reduction.

**When to use:** You need to choose a random forest size with evidence, not a default.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `X` | List[Point], 2D features | numeric |
| `y` | List[int], binary labels | 0/1 |

---

## How inputs shape the output

- **Variance falls substantially** with more trees (≥3× drop from 1 to 32 trees).
- **Bias stays ~flat** while variance falls — the whole premise.
- **The knee is an interior size** (4–16), not an extreme — the composition finds a real tradeoff.

---

## Worked example (real run)

```
$ python3 python/data-science/composed_tools/forest_size_by_variance.py
  trees= 1  bias²=0.123  variance=0.0456
  trees= 2  bias²=0.120  variance=0.0234
  trees= 4  bias²=0.121  variance=0.0123
  trees= 8  bias²=0.119  variance=0.0067
  trees=16  bias²=0.120  variance=0.0034
  trees=32  bias²=0.118  variance=0.0018
chosen forest size (80% variance-reduction knee): 8 (captures 85% of the achievable reduction)
forest_size_by_variance.py PASS
```

**Reading the output:** variance drops from 0.0456 (1 tree) to 0.0018 (32 trees). Bias stays ~0.12 throughout. The 80% knee is at 8 trees — past that, each doubling buys diminishing returns.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| very easy problem | 1 tree may be enough | knee at minimum |
| very hard problem | knee may be at maximum | needs more trees than tested |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20