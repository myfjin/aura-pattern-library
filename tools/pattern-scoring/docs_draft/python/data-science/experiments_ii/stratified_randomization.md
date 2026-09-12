# Stratified Randomization

**File:** `python/data-science/experiments_ii/stratified_randomization.py`
**Sphere:** Data Science — Experiments II

---

## What it solves

**Better experiments through smarter randomization.** Simple randomization can leave your treatment and control groups imbalanced on important covariates by chance. Stratified randomization splits the data into strata (e.g. by age group or gender) and randomizes within each stratum, ensuring balance. This pattern demonstrates that stratified randomization produces better covariate balance and lower estimator variance than simple randomization.

**When to use:** You have a known covariate that affects the outcome, and you want to ensure balance across treatment groups. Common in clinical trials, A/B tests with known confounders, and any experiment where covariate balance matters.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `n` | int > 0, sample size | — |
| `reps` | int > 0, replications | — |
| `x` (covariate) | list of float | — |

---

## How inputs shape the output

- **Stratification improves balance:** the absolute difference in covariate means between treatment and control is smaller with stratified randomization.
- **Stratification reduces variance:** the ATE estimator has lower variance under stratified randomization because the covariate is balanced.
- **The effect is reproducible across replications:** 50 replications show the pattern consistently.

---

## Worked example (real run)

```
$ python3 python/data-science/experiments_ii/stratified_randomization.py
PASS
```

**Reading the output:** stratified randomization achieves better covariate balance and lower variance than simple randomization, averaged over 50 replications.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| odd n within stratum | one extra unit in treatment or control | minor imbalance |
| single stratum | equivalent to simple randomization | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18
