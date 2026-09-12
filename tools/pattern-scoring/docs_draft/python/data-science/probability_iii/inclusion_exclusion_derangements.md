# Inclusion-Exclusion: Derangements

**File:** `python/data-science/probability_iii/inclusion_exclusion_derangements.py`
**Sphere:** Data Science — Probability III

---

## What it solves

**Count derangements (permutations with no fixed points) via inclusion-exclusion.** !n = n! · Σ (−1)^k / k! ≈ n! / e. For n=10, !10 = 1,334,961 and !n/n! ≈ 0.368 = 1/e. The exact formula matches simulation.

**When to use:** Understanding the probability that a random permutation has no fixed points — secret santa, password resets, any "nothing stays in place" problem.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `n` | int ≥ 0 | |

---

## How inputs shape the output

- **!n = n! · Σ (−1)^k / k!** — exact formula via inclusion-exclusion.
- **!n / n! → 1/e ≈ 0.368** as n → ∞ — verified for n=10.
- **Simulation matches exact proportion** within 5%.

---

## Worked example (real run)

```
$ python3 python/data-science/probability_iii/inclusion_exclusion_derangements.py
PASS
```

**Reading the output:** for n=10, !10/10! ≈ 0.368 = 1/e. Simulated proportion matches exact within 5%.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| n = 0 | !0 = 1 | correct (empty permutation) |
| n = 1 | !1 = 0 | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20