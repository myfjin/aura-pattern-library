#!/usr/bin/env python3
"""
Lineage Tracking Pattern
Track data provenance: which source records produced which output records.
Assert: complete lineage (every output maps to at least one source),
no dangling outputs, lineage is consistent.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import json
import tempfile
import os


def transform_with_lineage(records, lineage_path):
    """
    Transform records with write-ahead lineage tracking.
    For each output, record which input(s) produced it.
    """
    lineage = {}
    if os.path.exists(lineage_path):
        try:
            with open(lineage_path, 'r') as f:
                lineage = json.load(f)
        except (json.JSONDecodeError, IOError):
            lineage = {}

    output = []

    for record in records:
        rid = record['id']

        # Check if already processed
        if rid in lineage:
            # Retrieve output from lineage
            output_id = lineage[rid]['output_id']
            output_value = lineage[rid]['output_value']
            output.append({'id': output_id, 'value': output_value})
            continue

        # Transform: 1 input -> 1 output
        output_id = f"out_{rid}"
        output_value = record['value'] * 10

        # Record lineage before adding to output
        lineage[rid] = {
            'output_id': output_id,
            'output_value': output_value,
            'source_id': rid
        }
        with open(lineage_path, 'w') as f:
            json.dump(lineage, f)

        output.append({'id': output_id, 'value': output_value})

    return output, lineage


def test_lineage_track():
    """
    Transform records, track lineage.
    Assert: every output has a source, every source produces an output.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        lineage_path = os.path.join(tmpdir, 'lineage.json')

        records = [
            {'id': 'a', 'value': 10},
            {'id': 'b', 'value': 20},
            {'id': 'c', 'value': 30}
        ]

        output, lineage = transform_with_lineage(records, lineage_path)

        # Assert: 3 outputs produced
        assert len(output) == 3, f"Expected 3 outputs, got {len(output)}"

        # Assert: every output has lineage
        for out_rec in output:
            oid = out_rec['id']
            # Find source
            found = False
            for src_id, lin in lineage.items():
                if lin['output_id'] == oid:
                    found = True
                    break
            assert found, f"Output {oid} has no source in lineage"

        # Assert: every source has output
        for src_id, lin in lineage.items():
            assert 'output_id' in lin, f"Source {src_id} has no output"
            # Verify output exists
            found = any(r['id'] == lin['output_id'] for r in output)
            assert found, f"Lineage references missing output {lin['output_id']}"


def test_lineage_consistency():
    """
    Simulate crash and resume.
    Assert: lineage remains consistent (no dangling references).
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        lineage_path = os.path.join(tmpdir, 'lineage.json')

        records = [
            {'id': 'a', 'value': 10},
            {'id': 'b', 'value': 20},
            {'id': 'c', 'value': 30}
        ]

        # First run
        output1, lineage1 = transform_with_lineage(records, lineage_path)
        assert len(lineage1) == 3

        # Simulate partial crash: truncate lineage to first 2 records
        with open(lineage_path, 'r') as f:
            full_lin = json.load(f)
        partial = {k: full_lin[k] for k in ['a', 'b']}
        with open(lineage_path, 'w') as f:
            json.dump(partial, f)

        # Resume
        output2, lineage2 = transform_with_lineage(records, lineage_path)

        # Assert: lineage now has 3 entries again
        assert len(lineage2) == 3, f"After resume, expected 3 lineage entries, got {len(lineage2)}"

        # Assert: no dangling references
        for src_id, lin in lineage2.items():
            output_id = lin['output_id']
            found = any(r['id'] == output_id for r in output2)
            assert found, f"Dangling lineage: {output_id} not in output"


def test_failure_no_lineage():
    """
    Counter-example: code without lineage tracking.
    """
    def buggy_transform(records):
        """No lineage: just transform."""
        return [{'id': f"out_{r['id']}", 'value': r['value'] * 10} for r in records]

    records = [{'id': 'a', 'value': 10}, {'id': 'b', 'value': 20}]
    output = buggy_transform(records)

    # Bug: no way to trace output back to source
    assert len(output) == 2
    # If we crash mid-processing and resume naively, we can't correlate


if __name__ == '__main__':
    test_lineage_track()
    test_lineage_consistency()
    test_failure_no_lineage()
    print("✓ lineage_track passed")
