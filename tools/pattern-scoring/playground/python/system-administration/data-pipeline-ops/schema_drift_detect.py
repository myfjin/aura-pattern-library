#!/usr/bin/env python3
"""
Schema Drift Detection Pattern
Track expected schema. Detect when records deviate:
- New fields added
- Fields removed
- Field types changed
Assert: drift is detected and named explicitly.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import json
import tempfile
import os


class SchemaDriftError(Exception):
    pass


def infer_schema(records):
    """
    Infer schema: {field: type} for each record.
    """
    if not records:
        return {}
    schema = {}
    for record in records:
        for key, value in record.items():
            field_type = type(value).__name__
            if key in schema:
                if schema[key] != field_type:
                    # Type mismatch
                    schema[key] = 'mixed'
            else:
                schema[key] = field_type
    return schema


def detect_schema_drift(records, schema_path):
    """
    Compare current records against stored schema.
    Detect: new fields, removed fields, type changes.
    On first run (no stored schema), just store it. On subsequent runs, compare.
    """
    stored_schema = {}
    first_run = True

    if os.path.exists(schema_path):
        try:
            with open(schema_path, 'r') as f:
                stored_schema = json.load(f)
                first_run = False
        except (json.JSONDecodeError, IOError):
            stored_schema = {}
            first_run = True

    current_schema = infer_schema(records)
    drifts = []

    # On first run, no drift to report
    if first_run:
        with open(schema_path, 'w') as f:
            json.dump(current_schema, f)
        return drifts, current_schema

    # Subsequent runs: compare against stored schema
    # Check for new fields
    for field in current_schema:
        if field not in stored_schema:
            drifts.append(f"new_field:{field}")

    # Check for removed fields
    for field in stored_schema:
        if field not in current_schema:
            drifts.append(f"removed_field:{field}")

    # Check for type changes
    for field in stored_schema:
        if field in current_schema:
            if stored_schema[field] != current_schema[field]:
                drifts.append(
                    f"type_change:{field} "
                    f"({stored_schema[field]}->{current_schema[field]})"
                )

    # Update schema on disk for next comparison
    with open(schema_path, 'w') as f:
        json.dump(current_schema, f)

    return drifts, current_schema


def test_schema_drift_detect():
    """
    Process records with evolving schema.
    Assert: drift is detected and named.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        schema_path = os.path.join(tmpdir, 'schema.json')

        # Initial records
        records1 = [
            {'id': 'a', 'name': 'Alice', 'age': 30},
            {'id': 'b', 'name': 'Bob', 'age': 25}
        ]

        drifts1, schema1 = detect_schema_drift(records1, schema_path)
        assert len(drifts1) == 0, f"Expected no drift on first run, got {drifts1}"
        assert schema1 == {'id': 'str', 'name': 'str', 'age': 'int'}

        # Evolved records: new field 'email', age is now float (type change)
        records2 = [
            {'id': 'a', 'name': 'Alice', 'age': 30.5, 'email': 'alice@example.com'},
            {'id': 'b', 'name': 'Bob', 'age': 25.0, 'email': 'bob@example.com'}
        ]

        drifts2, schema2 = detect_schema_drift(records2, schema_path)
        assert len(drifts2) > 0, "Expected drift detection"

        # Check: new field detected
        new_field_drifts = [d for d in drifts2 if d.startswith('new_field')]
        assert len(new_field_drifts) == 1, f"Expected 1 new field drift, got {new_field_drifts}"
        assert 'email' in new_field_drifts[0], f"Expected 'email' in drift, got {new_field_drifts}"

        # Check: type change detected
        type_change_drifts = [d for d in drifts2 if d.startswith('type_change')]
        assert len(type_change_drifts) == 1, f"Expected 1 type change, got {type_change_drifts}"
        assert 'age' in type_change_drifts[0], f"Expected 'age' in drift, got {type_change_drifts}"
        assert 'int->float' in type_change_drifts[0], \
            f"Expected 'int->float' in drift, got {type_change_drifts[0]}"


def test_schema_removed_field():
    """
    Assert: removed fields are detected.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        schema_path = os.path.join(tmpdir, 'schema.json')

        records1 = [
            {'id': 'a', 'name': 'Alice', 'age': 30, 'ssn': '123-45-6789'}
        ]
        _, _ = detect_schema_drift(records1, schema_path)

        # Records without 'ssn'
        records2 = [
            {'id': 'a', 'name': 'Alice', 'age': 30}
        ]
        drifts2, _ = detect_schema_drift(records2, schema_path)

        removed_drifts = [d for d in drifts2 if d.startswith('removed_field')]
        assert len(removed_drifts) == 1, f"Expected 1 removed field, got {removed_drifts}"
        assert 'ssn' in removed_drifts[0], f"Expected 'ssn' in drift, got {removed_drifts}"


def test_failure_no_schema_tracking():
    """
    Counter-example: code without schema tracking.
    """
    def buggy_process(records):
        """No schema tracking: blindly accesses fields."""
        result = []
        for r in records:
            # Assumes 'age' is int, will fail if type changes
            try:
                age_squared = r['age'] ** 2
                result.append(age_squared)
            except TypeError:
                # Bug: silently fails on type change
                pass
        return result

    # Type mismatch: age is float in second batch
    records = [
        {'age': 30},  # int
        {'age': 25.5}  # float
    ]

    result = buggy_process(records)
    # Bug: may fail or return incomplete results


if __name__ == '__main__':
    test_schema_drift_detect()
    test_schema_removed_field()
    test_failure_no_schema_tracking()
    print("✓ schema_drift_detect passed")
