"""
Cross-Domain Query Expansion — the query that goes looking for bridges.

FUSED-BRIDGE COMPOSED PATTERN (third generation): broker_term_extraction (itself
a composed child) x query_expansion_prf — proposed by BOTH signals 2026-07-10:
structural edge `keyed_store` (broker scores feed the expander) + semantic 0.499.
Classic pseudo-relevance feedback expands a query with top-document terms and
finds MORE OF THE SAME domain. Expanding with BROKER terms — the words that sit
between topic clusters — makes retrieval surface the documents that CONNECT
domains: cross-domain discovery instead of deeper monoculture.

Human logic of the name: most queries dig deeper into their own field; this one
walks to the border and asks who crosses it.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from collections import defaultdict, deque
from typing import Dict, List, Set


# ── parent 1 mechanism: co-occurrence graph + betweenness (broker terms) ──
def cooccurrence_graph(docs: List[List[str]]) -> Dict[str, Set[str]]:
    g: Dict[str, Set[str]] = defaultdict(set)
    for words in docs:
        for a, b in zip(words, words[1:]):     # adjacent-pair windowing (parent law:
            if a != b:                          # all-pairs would bypass the broker)
                g[a].add(b)
                g[b].add(a)
    return g


def betweenness(g: Dict[str, Set[str]]) -> Dict[str, float]:
    bc = {v: 0.0 for v in g}
    for s in g:
        stack, preds = [], {v: [] for v in g}
        sigma = {v: 0.0 for v in g}; sigma[s] = 1.0
        dist = {v: -1 for v in g}; dist[s] = 0
        q = deque([s])
        while q:
            v = q.popleft(); stack.append(v)
            for w in g[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1; q.append(w)
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]; preds[w].append(v)
        delta = {v: 0.0 for v in g}
        while stack:
            w = stack.pop()
            for v in preds[w]:
                delta[v] += sigma[v] / sigma[w] * (1 + delta[w])
            if w != s:
                bc[w] += delta[w]
    return bc


# ── parent 2 mechanism: tf-idf retrieval + PRF expansion ──
def tfidf_vectors(docs: List[List[str]]):
    df: Dict[str, int] = defaultdict(int)
    for d in docs:
        for w in set(d):
            df[w] += 1
    n = len(docs)
    vecs = []
    for d in docs:
        tf: Dict[str, float] = defaultdict(float)
        for w in d:
            tf[w] += 1.0
        vecs.append({w: (c / len(d)) * math.log((n + 1) / (df[w] + 1)) for w, c in tf.items()})
    return vecs


def cosine(a: Dict[str, float], b: Dict[str, float]) -> float:
    dot = sum(v * b.get(k, 0.0) for k, v in a.items())
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na > 0 and nb > 0 else 0.0


def retrieve(query: List[str], docs: List[List[str]], k: int) -> List[int]:
    vecs = tfidf_vectors(docs)
    qv: Dict[str, float] = defaultdict(float)
    for w in query:
        qv[w] += 1.0
    scores = sorted(range(len(docs)), key=lambda i: -cosine(dict(qv), vecs[i]))
    return scores[:k]


def prf_expand(query: List[str], docs: List[List[str]], top_docs: int = 3,
               n_terms: int = 3) -> List[str]:
    """Classic PRF: add the most frequent non-query terms of the top retrieved docs."""
    top = retrieve(query, docs, top_docs)
    counts: Dict[str, int] = defaultdict(int)
    for i in top:
        for w in docs[i]:
            if w not in query:
                counts[w] += 1
    return query + sorted(counts, key=lambda w: -counts[w])[:n_terms]


def broker_expand(query: List[str], docs: List[List[str]], n_terms: int = 3) -> List[str]:
    """The composition: expand with the corpus's top BROKER terms instead."""
    bc = betweenness(cooccurrence_graph(docs))
    brokers = [w for w in sorted(bc, key=lambda w: -bc[w]) if w not in query]
    return query + brokers[:n_terms]


if __name__ == "__main__":
    random.seed(42)
    fin = "market price bond yield equity hedge margin portfolio".split()
    bio = "cell protein enzyme membrane genome neuron receptor tissue".split()
    brokers = ["model", "network"]

    docs: List[List[str]] = []
    for _ in range(10):                                   # finance monoculture
        docs.append([random.choice(fin) for _ in range(10)])
    for _ in range(10):                                   # biology monoculture
        docs.append([random.choice(bio) for _ in range(10)])
    bridge_ids = []
    for _ in range(3):                                    # the BRIDGE documents
        d = [random.choice(fin), brokers[0], random.choice(bio), brokers[1],
             random.choice(bio), brokers[0], random.choice(fin), brokers[1]]
        bridge_ids.append(len(docs))
        docs.append(d)

    query = ["market", "yield", "hedge"]
    k = 5

    prf_q = prf_expand(query, docs)
    broker_q = broker_expand(query, docs)
    hits_prf = sum(1 for i in retrieve(prf_q, docs, k) if i in bridge_ids)
    hits_broker = sum(1 for i in retrieve(broker_q, docs, k) if i in bridge_ids)

    print(f"PRF expansion:    {prf_q[3:]} → bridge docs in top-{k}: {hits_prf}/3")
    print(f"broker expansion: {broker_q[3:]} → bridge docs in top-{k}: {hits_broker}/3")

    # The composed claim, both directions measured:
    assert set(broker_q[3:]) & set(brokers), \
        f"broker expansion must actually pick broker terms: {broker_q[3:]}"
    assert hits_prf <= 1, \
        f"classic PRF should stay in its monoculture (≤1 bridge doc): {hits_prf}"
    assert hits_broker >= 2, \
        f"broker expansion must surface the bridge docs (≥2): {hits_broker}"
    print("cross_domain_query_expansion.py PASS")
