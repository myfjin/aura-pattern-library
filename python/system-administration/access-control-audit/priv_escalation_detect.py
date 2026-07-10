"""
priv_escalation_detect: detect privilege escalation by comparing user privileges
across time. If a user gains a new privilege they didn't have before, flag it.
This is state-change detection, not a static read.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys


class PrivilegeMonitor:
    """Monitor user privileges for unauthorized escalations."""

    def __init__(self):
        self.snapshots = []  # list of {user: {privileges}, ...}

    def snapshot(self, user_privileges):
        """
        Record a snapshot of user privileges.
        user_privileges = {user: {priv1, priv2, ...}, ...}
        """
        self.snapshots.append(user_privileges.copy())

    def detect_escalation(self):
        """
        Detect any user gaining new privileges.
        Returns (has_escalation, escalations) where escalations = {user: new_privs, ...}
        """
        if len(self.snapshots) < 2:
            return False, {}

        prev_snapshot = self.snapshots[-2]
        curr_snapshot = self.snapshots[-1]

        escalations = {}
        for user in curr_snapshot:
            curr_privs = curr_snapshot.get(user, set())
            prev_privs = prev_snapshot.get(user, set())

            new_privs = curr_privs - prev_privs
            if new_privs:
                escalations[user] = new_privs

        return len(escalations) > 0, escalations


if __name__ == "__main__":
    monitor = PrivilegeMonitor()

    # Initial snapshot: alice has read privilege only.
    snapshot1 = {
        "alice": {"read"},
        "bob": {"read", "write"},
    }
    monitor.snapshot(snapshot1)

    # Second snapshot (no changes).
    snapshot2 = {
        "alice": {"read"},
        "bob": {"read", "write"},
    }
    monitor.snapshot(snapshot2)

    # Check for escalation (should be none).
    has_escalation, escalations = monitor.detect_escalation()
    assert not has_escalation, "false positive escalation"

    # THE FAILURE: alice gains a new privilege (write).
    snapshot3 = {
        "alice": {"read", "write"},  # gained write!
        "bob": {"read", "write"},
    }
    monitor.snapshot(snapshot3)

    # ASSERT: escalation is detected.
    has_escalation, escalations = monitor.detect_escalation()
    assert has_escalation, "failed to detect escalation"
    assert "alice" in escalations, "alice not in escalations"
    assert "write" in escalations["alice"], "write not in alice's escalations"

    # THE FAILURE 2: bob gains admin privilege.
    snapshot4 = {
        "alice": {"read", "write"},
        "bob": {"read", "write", "admin"},  # gained admin!
    }
    monitor.snapshot(snapshot4)

    has_escalation, escalations = monitor.detect_escalation()
    assert has_escalation, "failed to detect bob's escalation"
    assert "bob" in escalations
    assert "admin" in escalations["bob"]

    # THE FAILURE 3: multiple users escalate at once.
    monitor2 = PrivilegeMonitor()
    snapshot_before = {
        "alice": {"read"},
        "bob": {"read"},
        "charlie": {"read"},
    }
    monitor2.snapshot(snapshot_before)

    snapshot_after = {
        "alice": {"read", "write"},  # escalated
        "bob": {"read", "delete"},   # escalated
        "charlie": {"read"},         # no escalation
    }
    monitor2.snapshot(snapshot_after)

    has_escalation, escalations = monitor2.detect_escalation()
    assert has_escalation
    assert len(escalations) == 2, f"expected 2 users with escalation, got {len(escalations)}"
    assert "alice" in escalations and "bob" in escalations

    import shutil
    print("✓ priv_escalation_detect passed")
    sys.exit(0)
