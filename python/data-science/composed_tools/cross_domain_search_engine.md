# cross domain search engine

**Language:** Python · **Category:** composed tools

## What it does

Cross-Domain Search Engine — a 4-pattern WORKFLOW that finds the bridges.

PIPELINE-BRIDGE COMPOSED PATTERN (four stages, each feeds the next), found by
pipeline_search over the composability graph 2026-07-10 (coherence 0.50):
  porter_stemmer_lite → broker_term_extraction → query_expansion_prf → bm25_ranking.

A plain search returns documents that share your query's WORDS — all inside your
own domain. This engine retrieves the documents that BRIDGE domains: (1) stem the
vocabulary so surface variants unify; (2) extract the corpus's broker terms (the
words on shortest paths between topic clusters); (3) expand the query with those
broker terms; (4) BM25-rank. A domain-A query then surfaces the cross-domain
bridge documents a plain BM25 search leaves buried.

Human logic of the name: ordinary search digs deeper into your own field; this
one walks to the borders and brings back what crosses them.

---
*△ AURA Pattern Library — © Reality Optimizer*
