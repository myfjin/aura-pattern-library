"""
graceful_shutdown_sigterm: install SIGTERM handler, save state gracefully, and exit.

On receiving SIGTERM the handler writes a state file, then the process exits
 cleanly. The disaster test sends SIGTERM to a child process and asserts that
 the handler ran and the expected state was saved.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import os
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path


CHILD_CODE = """
import signal
import sys

state_file = sys.argv[1]

def handle_sigterm(signum, frame):
    with open(state_file, 'w') as f:
        f.write("graceful_shutdown_complete")
    sys.exit(0)

signal.signal(signal.SIGTERM, handle_sigterm)
import time
while True:
    time.sleep(1)
"""


def install_graceful_shutdown_handler(state_file_path: str) -> str:
    """Return the child process code string with the given state file wired in.

    This is a helper, not the runtime installation. The actual handler is installed
    by the child process spawned by spawn_shutdown_child().

    Args:
        state_file_path: Path where the child will write on SIGTERM.

    Returns:
        Python source code for the child process.

    Guarantees:
        - The returned code installs a SIGTERM handler that writes the state file
          and exits with code 0.
    """
    return CHILD_CODE


def spawn_shutdown_child(state_file: str) -> subprocess.Popen:
    """Spawn a child process that has a SIGTERM handler installed.

    Args:
        state_file: Path the child will write on SIGTERM.

    Returns:
        Running subprocess.Popen instance.
    """
    return subprocess.Popen([sys.executable, "-c", CHILD_CODE, state_file])


def send_sigterm_and_wait(child: subprocess.Popen, settle: float = 0.1,
                          timeout: float = 2.0) -> None:
    """Send SIGTERM to a child and wait for it to exit cleanly.

    Args:
        child: The running child process.
        settle: Seconds to wait after spawning before signalling.
        timeout: Seconds to wait for the child to exit after SIGTERM.

    Raises:
        subprocess.TimeoutExpired: if the child does not exit within `timeout`.

    Guarantees:
        - SIGTERM is delivered to the child.
        - The child is reaped (child.wait() returns).
    """
    time.sleep(settle)
    os.kill(child.pid, signal.SIGTERM)
    child.wait(timeout=timeout)


def assert_state_saved(state_file: str, expected_content: str) -> None:
    """Assert that a state file exists and contains the expected content.

    Args:
        state_file:       Path to the state file produced by the handler.
        expected_content: The exact string expected inside the file.

    Raises:
        AssertionError: if the file is missing or its content differs.

    Failure scenario:
        A process that ignores SIGTERM or fails before saving state leaves the
        state file missing/wrong, which this assertion catches.
    """
    assert os.path.exists(state_file), "state_file was not created; SIGTERM handler did not run"
    with open(state_file, 'r') as f:
        content = f.read()
    assert content == expected_content, \
        f"state content={content!r}, expected {expected_content!r}"


def main() -> None:
    """Self-test: child installs SIGTERM handler, receives SIGTERM, saves state."""
    state_file = tempfile.mktemp(prefix="state_", suffix=".txt")

    child = spawn_shutdown_child(state_file)
    try:
        send_sigterm_and_wait(child)
        assert_state_saved(state_file, "graceful_shutdown_complete")
    finally:
        if os.path.exists(state_file):
            os.remove(state_file)

    print("graceful_shutdown_sigterm PASS")


if __name__ == "__main__":
    main()
