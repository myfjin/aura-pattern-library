# Online Bagging via Poisson(1) Weighting

**File:** `python/data-science/streaming_iii/online_bagging_poisson.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Bag an ensemble over a stream in one pass with bounded memory.** Batch bagging resamples each point ~Binomial(n, 1/n) times, which → Poisson(1) as n grows. Online bagging (Oza & Russell, 2001) draws k ~ Poisson(1) per arriving point per model and updates that model with weight k — no stored dataset, one pass. Oza's theorem: the online ensemble converges to the batch-bagging ensemble.

**When to use:** You need to train an ensemble on a stream where you can't store the data — and you need the same guarantees as batch bagging.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `Xtr` | list of feature vectors | numeric features |
| `ytr` | list of labels (0/1) | binary classification |
| `thresholds` | list of split candidates | should cover feature range |
| `n_models` | int > 0, ensemble size | larger = more diverse |

---

## How inputs shape the output

- **Oza's convergence theorem:** online bagging reproduces batch bagging — the demo proves prediction agreement ≥ 99% and matching accuracy.
- **Real diversity:** the ensemble produces ≥ 3 distinct stumps and differs from a single stump (agreement < 90%).
- **Denoising:** on 20% label noise, the bagged ensemble beats a single stump by > 3%.

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/online_bagging_poisson.py
online=0.888 batch=0.888 single=0.842 | online==batch agree=0.999  ensemble-vs-single agree=0.570  distinct=75
Online bagging (Poisson) PASS
```

**Reading the output:** online and batch bagging agree on 99.9% of test predictions and match in accuracy (88.8%). Both beat the single stump (84.2%) by a clear margin. All 75 stumps are distinct — a real ensemble.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| no label noise | ensemble still matches batch | convergence holds regardless |
| very few models (< 5) | may not beat single stump | not enough diversity |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20