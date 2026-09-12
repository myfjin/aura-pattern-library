"""Dotenv parser: parse .env files correctly, handle special chars, reject malformed.
Failure simulated: malformed key=value lines; special characters; unquoted values.
Asserts: exact parsed key/value; malformed line rejected with line number; valid .env loads.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys
import tempfile
from pathlib import Path

def parse_dotenv(filepath):
    """Parse .env file. Returns dict {key: value}.
    Raises ValueError with line number for malformed lines.
    """
    result = {}
    with open(filepath) as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            if '=' not in line:
                raise ValueError(f"Malformed .env line {line_num}: missing '='")

            key, _, value = line.partition('=')
            key = key.strip()
            value = value.strip()

            if not key:
                raise ValueError(f"Malformed .env line {line_num}: empty key")

            # Remove quotes if present
            if (value.startswith('"') and value.endswith('"')) or \
               (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]

            result[key] = value

    return result

if __name__ == "__main__":
    # VALID: simple key=value
    with tempfile.NamedTemporaryFile(mode='w', suffix='.env', delete=False) as tmp:
        tmp.write("HOST=localhost\nPORT=8080\nDEBUG=true\n")
        dotenv_file = tmp.name

    try:
        result = parse_dotenv(dotenv_file)
        assert result["HOST"] == "localhost"
        assert result["PORT"] == "8080"
        assert result["DEBUG"] == "true"

        # VALID: quoted values
        with open(dotenv_file, 'w') as f:
            f.write('MESSAGE="hello world"\nPATH="/usr/bin"\nSINGLE=\'single quoted\'\n')
        result = parse_dotenv(dotenv_file)
        assert result["MESSAGE"] == "hello world", "Should strip quotes"
        assert result["PATH"] == "/usr/bin"
        assert result["SINGLE"] == "single quoted"

        # VALID: comments and blank lines
        with open(dotenv_file, 'w') as f:
            f.write("# This is a comment\nKEY1=value1\n\n# Another comment\nKEY2=value2\n")
        result = parse_dotenv(dotenv_file)
        assert result["KEY1"] == "value1"
        assert result["KEY2"] == "value2"
        assert len(result) == 2, "Comments should be ignored"

        # FAILURE 1: missing equals sign
        with open(dotenv_file, 'w') as f:
            f.write("NO_EQUALS_HERE\n")
        try:
            parse_dotenv(dotenv_file)
            assert False, "Should reject line without '='"
        except ValueError as e:
            assert "=" in str(e), f"Error must mention missing '=': {e}"
            assert "line" in str(e).lower(), f"Error must mention line number: {e}"

        # FAILURE 2: empty key
        with open(dotenv_file, 'w') as f:
            f.write("=value_without_key\n")
        try:
            parse_dotenv(dotenv_file)
            assert False, "Should reject empty key"
        except ValueError as e:
            assert "empty key" in str(e).lower(), f"Error must mention empty key: {e}"

        # FAILURE 3: exact line number reported
        with open(dotenv_file, 'w') as f:
            f.write("KEY1=value1\nKEY2=value2\nBAD_LINE_3_MISSING_EQUALS\nKEY4=value4\n")
        try:
            parse_dotenv(dotenv_file)
            assert False, "Should fail on line 3"
        except ValueError as e:
            assert "line 3" in str(e), f"Error must report line 3: {e}"

        print("dotenv_parse: 6/6 asserts passed")
        sys.exit(0)
    finally:
        Path(dotenv_file).unlink()
