# Community Local Authority

**File:** `python/data-science/composed_tools/community_local_authority.py`
**Sphere:** Data Science — Composed Tools

---

## What it solves

**Find who matters inside each community, not just in the global ranking.** Global PageRank is dominated by the largest community's hubs — a small community's central figure is invisible in the global ranking. This composition detects communities first (label propagation), then ranks WITHIN each induced subgraph (PageRank). Local authority, recovered.

**When to use:** You need to find the important nodes in each community of a graph, especially when communities are of very different sizes.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `g` | graph as Dict[str, Set[str]] | undirected |

---

## How inputs shape the output

- **Label propagation finds communities** by each node adopting the most common label among its neighbors.
- **Within-community PageRank** ranks nodes only against their community peers, not the whole graph.
- **The village mayor is invisible globally (rank ≥ 5) but crowned locally** — the defining claim.

---

## Worked example (real run)

```
$ python3 python/data-science/composed_tools/community_local_authority.py
communities: 2 · sizes [6, 30]
global PageRank top-3: ['A0', 'A1', 'A2'] · B0 (mayor) global rank: 7
local authorities: ['A0', 'B0'] · village mayor: B0
community_local_authority.py PASS
```

**Reading the output:** B0 (the village mayor) ranks 7th globally — invisible. But within its own community, it's the top authority.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| single community | local = global | correct |
| bridge node between communities | may be assigned to either | legitimate ambiguity |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20