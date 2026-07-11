"""
Community Local Authority — who matters inside each village, not in the empire.

FUSED-BRIDGE COMPOSED PATTERN: label_propagation_communities x
pagerank_power_iteration — proposed by BOTH signals 2026-07-10: structural edge
`keyed_store` (community assignments feed the ranker) + semantic 0.495. Global
PageRank is dominated by the largest community's hubs — a small community's
central figure is invisible in the global ranking. Composed: detect communities
first, then rank WITHIN each induced subgraph. Local authority, recovered.

Human logic of the name: the mayor of a small town is nobody in the imperial
census — and still the person the town actually turns to.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from collections import defaultdict
from typing import Dict, List, Set


# ── parent 1 mechanism: label propagation ──
def label_propagation(g: Dict[str, Set[str]], iters: int = 30,
                      seed: int = 42) -> Dict[str, int]:
    rng = random.Random(seed)
    labels = {v: i for i, v in enumerate(sorted(g))}
    nodes = sorted(g)
    for _ in range(iters):
        rng.shuffle(nodes)
        changed = False
        for v in nodes:
            if not g[v]:
                continue
            counts: Dict[int, int] = defaultdict(int)
            for w in g[v]:
                counts[labels[w]] += 1
            best = max(counts.values())
            choices = sorted(l for l, c in counts.items() if c == best)
            new = choices[0]
            if new != labels[v]:
                labels[v] = new
                changed = True
        if not changed:
            break
    # normalize label ids to 0..k-1
    remap = {l: i for i, l in enumerate(sorted(set(labels.values())))}
    return {v: remap[l] for v, l in labels.items()}


# ── parent 2 mechanism: PageRank by power iteration (on any node subset) ──
def pagerank(g: Dict[str, Set[str]], nodes: Set[str], damping: float = 0.85,
             iters: int = 100) -> Dict[str, float]:
    nodes_l = sorted(nodes)
    pr = {v: 1.0 / len(nodes_l) for v in nodes_l}
    for _ in range(iters):
        new = {}
        for v in nodes_l:
            inflow = sum(pr[w] / max(1, len(g[w] & nodes))
                         for w in g[v] & nodes)
            new[v] = (1 - damping) / len(nodes_l) + damping * inflow
        pr = new
    s = sum(pr.values())
    return {v: p / s for v, p in pr.items()}


if __name__ == "__main__":
    random.seed(42)

    # Big community A (12 nodes, hub A0 linked to all) and small community B
    # (6 nodes, star around B0), joined by ONE weak cross-edge.
    g: Dict[str, Set[str]] = defaultdict(set)

    def link(a: str, b: str):
        g[a].add(b)
        g[b].add(a)

    # Empire A: a DENSE CORE of 6 mutually-linked hubs, each owning peripheral
    # nodes — so the global top-6 is all empire, and B0 can't crack it. (A single
    # empire hub isn't enough: a star mayor concentrates rank and sneaks to #2.)
    A = [f"A{i}" for i in range(30)]
    B = [f"B{i}" for i in range(6)]            # a small, sparse village (star)
    core = A[:6]
    for i in range(6):
        for j in range(i + 1, 6):
            link(core[i], core[j])             # clique of empire hubs
    for i, leaf in enumerate(A[6:]):
        link(core[i % 6], leaf)                # each hub owns its leaves
    for i in range(1, 6):
        link("B0", B[i])                       # B0 = the village mayor (star only)
    link("A0", "B3")                           # ONE bridge road

    comms = label_propagation(g)
    groups: Dict[int, Set[str]] = defaultdict(set)
    for v, c in comms.items():
        groups[c].add(v)

    global_pr = pagerank(g, set(g))
    global_rank = sorted(global_pr, key=lambda v: -global_pr[v])
    b0_global = global_rank.index("B0") + 1

    # rank within each community; report the mayor of the SMALL one
    local_top: Dict[int, str] = {}
    for c, members in groups.items():
        lp = pagerank(g, members)
        local_top[c] = max(lp, key=lambda v: lp[v])
    village = min(groups, key=lambda c: len(groups[c]))

    print(f"communities: {len(groups)} · sizes {sorted(len(m) for m in groups.values())}")
    print(f"global PageRank top-3: {global_rank[:3]} · B0 (mayor) global rank: {b0_global}")
    print(f"local authorities: {sorted(local_top.values())} · village mayor: {local_top[village]}")

    # The composed claim, measured. Community recovery is exact UP TO the bridge
    # node (B3 legitimately has a foot in each camp — a true ambiguity label
    # propagation must not fake away); the village CORE stays whole.
    assert len(groups) == 2, f"should find two communities: {len(groups)}"
    b_core = set(B) - {"B3"}
    assert b_core <= groups[village], \
        f"the village core must stay intact: {sorted(groups[village])}"
    assert len(groups[village]) <= len(B), "village must be the small community"
    # the load-bearing claim: the mayor is invisible in the empire-dominated global
    # ranking, but crowned by local (within-community) authority.
    assert b0_global >= 5, \
        f"the village mayor must be INVISIBLE globally (rank ≥5): {b0_global}"
    assert local_top[village] == "B0", \
        f"local ranking must crown the village mayor: {local_top[village]}"
    assert "A0" in local_top.values(), "the empire hub still wins its own community"
    print("community_local_authority.py PASS")
