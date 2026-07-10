"""
session_record: record a user session (login, commands, logout). Verify the record
is accurate and tamper-proof. Modify a logged command and verify tampering is detected.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import json
import hashlib
import tempfile
import os
import sys
from pathlib import Path


def sha256(data):
    """Compute SHA256 of data."""
    if isinstance(data, str):
        data = data.encode()
    return hashlib.sha256(data).hexdigest()


class SessionRecorder:
    """Record user sessions with tamper detection."""

    def __init__(self, session_file):
        self.session_file = session_file
        self.events = []
        self.session_hash = None

    def record_event(self, event_type, details):
        """Record an event (login, command, logout, etc)."""
        event = {
            "type": event_type,
            "details": details,
            "timestamp": len(self.events),  # simple ordering
        }
        self.events.append(event)

    def seal(self):
        """Seal the session: compute hash of all events."""
        event_str = json.dumps(self.events, sort_keys=True)
        self.session_hash = sha256(event_str)
        self._write()

    def _write(self):
        """Write session to disk."""
        record = {
            "events": self.events,
            "session_hash": self.session_hash,
        }
        with open(self.session_file, "w") as f:
            json.dump(record, f)

    def verify_integrity(self):
        """Verify the session hasn't been tampered."""
        with open(self.session_file) as f:
            record = json.load(f)

        stored_hash = record["session_hash"]
        event_str = json.dumps(record["events"], sort_keys=True)
        computed_hash = sha256(event_str)

        if stored_hash != computed_hash:
            raise ValueError(
                f"session tampering detected: hash mismatch "
                f"(expected {stored_hash}, got {computed_hash})"
            )
        return True

    def list_events(self):
        """List all recorded events."""
        return self.events


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    session_file = os.path.join(tmpdir, "session.json")

    # Record a session.
    recorder = SessionRecorder(session_file)
    recorder.record_event("login", {"user": "alice", "time": "10:00"})
    recorder.record_event("command", {"cmd": "ls -la /home", "status": "success"})
    recorder.record_event("command", {"cmd": "cat /etc/passwd", "status": "success"})
    recorder.record_event("logout", {"user": "alice", "time": "10:30"})

    # Seal the session.
    recorder.seal()

    # Verify integrity.
    assert recorder.verify_integrity()

    # List events.
    events = recorder.list_events()
    assert len(events) == 4
    assert events[0]["type"] == "login"
    assert events[-1]["type"] == "logout"

    # THE FAILURE: tamper with a recorded command on disk.
    with open(session_file) as f:
        record = json.load(f)

    # Modify the second event (command: ls).
    record["events"][1]["details"]["cmd"] = "rm -rf /"  # malicious modification

    # Write back.
    with open(session_file, "w") as f:
        json.dump(record, f)

    # Reload and verify.
    recorder2 = SessionRecorder(session_file)
    with open(session_file) as f:
        record2 = json.load(f)
    recorder2.events = record2["events"]
    recorder2.session_hash = record2["session_hash"]

    # ASSERT: tampering is detected.
    try:
        recorder2.verify_integrity()
        assert False, "should have detected tampering"
    except ValueError as e:
        assert "tampering" in str(e) and "hash mismatch" in str(e)

    import shutil
    shutil.rmtree(tmpdir)
    print("✓ session_record passed")
    sys.exit(0)
