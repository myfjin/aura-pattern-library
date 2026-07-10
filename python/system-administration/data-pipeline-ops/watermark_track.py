#!/usr/bin/env python3
"""
Watermark Tracking Pattern
Track the highest record timestamp processed.
On resume, only process records with timestamp > watermark.
Asserts: no reprocessing of old records, watermark monotonically increases.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import json
import tempfile
import os


def process_with_watermark(records, watermark_path):
    """
    Process records ordered by timestamp.
    Track high-water mark (highest timestamp processed).
    On resume, skip records with timestamp <= watermark.
    """
    watermark = 0
    if os.path.exists(watermark_path):
        try:
            with open(watermark_path, 'r') as f:
                data = json.load(f)
                watermark = data.get('watermark', 0)
        except (json.JSONDecodeError, IOError):
            watermark = 0

    processed = []
    skipped_count = 0

    for record in records:
        ts = record['timestamp']
        if ts <= watermark:
            skipped_count += 1
            continue

        # Process record
        processed.append({
            'id': record['id'],
            'timestamp': ts,
            'value': record['value']
        })

        # Update watermark
        watermark = max(watermark, ts)
        with open(watermark_path, 'w') as f:
            json.dump({'watermark': watermark}, f)

    return processed, watermark, skipped_count


def test_watermark_track():
    """
    Process stream with timestamps, crash, resume.
    Assert: no reprocessing, watermark advances.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        wm_path = os.path.join(tmpdir, 'watermark.json')

        # First batch: timestamps 10, 20, 30
        records1 = [
            {'id': 'a', 'timestamp': 10, 'value': 100},
            {'id': 'b', 'timestamp': 20, 'value': 200},
            {'id': 'c', 'timestamp': 30, 'value': 300}
        ]

        processed1, wm1, skipped1 = process_with_watermark(records1, wm_path)
        assert len(processed1) == 3, f"Expected 3 processed, got {len(processed1)}"
        assert wm1 == 30, f"Expected watermark 30, got {wm1}"
        assert skipped1 == 0, f"Expected 0 skipped, got {skipped1}"

        # Second batch: includes old records (ts <= 30) and new ones (ts > 30)
        records2 = [
            {'id': 'a', 'timestamp': 10, 'value': 100},  # Old
            {'id': 'b', 'timestamp': 20, 'value': 200},  # Old
            {'id': 'c', 'timestamp': 30, 'value': 300},  # Old
            {'id': 'd', 'timestamp': 40, 'value': 400},  # New
            {'id': 'e', 'timestamp': 50, 'value': 500}   # New
        ]

        processed2, wm2, skipped2 = process_with_watermark(records2, wm_path)
        assert len(processed2) == 2, f"Expected 2 new, got {len(processed2)}"
        assert skipped2 == 3, f"Expected 3 skipped, got {skipped2}"
        assert wm2 == 50, f"Expected watermark 50, got {wm2}"

        # Verify: only new records processed
        ids2 = [r['id'] for r in processed2]
        assert ids2 == ['d', 'e'], f"Expected ['d','e'], got {ids2}"


def test_watermark_monotonic():
    """
    Assert: watermark never decreases (monotonic).
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        wm_path = os.path.join(tmpdir, 'watermark.json')

        # Process records in order
        records = [
            {'id': 'a', 'timestamp': 100, 'value': 1},
            {'id': 'b', 'timestamp': 200, 'value': 2},
            {'id': 'c', 'timestamp': 150, 'value': 3}  # Out of order (but > 100)
        ]

        _, wm1, _ = process_with_watermark(records, wm_path)
        assert wm1 == 200, f"Expected watermark 200, got {wm1}"

        # Even if we replay, watermark doesn't decrease
        _, wm2, _ = process_with_watermark(records, wm_path)
        assert wm2 == 200, f"After replay, watermark should stay 200, got {wm2}"
        assert wm2 >= wm1, f"Watermark decreased: {wm1} -> {wm2}"


def test_failure_no_watermark():
    """
    Counter-example: code without watermark tracking.
    """
    def buggy_process(records):
        """No watermark: always processes."""
        return [{'id': r['id'], 'ts': r['timestamp']} for r in records]

    records = [
        {'id': 'a', 'timestamp': 10},
        {'id': 'b', 'timestamp': 20}
    ]

    result1 = buggy_process(records)
    result2 = buggy_process(records)  # Reprocess everything

    assert len(result1) == 2
    assert len(result2) == 2
    # Bug: if combined, we'd have duplicates
    combined = result1 + result2
    assert len(combined) == 4  # Duplicated


if __name__ == '__main__':
    test_watermark_track()
    test_watermark_monotonic()
    test_failure_no_watermark()
    print("✓ watermark_track passed")
