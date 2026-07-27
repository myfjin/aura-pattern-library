# exactly once dedup

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 19 · Data pipeline ops

**Signature:** `(records: List[dict], dedup_journal_path: str) → ?`

## What it does

Exactly-Once Deduplication Pattern
Process a stream that may contain duplicates (e.g., from retry logic).
Track processed record IDs in a journal, reject duplicates,
assert that no duplicate record IDs are processed.

## Guarantee

When it runs, exactly once dedup guarantees ids.count('c') == 2; len(processed) == 4; len(skipped) == 1 (proven by run).

**Checkable constraints:**

- `len(processed) == 4`
- `len(skipped) == 1`
- `skipped[0] == 'c'`
- `len(ids) == len(set(ids))`
- `set(ids) == {'a', 'b', 'c', 'd'}`
- `seqs == list(range(len(seqs)))`
- `len(processed1) == 3`
- `len(skipped2) == 4`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def deduplicate_stream(records, dedup_journal_path):`
**Valid input:** `records` is a list of dicts with unique `'id'` values plus intentional duplicates; `dedup_journal_path` is a writable JSON path.
**Core:** Maintains a journal set of processed record IDs; writes the journal before processing each record (write-ahead); skips any record whose ID is already journalized.
**Assert:** A stream `[a,b,c,c,d]` produces 4 processed records and 1 skipped duplicate; after a crash/resume replay the same stream skips the already-seen IDs and processes only new ones.
**⚠️ Defect:** Deduplication is by ID only, so two different records with the same ID are treated as duplicates even if their payloads differ. The journal is rewritten in full after every record, which is O(n²) write amplification for large streams. There is no journaling of skipped records beyond their count.

---
*△ AURA Pattern Library — © Reality Optimizer*
