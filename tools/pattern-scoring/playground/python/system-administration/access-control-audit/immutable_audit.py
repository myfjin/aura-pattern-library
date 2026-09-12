"""
immutable_audit: create an immutable audit log by sealing it with a cryptographic signature
once written. After sealing, any tampering is detectable. Tamper with a sealed log and
verify the signature breaks.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import hashlib
import hmac
import json
import tempfile
import os
import sys
from pathlib import Path


def sha256(data):
    """Compute SHA256 of data."""
    if isinstance(data, str):
        data = data.encode()
    return hashlib.sha256(data).hexdigest()


class ImmutableAudit:
    """Immutable audit log with HMAC sealing."""

    def __init__(self, log_path, secret_key):
        self.log_path = log_path
        self.secret_key = secret_key.encode() if isinstance(secret_key, str) else secret_key
        self.entries = []
        self.sealed = False
        self.seal_signature = None

    def append(self, event):
        """Append an event (only allowed before sealing)."""
        if self.sealed:
            raise ValueError("log is sealed; cannot append")
        self.entries.append(event)

    def seal(self):
        """Seal the log with an HMAC signature."""
        if self.sealed:
            raise ValueError("log already sealed")

        # Compute HMAC of all entries.
        entries_json = json.dumps(self.entries, sort_keys=True)
        signature = hmac.new(self.secret_key, entries_json.encode(), hashlib.sha256).hexdigest()

        self.seal_signature = signature
        self.sealed = True
        self._write()

    def _write(self):
        """Write log to disk."""
        record = {
            "entries": self.entries,
            "sealed": self.sealed,
            "seal_signature": self.seal_signature,
        }
        with open(self.log_path, "w") as f:
            json.dump(record, f)

    def verify_seal(self):
        """Verify the log seal is intact."""
        if not self.sealed:
            raise ValueError("log is not sealed")

        with open(self.log_path) as f:
            record = json.load(f)

        stored_signature = record["seal_signature"]
        entries_json = json.dumps(record["entries"], sort_keys=True)
        computed_signature = hmac.new(
            self.secret_key, entries_json.encode(), hashlib.sha256
        ).hexdigest()

        if stored_signature != computed_signature:
            raise ValueError(
                f"seal verification failed: tampering detected "
                f"(expected {stored_signature}, got {computed_signature})"
            )
        return True


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    log_path = os.path.join(tmpdir, "audit.sealed")
    secret_key = "super_secret_key_12345"

    # Create and seal an audit log.
    audit = ImmutableAudit(log_path, secret_key)
    audit.append({"event": "user alice logged in", "timestamp": 1000})
    audit.append({"event": "file /etc/passwd accessed", "timestamp": 1005})
    audit.append({"event": "user alice logged out", "timestamp": 1010})

    audit.seal()

    # Verify the seal is intact.
    assert audit.verify_seal()

    # THE FAILURE: tamper with a sealed log on disk.
    with open(log_path) as f:
        record = json.load(f)

    # Modify an entry.
    record["entries"][0]["event"] = "user alice HACKED system"  # tampered

    # Write back.
    with open(log_path, "w") as f:
        json.dump(record, f)

    # Reload and verify.
    audit2 = ImmutableAudit(log_path, secret_key)
    with open(log_path) as f:
        record2 = json.load(f)
    audit2.entries = record2["entries"]
    audit2.sealed = record2["sealed"]
    audit2.seal_signature = record2["seal_signature"]

    # ASSERT: tampering is detected.
    try:
        audit2.verify_seal()
        assert False, "should have detected tampering"
    except ValueError as e:
        assert "tampering" in str(e).lower() and "seal" in str(e).lower()

    # THE FAILURE 2: tamper with multiple entries.
    audit3 = ImmutableAudit(log_path, secret_key)
    with open(log_path) as f:
        record3 = json.load(f)

    record3["entries"][1]["event"] = "file /etc/shadow accessed"  # tampered

    with open(log_path, "w") as f:
        json.dump(record3, f)

    audit4 = ImmutableAudit(log_path, secret_key)
    with open(log_path) as f:
        record4 = json.load(f)
    audit4.entries = record4["entries"]
    audit4.sealed = record4["sealed"]
    audit4.seal_signature = record4["seal_signature"]

    try:
        audit4.verify_seal()
        assert False, "should have detected tampering"
    except ValueError as e:
        assert "tampering" in str(e).lower()

    import shutil
    shutil.rmtree(tmpdir)
    print("✓ immutable_audit passed")
    sys.exit(0)
