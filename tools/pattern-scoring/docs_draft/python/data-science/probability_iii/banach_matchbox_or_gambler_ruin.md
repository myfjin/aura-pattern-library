# Gambler's Ruin

**File:** `python/data-science/probability_iii/banach_matchbox_or_gambler_ruin.py`
**Sphere:** Data Science — Probability III

---

## What it solves

**Compute the probability of ruin (hitting 0 before N) in a bounded ±1 random walk.** A gambler starts with wealth a against an opponent with b (total N = a+b). For a fair game (p=0.5): P(ruin) = b/(a+b). For an asymmetric game: P(ruin) = (r^N − r^a)/(r^N − 1) where r = q/p.

**When to use:** Understanding risk of ruin in gambling, finance, or any bounded random walk.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `a` | int > 0, starting wealth | |
| `b` | int > 0, opponent's wealth | |
| `p` | float in [0,1], win probability | |

---

## How inputs shape the output

- **Fair game: P(ruin) = b/(a+b)** — verified against simulation.
- **Biased game favoring gambler: ruin probability < 0.1** — the defining claim.
- **Exact formula matches simulation** within 3% for both fair and biased games.

---

## Worked example (real run)

```
$ python3 python/data-science/probability_iii/banach_matchbox_or_gambler_ruin.py
PASS
```

**Reading the output:** asymmetric fair game (a=5, b=15): exact ruin = 0.75, sim ≈ 0.75. Biased game (a=10, b=10, p=0.6): exact ruin < 0.1.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| p = 0 or 1 | deterministic | correct |
| a or b = 0 | already ruined or won | edge case |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20