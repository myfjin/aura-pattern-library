"""
permission_matrix: manage a permission matrix (users × resources × actions).
Verify that a permission grants access. Tamper the matrix (flip a permission bit)
and verify the tamper is detected.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys


class PermissionMatrix:
    """User × Resource permission matrix."""

    def __init__(self):
        # perms[user][resource] = set of allowed actions
        self.perms = {}

    def grant(self, user, resource, action):
        """Grant a permission."""
        if user not in self.perms:
            self.perms[user] = {}
        if resource not in self.perms[user]:
            self.perms[user][resource] = set()
        self.perms[user][resource].add(action)

    def check(self, user, resource, action):
        """Check if a permission is granted. Raises ValueError if not."""
        if user not in self.perms:
            raise ValueError(f"user not in matrix: {user}")
        if resource not in self.perms[user]:
            raise ValueError(f"{user} has no permissions on {resource}")
        if action not in self.perms[user][resource]:
            raise ValueError(f"{user} not permitted to {action} {resource}")
        return True

    def verify_integrity(self, expected):
        """
        Verify matrix matches expected structure.
        expected = {user: {resource: {action, ...}, ...}, ...}
        """
        if set(self.perms.keys()) != set(expected.keys()):
            raise ValueError("user mismatch in matrix")
        for user, resources in self.perms.items():
            if set(resources.keys()) != set(expected[user].keys()):
                raise ValueError(f"resource mismatch for {user}")
            for resource, actions in resources.items():
                if actions != expected[user][resource]:
                    raise ValueError(
                        f"action mismatch for {user}:{resource}: "
                        f"expected {expected[user][resource]}, got {actions}"
                    )
        return True


if __name__ == "__main__":
    matrix = PermissionMatrix()

    # Build a permission matrix.
    matrix.grant("alice", "files", "read")
    matrix.grant("alice", "files", "write")
    matrix.grant("bob", "files", "read")
    matrix.grant("bob", "database", "query")

    # Verify integrity against expected structure.
    expected = {
        "alice": {"files": {"read", "write"}},
        "bob": {"files": {"read"}, "database": {"query"}},
    }

    # Clean case: matrix matches expected.
    assert matrix.verify_integrity(expected)

    # Allow alice to read files.
    assert matrix.check("alice", "files", "read")

    # THE FAILURE: tamper the matrix by adding an unauthorized permission.
    matrix.perms["bob"]["files"].add("write")  # bob shouldn't write

    # ASSERT: tampered matrix is detected on verification.
    tampered_expected = {
        "alice": {"files": {"read", "write"}},
        "bob": {"files": {"read"}, "database": {"query"}},
    }
    try:
        matrix.verify_integrity(tampered_expected)
        assert False, "should have detected tampering"
    except ValueError as e:
        assert "action mismatch" in str(e) and "bob" in str(e)

    # THE FAILURE 2: remove a legitimate permission (removal tampering).
    matrix2 = PermissionMatrix()
    matrix2.grant("charlie", "data", "read")
    matrix2.grant("charlie", "data", "write")

    # Simulate tampering by removing "write".
    matrix2.perms["charlie"]["data"].discard("write")

    expected2 = {
        "charlie": {"data": {"read", "write"}},
    }

    try:
        matrix2.verify_integrity(expected2)
        assert False, "should have detected removal tampering"
    except ValueError as e:
        assert "action mismatch" in str(e)

    import shutil
    print("✓ permission_matrix passed")
    sys.exit(0)
