# Group-By Aggregation (Multi-Key)

**File:** `python/data-science/data_wrangling_from_scratch/group_by_aggregate.py`
**Sphere:** Data Science — Data Wrangling from Scratch

---

## What it solves

**Split your data into groups, then summarize each group.** The SQL `GROUP BY` or pandas `groupby()` — implemented from scratch. Group records by one or more keys (e.g. category + region), then aggregate a value column (sum, mean, count, min, max). Verified against a brute-force nested-loop computation on the same data.

**When to use:** You need to understand how group-by aggregation works under the hood, or you're in a constrained environment where pandas/SQL aren't available. Every data analysis starts with group-by — this is the minimal honest version.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `records` | list of dicts with the expected keys | empty → `{}` |
| `group_keys` | list of str keys present in each record | missing key → KeyError |
| `agg_col` | str key present in each record | missing → KeyError |
| `agg_func` | one of "sum", "mean", "count", "min", "max" | unknown → KeyError |

---

## How inputs shape the output

- **Group keys determine granularity:** `["category", "region"]` gives finer groups than `["category"]` alone. More keys = more groups = fewer records per group.
- **Aggregation function changes the summary:** sum → total per group; mean → average; count → how many; min/max → range boundaries.
- **The brute-force verifier proves correctness:** every aggregation is checked against a naive nested-loop implementation — if they disagree, the test fails.

---

## Worked example (real run)

```
$ python3 python/data-science/data_wrangling_from_scratch/group_by_aggregate.py
Sum (cat, region): {('A', 'US'): 30, ('A', 'EU'): 15, ('B', 'US'): 5, ('B', 'EU'): 55} | Mean (cat): {('A',): 15.0, ('B',): 20.0} | Count (region): {('US',): 2, ('EU',): 3} | Min (cat): {('A',): 10, ('B',): 5} | PASS
```

**Reading the output:** category A has 30 total in US (10+20), 15 in EU. Mean of A is 15.0, B is 20.0. US has 2 records, EU has 3. All verified against brute force.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| empty records | returns `{}` | correct |
| missing key in record | KeyError | honest failure |
| unknown agg_func | KeyError in dispatch | needs explicit guard |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18 · evidence: `output/manual_audit_2026-07-19.csv`
