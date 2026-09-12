#!/usr/bin/env python3
"""
Backfill Range Pattern
Fill gaps in time series or sequence.
Assert: no gaps remain, existing records not duplicated.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import json
import tempfile
import os


def backfill_range(records, range_start, range_end, backfill_path):
    """
    Records are sparse (gaps in sequence).
    Backfill missing values in [range_start, range_end].
    Track which ranges already backfilled to avoid reprocessing.
    """
    backfilled_ranges = []
    if os.path.exists(backfill_path):
        try:
            with open(backfill_path, 'r') as f:
                data = json.load(f)
                backfilled_ranges = data.get('ranges', [])
        except (json.JSONDecodeError, IOError):
            backfilled_ranges = []

    # Collect existing records
    existing_seq = {r['seq'] for r in records}

    # Identify gaps
    all_seq = set(range(range_start, range_end + 1))
    gaps = sorted(all_seq - existing_seq)

    # Check if this range was already backfilled
    if [range_start, range_end] in backfilled_ranges:
        # Already backfilled: no new fills needed
        gaps = []
    else:
        # Backfill gaps
        for seq in gaps:
            records.append({
                'seq': seq,
                'value': f'backfilled_{seq}',
                'source': 'backfill'
            })

        # Mark range as backfilled
        backfilled_ranges.append([range_start, range_end])
        with open(backfill_path, 'w') as f:
            json.dump({'ranges': backfilled_ranges}, f)

    return records, len(gaps)


def test_backfill_range():
    """
    Records with gaps: seq 1, 3, 5 (missing 2, 4).
    Backfill to [1, 5], assert no gaps remain.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        backfill_path = os.path.join(tmpdir, 'backfill.json')

        # Initial records with gaps
        records = [
            {'seq': 1, 'value': 'a'},
            {'seq': 3, 'value': 'c'},
            {'seq': 5, 'value': 'e'}
        ]

        filled, gaps_filled = backfill_range(records, 1, 5, backfill_path)

        # Assert: 2 gaps filled (2, 4)
        assert gaps_filled == 2, f"Expected 2 gaps filled, got {gaps_filled}"
        assert len(filled) == 5, f"Expected 5 records after backfill, got {len(filled)}"

        # Assert: no gaps remain
        seqs = sorted({r['seq'] for r in filled})
        assert seqs == [1, 2, 3, 4, 5], f"Gaps remain: {seqs}"

        # Assert: backfilled records marked
        backfilled = [r for r in filled if r.get('source') == 'backfill']
        assert len(backfilled) == 2, f"Expected 2 backfilled records, got {len(backfilled)}"


def test_backfill_idempotent():
    """
    Backfill same range twice.
    Assert: second backfill doesn't duplicate.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        backfill_path = os.path.join(tmpdir, 'backfill.json')

        records = [
            {'seq': 1, 'value': 'a'},
            {'seq': 3, 'value': 'c'},
            {'seq': 5, 'value': 'e'}
        ]

        # First backfill
        filled1, gaps1 = backfill_range(records, 1, 5, backfill_path)
        assert gaps1 == 2
        assert len(filled1) == 5

        # Second backfill (simulating retry)
        filled2, gaps2 = backfill_range(filled1, 1, 5, backfill_path)
        assert gaps2 == 0, f"Second backfill should find no gaps, got {gaps2}"
        assert len(filled2) == 5, f"Second backfill should not add records, got {len(filled2)}"

        # Assert: records not duplicated
        seqs = [r['seq'] for r in filled2]
        assert len(seqs) == len(set(seqs)), f"Duplicate sequences: {seqs}"


def test_failure_no_backfill_tracking():
    """
    Counter-example: code that doesn't track backfill state.
    """
    def buggy_backfill(records, range_start, range_end):
        """No tracking: always backfills, causing duplicates."""
        existing_seq = {r['seq'] for r in records}
        all_seq = set(range(range_start, range_end + 1))
        gaps = sorted(all_seq - existing_seq)

        for seq in gaps:
            records.append({'seq': seq, 'value': f'backfilled_{seq}'})
        return records

    records = [{'seq': 1}, {'seq': 3}, {'seq': 5}]

    filled1 = buggy_backfill(records, 1, 5)
    assert len(filled1) == 5

    # Retry backfill (bug: doesn't check if already done)
    filled2 = buggy_backfill(filled1, 1, 5)
    # Bug: no new gaps, but code still "backfills" (should be no-op)
    # In this case buggy_backfill would add nothing because gaps is empty
    assert len(filled2) == 5  # OK by accident


if __name__ == '__main__':
    test_backfill_range()
    test_backfill_idempotent()
    test_failure_no_backfill_tracking()
    print("✓ backfill_range passed")
