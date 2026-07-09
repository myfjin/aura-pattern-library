"""
Inverted Index and Boolean Search.

Build an inverted index (term → docs), then answer AND/OR queries.
We verify that planted relevant docs are retrieved, irrelevant excluded,
and set operations match hand-computed results.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Set, Dict


def build_inverted_index(docs: Dict[str, str]) -> Dict[str, Set[str]]:
    """Build inverted index: term → set of doc IDs."""
    index = {}
    for doc_id, text in docs.items():
        words = text.lower().split()
        for word in words:
            if word not in index:
                index[word] = set()
            index[word].add(doc_id)
    return index


def query_and(index: Dict[str, Set[str]], terms: List[str]) -> Set[str]:
    """AND query: return docs containing ALL terms."""
    if not terms:
        return set()
    result = index.get(terms[0], set()).copy()
    for term in terms[1:]:
        result &= index.get(term, set())
    return result


def query_or(index: Dict[str, Set[str]], terms: List[str]) -> Set[str]:
    """OR query: return docs containing ANY term."""
    result = set()
    for term in terms:
        result |= index.get(term, set())
    return result


if __name__ == "__main__":
    # Plant documents
    docs = {
        "doc1": "python machine learning",
        "doc2": "python programming basics",
        "doc3": "machine learning neural networks",
        "doc4": "data science analytics",
        "doc5": "python data science",
    }

    # Build index
    index = build_inverted_index(docs)

    # AND query: "python" AND "machine" (should return docs containing both)
    # Hand-check: doc1 has both, doc3 has machine but not python
    and_result = query_and(index, ["python", "machine"])
    assert and_result == {"doc1"}, (
        f"AND query for ['python', 'machine'] should be {{'doc1'}}, "
        f"got {and_result}"
    )

    # OR query: "python" OR "machine" (docs containing either)
    # Hand-check: doc1, doc2, doc3, doc5 (doc4 has neither)
    or_result = query_or(index, ["python", "machine"])
    expected_or = {"doc1", "doc2", "doc3", "doc5"}
    assert or_result == expected_or, (
        f"OR query for ['python', 'machine'] should be {expected_or}, "
        f"got {or_result}"
    )

    # Single-term query
    python_docs = index.get("python", set())
    assert python_docs == {"doc1", "doc2", "doc5"}, (
        f"Term 'python' should be in {{'doc1', 'doc2', 'doc5'}}, "
        f"got {python_docs}"
    )

    # Verify irrelevant doc is excluded
    assert "doc4" not in or_result, (
        f"Doc4 (about 'data science') should not be in query result for "
        f"'python' OR 'machine'"
    )

    print(
        f"Index size: {len(index)} terms | "
        f"AND (python, machine): {and_result} | "
        f"OR (python, machine): {or_result} | "
        f"Term 'python': {python_docs} | PASS"
    )
