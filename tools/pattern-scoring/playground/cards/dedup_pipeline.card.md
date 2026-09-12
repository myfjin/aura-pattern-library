# CARD: dedup_pipeline.py
FILE: python/data-science/composed_tools/dedup_pipeline.py
CLAIM: MinHash near-duplicate detection pipeline over text docs; explains verified dup pairs.

VALID OUTPUT (baseline, exit 0):
  docs: 30 · all-pairs 435 · MinHash candidates 4 · verified near-dups 4
  explanation for pair (0, 1): -the +a +today
  dedup_pipeline.py PASS

FAILURE SIGNATURE: AssertionError or traceback; exit != 0.

ATTACKS (demo starts line 88; docs list built just after):
1. Add two IDENTICAL Ukrainian docs to the docs list: "сьогодні гарний день" twice.
   CONTRACT: text is text — should find them as near-dups ✅ · missing them ❌ (ASCII-only shingles = fake)
2. Add an empty string "" as a doc. Honest: explicit handling or clear error ✅ ·
   crash with cryptic ZeroDivision ❌ borderline — your call · silently wrong counts ❌
3. Call shingles("abc", k=0) (add line before final print). Error on k<1 ✅ · silent [] ❌
