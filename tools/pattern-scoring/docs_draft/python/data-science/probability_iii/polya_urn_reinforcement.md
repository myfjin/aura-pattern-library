# Pólya Urn Reinforcement

**File:** `python/data-science/probability_iii/polya_urn_reinforcement.py`
**Sphere:** Data Science — Probability III

---

## What it solves

**Model rich-get-richer feedback where the limiting proportion is RANDOM ~ Beta(a,b).** Start with a balls of color A, b of color B. Each draw: pick a ball, return it plus one more of the same color. A single urn's proportion does NOT converge to the mean a/(a+b) — it converges to a RANDOM limit distributed as Beta(a,b). Across many urns, the limiting proportions have mean a/(a+b) AND variance matching Beta(a,b).

**When to use:** Understanding reinforcement processes — preferential attachment, word frequency evolution, any "the rich get richer" dynamic.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `a` | int > 0, initial count of color A | |
| `b` | int > 0, initial count of color B | |
| `num_draws` | int > 0, number of draws | |

---

## How inputs shape the output

- **Mean of limiting proportions matches a/(a+b)** — the Beta mean.
- **Variance of limiting proportions matches Beta variance** — the defining claim (the urn SPREADS, it does not concentrate).
- **Variance is substantial** (> 0.01) — the urn does not converge to the mean.

---

## Worked example (real run)

```
$ python3 python/data-science/probability_iii/polya_urn_reinforcement.py
PASS
```

**Reading the output:** with a=b=5, across 400 urns the mean proportion ≈ 0.5 (matches Beta mean) and variance ≈ 0.021 (matches Beta variance 0.0227). The urn spreads — it does not concentrate.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| a or b = 0 | only one color possible | deterministic |
| very few draws | hasn't converged to limit | needs more draws |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20