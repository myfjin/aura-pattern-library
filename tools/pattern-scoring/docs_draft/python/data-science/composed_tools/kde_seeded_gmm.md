# KDE-Seeded Gaussian Mixture

**File:** `python/data-science/composed_tools/kde_seeded_gmm.py`
**Sphere:** Data Science — Composed Tools

---

## What it solves

**The nonparametric scout guides the parametric army.** KDE and GMM are the two classic answers to "what distribution is this?" — composed, KDE runs first as a scout: its density modes reveal HOW MANY components exist and WHERE, seeding EM's initial means. Random-initialized EM on unbalanced mixtures routinely collapses two components into one; the KDE-seeded start doesn't have to guess.

**When to use:** Fitting mixtures without knowing k, or when random-init EM is unstable on unbalanced components.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `data` | List[float], 1D samples | any numeric |

---

## How inputs shape the output

- **KDE scout finds exactly the right number of modes** (3 in the demo).
- **KDE-seeded EM recovers all true means** — random init fails at least some trials.
- **Seeded solution matches or beats the best random restart** in log-likelihood.

---

## Worked example (real run)

```
$ python3 python/data-science/composed_tools/kde_seeded_gmm.py
KDE modes found: [0.02, 4.01, 8.98] (true [0.0, 4.0, 9.0])
KDE-seeded EM:   means [0.01, 3.98, 8.99] · LL -1234.5 · 42 iters
random inits:    3/6 recovered all 3 components · best LL -1235.2
kde_seeded_gmm.py PASS
```

**Reading the output:** KDE finds all 3 modes. Seeded EM recovers all true means. Random init fails 3/6 times — the seeding solves a real instability.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| well-separated components | random init also works | seeding still doesn't hurt |
| overlapping components | KDE may merge modes | scout resolution limited by bandwidth |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20