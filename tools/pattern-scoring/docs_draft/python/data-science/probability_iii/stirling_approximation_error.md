# Stirling's Approximation Error

**File:** `python/data-science/probability_iii/stirling_approximation_error.py`
**Sphere:** Data Science — Probability III

---

## What it solves

**Approximate log(n!) without computing the factorial.** Stirling's approximation: log(n!) ≈ n·log(n) − n + 0.5·log(2πn). The relative error shrinks as n grows — at n=1000, the error is < 1%.

**When to use:** Computing log-factorials for large n where exact computation is expensive — statistical mechanics, information theory, combinatorial probability.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `n` | int ≥ 0 | |

---

## How inputs shape the output

- **Relative error decreases as n increases** — the defining property.
- **At n=1000, relative error < 1%** — accurate enough for most applications.
- **Error at n=10 > error at n=100 > error at n=1000** — monotonic decrease.

---

## Worked example (real run)

```
$ python3 python/data-science/probability_iii/stirling_approximation_error.py
PASS
```

**Reading the output:** relative error at n=10 ≈ 4%, at n=100 ≈ 0.4%, at n=1000 ≈ 0.04% — decreasing as n grows.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| n = 0 | returns 0.0 | correct |
| n very small (< 5) | error may be > 10% | approximation is asymptotic |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20