"""
AVL Tree Implementation

A self-balancing binary search tree where the heights of the two child subtrees 
of any node differ by at most one.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Optional, List, Iterator, Tuple
import sys


class AVLNode:
    """Node class for AVL tree."""
    
    def __init__(self, key: int) -> None:
        """
        Initialize an AVL node.
        
        Args:
            key: The value stored in the node
        """
        self.key: int = key
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None
        self.height: int = 1


class AVLTree:
    """AVL Tree implementation with self-balancing properties."""
    
    def __init__(self) -> None:
        """Initialize an empty AVL tree."""
        self.root: Optional[AVLNode] = None
    
    def _get_height(self, node: Optional[AVLNode]) -> int:
        """
        Get the height of a node.
        
        Args:
            node: The node to get height for
            
        Returns:
            Height of the node, 0 if node is None
        """
        if not node:
            return 0
        return node.height
    
    def _get_balance(self, node: Optional[AVLNode]) -> int:
        """
        Get the balance factor of a node.
        
        Args:
            node: The node to get balance for
            
        Returns:
            Balance factor (left height - right height)
        """
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _update_height(self, node: AVLNode) -> None:
        """
        Update the height of a node based on its children.
        
        Args:
            node: The node to update height for
        """
        node.height = 1 + max(self._get_height(node.left), 
                              self._get_height(node.right))
    
    def _rotate_right(self, y: AVLNode) -> AVLNode:
        """
        Perform right rotation on subtree rooted at y.
        
        Args:
            y: Root of subtree to rotate
            
        Returns:
            New root of rotated subtree
        """
        x = y.left
        if not x:
            raise ValueError("Cannot rotate right: left child is None")
            
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        self._update_height(y)
        self._update_height(x)
        
        return x
    
    def _rotate_left(self, x: AVLNode) -> AVLNode:
        """
        Perform left rotation on subtree rooted at x.
        
        Args:
            x: Root of subtree to rotate
            
        Returns:
            New root of rotated subtree
        """
        y = x.right
        if not y:
            raise ValueError("Cannot rotate left: right child is None")
            
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        self._update_height(x)
        self._update_height(y)
        
        return y
    
    def insert(self, key: int) -> None:
        """
        Insert a key into the AVL tree.
        
        Args:
            key: The key to insert
        """
        self.root = self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node: Optional[AVLNode], key: int) -> AVLNode:
        """
        Helper method to recursively insert a key.
        
        Args:
            node: Current node in recursion
            key: Key to insert
            
        Returns:
            Updated node after insertion
        """
        # Step 1: Perform normal BST insertion
        if not node:
            return AVLNode(key)
        
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        else:
            # Duplicate keys not allowed
            return node
        
        # Step 2: Update height of current node
        self._update_height(node)
        
        # Step 3: Get balance factor
        balance = self._get_balance(node)
        
        # Step 4: If unbalanced, there are 4 cases
        
        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)
        
        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)
        
        # Left Right Case
        if balance > 1 and key > node.left.key:
            if node.left:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right Left Case
        if balance < -1 and key < node.right.key:
            if node.right:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        # Return unchanged node
        return node
    
    def delete(self, key: int) -> None:
        """
        Delete a key from the AVL tree.
        
        Args:
            key: The key to delete
        """
        self.root = self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, node: Optional[AVLNode], key: int) -> Optional[AVLNode]:
        """
        Helper method to recursively delete a key.
        
        Args:
            node: Current node in recursion
            key: Key to delete
            
        Returns:
            Updated node after deletion
        """
        # Step 1: Perform standard BST delete
        if not node:
            return node
        
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Node to be deleted found
            if not node.left or not node.right:
                temp = node.left if node.left else node.right
                
                if not temp:
                    # No child case
                    node = None
                else:
                    # One child case
                    node = temp
            else:
                # Node with two children: Get inorder successor
                temp = self._get_min_value_node(node.right)
                
                if temp:
                    node.key = temp.key
                    node.right = self._delete_recursive(node.right, temp.key)
        
        # If the tree had only one node, return
        if not node:
            return node
        
        # Step 2: Update height of current node
        self._update_height(node)
        
        # Step 3: Get balance factor
        balance = self._get_balance(node)
        
        # Step 4: If unbalanced, there are 4 cases
        
        # Left Left Case
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        
        # Left Right Case
        if balance > 1 and self._get_balance(node.left) < 0:
            if node.left:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right Right Case
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        
        # Right Left Case
        if balance < -1 and self._get_balance(node.right) > 0:
            if node.right:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def _get_min_value_node(self, node: AVLNode) -> AVLNode:
        """
        Get the node with minimum key value in a subtree.
        
        Args:
            node: Root of subtree
            
        Returns:
            Node with minimum key value
        """
        current = node
        while current.left:
            current = current.left
        return current
    
    def inorder_traversal(self) -> List[int]:
        """
        Perform inorder traversal of the tree.
        
        Returns:
            List of keys in inorder sequence
        """
        result: List[int] = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: Optional[AVLNode], result: List[int]) -> None:
        """
        Helper method for recursive inorder traversal.
        
        Args:
            node: Current node in traversal
            result: List to store traversal result
        """
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
    
    def search(self, key: int) -> bool:
        """
        Search for a key in the AVL tree.
        
        Args:
            key: Key to search for
            
        Returns:
            True if key exists, False otherwise
        """
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node: Optional[AVLNode], key: int) -> bool:
        """
        Helper method to recursively search for a key.
        
        Args:
            node: Current node in recursion
            key: Key to search for
            
        Returns:
            True if key exists, False otherwise
        """
        if not node:
            return False
        
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
    
    def is_balanced(self) -> bool:
        """
        Check if the tree is balanced.
        
        Returns:
            True if tree is balanced, False otherwise
        """
        return self._is_balanced_recursive(self.root)
    
    def _is_balanced_recursive(self, node: Optional[AVLNode]) -> bool:
        """
        Helper method to recursively check if tree is balanced.
        
        Args:
            node: Current node in recursion
            
        Returns:
            True if subtree is balanced, False otherwise
        """
        if not node:
            return True
        
        balance = self._get_balance(node)
        if abs(balance) > 1:
            return False
        
        return (self._is_balanced_recursive(node.left) and 
                self._is_balanced_recursive(node.right))


def main() -> None:
    """Demo of AVL tree functionality."""
    # Create AVL tree
    avl = AVLTree()
    
    # Insert 50 keys
    keys = list(range(1, 51))
    for key in keys:
        avl.insert(key)
    
    # Verify tree is balanced
    print(f"Tree is balanced: {avl.is_balanced()}")
    
    # Display inorder traversal (should be sorted)
    traversal = avl.inorder_traversal()
    print(f"Inorder traversal (first 20): {traversal[:20]}")
    
    # Search for some keys
    print(f"Search for 25: {avl.search(25)}")
    print(f"Search for 100: {avl.search(100)}")
    
    # Delete some keys
    for key in [10, 20, 30]:
        avl.delete(key)
    
    # Verify still balanced
    print(f"Tree is balanced after deletions: {avl.is_balanced()}")
    
    # Display updated traversal
    traversal = avl.inorder_traversal()
    print(f"Inorder traversal after deletions (first 20): {traversal[:20]}")
    
    # Verify deleted keys are gone
    print(f"Search for 10 after deletion: {avl.search(10)}")


if __name__ == "__main__":
    main()