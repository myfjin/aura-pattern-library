"""Config versioning: track config version, detect drift (config changed without version bump).
Failure simulated: config content changed but version not bumped; version mismatch.
Asserts: exact version mismatch in error; version matches content hash; drift detected.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys
import json
import hashlib
import tempfile
from pathlib import Path

def compute_config_hash(config_dict):
    """Compute SHA256 hash of config content."""
    config_json = json.dumps(config_dict, sort_keys=True)
    return hashlib.sha256(config_json.encode()).hexdigest()

def validate_config_version(config_file, expected_version):
    """Load config and check version. Raises ValueError if version mismatches content hash.
    Returns (config, version, content_hash).
    """
    with open(config_file) as f:
        wrapper = json.load(f)

    if "version" not in wrapper:
        raise ValueError("Config missing 'version' field")

    config_version = wrapper["version"]
    if config_version != expected_version:
        raise ValueError(f"Config version mismatch: expected '{expected_version}', got '{config_version}'")

    if "content" not in wrapper:
        raise ValueError("Config missing 'content' field")

    config = wrapper["content"]
    content_hash = compute_config_hash(config)

    if "content_hash" not in wrapper:
        raise ValueError("Config missing 'content_hash' field for drift detection")

    stored_hash = wrapper["content_hash"]
    if stored_hash != content_hash:
        raise ValueError(f"Config drift detected: content changed but version not bumped. "
                        f"Stored hash={stored_hash}, computed hash={content_hash}")

    return config, config_version, content_hash

if __name__ == "__main__":
    # VALID: version matches, hash matches
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
        content = {"host": "localhost", "port": 8080}
        content_hash = compute_config_hash(content)
        wrapper = {
            "version": "1.0",
            "content": content,
            "content_hash": content_hash
        }
        json.dump(wrapper, tmp)
        config_file = tmp.name

    try:
        config, version, hash_val = validate_config_version(config_file, "1.0")
        assert config["host"] == "localhost"
        assert version == "1.0"
        assert hash_val == content_hash

        # VALID: different version string but hash matches
        content = {"host": "localhost", "port": 8080}
        content_hash = compute_config_hash(content)
        wrapper = {
            "version": "2.0",
            "content": content,
            "content_hash": content_hash
        }
        with open(config_file, 'w') as f:
            json.dump(wrapper, f)
        config, version, hash_val = validate_config_version(config_file, "2.0")
        assert version == "2.0"

        # FAILURE 1: version mismatch
        with open(config_file, 'w') as f:
            json.dump(wrapper, f)
        try:
            validate_config_version(config_file, "1.0")
            assert False, "Should reject version mismatch"
        except ValueError as e:
            assert "version mismatch" in str(e).lower(), f"Error must mention version mismatch: {e}"
            assert "1.0" in str(e) and "2.0" in str(e), f"Error must show both versions: {e}"

        # FAILURE 2: content changed but hash not updated (drift)
        wrapper["content"]["port"] = 9090  # Change content
        # Note: hash is still old, doesn't match new content
        with open(config_file, 'w') as f:
            json.dump(wrapper, f)
        try:
            validate_config_version(config_file, "2.0")
            assert False, "Should detect config drift"
        except ValueError as e:
            assert "drift" in str(e).lower(), f"Error must mention drift: {e}"
            assert "hash" in str(e).lower(), f"Error must mention hash mismatch: {e}"

        # FAILURE 3: missing version field
        with open(config_file, 'w') as f:
            json.dump({"content": {"host": "localhost"}, "content_hash": "abc"}, f)
        try:
            validate_config_version(config_file, "1.0")
            assert False, "Should reject missing version field"
        except ValueError as e:
            assert "version" in str(e).lower(), f"Error must mention version: {e}"

        # FAILURE 4: missing content_hash field
        with open(config_file, 'w') as f:
            json.dump({"version": "1.0", "content": {"host": "localhost"}}, f)
        try:
            validate_config_version(config_file, "1.0")
            assert False, "Should reject missing content_hash field"
        except ValueError as e:
            assert "content_hash" in str(e).lower(), f"Error must mention content_hash: {e}"

        # FAILURE 5: missing content field
        with open(config_file, 'w') as f:
            json.dump({"version": "1.0", "content_hash": "abc"}, f)
        try:
            validate_config_version(config_file, "1.0")
            assert False, "Should reject missing content field"
        except ValueError as e:
            assert "content" in str(e).lower(), f"Error must mention content: {e}"

        print("config_versioning: 7/7 asserts passed")
        sys.exit(0)
    finally:
        Path(config_file).unlink()
