# Interleaving Significance

**File:** `python/data-science/composed_tools/interleaving_significance.py`
**Sphere:** Data Science — Composed Tools

---

## What it solves

**The duel names a winner; the bootstrap says if it's real.** Team-draft interleaving is more sensitive than a split A/B test, but people report it as a bare win-count — no confidence. This composition collects interleaving's PER-QUERY paired preference and feeds it to the paired bootstrap: a confidence interval on the mean preference. A genuine ranker edge gives a CI that excludes zero; two equal rankers give a CI that straddles zero.

**When to use:** You need to compare two ranking systems with statistical confidence, especially when the better system wins fewer queries but by larger margins.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `ranking_a`, `ranking_b` | List[str], document rankings | same documents |
| `relevance` | dict, relevance scores per doc | 0–1 scale |

---

## How inputs shape the output

- **Raw per-query win-count can mislead:** A may win fewer queries but by larger margins.
- **The signed-credit bootstrap CI reveals the real edge** — the defining claim.
- **Two equal rankers give a CI straddling zero** — no false positive.

---

## Worked example (real run)

```
$ python3 python/data-science/composed_tools/interleaving_significance.py
A-better: raw per-query wins 107/300 · mean credit +0.123 · 95% CI [+0.045, +0.201]  SIGNIFICANT
null    : mean credit +0.002 · 95% CI [-0.078, +0.081]  correctly n.s.
interleaving_significance.py PASS
```

**Reading the output:** A wins only 107/300 queries (under half) — raw counts would say B wins. But the signed-credit CI [+0.045, +0.201] excludes zero, revealing A's real edge. The null case correctly shows a CI straddling zero.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| identical rankers | CI straddles zero | correct — no false positive |
| very few queries | CI may be wide | low power |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20