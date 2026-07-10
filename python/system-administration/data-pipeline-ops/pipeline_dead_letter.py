#!/usr/bin/env python3
"""
Dead Letter Queue Pattern
When processing fails, route to dead letter queue.
Retry logic: retry 3 times, then move to DLQ.
Assert: all records either processed or in DLQ, no lost records.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import json
import tempfile
import os


class ProcessingError(Exception):
    pass


def process_with_dlq(records, dlq_path, retry_limit=3):
    """
    Process records with retry and DLQ.
    Records that fail after retry_limit attempts go to DLQ.
    """
    dlq = []
    if os.path.exists(dlq_path):
        try:
            with open(dlq_path, 'r') as f:
                dlq = json.load(f)
        except (json.JSONDecodeError, IOError):
            dlq = []

    processed = []

    for record in records:
        rid = record['id']
        retry_count = 0
        success = False

        # Retry loop
        while retry_count < retry_limit:
            try:
                # Simulate processing that fails for certain records
                if record.get('bad_record'):
                    raise ProcessingError(f"Invalid field in record {rid}")

                # Process
                processed.append({
                    'id': rid,
                    'status': 'success',
                    'value': record['value']
                })
                success = True
                break
            except ProcessingError as e:
                retry_count += 1
                if retry_count >= retry_limit:
                    # Move to DLQ
                    dlq_entry = {
                        'id': rid,
                        'original': record,
                        'error': str(e),
                        'retry_count': retry_count
                    }
                    dlq.append(dlq_entry)
                    with open(dlq_path, 'w') as f:
                        json.dump(dlq, f)

    return processed, dlq


def test_pipeline_dlq():
    """
    Process records including some that fail.
    Assert: all records accounted for (success or DLQ).
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq_path = os.path.join(tmpdir, 'dlq.json')

        records = [
            {'id': 'a', 'value': 100},
            {'id': 'b', 'value': 200, 'bad_record': True},  # Will fail
            {'id': 'c', 'value': 300},
            {'id': 'd', 'value': 400, 'bad_record': True}   # Will fail
        ]

        processed, dlq = process_with_dlq(records, dlq_path, retry_limit=1)

        # Assert: 2 successes, 2 in DLQ
        assert len(processed) == 2, f"Expected 2 processed, got {len(processed)}"
        assert len(dlq) == 2, f"Expected 2 in DLQ, got {len(dlq)}"

        # Assert: all records accounted for
        success_ids = {r['id'] for r in processed}
        dlq_ids = {r['id'] for r in dlq}
        total_ids = success_ids | dlq_ids
        assert total_ids == {'a', 'b', 'c', 'd'}, f"Missing or extra records: {total_ids}"

        # Assert: no overlap
        assert len(success_ids & dlq_ids) == 0, "Record in both success and DLQ"


def test_dlq_retry_exhaustion():
    """
    Assert: record retried exactly retry_limit times before DLQ.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq_path = os.path.join(tmpdir, 'dlq.json')

        records = [
            {'id': 'bad', 'value': 1, 'bad_record': True}
        ]

        _, dlq = process_with_dlq(records, dlq_path, retry_limit=3)

        assert len(dlq) == 1, f"Expected 1 in DLQ, got {len(dlq)}"
        assert dlq[0]['retry_count'] == 3, \
            f"Expected 3 retries, got {dlq[0]['retry_count']}"


def test_failure_no_dlq():
    """
    Counter-example: code without DLQ loses records.
    """
    def buggy_process(records):
        """No DLQ: silently drops failed records."""
        result = []
        for r in records:
            try:
                if r.get('bad_record'):
                    raise ProcessingError("fail")
                result.append(r)
            except ProcessingError:
                pass  # Bug: record silently lost
        return result

    records = [
        {'id': 'a', 'value': 1},
        {'id': 'b', 'value': 2, 'bad_record': True},
        {'id': 'c', 'value': 3}
    ]

    result = buggy_process(records)
    # Bug: only 2 records, 1 lost
    assert len(result) == 2
    ids = {r['id'] for r in result}
    assert 'b' not in ids  # Lost record


if __name__ == '__main__':
    test_pipeline_dlq()
    test_dlq_retry_exhaustion()
    test_failure_no_dlq()
    print("✓ pipeline_dead_letter passed")
