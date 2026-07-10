#!/usr/bin/env python3
"""
Exactly-Once Deduplication Pattern
Process a stream that may contain duplicates (e.g., from retry logic).
Track processed record IDs in a journal, reject duplicates,
assert that no duplicate record IDs are processed.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import json
import tempfile
import os


def deduplicate_stream(records, dedup_journal_path):
    """
    Process records, deduplicate by ID using a write-ahead journal.
    On replay, skip records already in journal.
    """
    journal = set()
    if os.path.exists(dedup_journal_path):
        try:
            with open(dedup_journal_path, 'r') as f:
                journal = set(json.load(f))
        except (json.JSONDecodeError, IOError):
            journal = set()

    processed = []
    skipped = []

    for record in records:
        rid = record['id']
        if rid in journal:
            skipped.append(rid)
            continue

        # Write to journal BEFORE processing (write-ahead)
        journal.add(rid)
        with open(dedup_journal_path, 'w') as f:
            json.dump(sorted(journal), f)

        # Process record
        processed.append({'id': rid, 'value': record['value'], 'seq': len(processed)})

    return processed, skipped


def test_exactly_once_dedup():
    """
    Simulate a stream with duplicate records (from retry logic).
    Assert: Each record ID processed exactly once.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        journal_path = os.path.join(tmpdir, 'dedup.json')

        # Stream with duplicates: c appears twice (simulating retry)
        stream = [
            {'id': 'a', 'value': 10},
            {'id': 'b', 'value': 20},
            {'id': 'c', 'value': 30},  # First occurrence
            {'id': 'c', 'value': 35},  # Duplicate (retry)
            {'id': 'd', 'value': 40}
        ]

        processed, skipped = deduplicate_stream(stream, journal_path)

        # Assert: 4 unique records processed, 1 skipped
        assert len(processed) == 4, f"Expected 4 processed, got {len(processed)}"
        assert len(skipped) == 1, f"Expected 1 skipped, got {len(skipped)}"
        assert skipped[0] == 'c', f"Expected 'c' skipped, got {skipped}"

        # Assert: all processed IDs unique
        ids = [r['id'] for r in processed]
        assert len(ids) == len(set(ids)), f"Duplicate IDs in processed: {ids}"
        assert set(ids) == {'a', 'b', 'c', 'd'}, f"Wrong ID set: {set(ids)}"

        # Assert: sequence numbers are contiguous
        seqs = [r['seq'] for r in processed]
        assert seqs == list(range(len(seqs))), f"Non-contiguous sequence: {seqs}"


def test_crash_and_resume():
    """
    Simulate: first run processes a,b,c (c duplicated).
    Crash. Resume with a,b,c,c,d stream.
    Assert: still exactly-once.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        journal_path = os.path.join(tmpdir, 'dedup.json')

        # First run: partial stream
        stream1 = [
            {'id': 'a', 'value': 10},
            {'id': 'b', 'value': 20},
            {'id': 'c', 'value': 30}
        ]
        processed1, _ = deduplicate_stream(stream1, journal_path)
        assert len(processed1) == 3

        # Full stream with duplicates (simulating replay after crash)
        stream2 = [
            {'id': 'a', 'value': 10},
            {'id': 'b', 'value': 20},
            {'id': 'c', 'value': 30},
            {'id': 'c', 'value': 35},  # Duplicate
            {'id': 'd', 'value': 40}
        ]
        processed2, skipped2 = deduplicate_stream(stream2, journal_path)

        # Assert: new run skips a,b,c,c (4 already in journal + duplicate), processes only d
        assert len(skipped2) == 4, f"Expected 4 skipped (a,b,c,c), got {len(skipped2)}"
        assert len(processed2) == 1, f"Expected 1 new, got {len(processed2)}"
        assert processed2[0]['id'] == 'd', f"Expected new record to be 'd', got {processed2[0]['id']}"

        # Assert: total unique records = 4
        total_processed = [r['id'] for r in processed1] + [r['id'] for r in processed2]
        total_unique = set(total_processed)
        assert len(total_unique) == 4, f"Expected 4 unique, got {len(total_unique)}"


def test_failure_no_dedup_journal():
    """
    Counter-example: code without dedup journal.
    """
    def buggy_process(stream):
        """No journal: always processes."""
        return [{'id': r['id'], 'value': r['value']} for r in stream]

    stream = [
        {'id': 'a', 'value': 10},
        {'id': 'b', 'value': 20},
        {'id': 'c', 'value': 30},
        {'id': 'c', 'value': 35}  # Duplicate
    ]

    result = buggy_process(stream)
    # Bug: all 4 records processed, including duplicate 'c'
    assert len(result) == 4
    ids = [r['id'] for r in result]
    assert ids.count('c') == 2  # Duplicate detected (the bug)


if __name__ == '__main__':
    test_exactly_once_dedup()
    test_crash_and_resume()
    test_failure_no_dedup_journal()
    print("✓ exactly_once_dedup passed")
