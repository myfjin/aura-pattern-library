"""reachability_matrix: probe all nodes against all endpoints; build a matrix of reachability.
Failure simulated: 3 nodes with 3 endpoints each; after one endpoint fails, matrix changes.
Recovery asserted: matrix correctly reflects which nodes can reach which endpoints (binary/bool).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import socket
import threading
import time
import sys

def probe_endpoint(node_id, endpoint_host, endpoint_port, timeout_sec=0.3):
    """Try to connect from node_id to endpoint; return True if reachable."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout_sec)
        result = sock.connect_ex((endpoint_host, endpoint_port)) == 0
        sock.close()
        return result
    except Exception:
        return False

def build_reachability_matrix(nodes, endpoints, timeout_sec=0.3):
    """Build a matrix: matrix[node_id] = [reachable_to_endpoint1, reachable_to_endpoint2, ...]"""
    matrix = {}
    for node_id in nodes:
        matrix[node_id] = []
        for endpoint_host, endpoint_port in endpoints:
            reachable = probe_endpoint(node_id, endpoint_host, endpoint_port, timeout_sec)
            matrix[node_id].append(reachable)
    return matrix

if __name__ == "__main__":
    # Set up 3 local server endpoints on 127.0.0.1 with ephemeral ports
    servers = []
    endpoints = []

    for i in range(3):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("127.0.0.1", 0))
        server.listen(1)
        host, port = server.getsockname()
        servers.append(server)
        endpoints.append((host, port))

        # Start acceptor thread
        def accept_conns(s):
            while True:
                try:
                    conn, _ = s.accept()
                    conn.close()
                except OSError:
                    break

        t = threading.Thread(target=accept_conns, args=(server,))
        t.daemon = True
        t.start()

    time.sleep(0.05)

    # Define 3 nodes (they're just labels; probes come from this process on 127.0.0.1)
    nodes = ["node_1", "node_2", "node_3"]

    # Build matrix when all endpoints are UP
    matrix_up = build_reachability_matrix(nodes, endpoints, timeout_sec=0.3)

    # Assert all nodes can reach all endpoints (all True)
    for node_id in nodes:
        for reachable in matrix_up[node_id]:
            assert reachable is True, f"{node_id} should reach all endpoints when all are up"

    all_reachable_up = sum(sum(matrix_up[n]) for n in nodes)
    assert all_reachable_up == 9, f"All 9 connections should be reachable; got {all_reachable_up}"

    # Close the first endpoint (trigger failure)
    servers[0].close()
    time.sleep(0.05)

    # Build matrix when first endpoint is DOWN
    matrix_down = build_reachability_matrix(nodes, endpoints, timeout_sec=0.3)

    # Assert nodes can NOT reach the downed endpoint
    for node_id in nodes:
        assert matrix_down[node_id][0] is False, f"{node_id} should NOT reach endpoint 0 when it's down"

    # Assert nodes can still reach endpoints 1 and 2
    for node_id in nodes:
        assert matrix_down[node_id][1] is True, f"{node_id} should reach endpoint 1"
        assert matrix_down[node_id][2] is True, f"{node_id} should reach endpoint 2"

    all_reachable_down = sum(sum(matrix_down[n]) for n in nodes)
    assert all_reachable_down == 6, f"6 connections should be reachable after one endpoint down; got {all_reachable_down}"

    # Assert matrix changed correctly
    assert all_reachable_up == 9 and all_reachable_down == 6, \
        f"Reachability must change from 9→6 when endpoint fails; got {all_reachable_up}→{all_reachable_down}"

    # Clean up remaining servers
    for server in servers[1:]:
        server.close()

    sys.exit(0)
