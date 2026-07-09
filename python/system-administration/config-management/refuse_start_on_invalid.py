"""Refuse start on invalid config: raise PRECISE error with field name, never silent default.
Failure simulated: invalid config provided; code silently defaults instead of refusing.
Asserts: exact field name in error; startup blocks; valid config allows start.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys
import json
import tempfile
from pathlib import Path

def validate_and_load_config(config_file, required_fields):
    """Load config and validate. Raises specific ValueError with field name if invalid.
    Never silently defaults or proceeds with partial config.
    """
    try:
        with open(config_file) as f:
            config = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: '{config_file}'")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in config: {e.msg} at line {e.lineno}")

    # Check required fields
    for field in required_fields:
        if field not in config:
            raise ValueError(f"REFUSE START: required config field '{field}' is missing")

    # Type validation
    if "port" in config:
        if not isinstance(config["port"], int):
            raise ValueError(f"REFUSE START: field 'port' must be int, got {type(config['port']).__name__}")
        if config["port"] < 1 or config["port"] > 65535:
            raise ValueError(f"REFUSE START: field 'port' must be 1-65535, got {config['port']}")

    if "timeout" in config:
        if not isinstance(config["timeout"], (int, float)):
            raise ValueError(f"REFUSE START: field 'timeout' must be numeric, got {type(config['timeout']).__name__}")
        if config["timeout"] <= 0:
            raise ValueError(f"REFUSE START: field 'timeout' must be positive, got {config['timeout']}")

    return config

if __name__ == "__main__":
    # VALID: all required fields, valid types
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
        json.dump({"host": "localhost", "port": 8080, "timeout": 30.0}, tmp)
        config_file = tmp.name

    try:
        config = validate_and_load_config(config_file, ["host", "port", "timeout"])
        assert config["host"] == "localhost"
        assert config["port"] == 8080
        assert config["timeout"] == 30.0

        # FAILURE 1: missing required field
        with open(config_file, 'w') as f:
            json.dump({"host": "localhost", "timeout": 30.0}, f)
        try:
            validate_and_load_config(config_file, ["host", "port", "timeout"])
            assert False, "Should refuse start with missing 'port'"
        except ValueError as e:
            assert "port" in str(e).lower(), f"Error must name missing field 'port': {e}"
            assert "refuse" in str(e).lower(), f"Error must say REFUSE START: {e}"

        # FAILURE 2: wrong type for port
        with open(config_file, 'w') as f:
            json.dump({"host": "localhost", "port": "8080", "timeout": 30.0}, f)
        try:
            validate_and_load_config(config_file, ["host", "port", "timeout"])
            assert False, "Should refuse start with port as string"
        except ValueError as e:
            assert "port" in str(e).lower(), f"Error must name field 'port': {e}"
            assert "int" in str(e).lower(), f"Error must mention type: {e}"

        # FAILURE 3: port out of valid range
        with open(config_file, 'w') as f:
            json.dump({"host": "localhost", "port": 99999, "timeout": 30.0}, f)
        try:
            validate_and_load_config(config_file, ["host", "port", "timeout"])
            assert False, "Should refuse start with port > 65535"
        except ValueError as e:
            assert "port" in str(e).lower(), f"Error must mention 'port': {e}"
            assert "65535" in str(e), f"Error must show valid range: {e}"

        # FAILURE 4: negative timeout
        with open(config_file, 'w') as f:
            json.dump({"host": "localhost", "port": 8080, "timeout": -5.0}, f)
        try:
            validate_and_load_config(config_file, ["host", "port", "timeout"])
            assert False, "Should refuse start with negative timeout"
        except ValueError as e:
            assert "timeout" in str(e).lower(), f"Error must name field 'timeout': {e}"
            assert "positive" in str(e).lower(), f"Error must explain constraint: {e}"

        # FAILURE 5: config file not found
        try:
            validate_and_load_config("/nonexistent/config.json", ["host"])
            assert False, "Should refuse start with missing config file"
        except FileNotFoundError as e:
            assert "config.json" in str(e), f"Error must name missing file: {e}"

        # FAILURE 6: invalid JSON
        with open(config_file, 'w') as f:
            f.write("{invalid json}")
        try:
            validate_and_load_config(config_file, ["host"])
            assert False, "Should refuse start with invalid JSON"
        except ValueError as e:
            assert "JSON" in str(e), f"Error must mention JSON: {e}"

        print("refuse_start_on_invalid: 7/7 asserts passed")
        sys.exit(0)
    finally:
        Path(config_file).unlink()
