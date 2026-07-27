# inverted index search

**Language:** Python · **Sphere:** data-science · **Category:** Rankings & Information Retrieval

**Signature:** `(docs: Dict[str, str]) → Dict[str, Set[str]]`

## What it does

Inverted Index and Boolean Search.

Build an inverted index (term → docs), then answer AND/OR queries.
We verify that planted relevant docs are retrieved, irrelevant excluded,
and set operations match hand-computed results.

## Guarantee

When it runs, inverted index search guarantees or_result == expected_or; and_result == {'doc1'}; python_docs == {'doc1', 'doc2', 'doc5'} (proven by run).

**Checkable constraints:**

- `and_result == {'doc1'}`
- `or_result == expected_or`
- `python_docs == {'doc1', 'doc2', 'doc5'}`
- `'doc4' not in or_result`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
