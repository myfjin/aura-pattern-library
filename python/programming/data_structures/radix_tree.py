#!/usr/bin/env python3
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Optional, Dict, List, Tuple


class RadixNode:
    """A node in a radix tree (compressed trie)."""
    
    def __init__(self, key: str = "", value: Optional[object] = None):
        """
        Initialize a radix tree node.
        
        Args:
            key: The edge label from parent to this node
            value: The value stored at this node (None if not a leaf)
        """
        self.key: str = key
        self.value: Optional[object] = value
        self.children: Dict[str, 'RadixNode'] = {}
        self.is_leaf: bool = value is not None
    
    def __repr__(self) -> str:
        """String representation of the node."""
        return f"RadixNode(key='{self.key}', value={self.value}, children={list(self.children.keys())})"


class RadixTree:
    """A radix tree (compressed trie) implementation."""
    
    def __init__(self):
        """Initialize an empty radix tree."""
        self.root: RadixNode = RadixNode()
    
    def _longest_common_prefix(self, str1: str, str2: str) -> int:
        """
        Find the length of the longest common prefix between two strings.
        
        Args:
            str1: First string
            str2: Second string
            
        Returns:
            Length of the longest common prefix
        """
        i = 0
        min_len = min(len(str1), len(str2))
        while i < min_len and str1[i] == str2[i]:
            i += 1
        return i
    
    def insert(self, key: str, value: object) -> None:
        """
        Insert a key-value pair into the radix tree.
        
        Args:
            key: The string key to insert
            value: The value to associate with the key
        """
        if not key:
            raise ValueError("Key cannot be empty")
        
        self._insert_recursive(self.root, key, value)
    
    def _insert_recursive(self, node: RadixNode, key: str, value: object) -> None:
        """
        Recursively insert a key-value pair into the tree.
        
        Args:
            node: Current node in traversal
            key: Remaining key to insert
            value: Value to associate with the key
        """
        # Find the child with the longest common prefix
        matching_child = None
        common_prefix_len = 0
        
        for child_key, child_node in node.children.items():
            lcp_len = self._longest_common_prefix(key, child_key)
            if lcp_len > 0 and lcp_len > common_prefix_len:
                common_prefix_len = lcp_len
                matching_child = (child_key, child_node)
        
        if matching_child is None:
            # No matching child, create a new one
            node.children[key] = RadixNode(key, value)
            return
        
        child_key, child_node = matching_child
        
        if common_prefix_len == len(child_key):
            # Key matches the entire child key, continue down this path.
            remaining_key = key[common_prefix_len:]
            if not remaining_key:
                # Exact hit on this node: set/overwrite its value here.
                # (Recursing with "" used to create a phantom ''-edge child,
                # so overwriting an existing key silently kept the old value.)
                child_node.value = value
                child_node.is_leaf = True
                return
            self._insert_recursive(child_node, remaining_key, value)
        else:
            # Need to split the existing node
            # Create a new intermediate node
            common_prefix = child_key[:common_prefix_len]
            remaining_old = child_key[common_prefix_len:]
            remaining_new = key[common_prefix_len:]
            
            # Create new intermediate node
            intermediate = RadixNode(common_prefix)
            
            # Move the existing child down
            child_node.key = remaining_old
            intermediate.children[remaining_old] = child_node
            
            # Add the new node
            if remaining_new:
                new_node = RadixNode(remaining_new, value)
                intermediate.children[remaining_new] = new_node
            else:
                intermediate.value = value
                intermediate.is_leaf = True
            
            # Replace the old child with the intermediate node
            del node.children[child_key]
            node.children[common_prefix] = intermediate
    
    def search(self, key: str) -> Optional[object]:
        """
        Search for a key in the radix tree.
        
        Args:
            key: The key to search for
            
        Returns:
            The value associated with the key, or None if not found
        """
        if not key:
            return self.root.value if self.root.is_leaf else None
        
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node: RadixNode, key: str) -> Optional[object]:
        """
        Recursively search for a key in the tree.
        
        Args:
            node: Current node in traversal
            key: Remaining key to search for
            
        Returns:
            The value associated with the key, or None if not found
        """
        # Find the child with a matching prefix
        for child_key, child_node in node.children.items():
            if key.startswith(child_key):
                if key == child_key and child_node.is_leaf:
                    return child_node.value
                elif key == child_key:
                    return child_node.value if child_node.is_leaf else None
                else:
                    # Continue searching with the remaining key
                    remaining_key = key[len(child_key):]
                    return self._search_recursive(child_node, remaining_key)
        
        return None
    
    def delete(self, key: str) -> bool:
        """
        Delete a key from the radix tree.
        
        Args:
            key: The key to delete
            
        Returns:
            True if the key was deleted, False if it didn't exist
        """
        if not key:
            if self.root.is_leaf:
                self.root.is_leaf = False
                self.root.value = None
                return True
            return False
        
        return self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, node: RadixNode, key: str) -> bool:
        """
        Recursively delete a key from the tree.
        
        Args:
            node: Current node in traversal
            key: Remaining key to delete
            
        Returns:
            True if the key was deleted, False if it didn't exist
        """
        # Find the child with a matching prefix
        for child_key, child_node in node.children.items():
            if key.startswith(child_key):
                if key == child_key:
                    # Found the node to delete
                    if child_node.is_leaf:
                        if child_node.children:
                            # The key is also a prefix of longer keys: unmark
                            # the leaf but KEEP the subtree. (Unconditional
                            # deletion here used to destroy every longer key.)
                            child_node.is_leaf = False
                            child_node.value = None
                            self._merge_single_child(node, child_key)
                        else:
                            del node.children[child_key]
                        return True
                    else:
                        return False  # Not a leaf node
                else:
                    # Continue searching with the remaining key
                    remaining_key = key[len(child_key):]
                    result = self._delete_recursive(child_node, remaining_key)
                    if result:
                        # If child now has no children and is not a leaf, remove it
                        if not child_node.children and not child_node.is_leaf:
                            del node.children[child_key]
                        else:
                            # Try to merge the child node (parent dict in hand)
                            self._merge_single_child(node, child_key)
                    return result

        return False

    def _merge_single_child(self, parent: RadixNode, edge_key: str) -> None:
        """
        Compress parent.children[edge_key] with its single child, keeping the
        parent's children dict and the node's .key in sync. (The former
        version mutated .key without re-keying the dict, desyncing search()
        from keys().)
        """
        node = parent.children[edge_key]
        if node.is_leaf or len(node.children) != 1:
            return

        child_edge, child_node = next(iter(node.children.items()))
        merged_edge = edge_key + child_edge
        child_node.key = merged_edge
        del parent.children[edge_key]
        parent.children[merged_edge] = child_node
    
    def keys(self) -> List[str]:
        """
        Get all keys in the radix tree.
        
        Returns:
            List of all keys in the tree
        """
        return self._collect_keys(self.root, "")
    
    def _collect_keys(self, node: RadixNode, prefix: str) -> List[str]:
        """
        Recursively collect all keys in the tree.
        
        Args:
            node: Current node in traversal
            prefix: Prefix built up to this node
            
        Returns:
            List of all keys under this node
        """
        keys = []
        new_prefix = prefix + node.key
        
        if node.is_leaf:
            keys.append(new_prefix)
        
        for child_node in node.children.values():
            keys.extend(self._collect_keys(child_node, new_prefix))
        
        return keys


