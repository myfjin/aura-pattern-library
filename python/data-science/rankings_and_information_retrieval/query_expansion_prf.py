"""
Pseudo-Relevance Feedback (PRF) for Query Expansion.

Expand a query with terms from top-k initially-retrieved docs.
PRF finds synonym/related-term docs that the raw query misses.
We plant docs with synonyms, show that raw query misses them but expanded query finds them.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Dict, Set


def tf_search(query_terms: List[str], docs: Dict[str, str]) -> List[str]:
    """Simple TF-based search: rank docs by term match count."""
    scores = {}
    for doc_id, text in docs.items():
        words = set(text.lower().split())
        score = sum(1 for term in query_terms if term in words)
        if score > 0:
            scores[doc_id] = score
    return sorted(scores.keys(), key=lambda d: scores[d], reverse=True)


def expand_query_prf(
    query_terms: List[str],
    docs: Dict[str, str],
    k: int = 2,
    expansion_terms: int = 3,
) -> List[str]:
    """
    PRF: retrieve top-k docs via initial query, extract top expansion_terms,
    return as expanded query.
    """
    # Initial retrieval
    initial_results = tf_search(query_terms, docs)[:k]

    # Extract terms from top-k docs
    top_k_text = " ".join([docs[doc_id] for doc_id in initial_results])
    words = top_k_text.lower().split()

    # Term frequency
    term_freq = {}
    for word in words:
        term_freq[word] = term_freq.get(word, 0) + 1

    # Extract top expansion_terms (excluding original query terms)
    candidate_terms = [
        term for term in term_freq.keys() if term not in query_terms
    ]
    candidate_terms.sort(key=lambda t: term_freq[t], reverse=True)
    expansion = candidate_terms[:expansion_terms]

    return query_terms + expansion


if __name__ == "__main__":
    # Plant documents with synonyms
    # Query: "dog" should eventually find "canine" via PRF
    docs = {
        "doc1": "dog training obedience",
        "doc2": "dog canine animal canine",  # Contains synonym "canine" (freq 2)
        "doc3": "cat feline kitten",
        "doc4": "canine wolf species",  # Another "canine" doc
        "doc5": "bird avian chirp",
    }

    # Initial query: just "dog"
    query = ["dog"]
    initial_results = tf_search(query, docs)

    # Check: raw query finds doc1 and doc2 (both have "dog")
    assert "doc1" in initial_results, "Raw query should find doc1"
    assert "doc2" in initial_results, "Raw query should find doc2"

    # PRF expansion
    expanded_query = expand_query_prf(query, docs, k=2, expansion_terms=2)

    # Expanded query should include "canine"
    assert "canine" in expanded_query, (
        f"Expanded query {expanded_query} should include 'canine' from top docs"
    )

    # Re-search with expanded query
    expanded_results = tf_search(expanded_query, docs)

    # Now "doc4" (canine + wolf) should be retrieved (was not in initial results for "dog" only)
    assert "doc4" in expanded_results, (
        f"Expanded query should retrieve doc4 (which has 'canine'), "
        f"got {expanded_results}"
    )

    # Verify "doc3" (cat) is not in expanded results
    assert "doc3" not in expanded_results, (
        f"Irrelevant doc3 (cat) should not be in expanded results for 'dog' query"
    )

    print(
        f"Raw query: {query} → {initial_results[:3]} | "
        f"Expanded: {expanded_query} → {expanded_results[:3]} | "
        f"doc4 found: {('doc4' in expanded_results)} | PASS"
    )
