# Benford's Law Test

**File:** `python/data-science/probability_iii/benford_law_test.py`
**Sphere:** Data Science — Probability III

---

## What it solves

**Test whether a dataset follows Benford's law: P(digit d) = log₁₀(1 + 1/d).** Multiplicative data (powers of 2, stock prices, population sizes) follows Benford; uniform data violates it. Uses a chi-square test to measure fit.

**When to use:** Fraud detection, data integrity checks — Benford's law is a natural fingerprint of multiplicative processes.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `data` | List[float], numeric values | non-zero |

---

## How inputs shape the output

- **Multiplicative data fits Benford better** (lower chi-square) than uniform data.
- **Leading digit extraction** scales by powers of 10 into [1,10) — correct for values < 1.
- **Chi-square statistic** measures goodness of fit.

---

## Worked example (real run)

```
$ python3 python/data-science/probability_iii/benford_law_test.py
PASS
```

**Reading the output:** powers of 2 (multiplicative) have lower chi-square than uniform data — confirming Benford's law.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| all zeros | leading digit = 0, excluded | correct |
| very small sample | chi-square unreliable | needs more data |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20