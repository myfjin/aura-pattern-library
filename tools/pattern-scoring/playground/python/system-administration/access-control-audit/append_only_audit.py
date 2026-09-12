"""
append_only_audit: maintain an append-only audit log with hash chaining.
Each entry hash includes the previous entry's hash (forming a chain).
Tampering with an old entry breaks all subsequent hashes.
Flip a byte in a past entry and verify the chain verification catches the break.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import hashlib
import json
import tempfile
import os
import sys
from pathlib import Path


def sha256(data):
    """Compute SHA256 of data (bytes or str)."""
    if isinstance(data, str):
        data = data.encode()
    return hashlib.sha256(data).hexdigest()


class AppendOnlyAudit:
    """Append-only audit log with hash chaining."""

    def __init__(self, log_path):
        self.log_path = log_path
        self.entries = []
        self.prev_hash = "0" * 64  # initial hash

    def append(self, event):
        """Append an event to the log."""
        entry = {
            "event": event,
            "prev_hash": self.prev_hash,
            "hash": None,  # computed below
        }
        entry_json = json.dumps({"event": event, "prev_hash": self.prev_hash})
        entry["hash"] = sha256(entry_json)
        self.entries.append(entry)
        self.prev_hash = entry["hash"]
        self._write()

    def _write(self):
        """Write all entries to disk."""
        with open(self.log_path, "w") as f:
            for entry in self.entries:
                f.write(json.dumps(entry) + "\n")

    def verify_chain(self):
        """Verify the hash chain integrity. Raises ValueError if tampering detected."""
        if not self.entries:
            return True

        current_prev = "0" * 64
        for idx, entry in enumerate(self.entries):
            stored_prev = entry["prev_hash"]
            if stored_prev != current_prev:
                raise ValueError(
                    f"chain broken at entry {idx}: expected prev_hash {current_prev}, "
                    f"got {stored_prev}"
                )
            # Recompute this entry's hash.
            entry_json = json.dumps({"event": entry["event"], "prev_hash": entry["prev_hash"]})
            expected_hash = sha256(entry_json)
            if entry["hash"] != expected_hash:
                raise ValueError(
                    f"hash mismatch at entry {idx}: expected {expected_hash}, got {entry['hash']}"
                )
            current_prev = entry["hash"]

        return True


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    log_path = os.path.join(tmpdir, "audit.log")

    # Build an audit log.
    audit = AppendOnlyAudit(log_path)
    audit.append("user alice logged in")
    audit.append("user bob created file")
    audit.append("user alice deleted file")

    # Verify the chain is intact.
    assert audit.verify_chain()

    # THE FAILURE: tamper with an old entry on disk.
    # Read the log, modify an entry, write it back.
    with open(log_path, "r") as f:
        lines = f.readlines()

    # Parse the first entry.
    entry0 = json.loads(lines[0])
    entry0_str = json.dumps(entry0)
    # Flip a byte in the event string (change 'alice' to 'xlice').
    tampered_event = entry0_str.replace("alice", "xlice")
    lines[0] = tampered_event + "\n"

    # Write back the tampered log.
    with open(log_path, "w") as f:
        f.writelines(lines)

    # Reload the audit log from disk.
    audit2 = AppendOnlyAudit(log_path)
    with open(log_path) as f:
        for line in f:
            audit2.entries.append(json.loads(line))

    # ASSERT: verification catches the tampering.
    try:
        audit2.verify_chain()
        assert False, "should have detected tampering"
    except ValueError as e:
        assert "hash mismatch" in str(e) or "chain broken" in str(e)

    import shutil
    shutil.rmtree(tmpdir)
    print("✓ append_only_audit passed")
    sys.exit(0)
