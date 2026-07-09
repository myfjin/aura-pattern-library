"""Least privilege check: verify secret file has no world/group read bits.
Failure simulated: create secret with mode 0o666 (world+group readable);
guard checks and rejects or strips world/group bits. Assert world/group bits are 0.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import tempfile
from pathlib import Path

def least_privilege_check(filepath):
    """Check that secret file only has user bits set (0o600 or subset).
    Returns True if passed (no world/group bits), False if failed.
    """
    s = os.stat(filepath)
    mode = s.st_mode & 0o777
    # Check: only user bits should be set
    world_bits = mode & 0o007
    group_bits = (mode & 0o070) >> 3
    if world_bits != 0 or group_bits != 0:
        # Reject or raise
        return False
    return True

def enforce_least_privilege(filepath):
    """Enforce least privilege: strip group and world bits, keep user bits only."""
    s = os.stat(filepath)
    mode = s.st_mode & 0o777
    user_bits = (mode & 0o700) >> 6
    # Set mode to 0o600 * (user_bits / 6) if user_bits < 6, else 0o600
    new_mode = (user_bits << 6) if user_bits > 0 else 0o600
    os.chmod(filepath, new_mode)

if __name__ == "__main__":
    import random
    random.seed(42)

    with tempfile.TemporaryDirectory() as tmpdir:
        secret_file = os.path.join(tmpdir, "secret.key")

        # Write secret with insecure perms (world+group readable)
        Path(secret_file).write_text("SECRET_TOKEN_abc123")
        os.chmod(secret_file, 0o666)  # Insecure: rw-rw-rw-

        # Verify insecure state
        mode_before = os.stat(secret_file).st_mode & 0o777
        assert mode_before == 0o666, f"Setup failed: mode is {oct(mode_before)}, not 0o666"

        # Check fails on insecure file
        result = least_privilege_check(secret_file)
        assert result is False, "Check should fail on 0o666"

        # FAILURE SIM: extract world and group bits
        world_bits_before = mode_before & 0o007
        group_bits_before = (mode_before & 0o070) >> 3
        assert world_bits_before > 0, f"World bits should be >0, got {oct(world_bits_before)}"
        assert group_bits_before > 0, f"Group bits should be >0, got {oct(group_bits_before)}"

        # Enforce least privilege
        enforce_least_privilege(secret_file)

        # RECOVERY ASSERT 1: check now passes
        result_after = least_privilege_check(secret_file)
        assert result_after is True, "Check should pass after enforcement"

        # RECOVERY ASSERT 2: world bits are 0
        mode_after = os.stat(secret_file).st_mode & 0o777
        world_bits_after = mode_after & 0o007
        assert world_bits_after == 0, \
            f"World bits not cleared: {oct(world_bits_after)}"

        # RECOVERY ASSERT 3: group bits are 0
        group_bits_after = (mode_after & 0o070) >> 3
        assert group_bits_after == 0, \
            f"Group bits not cleared: {oct(group_bits_after)}"

        # RECOVERY ASSERT 4: mode is 0o600 (user bits set)
        assert mode_after == 0o600, \
            f"Mode should be 0o600, got {oct(mode_after)}"

        # RECOVERY ASSERT 5: file still readable/writable by owner
        with open(secret_file, 'r') as f:
            content = f.read()
        assert "SECRET_TOKEN_abc123" in content, "File content lost after mode change"

        print("least_privilege_check PASS")
