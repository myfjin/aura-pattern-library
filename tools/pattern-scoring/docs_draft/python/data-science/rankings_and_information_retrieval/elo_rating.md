# Elo Rating System

**File:** `python/data-science/rankings_and_information_retrieval/elo_rating.py`
**Sphere:** Data Science — Rankings and Information Retrieval

---

## What it solves

**Maintain skill ratings via pairwise wins/losses.** Elo(new) = Elo(old) + K × (observed − expected). Expected score = 1 / (1 + 10^((opponent_elo − my_elo)/400)). A stronger player's Elo converges higher after enough matches.

**When to use:** Rating players or items from pairwise comparisons — chess, gaming, any "who's better?" from head-to-head results.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `elo1`, `elo2` | float, current ratings | any positive |
| `observed_score` | float, 1.0 for win, 0.0 for loss | |
| `k` | float, update sensitivity (default 32) | |

---

## How inputs shape the output

- **Stronger player's Elo converges higher** after 100 matches with a 55-45 true split.
- **Expected score formula verified:** 100-Elo advantage → expected ~0.64.
- **Elo difference reflects the true skill gap.**

---

## Worked example (real run)

```
$ python3 python/data-science/rankings_and_information_retrieval/elo_rating.py
After 100 matches (true 55-45 split): Elo A=1632.5 | Elo B=1567.5 | Diff=65.0 | Expected(1700 vs 1600)=0.64 | PASS
```

**Reading the output:** after 100 matches with a 55% win rate, player A's Elo (1632) is higher than B's (1568). A 100-point advantage gives a 64% expected score.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| equal players | Elos stay close | correct |
| very few matches | Elo hasn't converged | needs more data |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20