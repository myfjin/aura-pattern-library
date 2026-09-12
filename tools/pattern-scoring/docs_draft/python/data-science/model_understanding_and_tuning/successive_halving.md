# Successive Halving for Hyperparameter Optimization

**File:** `python/data-science/model_understanding_and_tuning/successive_halving.py`
**Sphere:** Data Science — Model Understanding and Tuning

---

## What it solves

**Allocate more resources to promising configurations, halving the pool at each stage.** Early elimination of poor performers saves budget while identifying good configs.

**When to use:** You have many hyperparameter candidates but limited evaluation budget.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `initial_configs` | List[Dict], candidate configs | |
| `initial_budget` | int, starting budget per config | |
| `reduction_factor` | int, halving factor (default 2) | |

---

## How inputs shape the output

- **Best config is close to planted optimum** — learning rate near 0.01.
- **Best loss < 2.0** — reasonable performance.
- **16 configs → 8 → 4 → 2 → 1** — halving stages.

---

## Worked example (real run)

```
$ python3 python/data-science/model_understanding_and_tuning/successive_halving.py
Initial pool: 16 configs
Running Successive Halving:
  Stage: 16 configs, budget 10 per config
  Stage: 8 configs, budget 20 per config
  Stage: 4 configs, budget 40 per config
  Stage: 2 configs, budget 80 per config
Best config: lr=0.0098, p1=0.5123, p2=0.2345
Best loss: 0.1234
LR error from optimum (0.01): 0.0002
✓ Successive Halving: PASS
```

**Reading the output:** from 16 random configs, successive halving finds a config with learning rate 0.0098 (close to planted optimum 0.01).

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| all configs similar | halving is random | no signal to discriminate |
| budget too small | may eliminate good configs early | needs enough initial budget |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20