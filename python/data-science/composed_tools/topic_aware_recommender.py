"""
Topic-Aware Recommender — a 4-pattern WORKFLOW (premium solution template).

PIPELINE-BRIDGE COMPOSED PATTERN (four stages, each output feeds the next),
found by pipeline_search over the composability graph 2026-07-10 (coherence
0.56, `keyed_store` carried end-to-end):
  keyword_cooccurrence_graph  →  label_propagation_communities
  →  pagerank_power_iteration  →  item(document) recommendation.

From a raw text corpus: (1) build the term co-occurrence graph; (2) find topic
communities of terms by label propagation; (3) PageRank the terms WITHIN each
community to get each topic's signature terms; (4) recommend documents by their
overlap with a query document's TOPIC signature — not raw term overlap. The
end-to-end payoff no single stage gives: recommendations respect topic
structure. A flat term-overlap baseline mixes topics; the topic-aware pipeline
stays within-topic.

Human logic of the name: instead of "documents that share your words", it gives
"documents that share your TOPIC" — it understands the neighbourhood, not just
the vocabulary.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from collections import defaultdict
from typing import Dict, List, Set, Tuple


# ── stage 1: PMI-WEIGHTED term co-occurrence graph ──
def cooccurrence_graph(docs: List[List[str]]) -> Dict[str, Dict[str, float]]:
    """Edge weight = positive pointwise mutual information (PPMI), not raw count.
    THE load-bearing choice, and the pipeline's real advantage over naive
    overlap: a ubiquitous shared word has high marginal probability, so its PMI
    with everything is ~0 (down-weighted to nothing); a topic's core terms are
    individually rare but co-occur together, giving high PMI (heavy edges).
    Raw counts let the shared vocabulary dominate and merge all topics; PPMI
    discounts the ubiquitous terms and lets the cores separate."""
    import math
    n = len(docs)
    df: Dict[str, int] = defaultdict(int)
    cf: Dict[Tuple[str, str], int] = defaultdict(int)
    for words in docs:
        u = list(dict.fromkeys(words))
        for w in u:
            df[w] += 1
        for i, a in enumerate(u):
            for b in u[i + 1:]:
                cf[(a, b) if a < b else (b, a)] += 1
    g: Dict[str, Dict[str, float]] = defaultdict(dict)
    for (a, b), c in cf.items():
        pmi = math.log((c * n) / (df[a] * df[b]))       # log[ P(a,b) / (P(a)P(b)) ]
        if pmi > 0:                                       # positive PMI only
            g[a][b] = pmi
            g[b][a] = pmi
    return dict(g)


# ── stage 2: WEIGHTED label-propagation communities ──
def label_propagation(g: Dict[str, Dict[str, int]], iters: int = 40, seed: int = 42) -> Dict[str, int]:
    """Each term adopts the label carrying the most summed EDGE WEIGHT among its
    neighbours — dense core clusters resist the weak shared-vocabulary pull."""
    rng = random.Random(seed)
    labels = {v: i for i, v in enumerate(sorted(g))}
    nodes = sorted(g)
    for _ in range(iters):
        rng.shuffle(nodes)
        changed = False
        for v in nodes:
            if not g[v]:
                continue
            wsum: Dict[int, float] = defaultdict(float)
            for w, wt in g[v].items():
                wsum[labels[w]] += wt
            best = max(wsum.values())
            new = min(l for l, c in wsum.items() if c == best)
            if new != labels[v]:
                labels[v] = new
                changed = True
        if not changed:
            break
    remap = {l: i for i, l in enumerate(sorted(set(labels.values())))}
    return {v: remap[l] for v, l in labels.items()}


# ── stage 3: PageRank within a community ──
def pagerank(g: Dict[str, Dict[str, int]], nodes: Set[str], damping: float = 0.85,
             iters: int = 60) -> Dict[str, float]:
    ns = sorted(nodes)
    if not ns:
        return {}
    nbr = {v: [w for w in g.get(v, {}) if w in nodes] for v in ns}
    pr = {v: 1.0 / len(ns) for v in ns}
    for _ in range(iters):
        pr = {v: (1 - damping) / len(ns) +
                 damping * sum(pr[w] / max(1, len(nbr[w])) for w in nbr[v])
              for v in ns}
    s = sum(pr.values()) or 1.0
    return {v: p / s for v, p in pr.items()}


# ── stage 4: topic-aware document recommendation ──
def topic_signatures(g, comms) -> Dict[int, Dict[str, float]]:
    """Each community's PageRank-weighted signature terms."""
    groups: Dict[int, Set[str]] = defaultdict(set)
    for term, c in comms.items():
        groups[c].add(term)
    return {c: pagerank(g, members) for c, members in groups.items()}


def real_communities(comms: Dict[str, int], min_size: int = 2) -> Set[int]:
    """The multi-term communities — the topic cores. Ubiquitous shared words get
    ~0 PMI, become isolated singletons, and are excluded here as non-topical."""
    size: Dict[int, int] = defaultdict(int)
    for c in comms.values():
        size[c] += 1
    return {c for c, n in size.items() if n >= min_size}


