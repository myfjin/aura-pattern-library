# Block Maxima: Gumbel Distribution

**File:** `python/data-science/probability_iii/extreme_value_block_maxima.py`
**Sphere:** Data Science — Probability III

---

## What it solves

**Fit the Gumbel distribution to block maxima for return-level estimation.** The Gumbel distribution models the distribution of maximum values in blocks of data. Fitted parameters (μ, σ) estimate return levels: the value expected to be exceeded once every T periods.

**When to use:** Extreme value analysis — flood levels, maximum temperatures, worst-case latency, any "how bad will the worst case be?"

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `block_maxima` | List[float], maximum values per block | |
| `T` | float > 1, return period | |

---

## How inputs shape the output

- **Fitted parameters close to true** (μ within 5, σ within 3).
- **Gumbel CDF verified at median** — F(median) = 0.5 exactly.
- **Return level estimate within 2σ of true** — the defining claim.

---

## Worked example (real run)

```
$ python3 python/data-science/probability_iii/extreme_value_block_maxima.py
PASS
```

**Reading the output:** from 50 block maxima sampled from Gumbel(100, 10), the fitted parameters are within tolerance and the 100-period return level is accurately estimated.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| very few blocks | parameter estimates unreliable | needs more data |
| non-extreme data | Gumbel may not fit | wrong distribution family |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20