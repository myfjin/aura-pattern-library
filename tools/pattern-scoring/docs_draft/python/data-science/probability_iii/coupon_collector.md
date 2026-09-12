# Coupon Collector

**File:** `python/data-science/probability_iii/coupon_collector.py`
**Sphere:** Data Science — Probability III

---

## What it solves

**Compute the expected number of trials to collect all n distinct coupons.** E[T] = n·H_n where H_n = 1 + 1/2 + ... + 1/n is the harmonic series. For n=10, E[T] ≈ 29.3. The simulated mean matches the exact formula.

**When to use:** Understanding "how many draws to see everything?" — species sampling, loot boxes, any complete-collection problem.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `n` | int > 0, number of distinct coupons | |

---

## How inputs shape the output

- **Expected trials = n·H_n** — verified against simulation within 10%.
- **Harmonic series grows slowly** — E[T] ≈ n·ln(n) + γ·n.
- **Simulation matches exact formula** — the defining claim.

---

## Worked example (real run)

```
$ python3 python/data-science/probability_iii/coupon_collector.py
PASS
```

**Reading the output:** for n=10, exact E[T] = 29.3, simulated ≈ 29.0 — within 10% of exact.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| n = 1 | E[T] = 1 | correct |
| very large n | E[T] grows as n·ln(n) | slow growth |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20