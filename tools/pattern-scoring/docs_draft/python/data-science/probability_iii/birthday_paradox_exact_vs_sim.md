# Birthday Paradox: Exact vs Simulated

**File:** `python/data-science/probability_iii/birthday_paradox_exact_vs_sim.py`
**Sphere:** Data Science — Probability III

---

## What it solves

**Compute the probability that ≥2 people share a birthday among n people.** P(≥2 same birthday) ≈ 1 − n!/(365^n · (365−n)!). For n=23, P ≈ 50% — the famous birthday paradox. The exact formula matches simulation.

**When to use:** Understanding collision probability — hash collisions, random sampling, any "how many before a duplicate?" problem.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `n` | int > 0, number of people | |
| `days` | int > 0, number of possible values (default 365) | |

---

## How inputs shape the output

- **n=23 gives P ≈ 50%** — the famous result.
- **Exact formula matches simulation** within 10%.
- **For n > days, P = 1.0** — pigeonhole principle.

---

## Worked example (real run)

```
$ python3 python/data-science/probability_iii/birthday_paradox_exact_vs_sim.py
PASS
```

**Reading the output:** for n=23, exact P ≈ 0.507, simulated P ≈ 0.51 — both close to 50%.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| n = 1 | P = 0 | correct |
| n > days | P = 1.0 | pigeonhole principle |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20