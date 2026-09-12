#!/usr/bin/env python3
"""scribe — external materializer for relay-driven agents whose tool-calls don't fire.

Design (converged 2026-07-16, AURA mesh): a flash model reasons + writes code as TEXT
reliably, but its Write/Bash tool-CALLS sometimes don't execute. The scribe lives in the
RELAY — OUTSIDE the model's execution — so it cannot be confabulated. The model emits its
intent as tagged text; the scribe does the real write/run and reports the real result.

Convention the agent emits in its reply text:
    ===FILE:/abs/path===
    <file content>
    ===END===
    ===RUN:<shell command>===

Drop this file next to relay.py, then in relay.py main(), between run_agent() and send():
    from scribe import scribe_process
    try:
        reply, scribe_notes = scribe_process(reply)
        if scribe_notes:
            reply += "\\n\\n--- scribe ---\\n" + scribe_notes
    except Exception as e:
        log(f"scribe error: {e}")   # NEVER crash the forward path

Externality is the law: no self-check inside the model's loop — a confabulating model
confabulates its own stat. Only the relay's hands are trusted.
"""
from __future__ import annotations
import os, re, subprocess, tempfile

# strict parsing: exact markers, absolute path, explicit END — stray pseudo-code can't match
_FILE_RE = re.compile(r"===FILE:(?P<path>/[^\n=]+?)===\n(?P<body>.*?)\n===END===", re.S)
_RUN_RE  = re.compile(r"===RUN:(?P<cmd>[^\n]+?)===")

# reuse the self-body-guard destructive set — the scribe's hands must not do damage
_DESTRUCTIVE = re.compile(
    r"(?:(?<![\w-])(?:rm|rmdir|unlink|shred|wipefs|mkfs|dd|truncate|chattr)(?![\w-])"
    r"|\bfind\b[^|;&]*-delete\b|\bfind\b[^|;&]*-exec\s+rm\b"
    r"|\bgit\s+clean\b|\bmv\b|>\s*/dev/sd|:\(\)\s*\{)",
    re.IGNORECASE,
)
RUN_TIMEOUT = 120


def _materialize_file(path: str, body: str) -> str:
    if not os.path.isabs(path):
        return f"SCRIBE_FAIL: {path} — path not absolute"
    try:
        d = os.path.dirname(path) or "/"
        os.makedirs(d, exist_ok=True)
        # stage IN THE TARGET DIR so os.replace is atomic (same filesystem)
        fd, stage = tempfile.mkstemp(prefix=".scribe_", dir=d)
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(body)
        os.replace(stage, path)  # atomic
        # confirm from disk — the relay's own truth, not the agent's claim
        ok = os.path.exists(path)
        disk = open(path, encoding="utf-8").read() if ok else ""
        if ok and disk == body:
            return f"SCRIBE_OK: {path} ({len(body)} bytes on disk)"
        return f"SCRIBE_FAIL: {path} — post-write mismatch"
    except Exception as e:
        return f"SCRIBE_FAIL: {path} — {e}"


def _run_command(cmd: str) -> str:
    if _DESTRUCTIVE.search(cmd):
        return f"SCRIBE_BLOCK: refused destructive command: {cmd}"
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=RUN_TIMEOUT)
        out = (r.stdout or "").strip()[-700:]
        err = (r.stderr or "").strip()[-300:]
        tail = out + (("\n[stderr] " + err) if err else "")
        return f"SCRIBE_RUN exit={r.returncode}: {cmd}\n{tail}".rstrip()
    except subprocess.TimeoutExpired:
        return f"SCRIBE_RUN_FAIL: {cmd} — timeout after {RUN_TIMEOUT}s"
    except Exception as e:
        return f"SCRIBE_RUN_FAIL: {cmd} — {e}"


def scribe_process(reply: str) -> tuple[str, str]:
    """Return (reply_with_blocks_stripped, scribe_notes). Never raises for content reasons."""
    notes: list[str] = []

    def _file_sub(m: re.Match) -> str:
        notes.append(_materialize_file(m.group("path").strip(), m.group("body")))
        return ""  # strip the raw block from the forwarded text

    def _run_sub(m: re.Match) -> str:
        notes.append(_run_command(m.group("cmd").strip()))
        return ""

    cleaned = _FILE_RE.sub(_file_sub, reply)
    cleaned = _RUN_RE.sub(_run_sub, cleaned)
    return cleaned.strip(), "\n".join(notes)


if __name__ == "__main__":  # self-test: prove the scribe materializes, on real disk
    demo = (
        "Here is the oracle.\n"
        "===FILE:/tmp/scribe_selftest.txt===\n"
        "SIXELEMENT-EXECUTES\n"
        "===END===\n"
        "And a check:\n"
        "===RUN:cat /tmp/scribe_selftest.txt===\n"
        "Also this must be blocked:\n"
        "===RUN:rm -rf /tmp/scribe_selftest.txt===\n"
    )
    body, log_notes = scribe_process(demo)
    print("--- forwarded reply (blocks stripped) ---"); print(repr(body))
    print("--- scribe notes ---"); print(log_notes)
    print("--- disk truth ---")
    p = "/tmp/scribe_selftest.txt"
    print(f"{p} exists={os.path.exists(p)} content={open(p).read().strip()!r}" if os.path.exists(p) else "MISSING")
