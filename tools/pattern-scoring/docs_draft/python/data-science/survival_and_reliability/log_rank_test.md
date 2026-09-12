# Log-Rank Test for Survival Curves

**File:** `python/data-science/survival_and_reliability/log_rank_test.py`
**Sphere:** Data Science — Survival and Reliability
**Status:** PASS-WITH-FLAG (Illia's audit 2026-07-19)

---

## What it solves

"Do two groups survive differently?" The workhorse of medical trials: treatment vs control, does one live longer? Survival data is special because of **censoring** — some patients leave the study alive (outcome unknown, `event=0`); you can't just average. The log-rank test compares the observed vs expected deaths at each moment someone dies, across both groups, and returns a statistic + p-value. Low p → the groups really differ; high p → no evidence they do.

**When to use:** You have time-to-event data with censoring and want to know if two groups have different survival curves. This is the standard nonparametric test — no assumptions about the shape of the survival curves.

---

## How to drive it

```python
# event=1 means "died/failed observed"; event=0 means "censored" (left study alive)
z, p = log_rank_test(times_g1, events_g1, times_g2, events_g2)
# low p (<0.05) → groups differ · high p → fail to reject "same survival"
```

Variations to reason about:
- **more deaths, clearer separation** → lower p (more evidence).
- **all censored (all events=0)** → no deaths to compare → the var<ε guard returns (0.0, 1.0).
- **same distribution, independent draws** → high p (the demo's honest null — NOT the same array twice, which would force z=0 by identity; the author documented this distinction, a good sign).

---

## Valid inputs (the contract — to be enforced per fix #12)

| Input | Domain | Today → |
|---|---|---|
| `times_g*` / `events_g*` | equal length within each group | too-SHORT events → IndexError · too-LONG → **silently ignored (PASS)** |
| `events` | each in {0, 1} | `5` → silently treated as censored → confident (0.0, 1.0) |
| `times` | ≥ 0 (survival time) | negative runs silently (sort is sign-agnostic) |

---

## Failure modes (audited by hand)

| Trigger | What happens today | Meaning |
|---|---|---|
| events longer than times (330 vs 30) | **PASS** — extra flags ignored | asymmetric: short crashes, long passes silently |
| events shorter than times | IndexError (accidental) | same defect, opposite face |
| corrupt the `var < 1e-14` epsilon to `1e-144` | **still PASS** | that branch has ZERO test coverage — untested code in a VERIFIED pattern (hand-mutation find) |
| event flag = 5 | `(0.0, 1.0)` — silently "censored" | invalid flag reinterpreted, confident output from corrupt data |
| all censored / negative time | degenerate-handled / silently run | first is defensible; second is physically impossible |

**The mutation-testing lesson:** Illia changed a constant deep in the code and NO assert noticed — proof the safety branch is never exercised. A test suite that stays green under mutation is not testing that line. This is exactly what the validation tool's oracle-weakness scanner (v1.5) automates.

---

## Worked example (real run)

```
$ python3 python/data-science/survival_and_reliability/log_rank_test.py
PASS
```

Seed 42: different groups p≈0.036 (reject equality), same-distribution p≈0.83 (fail to reject). The null uses two INDEPENDENT samples from one distribution — a real statistical outcome, not a vacuous identity. (Receipts-poor output noted; retrofit prints the two p-values.)

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18 · Illia's audit 2026-07-19: PASS-WITH-FLAG; asymmetric-mismatch + zero-coverage branch (mutation) + flag-reinterpret → fix #12 · evidence: `output/manual_audit_2026-07-19.csv`
