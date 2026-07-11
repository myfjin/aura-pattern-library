# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import Optional, List, Tuple, Iterator
from enum import Enum

class Color(Enum):
    RED = 0
    BLACK = 1

class RBNode:
    """Red-Black Tree Node"""
    
    def __init__(self, key: int, color: Color = Color.RED):
        self.key: int = key
        self.color: Color = color
        self.left: Optional['RBNode'] = None
        self.right: Optional['RBNode'] = None
        self.parent: Optional['RBNode'] = None

    def __repr__(self) -> str:
        return f"RBNode(key={self.key}, color={self.color.name})"

class RBTree:
    """Red-Black Tree implementation with insert, delete, and traversal operations"""
    
    def __init__(self):
        self.NIL: RBNode = RBNode(0, Color.BLACK)
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.NIL.parent = self.NIL
        self.root: RBNode = self.NIL

    def insert(self, key: int) -> None:
        """Insert a key into the Red-Black tree"""
        node = RBNode(key)
        node.left = self.NIL
        node.right = self.NIL
        
        y: Optional[RBNode] = None
        x: RBNode = self.root
        
        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
            
        node.color = Color.RED
        self._insert_fixup(node)

    def _insert_fixup(self, z: RBNode) -> None:
        """Fix Red-Black tree properties after insertion"""
        while z.parent and z.parent.color == Color.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self._left_rotate(z.parent.parent)
        self.root.color = Color.BLACK

    def delete(self, key: int) -> bool:
        """Delete a key from the Red-Black tree. Returns True if key was found and deleted"""
        node = self._search(key)
        if node == self.NIL:
            return False
            
        self._delete_node(node)
        return True

    def _delete_node(self, z: RBNode) -> None:
        """Delete a node from the Red-Black tree"""
        y = z
        y_original_color = y.color
        
        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
                
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
            
        if y_original_color == Color.BLACK:
            self._delete_fixup(x)

    def _delete_fixup(self, x: RBNode) -> None:
        """Fix Red-Black tree properties after deletion"""
        while x != self.root and x.color == Color.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self._left_rotate(x.parent)
                    w = x.parent.right
                    
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.right.color == Color.BLACK:
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self._right_rotate(w)
                        w = x.parent.right
                        
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self._right_rotate(x.parent)
                    w = x.parent.left
                    
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.left.color == Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self._left_rotate(w)
                        w = x.parent.left
                        
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = Color.BLACK

    def _transplant(self, u: RBNode, v: RBNode) -> None:
        """Replace subtree rooted at u with subtree rooted at v"""
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node: RBNode) -> RBNode:
        """Find the node with minimum key in subtree rooted at node"""
        while node.left != self.NIL:
            node = node.left
        return node

    def _search(self, key: int) -> RBNode:
        """Search for a key in the Red-Black tree"""
        current = self.root
        while current != self.NIL and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current

    def _left_rotate(self, x: RBNode) -> None:
        """Perform left rotation on node x"""
        y = x.right
        x.right = y.left
        
        if y.left != self.NIL:
            y.left.parent = x
            
        y.parent = x.parent
        
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
            
        y.left = x
        x.parent = y

    def _right_rotate(self, y: RBNode) -> None:
        """Perform right rotation on node y"""
        x = y.left
        y.left = x.right
        
        if x.right != self.NIL:
            x.right.parent = y
            
        x.parent = y.parent
        
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
            
        x.right = y
        y.parent = x

    def inorder_traversal(self) -> List[int]:
        """Return inorder traversal of the tree"""
        result: List[int] = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node: RBNode, result: List[int]) -> None:
        """Helper method for inorder traversal"""
        if node != self.NIL:
            self._inorder_helper(node.left, result)
            result.append(node.key)
            self._inorder_helper(node.right, result)

    def is_valid_rb_tree(self) -> Tuple[bool, str]:
        """Check if the tree satisfies all Red-Black tree properties"""
        if self.root.color != Color.BLACK:
            return False, "Root is not black"
            
        if not self._is_valid_rb_tree_helper(self.root)[0]:
            return False, "Tree violates Red-Black properties"
            
        return True, "Valid Red-Black tree"

    def _is_valid_rb_tree_helper(self, node: RBNode) -> Tuple[bool, int]:
        """Helper to validate Red-Black tree properties"""
        if node == self.NIL:
            return True, 1  # Black height is 1 for NIL
            
        if node.color == Color.RED:
            if node.left.color == Color.RED or node.right.color == Color.RED:
                return False, 0
                
        left_valid, left_black_height = self._is_valid_rb_tree_helper(node.left)
        if not left_valid:
            return False, 0
            
        right_valid, right_black_height = self._is_valid_rb_tree_helper(node.right)
        if not right_valid:
            return False, 0
            
        if left_black_height != right_black_height:
            return False, 0
            
        black_height = left_black_height
        if node.color == Color.BLACK:
            black_height += 1
            
        return True, black_height

def main() -> None:
    """Self-test: sequential inserts keep ALL Red-Black properties (root black,
    no red-red edge, equal black heights), deletes preserve them, set-oracle fuzz."""
    import random
    random.seed(42)

    # Sequential 1..50 — adversarial for a plain BST.
    rb = RBTree()
    for key in range(1, 51):
        rb.insert(key)
    ok, msg = rb.is_valid_rb_tree()
    assert ok, f"RB properties violated after sequential insert: {msg}"
    traversal = rb.inorder_traversal()
    assert traversal == list(range(1, 51)), "inorder not sorted"
    assert sum(traversal) == 1275, "1..50 must sum to 1275"

    # Deletes must preserve every property.
    for key in (10, 20, 30, 40, 50):
        rb.delete(key)
    ok, msg = rb.is_valid_rb_tree()
    assert ok, f"RB properties violated after delete: {msg}"
    remaining = rb.inorder_traversal()
    assert remaining == [k for k in range(1, 51) if k % 10 != 0], \
        f"wrong survivors after deleting multiples of 10: {remaining[:10]}..."
    assert len(remaining) == 45

    # Deleting a missing key reports failure and leaves the tree intact.
    assert not rb.delete(100), "deleting a missing key reported success"
    assert len(rb.inorder_traversal()) == 45

    # Oracle fuzz: 600 ops vs a set; validity re-proved every 25 ops
    # (fixup bugs typically appear only after specific rotate/recolor chains).
    fuzz = RBTree()
    oracle = set()
    for step in range(600):
        k = random.randint(0, 80)
        if random.random() < 0.6:
            if k not in oracle:
                fuzz.insert(k)
                oracle.add(k)
        elif k in oracle:
            fuzz.delete(k)
            oracle.discard(k)
        if step % 25 == 24:
            ok, msg = fuzz.is_valid_rb_tree()
            assert ok, f"RB invariant broken at step {step}: {msg}"
    assert fuzz.inorder_traversal() == sorted(oracle), "final tree diverged from set oracle"
    ok, msg = fuzz.is_valid_rb_tree()
    assert ok, f"final RB validation failed: {msg}"

    print(f"red_black_tree: 50 sequential inserts valid (sum 1275), deletes "
          f"preserved properties, 600-op fuzz re-validated 24x — PASS")

if __name__ == "__main__":
    main()