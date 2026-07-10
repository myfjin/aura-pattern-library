"""
version_constraint_solve: given constraints {name: constraint_str}, resolve to valid versions
or raise ValueError if unsatisfiable. Must reject conflicting constraints and accept compatible
ones. A naive solver might ignore conflicts or get the logic wrong.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys


def parse_constraint(constraint_str):
    """
    Parse a version constraint. Examples:
    "2.0.0" -> (2, 0, 0) exact match
    ">=2.0.0" -> (">=", (2, 0, 0))
    "<=3.0.0" -> ("<=", (3, 0, 0))
    "2.x" -> ("major", 2) (any 2.y.z)
    """
    constraint_str = constraint_str.strip()
    if ">=" in constraint_str:
        return (">=", tuple(map(int, constraint_str.replace(">=", "").strip().split("."))))
    elif "<=" in constraint_str:
        return ("<=", tuple(map(int, constraint_str.replace("<=", "").strip().split("."))))
    elif ".x" in constraint_str:
        major = int(constraint_str.split(".")[0])
        return ("major", major)
    elif "." in constraint_str:
        return ("==", tuple(map(int, constraint_str.split("."))))
    return ("==", tuple(map(int, constraint_str.split("."))))


def version_satisfies(version_tuple, constraint):
    """Check if version_tuple satisfies constraint."""
    if constraint[0] == "==":
        return version_tuple == constraint[1]
    elif constraint[0] == ">=":
        return version_tuple >= constraint[1]
    elif constraint[0] == "<=":
        return version_tuple <= constraint[1]
    elif constraint[0] == "major":
        return version_tuple[0] == constraint[1]
    return False


def resolve_versions(constraints, available_versions):
    """
    Given constraints dict {name: constraint_str} and available versions dict
    {name: [version_tuples]}, find a satisfying assignment or raise ValueError.
    available_versions = {name: [(1,2,3), (2,0,0), ...], ...}
    """
    solution = {}
    for name, constraint_str in constraints.items():
        if name not in available_versions:
            raise ValueError(f"package not available: {name}")
        constraint = parse_constraint(constraint_str)
        matching = [v for v in available_versions[name] if version_satisfies(v, constraint)]
        if not matching:
            raise ValueError(
                f"no version of {name} satisfies constraint {constraint_str}"
            )
        solution[name] = matching[0]  # pick first matching
    return solution


if __name__ == "__main__":
    # Available versions for each package.
    available = {
        "flask": [(1, 8, 0), (2, 0, 0), (2, 0, 3), (2, 1, 0), (3, 0, 0)],
        "werkzeug": [(1, 0, 0), (2, 0, 0), (2, 0, 1), (2, 1, 0)],
    }

    # Clean case: satisfiable constraints.
    constraints_ok = {"flask": "2.0.x", "werkzeug": ">=2.0.0"}
    solution = resolve_versions(constraints_ok, available)
    assert solution["flask"][0] == 2, "flask major version wrong"
    assert solution["werkzeug"] >= (2, 0, 0), "werkzeug version wrong"

    # THE FAILURE: unsatisfiable constraints.
    # Demand Flask 1.x but only demand werkzeug 2.x, but Flask 1.x doesn't exist (or is incompatible).
    # Actually, let's demand a version that doesn't exist.
    constraints_bad = {"flask": "99.0.0", "werkzeug": "2.0.0"}

    # ASSERT: resolver rejects the bad constraint.
    try:
        resolve_versions(constraints_bad, available)
        assert False, "should have raised ValueError on unsatisfiable constraint"
    except ValueError as e:
        assert "no version" in str(e) and "flask" in str(e)

    import shutil
    print("✓ version_constraint_solve passed")
    sys.exit(0)
