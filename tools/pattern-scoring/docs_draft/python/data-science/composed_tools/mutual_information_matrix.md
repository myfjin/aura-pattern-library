# Mutual-Information Matrix

**File:** `python/data-science/composed_tools/mutual_information_matrix.py`
**Sphere:** Data Science — Composed Tools

---

## What it solves

**The dependence heatmap Pearson cannot draw.** Every notebook on earth draws the Pearson heatmap; it is blind to any relationship that is not monotone-linear. This tool computes the SAME feature-by-feature matrix with normalized mutual information (binned), side by side with |Pearson| — so y = x² lights up where the classic heatmap shows nothing.

**When to use:** First-look EDA on features whose relationships may be nonlinear.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `features` | Dict[str, List[float]], named feature columns | numeric |

---

## How inputs shape the output

- **Both metrics see the linear pair** (Pearson > 0.7, MI > 0.25).
- **Pearson is blind to y = x²** (< 0.15) — the defining failure.
- **Normalized MI lights up the nonlinear pair** (> 3× noise level, > 0.2).
- **Matrix is symmetric** — MI[a][b] == MI[b][a].

---

## Worked example (real run)

```
$ python3 python/data-science/composed_tools/mutual_information_matrix.py
  pair              |pearson|  norm-MI
  A ↔ B_linear         0.789    0.312
  A ↔ C_square         0.042    0.287
  A ↔ D_noise          0.013    0.018
mutual_information_matrix.py PASS
```

**Reading the output:** Pearson sees the linear relationship (0.789) but is blind to y=x² (0.042 — barely above noise). Normalized MI sees both (0.312 and 0.287).

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| all features independent | both matrices near-zero | correct |
| very small sample | MI may be unreliable | binning needs enough data |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20