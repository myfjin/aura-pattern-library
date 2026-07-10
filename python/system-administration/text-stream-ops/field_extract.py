#!/usr/bin/env python3
"""
field_extract: Extract specific fields from whitespace-separated lines.
THE ONE LAW: Parse real data with varying field counts, assert exact extraction.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

def extract_fields(line, field_indices, delimiter=None):
    """
    Extract fields from a line by index.
    field_indices: list of 0-based indices to extract.
    delimiter: None (split on whitespace) or a string.
    Return list of extracted fields, or None if index out of range.
    """
    if delimiter is None:
        parts = line.split()
    else:
        parts = line.split(delimiter)

    result = []
    for idx in field_indices:
        if idx < 0 or idx >= len(parts):
            return None
        result.append(parts[idx])

    return result

def extract_from_file(file_path, field_indices, delimiter=None):
    """Extract fields from each line of a file. Return list of field tuples."""
    result = []
    try:
        with open(file_path) as f:
            for line in f:
                fields = extract_fields(line.rstrip('\n'), field_indices, delimiter)
                if fields is not None:
                    result.append(tuple(fields))
    except IOError:
        return None
    return result

def main():
    # Synthetic whitespace-separated data (like ps output).
    ps_data = """PID   USER    COMMAND
1234  root    /bin/bash
5678  user    /usr/bin/python3
9012  admin   /sbin/sshd"""

    lines = ps_data.strip().split('\n')

    # Extract USER and COMMAND (indices 1 and 2).
    for line in lines[1:]:  # Skip header.
        fields = extract_fields(line, [1, 2])
        assert fields is not None, f"Should extract fields from: {line}"
        assert len(fields) == 2, f"Expected 2 fields, got {len(fields)}"

    user_cmd = extract_fields(lines[1], [1, 2])
    assert user_cmd == ['root', '/bin/bash'], f"Expected ['root', '/bin/bash'], got {user_cmd}"

    # Extract just PID (index 0).
    pid = extract_fields(lines[2], [0])
    assert pid == ['5678'], f"Expected ['5678'], got {pid}"

    # FAILURE SIMULATION: Requesting out-of-range index.
    fields = extract_fields(lines[1], [5])  # Only 3 fields available.
    assert fields is None, "Should return None for out-of-range index"

    # Extract multiple indices including 0 and last.
    multi = extract_fields(lines[3], [0, 1, 2])
    assert multi == ['9012', 'admin', '/sbin/sshd'], f"Expected all 3 fields, got {multi}"

    # Test with custom delimiter (CSV-like).
    csv_data = "john,30,engineer"
    csv_fields = extract_fields(csv_data, [0, 2], delimiter=',')
    assert csv_fields == ['john', 'engineer'], f"CSV extraction failed: {csv_fields}"

    # Edge case: Empty line.
    empty_fields = extract_fields("", [0])
    assert empty_fields is None, "Empty line should return None"

    # Edge case: Line with only whitespace.
    space_fields = extract_fields("   ", [0])
    assert space_fields is None, "Whitespace-only line should return None"

    # Verify exact field values and order.
    test_line = "alpha beta gamma delta epsilon"
    extracted = extract_fields(test_line, [4, 0, 2])
    assert extracted == ['epsilon', 'alpha', 'gamma'], f"Field order should be preserved, got {extracted}"

    # Boundary: last field.
    last_field = extract_fields(test_line, [4])
    assert last_field == ['epsilon'], "Should extract last field"

    print("✓ field_extract passed")

if __name__ == '__main__':
    main()
