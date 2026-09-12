# Three-Stage Dedup Pipeline

**File:** `python/data-science/composed_tools/dedup_pipeline.py`
**Sphere:** Data Science — Composed Tools
**Status:** PASS-WITH-FLAG (Illia's audit 2026-07-19)

---

## What it solves

You have thousands of documents and suspect near-duplicates (reposts, edited copies, boilerplate). Comparing all pairs is quadratic death. This pipeline: **shingle → MinHash → candidates → exact verify → explain**: cheap signatures prune >80% of comparisons, real Jaccard verifies survivors, and a diff explains *why* each pair matched.

**When to use:** Deduplicating document collections where all-pairs exact comparison is too expensive and silent deletion is unacceptable (the diff is the audit). Works on any language (unicode-clean — proven with Ukrainian).

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `docs` | list of str, any language (unicode-clean) | — |
| `k` (shingle size) | int ≥ 1 (default 3) | AURA-E009 (k ≤ 0 → degenerate `{''}`) |
| `cand_thresh` | float in [0, 1], MinHash similarity threshold | — |
| `verify_ratio` | float in [0, 1], max edit-distance ratio for verification | — |
| empty-string docs | currently ingested silently; two empties verify as "perfect dups" | AURA-E009 flag |

---

## How inputs shape the output

- **`k` is the granularity knob:** k=3 (word triples) balances precision/recall; smaller k → more candidates (looser matching), larger k → only long verbatim runs match. k ≤ 0 is nonsense and currently returns a degenerate signature instead of erroring — the flagged gap.
- **Edit distance drives survival:** the planted pairs differ by one word + one suffix and survive verification; unrelated filler docs (even from a tiny shared vocabulary) get pruned.
- **Doc count scales candidates, not correctness:** Illia's prepended docs shifted indices but every planted pair was still found at its new position.

---

## Worked example (real run)

```
$ python3 python/data-science/composed_tools/dedup_pipeline.py
docs: 30 · all-pairs 435 · MinHash candidates 4 · verified near-dups 4
explanation for pair (0, 1): -the +a +today
dedup_pipeline.py PASS
```

**Reading the output:** of 435 possible pairs, MinHash proposed only 4 (>99% pruned), all 4 verified as real near-dups, and the explanation reads as an edit script: doc 1 = doc 0 with "the"→"a" and "today" appended. That diff line is the trust anchor — you can *see* why they matched.

---

## Failure modes (audited by hand)

| Trigger | What happens today | Meaning |
|---|---|---|
| two identical Ukrainian docs | **found as verified dup** ✅ (unicode-clean shingling) | detection is language-blind, as it must be |
| the same, in the demo harness | harness assert crashes: "no false pairs" — **closed-world artifact**, planted-list only | use the function; the harness assumes only ITS dups exist |
| `shingles(text, k=0)` | silently returns `{''}` — AURA-E009 ⚠ | nonsense window size needs a guard |
| two empty docs | would verify as perfect duplicates (`{''}` signatures) | empty-doc policy undeclared |

---

## Provenance

Machine-VERIFIED (frozen ruler) · Illia's audit 2026-07-19: 8 runs → detection genuine, one silent-degenerate flag → PASS-WITH-FLAG · evidence: `output/manual_audit_2026-07-19.csv` · errors: AURA-E009 in `ERROR_CATALOG.md`
