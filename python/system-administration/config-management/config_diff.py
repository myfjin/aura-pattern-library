"""Config diff: report exact changes (added/removed/changed keys) between configs.
Failure simulated: missing changes reported; wrong keys in added/removed/changed.
Asserts: exact set of added keys; exact set of removed keys; exact dict of changed values.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys

def config_diff(old_config, new_config):
    """Compare two configs. Returns dict with 'added', 'removed', 'changed' sets/dict.
    'added': keys in new but not old.
    'removed': keys in old but not new.
    'changed': dict {key: (old_val, new_val)} for keys with different values.
    """
    old_keys = set(old_config.keys())
    new_keys = set(new_config.keys())

    added = new_keys - old_keys
    removed = old_keys - new_keys
    changed = {}

    for key in old_keys & new_keys:
        if old_config[key] != new_config[key]:
            changed[key] = (old_config[key], new_config[key])

    return {"added": added, "removed": removed, "changed": changed}

if __name__ == "__main__":
    # VALID: exact diff with added key
    old1 = {"host": "localhost", "port": 8080}
    new1 = {"host": "localhost", "port": 8080, "debug": True}
    diff = config_diff(old1, new1)
    assert diff["added"] == {"debug"}, f"Should have added 'debug': {diff}"
    assert diff["removed"] == set()
    assert diff["changed"] == {}

    # VALID: exact diff with removed key
    old2 = {"host": "localhost", "port": 8080, "debug": True}
    new2 = {"host": "localhost", "port": 8080}
    diff = config_diff(old2, new2)
    assert diff["added"] == set()
    assert diff["removed"] == {"debug"}, f"Should have removed 'debug': {diff}"
    assert diff["changed"] == {}

    # VALID: exact diff with changed value
    old3 = {"host": "localhost", "port": 8080}
    new3 = {"host": "localhost", "port": 9090}
    diff = config_diff(old3, new3)
    assert diff["added"] == set()
    assert diff["removed"] == set()
    assert diff["changed"]["port"] == (8080, 9090), f"Should show port change: {diff}"

    # VALID: complex diff (add + remove + change)
    old4 = {"host": "localhost", "port": 8080, "debug": True, "timeout": 30}
    new4 = {"host": "localhost", "port": 9090, "verbose": True}
    diff = config_diff(old4, new4)
    assert diff["added"] == {"verbose"}, f"Should have added 'verbose': {diff}"
    assert diff["removed"] == {"debug", "timeout"}, f"Should have removed 'debug', 'timeout': {diff}"
    assert diff["changed"] == {"port": (8080, 9090)}, f"Should show port change: {diff}"

    # VALID: no diff
    old5 = {"a": 1, "b": 2}
    new5 = {"a": 1, "b": 2}
    diff = config_diff(old5, new5)
    assert diff["added"] == set()
    assert diff["removed"] == set()
    assert diff["changed"] == {}

    print("config_diff: 5/5 asserts passed")
    sys.exit(0)
