#!/usr/bin/env python3
"""
robust_csv_parse: Parse CSV with edge cases (quotes, embedded commas, newlines in fields).
THE ONE LAW: Handle real CSV edge cases, reject genuinely broken rows with precise errors.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import csv
import io


def parse_csv_line(text, strict=True):
    """
    Parse CSV text using the stdlib csv module in STRICT mode (so malformed quoting is
    actually detected). text may span multiple physical lines if a field is quoted.
    strict=True: raise ValueError on a malformed row; strict=False: skip it (return None).
    An empty input returns [] (no row).
    """
    try:
        reader = csv.reader(io.StringIO(text), strict=True)
        return next(reader)
    except StopIteration:
        return []  # empty input -> no row
    except csv.Error as e:
        if strict:
            raise ValueError(f"Malformed CSV: {e}")
        return None


def parse_csv_file(file_path, strict=False):
    """
    Parse a CSV file into a list of row dicts keyed by header.
    strict=False: skip broken rows; True: raise ValueError on the first broken row.
    """
    result = []
    try:
        with open(file_path, newline="") as f:
            reader = csv.DictReader(f, strict=True)
            row_num = 1
            while True:
                row_num += 1
                try:
                    row = next(reader)
                except StopIteration:
                    break
                except csv.Error as e:
                    if strict:
                        raise ValueError(f"Row {row_num}: {e}")
                    continue
                result.append(row)
    except IOError:
        return None
    return result


def main():
    # Synthetic CSV data with edge cases.
    csv_data = 'name,age,address\nalice,30,"123 Main St, Apt 4"\nbob,25,456 Oak Ave'
    lines = csv_data.split("\n")

    # Header + rows parse exactly; the quoted embedded COMMA is preserved as one field.
    assert parse_csv_line(lines[0]) == ["name", "age", "address"], "header parse"
    alice = parse_csv_line(lines[1])
    assert alice == ["alice", "30", "123 Main St, Apt 4"], f"quoted comma field: {alice}"
    assert parse_csv_line(lines[2]) == ["bob", "25", "456 Oak Ave"], "plain row"

    # FAILURE SIMULATION: a genuinely malformed row (data after a closing quote) must be
    # REJECTED with a precise error under strict parsing — a no-op parser would not raise.
    malformed = 'a,"b"c,d'
    try:
        parse_csv_line(malformed, strict=True)
        assert False, "Should reject malformed CSV (data after a closing quote)"
    except ValueError as e:
        assert "Malformed CSV" in str(e), f"Expected precise error, got: {e}"
        assert "expected after" in str(e), f"Error should name the quoting fault, got: {e}"
    # Same row under strict=False is skipped (None), not raised.
    assert parse_csv_line(malformed, strict=False) is None, "non-strict skips the broken row"

    # A second malformed shape: unterminated quote.
    try:
        parse_csv_line('a,"b', strict=True)
        assert False, "Should reject unterminated quote"
    except ValueError as e:
        assert "Malformed CSV" in str(e), f"Expected precise error, got: {e}"

    # Embedded NEWLINE inside a quoted field: csv keeps it as ONE field spanning lines.
    multiline = 'name,"address\nline2"'
    assert parse_csv_line(multiline, strict=True) == ["name", "address\nline2"], \
        "quoted newline must stay a single field"

    # Leading/trailing spaces are preserved (csv does not trim by default).
    assert parse_csv_line("field1 , field2 ") == ["field1 ", " field2 "], "spaces preserved"

    # Extra fields parse fine (csv is lenient about column count).
    assert parse_csv_line("a,b,c,d") == ["a", "b", "c", "d"], "extra fields"

    # Empty input -> empty row.
    assert parse_csv_line("", strict=False) == [], "empty input -> no row"

    print("✓ robust_csv_parse passed")


if __name__ == "__main__":
    main()
