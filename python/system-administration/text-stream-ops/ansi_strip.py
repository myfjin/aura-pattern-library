#!/usr/bin/env python3
"""
ansi_strip: Strip ANSI escape codes from text (colors, bold, etc.).
THE ONE LAW: Remove all escape sequences, assert exact output.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import re

def strip_ansi(text):
    """
    Remove ANSI escape codes from text.
    ANSI pattern: ESC [ ... m (where ESC is chr(27)).
    Also handles other ANSI sequences.
    """
    # Pattern for ANSI escape sequences: ESC [ ... m
    ansi_pattern = re.compile(r'\x1b\[[0-9;]*m|\x1b\(B\x1b\[m')
    return ansi_pattern.sub('', text)

def strip_ansi_from_file(file_path):
    """Read file, strip ANSI codes, return cleaned text."""
    try:
        with open(file_path) as f:
            text = f.read()
        return strip_ansi(text)
    except IOError:
        return None

def main():
    # Synthetic ANSI-colored text.
    colored = "\x1b[31mRed text\x1b[0m \x1b[32mGreen text\x1b[0m"
    stripped = strip_ansi(colored)

    # Verify ANSI codes removed.
    assert '\x1b' not in stripped, f"ANSI escape should be removed, but found: {repr(stripped)}"
    assert 'Red text' in stripped, "Text content should be preserved"
    assert 'Green text' in stripped, "Text content should be preserved"
    assert stripped == 'Red text Green text', f"Expected 'Red text Green text', got '{stripped}'"

    # FAILURE SIMULATION: Not removing ANSI codes.
    def strip_ansi_broken(text):
        """Broken: doesn't remove escapes."""
        return text

    broken = strip_ansi_broken(colored)
    assert '\x1b' in broken, "Broken should leave ANSI codes"
    assert '\x1b' not in stripped, "Real version should remove them"

    # Test various ANSI codes.
    bold_red = "\x1b[1;31mBold Red\x1b[0m"
    bold_stripped = strip_ansi(bold_red)
    assert bold_stripped == 'Bold Red', f"Bold + color should strip, got '{bold_stripped}'"

    # Underline.
    underlined = "\x1b[4mUnderlined\x1b[0m"
    underlined_stripped = strip_ansi(underlined)
    assert underlined_stripped == 'Underlined', f"Underline should strip, got '{underlined_stripped}'"

    # Complex: multiple styles.
    complex_text = "\x1b[32m\x1b[1mBold Green\x1b[0m \x1b[33mYellow\x1b[0m Text"
    complex_stripped = strip_ansi(complex_text)
    assert complex_stripped == 'Bold Green Yellow Text', f"Complex should strip cleanly, got '{complex_stripped}'"

    # Edge case: No ANSI codes.
    plain = "Plain text without colors"
    plain_stripped = strip_ansi(plain)
    assert plain_stripped == plain, "Plain text should be unchanged"

    # Edge case: Only ANSI codes (no visible text).
    only_escape = "\x1b[31m\x1b[0m"
    only_escape_stripped = strip_ansi(only_escape)
    assert only_escape_stripped == '', f"Only escapes should yield empty string, got '{only_escape_stripped}'"

    # Edge case: Nested reset codes.
    nested = "\x1b[31mRed\x1b[0m\x1b[0m\x1b[0mText"
    nested_stripped = strip_ansi(nested)
    assert nested_stripped == 'RedText', f"Nested resets should strip, got '{nested_stripped}'"

    # Verify exact character count after stripping.
    exact_text = "\x1b[1mHello\x1b[0m \x1b[32mWorld\x1b[0m"
    exact_stripped = strip_ansi(exact_text)
    assert len(exact_stripped) == 11, f"'Hello World' should be 11 chars, got {len(exact_stripped)}"
    assert exact_stripped == 'Hello World', f"Expected 'Hello World', got '{exact_stripped}'"

    # Test with file (write colored text, read back stripped).
    import tempfile
    import os
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("\x1b[31mError message\x1b[0m")
        temp_file = f.name

    try:
        file_stripped = strip_ansi_from_file(temp_file)
        assert file_stripped == 'Error message', f"File strip failed: {file_stripped}"
    finally:
        os.unlink(temp_file)

    print("✓ ansi_strip passed")

if __name__ == '__main__':
    main()
