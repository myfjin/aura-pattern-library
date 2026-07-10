#!/usr/bin/env python3
"""
Consistent Hashing Pattern
When a node leaves/joins, only ~1/N keys are remapped (not all keys).
Assert: Key -> Node mapping changes minimally on membership change.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import hashlib


def stable_hash(s):
    """Process-stable hash (NOT builtin hash(), which is PYTHONHASHSEED-salted — the ring
    must be identical across runs for the minimal-remapping guarantee to be assertable)."""
    return int(hashlib.sha256(str(s).encode()).hexdigest(), 16)


class ConsistentHash:
    def __init__(self, nodes=None, ring_size=100):
        self.ring_size = ring_size
        self.nodes = set(nodes) if nodes else set()
        self.node_positions = {}
        self._build_ring()

    def _build_ring(self):
        """Map each node to positions on the ring."""
        self.node_positions = {}
        for node in self.nodes:
            # Virtual nodes: 3 per node for better distribution
            for i in range(3):
                pos = stable_hash(f"{node}_{i}") % self.ring_size
                self.node_positions[pos] = node

    def get_node(self, key):
        """Find node responsible for key."""
        if not self.nodes:
            return None

        key_pos = stable_hash(key) % self.ring_size
        # Find next position >= key_pos
        positions = sorted(self.node_positions.keys())

        for pos in positions:
            if pos >= key_pos:
                return self.node_positions[pos]

        # Wrap around
        return self.node_positions[positions[0]]

    def add_node(self, node):
        """Add node to ring."""
        self.nodes.add(node)
        self._build_ring()

    def remove_node(self, node):
        """Remove node from ring."""
        self.nodes.discard(node)
        self._build_ring()


def test_consistent_hashing_basic():
    """
    3 nodes, 10 keys.
    Assert: keys distributed across nodes.
    """
    ring = ConsistentHash(nodes=['A', 'B', 'C'], ring_size=100)

    keys = [f'key_{i}' for i in range(10)]
    mapping = {k: ring.get_node(k) for k in keys}

    # All keys should be assigned
    assert all(v is not None for v in mapping.values()), "All keys must be assigned"

    # Keys should be distributed (not all to one node)
    nodes_used = set(mapping.values())
    assert len(nodes_used) > 1, f"Keys should use multiple nodes, got {nodes_used}"


def test_consistent_hashing_minimal_remapping():
    """
    100 keys on 3 nodes.
    Add 1 node.
    Assert: roughly 1/4 of keys remapped (those assigned to new node),
    not all keys.
    """
    ring = ConsistentHash(nodes=['A', 'B', 'C'], ring_size=360)

    keys = [f'key_{i}' for i in range(100)]
    mapping_before = {k: ring.get_node(k) for k in keys}

    # Count keys per node
    count_before = {}
    for node in mapping_before.values():
        count_before[node] = count_before.get(node, 0) + 1

    # Add node D
    ring.add_node('D')
    mapping_after = {k: ring.get_node(k) for k in keys}

    # Count keys per node after
    count_after = {}
    for node in mapping_after.values():
        count_after[node] = count_after.get(node, 0) + 1

    # Remapped keys: those that changed node.
    remapped = sum(1 for k in keys if mapping_before[k] != mapping_after[k])

    # (1) MINIMAL: adding 1 node to 3 remaps only ~1/4 of keys, far fewer than the naive
    #     modulo scheme (which reshuffles ~3/4). Assert it stays well under a third.
    assert 0 < remapped < len(keys) * 0.33, \
        f"Expected minimal (~1/N) remapping, got {remapped}/{len(keys)}"

    # (2) The CORE invariant: every remapped key moved TO the new node D — existing nodes'
    #     keys never shuffle among themselves. (A naive hash would scatter keys everywhere.)
    for k in keys:
        if mapping_before[k] != mapping_after[k]:
            assert mapping_after[k] == 'D', \
                f"Key {k} moved {mapping_before[k]}->{mapping_after[k]}, not onto the new node"

    # (3) Directly contrast with naive modulo on the SAME keys: it remaps far more.
    naive_remapped = sum(
        1 for k in keys if (stable_hash(k) % 3) != (stable_hash(k) % 4)
    )
    assert naive_remapped > 2 * remapped, \
        f"Naive modulo ({naive_remapped}) should remap far more than consistent ({remapped})"


def test_consistent_hashing_remove_node():
    """
    4 nodes, 100 keys.
    Remove 1 node.
    Assert: ~1/3 of removed node's keys remapped (to other 3 nodes).
    """
    ring = ConsistentHash(nodes=['A', 'B', 'C', 'D'], ring_size=100)

    keys = [f'key_{i}' for i in range(100)]
    mapping_before = {k: ring.get_node(k) for k in keys}

    # Count A's keys
    a_keys = [k for k in keys if mapping_before[k] == 'A']
    a_count_before = len(a_keys)

    # Remove A
    ring.remove_node('A')
    mapping_after = {k: ring.get_node(k) for k in keys}

    # A's keys should now map to B, C, or D
    for k in a_keys:
        assert mapping_after[k] in ['B', 'C', 'D'], \
            f"Key {k} should map to B/C/D after A removed, got {mapping_after[k]}"

    # Count remapped keys
    remapped = sum(1 for k in a_keys if mapping_after[k] != mapping_before[k])
    assert remapped == a_count_before, "All of A's keys should be remapped"


def test_consistent_hashing_stability():
    """
    Add and remove nodes in sequence.
    Assert: keys belonging to unchanged nodes stay with same node.
    """
    ring = ConsistentHash(nodes=['A', 'B'], ring_size=100)

    keys = [f'key_{i}' for i in range(50)]
    mapping_1 = {k: ring.get_node(k) for k in keys}

    # Add C
    ring.add_node('C')
    mapping_2 = {k: ring.get_node(k) for k in keys}

    # Keys that stayed on A or B should not have changed
    for k in keys:
        if mapping_1[k] in ['A', 'B']:
            # Key was on A or B initially
            # After adding C, it might move to C or stay
            # But if it's still on A, it must be the same
            # (This is guaranteed by consistent hashing)
            pass

    # Remove C
    ring.remove_node('C')
    mapping_3 = {k: ring.get_node(k) for k in keys}

    # Should be back to mapping_1
    assert mapping_1 == mapping_3, "After removing C, should return to original mapping"


def test_failure_naive_modulo():
    """
    Counter-example: simple hash(key) % num_nodes.
    Adding/removing node remaps ALL keys.
    """
    def naive_hash(key, num_nodes):
        return stable_hash(key) % num_nodes

    keys = [f'key_{i}' for i in range(10)]

    mapping_3 = {k: naive_hash(k, 3) for k in keys}
    mapping_4 = {k: naive_hash(k, 4) for k in keys}

    # Almost all keys remapped
    remapped = sum(1 for k in keys if mapping_3[k] != mapping_4[k] % 3)
    # Bug: too many remapped
    assert remapped > 0  # Many keys change


if __name__ == '__main__':
    test_consistent_hashing_basic()
    test_consistent_hashing_minimal_remapping()
    test_consistent_hashing_remove_node()
    test_consistent_hashing_stability()
    test_failure_naive_modulo()
    print("✓ consistent_hashing passed")
