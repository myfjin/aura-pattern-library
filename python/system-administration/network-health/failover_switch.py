"""failover_switch: when primary endpoint fails, switch to secondary; assert the switch happens.
Failure simulated: primary server fails; failover_switch should detect and return secondary endpoint.
Recovery asserted: primary is marked failed; secondary is chosen; switch is verifiable.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import socket
import threading
import time
import sys

def is_reachable(host, port, timeout_sec=0.3):
    """Check if host:port is reachable."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout_sec)
        result = sock.connect_ex((host, port)) == 0
        sock.close()
        return result
    except Exception:
        return False

class FailoverSwitch:
    """Manages failover between primary and secondary endpoints."""
    def __init__(self, primary, secondary):
        self.primary = primary
        self.secondary = secondary
        self.current_endpoint = primary
        self.failed_primary = False

    def check_and_switch(self, timeout_sec=0.3):
        """
        Check if current endpoint is reachable.
        If primary is reachable, use it.
        If primary is down and not yet marked failed, switch to secondary.
        Return the active endpoint and whether a failover happened.
        """
        primary_reachable = is_reachable(self.primary[0], self.primary[1], timeout_sec)

        if primary_reachable:
            # Primary is healthy, use it
            self.current_endpoint = self.primary
            self.failed_primary = False
            return self.current_endpoint, False  # No failover

        # Primary is down; switch to secondary
        if not self.failed_primary:
            self.failed_primary = True
            self.current_endpoint = self.secondary
            return self.current_endpoint, True  # Failover happened

        # Already switched, stay on secondary
        return self.current_endpoint, False

if __name__ == "__main__":
    # Set up primary server on 127.0.0.1:ephemeral
    primary_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    primary_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    primary_server.bind(("127.0.0.1", 0))
    primary_server.listen(1)
    primary_host, primary_port = primary_server.getsockname()

    # Set up secondary server on 127.0.0.1:ephemeral
    secondary_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secondary_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    secondary_server.bind(("127.0.0.1", 0))
    secondary_server.listen(1)
    secondary_host, secondary_port = secondary_server.getsockname()

    # Start acceptor threads
    for s in [primary_server, secondary_server]:
        def accept_conns(server):
            while True:
                try:
                    conn, _ = server.accept()
                    conn.close()
                except OSError:
                    break

        t = threading.Thread(target=accept_conns, args=(s,))
        t.daemon = True
        t.start()

    time.sleep(0.05)

    # Initialize failover switch
    switcher = FailoverSwitch(
        primary=(primary_host, primary_port),
        secondary=(secondary_host, secondary_port)
    )

    # Test 1: Primary is up, should use primary
    endpoint, failover_happened = switcher.check_and_switch()
    assert endpoint == (primary_host, primary_port), f"Should use primary when it's up"
    assert failover_happened is False, "No failover should happen when primary is healthy"

    # Close primary server (trigger failure)
    primary_server.close()
    time.sleep(0.05)

    # Test 2: Primary is down, should failover to secondary
    endpoint, failover_happened = switcher.check_and_switch()
    assert endpoint == (secondary_host, secondary_port), f"Should failover to secondary when primary fails"
    assert failover_happened is True, "Failover should be marked as happened"

    # Test 3: Check again; should stay on secondary (no new failover)
    endpoint2, failover_happened2 = switcher.check_and_switch()
    assert endpoint2 == (secondary_host, secondary_port), f"Should stay on secondary"
    assert failover_happened2 is False, "No new failover should happen"

    # Assert state change: primary was primary, after failure secondary is active
    assert switcher.failed_primary is True, "Primary should be marked as failed"
    assert switcher.current_endpoint == (secondary_host, secondary_port), "Current endpoint should be secondary"

    # Clean up
    secondary_server.close()

    sys.exit(0)