def doc_topic_vector(doc: List[str], comms, sigs, real: Set[int]) -> Dict[int, float]:
    """A document's weight in each REAL topic = sum of its terms' signature
    weights (singleton shared-word communities excluded — they are noise that
    would otherwise leak flat-overlap confusion into the topic vector)."""
    v: Dict[int, float] = defaultdict(float)
    for w in doc:
        c = comms.get(w)
        if c is not None and c in real:
            v[c] += sigs[c].get(w, 0.0)
    return v


def recommend(query_doc, docs, comms, sigs, real, k: int) -> List[int]:
    """Topic-aware: rank docs by cosine over REAL-TOPIC vectors."""
    qv = doc_topic_vector(query_doc, comms, sigs, real)

    def cos(a, b):
        dot = sum(v * b.get(t, 0.0) for t, v in a.items())
        na = sum(v * v for v in a.values()) ** 0.5
        nb = sum(v * v for v in b.values()) ** 0.5
        return dot / (na * nb) if na and nb else 0.0

    scored = [(i, cos(qv, doc_topic_vector(d, comms, sigs, real))) for i, d in enumerate(docs)]
    return [i for i, _ in sorted(scored, key=lambda t: -t[1])[:k]]


def flat_recommend(query_doc, docs, k: int) -> List[int]:
    """Baseline: raw term-overlap (Jaccard), topic-blind."""
    q = set(query_doc)
    scored = [(i, len(q & set(d)) / len(q | set(d))) for i, d in enumerate(docs)]
    return [i for i, _ in sorted(scored, key=lambda t: -t[1])[:k]]


if __name__ == "__main__":
    random.seed(42)

    # THREE topics that SHARE a large common vocabulary (so raw term-overlap is
    # confused — cross-topic docs share many words) but differ in CO-OCCURRENCE
    # STRUCTURE: each topic has a small unique CORE that co-occurs tightly. Bag-
    # of-words overlap is dominated by the shared pool and mixes topics; the
    # co-occurrence graph's communities are driven by the cores and separate
    # them. (Disjoint vocabularies would make even the flat baseline trivially
    # perfect — a 1.0=1.0 non-demo; the baseline must be genuinely challenged.)
    # Shared vocabulary DOMINATES raw content (6 shared terms/doc) so bag-of-
    # words overlap is confused across topics; each topic's 2 core terms are
    # rare-but-cohesive, which PPMI recovers. This is the regime where topic
    # structure beats surface overlap — the whole point of the pipeline.
    shared = [f"w{i}" for i in range(24)]
    cores = {0: [f"A{i}" for i in range(8)],
             1: [f"B{i}" for i in range(8)],
             2: [f"C{i}" for i in range(8)]}

    docs: List[List[str]] = []
    labels: List[int] = []
    for t, core in cores.items():
        for _ in range(80):
            d = [random.choice(core) for _ in range(3)] + [random.choice(shared) for _ in range(9)]
            docs.append(d)
            labels.append(t)

    g = cooccurrence_graph(docs)
    comms = label_propagation(g)
    sigs = topic_signatures(g, comms)
    real = real_communities(comms)

    # Do the 3 topics' CORE terms land in 3 distinct communities? (Shared words
    # scatter into singletons — expected; the topical signal is in the cores.)
    core_comm = {t: {comms.get(w) for w in core if comms.get(w) in real}
                 for t, core in cores.items()}
    distinct_topic_comms = {next(iter(cs)) for cs in core_comm.values() if len(cs) == 1}

    k = 20                    # deeper list: flat's shared-only tail (topic-random)
                              # grows while topic-aware stays within-community pure
    topic_hits = flat_hits = 0
    for qi in range(0, len(docs), 4):
        qtopic = labels[qi]
        for i in recommend(docs[qi], docs, comms, sigs, real, k):
            topic_hits += (labels[i] == qtopic)
        for i in flat_recommend(docs[qi], docs, k):
            flat_hits += (labels[i] == qtopic)
    n_eval = len(range(0, len(docs), 4)) * k
    topic_rate = topic_hits / n_eval
    flat_rate = flat_hits / n_eval

    print(f"real (multi-term) communities: {len(real)} · each topic's cores cohesive: "
          f"{[len(cs) == 1 for cs in core_comm.values()]}")
    print(f"same-topic recommendation rate — topic-aware {topic_rate:.0%} vs flat {flat_rate:.0%}")

    # The workflow claim, end-to-end (what no single stage gives):
    assert all(len(cs) == 1 for cs in core_comm.values()), \
        f"each topic's core terms must form ONE community: {core_comm}"
    assert len(distinct_topic_comms) == 3, \
        f"the 3 topics must occupy 3 DISTINCT communities: {distinct_topic_comms}"
    assert topic_rate > 0.80, \
        f"topic-aware recs must stay within topic: {topic_rate:.0%}"
    assert topic_rate > flat_rate + 0.15, \
        f"the pipeline must clearly beat flat term-overlap (confused by shared vocab): " \
        f"{topic_rate:.0%} vs {flat_rate:.0%}"
    print("topic_aware_recommender.py PASS")
