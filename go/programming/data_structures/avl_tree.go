package main

import (
	"fmt"
	"math"
	"os"
)

// AVLNode is a node class for AVL tree.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type AVLNode struct {
	Key    int
	Left   *AVLNode
	Right  *AVLNode
	Height int
}

// NewAVLNode initializes an AVL node.
func NewAVLNode(key int) *AVLNode {
	return &AVLNode{Key: key, Height: 1}
}

// AVLTree is an AVL tree implementation with self-balancing properties.
type AVLTree struct {
	Root *AVLNode
}

// NewAVLTree initializes an empty AVL tree.
func NewAVLTree() *AVLTree {
	return &AVLTree{}
}

func (t *AVLTree) getHeight(node *AVLNode) int {
	if node == nil {
		return 0
	}
	return node.Height
}

func (t *AVLTree) getBalance(node *AVLNode) int {
	if node == nil {
		return 0
	}
	return t.getHeight(node.Left) - t.getHeight(node.Right)
}

func (t *AVLTree) updateHeight(node *AVLNode) {
	if node == nil {
		return
	}
	node.Height = 1 + int(math.Max(float64(t.getHeight(node.Left)), float64(t.getHeight(node.Right))))
}

func (t *AVLTree) rotateRight(y *AVLNode) *AVLNode {
	x := y.Left
	if x == nil {
		fmt.Fprintf(os.Stderr, "Cannot rotate right: left child is nil\n")
		os.Exit(1)
	}
	T2 := x.Right

	x.Right = y
	y.Left = T2

	t.updateHeight(y)
	t.updateHeight(x)

	return x
}

func (t *AVLTree) rotateLeft(x *AVLNode) *AVLNode {
	y := x.Right
	if y == nil {
		fmt.Fprintf(os.Stderr, "Cannot rotate left: right child is nil\n")
		os.Exit(1)
	}
	T2 := y.Left

	y.Left = x
	x.Right = T2

	t.updateHeight(x)
	t.updateHeight(y)

	return y
}

// Insert inserts a key into the AVL tree.
func (t *AVLTree) Insert(key int) {
	t.Root = t.insertRecursive(t.Root, key)
}

func (t *AVLTree) insertRecursive(node *AVLNode, key int) *AVLNode {
	if node == nil {
		return NewAVLNode(key)
	}

	if key < node.Key {
		node.Left = t.insertRecursive(node.Left, key)
	} else if key > node.Key {
		node.Right = t.insertRecursive(node.Right, key)
	} else {
		return node
	}

	t.updateHeight(node)
	balance := t.getBalance(node)

	// Left Left Case
	if balance > 1 && key < node.Left.Key {
		return t.rotateRight(node)
	}

	// Right Right Case
	if balance < -1 && key > node.Right.Key {
		return t.rotateLeft(node)
	}

	// Left Right Case
	if balance > 1 && key > node.Left.Key {
		node.Left = t.rotateLeft(node.Left)
		return t.rotateRight(node)
	}

	// Right Left Case
	if balance < -1 && key < node.Right.Key {
		node.Right = t.rotateRight(node.Right)
		return t.rotateLeft(node)
	}

	return node
}

// Delete deletes a key from the AVL tree.
func (t *AVLTree) Delete(key int) {
	t.Root = t.deleteRecursive(t.Root, key)
}

func (t *AVLTree) deleteRecursive(node *AVLNode, key int) *AVLNode {
	if node == nil {
		return node
	}

	if key < node.Key {
		node.Left = t.deleteRecursive(node.Left, key)
	} else if key > node.Key {
		node.Right = t.deleteRecursive(node.Right, key)
	} else {
		if node.Left == nil || node.Right == nil {
			var temp *AVLNode
			if node.Left != nil {
				temp = node.Left
			} else {
				temp = node.Right
			}
			if temp == nil {
				node = nil
			} else {
				node = temp
			}
		} else {
			temp := t.getMinValueNode(node.Right)
			node.Key = temp.Key
			node.Right = t.deleteRecursive(node.Right, temp.Key)
		}
	}

	if node == nil {
		return node
	}

	t.updateHeight(node)
	balance := t.getBalance(node)

	// Left Left Case
	if balance > 1 && t.getBalance(node.Left) >= 0 {
		return t.rotateRight(node)
	}

	// Left Right Case
	if balance > 1 && t.getBalance(node.Left) < 0 {
		node.Left = t.rotateLeft(node.Left)
		return t.rotateRight(node)
	}

	// Right Right Case
	if balance < -1 && t.getBalance(node.Right) <= 0 {
		return t.rotateLeft(node)
	}

	// Right Left Case
	if balance < -1 && t.getBalance(node.Right) > 0 {
		node.Right = t.rotateRight(node.Right)
		return t.rotateLeft(node)
	}

	return node
}

func (t *AVLTree) getMinValueNode(node *AVLNode) *AVLNode {
	current := node
	for current.Left != nil {
		current = current.Left
	}
	return current
}

// InorderTraversal performs inorder traversal of the tree.
func (t *AVLTree) InorderTraversal() []int {
	result := []int{}
	t.inorderRecursive(t.Root, &result)
	return result
}

func (t *AVLTree) inorderRecursive(node *AVLNode, result *[]int) {
	if node != nil {
		t.inorderRecursive(node.Left, result)
		*result = append(*result, node.Key)
		t.inorderRecursive(node.Right, result)
	}
}

// Search searches for a key in the AVL tree.
func (t *AVLTree) Search(key int) bool {
	return t.searchRecursive(t.Root, key)
}

func (t *AVLTree) searchRecursive(node *AVLNode, key int) bool {
	if node == nil {
		return false
	}
	if key == node.Key {
		return true
	} else if key < node.Key {
		return t.searchRecursive(node.Left, key)
	}
	return t.searchRecursive(node.Right, key)
}

// IsBalanced checks if the tree is balanced.
func (t *AVLTree) IsBalanced() bool {
	return t.isBalancedRecursive(t.Root)
}

func (t *AVLTree) isBalancedRecursive(node *AVLNode) bool {
	if node == nil {
		return true
	}
	balance := t.getBalance(node)
	if balance < -1 || balance > 1 {
		return false
	}
	return t.isBalancedRecursive(node.Left) && t.isBalancedRecursive(node.Right)
}

func main() {
	avl := NewAVLTree()

	keys := make([]int, 50)
	for i := 0; i < 50; i++ {
		keys[i] = i + 1
	}
	for _, key := range keys {
		avl.Insert(key)
	}

	fmt.Printf("Tree is balanced: %v\n", avl.IsBalanced())

	traversal := avl.InorderTraversal()
	fmt.Printf("Inorder traversal (first 20): %v\n", traversal[:20])

	fmt.Printf("Search for 25: %v\n", avl.Search(25))
	fmt.Printf("Search for 100: %v\n", avl.Search(100))

	for _, key := range []int{10, 20, 30} {
		avl.Delete(key)
	}

	fmt.Printf("Tree is balanced after deletions: %v\n", avl.IsBalanced())

	traversal = avl.InorderTraversal()
	fmt.Printf("Inorder traversal after deletions (first 20): %v\n", traversal[:20])

	fmt.Printf("Search for 10 after deletion: %v\n", avl.Search(10))
}
