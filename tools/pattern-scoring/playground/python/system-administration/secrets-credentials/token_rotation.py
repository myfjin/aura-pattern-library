"""Token rotation: keep only N most recent tokens, discard oldest on overflow.
Failure simulated: add 100 tokens with cap=5; assert only 5 remain and oldest are gone.
Defended outcome: file holds exactly N tokens; accessing beyond cap returns None.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import json
import tempfile
import os
from pathlib import Path

def token_rotation(token_file, max_tokens=5):
    """Context for managing rotated tokens. Returns dict with add_token, get_tokens, size."""
    class TokenRing:
        def __init__(self, fpath, cap):
            self.fpath = fpath
            self.cap = cap
            if not Path(self.fpath).exists():
                Path(self.fpath).write_text("[]")

        def add_token(self, token_id, secret):
            """Add token; drop oldest if over cap."""
            tokens = json.loads(Path(self.fpath).read_text())
            tokens.append({"id": token_id, "secret": secret})
            # Keep only the newest cap tokens
            if len(tokens) > self.cap:
                tokens = tokens[-self.cap:]
            Path(self.fpath).write_text(json.dumps(tokens))
            return len(tokens)

        def get_tokens(self):
            """Return list of current tokens."""
            return json.loads(Path(self.fpath).read_text())

        def size(self):
            """Return count of current tokens."""
            return len(self.get_tokens())

    return TokenRing(token_file, max_tokens)

if __name__ == "__main__":
    import random
    random.seed(42)

    with tempfile.TemporaryDirectory() as tmpdir:
        token_file = os.path.join(tmpdir, "tokens.json")
        ring = token_rotation(token_file, max_tokens=5)

        # Simulate adding 100 tokens (cap=5)
        added_tokens = []
        for i in range(100):
            token_id = f"token_{i:03d}"
            secret = f"secret_{i:03d}"
            ring.add_token(token_id, secret)
            added_tokens.append(token_id)

        # RECOVERY ASSERT 1: only 5 tokens remain
        final_count = ring.size()
        assert final_count == 5, f"Expected 5 tokens, got {final_count}"

        # RECOVERY ASSERT 2: newest tokens are present
        tokens = ring.get_tokens()
        token_ids = [t["id"] for t in tokens]
        # Oldest should be token_95, newest token_99
        expected_ids = [f"token_{i:03d}" for i in range(95, 100)]
        assert token_ids == expected_ids, \
            f"Token IDs mismatch: {token_ids} != {expected_ids}"

        # RECOVERY ASSERT 3: oldest tokens are gone
        assert "token_000" not in token_ids, "token_000 should be evicted"
        assert "token_050" not in token_ids, "token_050 should be evicted"

        # RECOVERY ASSERT 4: verify file size reflects only 5 tokens
        file_size = len(Path(token_file).read_text())
        expected_approx = 5 * 50  # rough estimate for 5 token objects
        assert file_size < 500, f"File size {file_size} suggests more than 5 tokens"

        print("token_rotation PASS")
