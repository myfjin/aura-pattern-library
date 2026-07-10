#!/usr/bin/env python3
"""
dedup_stream: Remove duplicate lines while preserving order.
THE ONE LAW: Deduplicate stream, assert exact count and order preservation.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import tempfile
import os

def dedup_lines(lines, keep_first=True):
    """
    Remove duplicate lines.
    keep_first=True: keep first occurrence; False: keep last occurrence.
    Preserve order of first (or last) occurrences.
    Return deduplicated list.
    """
    if keep_first:
        seen = set()
        result = []
        for line in lines:
            if line not in seen:
                result.append(line)
                seen.add(line)
        return result
    else:
        # Keep last: reverse, dedup, reverse back.
        seen = set()
        result = []
        for line in reversed(lines):
            if line not in seen:
                result.insert(0, line)
                seen.add(line)
        return result

def dedup_from_file(file_path, keep_first=True):
    """Read file, deduplicate lines, return deduplicated list."""
    try:
        with open(file_path) as f:
            lines = [line.rstrip('\n') for line in f]
        return dedup_lines(lines, keep_first=keep_first)
    except IOError:
        return None

def main():
    # Synthetic data with duplicates.
    log_data = """User: alice
User: bob
User: alice
User: charlie
User: bob
User: alice"""

    lines = log_data.strip().split('\n')
    deduped = dedup_lines(lines)

    # Verify exact count (should be 3 unique: alice, bob, charlie).
    assert len(deduped) == 3, f"Expected 3 unique lines, got {len(deduped)}"

    # Verify order preservation (first occurrence).
    expected = ['User: alice', 'User: bob', 'User: charlie']
    assert deduped == expected, f"Expected {expected}, got {deduped}"

    # FAILURE SIMULATION: Not deduplicating.
    def dedup_lines_broken(lines):
        """Broken: returns all lines."""
        return lines

    broken = dedup_lines_broken(lines)
    assert len(broken) == 6, "Broken version should have all 6 lines"
    assert len(broken) != len(deduped), "Broken dedup should have wrong count"

    # Test keep_last behavior.
    deduped_last = dedup_lines(lines, keep_first=False)
    assert len(deduped_last) == 3, "Last occurrence dedup should also have 3"
    # With keep_last, order is determined by which occurrence is last in the original list.
    # alice last at index 5, bob last at index 4, charlie last at index 3
    # Reversed order of last occurrences: charlie, bob, alice
    assert deduped_last == ['User: charlie', 'User: bob', 'User: alice'], f"Keep_last order wrong, got {deduped_last}"

    # Edge case: All identical lines.
    identical = ['Line X', 'Line X', 'Line X', 'Line X']
    deduped_ident = dedup_lines(identical)
    assert len(deduped_ident) == 1, f"All identical should dedupe to 1, got {len(deduped_ident)}"
    assert deduped_ident == ['Line X'], f"Should keep the line, got {deduped_ident}"

    # Edge case: No duplicates.
    unique = ['Line A', 'Line B', 'Line C']
    deduped_unique = dedup_lines(unique)
    assert len(deduped_unique) == 3, "Unique lines should stay as-is"
    assert deduped_unique == unique, "Order should be unchanged for unique lines"

    # Edge case: Empty input.
    empty = []
    deduped_empty = dedup_lines(empty)
    assert deduped_empty == [], "Empty input should return empty list"

    # Test with file.
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("alpha\nbeta\nalpha\ngamma\nbeta\n")
        temp_file = f.name

    try:
        file_deduped = dedup_from_file(temp_file)
        assert file_deduped == ['alpha', 'beta', 'gamma'], f"File dedup should be ['alpha', 'beta', 'gamma'], got {file_deduped}"
    finally:
        os.unlink(temp_file)

    # Verify exact order preservation with complex case.
    complex_data = ['A', 'B', 'C', 'B', 'D', 'A', 'E']
    complex_deduped = dedup_lines(complex_data)
    assert complex_deduped == ['A', 'B', 'C', 'D', 'E'], f"Complex case order wrong: {complex_deduped}"

    print("✓ dedup_stream passed")

if __name__ == '__main__':
    main()
