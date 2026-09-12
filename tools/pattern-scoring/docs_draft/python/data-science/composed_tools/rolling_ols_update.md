# Rolling OLS Update

**File:** `python/data-science/composed_tools/rolling_ols_update.py`
**Sphere:** Data Science — Composed Tools

---

## What it solves

**A running balance instead of a recount.** Sliding window regression REFITS OLS from scratch every step — O(window) work per sample. Since the OLS slope is just cov(x,y)/var(x), this composition maintains the window's covariance INCREMENTALLY (subtract the departing point, add the arriving point, Welford-style) and reads the slope off it: identical coefficients, O(1) per step instead of O(window).

**When to use:** You need time-varying regression coefficients on a high-frequency stream where O(window) per step is too expensive.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `xs`, `ys` | List[float], paired observations | numeric |
| `w` | int > 0, window size | larger = smoother, slower to adapt |

---

## How inputs shape the output

- **Rolling equals naive refit to machine precision** (max deviation < 1e-8).
- **Tracks planted slope changes** (0.5 → 2.5) correctly.
- **Rolling does < 10% of refit's work** — O(1) vs O(w) per step.

---

## Worked example (real run)

```
$ python3 python/data-science/composed_tools/rolling_ols_update.py
windows: 361 · max slope deviation naive-vs-rolling: 3.45e-15
tracked slope: early 0.48 (true 0.5) · late 2.47 (true 2.5)
per-step work: rolling 800 vs refit 14440 (5.5%)
rolling_ols_update.py PASS
```

**Reading the output:** rolling and refit agree to machine precision. Both track the planted slope change. Rolling does 5.5% of refit's work.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| constant x in window | division by near-zero | slope clamped to 0 |
| window size 1 | no slope possible | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20