if __name__ == "__main__":
    # Self-test: exact lookups through edge-splits, prefix-safe deletes,
    # and a dict oracle fuzz over a shared-prefix-heavy key space.
    import random
    random.seed(42)

    tree = RadixTree()
    test_data = [("apple", 1), ("app", 2), ("application", 3), ("apply", 4),
                 ("banana", 5), ("band", 6), ("bandana", 7),
                 ("cat", 8), ("car", 9), ("card", 10)]
    for key, value in test_data:
        tree.insert(key, value)

    # Every inserted key resolves to exactly its value (through splits).
    for key, value in test_data:
        assert tree.search(key) == value, f"search({key!r}) must be {value}"
    assert tree.search("missing") is None
    assert tree.search("appl") is None, "internal edge fragment reported as a key"
    assert tree.search("ap") is None
    assert sorted(tree.keys()) == sorted(k for k, _ in test_data)
    assert sum(tree.search(k) for k, _ in test_data) == 55, \
        "values 1..10 must sum to 55"

    # Overwrite updates in place.
    tree.insert("app", 20)
    assert tree.search("app") == 20 and len(tree.keys()) == 10

    # Deleting a key that PREFIXES others must not harm the longer keys.
    assert tree.delete("app") is True
    assert tree.search("app") is None
    assert tree.search("apple") == 1 and tree.search("application") == 3, \
        "deleting a prefix key destroyed longer keys"
    assert tree.delete("banana") is True
    assert tree.search("band") == 6 and tree.search("bandana") == 7
    assert tree.delete("missing") is False, "deleting a missing key reported success"
    assert tree.delete("app") is False, "double delete reported success"
    assert len(tree.keys()) == 8

    # Oracle fuzz: 400 ops over a deliberately collision-heavy key space.
    fragments = ["a", "ab", "abc", "abd", "b", "ba", "bad", "badge", "bat", "batch"]
    fuzz = RadixTree()
    oracle = {}
    for step in range(400):
        k = random.choice(fragments) + random.choice(["", "x", "xy", "z"])
        op = random.random()
        if op < 0.5:
            v = random.randint(0, 999)
            fuzz.insert(k, v)
            oracle[k] = v
        elif op < 0.75:
            assert fuzz.delete(k) == (k in oracle), f"delete({k!r}) disagrees at step {step}"
            oracle.pop(k, None)
        else:
            assert fuzz.search(k) == oracle.get(k), f"search({k!r}) disagrees at step {step}"
    assert sorted(fuzz.keys()) == sorted(oracle.keys()), "final key set diverged from oracle"

    print(f"radix_tree: 10 keys exact through splits (sum 55), prefix-delete safe, "
          f"400-op oracle on collision-heavy keys agreed ({len(oracle)} final) — PASS")