# topic aware recommender

**Language:** Python · **Category:** composed tools

## What it does

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

---
*△ AURA Pattern Library — © Reality Optimizer*
