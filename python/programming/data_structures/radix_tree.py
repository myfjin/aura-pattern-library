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
            # Key matches the entire child key, continue down this path
            remaining_key = key[common_prefix_len:]
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
                        del node.children[child_key]
                        # Try to merge nodes if this node now has only one child
                        self._merge_single_child(node)
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
                            # Try to merge the child node
                            self._merge_single_child(child_node)
                    return result
        
        return False
    
    def _merge_single_child(self, node: RadixNode) -> None:
        """
        Merge a node with its single child if it has no value.
        
        Args:
            node: Node to potentially merge
        """
        if node.is_leaf or len(node.children) != 1:
            return
        
        # Get the only child
        child_key, child_node = next(iter(node.children.items()))
        
        # Merge the keys and move the child up
        merged_key = node.key + child_key
        child_node.key = merged_key
        
        # Replace this node with the child in the parent's children
        # This is handled at a higher level since we don't have parent references
    
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
    # Demo the radix tree
    tree = RadixTree()
    
    # Insert some key-value pairs
    test_data = [
        ("apple", 1),
        ("app", 2),
        ("application", 3),
        ("apply", 4),
        ("banana", 5),
        ("band", 6),
        ("bandana", 7),
        ("cat", 8),
        ("car", 9),
        ("card", 10)
    ]
    
    print("Inserting key-value pairs:")
    for key, value in test_data:
        tree.insert(key, value)
        print(f"  Inserted: {key} -> {value}")
    
    print("\nAll keys in tree:", tree.keys())
    
    print("\nSearching for keys:")
    search_keys = ["app", "apple", "application", "apply", "banana", "band", "missing"]
    for key in search_keys:
        result = tree.search(key)
        print(f"  Search '{key}': {result}")
    
    print("\nDeleting keys:")
    delete_keys = ["app", "banana", "missing"]
    for key in delete_keys:
        result = tree.delete(key)
        print(f"  Delete '{key}': {result}")
    
    print("\nKeys after deletion:", tree.keys())
    
    print("\nSearching after deletion:")
    for key in ["app", "apple", "banana"]:
        result = tree.search(key)
        print(f"  Search '{key}': {result}")