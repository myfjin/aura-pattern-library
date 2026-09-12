# Peeking Alpha Inflation

**File:** `python/data-science/experiments_ii/peeking_alpha_inflation.py`
**Sphere:** Data Science — Experiments II

---

## What it solves

**The silent p-value cheat.** You run an A/B test, peek at the p-value halfway through, see it's not significant yet, so you keep collecting data and test again. This "peeking" inflates your type-I error rate from the nominal 5% to 20-30% — you're much more likely to declare a false positive. This pattern demonstrates the inflation by comparing fixed-n testing (no peeking) against a peeking strategy under the null hypothesis.

**When to use:** Any time you run experiments and are tempted to check results early. The rule: if you peek, you must adjust your stopping rule (sequential testing, alpha spending). This pattern shows you exactly how much damage peeking does.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `n_per_arm` | int > 0 | — |
| `n_looks` | int ≥ 1, number of interim analyses | 1 → same as fixed-n |
| `reps` | int > 0, Monte Carlo replications | — |

---

## How inputs shape the output

- **More peeks = more inflation:** 5 interim looks inflates type-I from ~5% to ~15-25%. More looks = worse.
- **The fixed-n baseline is honest:** with no peeking, the type-I error stays near the nominal 5% (within Monte Carlo error).
- **The inflation is measurable and reproducible:** 2000 replications give stable estimates. The assert requires peeking to at least double the type-I rate.

---

## Worked example (real run)

```
$ python3 python/data-science/experiments_ii/peeking_alpha_inflation.py
PASS — no_peek=0.055  peek=0.195  3.5x inflation
```

**Reading the output:** fixed-n testing has 5.5% type-I (close to nominal 5%). Peeking 5 times inflates it to 19.5% — a 3.5× increase. You're nearly 4× more likely to see a false positive.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| `n_per_arm < 2` | returns 1.0 (degenerate) | needs guard |
| `reps = 0` | ZeroDivision | needs guard |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18
